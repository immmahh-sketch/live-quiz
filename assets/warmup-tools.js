// Warm-up tools for the builder pages (index.html, build.html).
//
// A warm-up is a normal quiz with settings.warmup = { code, open, until, season, forQuiz }: players play it on their
// own phones before quiz night, until `until`. `forQuiz` is the quiz night it leads up to, and the two must never
// share a question: `fix` swaps anything they share out of the warm-up (the quiz night, once confirmed, is the one
// that stays as it is). `refresh` writes the warm-up afresh from the bank for a later quiz, with a new end time and a
// new season (a fresh scoreboard, so everyone can play again).
window.LQW = (() => {
  'use strict';
  const api = (...a) => LQ.api(...a);
  const uid = (p) => p + '_' + Math.random().toString(36).slice(2, 10);
  const GAMES = ['potato', 'koth', 'chase', 'blockbusters'];
  const TIMES = { nearest: 25, catchphrase: 50, reveal: 40, choice: 20, text: 30, order: 45, pin: 25, match: 45, tf: 15, sort: 45, wipeout: 5, race: 120, smash: 30, wheel: 60, highlow: 40, rhyme: 30, club: 30, dingbat: 45, potato: 60, twenty: 150, unique: 25, koth: 15 };
  const BRIEF = "A warm-up anyone can enjoy on their own phone: mainstream, guessable and fun, with surprising 'well I never' facts. Nothing obscure, nothing regional, no specialist sport.";
  // The writer slips an Alan Shearer and a Roger question into any quiz that has neither; the quiz night has its own.
  const NO_SIGNATURES = [{ type: 'text', text: '(signature)', answers: ['Alan Shearer'] }, { type: 'text', text: '(signature)', answers: ['Roger'] }];

  /** Next Friday at 5pm, local time (today, if it is Friday before 5pm). */
  function nextFriday5pm(from = new Date()) {
    const d = new Date(from); d.setHours(17, 0, 0, 0);
    while (d.getDay() !== 5 || d <= from) { d.setDate(d.getDate() + 1); d.setHours(17, 0, 0, 0); }
    return d;
  }
  /** "2026-10-02T17:00" for a datetime-local input, in local time. */
  const toLocalInput = (d) => { const p = (n) => String(n).padStart(2, '0'); return `${d.getFullYear()}-${p(d.getMonth() + 1)}-${p(d.getDate())}T${p(d.getHours())}:${p(d.getMinutes())}`; };
  const fmtEnd = (iso) => new Date(iso).toLocaleString('en-GB', { weekday: 'long', day: 'numeric', month: 'long', hour: 'numeric', minute: '2-digit' }).replace(':00', '').replace(' pm', 'pm').replace(' am', 'am');

  /** What must not be repeated: every quiz's questions (from history) and the quiz night's game rows. */
  async function avoidFor(wuId, forQuiz) {
    let avoid = [];
    try { avoid = (await api('history', { exclude: wuId })).questions.map((q) => q.text); } catch {}
    if (forQuiz) try { for (const q of (await api('get', { id: forQuiz })).quiz.questions) { for (const b of q.bank || []) avoid.push(b.text); for (const p of q.prompts || []) avoid.push(typeof p === 'string' ? p : p.p); } } catch {}
    return avoid;
  }
  const ctxOf = (qs) => qs.filter((q) => q && q.type !== 'slide').map((q) => ({ round: q.round, type: q.type, text: String(q.text || '').slice(0, 200), category: q.category || '', ...(q.type === 'choice' ? { options: q.options, correct: q.correct } : {}), ...(Array.isArray(q.answers) ? { answers: q.answers.slice(0, 2) } : {}) })).concat(NO_SIGNATURES);

  /** One fresh item of this type from the bank, for slot `round` of warm-up `quiz`. */
  async function fresh(quiz, type, round, avoid, not = () => false) {
    const req = GAMES.includes(type) ? { topic: 'General knowledge', title: 'General knowledge', brief: '' } : { topic: 'General knowledge', title: 'Warm-up', brief: BRIEF };
    for (let tries = 0; tries < 3; tries++) {
      const res = await api('generate', { ...req, count: 1, difficulty: 'mixed', types: [type], pictures: true, web: true, avoid, quizId: quiz.id, round, context: ctxOf(quiz.questions) }, { timeout: 120000 });
      const q = (res.questions || []).find((x) => (x.kind || x.type) === type && !(x.collage && !x.media?.url) && !not(x));
      if (q) { q.round = round; q.time = TIMES[type] || 30; avoid.push(q.text); return q; }
    }
    throw new Error('Nothing suitable came back for ' + ((LQ.TYPES[type] || {}).label || type));
  }
  const save = (quiz) => api('save', { quiz: LQ.quizForSave(quiz) }); // the rounds go back into settings

  /** What the warm-up shares with its quiz night (or with `against`). */
  const clashes = (id, against) => api('warmup_clash', { id, ...(against ? { against } : {}) });

  /** Swaps out of the warm-up everything it shares with its quiz night, checking again until nothing is left
   *  (three goes at most). Returns { fixed, left, against }. */
  async function fix(id, onStep = () => {}) {
    let fixed = 0, left = [], against = null;
    for (let pass = 0; pass < 3; pass++) {
      const r = await clashes(id); against = r.against; left = r.clashes || [];
      if (!left.length) break;
      const quiz = LQ.normalizeQuiz((await api('get', { id })).quiz);
      const night = (await api('get', { id: against.id })).quiz;
      const nightAnswers = new Set(night.questions.flatMap((q) => (q.bank || []).map((b) => LQ.normText(String(b.options?.[0] ?? '')))));
      const avoid = await avoidFor(id, against.id);
      const done = new Set();
      for (const c of left) {
        const key = c.warmup.i + ':' + c.warmup.row; if (done.has(key)) continue; done.add(key);
        const q = quiz.questions[c.warmup.i]; if (!q) continue;
        onStep(`Swapping out “${c.warmup.text.slice(0, 60)}”…`);
        if (c.warmup.row >= 0 && Array.isArray(q.bank) && GAMES.concat('race').includes(q.type) && q.type !== 'race') {
          // a row in a dealt game: a fresh row from the bank
          const have = new Set(q.bank.map((b) => LQ.normText(String(b.options?.[0] ?? ''))));
          const { rows } = await api('game_rows', { game: q.type, quizId: id, count: 8 });
          const n = (rows || []).find((x) => !nightAnswers.has(LQ.normText(String(x.options?.[0] ?? ''))) && !have.has(LQ.normText(String(x.options?.[0] ?? ''))));
          if (n) { q.bank[c.warmup.row] = n; fixed++; }
        } else if (c.warmup.row >= 0 && Array.isArray(q.prompts) && q.prompts.length > 3) {
          q.prompts.splice(c.warmup.row, 1); fixed++;
        } else {
          // the whole item (a Race whose rows clash goes too: its rows are a set)
          quiz.questions[c.warmup.i] = await fresh(quiz, q.kind || q.type, q.round, avoid); fixed++;
        }
      }
      await save(quiz);
    }
    if (left.length) { const r = await clashes(id); left = r.clashes || []; against = r.against; }
    return { fixed, left, against };
  }

  /** Writes the whole warm-up afresh for a later quiz: same running order of types, new questions from the bank,
   *  a new end time and a new season (a fresh scoreboard). Then checks it against that quiz. */
  async function refresh(id, { until, forQuiz }, onStep = () => {}) {
    const quiz = LQ.normalizeQuiz((await api('get', { id })).quiz);
    const order = quiz.questions.filter((q) => q.type !== 'slide').map((q) => ({ type: q.kind || q.type, round: q.round }));
    const avoid = await avoidFor(id, forQuiz);
    const out = [];
    quiz.questions = out; // the context for each pick is what has been picked so far
    for (const [n, s] of order.entries()) {
      onStep(`Question ${n + 1} of ${order.length}: ${(LQ.TYPES[s.type] || {}).label || s.type}…`);
      out.push(await fresh(quiz, s.type, s.round, avoid));
    }
    quiz.settings.warmup = { ...(quiz.settings.warmup || {}), open: true, until: new Date(until).toISOString(), forQuiz: forQuiz || null, season: 's' + Date.now().toString(36) };
    delete quiz.settings.report; delete quiz.settings.confirmed;
    await save(quiz);
    onStep('Checking it against the quiz…');
    const f = forQuiz ? await fix(id, onStep) : { fixed: 0, left: [] };
    return { count: out.length, ...f };
  }

  /** After the quiz night is confirmed: every warm-up leading up to it is checked, and anything shared is swapped
   *  out of the warm-up. Returns [{ title, fixed, left }]. */
  async function afterConfirm(quizId, onStep = () => {}) {
    const out = [];
    const r = await api("warmup_board");
    for (const w of (r.warmups || []).filter((x) => x.forQuiz === quizId)) { onStep("Checking the warm-up “" + w.title + "”…"); const f = await fix(w.id, onStep); out.push({ title: w.title, fixed: f.fixed, left: f.left.length }); }
    return out;
  }

  return { nextFriday5pm, toLocalInput, fmtEnd, clashes, fix, refresh, afterConfirm };
})();
