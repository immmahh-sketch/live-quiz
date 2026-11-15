/* Box Clever hands-free (phones): the phone reads the game out loud and listens for your choices, for a passenger or a parked car.
 * It uses the browser's own speech: speechSynthesis to talk, SpeechRecognition (webkitSpeechRecognition on iPhone and Chrome) to listen.
 * Every choice is read back and needs a "yes" before it is sent, because a mis-heard word costs real points.
 * Hooked in at the end of bxBind (boxes-phone.js); the button appears on the Box Clever screens of a game played on phones. */
const BV = { pending: null, sayId: 0, on: false, tok: 0, key: '', rec: null, told: {}, voice: null, listening: false };
try { BV.on = localStorage.getItem('lq_handsfree') === '1'; } catch {}
const BV_TTS = typeof speechSynthesis !== 'undefined' && typeof SpeechSynthesisUtterance !== 'undefined';
const BV_SR = typeof window !== 'undefined' && (window.SpeechRecognition || window.webkitSpeechRecognition);

// ---------------------------------------------------------------- understanding what was said (pure, tested apart)
const BVP = (() => {
  const UNITS = { zero: 0, oh: 0, one: 1, two: 2, three: 3, four: 4, five: 5, six: 6, seven: 7, eight: 8, nine: 9, ten: 10, eleven: 11, twelve: 12, thirteen: 13, fourteen: 14, fifteen: 15, sixteen: 16, seventeen: 17, eighteen: 18, nineteen: 19 };
  const TENS = { twenty: 20, thirty: 30, forty: 40, fifty: 50, sixty: 60, seventy: 70, eighty: 80, ninety: 90 };
  const ORD = { first: 1, second: 2, third: 3, fourth: 4, fifth: 5, sixth: 6, seventh: 7, eighth: 8, ninth: 9, tenth: 10 };
  const norm = (s) => String(s || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/&/g, ' and ').replace(/[^a-z0-9 ]+/g, ' ').replace(/\s+/g, ' ').trim();
  const toks = (s) => norm(s).split(' ').filter(Boolean);
  /** "14", "fourteen", "twenty one", "five hundred", "1,500" -> a number, or null. */
  function number(text) {
    const d = String(text).replace(/(\d),(\d{3})/g, '$1$2').match(/\d+/);
    if (d) return +d[0];
    let total = 0, cur = 0, seen = false;
    for (const t of toks(text)) {
      if (t in UNITS) { cur += UNITS[t]; seen = true; } else if (t in TENS) { cur += TENS[t]; seen = true; }
      else if (t === 'hundred') { cur = (cur || 1) * 100; seen = true; } else if (t === 'thousand') { total += (cur || 1) * 1000; cur = 0; seen = true; }
    }
    return seen ? total + cur : null;
  }
  const STOP = new Set(['the', 'and', 'of', 'a']);
  /** Which box: a number ("box 14"), or a category and a place in its row ("traitors three"). cats: [{n}], cols per row, board: ['open'|...]. */
  function box(text, cats, cols, board) {
    const t = new Set(toks(text));
    for (let r = 0; r < cats.length; r++) {
      const w = toks(cats[r].n).filter((x) => !STOP.has(x)), long = w.filter((x) => x.length >= 4);
      const hit = long.length ? long.some((x) => t.has(x)) : w.every((x) => t.has(x));
      if (!hit) continue;
      let pos = null; for (const x of toks(text)) if (x in ORD) pos = ORD[x];
      if (pos == null) { const rest = toks(text).filter((x) => !w.includes(x)).join(' '); pos = number(rest); }
      if (pos >= 1 && pos <= cols) { const n = r * cols + pos; return board[n - 1] === 'open' ? { n } : { gone: n }; }
      return { cat: r };
    }
    const n = number(text);
    if (n >= 1 && n <= board.length) return board[n - 1] === 'open' ? { n } : { gone: n };
    return null;
  }
  const LETTERS = [['a', 'ay', 'eh', 'hey'], ['b', 'be', 'bee', 'bea'], ['c', 'see', 'sea', 'si', 'cee'], ['d', 'dee']];
  /** Which option: "B", "option c", "bee", "the second one", or the words of the option itself. Returns an index or -1. */
  function letter(text, opts) {
    const w = toks(text), n = opts.length;
    if (w.length <= 3) for (let i = 0; i < n; i++) if (w.some((x) => LETTERS[i].includes(x))) return i;
    for (const x of w) if (x in ORD && ORD[x] <= n) return ORD[x] - 1;
    let best = -1, bs = 0, tie = false; const sp = new Set(w);
    opts.forEach((o, i) => { const ot = toks(o); if (!ot.length) return; const sc = ot.filter((x) => sp.has(x)).length / ot.length; if (sc > bs) { bs = sc; best = i; tie = false; } else if (sc === bs && sc > 0) tie = true; });
    if (bs >= 0.6 && !tie) return best;
    const hits = opts.map((o, i) => (toks(o).some((x) => x.length >= 4 && sp.has(x)) ? i : -1)).filter((i) => i >= 0); // one name out of several: only one option has it
    return hits.length === 1 ? hits[0] : -1;
  }
  /** "yes" / "no" / null. */
  function yesno(text) {
    const w = toks(text);
    if (w.some((x) => ['no', 'nope', 'nah', 'wrong', 'cancel', 'change', 'back'].includes(x))) return 'no';
    if (w.some((x) => ['yes', 'yeah', 'yep', 'yup', 'okay', 'ok', 'sure', 'correct', 'right', 'confirm', 'lock'].includes(x))) return 'yes';
    return null;
  }
  /** How much to gamble: "all in", or any amount up to the pot. */
  function stake(text, pot) {
    if (/\b(all in|everything|the lot|the maximum|max)\b/.test(norm(text))) return pot;
    const n = number(text);
    return n >= 1 ? Math.min(n, pot) : null;
  }
  /** The box and the stake in one breath: "box 3, 1000 points", "box three one thousand", "history three, all in", "7 and 500".
   *  Returns { n } (a box that is open), { gone }, { cat } (a row but no place), plus { amt } when a stake was said, or null when neither was. */
  function pickStake(text, cats, cols, board, pot) {
    text = String(text).replace(/(\d),(\d{3})/g, '$1$2'); // 2,000 -> 2000
    const t = toks(text), kind = (x) => (/^\d+$/.test(x) ? 'd' : x === 'hundred' ? 'h' : x === 'thousand' ? 'k' : x in TENS ? 't' : x in UNITS ? (UNITS[x] >= 10 ? 'e' : 'u') : '');
    const joins = (k, prev) => (k === 'h' ? prev === 'u' : k === 'k' ? 'utehk'.includes(prev) && prev !== '' : k === 'u' ? 'thk'.includes(prev) && prev !== '' : (k === 't' || k === 'e') ? prev === 'h' || prev === 'k' : false);
    const groups = []; let cur = null;
    t.forEach((x, i) => { const k = kind(x); if (!k) { cur = null; return; } if (cur && k !== 'd' && joins(k, cur.last)) { cur.to = i; cur.last = k; } else { cur = { from: i, to: i, last: k }; groups.push(cur); } });
    groups.forEach((g) => { g.v = number(t.slice(g.from, g.to + 1).join(' ')); });
    const allin = /\b(all in|everything|the lot|the maximum|max)\b/.test(norm(text));
    let amt = allin ? pot : null, boxTokens = t.slice();
    const hasCat = cats.some((c) => { const w = toks(c.n).filter((x) => !STOP.has(x)), long = w.filter((x) => x.length >= 4); return long.length ? long.some((x) => t.includes(x)) : w.length && w.every((x) => t.includes(x)); });
    if (groups.length >= 2 && !allin) { const g = groups[groups.length - 1]; amt = g.v; boxTokens = t.slice(0, g.from).concat(t.slice(g.to + 1)); }
    else if (groups.length >= 2 && allin) boxTokens = t.slice(0, groups[0].to + 1);
    else if (groups.length === 1 && !allin && !hasCat && groups[0].v > board.length) return amt === null && groups[0].v >= 1 ? { amt: Math.min(groups[0].v, pot) } : null; // only a stake was said
    const b = box(boxTokens.join(' '), cats, cols, board);
    if (amt !== null) amt = Math.min(Math.max(1, amt), pot);
    if (!b) return amt ? { amt } : null;
    return amt ? Object.assign({}, b, { amt }) : b;
  }
  const go = (text) => /\b(go|start|ready|begin|yes|yeah|okay|ok|lets)\b/.test(norm(text));
  const pass = (text) => /\bpass\b/.test(norm(text));
  return { number, box, pickStake, letter, yesno, stake, go, pass, norm };
})();

