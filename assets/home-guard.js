// Keeps hosted quizzes and the play-at-home games apart (builder pages).
//
// The play-at-home games (home/sets) take their questions out of the bank, so the builder never picks them. A question
// the AI writes for a hosted quiz could still happen to be one of them, so when a quiz is confirmed, `fix` swaps out
// anything it shares with a home game: the same question, the same answer to a question about the same thing, or one
// fact asked both ways round. The home game stays as it is: phones may already have played it.
window.LQH = (() => {
  'use strict';
  const api = (...a) => LQ.api(...a);
  const norm = LQ.normText;
  const STOP = new Set('which what where when whose does were that this with from have into about their there these those they them than then name named first most many much only also over under after before your called known'.split(' '));
  const words = (s) => new Set(norm(s).split(' ').filter((w) => w.length > 3 && !STOP.has(w)));
  const key = (text, answer) => ({ text: String(text || ''), words: words(text), ans: norm(answer || ''), t: ' ' + norm(text) + ' ' });
  /** The same test as tools/home-lib.mjs clash(…, strict = false). */
  function clash(a, b) {
    let common = 0; for (const w of a.words) if (b.words.has(w)) common++;
    const sameAns = a.ans.length > 3 && a.ans === b.ans && !/^(true|false|yes|no)$/.test(a.ans);
    if (sameAns && common >= 1) return 'same answer';
    if (common >= 3 && common / Math.max(1, Math.max(a.words.size, b.words.size)) >= 0.75) return 'same question';
    if (a.ans.length >= 4 && b.ans.length >= 4 && b.t.includes(' ' + a.ans + ' ') && a.t.includes(' ' + b.ans + ' ')) return 'same fact both ways';
    return '';
  }

  let homeKeys = null;
  /** Every question in every home game, as clash keys (fetched once). */
  async function home() {
    if (homeKeys) return homeKeys;
    const idx = await (await fetch('home/sets/index.json', { cache: 'no-cache' })).json();
    const files = [];
    for (const [game, v] of Object.entries(idx)) if (v && v.sets) for (let n = 1; n <= v.sets; n++) files.push(`home/sets/${game}-${String(n).padStart(2, '0')}.json`);
    const sets = await Promise.all(files.map((f) => fetch(f, { cache: 'no-cache' }).then((r) => r.json()).catch(() => null)));
    homeKeys = [];
    for (const s of sets.filter(Boolean)) for (const list of Object.values(s.lists || {})) for (const q of list) homeKeys.push({ ...key(q.text, q.answers ? q.answers[0] : q.options[q.correct]), where: `${s.game} ${s.set}` });
    return homeKeys;
  }
  /** A hosted quiz's questions and game rows, as clash keys with where they sit. */
  function items(quiz) {
    const out = [];
    (quiz.questions || []).forEach((q, i) => {
      if (!q || q.type === 'slide') return;
      const right = q.type === 'choice' ? (q.options || []).find((o) => o.id === q.correct)?.text : q.type === 'smash' ? q.smash : q.type === 'wheel' ? q.phrase : q.type === 'pin' ? q.place : Array.isArray(q.answers) ? q.answers[0] : '';
      const text = q.type === 'wheel' ? q.phrase : q.text;
      if (text && !/^(picture reveal|20 questions|say what you see|catchphrase|draw it|only one|hot potato|king of the hill|the chase|blockbusters)/i.test(text)) out.push({ i, row: -1, ...key(text, right) });
      (Array.isArray(q.bank) ? q.bank : []).forEach((b, j) => out.push({ i, row: j, ...key(b?.text, b?.options?.[0]) }));
    });
    return out;
  }
  /** What a hosted quiz shares with the home games: [{ i, row, text, home, why }]. */
  async function clashes(quiz) {
    const H = await home(), out = [];
    for (const it of items(quiz)) for (const h of H) { const why = clash(it, h); if (why) { out.push({ i: it.i, row: it.row, text: it.text, home: h.where, homeText: h.text, why }); break; } }
    return out;
  }
  /** Swaps out of `quiz` (in memory: the caller saves it) everything it shares with a home game, checking again
   *  until nothing is left (three goes at most). Returns { fixed, left }. */
  async function fixInPlace(quiz, onStep = () => {}) {
    let fixed = 0, left = [];
    const id = quiz.id;
    for (let pass = 0; pass < 3; pass++) {
      left = await clashes(quiz);
      if (!left.length) break;
      const done = new Set();
      for (const c of left) {
        const k = c.i + ':' + c.row; if (done.has(k)) continue; done.add(k);
        const q = quiz.questions[c.i]; if (!q) continue;
        onStep(`Swapping out “${c.text.slice(0, 60)}” (it's in ${c.home} at home)…`);
        try {
          if (c.row >= 0 && Array.isArray(q.bank) && q.type !== 'race') {
            const have = new Set(q.bank.map((b) => norm(String(b.options?.[0] ?? ''))));
            const { rows } = await api('game_rows', { game: q.type, quizId: id, count: 8 });
            const H = await home();
            const n = (rows || []).find((x) => !have.has(norm(String(x.options?.[0] ?? ''))) && !H.some((h) => clash(key(x.text, x.options?.[0]), h)));
            if (n) { q.bank[c.row] = n; fixed++; }
          } else if (window.LQW?.fresh) {
            quiz.questions[c.i] = await LQW.fresh(quiz, q.kind || q.type, q.round, [c.text, c.homeText]); fixed++;
          }
        } catch (e) { onStep('Could not swap one: ' + e.message); }
      }
    }
    return { fixed, left };
  }
  /** The same for a saved quiz, by id: fixes it and saves it. */
  async function fix(id, onStep = () => {}) {
    const quiz = LQ.normalizeQuiz((await api('get', { id })).quiz);
    const r = await fixInPlace(quiz, onStep);
    if (r.fixed) await api('save', { quiz: LQ.quizForSave(quiz) });
    return r;
  }
  return { home, clashes, fix, fixInPlace, clash, key };
})();
