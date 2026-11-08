/* Box Clever: the team gambling quiz (host side). Written 7 Nov 2026 to the host's spec.
 *
 * 50 numbered boxes in 5 rows (a category per row). Players are split into teams when the game starts (2 teams for 6 or fewer,
 * 3 for 7-10, 4 for 11 or more); each team votes in a captain (a tie is settled by a spinner) who has the deciding say. Every team
 * starts with 10,000. On a team's turn the captain picks a box, how much of the pot to gamble (right: it comes back doubled;
 * wrong: it's gone) and may play a power: Double bet (4x back), Swap, Make them answer, Make the host answer, 50:50. Each power
 * once. No clocks. With more than 15 players the board grows by 10 boxes for every 5 more.
 *
 * It is a run of quiz items (type 'boxes', part 1 to 4) with the bonus rounds between them. G.bx is the game, kept across the
 * parts; each part ends after its share of the questions (12, 25, 37, 50) and hands on with nextFrom(). Points that players earn in
 * the bonus rounds go into their team's pot when the next part (or the final result) begins.
 *
 * Pool on the item (part 1): q.cats = [{ name, emoji, qs: [Q] }], q.reserve = [Q] (fills a category that runs short; Swap uses its own category's leftovers), q.hostq = [Q] (questions the host has
 * never seen, for "Make the host answer"). Q is { t, o: [right, wrong, wrong, wrong] } or { t, a: [accepted answers], w: 'a wrong answer that looks right' }.
 * Phones talk to it with answer payloads { bx: 'v', k, v, go, dbl, target }: see bxAnswer. */
const BX_START = 10000, BX_LOAN = 1000;
const BX_SOLO = [{ color: '#3b82f6' }, { color: '#e5484d' }, { color: '#30a46c' }, { color: '#f5a524' }, { color: '#a855f7' }, { color: '#14b8a6' }];
/** The stake buttons for a pot: 10%, 30%, 50% and 75% of a base, then all in. The base only steps up with every 5,000 held, so 1,000 to 4,999
 *  plays as 1,000 (100, 300, 500, 750), 5,000 to 9,999 as 5,000 (500, 1,500, 2,500, 3,750), 10,000 to 14,999 as 10,000 (1,000, 3,000, 5,000,
 *  7,500), and 100,000 as 100,000 (10,000, 30,000, 50,000, 75,000). Under 1,000 the base is the pot itself. A team can also type its own. */
