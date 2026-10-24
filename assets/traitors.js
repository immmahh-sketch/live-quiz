/* Let's Quiz host screen: THE TRAITORS (October 2026).
 *
 * One player is secretly the Traitor, picked from the host's own phone (the 🗡 Traitors button on the quiz's card in the builder).
 * The Traitor gets a secret menu on their phone: steal points (100-1000, once every 5 questions, the same person once every 15),
 * gift a free answer, block someone from a question, double someone's points (5 of each), and send secret or whole-group messages.
 * Everyone earns a 🛡 shield by getting 3 in a row (the Traitor can't touch them for the next question). After the last question
 * before half time, 3 minutes at the Round Table, then a vote to banish the Traitor. At half time the Traitor ticks a 20 Questions
 * list about themselves, which becomes the last round: find the Traitor. See docs/traitors-guide.html (also the PDF the players get).
 *
 * Secrets never go in the shared game state: a private message ('trs') goes out for the one phone it is for. The host's phone control
 * panel talks to this screen with sealed ('trctl') messages. Hooks into host.html and party.js are small and named tr*.
 * Loaded after party.js; runs once a game exists. */

const TR = { STEAL_EVERY: 5, SAME_VICTIM: 15, MIN: 100, MAX: 1000, USES: 5, TABLE_MS: 180000, BANISH_LOSS: 5000, VOTER_BONUS: 2000, SLIP_BONUS: 2000, FINDER_BONUS: 2000, CAUGHT_LOSS: 2000, AWAY_BONUS: 5000, MSGS: 3, MSG_LEN: 140 };
const trFresh = () => ({ gift: TR.USES, block: TR.USES, dbl: TR.USES });
const trNames = (pids) => pids.map((p) => pname(p)).join(' and ').replace(/, ([^,]*)$/, ' and $1');
const trLog = (text) => { if (G.tr) { G.tr.log.push({ t: Date.now(), q: G.tr.qDone, text }); G.tr.log = G.tr.log.slice(-80); } };
const trOn = () => !!G?.tr?.on;
const trShielded = (pid) => (G.tr?.shield?.[pid] ?? -1) > (G.tr?.qDone ?? 0);

/** The mode switched on in the quiz's settings: build the traitor state once. Not in warm-ups, previews or the demo. */
function trEnsure() {
  if (G.tr || !G.quiz?.settings?.traitors?.on || WARMUP || PREVIEW || DEMO) return;
  G.tr = { on: true, traitor: null, history: [], qDone: 0, lastStealQ: -99, victimQ: {}, stolen: 0, steals: 0, powers: trFresh(), set: { gift: null, block: null, dbl: null }, used: { gift: 0, block: 0, dbl: 0 },
    streak: {}, shield: {}, notices: [], screen: null, hidden: 0, tableDone: false, votes: {}, list: null, twentyAdded: false, revealed: false, log: [], msgBreak: 0, msgs: 0, stealShown: false, banishedBefore: [] };
  persist();
}
/** The code of this live game, left on the quiz so the host's phone can find it (builder: 🗡 Traitors on the quiz's card). */
function trRegisterLive() { if (!trOn() || !G.quizId) return; api('live_set', { id: G.quizId, code: G.code }).catch(() => {}); }