// ---------------------------------------------------------------- talking and listening
// Media audio: tell the phone this is playback (like music), not a call or a web beep, so it goes to the car speakers over Bluetooth/CarPlay.
// A silent looping track keeps the phone's media session open between spoken lines, and shows "Box Clever" on the car's Now Playing screen.
function bvAudioType(t) { try { if (navigator.audioSession) navigator.audioSession.type = t; } catch {} }
function bvSilence() {
  const n = 8000, b = new Uint8Array(44 + n * 2), v = new DataView(b.buffer), w = (o, x) => { for (let i = 0; i < x.length; i++) b[o + i] = x.charCodeAt(i); };
  w(0, 'RIFF'); v.setUint32(4, 36 + n * 2, true); w(8, 'WAVEfmt '); v.setUint32(16, 16, true); v.setUint16(20, 1, true); v.setUint16(22, 1, true); v.setUint32(24, 8000, true); v.setUint32(28, 16000, true); v.setUint16(32, 2, true); v.setUint16(34, 16, true); w(36, 'data'); v.setUint32(40, n * 2, true);
  let bin = ''; for (let i = 0; i < b.length; i++) bin += String.fromCharCode(b[i]);
  return 'data:audio/wav;base64,' + btoa(bin);
}
function bvMedia(on) {
  try {
    if (on) {
      bvAudioType('playback'); bvUnlock();
      if (!BV.media) { const a = new Audio(bvSilence()); a.loop = true; a.volume = 0.01; a.setAttribute('playsinline', ''); BV.media = a; }
      BV.media.play().catch(() => {});
      if ('mediaSession' in navigator && window.MediaMetadata) {
        navigator.mediaSession.metadata = new MediaMetadata({ title: 'Box Clever', artist: "Let's Quiz!", album: 'Hands-free' });
        navigator.mediaSession.playbackState = 'playing';
      }
    } else if (BV.media) { BV.media.pause(); if ('mediaSession' in navigator) navigator.mediaSession.playbackState = 'none'; }
  } catch {}
}
function bvStatus(t) {
  const el = document.getElementById('bvstat'); if (el) el.textContent = t || '';
  // the phone app shows what is happening on the car screen: speaking, listening or idle
  try { if (window.ReactNativeWebView) window.ReactNativeWebView.postMessage(JSON.stringify({ t: 'voice', s: /^🔊/.test(t || '') ? 'speaking' : /^🎙/.test(t || '') ? 'listening' : 'idle' })); } catch {}
}
function bvAbort() { BV.sayId++; try { if (BV_TTS) speechSynthesis.cancel(); } catch {} BVN.gen++; try { BVN.stop && BVN.stop(); } catch {} try { BV.rec && BV.rec.abort(); } catch {} BV.rec = null; bvStatus(''); }

