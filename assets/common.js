/* Let's Quiz! — shared config and helpers used by the builder, host screen and player app. */
// GitHub Pages lets browsers keep a page for up to 10 minutes, so after an update people can be served the old one.
// On opening, ask for the page afresh; if a newer one is live, reload once to pick it up.
(async () => {
  try {
    const r = await fetch(location.pathname, { method: 'HEAD', cache: 'no-store' });
    const live = r.headers.get('last-modified');
    if (!live || new Date(live) - new Date(document.lastModified) < 2000 || sessionStorage.getItem('lq_reloaded_for') === live) return;
    sessionStorage.setItem('lq_reloaded_for', live);
    location.reload();
  } catch {}
})();
window.LQ = (() => {
  const SUPABASE_URL = 'https://safcrtrfdzsnftghibot.supabase.co';
  const SUPABASE_KEY = 'sb_publishable_RGaIB8W145BFCWzOxamQvA_7VIkTHMU';
  const API = SUPABASE_URL + '/functions/v1/quiz-api';
  const PW_KEY = 'lq_host_pw';

  // ---------------------------------------------------------------- basics
  const $ = (sel, root = document) => root.querySelector(sel);
  const $$ = (sel, root = document) => Array.from(root.querySelectorAll(sel));
  const esc = (s) => String(s ?? '').replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const uid = (p = 'x') => p + '_' + Math.random().toString(36).slice(2, 10);
  const clamp = (n, a, b) => Math.min(b, Math.max(a, n));
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
  function shuffle(arr) { const a = arr.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; }
  function store(key, val) { try { if (val === undefined) return JSON.parse(localStorage.getItem(key)); localStorage.setItem(key, JSON.stringify(val)); } catch { return null; } }
  function unstore(key) { try { localStorage.removeItem(key); } catch {} }

  // ---------------------------------------------------------------- API
  function hostPassword() { try { return localStorage.getItem(PW_KEY) || ''; } catch { return ''; } }
  function setHostPassword(pw) { try { pw ? localStorage.setItem(PW_KEY, pw) : localStorage.removeItem(PW_KEY); } catch {} }
  async function api(action, payload = {}, opts = {}) {
    const ctrl = new AbortController();
    const t = setTimeout(() => ctrl.abort(), opts.timeout || 60000);
    let r, data;
    try {
      r = await fetch(API, {
        method: 'POST', signal: ctrl.signal,
        headers: { 'content-type': 'application/json', apikey: SUPABASE_KEY, Authorization: 'Bearer ' + SUPABASE_KEY },
        body: JSON.stringify({ action, password: opts.password ?? hostPassword(), ...payload }),
      });
      data = await r.json().catch(() => ({ error: 'The server sent back something unexpected.' }));
    } catch (e) {
      throw new Error(e.name === 'AbortError' ? 'That took too long and was cancelled.' : 'Could not reach the server. Check your connection.');
    } finally { clearTimeout(t); }
    if (!r.ok || data.error) {
      const msg = data.error || (r.status === 504 || r.status === 546 ? 'The server took too long on that. Try again, or ask for fewer at once.' : 'Request failed (' + r.status + ')');
      const err = new Error(msg); err.status = r.status; throw err;
    }
    if (action === 'generate' && data && typeof data === 'object') Object.defineProperty(data, '__req', { value: payload, enumerable: false }); // for the build log
    return data;
  }
  function client() {
    return supabase.createClient(SUPABASE_URL, SUPABASE_KEY, { realtime: { params: { eventsPerSecond: 30 } } });
  }

  // ---------------------------------------------------------------- question types
  const TYPES = {
    choice: { label: 'Multiple choice', icon: '◆', blurb: 'One right answer and up to three wrong ones.' },
    text:   { label: 'Type the answer', icon: '✎', blurb: 'Players type it in. Spelling and wording are judged by AI.' },
    order:  { label: 'Put in order',    icon: '↕', blurb: 'Players arrange the items into the right order.' },
    pin:    { label: 'Drop the pin',    icon: '📍', blurb: 'Players tap a spot on a picture. Closest scores most.' },
    match:  { label: 'Match up',        icon: '⇄', blurb: 'Pair each word with its picture or partner.' },
    tf:     { label: 'True or false',   icon: '✓✗', blurb: 'A statement. Players say true or false.' },
    sort:   { label: 'Categorise',      icon: '🗂', blurb: 'Players drop each answer into the right category.' },
    wipeout:{ label: 'Wipeout',         icon: '💥', blurb: 'Answers scattered on screen, some wrong. Players take turns picking a right one. Pick a wrong one and you are wiped out.' },
    race:   { label: 'The Race',        icon: '🏁', blurb: 'A bank of quick questions on the phones. First to ten right wins the prize. Their emoji races across the screen.' },
    smash:  { label: 'Answer Smash',    icon: '🔀', blurb: 'A picture and a clue whose answers overlap. Players type the two smashed together.' },
    wheel:  { label: 'Wheel of Fortune', icon: '🎡', blurb: 'A hidden phrase on the board. Letters flip over one by one; the sooner you solve it, the more you score.' },
    highlow:{ label: 'Highbrow Lowbrow', icon: '🎓', blurb: 'A hard, scholarly clue on the screen. Stuck? Tap your phone for the easy, pop-culture clue with the same answer, for half the points.' },
    rhyme:  { label: 'Rhyme Time',      icon: '🎤', blurb: 'Two clues whose answers rhyme. Players type both answers in one go.' },
    club:   { label: 'The 1% Club',    icon: '🧠', blurb: 'Logic, wordplay and lateral thinking. No knowledge needed, just work it out. The fewer people who get it, the more it pays.' },
    dingbat:{ label: 'Dingbats',        icon: '🔤', blurb: 'Say what you see: a well-known phrase hidden in how the words are laid out.' },
    catchphrase: { label: 'Catchphrase', icon: '🗯️', blurb: 'A clip from the show plays on the screen. Players type the well-known phrase it shows.' },
    tune:   { label: 'Name That Tune',  icon: '🎵', blurb: 'A clip plays on the screen. Name the song, the artist, the film it is from, the year, or the next line.' },
    potato: { label: 'Hot Potato',      icon: '💣', blurb: 'A lit bomb passes round the room. Whoever holds it answers on their phone; get it right and pass it on. Holding it when it blows costs you points.' },
    koth:   { label: 'King of the Hill', icon: '👑', blurb: 'Fastest finger picks two players for a head-to-head buzzer battle, answered out loud. Right keeps you on the hill. First to the target wins the prize.' },
    chase:  { label: 'The Chase',       icon: '🏃', blurb: 'The leader becomes the Chaser and takes on everyone else as one team, who start a few steps ahead. First right answer on each question moves that side a step. Get home before you are caught.' },
    blockbusters: { label: 'Blockbusters', icon: '⬢', blurb: 'Two teams battle across a board of letter hexagons. First to type the answer claims the hex; the first team to link its two sides wins.' },
  };
  /** The games that run on a bank of quick questions, like The Race. */
  const BANK_GAMES = ['race', 'potato', 'koth', 'blockbusters', 'chase'];
  /** Not a question: a title, a few lines and an optional picture or video on the screen and the phones. No clock, no points. */
  const SLIDE = { label: 'Slide', icon: '🪧', blurb: 'Not a question: a welcome, the rules, a break or a message, on the screen and the phones. No points.' };
  /** Label and icon for any item in a quiz, slides included. */
  function typeInfo(t, q) { return TYPES[t] || (t === 'slide' ? (q?.break ? BREAK : SLIDE) : { icon: '❓', label: String(t || ''), blurb: '' }); }
  /** A slide's text as HTML: lines starting "-", "•" or "1." become a list, the rest paragraphs. */
  function slideHtml(body) {
    let html = '', list = [];
    const flush = () => { if (list.length) { html += `<ul>${list.map((l) => `<li>${esc(l)}</li>`).join('')}</ul>`; list = []; } };
    for (const raw of String(body || '').split(/\r?\n/)) {
      const l = raw.trim(); if (!l) { flush(); continue; }
      const m = l.match(/^(?:[-•*]|\d+[.)])\s+(.*)$/);
      if (m) list.push(m[1]); else { flush(); html += `<p>${esc(l)}</p>`; }
    }
    flush(); return html;
  }
  /** A break slide: a slide with a countdown clock. */
  const BREAK = { label: 'Break', icon: '☕', blurb: 'A big countdown clock on the screen and the phones, for half-time or a bar run. Add or take off minutes while it runs.' };
  function breakMs(q) { return clamp(Math.round(+q?.breakMins || 10), 1, 120) * 60000; }
  /** 9:05, or 1:02:05 for an hour or more. */
  function clockText(ms) { const t = Math.max(0, Math.ceil(ms / 1000)), h = Math.floor(t / 3600), m = Math.floor((t % 3600) / 60), s = t % 60; return h ? `${h}:${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}` : `${m}:${String(s).padStart(2, '0')}`; }
  /** The countdown ring: minute ticks round the edge, an arc that drains, the time in the middle. Ids get a prefix so screen and phone can differ. */
  function breakClockHtml(p = 'brk') {
    return `<div class="brkclock" id="${p}Clock"><svg viewBox="0 0 200 200" aria-hidden="true"><circle class="ticks" cx="100" cy="100" r="95" pathLength="120"/><circle class="trk" cx="100" cy="100" r="82"/><circle class="arc" id="${p}Arc" cx="100" cy="100" r="82" pathLength="1000" transform="rotate(-90 100 100)"/></svg><div class="brktime"><span id="${p}Time">0:00</span><small id="${p}Note">left of the break</small></div></div>`;
  }
  /** Moves a clock drawn by breakClockHtml on to `rem` of `total` ms. */
  function setBreakClock(p, rem, total) {
    const c = document.getElementById(p + 'Clock'); if (!c) return;
    const f = total > 0 ? clamp(rem / total, 0, 1) : 0;
    document.getElementById(p + 'Arc').style.strokeDashoffset = String(1000 * (1 - f));
    document.getElementById(p + 'Time').textContent = rem > 0 ? clockText(rem) : '0:00';
    document.getElementById(p + 'Note').textContent = rem > 0 ? 'left of the break' : "time's up!";
    c.classList.toggle('warn', rem > 0 && rem <= 120000); c.classList.toggle('end', rem > 0 && rem <= 30000); c.classList.toggle('over', rem <= 0);
  }
  // ---- Wheel of Fortune board: the show's four rows of 12/14/14/12 tiles ----
  const WHEEL_ROWS = [12, 14, 14, 12];
  /** Lays the phrase's words onto the board, centred, never splitting a word. Returns rows of tiles or null if it will not fit. */
  function wheelLayout(phrase) {
    const words = String(phrase || '').toUpperCase().replace(/\s+/g, ' ').trim().split(' ').filter(Boolean);
    if (!words.length) return null;
    // Greedy fill of the middle rows first (they are longest), then the outer ones, keeping word order top to bottom.
    const tryFit = (rowsOrder) => {
      const lines = WHEEL_ROWS.map(() => []); let wi = 0;
      for (const r of rowsOrder) { let len = 0; while (wi < words.length) { const w = words[wi]; const need = (len ? 1 : 0) + w.length; if (len + need > WHEEL_ROWS[r]) break; lines[r].push(w); len += need; wi++; } }
      return wi === words.length ? lines : null;
    };
    const total = words.join(' ').length;
    let lines = null;
    if (total <= 14) lines = tryFit([1]) || tryFit([1, 2]);
    if (!lines) lines = tryFit([1, 2]) || tryFit([0, 1, 2]) || tryFit([1, 2, 3]) || tryFit([0, 1, 2, 3]);
    if (!lines) return null;
    return lines.map((ws, r) => {
      const text = ws.join(' '), width = WHEEL_ROWS[r], pad = Math.floor((width - text.length) / 2);
      const tiles = [];
      for (let i = 0; i < width; i++) { const ch = text[i - pad]; tiles.push(!ch ? { t: 'off' } : ch === ' ' ? { t: 'gap' } : /[A-Z]/.test(ch) ? { t: 'L', ch } : { t: 'sym', ch }); }
      return tiles;
    });
  }
  /** The board as HTML. `revealed` is a string of letters already turned; `all` shows everything. */
  function wheelBoardHtml(layout, revealed = '', all = false) {
    if (!layout) return '';
    const rev = new Set(String(revealed).toUpperCase());
    return `<div class="wof">${layout.map((row) => `<div class="wof-row">${row.map((t) => t.t === 'off' ? '<span class="wt off"></span>' : t.t === 'gap' ? '<span class="wt gap"></span>' : t.t === 'sym' ? `<span class="wt on">${esc(t.ch)}</span>` : (all || rev.has(t.ch)) ? `<span class="wt on lit">${t.ch}</span>` : '<span class="wt on"></span>').join('')}</div>`).join('')}</div>`;
  }
  /** Answer Smash: the longest run of letters that ends the first answer and starts the second. */
  function smashOf(a, b) {
    const letters = (s) => String(s || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[^a-z0-9]/g, '');
    const la = letters(a), lb = letters(b);
    let n = 0;
    for (let k = Math.min(la.length - 1, lb.length - 1); k >= 1; k--) if (la.slice(-k) === lb.slice(0, k)) { n = k; break; }
    if (!n) return { smash: '', overlap: 0 };
    // Drop the first n letters of b (keeping its spacing after them) and glue.
    let seen = 0, i = 0; const bs = String(b);
    while (i < bs.length && seen < n) { if (/[a-z0-9]/i.test(bs[i].normalize('NFD')[0])) seen++; i++; }
    return { smash: String(a).trimEnd() + bs.slice(i), overlap: n };
  }
  const EMOJIS = ['🦊', '🐸', '🐼', '🦁', '🐙', '🦄', '🐢', '🐝', '🦖', '🐧', '🐨', '🦉', '🐬', '🦋', '🍕', '🚀', '🎸', '🏆', '👾', '🧙',
    '🐶', '🐱', '🐯', '🐮', '🐷', '🐵', '🦒', '🦓', '🐘', '🦈', '🐳', '🦀', '🐞', '🦜', '🌵', '🌈', '⚡', '🍔', '🎮', '👑'];
  /** What a player needs to know before a run of questions of a new type: shown on the title card, on the screen and the phones. */
  const HOWTO = {
    choice: 'Four answers on your phone. Tap the right one. The faster you are, the more you score.',
    text: 'Type your answer on your phone. Close spellings count.',
    order: 'Put the items on your phone into the right order, then lock it in.',
    pin: 'Work out the answer, then drop your pin on it. The closer you are, the more you score.',
    match: 'Tap an item, then tap its partner, until everything is paired up.',
    tf: 'True or false? Tap your answer. Quick!',
    sort: 'Put each answer into the right category.',
    wipeout: 'A board full of answers, and some of them are wrong. You get a good look first, then take turns to pick a right one. Pick a wrong one and you are wiped out.',
    race: 'Quick-fire questions on your phone. First to the target wins the bonus. Watch your emoji race across the screen.',
    smash: 'Name the picture, answer the clue, then smash the two together where they overlap: Brad Pitt + Pittsburgh = Brad Pittsburgh.',
    wheel: 'A hidden phrase. Letters turn over one at a time. Solve it on your phone: the sooner you do, the more you score.',
    highlow: 'A hard clue on the screen. Stuck? Tap your phone for the easy clue, for half the points.',
    rhyme: 'Two clues whose answers rhyme. Type both answers.',
    club: 'No knowledge needed, just logic. The fewer people who get it, the more it is worth.',
    dingbat: 'Say what you see: a well-known phrase hidden in how the words are laid out.',
    catchphrase: 'Watch the clip and say what you see: type the well-known saying it shows.',
    tune: 'Listen to the clip and answer on your phone.',
    potato: 'The bomb is lit and nobody knows how long the fuse is. If it lands on you, answer the question on your phone. Get it right and you choose who gets it next. Holding it when it goes bang costs you points.',
    koth: 'Fastest finger first picks two players to go head to head. Buzz on your phone, then say your answer out loud. Get it right and you stay on the hill and win a hill point: every one is worth points. First to the target wins the bonus too, but there are only so many head-to-heads.',
    chase: 'Whoever is in the lead is the Chaser. Everyone else plays as one team with a head start. The first right answer on each question moves that side one step: the team towards home, the Chaser towards the team. Get home before you are caught!',
    blockbusters: 'Pick a side. Your side chooses a letter, and the answer starts with it. First to type the right answer wins the hexagon for their side. Link your two sides of the board to win.',
  };
  /** The build log: every writer call for a quiz, with what was asked and what came back, kept in its settings. */
  function genLog(settings, how, res, extra = {}) {
    if (!settings || !res) return;
    const q = res.__req || {};
    const got = (res.questions || []).map((x) => ({ type: x.type, text: String(x.text || x.phrase || x.place || x.track || '').slice(0, 140), bank: !!x.fromBank }));
    pushLog(settings, { at: new Date().toISOString(), how, round: extra.round || q.title || '', topic: String(q.topic || ''), brief: String(q.brief || '').slice(0, 600), types: q.types || [], asked: q.count || 0, difficulty: q.difficulty || '', fromBank: res.fromBank || 0, written: Math.max(0, got.length - (res.fromBank || 0)), keywords: res.bankInfo?.keywords || null, matching: res.bankInfo?.matching ?? null, got, warnings: (res.warnings || []).slice(0, 4) });
  }
  function genPlan(settings, how, rounds) {
    pushLog(settings, { at: new Date().toISOString(), how, plan: (rounds || []).map((r) => ({ title: r.title || '', brief: String(r.brief || '').slice(0, 600), mix: r.mix || {} })) });
  }
  function pushLog(settings, entry) {
    if (!settings) return;
    settings.buildLog = Array.isArray(settings.buildLog) ? settings.buildLog : [];
    settings.buildLog.push(entry);
    if (settings.buildLog.length > 150) settings.buildLog.splice(0, settings.buildLog.length - 150);
  }
  const COLORS = [
    { name: 'red',    hex: '#e21b3c', shape: '▲' },
    { name: 'blue',   hex: '#1368ce', shape: '◆' },
    { name: 'yellow', hex: '#d89e00', shape: '●' },
    { name: 'green',  hex: '#26890c', shape: '■' },
  ];
  const DEFAULT_TIMES = { catchphrase: 50, choice: 20, text: 30, order: 45, pin: 25, match: 45, tf: 15, sort: 45, wipeout: 5, race: 120, smash: 30, wheel: 60, highlow: 40, rhyme: 30, club: 30, dingbat: 45, tune: 30, potato: 90, koth: 15, blockbusters: 20, chase: 15 };
  const DEFAULT_SETTINGS = { maxPoints: 1000, minPoints: 500, defaultTime: 30, showAnswersOnPhones: true, timeByType: { ...DEFAULT_TIMES } };

  /** The time limit a question of this type gets by default in this quiz. */
  function timeFor(type, settings = DEFAULT_SETTINGS) {
    const t = +(settings.timeByType || {})[type];
    return clamp(t || +settings.defaultTime || DEFAULT_TIMES[type] || 30, 5, 180);
  }

  /** Fills in what an older or partial quiz is missing: settings defaults, rounds, and a round on every question. */
  function normalizeQuiz(q) {
    const settings = { ...DEFAULT_SETTINGS, ...(q.settings || {}), timeByType: { ...DEFAULT_TIMES, ...((q.settings || {}).timeByType || {}) } };
    const questions = Array.isArray(q.questions) ? q.questions : [];
    let rounds = Array.isArray(q.rounds) ? q.rounds : Array.isArray(settings.rounds) ? settings.rounds : [];
    rounds = rounds.filter((r) => r && r.id).map((r) => {
      // The mix is how many of each type the round should have; types and count follow from it.
      let mix = r.mix && typeof r.mix === 'object' ? Object.fromEntries(Object.entries(r.mix).filter(([k, v]) => TYPES[k] && +v > 0).map(([k, v]) => [k, Math.min(40, Math.round(+v))])) : null;
      if (!mix) { const types = Array.isArray(r.types) ? r.types.filter((t) => TYPES[t]) : []; const total = +r.count || 0; mix = {}; if (types.length && total) { const each = Math.floor(total / types.length); types.forEach((t, i) => { mix[t] = each + (i < total - each * types.length ? 1 : 0); }); } }
      const types = Object.keys(mix), count = Object.values(mix).reduce((a, b) => a + b, 0);
      return { id: r.id, title: r.title || '', intro: r.intro || '', brief: r.brief || '', mix, types, count, practice: !!r.practice };
    });
    if (!rounds.length) rounds = [{ id: uid('r'), title: 'Round 1', intro: '', brief: '', mix: {}, count: 0, types: [] }];
    const ids = new Set(rounds.map((r) => r.id));
    for (const qu of questions) if (!ids.has(qu.round)) qu.round = rounds[rounds.length - 1].id;
    // Races saved under the old scoring (5000 to the winner, nothing per right answer) move to today's: 100 per right answer, 500/200/100, −200 for last.
    for (const qu of questions) if (qu.type === 'race' && qu.perCorrect === undefined) Object.assign(qu, { perCorrect: 100, prize: 500, prize2: 200, prize3: 100, forfeit: 200 });
    for (const qu of questions) if (qu.type === 'race' && qu.maxWrong === undefined) qu.maxWrong = 10;
    for (const qu of questions) if (NEW_GAME_DEFAULTS[qu.type]) for (const [k, v] of Object.entries(NEW_GAME_DEFAULTS[qu.type]())) if (qu[k] === undefined) qu[k] = v;
    delete settings.rounds;
    const quiz = { id: q.id || null, title: q.title || 'Untitled quiz', settings, rounds, questions };
    orderQuestions(quiz);
    return quiz;
  }
  /** A practice question scores nothing: ticked on its own, or its whole round is a practice round. */
  function isPractice(quiz, q) { return !!(q && (q.practice || (quiz?.rounds || []).find((r) => r.id === q.round)?.practice)); }
  /** Keeps the flat question list in play order: round by round. */
  function orderQuestions(quiz) {
    quiz.questions = quiz.rounds.flatMap((r) => quiz.questions.filter((q) => q.round === r.id));
    return quiz;
  }
  /** What gets sent to the server: rounds ride inside settings so the table needs no new column. */
  function quizForSave(quiz) {
    return { id: quiz.id, title: quiz.title, settings: { ...quiz.settings, rounds: quiz.rounds }, questions: quiz.questions };
  }

  function newQuestion(type = 'choice', settings = DEFAULT_SETTINGS) {
    if (type === 'slide') return { id: uid('q'), type: 'slide', text: '', body: '', time: 20, media: { kind: 'none' } };
    if (type === 'catchphrase') { const c = newQuestion('text', settings); c.kind = 'catchphrase'; c.text = 'Catchphrase: say what you see'; c.media = { kind: 'youtube', url: '', videoId: '', start: 0 }; c.time = timeFor('catchphrase', settings); return c; }
    const q = { id: uid('q'), type, text: '', time: timeFor(type, settings), media: { kind: 'none' }, partial: false };
    if (type === 'choice') { q.options = [0, 1, 2, 3].map(() => ({ id: uid('o'), text: '' })); q.correct = q.options[0].id; }
    if (type === 'text') { q.answers = ['']; q.ai = true; }
    if (type === 'order') { q.items = [0, 1, 2, 3].map(() => ({ id: uid('i'), text: '' })); q.hint = ''; }
    if (type === 'pin') { q.media = { kind: 'image', url: '' }; q.mode = 'point'; q.pin = { x: 0.5, y: 0.5 }; q.radiusFull = 0.04; q.radiusZero = 0.2; }
    if (type === 'smash') { q.media = { kind: 'image', url: '' }; q.pictureAnswer = ''; q.clueAnswer = ''; q.smash = ''; q.ai = true; }
    if (type === 'wheel') { q.phrase = ''; q.category = 'Phrase'; q.revealEvery = 4; q.startLetters = ''; q.ai = true; }
    if (type === 'highlow') { q.lowText = ''; q.answers = ['']; q.highPoints = 1000; q.lowPoints = 500; q.ai = true; }
    if (type === 'club') { q.answers = ['']; q.pct = 50; q.ai = true; }
    if (type === 'dingbat') { q.answers = ['']; q.elements = [{ t: '', x: 50, y: 50, s: 4 }]; q.ai = true; }
    if (type === 'tune') { q.ask = 'song'; q.track = ''; q.artist = ''; q.year = ''; q.film = ''; q.cue = ''; q.answers = ['']; q.tolerance = 1; q.media = { kind: 'audio', url: '', start: 0, length: 15 }; q.ai = true; }
    if (type === 'rhyme') { q.text2 = ''; q.answer1 = ''; q.answer2 = ''; q.ai = true; }
    if (type === 'match') { q.pairs = [0, 1, 2, 3].map(() => ({ id: uid('p'), left: '', right: { kind: 'text', value: '' } })); }
    if (type === 'tf') { q.answer = true; }
    if (type === 'sort') { q.categories = [0, 1].map(() => ({ id: uid('c'), name: '' })); q.items = [0, 1, 2, 3].map(() => ({ id: uid('i'), text: '', category: q.categories[0].id })); }
    if (type === 'wipeout') { q.right = Array.from({ length: 8 }, () => ({ id: uid('w'), text: '' })); q.wrong = Array.from({ length: 3 }, () => ({ id: uid('w'), text: '' })); q.pickPoints = 200; q.penalty = 500; q.study = 20; }
    if (type === 'race') { q.target = 10; q.maxWrong = 10; q.perCorrect = 100; q.prize = 500; q.prize2 = 200; q.prize3 = 100; q.forfeit = 200; q.bank = Array.from({ length: 20 }, () => newBankItem()); }
    if (NEW_GAME_DEFAULTS[type]) Object.assign(q, NEW_GAME_DEFAULTS[type](), { bank: Array.from({ length: type === 'potato' ? 20 : 30 }, () => newBankItem()) });
    return q;
  }
  /** Settings for the three newer bank games: filled in on new questions, and on older saves that lack them. */
  const NEW_GAME_DEFAULTS = {
    potato: () => ({ fuseMin: 40, fuseMax: 90, perCorrect: 50, penalty: 300 }),
    koth: () => ({ target: 3, prize: 1000, answerSecs: 3, perPoint: 100, maxRounds: 12 }),
    chase: () => ({ headStart: 2, target: 5, teamPrize: 1000, chaserPrize: 200 }),
    blockbusters: () => ({ teams: [{ name: 'Newcastle', color: '#f2f2f2' }, { name: 'Sunderland', color: '#e21b3c' }], hexPoints: 50, prize: 500 }),
  };
  /** The bank rows a game can use: a question and its right answer, plus (except in Blockbusters) at least one wrong one. */
  function goodRows(q) { return (q.bank || []).filter((b) => b.text?.trim() && b.options?.[0]?.trim() && (q.type === 'blockbusters' || b.options.filter((o) => o.trim()).length >= 2)); }
  function newBankItem() { return { id: uid('b'), text: '', options: ['', '', '', ''] }; }
  /** The id a right answer maps to, for the types that have one. */
  function correctId(q) { return q.type === 'tf' ? String(q.answer) : q.correct; }

  /** Something wrong with the question that would stop it being played. */
  function validate(q) {
    const problems = [];
    if (q.type === 'slide') {
      if (!(q.text || '').trim() && !(q.body || '').trim() && !q.break) problems.push('Needs a title or some text.');
      if (q.break && !(+q.breakMins >= 1 && +q.breakMins <= 120)) problems.push('A break lasts between 1 and 120 minutes.');
      if (q.media && q.media.kind === 'youtube' && !q.media.videoId) problems.push('The YouTube link is not valid.');
      return problems;
    }
    if (q.type === 'wheel') {
      if (!(q.phrase || '').trim()) problems.push('Needs the phrase.');
      else if (!wheelLayout(q.phrase)) problems.push('The phrase does not fit the board (four rows of 12, 14, 14 and 12 letters; a word cannot be split).');
      if (!(q.category || '').trim()) problems.push('Needs a category, like Phrase, Person or Place.');
      return problems;
    }
    if (q.type !== 'tune' && (!q.text || !q.text.trim())) problems.push('Needs question text.');
    if (q.type === 'choice') {
      const filled = (q.options || []).filter((o) => o.text.trim());
      if (filled.length < 2) problems.push('Needs at least two answers.');
      if (!(q.options || []).some((o) => o.id === q.correct && o.text.trim())) problems.push('Mark which answer is right.');
    }
    if (q.type === 'text' && !(q.answers || []).some((a) => a.trim())) problems.push('Needs an accepted answer.');
    if (q.type === 'order' && (q.items || []).filter((i) => i.text.trim()).length < 2) problems.push('Needs at least two items.');
    if (q.type === 'pin') {
      if (!q.media || q.media.kind !== 'image' || !q.media.url) problems.push('Needs a picture to drop the pin on.');
      if (q.mode === 'area') { if (!q.target || !(q.target.w > 0.01) || !(q.target.h > 0.01)) problems.push('Draw a box around the right thing, or pick the right tile.'); }
      else if (!q.pin) problems.push('Set where the pin goes.');
    }
    if (q.type === 'club') {
      if (!(q.answers || []).some((a) => a.trim())) problems.push('Needs the answer.');
      if (!(q.pct >= 1 && q.pct <= 99)) problems.push('Pick how many people get it (1–99%).');
    }
    if (q.type === 'tune') {
      if (!(q.media?.kind === 'audio' && q.media.url)) problems.push('Needs a clip: search for the song.');
      if (!(q.answers || []).some((a) => String(a).trim())) problems.push('Needs the answer.');
      if (q.ask === 'year' && !/^\d{4}$/.test(String(q.answers?.[0] || '').trim())) problems.push('The year needs four digits.');
    }
    if (q.type === 'dingbat') {
      if (!(q.answers || []).some((a) => a.trim())) problems.push('Needs the phrase it stands for.');
      if (!(q.elements || []).some((e) => (e.t || '').trim()) && !(q.media?.kind === 'image' && q.media.url)) problems.push('Lay out the dingbat (or upload a picture of one).');
    }
    if (q.type === 'highlow') {
      if (!(q.lowText || '').trim()) problems.push('Needs the lowbrow clue.');
      if (!(q.answers || []).some((a) => a.trim())) problems.push('Needs the answer.');
    }
    if (q.type === 'rhyme') {
      if (!(q.text2 || '').trim()) problems.push('Needs the second clue.');
      if (!(q.answer1 || '').trim() || !(q.answer2 || '').trim()) problems.push('Needs both answers.');
    }
    if (q.type === 'smash') {
      if (!q.media || !q.media.url) problems.push('Needs the picture.');
      if (!q.pictureAnswer?.trim()) problems.push('What is the picture of?');
      if (!q.clueAnswer?.trim()) problems.push('Needs the clue\'s answer.');
      if (!(q.smash || '').trim()) problems.push('The two answers don\'t overlap — change one, or type the smash yourself.');
    }
    if (q.type === 'match') {
      const ok = (q.pairs || []).filter((p) => p.left.trim() && p.right && p.right.value);
      if (ok.length < 2) problems.push('Needs at least two complete pairs.');
    }
    if (q.type === 'sort') {
      const cats = (q.categories || []).filter((c) => c.name.trim());
      if (cats.length < 2) problems.push('Needs at least two named categories.');
      const items = (q.items || []).filter((i) => i.text.trim());
      if (items.length < 2) problems.push('Needs at least two answers to sort.');
      if (items.some((i) => !cats.some((c) => c.id === i.category))) problems.push('Every answer needs a category.');
    }
    if (q.type === 'wipeout') {
      const r = (q.right || []).filter((i) => i.text.trim()).length, w = (q.wrong || []).filter((i) => i.text.trim()).length;
      if (r < 3) problems.push('Needs at least three right answers.');
      if (w < 1) problems.push('Needs at least one wrong answer.');
      if (r + w > 35) problems.push('Thirty-five answers on the board at most.');
    }
    if (q.type === 'race') {
      const good = (q.bank || []).filter((b) => b.text.trim() && b.options[0].trim() && b.options.filter((o) => o.trim()).length >= 2);
      const target = +q.target || 10, lives = q.maxWrong ?? 10;
      if (good.length < target + lives) problems.push(`Needs ${target + lives} complete questions in the bank (it has ${good.length}), so a player can get ${lives} wrong and still finish.`);
    }
    if (q.type === 'potato') {
      const n = goodRows(q).length;
      if (n < 10) problems.push(`Needs at least 10 complete questions in the bank (it has ${n}). They are reused if the bomb goes round a lot.`);
      if (!(+q.fuseMin >= 10) || !(+q.fuseMax >= +q.fuseMin) || +q.fuseMax > 600) problems.push('The fuse needs a shortest time of at least 10 seconds, and a longest time no shorter than that (600 at most).');
    }
    if (q.type === 'koth') {
      const n = goodRows(q).length;
      if (n < 12) problems.push(`Needs at least 12 complete questions in the bank (it has ${n}); a game to ${q.target || 3} can easily use 20 or more.`);
      if (!(+q.target >= 1 && +q.target <= 10)) problems.push('Points to win must be between 1 and 10.');
    }
    if (q.type === 'chase') {
      const n = goodRows(q).length;
      if (n < 15) problems.push(`Needs at least 15 complete questions in the bank (it has ${n}); a close chase can use 20 or more.`);
      if (!(+q.target >= 1 && +q.target <= 15) || !(+q.headStart >= 0 && +q.headStart <= 10)) problems.push('Steps home must be 1 to 15, and the head start 0 to 10.');
    }
    if (q.type === 'blockbusters') {
      const n = goodRows(q).length;
      if (n < BB_COLS * BB_ROWS) problems.push(`Needs at least ${BB_COLS * BB_ROWS} complete questions, one for each hexagon (it has ${n}). A few spares cover the ones nobody gets.`);
      if ((q.teams || []).length !== 2 || !q.teams.every((t) => (t.name || '').trim())) problems.push('Both teams need a name.');
    }
    if (q.media && q.media.kind === 'youtube' && !q.media.videoId) problems.push('The YouTube link is not valid.');
    return problems;
  }

  // ---- Blockbusters board: five columns of four hexagons, every other column dropped half a hex, as on the show ----
  const BB_COLS = 5, BB_ROWS = 4;
  /** The hexagons touching hexagon i (i = row * BB_COLS + column). */
  function bbNeighbours(i) {
    const c = i % BB_COLS, r = Math.floor(i / BB_COLS), odd = c % 2 === 1;
    const cand = [[c, r - 1], [c, r + 1], [c - 1, odd ? r : r - 1], [c - 1, odd ? r + 1 : r], [c + 1, odd ? r : r - 1], [c + 1, odd ? r + 1 : r]];
    return cand.filter(([x, y]) => x >= 0 && x < BB_COLS && y >= 0 && y < BB_ROWS).map(([x, y]) => y * BB_COLS + x);
  }
  /** A team's linked path as hexagon indices, or null. Team 0 joins left to right; team 1 joins top to bottom. */
  function bbPath(owner, team) {
    const n = BB_COLS * BB_ROWS, prev = {};
    const start = [...Array(n).keys()].filter((i) => owner[i] === team && (team === 0 ? i % BB_COLS === 0 : i < BB_COLS));
    const seen = new Set(start), queue = start.slice();
    while (queue.length) {
      const i = queue.shift();
      if (team === 0 ? i % BB_COLS === BB_COLS - 1 : i >= n - BB_COLS) { const path = [i]; let p = i; while (prev[p] !== undefined) { p = prev[p]; path.push(p); } return path; }
      for (const j of bbNeighbours(i)) if (owner[j] === team && !seen.has(j)) { seen.add(j); prev[j] = i; queue.push(j); }
    }
    return null;
  }
  /** Dark or light writing, whichever reads on a team's colour. */
  function inkOn(hex) { const h = String(hex || '').replace('#', ''); if (h.length < 6) return '#fff'; const [r, g, b] = [0, 2, 4].map((k) => parseInt(h.slice(k, k + 2), 16)); return (r * 299 + g * 587 + b * 114) / 1000 > 150 ? '#1b1640' : '#fff'; }
  /** The board as HTML. hexes: [{ letter, owner (-1 open, 0 or 1) }]; opts: { teams, hot (index), win (indices), pick (open ones tappable), cls }. */
  function bbBoardHtml(hexes, opts = {}) {
    const teams = opts.teams || [], win = new Set(opts.win || []);
    const col = (t) => teams[t]?.color || (t === 0 ? '#f2f2f2' : '#e21b3c');
    const cells = hexes.map((h, i) => {
      const c = i % BB_COLS, r = Math.floor(i / BB_COLS);
      const style = `left:${c * 18.75}%;top:${((r + (c % 2) / 2) / 4.5) * 100}%;${h.owner >= 0 ? `--hx:${col(h.owner)};color:${inkOn(col(h.owner))}` : ''}`;
      const tag = opts.pick && h.owner < 0 ? 'button' : 'div';
      return `<${tag} class="bbhex ${h.owner >= 0 ? 'owned' : ''} ${opts.hot === i ? 'hot' : ''} ${win.has(i) ? 'win' : ''}" style="${style}" ${tag === 'button' ? `data-hex="${i}"` : ''}><span>${esc(h.letter || '')}</span></${tag}>`;
    }).join('');
    return `<div class="bbframe ${opts.cls || ''}" style="--t0:${col(0)};--t1:${col(1)}"><div class="bbboard">${cells}</div></div>`;
  }

  function youtubeId(url) {
    const m = String(url || '').match(/(?:youtu\.be\/|v=|\/shorts\/|\/embed\/|\/live\/)([A-Za-z0-9_-]{11})/);
    return m ? m[1] : (/^[A-Za-z0-9_-]{11}$/.test(String(url || '').trim()) ? url.trim() : '');
  }

  // ---------------------------------------------------------------- scoring
  function speedPoints(elapsedMs, timeMs, settings = DEFAULT_SETTINGS) {
    const max = +settings.maxPoints || 1000, min = Math.min(+settings.minPoints || 0, max);
    const f = clamp(elapsedMs / Math.max(1, timeMs), 0, 1);
    return Math.round(max - (max - min) * f);
  }
  function normText(s) {
    return String(s || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '')
      .replace(/&/g, ' and ').replace(/[^a-z0-9]+/g, ' ').trim().replace(/^(the|a|an) /, '');
  }
  function levenshtein(a, b) {
    if (a === b) return 0; if (!a.length) return b.length; if (!b.length) return a.length;
    let prev = Array.from({ length: b.length + 1 }, (_, i) => i);
    for (let i = 1; i <= a.length; i++) {
      const cur = [i];
      for (let j = 1; j <= b.length; j++) cur[j] = Math.min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1));
      prev = cur;
    }
    return prev[b.length];
  }
  function similarity(a, b) { return 1 - levenshtein(a, b) / Math.max(a.length, b.length, 1); }
  /** 'right' | 'wrong' | 'unsure' — unsure goes to the AI. */
  function textMatch(answer, accepted) {
    const n = normText(answer);
    if (!n) return 'wrong';
    for (const acc of accepted || []) {
      const m = normText(acc);
      if (!m) continue;
      if (n === m) return 'right';
      if (m.length >= 4 && similarity(n, m) >= 0.85) return 'right';
      if (/^\d+$/.test(m) && n.replace(/\s/g, '') === m) return 'right';
    }
    return 'unsure';
  }

  // ---------------------------------------------------------------- game code + join URL
  const CODE_CHARS = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789';
  function newCode() { let c = ''; for (let i = 0; i < 6; i++) c += CODE_CHARS[Math.floor(Math.random() * CODE_CHARS.length)]; return c; }
  function playUrl(code) {
    const u = new URL('play.html', location.href);
    u.search = '?g=' + encodeURIComponent(code);
    return u.toString();
  }
  function shortPlayUrl() { return new URL('play', location.href).toString().replace(/^https?:\/\//, ''); }

  // ---------------------------------------------------------------- images
  /** Shrinks a picked image file in the browser before upload. Returns {data (base64), contentType}. */
  function resizeImage(file, maxSide = 1600) {
    return new Promise((resolve, reject) => {
      const img = new Image();
      const url = URL.createObjectURL(file);
      img.onload = () => {
        const scale = Math.min(1, maxSide / Math.max(img.width, img.height));
        const c = document.createElement('canvas');
        c.width = Math.round(img.width * scale); c.height = Math.round(img.height * scale);
        c.getContext('2d').drawImage(img, 0, 0, c.width, c.height);
        const png = file.type === 'image/png' && file.size < 1500000;
        const dataUrl = c.toDataURL(png ? 'image/png' : 'image/jpeg', 0.86);
        URL.revokeObjectURL(url);
        resolve({ data: dataUrl.split(',')[1], contentType: png ? 'image/png' : 'image/jpeg', width: c.width, height: c.height });
      };
      img.onerror = () => { URL.revokeObjectURL(url); reject(new Error('That file is not a picture we can read.')); };
      img.src = url;
    });
  }

  // ---------------------------------------------------------------- collages (Drop the pin on one of several pictures)
  /** Tiles pictures into one image in the browser. Returns the upload payload and each tile's rectangle as fractions. */
  async function composeCollage(tiles) {
    const imgs = await Promise.all(tiles.map((t) => new Promise((res, rej) => { const im = new Image(); im.crossOrigin = 'anonymous'; im.onload = () => res(im); im.onerror = () => rej(new Error(`Could not load ${t.title || 'a picture'}.`)); im.src = t.url; })));
    const n = tiles.length, cols = n <= 4 ? 2 : 3, rows = Math.ceil(n / cols), cw = 560, chh = 420, gap = 14;
    const c = document.createElement('canvas'); c.width = cols * cw + gap * (cols + 1); c.height = rows * chh + gap * (rows + 1);
    const ctx = c.getContext('2d'); ctx.fillStyle = '#ffffff'; ctx.fillRect(0, 0, c.width, c.height);
    const rects = imgs.map((im, i) => {
      const x = gap + (i % cols) * (cw + gap), y = gap + Math.floor(i / cols) * (chh + gap);
      const s = Math.max(cw / im.width, chh / im.height), sw = cw / s, sh = chh / s; // cover
      ctx.save(); ctx.beginPath(); ctx.rect(x, y, cw, chh); ctx.clip();
      ctx.drawImage(im, (im.width - sw) / 2, (im.height - sh) / 2, sw, sh, x, y, cw, chh); ctx.restore();
      ctx.strokeStyle = '#d6d6e4'; ctx.lineWidth = 3; ctx.strokeRect(x + 1.5, y + 1.5, cw - 3, chh - 3);
      return { x: x / c.width, y: y / c.height, w: cw / c.width, h: chh / c.height };
    });
    return { data: c.toDataURL('image/jpeg', 0.86).split(',')[1], contentType: 'image/jpeg', rects };
  }
  /** Composes and uploads a collage for a question whose tiles are known, and points the target at the answer. */
  async function buildCollageFor(q) {
    const tiles = (q.collage || []).filter((t) => t.url);
    if (tiles.length < 2) throw new Error('A collage needs at least two pictures.');
    const out = await composeCollage(tiles);
    const up = await api('upload', { data: out.data, contentType: out.contentType }, { timeout: 90000 });
    q.media = { kind: 'image', url: up.url, credit: tiles.map((t) => t.credit).filter(Boolean).join('; ') || undefined };
    q.collage = tiles.map((t, i) => ({ ...t, rect: out.rects[i] }));
    q.mode = 'area';
    const ai = Number.isInteger(q.answerIndex) && q.answerIndex < tiles.length ? q.answerIndex : 0;
    q.answerIndex = ai; q.target = { ...out.rects[ai] };
  }

  // ---------------------------------------------------------------- The 1% Club + Dingbats
  /** Flat points for a 1% Club question: the rarer the right answer, the more it pays (90% → 200, 50% → 600, 10% → 1000). */
  function clubPoints(pct) { return clamp(Math.round(1100 - 10 * (+pct || 50)), 200, 1000); }
  const CLUB_PCTS = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 1];
  /** Draws a dingbat: text elements placed by percentage on a white board. Sizes 1–6; rot in degrees; flip h/v; style strike/underline/box/outline. */
  function dingbatHtml(elements, cls = '') {
    const els = (elements || []).filter((e) => (e.t || '').trim());
    return `<div class="dingbat ${cls}">${els.map((e) => {
      const sz = clamp(+e.s || 3, 1, 6);
      const tf = ['translate(-50%,-50%)', e.rot ? `rotate(${clamp(+e.rot, -180, 180)}deg)` : '', e.flip === 'h' ? 'scaleX(-1)' : e.flip === 'v' ? 'scaleY(-1)' : ''].filter(Boolean).join(' ');
      const color = /^#[0-9a-f]{3,8}$/i.test(e.color || '') ? `color:${e.color};` : '';
      return `<span class="db-el ${['strike', 'underline', 'box', 'outline'].includes(e.style) ? e.style : ''}" style="left:${clamp(+e.x || 50, 0, 100)}%;top:${clamp(+e.y || 50, 0, 100)}%;font-size:${sz}em;transform:${tf};${color}">${esc(e.t)}</span>`;
    }).join('')}</div>`;
  }

  // ---------------------------------------------------------------- AI usage and a rough cost
  // List prices in US dollars per million tokens (in, out); cache reads cost a tenth of input, cache writes a quarter more.
  // Edit here if the prices change. Web searches are priced per thousand.
  const AI_PRICES = { 'claude-opus-5': [15, 75], 'claude-sonnet-5': [3, 15], 'claude-haiku-4-5-20251001': [1, 5] };
  const SEARCH_PRICE = 10;
  const AI_NAMES = { 'claude-opus-5': 'Opus', 'claude-sonnet-5': 'Sonnet', 'claude-haiku-4-5-20251001': 'Haiku' };
  /** Adds one call's usage (as the server reports it) to a quiz's running total. */
  function addUsage(settings, u) {
    if (!settings || !u || !u.model) return;
    const all = settings.aiUsage = settings.aiUsage || {};
    const m = all[u.model] = all[u.model] || { input: 0, output: 0, cacheRead: 0, cacheWrite: 0, searches: 0, calls: 0 };
    for (const k of ['input', 'output', 'cacheRead', 'cacheWrite', 'searches']) m[k] += +u[k] || 0;
    m.calls += 1;
  }
  function usageCost(all) {
    let usd = 0;
    for (const [model, m] of Object.entries(all || {})) { const [pi, po] = AI_PRICES[model] || [15, 75]; usd += (m.input * pi + m.cacheRead * pi * 0.1 + m.cacheWrite * pi * 1.25 + m.output * po) / 1e6 + (m.searches || 0) * SEARCH_PRICE / 1000; }
    return usd;
  }
  /** One line per model, plus the estimate. */
  function usageSummary(all) {
    const rows = Object.entries(all || {}).map(([model, m]) => `${AI_NAMES[model] || model}: ${m.calls} call${m.calls === 1 ? '' : 's'}, ${Math.round((m.input + m.cacheRead + m.cacheWrite) / 1000)}k in (${Math.round(m.cacheRead / 1000)}k cached), ${Math.round(m.output / 1000)}k out${m.searches ? `, ${m.searches} searches` : ''}`);
    return rows.length ? { rows, usd: usageCost(all) } : null;
  }

  // ---------------------------------------------------------------- Name That Tune
  const TUNE_ASKS = { song: { label: 'Name the song', prompt: '🎵 Name that tune' }, artist: { label: 'Name the artist', prompt: '🎤 Who is this?' }, film: { label: 'Which film is it from?', prompt: '🎬 Which film is this music from?' }, year: { label: 'What year?', prompt: '📅 What year was this released?' }, lyric: { label: 'Next line of the lyric', prompt: '🎶 The clip stops — what is the next line?' } };
  /** What the screen and phones ask for a tune question: the host's own wording, or the ask's default. */
  function tunePrompt(q) { if ((q.text || '').trim()) return q.text.trim(); if (q.ask === 'lyric' && (q.cue || '').trim()) return `🎶 What line comes after: “${q.cue.trim()}”?`; return (TUNE_ASKS[q.ask] || TUNE_ASKS.song).prompt; }
  /** A track title without the "(feat. …)", "- Remastered" and "[Single Version]" clutter: what a player would actually say. */
  function cleanTitle(t) { return String(t || '').replace(/\s*[\(\[][^)\]]*(feat\.|featuring|remaster|remastered|version|edit|mix|mono|stereo|live|radio)[^)\]]*[\)\]]/gi, '').replace(/\s+-\s+(remaster(ed)?|single version|radio edit|\d{4} remaster).*$/i, '').trim(); }
  /** Bigger Apple artwork from the 100px thumbnail the search returns. */
  function bigArt(url) { return String(url || '').replace(/\/\d+x\d+bb\./, '/600x600bb.'); }

  function fmtTime(ms) { const s = Math.max(0, Math.ceil(ms / 1000)); return s + 's'; }
  function ordinal(n) { const s = ['th', 'st', 'nd', 'rd'], v = n % 100; return n + (s[(v - 20) % 10] || s[v] || s[0]); }

  return { SUPABASE_URL, SUPABASE_KEY, $, $$, esc, uid, clamp, sleep, shuffle, store, unstore, hostPassword, setHostPassword, api, client,
    TYPES, BANK_GAMES, NEW_GAME_DEFAULTS, goodRows, BB_COLS, BB_ROWS, bbNeighbours, bbPath, bbBoardHtml, inkOn, SLIDE, BREAK, isPractice, typeInfo, slideHtml, breakMs, clockText, breakClockHtml, setBreakClock, EMOJIS, HOWTO, genLog, genPlan, pushLog, COLORS, DEFAULT_SETTINGS, DEFAULT_TIMES, timeFor, normalizeQuiz, orderQuestions, quizForSave, newQuestion, newBankItem, correctId, validate, smashOf, wheelLayout, wheelBoardHtml, WHEEL_ROWS, youtubeId, speedPoints, normText, similarity, textMatch,
    newCode, playUrl, shortPlayUrl, resizeImage, fmtTime, ordinal, composeCollage, buildCollageFor, clubPoints, CLUB_PCTS, dingbatHtml, addUsage, usageCost, usageSummary, AI_PRICES, TUNE_ASKS, tunePrompt, bigArt, cleanTitle };
})();