// ---------------------------------------------------------------- what the phones are told
/** The public side of it, in every state broadcast: nothing here says who the Traitor is. */
function trState(s) {
  if (!trOn()) return;
  const t = G.tr, sc = t.screen;
  s.tr = { on: true, picked: !!t.traitor, window: trWindow(), qDone: t.qDone, tableDone: t.tableDone,
    players: Object.values(G.players).map((p) => ({ pid: p.id, name: p.name, emoji: p.emoji || '', score: p.score, shield: trShielded(p.id) })),
    blocked: G.phase === 'question' && G.q?.trfx?.block ? { [G.q.trfx.block]: true } : {},
    screen: sc ? trPublicScreen(sc) : null };
}
function trPublicScreen(sc) {
  const o = { id: sc.id, kind: sc.kind };
  if (sc.kind === 'notice') Object.assign(o, { title: sc.title, lines: sc.lines, quote: sc.quote || '' });
  if (sc.kind === 'table') Object.assign(o, { endsAt: sc.endsAt, total: sc.total, left: Math.max(0, sc.endsAt - (G.paused ? G.pausedAt : Date.now())), voted: Object.keys(G.tr.votes), locked: !!sc.locked });
  if (sc.kind === 'verdict') Object.assign(o, { rows: sc.rows, banished: sc.banished, correct: sc.correct, winners: sc.winners, tie: !!sc.tie });
  if (sc.kind === 'final') Object.assign(o, { traitor: sc.traitor, lines: sc.lines });
  return o;
}
/** A private word to one phone (or all of them, for ping-style banners). Only the phone it is for acts on it. */
const trTell = (to, kind, data = {}) => send('trs', { to, kind, ...data });
function trSync() {
  const t = G.tr?.traitor; if (!t || !G.players[t]) return;
  const qd = G.tr.qDone, since = qd - G.tr.lastStealQ, victims = {};
  for (const p of Object.keys(G.players)) if (p !== t) victims[p] = { shield: trShielded(p), wait: Math.max(0, TR.SAME_VICTIM - (qd - (G.tr.victimQ[p] ?? -99))), score: G.players[p].score };
  trTell(t, 'sync', { d: { powers: G.tr.powers, set: G.tr.set, canSteal: since >= TR.STEAL_EVERY, stealWait: Math.max(0, TR.STEAL_EVERY - since), victims, window: trWindow(), nextPlain: powerNextPlain() >= 0, msgsLeft: Math.max(0, TR.MSGS - G.tr.msgBreak),
    needList: G.tr.tableDone && !G.tr.list, list: G.tr.list, qDone: qd, players: Object.values(G.players).filter((p) => p.id !== t).map((p) => ({ pid: p.id, name: p.name, emoji: p.emoji || '' })) } });
}
/** A phone says hello (joining, or coming back after a drop): a Traitor is reminded who they are. */
function trOnHello(pid) { if (trOn() && G.tr.traitor === pid) { trTell(pid, 'role', { again: true, reason: G.tr.history.at(-1)?.reason, n: G.tr.history.length }); trSync(); } }

// ---------------------------------------------------------------- picking the Traitor
function trSetTraitor(pid, reason = 'picked') {
  trEnsure(); if (!trOn() || !G.players[pid]) return false;
  G.tr.traitor = pid; G.tr.history.push({ pid, at: G.tr.qDone, reason });
  Object.assign(G.tr, { powers: trFresh(), set: { gift: null, block: null, dbl: null }, used: { gift: 0, block: 0, dbl: 0 }, lastStealQ: -99, victimQ: {}, list: null, msgBreak: 0 });
  trLog(`${pname(pid)} is the Traitor (${reason})`);
  trTell(pid, 'role', { reason, n: G.tr.history.length }); trSync(); persist(); broadcastState();
  return true;
}