// ---------------------------------------------------------------- the natural voice
// A neural British woman (Cloudflare Workers AI, Deepgram Aura-2, via the quiz-api "tts" action) reads each line. Every line is kept as an MP3 in the public
// quiz-media bucket under a hash of the voice and the words, so a sentence is generated once for everyone; the browser works the hash out itself and goes
// straight to the file when it exists. If the service is not set up, is slow or fails, the device's own voice (below) reads it instead, as before.
// The choice is on the voice check page: lq_nvoice = a voice name, or "off" for the device voice only.
const BVN = { gen: 0, voice: 'pandora', off: false, fails: 0, audio: null, stop: null, urls: new Map(), base: 'https://safcrtrfdzsnftghibot.supabase.co/storage/v1/object/public/quiz-media/tts/' };
try { const v = localStorage.getItem('lq_nvoice'); if (v === 'off') BVN.off = true; else if (v) BVN.voice = v; } catch {}
const bvNorm = (t) => String(t || '').replace(/\s+/g, ' ').trim().slice(0, 400);
async function bvHash(s) { const d = new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(s))); return Array.from(d.slice(0, 16)).map((b) => b.toString(16).padStart(2, '0')).join(''); }
/** The MP3 for this line in this voice (making it first if it has never been spoken), or '' when the service can't be used. */
async function bvClip(text, voice) {
  const t = bvNorm(text), v = voice || BVN.voice, key = 'a2|' + v + '|' + t;
  if (BVN.urls.has(key)) return BVN.urls.get(key);
  const p = (async () => {
    try { const direct = BVN.base + (await bvHash(key)) + '.mp3', r = await fetch(direct, { method: 'HEAD' }); if (r.ok) return direct; } catch {}
    try { const r = await LQ.api('tts', { text: t, voice: v }, { timeout: 20000 }); return (r && r.url) || ''; } catch (e) { if (/501|set up/i.test(String(e && (e.message || e)))) BVN.fails = 99; return ''; }
  })();
  BVN.urls.set(key, p); const url = await p; if (!url) BVN.urls.delete(key); return url;
}
// A line to speak is a string, or a list of pieces ("segments"), each a string or { s: what is said, t: what is shown }. Pieces are made and kept one by one, so a
// sentence built from pieces that were spoken before (a name, a number, a letter) is nearly all in the cache already and plays without a wait.
const BV_LETTER_SAYS = ['Ay.', 'Bee.', 'Sea.', 'Dee.', 'Ee.', 'Eff.', 'Gee.', 'Aitch.', 'Eye.', 'Jay.', 'Kay.', 'El.', 'Em.', 'En.', 'Oh.', 'Pee.', 'Queue.', 'Are.', 'Ess.', 'Tee.', 'You.', 'Vee.', 'Double you.', 'Ex.', 'Why.', 'Zed.'];
/** The piece for a menu letter: said as its sound ("Bee."), shown as "B:". */
const bvLetter = (i) => ({ s: BV_LETTER_SAYS[i] || 'Next.', t: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[i] + ':' });
const bvSeg = (x) => (x && typeof x === 'object' ? x.s : x);
const bvText = (x) => (Array.isArray(x) ? x.map((y) => (y && typeof y === 'object' ? y.t : y)).join(' ') : String(x == null ? '' : x));
/** Warms the cache for lines that will be spoken soon (the questions to come), three at a time, so they play without a wait. */
const bvQ = { list: [], run: 0 };
function bvPrefetchMany(texts) {
  if (BVN.off || BVN.fails >= 3) return;
  for (const x of texts || []) for (const y of Array.isArray(x) ? x : [x]) { const t = bvSeg(y); if (t && !bvQ.list.includes(t)) bvQ.list.push(t); }
  while (bvQ.run < 3 && bvQ.list.length) { bvQ.run++; bvClip(bvQ.list.shift()).catch(() => {}).then(() => { bvQ.run--; bvPrefetchMany([]); }); }
}
const bvPrefetch = (text) => bvPrefetchMany([text]);
/** Whatever is being spoken stops (the natural voice and the device voice): only one voice is ever heard. */
function bvHush() { try { if (BV_TTS) speechSynthesis.cancel(); } catch {} try { BVN.stop && BVN.stop(); } catch {} }
/** A tap is what lets the phone play sound: play a moment of silence on the voice's own player. */
function bvUnlock() { try { if (!BVN.audio) { BVN.audio = new Audio(); BVN.audio.setAttribute('playsinline', ''); } BVN.audio.src = bvSilence(); BVN.audio.play().catch(() => {}); } catch {} }
/** Speaks with the natural voice for the line `id` (see bvSay): the pieces one after another, the later ones being fetched while the first plays. Resolves 'done' when it
 *  was read, 'cut' when something newer took over or it was stopped, 'fail' when it could not be played, so the device voice can read it instead (BVN.rest holds what is left
 *  to read if some pieces had already been heard). Once a piece has started it is never repeated by the device voice. */
