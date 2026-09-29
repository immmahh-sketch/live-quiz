/* Let's Quiz! at home — shared by the play-at-home games (millionaire, chase, weakest, club).
 *
 * Every game draws its questions from a numbered set (home/sets/<game>-NN.json). A phone remembers which sets it has
 * played (localStorage lq_home) and always starts the lowest one it has not, so nobody answers the same question twice.
 * With friends, one phone leads: it runs the game, the others join by QR code and send their answers to it, and the
 * set chosen is the first one none of the phones in the room has played.
 */
window.HQ = (() => {
  'use strict';
  const { $, $$, esc, uid, store, shuffle, sleep, clamp } = LQ;

  const GAMES = {
    millionaire: { title: 'Who Wants to Be a Millionaire?', short: 'Millionaire', url: 'millionaire', icon: '💰' },
    chase: { title: 'The Chase', short: 'The Chase', url: 'chase', icon: '🏃' },
    weakest: { title: 'The Weakest Link', short: 'Weakest Link', url: 'weakest', icon: '🔗' },
    club: { title: 'The 1% Club', short: '1% Club', url: 'club', icon: '🧠' },
  };

  // ------------------------------------------------------------------ who am I (shared with the player app)
  function me() {
    const s = store('lq_player') || {};
    const pid = /^p_[a-z0-9]{6,12}$/.test(s.pid || '') ? s.pid : uid('p');
    const emoji = LQ.EMOJIS.includes(s.emoji) ? s.emoji : LQ.EMOJIS[Math.floor(Math.random() * LQ.EMOJIS.length)];
    if (s.pid !== pid || s.emoji !== emoji) store('lq_player', { ...s, pid, emoji });
    return { pid, name: s.name || '', emoji };
  }
  function saveMe(name, emoji) { const s = store('lq_player') || {}; store('lq_player', { ...s, pid: me().pid, name, emoji }); }

  // ------------------------------------------------------------------ sets and progress
  const PKEY = 'lq_home';
  const prog = () => store(PKEY) || {};
  function played(game) { return (prog()[game] || {}).played || []; }
  function markPlayed(game, n) {
    const p = prog(); const g = p[game] || (p[game] = { played: [], at: {} });
    if (!g.played.includes(n)) g.played.push(n);
    g.at = g.at || {}; g.at[n] = Date.now(); store(PKEY, p);
  }
  function best(game, val) { const p = prog(); const g = p[game] || (p[game] = { played: [], at: {} }); if (val !== undefined) { if (!(g.best >= val)) { g.best = val; store(PKEY, p); return true; } return false; } return g.best; }
  let INDEX = null;
  async function index() {
    if (INDEX) return INDEX;
    const r = await fetch('home/sets/index.json', { cache: 'no-cache' });
    if (!r.ok) throw new Error('Could not load the list of games. Check your connection.');
    return (INDEX = await r.json());
  }
  /** The set to play: the lowest one that neither this phone nor any other in the room (`others`: their played
   *  lists) has played. When every set has been played by someone, the one played longest ago here. */
  async function pickSet(game, others = []) {
    const total = ((await index())[game] || {}).sets || 0;
    const lists = [played(game), ...others];
    for (let i = 1; i <= total; i++) if (lists.every((l) => !(l || []).includes(i))) return { n: i, fresh: true, total };
    for (let i = 1; i <= total; i++) if (!played(game).includes(i)) return { n: i, fresh: false, total }; // new to me, not to them
    const at = (prog()[game] || {}).at || {};
    let n = 1; for (let i = 1; i <= total; i++) if ((at[i] || 0) < (at[n] || 0)) n = i;
    return { n, fresh: false, total, replay: true };
  }
  async function loadSet(game, n) {
    const r = await fetch(`home/sets/${game}-${String(n).padStart(2, '0')}.json`, { cache: 'no-cache' });
    if (!r.ok) throw new Error('Could not load that game. Check your connection.');
    return r.json();
  }

  // ------------------------------------------------------------------ typed answers
  const WORDNUM = { zero: 0, one: 1, two: 2, three: 3, four: 4, five: 5, six: 6, seven: 7, eight: 8, nine: 9, ten: 10, eleven: 11, twelve: 12, thirteen: 13, fourteen: 14, fifteen: 15, sixteen: 16, seventeen: 17, eighteen: 18, nineteen: 19, twenty: 20, thirty: 30, forty: 40, fifty: 50, sixty: 60, seventy: 70, eighty: 80, ninety: 90 };
  function norm(s) {
    let t = String(s ?? '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '')
      .replace(/½/g, '.5').replace(/&/g, ' and ').replace(/(\d),(\d{3})/g, '$1$2').replace(/(\d),(\d{3})/g, '$1$2')
      .replace(/(^|[^\w])[-−–](?=\d)/g, '$1minus ').replace(/(\d)\.(\d)/g, '$1DOT$2')
      .replace(/[^a-z0-9]+/g, ' ').replace(/DOT/gi, '.').trim();
    // "twenty one" → 21; a lone number word → digits
    t = t.replace(/\b(twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety)[ ](one|two|three|four|five|six|seven|eight|nine)\b/g, (_, a, b) => String(WORDNUM[a] + WORDNUM[b]));
    t = t.replace(/\b(zero|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety)\b/g, (w) => String(WORDNUM[w]));
    return t.replace(/^(the|a|an) /, '').replace(/ (pence|p|pounds|degrees|years|metres|meters|miles|minutes|seconds|hours|days)$/, '').trim();
  }
  const numVal = (s) => { const m = String(s).replace(/^minus /, '-').match(/^-?\d+(\.\d+)?$/); return m ? parseFloat(m[0]) : null; };
  /** Is a typed answer right? Forgives case, accents, punctuation, "the", number words, small typos and a
   *  plural; takes a longer answer that has the whole right answer in it. */
  function isRight(typed, answers) {
    const n = norm(typed); if (!n) return false;
    const words = new Set(n.split(' '));
    for (const acc of answers || []) {
      // "~horse": right if every one of these words is in the answer (for riddles answered in a phrase)
      if (String(acc).startsWith('~')) { const need = norm(String(acc).slice(1)).split(' ').filter(Boolean); if (need.length && need.every((w) => words.has(w))) return true; continue; }
      const m = norm(acc); if (!m) continue;
      if (n === m) return true;
      const a = numVal(n), b = numVal(m);
      if (a !== null || b !== null) { if (a !== null && b !== null && a === b) return true; if (b !== null) continue; }
      if (m.length >= 4 && (n === m + 's' || n + 's' === m || n === m.replace(/s$/, '') || n.replace(/s$/, '') === m)) return true;
      if (m.length >= 4 && LQ.similarity(n, m) >= (m.length >= 8 ? 0.8 : 0.85)) return true;
      if (m.length >= 4 && (' ' + n + ' ').includes(' ' + m + ' ') && n.split(' ').length <= m.split(' ').length + 2) return true;
    }
    return false;
  }

  // ------------------------------------------------------------------ sound (made in the browser, no music files)
  let actx = null, muted = !!store('lq_home_mute');
  function ac() { if (!actx) { try { actx = new (window.AudioContext || window.webkitAudioContext)(); } catch { return null; } } if (actx.state === 'suspended') actx.resume(); return actx; }
  function tone(freq, dur, { type = 'sine', vol = 0.15, at = 0, slide = 0, attack = 0.01 } = {}) {
    if (muted) return; const c = ac(); if (!c) return;
    const t = c.currentTime + at, o = c.createOscillator(), g = c.createGain();
    o.type = type; o.frequency.setValueAtTime(freq, t); if (slide) o.frequency.exponentialRampToValueAtTime(Math.max(20, freq + slide), t + dur);
    g.gain.setValueAtTime(0, t); g.gain.linearRampToValueAtTime(vol, t + attack); g.gain.exponentialRampToValueAtTime(0.0001, t + dur);
    o.connect(g).connect(c.destination); o.start(t); o.stop(t + dur + 0.05);
  }
  function noise(dur, { vol = 0.08, at = 0, hp = 800 } = {}) {
    if (muted) return; const c = ac(); if (!c) return;
    const b = c.createBuffer(1, Math.ceil(c.sampleRate * dur), c.sampleRate), d = b.getChannelData(0);
    for (let i = 0; i < d.length; i++) d[i] = (Math.random() * 2 - 1) * (1 - i / d.length);
    const s = c.createBufferSource(), f = c.createBiquadFilter(), g = c.createGain(); f.type = 'highpass'; f.frequency.value = hp; g.gain.value = vol;
    s.buffer = b; s.connect(f).connect(g).connect(c.destination); s.start(c.currentTime + at);
  }
  const SOUNDS = {
    tap: () => tone(660, 0.06, { type: 'triangle', vol: 0.08 }),
    tick: () => tone(1200, 0.03, { type: 'square', vol: 0.04 }),
    tock: () => tone(900, 0.03, { type: 'square', vol: 0.04 }),
    right: () => { tone(660, 0.12, { type: 'triangle' }); tone(990, 0.22, { type: 'triangle', at: 0.1 }); },
    wrong: () => { tone(180, 0.35, { type: 'sawtooth', vol: 0.1 }); tone(140, 0.4, { type: 'sawtooth', vol: 0.08, at: 0.05 }); },
    lock: () => { tone(110, 0.5, { type: 'sine', vol: 0.3, slide: -40 }); noise(0.25, { vol: 0.05, hp: 200 }); },
    reveal: () => { [523, 659, 784, 1047].forEach((f, i) => tone(f, 0.25, { type: 'triangle', vol: 0.1, at: i * 0.06 })); },
    win: () => { [523, 659, 784, 1047, 1319].forEach((f, i) => tone(f, 0.5, { type: 'triangle', vol: 0.12, at: i * 0.12 })); },
    lose: () => { [392, 330, 262, 196].forEach((f, i) => tone(f, 0.45, { type: 'sine', vol: 0.12, at: i * 0.18 })); },
    step: () => { tone(90, 0.18, { vol: 0.35, slide: -30 }); },
    chaser: () => { tone(70, 0.3, { type: 'sawtooth', vol: 0.12, slide: -20 }); tone(55, 0.35, { vol: 0.3, at: 0.02 }); },
    caught: () => { [220, 233, 247].forEach((f) => tone(f, 1.2, { type: 'sawtooth', vol: 0.06 })); tone(55, 1.4, { vol: 0.35 }); },
    home: () => { [392, 523, 659, 784].forEach((f, i) => tone(f, 0.4, { type: 'triangle', vol: 0.12, at: i * 0.1 })); },
    bank: () => { tone(1568, 0.08, { type: 'square', vol: 0.05 }); tone(2093, 0.3, { type: 'triangle', vol: 0.1, at: 0.07 }); },
    whoosh: () => noise(0.5, { vol: 0.08, hp: 1500 }),
    elim: () => { tone(400, 0.8, { type: 'sawtooth', vol: 0.06, slide: -320 }); noise(0.6, { vol: 0.05, hp: 600 }); },
    ring: () => { for (let i = 0; i < 2; i++) { tone(440, 0.4, { vol: 0.07, at: i * 0.5 }); tone(480, 0.4, { vol: 0.07, at: i * 0.5 }); } },
    heart: () => { tone(60, 0.12, { vol: 0.4 }); tone(55, 0.14, { vol: 0.3, at: 0.18 }); },
    buzz: () => tone(120, 0.6, { type: 'square', vol: 0.08 }),
  };
  function sound(name) { try { SOUNDS[name]?.(); } catch {} }
  function setMuted(v) { muted = !!v; store('lq_home_mute', muted); }
  const isMuted = () => muted;
  let beatT = null;
  function heartbeat(on) { clearInterval(beatT); beatT = null; if (on) { sound('heart'); beatT = setInterval(() => sound('heart'), 900); } }
  function buzzPhone(ms) { try { navigator.vibrate?.(ms); } catch {} }

  // ------------------------------------------------------------------ keep the screen on while playing
  let lock = null;
  async function wake(on = true) {
    try {
      if (!on) { await lock?.release(); lock = null; return; }
      if (!('wakeLock' in navigator) || lock) return;
      lock = await navigator.wakeLock.request('screen'); lock.addEventListener('release', () => { lock = null; });
    } catch {}
  }
  document.addEventListener('visibilitychange', () => { if (document.visibilityState === 'visible' && wantWake) wake(true); });
  let wantWake = false;
  function keepAwake(on) { wantWake = on; wake(on); }

  // ------------------------------------------------------------------ bots
  const BOT_NAMES = ['Dave', 'Priya', 'Big Keith', 'Auntie Pat', 'Gaz', 'Shaz', 'Terry', 'Chantelle', 'Rob', 'Niamh', 'Mo', 'Bev', 'Craig', 'Siobhan', 'Raj', 'Linda', 'Kev', 'Fiona', 'Dom', 'Jade', 'Barry', 'Tasha', 'Ian', 'Leanne', 'Wes', 'Carol', 'Ade', 'Gemma', 'Stu', 'Nadia', 'Phil', 'Aisha', 'Mick', 'Becky', 'Tom', 'Sandra', 'Kai', 'Hayley', 'Des', 'Lorraine', 'Callum', 'Yvonne', 'Ravi', 'Stacey', 'Nige', 'Claire', 'Ollie', 'Denise', 'Jas', 'Paula', 'Ken', 'Mel', 'Ahmed', 'Tracey', 'Neil', 'Rosie', 'Pete', 'Zara', 'Glen', 'Dawn', 'Lee', 'Julie', 'Sanjay', 'Kerry', 'Frank', 'Amy', 'Gordon', 'Ruth', 'Jamal', 'Nicola', 'Alf', 'Sue', 'Harvey', 'Megan', 'Clive', 'Lisa', 'Tariq', 'Jo', 'Roy', 'Kim', 'Declan', 'Emma', 'Wayne', 'Holly', 'Sid', 'Anita', 'Jack', 'Val', 'Owen', 'Katie', 'Norm', 'Freya', 'Imran', 'Jean', 'Sean', 'Lucy', 'Vic', 'Poppy', 'Graham', 'Maxine'];
  const BOT_EMOJI = ['🧔', '👩🏽', '🧑‍🦲', '👵', '🧢', '💅', '👴', '💁‍♀️', '🧑', '👩‍🦰', '🧕', '👩‍🦳', '🧑🏻', '👱‍♀️', '👨🏾', '👩', '🧔🏻', '👩🏼', '🧑🏽', '👩🏾', '🎩', '👓', '🦸', '🧑‍🎤', '🧑‍🍳', '🧑‍🔧', '🧑‍🏫', '🧑‍🚀', '🧑‍🌾', '🧑‍🎨'];
  function bots(n, avoid = []) {
    const taken = new Set(avoid.map((x) => String(x).toLowerCase()));
    const names = shuffle(BOT_NAMES).filter((x) => !taken.has(x.toLowerCase()));
    const out = [];
    for (let i = 0; i < n; i++) out.push({ id: 'b_' + i + '_' + Math.random().toString(36).slice(2, 6), name: names[i % names.length] + (i >= names.length ? ' ' + (Math.floor(i / names.length) + 1) : ''), emoji: BOT_EMOJI[Math.floor(Math.random() * BOT_EMOJI.length)], bot: true });
    return out;
  }
  const chance = (p) => Math.random() < p;
  const rand = (a, b) => a + Math.random() * (b - a);
  const pick = (arr) => arr[Math.floor(Math.random() * arr.length)];

  // ------------------------------------------------------------------ playing with friends: one phone leads
  /** The lead phone: runs the game and tells the others. `onAct(pid, kind, data)` gets their moves;
   *  `onJoin(player)` a phone saying hello. */
  function lead(code, { onAct, onJoin, onPresence, who } = {}) {
    const sb = LQ.client(), mePid = (who || me()).pid;
    const ch = sb.channel('home-' + code, { config: { broadcast: { self: false }, presence: { key: mePid } } });
    ch.on('broadcast', { event: 'act' }, ({ payload: p }) => { if (!p || !p.pid) return; if (p.kind === 'hello') onJoin?.(p); else onAct?.(p.pid, p.kind, p.data || {}); });
    ch.on('presence', { event: 'sync' }, () => onPresence?.(Object.keys(ch.presenceState())));
    let ready = false; const queued = [];
    ch.subscribe(async (s) => { if (s === 'SUBSCRIBED') { ready = true; await ch.track({ lead: true }); while (queued.length) ch.send(queued.shift()); } });
    return {
      code,
      state(view) { const msg = { type: 'broadcast', event: 'state', payload: view }; if (ready) ch.send(msg); else { queued.length = 0; queued.push(msg); } },
      leave() { try { sb.removeChannel(ch); } catch {} },
    };
  }
  /** A phone joining someone else's game: sends hello until the lead phone lists it, then its moves. */
  function join(code, hello, { onState, onLost, who } = {}) {
    const sb = LQ.client(), p = who || me();
    const ch = sb.channel('home-' + code, { config: { broadcast: { self: false }, presence: { key: p.pid } } });
    let last = 0, known = false, helloT = null, lostT = null;
    ch.on('broadcast', { event: 'state' }, ({ payload }) => { last = Date.now(); if (payload?.players?.some?.((x) => x.id === p.pid)) known = true; onState?.(payload); });
    const sayHello = () => { if (!known) ch.send({ type: 'broadcast', event: 'act', payload: { pid: p.pid, kind: 'hello', ...hello() } }); };
    ch.subscribe(async (s) => { if (s === 'SUBSCRIBED') { await ch.track({ lead: false }); sayHello(); clearInterval(helloT); helloT = setInterval(sayHello, 2000); } });
    lostT = setInterval(() => onLost?.(last && Date.now() - last > 7000), 2000);
    return {
      act(kind, data = {}) { ch.send({ type: 'broadcast', event: 'act', payload: { pid: p.pid, kind, data } }); },
      rehello() { known = false; sayHello(); },
      leave() { clearInterval(helloT); clearInterval(lostT); try { sb.removeChannel(ch); } catch {} },
    };
  }
  const joinUrl = (game, code) => { const u = new URL(GAMES[game].url, location.href); u.search = '?j=' + code; return u.toString(); };
  function qr(el, text, size = 220) { el.innerHTML = ''; try { new QRCode(el, { text, width: size, height: size, correctLevel: QRCode.CorrectLevel.M }); } catch { el.textContent = text; } }

  // ------------------------------------------------------------------ bits of screen
  let toastT;
  function toast(msg, bad) { let t = $('#hqToast'); if (!t) { t = document.createElement('div'); t.id = 'hqToast'; t.className = 'hq-toast'; document.body.appendChild(t); } t.textContent = msg; t.className = 'hq-toast show' + (bad ? ' bad' : ''); clearTimeout(toastT); toastT = setTimeout(() => t.classList.remove('show'), 2600); }
  const money = (n) => (n < 0 ? '−£' : '£') + Math.abs(Math.round(n)).toLocaleString('en-GB');
  /** A typed-answer bar that keeps its place (and the keyboard) across screen updates. */
  function answerBar(host, { placeholder = 'Type your answer', go = 'Go', onSubmit, onPass, passLabel = 'Pass' }) {
    host.innerHTML = `<form class="hq-answer" autocomplete="off"><input type="text" enterkeyhint="send" autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false" placeholder="${esc(placeholder)}" maxlength="60"><button class="hq-go" type="submit">${esc(go)}</button>${onPass ? `<button class="hq-pass" type="button">${esc(passLabel)}</button>` : ''}</form>`;
    const f = host.querySelector('form'), inp = f.querySelector('input');
    f.onsubmit = (e) => { e.preventDefault(); const v = inp.value.trim(); if (!v) return; inp.value = ''; onSubmit(v); inp.focus(); };
    if (onPass) f.querySelector('.hq-pass').onclick = () => { inp.value = ''; onPass(); inp.focus(); };
    return { input: inp, focus: () => { try { inp.focus({ preventScroll: true }); } catch {} }, disable(v) { inp.disabled = v; f.querySelectorAll('button').forEach((b) => b.disabled = v); } };
  }
  function confetti(n = 120) {
    const box = document.createElement('div'); box.className = 'hq-confetti'; document.body.appendChild(box);
    const cols = ['#ffd60a', '#5b3df5', '#26c281', '#ff4d6d', '#35a7ff', '#fff'];
    for (let i = 0; i < n; i++) { const s = document.createElement('i'); s.style.left = Math.random() * 100 + '%'; s.style.background = pick(cols); s.style.animationDelay = Math.random() * 0.8 + 's'; s.style.animationDuration = 2 + Math.random() * 2 + 's'; s.style.transform = `rotate(${Math.random() * 360}deg)`; box.appendChild(s); }
    setTimeout(() => box.remove(), 5000);
  }
  async function share(text) {
    try { if (navigator.share) { await navigator.share({ text, url: location.origin + location.pathname }); return; } } catch { return; }
    try { await navigator.clipboard.writeText(text + ' ' + location.origin + location.pathname); toast('Copied, ready to paste'); } catch { toast('Could not share from this browser', true); }
  }
  /** The name-and-emoji form a joining phone fills in once. */
  function nameForm(host, { title, sub, button = 'Join', onDone }) {
    const p = me(); let emo = p.emoji;
    host.innerHTML = `<div class="hq-card hq-join"><h2>${esc(title)}</h2>${sub ? `<p class="hq-muted">${esc(sub)}</p>` : ''}
      <form id="hqName"><label class="hq-label">Your name</label><input type="text" id="hqNm" maxlength="16" value="${esc(p.name)}" placeholder="What should we call you?" autocomplete="nickname">
      <label class="hq-label">Your emoji</label><div class="hq-emos">${LQ.EMOJIS.map((e) => `<button type="button" data-e="${e}" class="${e === emo ? 'on' : ''}">${e}</button>`).join('')}</div>
      <button class="hq-btn hq-btn-main" type="submit">${esc(button)}</button></form></div>`;
    host.querySelectorAll('[data-e]').forEach((b) => b.onclick = () => { emo = b.dataset.e; host.querySelectorAll('[data-e]').forEach((x) => x.classList.toggle('on', x === b)); });
    host.querySelector('#hqName').onsubmit = (e) => { e.preventDefault(); const n = host.querySelector('#hqNm').value.replace(/\s+/g, ' ').trim(); if (!n) return toast('Pop your name in first', true); saveMe(n, emo); onDone({ ...me(), name: n, emoji: emo }); };
  }
  /** Top bar: back to the games list, the game's name, sound on/off. */
  function topBar(host, title, { onBack } = {}) {
    host.innerHTML = `<a class="hq-back" href="home" aria-label="All games">‹</a><div class="hq-title">${esc(title)}</div><button class="hq-mute" aria-label="Sound">${muted ? '🔇' : '🔊'}</button>`;
    host.querySelector('.hq-mute').onclick = (e) => { setMuted(!muted); e.currentTarget.textContent = muted ? '🔇' : '🔊'; if (!muted) sound('tap'); };
    if (onBack) host.querySelector('.hq-back').onclick = (e) => { if (onBack() === false) e.preventDefault(); };
  }
  // the first tap anywhere wakes the audio (browsers insist)
  document.addEventListener('pointerdown', () => ac(), { once: true });

  // ------------------------------------------------------------------ the keyboard
  // An iPhone's keyboard slides up over the page without making it shorter, so a bar pinned to the bottom (the
  // answer box, Pass) ends up behind it. While the keyboard is up, the dock sits just above it instead: the gap
  // between the bottom of the page and the bottom of what can still be seen (the visual viewport).
  if (window.visualViewport) {
    const vv = window.visualViewport, root = document.documentElement;
    const fitKeyboard = () => {
      const kb = Math.max(0, Math.round(root.clientHeight - (vv.height + vv.offsetTop)));
      const up = kb > 80; // a real keyboard, not the browser's toolbar shuffling
      document.body.classList.toggle('hq-kb', up);
      root.style.setProperty('--hq-kb', (up ? kb : 0) + 'px');
      const dock = document.querySelector('.hq-dock'); if (dock) root.style.setProperty('--hq-dockh', dock.offsetHeight + 'px');
    };
    vv.addEventListener('resize', fitKeyboard); vv.addEventListener('scroll', fitKeyboard);
    document.addEventListener('focusin', () => setTimeout(fitKeyboard, 300));
    document.addEventListener('focusout', () => setTimeout(fitKeyboard, 300));
  }

  // ------------------------------------------------------------------ clocks
  // Any element with data-dl (a performance.now() deadline) and data-total (ms) counts down by itself: its text shows
  // the seconds left (data-fmt="mmss" for 1:59), and a .hq-clockbar's bar shrinks. data-tick="5" ticks the last 5 seconds.
  let lastTickSec = -1;
  function clockLoop() {
    const now = performance.now();
    for (const el of document.querySelectorAll('[data-dl]')) {
      const left = Math.max(0, +el.dataset.dl - now), total = +el.dataset.total || 1, s = Math.ceil(left / 1000);
      if (el.classList.contains('hq-clockbar')) { const i = el.firstElementChild; if (i) i.style.transform = `scaleX(${left / total})`; el.classList.toggle('low', left < 5000); }
      else el.textContent = el.dataset.fmt === 'mmss' ? `${Math.floor(s / 60)}:${String(s % 60).padStart(2, '0')}` : String(s);
      if (el.dataset.tick && s <= +el.dataset.tick && s > 0 && s !== lastTickSec && left > 0) { lastTickSec = s; sound('tick'); }
    }
    requestAnimationFrame(clockLoop);
  }
  requestAnimationFrame(clockLoop);
  /** A clock element counting down `ms` from when view V arrived. */
  const clock = (V, ms, total, extra = '') => `data-dl="${(V.recv || performance.now()) + (ms || 0)}" data-total="${total || ms || 1}" ${extra}`;

  // ------------------------------------------------------------------ a game on one phone or several
  /**
   * Runs a game for the play-at-home pages that can be played with friends. One phone leads: it runs `engine` and
   * sends every other phone the view it makes; the others send their moves back. On your own, it's the same game
   * with no one else in the room.
   *
   * cfg: { game, main, dock, intro(pick) → html, defaults: {options}, maxPlayers, minPlayers (with friends),
   *        lobbyHtml(opts, players, isLead) → html, lobbyBind(root, opts, redo), soloOk(opts) → true,
   *        engine: { create({ players, opts, set, now }) → S, act(S, pid, kind, data, now), tick(S, now) → changed?, view(S, now) → V },
   *        render(V, ctx) where ctx = { me, lead, act(kind, data) } }
   */
  function session(cfg) {
    const { game, main, dock, engine } = cfg;
    const SAVE_KEY = 'lq_home_live_' + game;
    const params = new URLSearchParams(location.search);
    const joinCode = (params.get('j') || '').toUpperCase().replace(/[^A-Z0-9]/g, '');
    let S = null, room = null, follow = null, lobby = null, lastV = null, marked = 0, tickT = null, beatT = null, saveT = 0;
    // who this phone is, fixed for the whole game (refreshed when the name form is filled in)
    let ME = me(); const my = () => ME;

    const ctx = { get me() { return my().pid; }, get lead() { return !follow; }, act };
    function act(kind, data = {}) {
      if (follow) return follow.act(kind, data);
      if (!S) return;
      engine.act(S, my().pid, kind, data, Date.now()); publish();
    }
    function show(V) {
      V.recv = performance.now(); lastV = V;
      if (V.phase !== 'lobby' && V.set && marked !== V.set) { marked = V.set; markPlayed(game, V.set); keepAwake(true); }
      if (V.phase === 'over') keepAwake(false);
      cfg.render(V, ctx);
    }
    function publish() {
      const V = engine.view(S, Date.now()); V.set = S.set; V.game = game;
      if (room) room.state(V);
      show(JSON.parse(JSON.stringify(V)));
      if (Date.now() - saveT > 1500 || V.phase === 'over') { saveT = Date.now(); store(SAVE_KEY, V.phase === 'over' ? null : { S, code: room?.code || null, at: Date.now() }); }
    }
    function run() {
      clearInterval(tickT); clearInterval(beatT);
      tickT = setInterval(() => { if (S && engine.tick(S, Date.now())) publish(); }, 120);
      beatT = setInterval(() => { if (S && room) { const V = engine.view(S, Date.now()); V.set = S.set; V.game = game; room.state(V); } }, 2500);
    }

    // ---- the lead phone's lobby
    function publishLobby() {
      const V = { phase: 'lobby', code: lobby.code, opts: lobby.opts, players: lobby.players.map(({ played, ...p }) => p), host: my().name };
      room.state(V); renderLobby(V, true);
    }
    function renderLobby(V, isLead) {
      const url = joinUrl(game, V.code);
      main.innerHTML = `<div class="hq-card" style="text-align:center">
          ${isLead ? `<div class="hq-muted hq-small">Friends scan this with their phone camera to join</div><div class="hq-qr" id="hqQr" style="margin-top:10px"></div><div class="hq-code">${esc(V.code)}</div><div class="hq-muted hq-small">or go to ${esc(url.replace(/^https?:\/\//, '').replace(/\?.*$/, ''))} and type the code</div>`
          : `<div style="font-size:2.2rem">⏳</div><b>You're in!</b><div class="hq-muted">Waiting for ${esc(V.host || 'the host')} to start the game…</div>`}
        </div>
        <div class="hq-card"><b>Players (${V.players.length})</b><div class="hq-people" style="margin-top:10px">${V.players.map((p) => `<span class="hq-person">${esc(p.emoji)} ${esc(p.name)}${isLead && p.id !== my().pid ? ` <button class="x" data-kick="${esc(p.id)}" aria-label="Remove">✕</button>` : ''}</span>`).join('')}</div></div>
        <div id="hqLobbyOpts">${cfg.lobbyHtml ? cfg.lobbyHtml(V.opts, V.players, isLead) : ''}</div>`;
      if (isLead) {
        qr($('#hqQr'), url, 190);
        $$('[data-kick]', main).forEach((b) => b.onclick = () => { lobby.players = lobby.players.filter((p) => p.id !== b.dataset.kick); publishLobby(); });
        if (cfg.lobbyBind) cfg.lobbyBind($('#hqLobbyOpts'), lobby.opts, () => publishLobby(), lobby.players);
        const min = cfg.minPlayers || 1, max = cfg.maxPlayers || 100;
        const why = cfg.lobbyCheck ? cfg.lobbyCheck(lobby.opts, lobby.players) : '';
        dock.innerHTML = `${why ? `<div class="hq-banner" style="margin-bottom:8px">${esc(why)}</div>` : ''}<button class="hq-btn hq-btn-main" id="hqStart" ${lobby.players.length < min || lobby.players.length > max || why ? 'disabled' : ''}>Start the game</button>`;
        $('#hqStart').onclick = () => begin(lobby.players, lobby.opts);
      } else dock.innerHTML = '';
    }
    async function begin(players, opts) {
      $('#hqStart') && ($('#hqStart').disabled = true);
      let pick;
      try { pick = await pickSet(game, players.filter((p) => p.id !== my().pid).map((p) => p.played || [])); } catch (e) { toast(e.message, true); return; }
      let set; try { set = await loadSet(game, pick.n); } catch (e) { toast(e.message, true); return; }
      if (pick.replay) toast("You've all played every game: this one is a replay");
      S = engine.create({ players: players.map(({ played, ...p }) => p), opts, set, now: Date.now() });
      S.set = pick.n; sound('reveal'); run(); publish();
    }

    // ---- start: follow someone else's game, or offer to play
    if (joinCode) {
      nameForm(main, { title: "Join the game", sub: 'Code ' + joinCode, button: 'Join', onDone() {
        ME = me();
        main.innerHTML = `<div class="hq-card" style="text-align:center">Connecting…</div>`; dock.innerHTML = '';
        let lostBox = null;
        follow = join(joinCode, () => ({ name: my().name, emoji: my().emoji, played: played(game) }), { who: my(),
          onState(V) { if (V.phase === 'lobby') renderLobby({ ...V, recv: performance.now() }, false); else show(V); },
          onLost(lost) { if (lost && !lostBox) { lostBox = document.createElement('div'); lostBox.className = 'hq-lost'; lostBox.textContent = "Lost touch with the host's phone. Waiting for it…"; document.body.appendChild(lostBox); } else if (!lost && lostBox) { lostBox.remove(); lostBox = null; } },
        });
      } });
      return;
    }
    (async () => {
      let pick; try { pick = await pickSet(game); } catch (e) { main.innerHTML = `<div class="hq-card">${esc(e.message)}</div>`; return; }
      const saved = store(SAVE_KEY);
      const resumable = saved && saved.S && Date.now() - saved.at < 3 * 3600000;
      main.innerHTML = cfg.intro(pick);
      dock.innerHTML = `<div style="display:grid;gap:10px">${resumable ? `<button class="hq-btn hq-btn-main" id="hqResume">Carry on with your game</button>` : ''}
        <button class="hq-btn ${resumable ? 'hq-btn-ghost' : 'hq-btn-main'}" id="hqSolo">${esc(cfg.soloLabel || 'Play on my own')}</button>
        <button class="hq-btn hq-btn-ghost" id="hqFriends">${esc(cfg.friendsLabel || 'Play with friends')}</button>
        <form id="hqJoin" class="hq-answer" style="margin-top:2px"><input type="text" maxlength="6" placeholder="Got a code? Join a friend's game" autocapitalize="characters" autocomplete="off" style="text-transform:uppercase;font-size:1rem"><button class="hq-go" type="submit">Join</button></form></div>`;
      $('#hqJoin').onsubmit = (e) => { e.preventDefault(); const c = e.target.querySelector('input').value.toUpperCase().replace(/[^A-Z0-9]/g, ''); if (c.length !== 6) return toast('The code is six letters and numbers', true); location.href = GAMES[game].url + '?j=' + c; };
      if (resumable) $('#hqResume').onclick = () => {
        S = saved.S;
        if (saved.code) room = lead(saved.code, { onAct: (pid, kind, data) => { engine.act(S, pid, kind, data, Date.now()); publish(); }, onJoin: () => publish() });
        run(); publish();
      };
      $('#hqSolo').onclick = () => { store(SAVE_KEY, null); begin([{ id: my().pid, name: my().name || 'You', emoji: my().emoji }], { ...(cfg.defaults || {}), solo: true }); };
      $('#hqFriends').onclick = () => {
        store(SAVE_KEY, null);
        nameForm(main, { title: 'Your name', sub: 'So your friends know whose game it is', button: 'Open the game', onDone() {
          ME = me();
          const code = LQ.newCode();
          lobby = { code, opts: { ...(cfg.defaults || {}), solo: false }, players: [{ id: my().pid, name: my().name, emoji: my().emoji, played: played(game) }] };
          room = lead(code, { who: my(),
            onJoin(p) {
              if (S) { publish(); return; } // back after a blip: they get the game as it is
              const known = lobby.players.find((x) => x.id === p.pid);
              if (known) Object.assign(known, { name: String(p.name || known.name).slice(0, 16), emoji: p.emoji || known.emoji, played: p.played || [] });
              else if (lobby.players.length < (cfg.maxPlayers || 100)) { lobby.players.push({ id: p.pid, name: String(p.name || 'Player').slice(0, 16), emoji: p.emoji || '🙂', played: Array.isArray(p.played) ? p.played : [] }); sound('tap'); }
              publishLobby();
            },
            onAct(pid, kind, data) { if (!S) return; engine.act(S, pid, kind, data, Date.now()); publish(); },
          });
          publishLobby();
          keepAwake(true);
        } });
      };
    })();
    return { get S() { return S; }, publish, act };
  }

  return { GAMES, me, saveMe, played, markPlayed, best, index, pickSet, loadSet, norm, isRight, sound, setMuted, isMuted, heartbeat, buzzPhone, keepAwake,
    bots, chance, rand, pick, lead, join, joinUrl, qr, toast, money, answerBar, confetti, share, nameForm, topBar, clock, session };
})();