// ---------------------------------------------------------------- the Traitor's actions (from their phone)
/** Between questions: the same break the power cards are played in. Not while a vote or a notice is up. */
function trWindow() { return trOn() && ['round', 'slide', 'typecard', 'countdown', 'reveal', 'scoreboard'].includes(G.phase) && !(G.tr.screen && ['table', 'verdict', 'final'].includes(G.tr.screen.kind)); }
const trNo = (why) => trTell(G.tr.traitor, 'no', { why });
function onTr({ pid, op, ...a }) {
  if (!trOn() || !G.players[pid]) return;
  if (op === 'sync') { if (pid === G.tr.traitor) trSync(); return; }
  if (op === 'vote') return trVote(pid, a.target);
  if (pid !== G.tr.traitor) return;
  if (op === 'steal') return trSteal(a);
  if (op === 'power') return trPower(a);
  if (op === 'msg') return trMsg(a);
  if (op === 'list') return trList(a);
}
function trSteal({ victim, amount, to }) {
  const t = G.tr.traitor, qd = G.tr.qDone;
  if (!trWindow()) return trNo('Wait for the break between questions.');
  if (qd - G.tr.lastStealQ < TR.STEAL_EVERY) return trNo(`You can steal once every ${TR.STEAL_EVERY} questions: ${TR.STEAL_EVERY - (qd - G.tr.lastStealQ)} more to go.`);
  if (!G.players[victim] || victim === t) return trNo('Pick someone else to steal from.');
  if (!G.players[to] || to === t || to === victim) return trNo('Give the points to a different player: not yourself, and not the one you took them from.');
  if (trShielded(victim)) return trNo(`${pname(victim)} has a 🛡 shield.`);
  const wait = TR.SAME_VICTIM - (qd - (G.tr.victimQ[victim] ?? -99)); if (wait > 0) return trNo(`You can only steal from ${pname(victim)} once every ${TR.SAME_VICTIM} questions: ${wait} more to go.`);
  const want = Math.round((+amount || 0) / 100) * 100; if (want < TR.MIN || want > TR.MAX) return trNo(`Steal between ${TR.MIN} and ${TR.MAX}.`);
  const amt = Math.min(want, Math.max(0, G.players[victim].score)); if (amt <= 0) return trNo(`${pname(victim)} has no points to steal.`);
  G.players[victim].score -= amt; G.players[to].score += amt;
  G.tr.lastStealQ = qd; G.tr.victimQ[victim] = qd; G.tr.stolen += amt; G.tr.steals++;
  const afterIdx = ['reveal', 'scoreboard', 'slide'].includes(G.phase) ? G.qIndex + 1 : G.qIndex; // the question that comes next: the notice follows it
  G.tr.notices.push({ kind: 'steal', amt, first: !G.tr.stealShown, afterIdx }); G.tr.stealShown = true;
  trLog(`Stole ${amt} from ${pname(victim)} and gave it to ${pname(to)}`);
  trTell(t, 'ok', { text: `🗡 Done: ${amt} points taken from ${pname(victim)} and given to ${pname(to)}.` });
  trSync(); persist(); broadcastState(); if (['reveal', 'scoreboard'].includes(G.phase)) render();
}
function trPower({ kind, target }) {
  const t = G.tr.traitor; if (!['gift', 'block', 'dbl'].includes(kind)) return;
  if (!trWindow()) return trNo('Pick before the question starts, in the break.');
  if (powerNextPlain() < 0) return trNo('There is no everyone-answers question left to use it on.');
  if (target === null || target === undefined || target === '') { G.tr.set[kind] = null; trSync(); persist(); return trTell(t, 'ok', { text: 'Taken back: it is not used.' }); }
  if (!G.players[target]) return;
  if (G.tr.powers[kind] <= 0) return trNo('You have none of those left.');
  for (const k of ['gift', 'block', 'dbl']) if (k !== kind && G.tr.set[k] === target) return trNo(`${pname(target)} already has something from you for the next question.`);
  if (kind === 'block' && target !== t && trShielded(target)) return trNo(`${pname(target)} has a 🛡 shield: you can't block them.`);
  G.tr.set[kind] = target; trSync(); persist();
  trTell(t, 'ok', { text: { gift: `🎁 ${target === t ? 'You' : pname(target)} will get a free answer on the next question.`, block: `🚫 ${target === t ? 'You' : pname(target)} will be blocked from the next question.`, dbl: `✨ ${target === t ? 'Your' : pname(target) + "'s"} points will be doubled on the next question.` }[kind] });
}
function trMsg({ to, text }) {
  const t = G.tr.traitor, msg = String(text || '').replace(/\s+/g, ' ').trim().slice(0, TR.MSG_LEN);
  if (!msg) return trNo('Write a message first.');
  if (G.tr.msgBreak >= TR.MSGS) return trNo(`That's ${TR.MSGS} messages for this break. Wait for the next question.`);
  if (to !== 'all' && (!G.players[to] || to === t)) return trNo('Pick someone to send it to.');
  G.tr.msgBreak++; G.tr.msgs++;
  if (to === 'all') { trPushNotice({ kind: 'notice', title: '📜 A MESSAGE FROM THE TRAITOR', quote: msg, lines: ['Can you work out who it is?'], afterIdx: 0 }, true); trLog(`Message to everyone: ${msg}`); }
  else { trTell(to, 'msg', { text: msg }); trLog(`Secret message to ${pname(to)}: ${msg}`); }
  trTell(t, 'ok', { text: to === 'all' ? '📜 Sent to everyone.' : `🤫 Sent to ${pname(to)}.` }); trSync(); persist();
}
function trList({ items }) {
  if (!Array.isArray(items)) return;
  const list = items.map((x, i) => ({ id: 'c' + (i + 1), text: String(x.text || '').trim().slice(0, 90), yes: !!x.yes, own: !!x.own })).filter((x) => x.text).slice(0, 90);
  if (list.filter((x) => x.yes).length < 3) return trNo('Tick at least 3 that are true of you.');
  G.tr.list = list; trLog(`The Traitor's 20 Questions list is in (${list.length} questions)`); trTell(G.tr.traitor, 'ok', { text: '✅ Your list is saved. Honesty is the whole game!' }); trSync(); persist();
}
/** A notice for the screen (and the phones): up at once if the game is between questions, else when it next pauses. */
function trPushNotice(n, now) {
  G.tr.notices.push(n);
  if (now && G.phase !== 'question' && G.phase !== 'grading' && !G.tr.screen) trInterlude(true);
  persist(); broadcastState();
}