function bvNeuralSay(segs, id) {
  return new Promise(async (res) => {
    BVN.rest = '';
    if (BVN.off || BVN.fails >= 3 || typeof LQ === 'undefined') return res('fail');
    const gen = BVN.gen, pieces = segs.map(bvSeg).filter(Boolean), clips = pieces.map((t) => bvClip(t)); // all made at once; the ones already kept come straight back
    clips.forEach((p) => p.catch(() => {}));
    let done = false, a = BVN.audio || (BVN.audio = new Audio()); a.setAttribute('playsinline', '');
    const fin = (r) => { if (done) return; done = true; BVN.stop = null; a.onended = a.onerror = null; res(r); };
    BVN.stop = () => { try { a.pause(); } catch {} fin('cut'); };
    for (let i = 0; i < pieces.length && !done; i++) {
      const url = await Promise.race([clips[i], bvWait(15000).then(() => '')]);
      if (done || gen !== BVN.gen || id !== BV.sayId) return fin('cut'); // stopped, or a newer line has taken over, while the clip was being made
      if (!url) { BVN.fails++; BVN.rest = pieces.slice(i).join(' '); return fin(i ? 'fail' : 'fail'); }
      const r = await new Promise((ok) => {
        const tm = setTimeout(() => { try { a.pause(); } catch {} ok('done'); }, 70000);
        let started = false; const end = (v) => { clearTimeout(tm); a.onended = a.onerror = null; ok(v); };
        BVN.stop = () => { clearTimeout(tm); try { a.pause(); } catch {} a.onended = a.onerror = null; ok('cut'); };
        a.onended = () => end('done'); a.onerror = () => { if (!started) BVN.fails++; end(started ? 'done' : 'fail'); };
        bvAudioType('playback'); a.src = url;
        a.play().then(() => { started = true; BVN.fails = 0; }).catch(() => end(started ? 'done' : 'fail'));
      });
      if (r === 'cut') return fin('cut');
      if (r === 'fail') { BVN.rest = pieces.slice(i).join(' '); return fin('fail'); }
    }
    fin('done');
  });
}
/** Which voice speaks: a natural-sounding British woman. A voice chosen on the voice check page (lq_voice) wins; otherwise the best en-GB female voice on the device
 *  (iPhone: Serena, Kate, Martha; Windows/Edge: Sonia, Libby, Hazel, Susan; Chrome: Google UK English Female; Android: the female Google en-GB voices), the better
 *  "premium / enhanced / natural / online" versions first. A man's voice is only used if nothing else British is there. */
