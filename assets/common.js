/* Let's Quiz! — shared config and helpers used by the builder, host screen and player app. */
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
    highlow:{ label: 'Highbrow Lowbrow', icon: '🎓', blurb: 'A hard, scholarly clue first. Later an easy, pop-culture clue with the same answer joins it, for half the points.' },
    rhyme:  { label: 'Rhyme Time',      icon: '🎤', blurb: 'Two clues whose answers rhyme. Players type both answers in one go.' },
  };
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
  const EMOJIS = ['🦊', '🐸', '🐼', '🦁', '🐙', '🦄', '🐢', '🐝', '🦖', '🐧', '🐨', '🦉', '🐬', '🦋', '🍕', '🚀', '🎸', '🏆', '👾', '🧙'];
  const COLORS = [
    { name: 'red',    hex: '#e21b3c', shape: '▲' },
    { name: 'blue',   hex: '#1368ce', shape: '◆' },
    { name: 'yellow', hex: '#d89e00', shape: '●' },
    { name: 'green',  hex: '#26890c', shape: '■' },
  ];
  const DEFAULT_TIMES = { choice: 20, text: 30, order: 45, pin: 25, match: 45, tf: 15, sort: 45, wipeout: 5, race: 120, smash: 30, wheel: 60, highlow: 40, rhyme: 30 };
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
      return { id: r.id, title: r.title || '', intro: r.intro || '', brief: r.brief || '', mix, types, count };
    });
    if (!rounds.length) rounds = [{ id: uid('r'), title: 'Round 1', intro: '', brief: '', mix: {}, count: 0, types: [] }];
    const ids = new Set(rounds.map((r) => r.id));
    for (const qu of questions) if (!ids.has(qu.round)) qu.round = rounds[rounds.length - 1].id;
    delete settings.rounds;
    const quiz = { id: q.id || null, title: q.title || 'Untitled quiz', settings, rounds, questions };
    orderQuestions(quiz);
    return quiz;
  }
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
    const q = { id: uid('q'), type, text: '', time: timeFor(type, settings), media: { kind: 'none' }, partial: false };
    if (type === 'choice') { q.options = [0, 1, 2, 3].map(() => ({ id: uid('o'), text: '' })); q.correct = q.options[0].id; }
    if (type === 'text') { q.answers = ['']; q.ai = true; }
    if (type === 'order') { q.items = [0, 1, 2, 3].map(() => ({ id: uid('i'), text: '' })); q.hint = ''; }
    if (type === 'pin') { q.media = { kind: 'image', url: '' }; q.mode = 'point'; q.pin = { x: 0.5, y: 0.5 }; q.radiusFull = 0.04; q.radiusZero = 0.2; }
    if (type === 'smash') { q.media = { kind: 'image', url: '' }; q.pictureAnswer = ''; q.clueAnswer = ''; q.smash = ''; q.ai = true; }
    if (type === 'wheel') { q.phrase = ''; q.category = 'Phrase'; q.revealEvery = 4; q.startLetters = ''; q.ai = true; }
    if (type === 'highlow') { q.lowText = ''; q.answers = ['']; q.switchAt = 20; q.highPoints = 1000; q.lowPoints = 500; q.ai = true; }
    if (type === 'rhyme') { q.text2 = ''; q.answer1 = ''; q.answer2 = ''; q.ai = true; }
    if (type === 'match') { q.pairs = [0, 1, 2, 3].map(() => ({ id: uid('p'), left: '', right: { kind: 'text', value: '' } })); }
    if (type === 'tf') { q.answer = true; }
    if (type === 'sort') { q.categories = [0, 1].map(() => ({ id: uid('c'), name: '' })); q.items = [0, 1, 2, 3].map(() => ({ id: uid('i'), text: '', category: q.categories[0].id })); }
    if (type === 'wipeout') { q.right = Array.from({ length: 8 }, () => ({ id: uid('w'), text: '' })); q.wrong = Array.from({ length: 3 }, () => ({ id: uid('w'), text: '' })); q.pickPoints = 200; q.penalty = 500; q.study = 10; }
    if (type === 'race') { q.target = 10; q.perCorrect = 100; q.prize = 500; q.prize2 = 200; q.prize3 = 100; q.forfeit = 200; q.bank = Array.from({ length: 20 }, () => newBankItem()); }
    return q;
  }
  function newBankItem() { return { id: uid('b'), text: '', options: ['', '', '', ''] }; }
  /** The id a right answer maps to, for the types that have one. */
  function correctId(q) { return q.type === 'tf' ? String(q.answer) : q.correct; }

  /** Something wrong with the question that would stop it being played. */
  function validate(q) {
    const problems = [];
    if (q.type === 'wheel') {
      if (!(q.phrase || '').trim()) problems.push('Needs the phrase.');
      else if (!wheelLayout(q.phrase)) problems.push('The phrase does not fit the board (four rows of 12, 14, 14 and 12 letters; a word cannot be split).');
      if (!(q.category || '').trim()) problems.push('Needs a category, like Phrase, Person or Place.');
      return problems;
    }
    if (!q.text || !q.text.trim()) problems.push('Needs question text.');
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
    if (q.type === 'highlow') {
      if (!(q.lowText || '').trim()) problems.push('Needs the lowbrow clue.');
      if (!(q.answers || []).some((a) => a.trim())) problems.push('Needs the answer.');
      if (!((q.switchAt || 0) < q.time)) problems.push('The lowbrow clue must appear before the time limit ends.');
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
      const target = +q.target || 10;
      if (good.length < target) problems.push(`Needs at least ${target} complete questions in the bank (it has ${good.length}); more than that leaves room for skips.`);
    }
    if (q.media && q.media.kind === 'youtube' && !q.media.videoId) problems.push('The YouTube link is not valid.');
    return problems;
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

  function fmtTime(ms) { const s = Math.max(0, Math.ceil(ms / 1000)); return s + 's'; }
  function ordinal(n) { const s = ['th', 'st', 'nd', 'rd'], v = n % 100; return n + (s[(v - 20) % 10] || s[v] || s[0]); }

  return { SUPABASE_URL, SUPABASE_KEY, $, $$, esc, uid, clamp, sleep, shuffle, store, unstore, hostPassword, setHostPassword, api, client,
    TYPES, EMOJIS, COLORS, DEFAULT_SETTINGS, DEFAULT_TIMES, timeFor, normalizeQuiz, orderQuestions, quizForSave, newQuestion, newBankItem, correctId, validate, smashOf, wheelLayout, wheelBoardHtml, WHEEL_ROWS, youtubeId, speedPoints, normText, similarity, textMatch,
    newCode, playUrl, shortPlayUrl, resizeImage, fmtTime, ordinal };
})();