// ---------------------------------------------------------------- the questions: powers land, answers are changed, shields are earned
function trStartQuestion(q) {
  if (!trOn()) return;
  G.tr.msgBreak = 0;
  if (!partyPlain(q)) return; // the powers wait for the next everyone-answers question
  const set = G.tr.set, fx = {};
  for (const k of ['gift', 'block', 'dbl']) if (set[k] && G.players[set[k]]) { fx[k] = set[k]; G.tr.powers[k]--; G.tr.used[k]++; }
  G.tr.set = { gift: null, block: null, dbl: null };
  if (fx.gift && fx.gift !== G.tr.traitor) trTell(fx.gift, 'ping', { icon: '🎁', text: 'The traitor has gifted you full points for this question!' });
  if (fx.block && fx.block !== G.tr.traitor) trTell(fx.block, 'ping', { icon: '🚫', text: 'The traitor has blocked you from this question.' });
  if (fx.dbl && fx.dbl !== G.tr.traitor) trTell(fx.dbl, 'ping', { icon: '✨', text: 'The traitor has doubled your points on this question!' });
  if (Object.keys(fx).length) { G.q.trfx = fx; trLog(`Used for this question: ${Object.entries(fx).map(([k, p]) => `${{ gift: 'free answer', block: 'block', dbl: 'double' }[k]} on ${pname(p)}`).join(', ')}`); }
  trSync();
}
/** A blocked player can't answer (party.js partyBlocks asks). */
const trBlocked = (pid) => G.q?.trfx?.block === pid;
function trAfterGrade(byPlayer) {
  if (!trOn()) return;
  const q = question(), blank = () => ({ answered: false, correct: false, partial: 0, points: 0 });
  if (q.trTwenty) return trAfterTwenty(byPlayer);
  if (practiceQ()) return;
  G.tr.qDone++; // every question that scores counts toward the Traitor's waits
  if (!partyPlain(q)) return trSync();
  const fx = G.q.trfx || {}, full = Math.round(+G.quiz.settings.maxPoints || 1000);
  // streaks and shields count what people really answered, before the Traitor's gifts
  for (const pid of Object.keys(G.players)) {
    const r = byPlayer[pid], right = !!r?.correct && !r.frozen && fx.block !== pid;
    G.tr.streak[pid] = right ? (G.tr.streak[pid] || 0) + 1 : 0;
    if (G.tr.streak[pid] >= 3) { G.tr.streak[pid] = 0; G.tr.shield[pid] = G.tr.qDone + 1; trTell(pid, 'ping', { icon: '🛡', text: "Shield earned! The traitor can't touch you for the next question." }); }
  }
  if (fx.block) { const r = byPlayer[fx.block] = byPlayer[fx.block] || blank(); r.points = 0; r.correct = false; r.partial = 0; r.blocked = true; partyNote(r, '🚫 The Traitor blocked you from this question'); }
  if (fx.gift) { const r = byPlayer[fx.gift] = byPlayer[fx.gift] || blank(); r.answered = true; r.points = Math.max(r.points || 0, full); r.correct = true; r.partial = 1; partyNote(r, '🎁 The Traitor gifted you full points!'); }
  if (fx.dbl) { const r = byPlayer[fx.dbl] = byPlayer[fx.dbl] || blank(); if (r.points > 0) { r.points *= 2; partyNote(r, '✨ The Traitor doubled your points!'); } else partyNote(r, '✨ Doubled… but double nothing is nothing'); }
  if (fx.gift || fx.block || fx.dbl) {
    const lines = [];
    if (fx.gift) lines.push(`🎁 ${pname(fx.gift)} was gifted a free answer: full points whatever they said.`);
    if (fx.block) lines.push(`🚫 ${pname(fx.block)} was blocked from that question.`);
    if (fx.dbl) lines.push(`✨ ${pname(fx.dbl)}'s points were doubled.`);
    G.tr.notices.push({ kind: 'notice', title: '🗡 THE TRAITOR WAS BUSY…', lines, quote: '', afterIdx: 0, sound: 'whoosh' });
  }
  trSync();
}