function bvVoices() { try { return (speechSynthesis.getVoices() || []).slice(); } catch { return []; } }
function bvScore(v) {
  const n = (v.name || '') + ' ' + (v.voiceURI || ''), gb = /^en[-_]GB/i.test(v.lang || ''), en = /^en/i.test(v.lang || '');
  const MALE = /daniel|oliver|arthur|george|thomas|ryan|james|harry|\bmale\b|\bman\b|rjs|gbb|gbd|rishi|aaron|alex\b|fred|evan/i;
  const NAMES = ['serena', 'kate', 'martha', 'stephanie', 'sonia', 'libby', 'hazel', 'susan', 'google uk english female', 'gba', 'gbc', 'gbg', 'fis', 'female'];
  let sc = gb ? 100 : en ? 20 : 0; if (!sc) return -1;
  const i = NAMES.findIndex((x) => n.toLowerCase().includes(x)); if (i >= 0) sc += 60 - i * 3;
  if (MALE.test(n) && !/female/i.test(n)) sc -= 80;
  if (/premium|enhanced|natural|neural|online/i.test(n)) sc += 25;
  if (/siri/i.test(n)) sc -= 5;
  return sc;
}
function bvPickVoice(force) {
  if (!BV_TTS || (BV.voice && !force)) return;
  const vs = bvVoices(); if (!vs.length) return;
  let want = ''; try { want = localStorage.getItem('lq_voice') || ''; } catch {}
  BV.voice = (want && vs.find((v) => v.voiceURI === want || v.name === want)) || vs.map((v) => [bvScore(v), v]).filter((x) => x[0] >= 0).sort((a, b) => b[0] - a[0]).map((x) => x[1])[0] || null;
}
if (typeof speechSynthesis !== 'undefined') { try { speechSynthesis.addEventListener('voiceschanged', () => { BV.voice = null; bvPickVoice(); }); } catch {} }
function bvSay(line) {
  return new Promise(async (res) => {
    const segs = Array.isArray(line) ? line : [line], shown = bvText(line);
    if (!shown.trim()) return res();
    const id = ++BV.sayId; bvHush(); // only the newest line is ever spoken, and never two voices at once
    bvStatus('🔊 ' + shown);
    if ((await bvNeuralSay(segs, id)) !== 'fail' || id !== BV.sayId) return res();
    if (!BV_TTS) return res();
    const text = BVN.rest || segs.map(bvSeg).join(' ');
    bvPickVoice();
    const u = new SpeechSynthesisUtterance(text); u.lang = 'en-GB'; u.rate = 1; u.pitch = 1; if (BV.voice) { u.voice = BV.voice; u.lang = BV.voice.lang || 'en-GB'; }
    let done = false; const fin = () => { if (!done) { done = true; clearTimeout(t); res(); } };
    u.onend = fin; u.onerror = fin; const t = setTimeout(fin, 5000 + text.length * 95);
    bvAudioType('playback'); if (BV.media && BV.media.paused) BV.media.play().catch(() => {});
    try { speechSynthesis.speak(u); } catch { fin(); }
  });
}
/** Listens once; resolves with the alternatives heard (best first), or [] when nothing was heard. */
function bvListen(ms) {
  return new Promise((res) => {
    if (!BV_SR) return res([]);
    const r = new BV_SR(); let got = [], done = false; BV.lastErr = ''; BV.lastHeard = [];
    r.lang = 'en-GB'; r.interimResults = false; r.continuous = false; r.maxAlternatives = 4;
    const fin = () => { if (done) return; done = true; clearTimeout(t); BV.listening = false; bvAudioType('playback'); try { r.stop(); } catch {} if (BV.rec === r) BV.rec = null; res(got); };
    r.onresult = (e) => { const last = e.results[e.results.length - 1]; got = [...last].map((a) => String(a.transcript || '').trim()).filter(Boolean); BV.lastHeard = got; fin(); };
    r.onerror = (e) => { BV.lastErr = String((e && (e.error || e.message)) || 'error'); fin(); }; r.onend = fin;
    const t = setTimeout(() => { if (!got.length && !BV.lastErr) BV.lastErr = 'timeout'; fin(); }, ms || 7000);
    BV.rec = r; BV.listening = true; bvStatus('🎙️ Listening…');
    bvAudioType('play-and-record');
    try { r.start(); } catch { fin(); }
  });
}
const bvWait = (ms) => new Promise((r) => setTimeout(r, ms));