function bxStakes(pot) {
  pot = Math.max(0, Math.round(pot)); if (pot <= 0) return [];
  const base = pot < 1000 ? pot : pot < 5000 ? 1000 : Math.floor(pot / 5000) * 5000, step = base < 1000 ? 10 : 50;
  return [...[0.1, 0.3, 0.5, 0.75].map((f) => Math.max(step, Math.round(base * f / step) * step)).filter((x, i, a) => x < pot && a.indexOf(x) === i), pot];
}
/** A team that has lost everything is lent a thousand to carry on with; it comes off its score at the end. */
function bxBroke(t) { if (t.pot > 0) return false; t.owes = true; return true; } // down to nothing: 0 points until its next go, when bxLend steps in
/** A team that went bankrupt is lent its thousand when its next go comes round, with a pop-up (b.loanNote) on the phones and the big screen. */
function bxLend() {
  const b = G.bx, t = b.teams[b.turn]; if (!t || !t.owes) return;
  t.owes = false; if (t.pot > 0) return; // it has points again (bonus round): no loan needed
  t.pot = BX_LOAN; t.loan = (t.loan || 0) + BX_LOAN; b.loanNote = { team: t.i, at: Date.now() };
}
const bxNet = (t) => Math.max(0, t.pot) - (t.loan || 0);
const BX_TEAMS = [
  { name: 'Red Dragons', emoji: '🐉', color: '#e5484d' }, { name: 'Blue Sharks', emoji: '🦈', color: '#3b82f6' },
  { name: 'Green Frogs', emoji: '🐸', color: '#30a46c' }, { name: 'Gold Lions', emoji: '🦁', color: '#f5a524' },
];
const BX_POWERS = {
  double: { icon: '⚡', name: 'Double bet', how: 'Play before the question: a right answer pays 4× your stake back' },
  swap: { icon: '🔄', name: 'Swap question', how: 'Bin this question for a different one' },
  make: { icon: '👉', name: 'Make them answer', how: 'Pick another team to answer: their points, not yours, change' },
  host: { icon: '🎤', name: 'Make the host answer', how: 'The host has to answer it. Right or wrong, it counts for you' },
  fifty: { icon: '✂️', name: '50:50', how: 'Two answers left: the right one and one that looks right' },
  pickfor: { icon: '👈', name: 'Pick their box', how: "Choose the box another team has to play on its next turn. They still decide how much to bet" },
};
const bxShuffle = (a) => { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
const bxN = (n) => Math.round(n).toLocaleString('en-GB');
const bxTeamOf = (pid) => (G.bx ? G.bx.teams.findIndex((t) => t.members.includes(pid)) : -1);
const bxPids = () => Object.keys(G.players).filter((p) => !(G.viewers || {})[p]);

/** The game's size from the number of players: teams, questions, boxes per row, and where the bonus rounds fall. */
function bxSizes(n) {
  const teams = Math.max(1, Math.min(n <= 6 ? 2 : n <= 10 ? 3 : 4, n)), total = 50 + (n > 15 ? Math.ceil((n - 15) / 5) * 10 : 0);
  return { teams, total, cols: total / 5, cuts: [0.24, 0.5, 0.74, 1].map((f) => Math.round(total * f)) };
}
function bxInit(q) {
  const solo = !!WARMUP || !!q.solo, isBot = (p) => (G.bots || []).some((x) => x.pid === p), start = +q.start || BX_START;
  let ps = bxShuffle(bxPids()), sz = bxSizes(ps.length), teams;
  if (solo) { // the warm-up: one phone, everyone for themselves (the real player first), no host to ask, so no "Make the host answer"
    ps = [...ps.filter((p) => !isBot(p)), ...ps.filter(isBot)];
    const cols = +q.cols || 10, total = cols * 5;
    sz = { teams: ps.length, total, cols, cuts: q.cuts || [0.24, 0.5, 0.74, 1].map((f) => Math.round(total * f)) };
    teams = ps.map((p, i) => ({ i, name: G.players[p].name, emoji: G.players[p].emoji || '🙂', color: BX_SOLO[i % BX_SOLO.length].color, members: [p], captain: p, pot: start, loan: 0, powers: { double: 1, swap: 1, make: 1, fifty: 1, pickfor: 1 } }));
  } else {
    teams = BX_TEAMS.slice(0, sz.teams).map((t, i) => ({ i, ...t, members: [], captain: null, pot: start, loan: 0, powers: { double: 1, swap: 1, make: 1, host: 1, fifty: 1, pickfor: 1 } }));
    ps.forEach((p, i) => teams[i % teams.length].members.push(p));
  }
  const all = q.cats || [], cats = (solo && all.length <= 5 ? all : bxShuffle(all)).slice(0, 5), reserve = bxShuffle(q.reserve || []); // the warm-up's five categories are the same for everyone, in the same order
  const board = [], spare = [];
  cats.forEach((c, r) => {
    const qs = bxShuffle((c.qs || []).filter((x) => !(solo && x.m && x.m.k === 'img'))); // no blurred pictures on one phone: with no clock you could just wait for them to clear
    for (let k = 0; k < sz.cols; k++) board.push({ cat: r, q: qs[k] || reserve.pop() || { t: 'A spare question: what is 2 + 2?', o: ['4', '3', '5', '22'] }, st: 'open' });
    spare.push(qs.slice(sz.cols)); // Swap draws from the same category's own leftovers
  });
  G.bx = { v: 1, solo, start, ...sz, cats: cats.map((c) => ({ n: c.name, e: c.emoji || '' })), board, teams, turn: 0, asked: 0, part: 1, step: solo ? 'seg' : 'teams', votes: {}, cur: null, reserve: bxShuffle(reserve), spare, hostq: bxShuffle(q.hostq || []), snap: Object.fromEntries(Object.values(G.players).map((p) => [p.id, p.score])), log: [] };
}
/** Points earned by individuals in the bonus rounds since the last look go into their team's pot. */
function bxAbsorb() {
  const b = G.bx; if (!b) return {};
  const got = {};
  for (const p of Object.values(G.players)) {
    const ti = bxTeamOf(p.id), d = p.score - (b.snap[p.id] ?? p.score); b.snap[p.id] = p.score;
    if (ti >= 0 && d) { const t = b.teams[ti]; t.pot = Math.max(0, t.pot + d); bxBroke(t); got[ti] = (got[ti] || 0) + d; }
  }
  return got;
}
/** A player who joins after the teams were made goes to the smallest team. */
function bxSync() {
  const b = G.bx; if (!b || b.solo || b.step === 'teams') return;
  for (const t of b.teams) { // someone removed from the game leaves their team; a captain who has gone is replaced
    t.members = t.members.filter((m) => G.players[m]);
    if (t.captain && !t.members.includes(t.captain) && b.step !== 'vote') t.captain = t.members[0] || null;
  }
  for (const pid of bxPids()) if (bxTeamOf(pid) < 0) b.teams.slice().sort((x, y) => x.members.length - y.members.length)[0].members.push(pid);
}
function bxStart() {
  const q = question();
  G.q.bx = { part: q.part || 1 };
  if (!G.bx) bxInit(q);
  const b = G.bx; b.part = q.part || 1; b.votes = {};
  if (b.part === 1 && (b.step === 'teams' || (b.solo && !b.asked && !b.cur))) { /* the team reveal / the warm-up's first screen */ }
  else { b.lastAbsorb = bxAbsorb(); b.step = 'seg'; }
  persist(); render(); broadcastState(); bxBots();
}
function bxGo(step) { const b = G.bx; b.step = step; b.votes = {}; persist(); render(); broadcastState(); bxBots(); }

// ---------------------------------------------------------------- what the phones are told
function bxPublic() {
  const b = G.bx; if (!b) return null; bxSync();
  const c = b.cur;
  return { v: 1, step: b.step, part: b.part, turn: b.turn, solo: !!b.solo, closing: !!b.closing, pickTeam: bxPickTeam(), forcedBy: b.forcedBy || {}, pickNote: b.pickNote || '', total: b.total, cols: b.cols, asked: b.asked, cut: b.cuts[b.part - 1], cats: b.cats, board: b.board.map((x) => x.st), boardBy: b.board.map((x) => x.by ?? -1),
    teams: b.teams.map((t) => ({ i: t.i, name: t.name, emoji: t.emoji, color: t.color, members: t.members, captain: t.captain, pot: t.pot, loan: t.loan || 0, owes: !!t.owes, stakes: bxStakes(t.pot), powers: t.powers, spin: t.spin || null })),
    loanNote: b.loanNote || null, votes: b.votes, absorb: b.lastAbsorb || null, names: Object.fromEntries(Object.values(G.players).map((p) => [p.id, { name: p.name, emoji: p.emoji || '' }])),
    cur: c ? { num: c.num, at: c.openedAt || 0, cat: c.cat, stake: c.stake, dbl: c.dbl, by: c.by, origin: c.origin, mode: c.mode, sub: c.sub || '', canPass: c.mode === 'own' && !c.noPass, passes: (c.passes || 0), locked: c.locked !== undefined, lockedAs: c.locked !== undefined ? c.locked : null,
      q: b.step === 'stake' || b.step === 'open' ? { t: '', kind: c.q.kind, opts: null } : { t: c.q.t, kind: c.q.kind, opts: c.q.opts ? c.q.opts.map((o) => o.t) : null, m: c.q.m || null }, used: c.used || [], res: b.step === 'result' || c.sub === 'judged' ? c.res : null, note: c.note || '' } : null };
}

// ---------------------------------------------------------------- what the phones do
function bxAnswer(pid, a) {
  const b = G.bx; if (!b || !a || a.bx !== 'v') return;
  const ti = bxTeamOf(pid); if (ti < 0) return;
  const t = b.teams[ti], cap = t.captain === pid, k = String(a.k || ''), v = a.v, go = !!a.go && cap, c = b.cur;
  if (b.solo && k === 'next') { if (b.step === 'seg') return bxClickGo(); if (b.step === 'result' && !b.closing) return bxClose(bxNextTurn); return; }
  if (b.step === 'vote' && k === 'cap') { if (t.members.includes(v)) b.votes[pid] = v; }
  else if (b.step === 'pick' && ti === bxPickTeam() && k === 'pick') {
    const n = Math.round(+v); if (!(n >= 1 && n <= b.board.length) || b.board[n - 1].st !== 'open') return;
    b.votes[pid] = n; if (go) return bxPick(n);
  } else if (b.step === 'pick' && ti === b.turn && ti === bxPickTeam() && k === 'pow') {
    (b.votes.pow = b.votes.pow || {})[pid] = String(v); if (go && v === 'pickfor') return bxPower('pickfor', a.target);
  } else if (b.step === 'stake' && ti === b.turn && k === 'stake') {
    const amt = Math.max(0, Math.round(+v) || 0); b.votes[pid] = { amt, dbl: !!a.dbl && !!t.powers.double };
    if (go) return bxStake(amt, !!a.dbl);
  } else if (b.step === 'ask' && c && ti === c.by && c.mode !== 'host' && k === 'ans') {
    const val = c.q.kind === 'text' && !c.q.opts ? String(v ?? '').trim().slice(0, 60) : Math.round(+v);
    if (c.q.kind === 'text' && !c.q.opts ? !val : !(val >= 0 && val < c.q.opts.length)) return;
    (b.votes.ans = b.votes.ans || {})[pid] = val; if (go) return bxLock(val);
  } else if (b.step === 'ask' && c && ti === c.by && c.mode === 'own' && !c.noPass && k === 'pass') {
    (b.votes.pass = b.votes.pass || {})[pid] = 1; if (go) return bxPass();
  } else if (b.step === 'ask' && c && ti === c.origin && c.by === c.origin && c.mode === 'own' && k === 'pow') {
    (b.votes.pow = b.votes.pow || {})[pid] = String(v); if (go) return bxPower(String(v), a.target);
  } else return;
  persist(); render(); broadcastState();
}

// ---------------------------------------------------------------- the turn
function bxCount() { // captains from the votes; a tie goes to the spinner
  const b = G.bx;
  for (const t of b.teams) {
    const tally = {}; for (const m of t.members) tally[m] = 0;
    for (const [pid, who] of Object.entries(b.votes)) if (t.members.includes(pid) && who in tally) tally[who]++;
    const top = Math.max(...Object.values(tally)), cands = Object.keys(tally).filter((m) => tally[m] === top);
    t.captain = cands[Math.floor(Math.random() * cands.length)];
    t.spin = { cands, tally, tie: cands.length > 1, at: Date.now() };
  }
  b.step = 'captains'; b.votes = {}; sound('fanfare'); persist(); render(); broadcastState(); bxBots();
}
function bxPick(n) {
  const b = G.bx, cell = b.board[n - 1], t = b.teams[b.turn];
  cell.st = 'now';
  const raw = cell.q, kind = raw.o ? 'choice' : 'text';
  b.cur = { num: n, cat: cell.cat, stake: 0, dbl: false, by: b.turn, origin: b.turn, mode: 'own', used: [], q: bxMakeQ(raw, kind), raw, noPass: !!cell.passed };
  delete b.pickNote; const forcer = (b.forcedBy || {})[b.turn];
  if (forcer !== undefined) { b.cur.note = `👈 ${b.teams[forcer].name} chose this box for ${t.name}`; delete b.forcedBy[b.turn]; }
  b.step = 'stake'; b.votes = {}; sound('ding'); persist(); render(); broadcastState(); bxBots();
}
function bxMakeQ(raw, kind) {
  const q = { id: raw.id || raw.t, t: raw.t, kind, answers: raw.a || [], decoy: raw.w || '' }; if (raw.m) q.m = raw.m; // m: { k: 'img', url } a picture that clears as the seconds pass, or { k: 'tune', url, start, len } a clip
  if (kind === 'choice') q.opts = bxShuffle(raw.o.map((t, i) => ({ t, ok: i === 0 })));
  return q;
}
function bxStake(amt, dbl) {
  const b = G.bx, c = b.cur, t = b.teams[b.turn];
  c.stake = Math.min(t.pot, Math.max(Math.min(10, t.pot), Math.round(amt) || 0));
  if (dbl && t.powers.double) { t.powers.double = 0; c.dbl = true; c.used.push('double'); }
  b.step = 'open'; b.votes = {}; sound('go'); persist(); render(); broadcastState();
}
/** The host clicks the drawer: it is pulled out, a paper comes out and unfolds, and the question is revealed (to the screen and the phones). */
function bxOpen() {
  const b = G.bx, c = b.cur; if (!c || b.step !== 'open') return;
  c.openedAt = Date.now(); b.step = 'ask'; b.votes = {}; sound('whoosh'); persist(); render(); broadcastState(); bxBots();
}
/** Pass: the team leaves the box shut again and loses half the stake. Everyone has seen the question, so the next team to take
 *  this box must answer it (a box can only be passed once). Passed boxes do not count towards the bonus rounds or the end. */
function bxPass() {
  const b = G.bx, c = b.cur; if (!c || b.step !== 'ask' || c.mode !== 'own' || c.noPass || c.locked !== undefined) return;
  const t = b.teams[c.by], delta = -Math.min(Math.floor(c.stake / 2), t.pot);
  t.pot = Math.max(0, t.pot + delta);
  const cell = b.board[c.num - 1]; cell.st = 'open'; cell.passed = true; cell.q = c.raw;
  c.res = { passed: true, ok: null, delta, team: t.i, right: '', said: '', broke: bxBroke(t) };
  b.log.push({ n: c.num, team: t.i, passed: true, delta }); b.step = 'result';
  sound('trombone'); persist(); render(); broadcastState();
}
/** The drawer shuts (and the paper folds away) before the next team is up. */
function bxClose(then) {
  const b = G.bx; if (b.closing) return;
  b.closing = true; sound('whoosh'); render(); broadcastState();
  setTimeout(() => { if (G.bx !== b) return; b.closing = false; then(); }, 1000);
}
function bxIsRight(c, v) {
  if (c.q.opts) return !!c.q.opts[v]?.ok;
  const acc = c.q.answers.join('/'); return LQ.textMatch(String(v), c.q.answers) === 'right' || LQ.behindRight(String(v), acc);
}
function bxRightText(c) { return c.q.opts ? (c.q.opts.find((o) => o.ok)?.t || '') : (c.q.answers[0] || ''); }
function bxLock(v) {
  const c = G.bx.cur; if (!c || c.locked !== undefined) return;
  c.locked = v; G.bx.step = 'locked'; G.bx.votes.ans = G.bx.votes.ans || {}; sound('ding'); persist(); render(); broadcastState();
}
/** The answer is revealed and the pot moves. who: the team it lands on; ok: right or wrong. */
function bxSettle(ok) {
  const b = G.bx, c = b.cur, t = b.teams[c.by];
  const delta = ok ? (c.dbl ? 3 : 1) * c.stake : -Math.min(c.stake, t.pot);
  t.pot = Math.max(0, t.pot + delta);
  const cell = b.board[c.num - 1]; cell.st = ok ? 'won' : 'lost'; cell.by = t.i;
  c.res = { ok, delta, team: t.i, broke: bxBroke(t), right: bxRightText(c), said: c.mode === 'host' ? 'the host' : c.locked !== undefined ? (c.q.opts ? c.q.opts[c.locked]?.t : c.locked) : '' };
  b.log.push({ n: c.num, team: t.i, ok, delta }); b.asked++; b.step = 'result';
  sound(ok ? 'fanfare' : 'trombone'); if (ok) confetti();
  persist(); render(); broadcastState();
}
function bxReveal() { const c = G.bx.cur; if (!c) return; if (c.mode === 'host') { c.sub = 'revealed'; persist(); render(); broadcastState(); return; } bxSettle(bxIsRight(c, c.locked)); }
function bxNextTurn() {
  const b = G.bx; if (G.phase !== 'question') return; // a late timer from the last box must not carry on past the next item (it skipped Hot Potato)
  b.cur = null; b.votes = {};
  b.turn = (b.turn + 1) % b.teams.length;
  for (const cell of b.board) if (cell.st === 'now') cell.st = 'open'; // nothing is on the table now: a box left half-picked goes back
  if (!b.board.some((x) => x.st === 'open')) b.asked = Math.max(b.asked, b.cuts[b.part - 1]); // and with no box left the part is over, whatever the count
  if (b.asked >= b.cuts[b.part - 1]) { b.lastSnap = true; for (const p of Object.values(G.players)) b.snap[p.id] = p.score; b.step = 'seg'; persist(); return nextFrom(G.qIndex); }
  b.step = 'pick'; bxLend(); persist(); render(); broadcastState(); bxBots();
}
/** Skip (the host panel's Skip this question): the box on the table is thrown away, nobody wins or loses, and the next team is up. */
function bxSkip() {
  const b = G.bx; if (!b) return false;
  if (b.step === 'teams' || b.step === 'vote' || b.step === 'captains') { return false; }
  if (b.step === 'seg') { b.step = 'pick'; bxLend(); persist(); render(); broadcastState(); bxBots(); return true; }
  if (b.cur) { const cell = b.board[b.cur.num - 1]; if (cell) cell.st = 'void'; b.asked++; }
  bxNextTurn(); return true;
}

// ---------------------------------------------------------------- powers
/** Whose phones pick the box: the team whose turn it is, unless another team has played Pick their box on them. */
function bxPickTeam() { const b = G.bx; const f = (b.forcedBy || {})[b.turn]; return f !== undefined ? f : b.turn; }
function bxPower(name, target) {
  const b = G.bx, c = b.cur;
  if (name === 'pickfor') { // played on the team's own turn, before or after its own box is picked
    const origin = c ? c.origin : b.turn, t = b.teams[origin], to = Math.round(+target);
    if (!t.powers.pickfor || (c && (c.mode !== 'own' || c.locked !== undefined)) || !(to >= 0 && to < b.teams.length) || to === origin) return;
    b.forcedBy = b.forcedBy || {}; if (b.forcedBy[to] !== undefined) return;
    t.powers.pickfor = 0; b.forcedBy[to] = origin; b.votes = {};
    if (c) { c.used.push('pickfor'); c.note = `👈 ${t.name} will pick ${b.teams[to].name}'s next box`; } else b.pickNote = `👈 ${t.name} will pick ${b.teams[to].name}'s next box`;
    sound('go'); return bxDone();
  }
  if (!c) return; const t = b.teams[c.origin]; if (!t.powers[name] || c.mode !== 'own' || c.locked !== undefined) return;
  if (name === 'double') return; // played with the stake
  if (name === 'fifty') {
    if (c.q.opts && c.q.opts.length <= 2) return;
    t.powers.fifty = 0; c.used.push('fifty');
    if (c.q.opts) { const right = c.q.opts.find((o) => o.ok), wrong = bxShuffle(c.q.opts.filter((o) => !o.ok))[0]; c.q.opts = bxShuffle([right, wrong]); }
    else { c.q.opts = bxShuffle([{ t: c.q.answers[0], ok: true }, { t: c.q.decoy || bxDecoy(c), ok: false }]); }
    c.note = '✂️ 50:50 played';
  } else if (name === 'swap') {
    const next = (b.spare && b.spare[c.cat] || []).shift(); if (!next) { c.note = 'There are no spare questions left in this category.'; return bxDone(); }
    t.powers.swap = 0; c.used.push('swap'); c.raw = next; const keep = c.used, st = c.stake, dbl = c.dbl; c.q = bxMakeQ(next, next.o ? 'choice' : 'text'); c.used = keep; c.stake = st; c.dbl = dbl;
    c.note = '🔄 Swapped for a new question';
  } else if (name === 'make') {
    const to = Math.round(+target); if (!(to >= 0 && to < b.teams.length) || to === c.origin) return;
    t.powers.make = 0; c.used.push('make'); c.by = to; c.mode = 'made'; c.note = `👉 ${b.teams[to].name} must answer. Their points change, not ${t.name}'s`;
  } else if (name === 'host') {
    t.powers.host = 0; c.used.push('host'); c.mode = 'host'; c.sub = 'think'; c.note = '🎤 The host has to answer this one';
  } else return;
  b.votes = {}; sound('go'); bxDone();
}
function bxDone() { persist(); render(); broadcastState(); bxBots(); }
function bxDecoy(c) { // a wrong answer from another text question in the pool, the closest thing to a believable one
  const b = G.bx, others = b.board.filter((x) => x.q.a && x.q !== c.raw && x.cat === c.cat).map((x) => x.q.a[0]); return others.length ? others[Math.floor(Math.random() * others.length)] : 'None of these';
}
/** "I've seen this one": the host's question is swapped for one from the unseen pile. */
function bxHostNew() {
  const b = G.bx, c = b.cur; if (!c || c.mode !== 'host') return;
  const h = b.hostq.shift() || b.reserve.shift(); if (!h) { toast('No unseen questions are left.', true); return; }
  c.q = bxMakeQ(h, h.o ? 'choice' : 'text'); c.raw = h; c.sub = 'think'; c.note = '🎤 A question the host has not seen'; bxDone();
}
function bxHostJudge(ok) { const c = G.bx.cur; if (!c || c.mode !== 'host' || c.sub !== 'revealed') return; c.locked = undefined; c.sub = 'judged'; bxSettle(ok); }

// ---------------------------------------------------------------- the host's own buttons
function bxForce() { // a safety net: the host decides for a captain whose phone has gone
  const b = G.bx, t = b.teams[b.turn];
  if (b.step === 'vote') return bxCount();
  if (b.step === 'pick') { const open = b.board.map((x, i) => x.st === 'open' ? i + 1 : 0).filter(Boolean); return bxPick(open[Math.floor(Math.random() * open.length)]); }
  if (b.step === 'stake') return bxStake(Math.min(t.pot, 500), false);
  if (b.step === 'open') return bxOpen();
  if (b.step === 'ask' && b.cur) { const c = b.cur; return bxLock(c.q.opts ? Math.floor(Math.random() * c.q.opts.length) : '(no answer)'); }
}
function bxWaitNote() {
  const b = G.bx; if (!b) return '';
  const t = b.teams[b.cur && b.step !== 'pick' ? b.cur.by : b.turn];
  if (b.step === 'pick') return `Waiting for ${b.teams[bxPickTeam()].name}'s captain to pick a box. Use "Pick for them" if their phone has gone.`;
  if (b.step === 'stake') return `Waiting for ${t.name}'s captain to set the stake.`;
  if (b.step === 'ask') return `Waiting for ${t.name}'s captain to lock in an answer.`;
  if (b.cur?.mode === 'host') return b.cur.sub === 'revealed' ? 'Press "I got it right" or "I got it wrong".' : '';
  return '';
}
document.addEventListener('click', (e) => {
  const el = e.target.closest?.('[data-bx]'); if (!el || !G?.bx) return;
  const k = el.dataset.bx;
  if (k === 'replay') { const m = G.bx.cur?.q.m; if (m) playTune({ media: { url: m.url, start: m.start || 0, length: m.len || 15 } }); } else if (k === 'force') bxForce(); else if (k === 'hostnew') bxHostNew(); else if (k === 'hostright') bxHostJudge(true); else if (k === 'hostwrong') bxHostJudge(false);
  else if (k === 'flip' && G.bx.step === 'result') { const c = G.bx.cur, r = c.res, t = G.bx.teams[r.team]; if (r.broke) t.owes = false; t.pot = Math.max(0, t.pot - r.delta); const cell = G.bx.board[c.num - 1]; const ok = !r.ok; const delta = ok ? (c.dbl ? 3 : 1) * c.stake : -Math.min(c.stake, t.pot); t.pot = Math.max(0, t.pot + delta); cell.st = ok ? 'won' : 'lost'; c.res = { ...r, ok, delta, broke: bxBroke(t) }; persist(); render(); broadcastState(); }
});
function bxNextBtn() { // the step button for each screen
  const b = G.bx, c = b.cur;
  const go = (label, on) => `<button class="btn btn-primary btn-lg" id="bxGo" data-next="1">${label}</button>`;
  if (b.step === 'teams') return go('Choose captains ▶');
  if (b.step === 'vote') return go('Count the votes ▶');
  if (b.step === 'captains') return go('Start the game ▶');
  if (b.step === 'seg') return go(b.part === 1 ? 'Start ▶' : 'Carry on ▶');
  if (b.step === 'open') return go(`Open box ${c.num} ▶`);
  if (b.step === 'locked') return go('Reveal the answer ▶');
  if (b.step === 'result') return go(b.asked >= b.cuts[b.part - 1] ? (b.part < 4 ? 'On to the bonus round ▶' : 'On to the Answer Smashes ▶') : 'Next team ▶');
  if (b.step === 'ask' && c?.mode === 'host') return c.sub === 'revealed' ? '<button class="btn btn-primary btn-lg" data-bx="hostright">✔ I got it right</button><button class="btn btn-ghost btn-lg" data-bx="hostwrong">✘ I got it wrong</button>' : `<button class="btn btn-ghost" data-bx="hostnew">I've seen this one: new question</button><button class="btn btn-primary btn-lg" id="bxReveal" data-next="1">Reveal the answer ▶</button>`;
  return `<button class="btn btn-ghost" data-bx="force">${b.step === 'pick' ? 'Pick a box for them' : b.step === 'stake' ? 'Set 500 for them' : b.step === 'ask' ? 'Lock in for them' : 'Decide for them'}</button>`;
}
function bxClickGo() {
  const b = G.bx, c = b.cur;
  if (b.step === 'teams') return bxGo('vote');
  if (b.step === 'vote') return bxCount();
  if (b.step === 'captains') { b.step = 'pick'; b.votes = {}; bxLend(); persist(); render(); broadcastState(); bxBots(); return; }
  if (b.step === 'seg') { b.step = 'pick'; b.votes = {}; bxLend(); persist(); render(); broadcastState(); bxBots(); return; }
  if (b.step === 'open') return bxOpen();
  if (b.step === 'locked') return bxReveal();
  if (b.step === 'result') return bxClose(bxNextTurn);
  if (b.step === 'ask' && c?.mode === 'host') return bxReveal();
}

// ---------------------------------------------------------------- the host screen
function bxStrip() {
  const b = G.bx, act = b.step === 'pick' || b.step === 'stake' || b.step === 'ask' || b.step === 'locked' ? (b.cur ? b.cur.by : b.turn) : -1;
  return `<div class="bxteams">${b.teams.map((t) => `<div class="bxteam ${t.i === act ? 'on' : ''} ${b.cur && t.i === b.cur.origin && b.cur.by !== b.cur.origin ? 'asker' : ''}" style="--tc:${t.color}">
    <div class="bxtn">${t.emoji} ${esc(t.name)}${(b.forcedBy || {})[t.i] !== undefined ? ` · 👈 ${esc(b.teams[b.forcedBy[t.i]].name)} pick their box` : ''}</div><div class="bxpot">${bxN(t.pot)}</div>${t.loan ? `<div class="bxcap">🏦 owes ${bxN(t.loan)}</div>` : ''}
    <div class="bxcap">${t.captain ? '👑 ' + esc(pname(t.captain)) : esc(t.members.map(pname).join(', '))}</div>
    <div class="bxpw">${Object.entries(BX_POWERS).map(([k, p]) => `<span class="${t.powers[k] ? '' : 'gone'}" title="${esc(p.name)}">${p.icon}</span>`).join('')}</div></div>`).join('')}</div>`;
}
/** The cabinet: a drawer for every box, numbered on the front. The chosen one glows until the host clicks it, then it is pulled out;
 *  once it is answered (right or wrong) it shuts with the number gone; a passed box shuts and goes back to normal. */
function bxCabinet() {
  const b = G.bx, c = b.cur, inQ = c && ['ask', 'locked', 'result'].includes(b.step), inSel = c && ['stake', 'open'].includes(b.step);
  return `<div class="bxcab ${b.closing ? 'closing' : ''}" style="--cols:${b.cols}">${b.cats.map((cat, r) => `<div class="bxcabrow"><div class="bxcat">${cat.e} ${esc(cat.n)}</div><div class="bxdrawers">${Array.from({ length: b.cols }, (_, k) => {
    const n = r * b.cols + k + 1, cell = b.board[n - 1], cur = c && c.num === n;
    const cls = cur && inQ ? 'out' : cur && inSel ? 'sel' : (cell.st === 'won' || cell.st === 'lost' || cell.st === 'void') ? 'done' : '';
    const tc = cell.by !== undefined && cls === 'done' ? `--tc:${b.teams[cell.by]?.color}` : '';
    return `<div class="bxdr ${cls}${cur && inQ && b.closing ? ' shut' : ''}" data-n="${n}" style="${tc}"><div class="bxdrface"><span class="bxplate">${cls === 'done' ? '' : n}</span><i class="bxhandle"></i></div></div>`; }).join('')}</div></div>`).join('')}</div>`;
}
let bxAnimDone = '';
/** The paper that comes out of the drawer: it unfolds the first time it is drawn, and folds away when the drawer shuts. */
function bxPaper(inner) {
  const b = G.bx, c = b.cur, key = c.num + ':' + (c.openedAt || 0);
  return `<div class="bxpaper ${c.openedAt && bxAnimDone !== key ? 'fresh' : ''} ${b.closing ? 'fold' : ''}" data-key="${key}">${inner}</div>`;
}
function bxVoteCounts() { // for the chart: how the answering team's members are voting
  const b = G.bx, c = b.cur, t = b.teams[c.by], v = (b.votes.ans || {}), mem = t.members.filter((m) => v[m] !== undefined);
  if (c.q.opts) return { n: mem.length, of: t.members.length, bars: c.q.opts.map((o, i) => ({ t: o.t, p: mem.length ? Math.round(mem.filter((m) => v[m] === i).length / mem.length * 100) : 0, n: mem.filter((m) => v[m] === i).length })) };
  const tally = {}; for (const m of mem) { const k = LQ.normText(v[m]); (tally[k] = tally[k] || { t: v[m], n: 0 }).n++; }
  return { n: mem.length, of: t.members.length, bars: Object.values(tally).sort((x, y) => y.n - x.n).map((x) => ({ t: x.t, p: Math.round(x.n / mem.length * 100), n: x.n })) };
}
/** The picture (blurred at first, clearing over 20 seconds) or the tune player of a question. */
function bxMediaHtml(c, reveal) {
  const m = c.q.m; if (!m) return '';
  if (m.k === 'img') return `<div class="bxpic"><img src="${esc(m.url)}" alt="" style="animation-delay:-${reveal ? 99 : Math.max(0, (Date.now() - (c.openedAt || Date.now())) / 1000).toFixed(1)}s"></div>`;
  if (m.k === 'tune') return `<div class="bxtune"><span class="bxvinyl" id="vinyl"></span><div class="bxtbar"><i id="tuneBar"></i></div>${G.bx.solo ? '' : '<button class="btn btn-ghost btn-sm" data-bx="replay">▶ Play again</button>'}</div>`;
  return '';
}
let bxTuneKey = '';
function bxQuestionHtml(reveal) {
  const b = G.bx, c = b.cur, ans = c.mode === 'host' ? null : bxVoteCounts(), tm = b.teams[c.by], org = b.teams[c.origin];
  const colors = ['#e21b3c', '#1368ce', '#d89e00', '#26890c'];
  let opts = '';
  if (c.q.opts) opts = `<div class="bxopts">${c.q.opts.map((o, i) => { const bar = ans?.bars[i], locked = c.locked === i, rt = reveal && o.ok; return `<div class="bxopt ${locked ? 'lock' : ''} ${reveal ? (o.ok ? 'right' : locked ? 'wrongpick' : 'dim') : ''}" style="--oc:${colors[i % 4]}"><i class="bxbar" style="width:${bar && !reveal ? bar.p : 0}%"></i><span class="bxot">${esc(o.t)}</span>${bar && !reveal && ans.n ? `<b>${bar.p}%</b>` : ''}${rt ? '<b>✔</b>' : ''}</div>`; }).join('')}</div>`;
  else opts = `<div class="bxtype">${reveal ? '' : ans && ans.n ? ans.bars.slice(0, 5).map((x) => `<div class="bxopt" style="--oc:#1368ce"><i class="bxbar" style="width:${x.p}%"></i><span class="bxot">${esc(x.t)}</span><b>${x.p}%</b></div>`).join('') : '<div class="bxwait">⌨️ Type your answer on your phone</div>'}${c.locked !== undefined && !c.q.opts ? `<div class="bxlocked">🔒 Locked in: <b>${esc(String(c.locked))}</b></div>` : ''}</div>`;
  const status = c.mode === 'host' ? (c.sub === 'revealed' ? `🎤 The answer is… ${esc(bxRightText(c))}. Host: how did you do?` : '🎤 Host, you answer this one! Say it out loud.')
    : reveal ? '' : c.locked !== undefined ? `🔒 ${esc(tm.name)}'s captain has locked in an answer` : `${tm.emoji} ${esc(tm.name)}: ${ans.n} of ${ans.of} have picked${c.mode === 'made' ? ` · ${org.emoji} ${esc(org.name)} made them answer` : ''}`;
  const tags = `<span class="bxtag">Box ${c.num}</span><span class="bxtag">${esc(b.cats[c.cat].e)} ${esc(b.cats[c.cat].n)}</span><span class="bxtag gold">🎲 ${bxN(c.stake)} at stake${c.dbl ? ' · ⚡ ×4' : ''}</span>${(c.used || []).filter((u) => u !== 'double').map((u) => `<span class="bxtag">${BX_POWERS[u].icon} ${BX_POWERS[u].name}</span>`).join('')}`;
  return `<div class="bxq"><div class="bxtags">${tags}</div><h1 class="bxqt">${esc(c.q.t)}</h1>${bxMediaHtml(c, reveal)}${opts}<div class="bxstatus">${status}</div>${c.note ? `<div class="bxnote">${esc(c.note)}</div>` : ''}</div>`;
}
function bxRender() {
  const b = G.bx; if (!b) return;
  bxLoanPopHost();
  bxSync();
  let main = '';
  const t = b.teams[b.turn], c = b.cur;
  if (b.step === 'teams') main = `<div class="bxhero"><h1 class="big">📦 Box Clever</h1><p class="bxsub">${bxPids().length} players · ${b.teams.length} teams · ${b.total} boxes · ${bxN(b.start)} each to start</p><div class="bxteamlist">${b.teams.map((tt) => `<div class="bxtl" style="--tc:${tt.color}"><h2>${tt.emoji} ${esc(tt.name)}</h2><div>${tt.members.map((m) => `<span class="bxmem">${pem(m)} ${esc(pname(m))}</span>`).join('')}</div></div>`).join('')}</div></div>`;
  else if (b.step === 'vote') main = `<div class="bxhero"><h1 class="big">👑 Vote for your captain</h1><p class="bxsub">On your phone: tap the teammate who should have the final say. The captain's phone gets the deciding vote on everything.</p><div class="bxteamlist">${b.teams.map((tt) => { const done = tt.members.filter((m) => b.votes[m]).length; return `<div class="bxtl" style="--tc:${tt.color}"><h2>${tt.emoji} ${esc(tt.name)}</h2><div class="bxdone">${done} of ${tt.members.length} voted</div></div>`; }).join('')}</div></div>`;
  else if (b.step === 'captains') main = `<div class="bxhero"><h1 class="big">👑 Your captains</h1><div class="bxteamlist">${b.teams.map((tt) => `<div class="bxtl" style="--tc:${tt.color}"><h2>${tt.emoji} ${esc(tt.name)}</h2>${tt.spin?.tie ? `<div class="bxspin" data-at="${tt.spin.at}" data-cands="${esc(JSON.stringify(tt.spin.cands.map(pname)))}" data-win="${esc(pname(tt.captain))}"><span class="bxspinw">…</span><small>It's a tie: the spinner decides</small></div>` : `<div class="bxcapname">👑 ${pem(tt.captain)} ${esc(pname(tt.captain))}</div>`}</div>`).join('')}</div></div>`;
  else if (b.step === 'seg') main = `<div class="bxhero"><h1 class="big">${b.part === 1 ? 'Ready?' : '💰 Bonus round points'}</h1>${b.part > 1 ? `<div class="bxteamlist">${b.teams.map((tt) => { const d = (b.lastAbsorb || {})[tt.i] || 0; return `<div class="bxtl" style="--tc:${tt.color}"><h2>${tt.emoji} ${esc(tt.name)}</h2><div class="bxcapname">${d >= 0 ? '+' : '−'}${bxN(Math.abs(d))}</div><small>now ${bxN(tt.pot)}</small></div>`; }).join('')}</div>` : '<p class="bxsub">First up: ' + esc(t.name) + '</p>'}</div>`;
  else if (b.step === 'pick') { const pt = b.teams[bxPickTeam()]; main = `<div class="bxturn" style="--tc:${pt.color}">${pt.i !== b.turn ? `👈 ${pt.emoji} ${esc(pt.name)} choose ${t.emoji} ${esc(t.name)}'s box!` : `${pt.emoji} ${esc(pt.name)}: ${pt.captain ? esc(pname(pt.captain)) + ', ' : ''}pick a box`}</div>${b.pickNote ? `<div class="bxnote">${esc(b.pickNote)}</div>` : ''}${bxCabinet()}`; }
  else if (b.step === 'stake') main = `<div class="bxturn" style="--tc:${t.color}">${t.emoji} ${esc(t.name)} picked box ${c.num} · ${esc(b.cats[c.cat].e)} ${esc(b.cats[c.cat].n)}${c.noPass ? ' · 👀 already seen once: no passing' : ''}</div><div class="bxnote">🎲 ${t.captain ? esc(pname(t.captain)) : 'The captain'} is deciding how much to gamble · ${bxN(t.pot)} in the pot</div>${bxCabinet()}`;
  else if (b.step === 'open') main = `<div class="bxturn" style="--tc:${t.color}">${t.emoji} ${esc(t.name)} · box ${c.num} · ${esc(b.cats[c.cat].e)} ${esc(b.cats[c.cat].n)} · 🎲 ${bxN(c.stake)}${c.dbl ? ' ⚡×4' : ''}</div><div class="bxnote">Host: click the glowing drawer to open it</div>${bxCabinet()}`;
  else if (b.step === 'ask' || b.step === 'locked') main = bxCabinet() + bxPaper(bxQuestionHtml(c.mode === 'host' && c.sub === 'revealed'));
  else if (b.step === 'result') {
    const r = c.res, tt = b.teams[r.team];
    const inner = r.passed
      ? `<div class="bxresult pass"><div class="bxbig">🏳️ Passed</div><div class="bxrans">${esc(c.q.t)}<br><small>Everyone has seen this one. The box goes back, and whoever takes it next can't pass it.</small></div><div class="bxdelta" style="--tc:${tt.color}">${tt.emoji} ${esc(tt.name)} −${bxN(Math.abs(r.delta))} → ${bxN(tt.pot)}</div>${r.broke ? bxBrokeNote(tt) : ''}</div>`
      : `<div class="bxresult ${r.ok ? 'ok' : 'no'}"><div class="bxbig">${r.ok ? '✅ Correct!' : '❌ Wrong!'}</div>${bxMediaHtml(c, true)}<div class="bxrans">${esc(c.q.t)}<br><b>${esc(r.right)}</b></div>${r.said ? `<div class="bxsaid">${esc(tt.name)} said: ${esc(String(r.said))}</div>` : ''}<div class="bxdelta" style="--tc:${tt.color}">${tt.emoji} ${esc(tt.name)} ${r.delta >= 0 ? '+' : '−'}${bxN(Math.abs(r.delta))} → ${bxN(tt.pot)}</div>${r.broke ? bxBrokeNote(tt) : ''}${!c.q.opts ? '<button class="btn btn-ghost btn-sm" data-bx="flip">↺ Mark it the other way</button>' : ''}</div>`;
    main = bxCabinet() + bxPaper(inner);
  }
  const cutLeft = b.cuts[b.part - 1] - b.asked;
  stage.innerHTML = `${topBar(`<div class="pillbox"><span class="hpill">📦 ${b.asked} of ${b.total} boxes</span>${b.step !== 'teams' ? `<span class="hpill">${cutLeft > 0 ? cutLeft + ' to the bonus round' : 'bonus round next'}</span>` : ''}</div>`)}
    <div class="stage-main bxstage">${b.step === 'teams' || b.step === 'vote' || b.step === 'captains' ? '' : bxStrip()}${main}</div>
    ${hostBar(`<button class="btn btn-ghost" data-act="end">End game</button>${bxNextBtn()}`)}`;
  const go = $('#bxGo') || $('#bxReveal'); if (go) go.onclick = bxClickGo;
  $$('.bxdr.sel').forEach((el) => el.onclick = () => { if (G.bx.step === 'open') bxOpen(); });
  const paper = $('.bxpaper'), drawer = $('.bxdr.out');
  if (paper && paper.classList.contains('fresh')) { // unfold from the drawer: measure where it is, then let it run
    if (drawer) { const a = drawer.getBoundingClientRect(), o = paper.getBoundingClientRect(); paper.style.setProperty('--dx', (a.left + a.width / 2 - (o.left + o.width / 2)) + 'px'); paper.style.setProperty('--dy', (a.top + a.height / 2 - (o.top + o.height / 2)) + 'px'); }
    paper.style.animationPlayState = 'running'; bxAnimDone = paper.dataset.key;
  }
  bind(); bxSpin();
  if (b.solo && !bxAutoI) bxAutoI = setInterval(bxAuto, 400);
  const tm = c?.q?.m, tkey = tm?.k === 'tune' && !b.solo && (b.step === 'ask' || b.step === 'locked') ? c.num + ':' + c.openedAt + ':' + tm.url : '';
  if (tkey && bxTuneKey !== tkey) { bxTuneKey = tkey; playTune({ media: { url: tm.url, start: tm.start || 0, length: tm.len || 15 } }); }
  else if (!tkey && bxTuneKey) { bxTuneKey = ''; stopTune(); }
}
/** The spinner: runs through the tied names, slowing down, and lands on the winner. */
function bxSpin() {
  $$('.bxspin').forEach((el) => {
    if (el.dataset.ran) return; el.dataset.ran = '1';
    const names = JSON.parse(el.dataset.cands), win = el.dataset.win, out = el.querySelector('.bxspinw');
    if (Date.now() - (+el.dataset.at || 0) > 9000) { out.textContent = '👑 ' + win; out.classList.add('landed'); return; } // redrawn after it landed: show the result
    let i = 0, delay = 60, n = 0; const total = 22 + Math.floor(Math.random() * 6);
    const step = () => { i++; n++; const last = n >= total; out.textContent = last ? '👑 ' + win : names[i % names.length]; out.classList.toggle('landed', last); if (last) { sound('ding'); return; } delay *= 1.12; setTimeout(step, delay); };
    setTimeout(step, 500);
  });
}
/** The teams' pots with any bonus round points not yet banked counted in (the between-rounds scoreboard). */
function bxProjected() {
  const b = G.bx, add = {};
  for (const p of Object.values(G.players)) { const ti = bxTeamOf(p.id); if (ti >= 0 && !b.finalDone) add[ti] = (add[ti] || 0) + (p.score - (b.snap[p.id] ?? p.score)); }
  return b.teams.map((t) => { const pot = Math.max(0, t.pot + (add[t.i] || 0)); return { t, add: add[t.i] || 0, pot, loan: t.loan || 0, net: pot - (t.loan || 0) }; }).sort((x, y) => y.net - x.net);
}
function bxScoreboard() {
  const rows = bxProjected(), top = Math.max(1, rows[0].net);
  stage.innerHTML = `${topBar()}<div class="stage-main"><h1 class="big" style="font-size:2.6rem">📦 Team pots</h1><div class="board">${rows.map((r, i) => `<div class="brow"><div class="fill" data-w="${(Math.max(0, r.net) / top) * 100}" style="background:${r.t.color}"></div><div class="rank">${i + 1}</div><div>${r.t.emoji} ${esc(r.t.name)}<small style="opacity:.7"> · ${esc(r.t.members.map(pname).join(', '))}</small>${r.add ? `<span class="delta" ${r.add < 0 ? 'style="color:#ffb3c0"' : ''}>${r.add > 0 ? '+' : ''}${bxN(r.add)} bonus</span>` : ''}</div><div>${bxN(r.net)}${r.loan ? `<small style="display:block;opacity:.7;font-size:.5em">after repaying 🏦 ${bxN(r.loan)}</small>` : ''}</div></div>`).join('')}</div></div>
    ${hostBar(`<button class="btn btn-ghost" data-act="end">End game</button><button class="btn btn-primary" data-act="primary">${G.qIndex + 1 < G.quiz.questions.length ? 'Next ▶' : 'Final results 🏆'}</button>`)}`;
  requestAnimationFrame(() => $$('.fill').forEach((f) => f.style.width = f.dataset.w + '%'));
  bind();
}
const bxBrokeNote = (t) => `<div class="bxnote">💸 ${esc(t.name)} went bankrupt! They are on 0 until their next go, when the bank lends ${bxN(BX_LOAN)} to carry on. It comes off the final score.</div>`;
function bxFinalHtml() {
  const rows = bxProjected();
  return `<h1 class="big" style="font-size:2.8rem">🏆 ${rows[0].t.emoji} ${esc(rows[0].t.name)} win!</h1><div class="bxteamlist">${rows.map((r, i) => `<div class="bxtl" style="--tc:${r.t.color};${i === 0 ? 'transform:scale(1.08)' : ''}"><h2>${['🥇', '🥈', '🥉', '4.'][i] || i + 1 + '.'} ${r.t.emoji} ${esc(r.t.name)}</h2><div class="bxcapname">${bxN(r.net)}</div>${r.loan ? `<small>after repaying 🏦 ${bxN(r.loan)} borrowed</small>` : ''}<div>${r.t.members.map((m) => `<span class="bxmem">${pem(m)} ${esc(pname(m))}${m === r.t.captain ? ' 👑' : ''}</span>`).join('')}</div></div>`).join('')}</div>`;
}
/** The last screen: every player carries their team's pot, so the usual final results rank the teams. */
function bxFinal() {
  const b = G.bx; if (!b || b.finalDone) return; b.finalDone = true;
  bxAbsorb();
  for (const p of Object.values(G.players)) { const ti = bxTeamOf(p.id); if (ti >= 0) p.score = bxNet(b.teams[ti]); }
  b.winner = b.teams.slice().sort((x, y) => bxNet(y) - bxNet(x))[0]?.i;
  persist();
}

/** The bank's pop-up on the big screen (a hosted game; on one phone the phone shows it). */
let bxLoanSeenHost = 0;
function bxLoanPopHost() {
  const b = G.bx, n = b?.loanNote; if (!n || b.solo || bxLoanSeenHost === n.at || Date.now() - n.at > 15000 || $('#bxLoanH')) return;
  const t = b.teams[n.team]; if (!t) return; bxLoanSeenHost = n.at;
  const d = document.createElement('div'); d.id = 'bxLoanH'; d.className = 'bxloan';
  d.innerHTML = `<div class="bxloancard"><div class="em">🏦</div><h2>${esc(t.emoji)} ${esc(t.name)}</h2><p>went bankrupt, so the bank lends them <b>${bxN(BX_LOAN)}</b> points to carry on.</p><p class="muted">It comes off their final score.</p></div>`;
  document.body.appendChild(d); try { sound('ding'); } catch {} setTimeout(() => d.remove(), 6000);
}

// ---------------------------------------------------------------- bots (test games and the warm-up)
/** Each bot is given a risk factor when it first has to bet: 0 is cautious (the small stakes), 1 is bold (big stakes, all in). A quarter of
 *  them are "mixers" whose stakes could be anything. Risky bots double up more often and pass less. */
function bxRisk(pid) {
  const b = G.bx, own = (G.bots || []).find((x) => x.pid === pid)?.risk; if (own) return own; // a bot with a set nature keeps it
  b.risk = b.risk || {};
  if (!b.risk[pid]) b.risk[pid] = { r: Math.round(Math.random() * 100) / 100, s: chance(0.25) ? 0.6 : 0.2 };
  return b.risk[pid];
}
function bxBotStake(pid, pot) {
  const st = bxStakes(pot), k = bxRisk(pid), w = st.map((_, i) => Math.exp(-Math.pow(i / Math.max(1, st.length - 1) - k.r, 2) / (2 * k.s * k.s)));
  let x = Math.random() * w.reduce((a, c) => a + c, 0), i = 0;
  for (; i < w.length - 1; i++) { x -= w[i]; if (x <= 0) break; }
  return st[i];
}
/** A number from 0 to 1 that depends only on the two strings, so it comes out the same in every game. */
function bxHash(a, b) {
  let h = 2166136261; for (const ch of a + '|' + b) { h ^= ch.charCodeAt(0); h = Math.imul(h, 16777619); }
  h ^= h >>> 13; h = Math.imul(h, 0x5bd1e995); h ^= h >>> 15; return (h >>> 0) / 4294967296;
}
function bxBots() {
  const b = G.bx; if (!b || !(G.bots || []).length) return;
  const bot = (pid) => (G.bots || []).some((x) => x.pid === pid), sp = b.solo ? 0.45 : 1; // on one phone the bots do not dawdle
  const later = (fn, ms) => botLater(() => { if (G.bx === b) fn(); }, ms * sp);
  const step = b.step, c = b.cur;
  const skill = (m) => G.bots.find((x) => x.pid === m)?.skill ?? 0.5;
  const botOf = (m) => G.bots.find((x) => x.pid === m);
  // A bot with a set nature (the warm-up's rivals) has a fixed result for every question, the same in every game: it either knows that one or
  // it does not, whatever it does with its powers. The same goes for which wrong answer it gives.
  const knows = (m, c) => { const bt = botOf(m); return bt?.fixed ? bxHash(bt.name, c.q.id) < 0.35 + bt.skill * 0.5 : chance(0.35 + skill(m) * 0.5); };
  const guess = (m, c) => {
    const right = knows(m, c), fixed = botOf(m)?.fixed;
    if (c.q.opts) {
      if (right) return c.q.opts.findIndex((o) => o.ok);
      const wrong = c.q.opts.map((o, i) => ({ o, i })).filter((x) => !x.o.ok);
      return (fixed ? wrong.sort((x, y) => bxHash(botOf(m).name, x.o.t) - bxHash(botOf(m).name, y.o.t))[0] : partyPick(wrong)).i;
    }
    return right ? c.q.answers[0] : fixed ? 'No idea' : partyPick(['No idea', 'Pass', 'Dunno']);
  };
  if (step === 'vote') for (const t of b.teams) for (const m of t.members) if (bot(m)) later(() => bxAnswer(m, { bx: 'v', k: 'cap', v: partyPick(t.members) }), rnd(1000, 4000));
  if (step === 'pick') { const t = b.teams[bxPickTeam()], open = () => b.board.map((x, i) => x.st === 'open' ? i + 1 : 0).filter(Boolean); if (bot(t.captain)) later(() => { if (b.step === 'pick') bxAnswer(t.captain, { bx: 'v', k: 'pick', v: partyPick(open()), go: true }); }, rnd(2500, 6000)); }
  if (step === 'stake') { const t = b.teams[b.turn]; if (bot(t.captain)) later(() => { if (b.step === 'stake') { bxAnswer(t.captain, { bx: 'v', k: 'stake', v: bxBotStake(t.captain, t.pot), dbl: chance(0.03 + 0.2 * bxRisk(t.captain).r), go: true }); } }, rnd(2000, 5000)); }
  if (step === 'ask' && c && c.mode !== 'host') {
    const t = b.teams[c.by];
    if (!b.solo) for (const m of t.members) if (bot(m)) later(() => {
      if (b.step !== 'ask' || b.cur !== c) return;
      bxAnswer(m, { bx: 'v', k: 'ans', v: guess(m, c) });
    }, rnd(2000, 7000));
    if (bot(t.captain)) later(() => {
      if (b.step !== 'ask' || b.cur !== c) return; const vs = b.votes.ans || {}, vals = Object.values(vs);
      if (c.mode === 'own' && !c.noPass && (botOf(t.captain)?.fixed ? !knows(t.captain, c) && chance(0.2 + 0.4 * (1 - bxRisk(t.captain).r)) : chance(0.2 * (1 - bxRisk(t.captain).r)))) return bxAnswer(t.captain, { bx: 'v', k: 'pass', v: 1, go: true });
      if (c.mode === 'own' && chance(0.3) && !c.used.includes('fifty') && b.teams[c.origin].powers.fifty && (!c.q.opts || c.q.opts.length > 2)) return bxAnswer(t.captain, { bx: 'v', k: 'pow', v: 'fifty', go: true });
      const v = vals.length ? vals.sort((x, y) => vals.filter((z) => z === y).length - vals.filter((z) => z === x).length)[0] : guess(t.captain, c);
      bxAnswer(t.captain, { bx: 'v', k: 'ans', v, go: true });
    }, b.solo ? rnd(3500, 7000) : rnd(8000, 12000));
  }
}

// ---------------------------------------------------------------- the warm-up: nobody is there to press the host's buttons
let bxAutoKey = '', bxAutoT = null, bxAutoI = null;
/** On one phone the host screen is hidden, so the drawer opens, the answer is revealed and a bot's result moves on by itself. The
 *  player's own result waits for their tap (a long fallback in case they have wandered off). */
function bxAuto() {
  const b = G.bx; if (!b || !b.solo) return;
  if (G.phase !== 'question') { clearTimeout(bxAutoT); bxAutoKey = ''; return; } // nothing left over from a box goes on into the next item
  const c = b.cur, key = [b.step, b.part, b.asked, c?.num, c?.mode, c?.locked !== undefined ? 1 : 0, b.closing ? 1 : 0].join();
  if (key === bxAutoKey) return; bxAutoKey = key; clearTimeout(bxAutoT);
  const at = (ms, fn) => { bxAutoT = setTimeout(() => { if (G.bx === b && bxAutoKey === key && !b.closing) fn(); }, ms); };
  const botTeam = (ti) => (G.bots || []).some((x) => x.pid === b.teams[ti]?.captain);
  if (b.step === 'open') at(1300, bxOpen);
  else if (b.step === 'locked') at(1500, bxReveal);
  else if (b.step === 'result') at(botTeam(b.cur?.res?.team ?? b.turn) ? 4500 : 30000, () => bxClose(bxNextTurn));
}