// ---------------------------------------------------------------- the game pauses: notices up on the host screen and the phones
/** After a question (reveal, scoreboard): a waiting notice goes up. Returns true if it did. */
function trInterlude(now) {
  if (!trOn() || G.tr.screen) return false;
  const i = G.tr.notices.findIndex((n) => now ? true : (n.afterIdx || 0) <= G.qIndex);
  if (i < 0) return false;
  const n = G.tr.notices.splice(i, 1)[0];
  if (n.kind === 'steal') {
    n.title = n.first ? '🗡 A TRAITOR AMONG YOU' : '🗡 THE TRAITOR HAS STRUCK AGAIN';
    n.lines = n.first
      ? [`At the start of tonight's quiz… a "Traitor" was selected.`, `The Traitor just stole ${n.amt.toLocaleString('en-GB')} points from a player and gave them to another player…`, `At half time you will have the chance to "banish" who you think the Traitor is. If you're right, that person loses their power and 5,000 points, and everyone who voted for them wins 2,000.`]
      : [`${n.amt.toLocaleString('en-GB')} points were stolen from one player and given to another…`, `Who is the Traitor? You'll get your chance to banish them at half time.`];
    n.sound = 'caught';
  }
  G.tr.screen = { id: uid('s'), kind: 'notice', title: n.title, lines: n.lines || [], quote: n.quote || '', cont: !now };
  persist(); sound(n.sound || 'gong'); render(); broadcastState();
  return true;
}
/** The host presses Next on a Traitors screen. */
function trScreenNext() {
  const sc = G.tr.screen; if (!sc) return false;
  if (sc.kind === 'notice') { G.tr.screen = null; persist(); broadcastState(); if (sc.cont) nextFrom(G.qIndex); else render(); return true; }
  if (sc.kind === 'table') { trLockVotes(); return true; }
  if (sc.kind === 'verdict') { G.tr.screen = null; G.tr.tableDone = true; persist(); trSync(); broadcastState(); goTo(sc.next); return true; }
  if (sc.kind === 'final') { G.tr.screen = null; G.tr.revealed = true; persist(); broadcastState(); finish(); return true; }
  return false;
}