// ---------------------------------------------------------------- the game, step by step
const bvPlaces = (n) => n.toLocaleString('en-GB');
async function bvStep(s, my) {
  const live = () => BV.tok === my && BV.on;
  const g = s.bx, me = bxMe(s), c = g.cur, T = (i) => g.teams[i], car = lqLocalPids().length > 0, turnOf = car ? `${me.t.name}, your go. ` : '', catName = (n) => g.cats[Math.floor((n - 1) / g.cols)].n;
  let noteNext = ''; // what a handler wants said before asking again ("Box 5 has gone.")
  /** Say `prompt` (a line, or its pieces), listen, and let `handle(alternatives)` return a result (or null to try again with `retry`). */
  const ask = async (prompt, retry, handle) => {
    let lead = '', noted = false;
    for (let i = 0; i < 4 && live(); i++) {
      await bvSay(i ? [noted ? lead : lead + (retry || bvText(prompt))] : prompt); // a note ("Box 3 has gone. Which box?") already asks again if (!live()) return null;
      const alts = await bvListen(i ? 8000 : 10000); if (!live()) return null;
      if (!alts.length) { lead = 'I did not hear anything. '; noted = false; continue; }
      noteNext = ''; const r = handle(alts); if (r !== null && r !== undefined) return r;
      noted = !!noteNext; lead = noteNext ? noteNext + ' ' : '';
    }
    if (live()) { await bvSay('Tap the microphone button when you are ready to try again.'); bvStatus('Tap 🎙 to try again'); }
    return null;
  };
  const first = (alts, f) => { for (const a of alts) { const r = f(a); if (r !== null && r !== undefined && r !== -1 && r !== false) return r; } return null; };
  // The spoken flow asks as little as it can: one go is "box three, one thousand" (the box and the stake together), one answer is "B". Nothing is read back for a yes:
  // the next line says what was taken ("Box 3, History, for 1,000."), and the verdict follows the answer.

  if (g.step === 'seg' && s.bx.solo) {
    if (g.part !== 1) return;
    const rows = g.cats.map((x) => x.n).join(', ');
    await bvSay([`Box Clever. ${g.total} boxes in ${g.cats.length} rows: ${rows}.`, `Everyone starts on ${bxFmt(me.t.pot)}. Let's go!`]);
    if (live()) bxSend('next', 1);
    return;
  }
  if (g.step === 'pick') {
    const picker = T(g.pickTeam), mine = g.pickTeam === me.ti;
    if (!mine) return void (await bvSay(`${picker.name} is choosing a box.`));
    const pot = me.t.pot, rowsTold = BV.told.rows; BV.told.rows = true;
    const rows = g.cats.map((x, r) => `${x.n}, boxes ${r * g.cols + 1} to ${(r + 1) * g.cols}`).join('. ');
    const prompt = [`${me.t.name}, it's your turn.`, `You have ${bvPlaces(pot)} points in the pot.`, ...(rowsTold ? [] : [`The rows are: ${rows}.`]), 'Choose your next box and how much to gamble.',
      ...(rowsTold ? [] : [`Say a box number and your stake, like ${g.cats[g.cats.length - 1].n} three, one thousand.`])];
    let held = null; // a stake heard on its own, kept until the box comes
    const r = await ask(prompt, 'Say a box and how much to gamble, like box three, five hundred.', (alts) => {
      for (const a of alts) {
        const x = BVP.pickStake(a, g.cats, g.cols, P.state.bx.board, pot); if (!x) continue;
        if (x.amt) held = x.amt;
        if (x.n) return { n: x.n, amt: x.amt || held };
        if (x.gone) noteNext = `Box ${x.gone} has gone. Which box?`; else if (x.cat !== undefined) noteNext = 'Which place in the row?'; else if (x.amt) noteNext = `${bvPlaces(x.amt)}. Which box?`;
      }
      return null;
    });
    if (!r || !live()) return;
    BV.pending = r.amt ? { num: r.n, amt: r.amt } : null;
    return void bxSend('pick', r.n, { go: true });
  }
  if (g.step === 'stake') {
    const at = T(g.turn);
    if (g.turn !== me.ti) return void (await bvSay(`${at.name} is deciding how much to gamble.`));
    const t = me.t, pot = t.pot, pend = BV.pending; BV.pending = null;
    if (pend && pend.num === c.num && pend.amt) return void bxSend('stake', Math.max(1, Math.min(pend.amt, pot)), { go: true }); // already said with the box
    const chips = t.stakes || [], opts = chips.slice(0, -1).map(bvPlaces).join(', ');
    const amt = await ask([`Box ${c.num}, ${catName(c.num)}.`, `You have ${bvPlaces(pot)}. How much to gamble? Say ${opts ? opts + ', ' : ''}any amount, or all in.`], 'Say an amount, or all in.', (alts) => first(alts, (a) => BVP.stake(a, pot)));
    if (!amt || !live()) return;
    return void bxSend('stake', amt, { go: true });
  }
  if (g.step === 'ask' && c && c.mode !== 'host' && !c.locked) {
    const q = c.q, opts = q.opts, L = 'ABCD', mineAns = c.by === me.ti, who = T(c.by).name;
    if (q.m && q.m.k === 'tune') { await bvSay('Listen to the clip.'); for (let i = 0; i < 17 && live(); i++) await bvWait(1000); if (!live()) return; }
    const head = `Box ${c.num}, ${catName(c.num)}${c.stake ? `, for ${bvPlaces(c.stake)}` : ''}.`;
    const read = [q.t, ...(opts ? opts.flatMap((o, i) => [bvLetter(i), `${o}.`]) : [])]; // each piece is made once and kept, so the options can come in any order
    if (!mineAns) return void (await bvSay([head, ...read, `${who} is answering.`]));
    const lead = [...(turnOf ? [turnOf.trim()] : []), head, ...read];
    if (opts) {
      const say = `Say ${opts.map((_, i) => L[i]).join(', ')}${c.canPass ? ', or pass' : ''}.`;
      const r = await ask([...lead, say], say, (alts) => {
        if (c.canPass && alts.some((a) => BVP.pass(a))) return 'pass';
        return first(alts, (a) => { const i = BVP.letter(a, opts); return i >= 0 ? i : null; });
      });
      if (r === null || !live()) return;
      return void (r === 'pass' ? bxSend('pass', 1, { go: true }) : bxSend('ans', r, { go: true }));
    }
    const said = await ask([...lead, `Say your answer${c.canPass ? ', or pass' : ''}.`], 'Say your answer.', (alts) => (c.canPass && alts.some((a) => BVP.pass(a)) ? { pass: true } : { text: alts[0] }));
    if (!said || !live()) return;
    return void (said.pass ? bxSend('pass', 1, { go: true }) : bxSend('ans', said.text, { go: true }));
  }
  if (g.step === 'result' && c?.res) {
    const r = c.res, rt = T(r.team);
    await bvSay([...(r.passed ? ['Passed.'] : r.ok ? ['Correct!'] : ['Wrong.', `The answer was ${r.right}.`]), `${rt.name} ${r.delta >= 0 ? 'plus' : 'minus'} ${bvPlaces(Math.abs(r.delta))}.`, `${rt.name} now has ${bvPlaces(rt.pot)}.`]);
    if (!live()) return;
    await bvWait(400); if (live() && !P.state.bx.closing) bxSend('next', 1);
  }
}
/** What a Box Clever game will read out, piece by piece (its questions, options and right answers), so the natural voice can make them before they are needed. game = the game's file. */
function bvBoxLines(game) {
  const out = BV_LETTER_SAYS.slice(0, 4);
  for (const row of ((game && game.questions && game.questions[0] && game.questions[0].cats) || [])) for (const q of row.qs || []) {
    if (q.t) out.push(q.t);
    for (const o of q.o || []) out.push(`${o}.`);
    for (const o of q.a || []) out.push(`${o}.`);
    if (q.w) out.push(`${q.w}.`);
    const right = q.o ? q.o[0] : (q.a || [])[0]; if (right) out.push(`The answer was ${right}.`);
  }
  return out;
}
/** Called at the end of bxBind: start the spoken part of a new step (once per step). */
function bxVoiceTick(s) {
  if (!s?.bx?.solo || window.LQ_TV) return; // only the games played on phones (not the TV version, which is read and moved with the remote)
  bvButton();
  if (!BV.on) return;
  const g = s.bx, c = g.cur;
  const key = [g.step, g.turn, g.pickTeam, g.asked, c?.num, c?.q?.t, c?.q?.opts?.length, c?.locked ? 1 : 0, c?.by, c?.res ? 1 : 0].join('|');
  if (key === BV.key) return;
  BV.key = key; bvAbort(); const my = ++BV.tok;
  bvStep(s, my).catch(() => {});
}
/** The end of a game: the scores, read out. */
function bxVoiceFinal(s) {
  if (!s?.bx?.solo) return;
  bvButton();
  if (!BV.on || BV.key === 'final') return;
  BV.key = 'final'; bvAbort(); ++BV.tok;
  const t = (s.bx?.teams || []).map((x) => ({ n: x.name, v: Math.max(0, x.pot) - (x.loan || 0) })).sort((a, b) => b.v - a.v);
  if (t.length) bvSay(`Game over. ${t.map((x) => `${x.n} ${bvPlaces(x.v)}`).join('. ')}. ${t[0].n} wins!`);
}
function bvButton() {
  if (document.getElementById('bvbtn')) return;
  const wrap = document.createElement('div');
  wrap.id = 'bvbtn';
  wrap.style.cssText = 'position:fixed;left:0;right:0;bottom:0;z-index:50;display:flex;flex-direction:column;align-items:center;gap:4px;padding:6px 10px calc(6px + env(safe-area-inset-bottom,0px));pointer-events:none';
  wrap.innerHTML = '<div id="bvstat" style="max-width:100%;font-size:.8rem;color:#fff;background:rgba(20,16,50,.82);border-radius:10px;padding:3px 10px;display:none"></div><button type="button" id="bvtog" style="pointer-events:auto;border:0;border-radius:999px;padding:9px 16px;font:700 .9rem system-ui;background:#1b1544;color:#fff;box-shadow:0 2px 10px rgba(0,0,0,.35)"></button>';
  document.body.appendChild(wrap); document.body.style.paddingBottom = '70px'; // so the button never sits over the game's own buttons
  const tog = wrap.querySelector('#bvtog'), stat = wrap.querySelector('#bvstat');
  const paint = () => { tog.textContent = BV.on ? '🎙️ Hands-free: ON (tap to turn off)' : '🎙️ Hands-free'; tog.style.background = BV.on ? '#2e9d57' : '#1b1544'; };
  new MutationObserver(() => { stat.style.display = stat.textContent ? 'block' : 'none'; }).observe(stat, { childList: true, characterData: true, subtree: true });
  paint();
  tog.onclick = () => {
    BV.on = !BV.on; try { localStorage.setItem('lq_handsfree', BV.on ? '1' : '0'); } catch {}
    paint(); BV.key = ''; ++BV.tok; bvAbort();
    bvMedia(BV.on);
    if (BV.on) {
      try { if (BV_TTS) { speechSynthesis.cancel(); speechSynthesis.speak(new SpeechSynthesisUtterance('')); } } catch {} // a tap is what lets the phone start talking
      if (!BV_TTS) toast('This browser cannot read aloud.', true);
      else if (!BV_SR) toast("This browser can read the game out but can't listen. Tap your answers.", false);
      if (P.state?.bx) { if (P.state.phase === 'final') { BV.key = ''; bxVoiceFinal(P.state); } else bxVoiceTick(P.state); }
    }
  };
}
