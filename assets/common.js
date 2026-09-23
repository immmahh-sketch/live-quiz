/* Live Quiz — shared config and helpers used by the builder, host screen and player app. */
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
  };
  const COLORS = [
    { name: 'red',    hex: '#e21b3c', shape: '▲' },
    { name: 'blue',   hex: '#1368ce', shape: '◆' },
    { name: 'yellow', hex: '#d89e00', shape: '●' },
    { name: 'green',  hex: '#26890c', shape: '■' },
  ];
  const DEFAULT_TIMES = { choice: 20, text: 30, order: 45, pin: 25, match: 45 };
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
    rounds = rounds.filter((r) => r && r.id).map((r) => ({ id: r.id, title: r.title || '', brief: r.brief || '' }));
    if (!rounds.length) rounds = [{ id: uid('r'), title: 'Round 1', brief: '' }];
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
    if (type === 'pin') { q.media = { kind: 'image', url: '' }; q.pin = { x: 0.5, y: 0.5 }; q.radiusFull = 0.04; q.radiusZero = 0.2; }
    if (type === 'match') { q.pairs = [0, 1, 2, 3].map(() => ({ id: uid('p'), left: '', right: { kind: 'text', value: '' } })); }
    return q;
  }

  /** Something wrong with the question that would stop it being played. */
  function validate(q) {
    const problems = [];
    if (!q.text || !q.text.trim()) problems.push('Needs question text.');
    if (q.type === 'choice') {
      const filled = (q.options || []).filter((o) => o.text.trim());
      if (filled.length < 2) problems.push('Needs at least two answers.');
      if (!(q.options || []).some((o) => o.id === q.correct && o.text.trim())) problems.push('Mark which answer is right.');
    }
    if (q.type === 'text' && !(q.answers || []).some((a) => a.trim())) problems.push('Needs an accepted answer.');
    if (q.type === 'order' && (q.items || []).filter((i) => i.text.trim()).length < 2) problems.push('Needs at least two items.');
    if (q.type === 'pin') { if (!q.media || q.media.kind !== 'image' || !q.media.url) problems.push('Needs a picture to drop the pin on.'); if (!q.pin) problems.push('Set where the pin goes.'); }
    if (q.type === 'match') {
      const ok = (q.pairs || []).filter((p) => p.left.trim() && p.right && p.right.value);
      if (ok.length < 2) problems.push('Needs at least two complete pairs.');
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
    TYPES, COLORS, DEFAULT_SETTINGS, DEFAULT_TIMES, timeFor, normalizeQuiz, orderQuestions, quizForSave, newQuestion, validate, youtubeId, speedPoints, normText, similarity, textMatch,
    newCode, playUrl, shortPlayUrl, resizeImage, fmtTime, ordinal };
})();