// ---------------------------------------------------------------- half time: the Round Table and the vote
/** Item index of half time: the first break slide, else the middle of the quiz. */
function trHalfIndex() { const qs = G.quiz.questions, b = qs.findIndex((x) => x.type === 'slide' && x.break); return b >= 0 ? b : Math.floor(qs.length / 2); }
const trWantsTable = (i) => trOn() && G.tr.traitor && !G.tr.tableDone && trHalfIndex() === i + 1 && i + 1 < G.quiz.questions.length;
let trTickT = null;
function trTable(i) {
  clearInterval(tickT); clearInterval(countT);
  G.tr.votes = {}; G.tr.screen = { id: uid('s'), kind: 'table', endsAt: Date.now() + TR.TABLE_MS, total: TR.TABLE_MS, next: i + 1 };
  persist(); sound('drumroll'); render(); broadcastState(); trStartTick();
  for (const b of G.bots || []) botLater(() => { const sc = G.tr?.screen; if (sc?.kind !== 'table' || sc.locked) return; const others = Object.keys(G.players).filter((p) => p !== b.pid); trVote(b.pid, chance(0.45) && G.tr.traitor !== b.pid ? G.tr.traitor : others[Math.floor(Math.random() * others.length)]); }, rnd(15000, 150000));
}
function trStartTick() {
  clearInterval(trTickT);
  trTickT = setInterval(() => {
    const sc = G.tr?.screen; if (sc?.kind !== 'table') { clearInterval(trTickT); trTickT = null; return; }
    if (G.paused) return;
    const left = Math.max(0, sc.endsAt - Date.now()), c = document.getElementById('trClock'); if (c) c.textContent = `${Math.floor(left / 60000)}:${String(Math.floor(left / 1000) % 60).padStart(2, '0')}`;
    if (left <= 0 && !sc.locked) trLockVotes();
  }, 250);
}
function trVote(pid, target) {
  const sc = G.tr?.screen; if (sc?.kind !== 'table' || sc.locked || !G.players[pid] || !G.players[target] || target === pid) return;
  G.tr.votes[pid] = target; persist(); broadcastState();
  const n = document.getElementById('trVoted'); if (n) n.textContent = `${Object.keys(G.tr.votes).length} of ${Object.keys(G.players).length} have voted`;
}
/** The votes are in: count them, and the points move (the Traitor's own bonus is held back until the end). */
function trLockVotes() {
  const sc = G.tr.screen; if (sc?.kind !== 'table' || sc.locked) return;
  sc.locked = true; clearInterval(trTickT); trTickT = null;
  const count = {}; for (const t of Object.values(G.tr.votes)) count[t] = (count[t] || 0) + 1;
  const rows = Object.entries(count).map(([pid, n]) => ({ pid, n })).sort((a, b) => b.n - a.n), tie = rows.length > 1 && rows[0].n === rows[1].n;
  const banished = rows.length && !tie ? rows[0].pid : null, traitor = G.tr.traitor, correct = banished && banished === traitor;
  let winners = [];
  if (correct) {
    G.players[traitor].score -= TR.BANISH_LOSS;
    winners = Object.entries(G.tr.votes).filter(([v, t]) => t === traitor && v !== traitor).map(([v]) => v);
    for (const v of winners) G.players[v].score += TR.VOTER_BONUS;
    G.tr.banishedBefore.push(traitor); trLog(`${pname(traitor)} was banished (right!): -${TR.BANISH_LOSS}, ${winners.length} voters +${TR.VOTER_BONUS}`);
    trTell(traitor, 'banished', { text: `You were banished! You lose your power and ${TR.BANISH_LOSS.toLocaleString('en-GB')} points.` });
    const pool = Object.keys(G.players).filter((p) => p !== traitor); const next = pool[Math.floor(Math.random() * pool.length)];
    trSetTraitor(next, 'new');
  } else { G.tr.hidden += TR.SLIP_BONUS; trLog(`The vote missed (${banished ? pname(banished) : 'a tie'}): ${TR.SLIP_BONUS} held back for the Traitor`); }
  sc.kind = 'verdict'; Object.assign(sc, { rows, banished, correct: !!correct, winners, tie, locked: true });
  persist(); sound(correct ? 'fanfare' : 'trombone'); render(); broadcastState(); if (correct) confetti();
}

