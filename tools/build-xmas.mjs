// Builds the Christmas Day night (assets/xmas*.js) from the question bank and saves it as a draft quiz, the same way the portal's
// "🎄 Make a Christmas Day night" button does, but from Node so it needs no browser sign-in (host password in LQ_PASSWORD).
//   LQ_PASSWORD=... node tools/build-xmas.mjs [--title "Christmas Day · 27 Nov"] [--save] [--break 15] [--ketchup 3] [--no-games] [--no-finish]
// It writes tools/xmas-last.json first (always); --save then saves it as a draft quiz and prints the id.
// The dish categories below lean on the four Christmas topics so the night feels festive; change DISHCATS to taste.
import fs from 'node:fs'; import vm from 'node:vm'; import path from 'node:path'; import url from 'node:url';
const here = path.dirname(url.fileURLToPath(import.meta.url)), ROOT = path.join(here, '..');
const args = process.argv.slice(2), arg = (k, d) => (args.includes(k) ? args[args.indexOf(k) + 1] : d), has = (k) => args.includes(k);
const KEY = 'sb_publishable_RGaIB8W145BFCWzOxamQvA_7VIkTHMU';
const api = async (action, body) => {
  for (let i = 0; i < 4; i++) {
    try {
      const r = await fetch('https://safcrtrfdzsnftghibot.supabase.co/functions/v1/quiz-api', { method: 'POST', headers: { 'content-type': 'application/json', apikey: KEY, Authorization: 'Bearer ' + KEY }, body: JSON.stringify({ password: process.env.LQ_PASSWORD, action, ...body }) });
      const d = await r.json().catch(() => ({})); if (!r.ok || d.error) throw new Error(d.error || 'HTTP ' + r.status); return d;
    } catch (e) { if (i === 3) throw e; await new Promise((s) => setTimeout(s, 1500)); }
  }
};
const uid = (p) => p + '_' + Math.random().toString(36).slice(2, 10);
const shuffle = (a) => { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };

// ---- LQ (common.js + the Christmas Day data) in a vm, as tools/lq.mjs does
const ctxv = { document: { addEventListener() {}, querySelector() { return null; }, querySelectorAll() { return []; }, createElement() { return { style: {}, setAttribute() {}, appendChild() {} }; }, head: { appendChild() {} } }, location: { href: 'https://letsquiz.uk/', search: '', pathname: '/' }, navigator: { userAgent: 'node' }, localStorage: { getItem() { return null; }, setItem() {}, removeItem() {} }, sessionStorage: { getItem() { return null; }, setItem() {}, removeItem() {} }, setTimeout, clearTimeout, setInterval, clearInterval, console, fetch, URLSearchParams, URL, crypto };
ctxv.window = ctxv; vm.createContext(ctxv);
for (const f of ['assets/common.js', 'assets/xmas-data.js']) vm.runInContext(fs.readFileSync(path.join(ROOT, f), 'utf8'), ctxv);
const LQ = ctxv.LQ, X = LQ.XMAS;
if (!X) throw new Error('assets/xmas-data.js did not load');

// ---- the portal's own layout code, lifted out of assets/night-tools.js so the two can never drift apart
const nt = fs.readFileSync(path.join(ROOT, 'assets/night-tools.js'), 'utf8');
const grab = (start) => { const i = nt.indexOf(start); if (i < 0) throw new Error('night-tools.js: cannot find ' + start); let p = nt.indexOf('(', i), pd = 0; for (; p < nt.length; p++) { if (nt[p] === '(') pd++; else if (nt[p] === ')') { pd--; if (pd === 0) break; } } let j = nt.indexOf('{', p), d = 0; for (; j < nt.length; j++) { if (nt[j] === '{') d++; else if (nt[j] === '}') { d--; if (d === 0) break; } } return nt.slice(i, j + 1); };
const grabLine = (start) => { const i = nt.indexOf(start); if (i < 0) throw new Error('night-tools.js: cannot find ' + start); return nt.slice(i, nt.indexOf('\n', i)); };
const S = { quiz: null, sel: 0 };
const box = { LQ, S, uid, shuffle, touch() {}, renderEditor() {}, Math, Object, Array, JSON, Number, String };
vm.createContext(box);
vm.runInContext([grabLine('const STYLES ='), grabLine('const GAMES ='), grabLine('const xmMix ='), grab('function xmInterleave('), grab('function xmLayout('), 'const $ = LQ.$, $$ = LQ.$$;'].join('\n') + '\nthis.xmLayout = xmLayout; this.xmMix = xmMix; this.STYLES = STYLES; this.GAMES = GAMES;', box);
const { xmLayout, xmMix, STYLES, GAMES } = box;