// ---------------------------------------------------------------- the last round: the Traitor's 20 Questions
/** nextFrom's turn: after the last item, add the Traitor's 20 Questions, then the reveal. Returns true if it took over. */
function trEnd() {
  if (!trOn() || !G.tr.traitor) return false;
  if (!G.tr.twentyAdded && G.tr.list?.length) {
    G.tr.twentyAdded = true;
    const last = G.quiz.questions[G.quiz.questions.length - 1], nm = pname(G.tr.traitor), q = LQ.newQuestion('twenty', G.quiz.settings);
    Object.assign(q, { text: '🗡 The Traitor\'s 20 Questions: who is the Traitor?', answers: [nm, nm.split(/\s+/)[0]], what: 'c_kind', customKind: { text: 'Is it one of tonight\'s players?' }, skipKind: true, trTwenty: true, trBonus: TR.FINDER_BONUS,
      custom: G.tr.list.map((x) => ({ ...x })), prize: 0, prize2: 0, prize3: 0, penalty: 0, maxQ: 20, time: 600, round: last?.round });
    G.quiz.questions.push(q); persist();
    return goTo(G.quiz.questions.length - 1), true;
  }
  if (!G.tr.revealed && !G.tr.screen) { trShowFinal(); return true; }
  return false;
}
function trAfterTwenty(byPlayer) {
  const t = G.tr.traitor, tq = G.q.tq?.players || {}, others = Object.keys(G.players).filter((p) => p !== t);
  const right = others.filter((p) => tq[p]?.done), most = right.length > others.length / 2;
  const r = byPlayer[t] = byPlayer[t] || { answered: false, correct: false, partial: 0, points: 0 };
  if (most) { r.points -= TR.CAUGHT_LOSS; partyNote(r, `🗡 Found out by most of the room: −${TR.CAUGHT_LOSS.toLocaleString('en-GB')}`); }
  else { G.tr.hidden += TR.AWAY_BONUS; }
  G.tr.found = { right, most };
  trLog(`20 Questions: ${right.length} of ${others.length} found the Traitor. ${most ? 'Caught' : 'Got away with it'}`);
}
function trShowFinal() {
  const t = G.tr.traitor, f = G.tr.found, lines = [];
  lines.push(`Over the night: ${G.tr.steals} steal${G.tr.steals === 1 ? '' : 's'}, ${G.tr.stolen.toLocaleString('en-GB')} points taken in all.`);
  const u = G.tr.used; lines.push(`🎁 ${u.gift} free answer${u.gift === 1 ? '' : 's'} · 🚫 ${u.block} block${u.block === 1 ? '' : 's'} · ✨ ${u.dbl} double${u.dbl === 1 ? '' : 's'} · 📜 ${G.tr.msgs} message${G.tr.msgs === 1 ? '' : 's'}.`);
  if (G.tr.banishedBefore.length) lines.push(`${trNames(G.tr.banishedBefore)} ${G.tr.banishedBefore.length === 1 ? 'was' : 'were'} banished at half time.`);
  if (f) lines.push(f.most ? `Most of the room worked it out: caught, and they lose ${TR.CAUGHT_LOSS.toLocaleString('en-GB')}.` : `Most of the room never worked it out: they get away with it, plus a ${TR.AWAY_BONUS.toLocaleString('en-GB')} bonus.`);
  if (G.tr.hidden && !f?.most) lines.push(`Their secret bonuses, ${G.tr.hidden.toLocaleString('en-GB')} points, are added now.`);
  G.tr.screen = { id: uid('s'), kind: 'final', traitor: t, lines };
  persist(); sound('fanfare'); render(); broadcastState(); confetti();
}

/** The Traitor's hidden bonuses are added to their score at the very end (finish() calls this, so ending the game early pays them too). */
function trPayHidden() {
  if (!trOn()) return; G.tr.screen = null;
  const t = G.tr.traitor; if (t && G.players[t] && G.tr.hidden) { G.players[t].score += G.tr.hidden; trLog(`Hidden bonuses paid out: ${G.tr.hidden}`); G.tr.hidden = 0; persist(); }
}

// ---------------------------------------------------------------- the host screen
function trRenderScreen() {
  const sc = G.tr.screen;
  if (sc.kind === 'table' && !sc.locked && !trTickT) trStartTick();
  const wrap = (inner, btn) => { stage.innerHTML = `<div class="stage-top"><div class="pillbox"><span class="hpill">🗡 The Traitors</span><span class="hpill">${esc(G.quiz.title)}</span></div></div><div class="stage-main trstage">${inner}</div>${hostBar(`<button class="btn btn-ghost" data-act="end">End game</button>${btn}`)}`; bind(); };
  const nextBtn = (label) => `<button class="btn btn-primary" data-act="primary">${label}</button>`;
  if (sc.kind === 'notice') return wrap(`<div class="trbig">${esc(sc.title)}</div>${sc.quote ? `<div class="trquote">“${esc(sc.quote)}”</div>` : ''}${(sc.lines || []).map((l) => `<p class="trline">${esc(l)}</p>`).join('')}`, nextBtn('Continue ▶'));
  if (sc.kind === 'table') {
    const left = Math.max(0, sc.endsAt - Date.now()), n = Object.keys(G.tr.votes).length, all = Object.keys(G.players).length;
    return wrap(`<div class="trbig">🕯 THE ROUND TABLE</div><p class="trline">One of you is the Traitor. Talk it over, then vote on your phone for who to banish.</p>
      <div class="trclock" id="trClock">${Math.floor(left / 60000)}:${String(Math.floor(left / 1000) % 60).padStart(2, '0')}</div>
      <p class="trline small" id="trVoted">${n} of ${all} have voted</p>
      <div class="trfaces">${Object.values(G.players).map((p) => `<span class="trface">${esc(p.emoji || '🙂')} ${esc(p.name)}</span>`).join('')}</div>
      <p class="trline small">Right: the Traitor loses their power and 5,000 points, and everyone who voted for them wins 2,000. Wrong: the Traitor stays.</p>`, nextBtn('Lock the votes ▶'));
  }
  if (sc.kind === 'verdict') {
    const mx = Math.max(1, ...sc.rows.map((r) => r.n)), top = sc.banished;
    const head = sc.tie ? 'NO MAJORITY' : sc.correct ? `${esc(pname(top))} IS BANISHED!` : top ? `${esc(pname(top))} IS BANISHED…` : 'NOBODY VOTED';
    const verdict = sc.tie ? 'The votes were split. Nobody is banished. The Traitor lives on…' : !top ? 'Nobody voted, so nobody is banished.' : sc.correct ? `…and ${esc(pname(top))} WAS the Traitor! They lose their power and ${TR.BANISH_LOSS.toLocaleString('en-GB')} points. A new Traitor has been chosen, in secret.` : `…but ${esc(pname(top))} was NOT the Traitor. The Traitor is still among you, and stays for the second half.`;
    return wrap(`<div class="trbig">${head}</div><div class="trbars">${sc.rows.map((r) => `<div class="trbar"><span class="trbn">${esc(pem(r.pid))} ${esc(pname(r.pid))}</span><i style="width:${Math.max(6, r.n / mx * 100)}%"></i><b>${r.n}</b></div>`).join('')}</div>
      <p class="trline">${verdict}</p>${sc.correct && sc.winners.length ? `<p class="trline">🏅 Right: ${esc(trNames(sc.winners))} win ${TR.VOTER_BONUS.toLocaleString('en-GB')} each.</p>` : ''}`, nextBtn('On to half time ▶'));
  }
  if (sc.kind === 'final') return wrap(`<div class="trsmall">THE TRAITOR WAS…</div><div class="trbig trname">${esc(pem(sc.traitor))} ${esc(pname(sc.traitor))}</div>${sc.lines.map((l) => `<p class="trline">${esc(l)}</p>`).join('')}`, nextBtn('Final results 🏆'));
}

// ---------------------------------------------------------------- the host's phone: the control panel (sealed messages)
/** A message from the builder's 🗡 Traitors panel: sealed with the host password, so the players on the same channel can't read or fake it. */
async function onTrCtl(payload) {
  const pw = LQ.hostPassword(); if (!pw || !payload?.m) return;
  let m; try { m = await LQ.unseal(pw, G.code, payload.m); } catch { return; }
  if (!m || Math.abs(Date.now() - (+m.ts || 0)) > 120000 || (G.trCtlNonce && +m.ts <= G.trCtlNonce)) return;
  G.trCtlNonce = +m.ts; trEnsure();
  let note = '';
  if (!trOn()) note = 'Traitors mode is not switched on for this quiz (Settings).';
  else if (m.op === 'pick') note = trSetTraitor(m.pid, 'picked') ? '' : 'That player is not in the game.';
  else if (m.op === 'random') { const pool = Object.keys(G.players); if (pool.length) trSetTraitor(pool[Math.floor(Math.random() * pool.length)], 'picked'); else note = 'Nobody has joined yet.'; }
  const t = trOn() ? G.tr : null;
  const reply = { ts: Date.now(), note, on: !!t, players: Object.values(G.players).map((p) => ({ pid: p.id, name: p.name, emoji: p.emoji || '', score: p.score, bot: p.id.startsWith('p_bot') })),
    traitor: t?.traitor || null, powers: t?.powers, qDone: t?.qDone, tableDone: t?.tableDone, hidden: t?.hidden, listIn: !!t?.list, phase: G.phase, log: (t?.log || []).slice(-25) };
  send('trctlr', { m: await LQ.seal(pw, G.code, reply) });
}