// ---- the night
const TITLE = arg('--title', 'Christmas Day · ' + new Date().toLocaleDateString('en-GB', { day: 'numeric', month: 'short' }));
const MINS = Math.max(1, Math.min(60, +arg('--break', 15))), NK = Math.max(1, Math.min(4, X.KETCHUP_QS.length, +arg('--ketchup', 3)));
// dish key -> bank category (the dish defaults are in assets/xmas-data.js; these lean on the Christmas topics)
const DISHCATS = { turkey: 'Christmas', potatoes: 'Christmas films', pigs: 'Christmas songs', stuffing: 'History', parsnips: 'Geography', sprouts: 'Food and drink', gravy: 'Christmas TV', cranberry: 'Sport', yorkie: 'Science' };
const dishes = X.dishes().map((i) => ({ k: i.k, cat: DISHCATS[i.k] || i.cat, n: i.n }));
const style = STYLES.mixed, games = has('--no-games') ? [] : ['potato', 'blockbusters', 'race'], fin = !has('--no-finish');
const settings = { ...LQ.DEFAULT_SETTINGS, xmas: { on: true }, hostPanel: true };
const rounds = [], questions = [];
const slide = (text, body, extra = {}) => ({ ...LQ.newQuestion('slide', settings), id: uid('q'), text, body, ...extra });
const mkRound = (t, intro, extra = {}) => ({ id: uid('r'), title: t, intro: intro || '', brief: '', mix: {}, count: 0, types: [], practice: false, ...extra });
const welcome = mkRound('Welcome', ''); rounds.push(welcome);
const fam = X.CHARS.map((c) => `${c.icon} ${c.name}: ${c.power}`).join('\n');
questions.push(
  slide('Welcome to Christmas Day!', 'Join on your phone at letsquiz.uk/play. Tonight is one long Christmas Day, from stockings at 7am to midnight, and everybody is building a Christmas dinner.', { round: welcome.id }),
  slide('🎄 Build your Christmas dinner', `Every question belongs to a category, and every category is a dish: ${X.dishes().map((i) => `${i.icon} ${i.name}`).join(', ')}. Get a question right and the item goes on your dish. The rarer items turn up less often, and only the quickest right answers collect them.\n\nThe last item, the tomato ketchup, is won only with a 1% question.`, { round: welcome.id }),
  slide('👨‍👩‍👧 Meet the family', `Everyone has been dealt a family member, with a quirk that always works and one power to play between questions. Tap 🍽 on your phone to see yours.\n\n${fam}`, { round: welcome.id }));
const dishRounds = dishes.map((d) => { const it = X.item(d.k), r = mkRound(d.cat, '', { source: 'bankonly', difficulty: X.RARITY[it.rar].diff, mix: xmMix(style, d.n), count: d.n, _xm: d.k }); r.types = Object.keys(r.mix).filter((t) => r.mix[t] > 0); rounds.push(r); return r; });
const gameRounds = games.map((g) => { const label = GAMES.find((x) => x[0] === g)[1]; const r = mkRound(label, '', { mix: { [g]: 1 }, count: 1, types: [g], source: 'bankonly' }); rounds.push(r); return r; });
let smashR = null, chaseR = null;
if (fin) { smashR = mkRound('Double Points: Answer Smash', '', { mix: { smash: 5 }, count: 5, types: ['smash'], source: 'bankonly', double: true }); chaseR = mkRound('The Final Chase', '', { mix: { chase: 1 }, count: 1, types: ['chase'], source: 'bankonly' }); rounds.push(smashR, chaseR); }
settings.rounds = rounds;
const quiz = LQ.normalizeQuiz({ title: TITLE, settings, rounds, questions }); S.quiz = quiz;

// ---- save a skeleton first so the bank can stamp what it hands over as used for this quiz
let quizId = null;
if (has('--save')) { const r = await api('save', { quiz: LQ.quizForSave(quiz) }); quizId = r.quiz.id; quiz.id = quizId; console.log('Draft quiz created:', quizId); }

// ---- fill every round from the bank (no AI), one type at a time, as the portal does
const avoid = []; const short = [];
for (const r of quiz.rounds) {
  if (!r.count) continue;
  for (const type of Object.keys(r.mix)) {
    const need = r.mix[type]; if (!need) continue;
    let got = 0;
    while (got < need) {
      const ask = { topic: r.title, title: r.title, brief: '', usedPictures: [], count: Math.min(need - got, ['potato', 'koth', 'blockbusters', 'chase'].includes(type) ? 1 : 6), difficulty: r.difficulty || 'mixed', useBank: true, bankOnly: true, types: [type], pictures: true, web: true, avoid, premium: false, quizId, round: r.id };
      let res; try { res = await api('generate', ask); } catch (e) { console.log(`  ${r.title} ${type}: ${e.message}`); break; }
      if (!res.questions?.length) break;
      for (const q of res.questions) { q.round = r.id; q.time = LQ.timeFor(q.kind || q.type, settings); quiz.questions.push(q); avoid.push(q.text); got++; }
    }
    if (got < need) short.push(`${r.title} ${type}: ${got}/${need}`);
    console.log(`  ${r.title} · ${type}: ${got}/${need}`);
  }
}

// ---- tag every item question with its dish, mix them into four courses, add the games, ketchup, break and finale
const dm = Object.fromEntries(dishRounds.map((r) => [r.id, r._xm]));
xmLayout({ dishIds: dm, gameIds: gameRounds.map((r) => r.id), smashId: smashR?.id, chaseId: chaseR?.id, welcomeId: welcome.id, nk: NK, mins: MINS });

// ---- check every question can be played
const bad = []; quiz.questions.forEach((q, i) => { const p = LQ.validate(q); if (p.length) bad.push(`#${i + 1} ${String(q.text || q.type).slice(0, 50)}: ${p[0]}`); });
const real = quiz.questions.filter((q) => q.type !== 'slide').length;
const out = path.join(here, 'xmas-last.json'); fs.writeFileSync(out, JSON.stringify(LQ.quizForSave(quiz), null, 1));
console.log(`\n${quiz.rounds.length} rounds, ${quiz.questions.length} items (${real} questions). Written to tools/xmas-last.json`);
if (short.length) console.log('SHORT:', short.join('; '));
if (bad.length) console.log('NOT PLAYABLE:', bad.join('\n  '));
if (has('--save')) { const r = await api('save', { quiz: LQ.quizForSave(quiz) }); console.log('SAVED', r.quiz?.id || JSON.stringify(r).slice(0, 200)); } else console.log('(dry run: nothing saved; add --save to create the draft)');
