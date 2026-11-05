/* Let's Quiz host screen: THE TRAITORS (October 2026).
 *
 * One player is secretly the Traitor, picked from the host's own phone (the 🗡 Traitors button on the quiz's card in the builder).
 * The Traitor gets a secret menu on their phone: steal points (100-1000, up to 5 times a half, the same person once every 15 questions),
 * gift a free answer, block someone from a question, double someone's points (5 of each per half: they all come back at half time), and send secret or whole-group messages.
 * Everyone earns a 🛡 shield by getting 3 in a row (the Traitor can't touch them until they get one wrong). Points the Traitor
 * gives themselves (free answer, double) are only for show: taken off again at the very end. After the last question
 * before half time, 3 minutes at the Round Table, then a vote to banish the Traitor. At half time the Traitor ticks a 20 Questions
 * list about themselves, which becomes the last round: find the Traitor. See docs/traitors-guide.html (also the PDF the players get).
 *
 * Secrets never go in the shared game state: a private message ('trs') goes out for the one phone it is for. The host's phone control
 * panel talks to this screen with sealed ('trctl') messages. Hooks into host.html and party.js are small and named tr*.
 * Loaded after party.js; runs once a game exists. */

const TR = { STEALS: 5, SAME_VICTIM: 15, MIN: 100, MAX: 1000, USES: 5, TABLE_MS: 180000, BANISH_LOSS: 5000, WRONG_LOSS: 3000, VOTER_BONUS: 2000, SLIP_BONUS: 2000, FINDER_BONUS: 2000, CAUGHT_LOSS: 2000, AWAY_BONUS: 5000, MSGS: 3, MSG_LEN: 140 };
const trFresh = () => ({ gift: TR.USES, block: TR.USES, dbl: TR.USES });
const trNames = (pids) => pids.map((p) => pname(p)).join(' and ').replace(/, ([^,]*)$/, ' and $1');
let trPushT = null;
const trCtlPushSoon = () => { clearTimeout(trPushT); trPushT = setTimeout(() => { try { trCtlPush(); } catch {} }, 250); }; // the host's phone panel sees every entry as it happens
const trLog = (text) => { if (G.tr) { G.tr.log.push({ t: Date.now(), q: G.tr.qDone, text }); G.tr.log = G.tr.log.slice(-80); trCtlPushSoon(); } };
const trOn = () => !!G?.tr?.on;
/** What the letters say. The Traitor signs them all, and never names themselves. */
const trPick = (a) => a[Math.floor(Math.random() * a.length)];
const TR_SAY = {
  // read out on the big screen, about somebody
  steal: (v, to, n) => !to ? trPick([`${v}, ${n} of your points are now mine. Sleep well.`, `I have taken ${n} points from ${v} and kept every one. Who will be next?`, `${v}, did you really think your ${n} points were safe? They are mine now.`]) : trPick([`${v}, ${n} of your points now belong to ${to}. Sleep well.`, `I have taken ${n} points from ${v} and gifted them to ${to}. Who will be next?`, `${v}, did you really think your ${n} points were safe? ${to} sends their thanks.`, `${n} points changed hands tonight: from ${v} to ${to}. Trust no one.`]),
  gift: (v) => trPick([`${v} has been handed a free answer: full points, whatever they say. A gift from me… for now.`, `A little present for ${v}: full points on this question. Ask yourselves why.`]),
  block: (v) => trPick([`${v} has been silenced for this question. Sit back and watch.`, `${v}, not a word from you on this one. Sit this out.`]),
  dbl: (v) => trPick([`${v}'s points are doubled on this question. Enjoy it… while it lasts.`, `Double points for ${v}, courtesy of me. You are welcome.`]),
  // whispered to the person it happened to
  steal2: (to, n) => !to ? trPick([`I have taken ${n} of your points and kept them. Better luck next time.`, `${n} of your points are now mine. Did you see it coming?`]) : trPick([`I have taken ${n} of your points and given them to ${to}. Better luck next time.`, `${n} of your points now belong to ${to}. Did you see it coming?`]),
  gift2: () => trPick(['A gift: full points on this question, whatever you answer. Ask yourself why.', 'I have given you a free answer. Full points, no questions asked. For now.']),
  block2: () => trPick(['I have silenced you for this question. Sit back and watch.', 'Not a word from you on this one. You are blocked.']),
  dbl2: () => trPick(['Your points are doubled on this question. Do not trust a gift.', 'Double points for you this time. You are welcome.'])
};
const trShielded = (pid) => !!G.tr?.shield?.[pid]; // earned with 3 right in a row, kept until the next wrong answer

/** The mode switched on in the quiz's settings: build the traitor state once. Not in warm-ups, previews or the demo. */
function trEnsure() {
  if (G.tr || !G.quiz?.settings?.traitors?.on || WARMUP || PREVIEW || DEMO) return;
  G.tr = { on: true, traitor: null, history: [], qDone: 0, lastStealQ: -99, victimQ: {}, stolen: 0, steals: 0, stealsHalf: 0, powers: trFresh(), set: { gift: null, block: null, dbl: null }, used: { gift: 0, block: 0, dbl: 0 },
    streak: {}, shield: {}, notices: [], screen: null, hidden: 0, fake: {}, show: {}, hold: null, tableDone: false, votes: {}, list: null, twentyAdded: false, revealed: false, log: [], msgBreak: 0, msgs: 0, stealShown: false, banishedBefore: [] };
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
  if (sc.kind === 'notice') Object.assign(o, { title: sc.title, lines: sc.lines, quote: sc.quote || '', letter: sc.letter || '' });
  if (sc.kind === 'table') Object.assign(o, { endsAt: sc.endsAt, total: sc.total, left: Math.max(0, sc.endsAt - (G.paused ? G.pausedAt : Date.now())), voted: Object.keys(G.tr.votes), locked: !!sc.locked });
  if (sc.kind === 'chosen') Object.assign(o, { rows: sc.rows, banished: sc.banished });
  if (sc.kind === 'verdict') Object.assign(o, { rows: sc.rows, banished: sc.banished, correct: sc.correct, winners: sc.winners, wrongVoters: sc.wrongVoters || [], tie: !!sc.tie, wrongLoss: !!sc.wrongLoss });
  if (sc.kind === 'final') Object.assign(o, { traitor: sc.traitor, lines: sc.lines });
  return o;
}
// ---------------------------------------------------------------- "Hold on": the Traitor asks the host not to rush the next question
const TR_HOLD_MS = 180000; // forgotten holds let go by themselves
const trHoldOn = () => !!(trOn() && G.tr.hold && Date.now() - G.tr.hold.at < TR_HOLD_MS);
function trHold(on) {
  if (!trOn() || !G.tr.traitor) return;
  const was = trHoldOn(); G.tr.hold = on ? { at: Date.now() } : null;
  if (was !== trHoldOn()) trLog(on ? '✋ The Traitor asked you to HOLD ON' : '✋ The Traitor let the hold go');
  trHoldUI(); trSync(); persist(); trCtlPush();
  if (on) trTell(G.tr.traitor, 'ok', { text: '✋ The host has been asked to hold on. It lifts when you send something, or tap again.' });
}
/** Whatever the Traitor sends lifts the hold: the host is free to carry on. */
function trHoldClear() { if (!G.tr?.hold) return; G.tr.hold = null; trHoldUI(); trCtlPush(); }
/** Nothing about a hold shows on the host screen (everyone can see it): the alert is only on the host's phone panel. A game on auto does not move on while one is up. */
function trHoldUI() { document.getElementById('trHoldBar')?.remove(); }
setInterval(() => { try { if (typeof G === 'undefined' || !G?.tr) return; if (G.tr.hold && !trHoldOn()) { G.tr.hold = null; trSync(); trCtlPush(); } trHoldUI(); } catch {} }, 1000);

/** A demo slide that plays a sample letter: on the big screen and every phone, or ('phones') only on the real players' phones. */
function trDemoLetter(q) {
  if (!trOn() || !q.letter) return;
  if (q.letterMode === 'phones') { for (const p of Object.values(G.players)) if (!p.id.startsWith('p_bot')) trTell(p.id, 'letter', { now: true, text: q.letter }); return; }
  const at = G.qIndex;
  setTimeout(() => { if (G.qIndex === at && G.phase === 'slide' && !G.tr.screen) trPushNotice({ kind: 'notice', title: TR_LETTER_TITLE, letter: q.letter, afterIdx: 0, sound: 'whoosh' }, true); }, 500);
}
/** A private word to one phone (or all of them, for ping-style banners). Only the phone it is for acts on it. */
const trTell = (to, kind, data = {}) => send('trs', { to, kind, ...data });
function trSync() {
  const t = G.tr?.traitor; if (!t || !G.players[t]) return;
  const qd = G.tr.qDone, victims = {};
  for (const p of Object.keys(G.players)) if (p !== t) victims[p] = { shield: trShielded(p), wait: Math.max(0, TR.SAME_VICTIM - (qd - (G.tr.victimQ[p] ?? -99))), score: G.players[p].score };
  trTell(t, 'sync', { d: { powers: G.tr.powers, set: G.tr.set, canSteal: (G.tr.stealsHalf || 0) < TR.STEALS, stealsLeft: Math.max(0, TR.STEALS - (G.tr.stealsHalf || 0)), victims, window: trWindow(), nextPlain: powerNextPlain() >= 0, msgsLeft: Math.max(0, TR.MSGS - G.tr.msgBreak), hold: trHoldOn(),
    needList: G.tr.tableDone && !G.tr.list, list: G.tr.list, qDone: qd, players: Object.values(G.players).filter((p) => p.id !== t).map((p) => ({ pid: p.id, name: p.name, emoji: p.emoji || '' })) } });
}
/** A phone says hello (joining, or coming back after a drop): a Traitor is reminded who they are. */
function trOnHello(pid) { if (trOn() && G.tr.traitor === pid) { trTell(pid, 'role', { again: true, reason: G.tr.history.at(-1)?.reason, n: G.tr.history.length }); trSync(); } }

// ---------------------------------------------------------------- picking the Traitor
function trSetTraitor(pid, reason = 'picked') {
  trEnsure(); if (!trOn() || !G.players[pid]) return false;
  G.tr.traitor = pid; G.tr.history.push({ pid, at: G.tr.qDone, reason });
  Object.assign(G.tr, { powers: trFresh(), set: { gift: null, block: null, dbl: null }, used: { gift: 0, block: 0, dbl: 0 }, lastStealQ: -99, stealsHalf: 0, victimQ: {}, list: null, msgBreak: 0, hold: null });
  trLog(`${pname(pid)} is the Traitor (${reason})`);
  trTell(pid, 'role', { reason, n: G.tr.history.length }); trSync(); persist(); broadcastState();
  if (G.phase === 'lobby') render(); // the lobby says a Traitor is picked
  return true;
}

// ---------------------------------------------------------------- the Traitor's actions (from their phone)
/** Between questions: the same break the power cards are played in. Not while a vote or a notice is up. */
function trWindow() { return trOn() && ['round', 'slide', 'typecard', 'countdown', 'reveal', 'scoreboard'].includes(G.phase) && !(G.tr.screen && ['table', 'chosen', 'verdict', 'final'].includes(G.tr.screen.kind)); }
const trNo = (why) => trTell(G.tr.traitor, 'no', { why });
function onTr({ pid, op, ...a }) {
  if (!trOn() || !G.players[pid]) return;
  if (op === 'sync') { if (pid === G.tr.traitor) trSync(); return; }
  if (op === 'vote') return trVote(pid, a.target);
  if (pid !== G.tr.traitor) return;
  if (op === 'hold') return trHold(!!a.on);
  if (op === 'steal') return trSteal(a);
  if (op === 'power') return trPower(a);
  if (op === 'msg') return trMsg(a);
  if (op === 'list') return trList(a);
}
function trSteal({ victim, amount, to, show }) {
  const t = G.tr.traitor, qd = G.tr.qDone;
  if (!trWindow()) return trNo('Wait for the break between questions.');
  if ((G.tr.stealsHalf || 0) >= TR.STEALS) return trNo(`You have used all ${TR.STEALS} steals for this half. They come back at half time.`);
  if (!G.players[victim] || victim === t) return trNo('Pick someone else to steal from.');
  if (!G.players[to] || to === victim) return trNo('Give the points to someone other than the player you took them from (you can keep them yourself, but they only count for show).');
  if (trShielded(victim)) return trNo(`${pname(victim)} has a 🛡 shield.`);
  const wait = TR.SAME_VICTIM - (qd - (G.tr.victimQ[victim] ?? -99)); if (wait > 0) return trNo(`You can only steal from ${pname(victim)} once every ${TR.SAME_VICTIM} questions: ${wait} more to go.`);
  const want = Math.round((+amount || 0) / 100) * 100; if (want < TR.MIN || want > TR.MAX) return trNo(`Steal between ${TR.MIN} and ${TR.MAX}.`);
  const amt = Math.min(want, Math.max(0, G.players[victim].score)); if (amt <= 0) return trNo(`${pname(victim)} has no points to steal.`);
  G.players[victim].score -= amt; G.players[to].score += amt;
  if (to === t) { G.tr.fake = G.tr.fake || {}; G.tr.fake[t] = (G.tr.fake[t] || 0) + amt; } // kept for themselves: only for show, it comes off again at the very end
  G.tr.lastStealQ = qd; G.tr.victimQ[victim] = qd; G.tr.stolen += amt; G.tr.steals++; G.tr.stealsHalf = (G.tr.stealsHalf || 0) + 1;
  const afterIdx = ['reveal', 'scoreboard', 'slide'].includes(G.phase) ? G.qIndex + 1 : G.qIndex; // the question that comes next: the notice follows it
  if (show === 'secret') trTell(victim, 'letter', { text: TR_SAY.steal2(to === t ? null : pname(to), amt.toLocaleString('en-GB')) });
  else {
    G.tr.notices.push({ kind: 'notice', title: TR_LETTER_TITLE, letter: TR_SAY.steal(pname(victim), to === t ? null : pname(to), amt.toLocaleString('en-GB')), afterIdx, sound: 'whoosh',
      lines: G.tr.stealShown ? [] : ['At half time you will have the chance to "banish" who you think the Traitor is. If you are right, they lose their power and 5,000 points, and everyone who voted for them wins 2,000.'] });
    G.tr.stealShown = true;
  }
  trLog(`💰 Stole ${amt} from ${pname(victim)} and gave it to ${to === t ? 'themselves (for show)' : pname(to)} · ${show === 'secret' ? '🤫 only ' + pname(victim) + ' sees the letter' : '📺 letter on the big screen'}`);
  trTell(t, 'ok', { text: `🗡 Done: ${amt} points taken from ${pname(victim)} and ${to === t ? 'kept for yourself (only for show: they come off at the end)' : 'given to ' + pname(to)}.` }); trHoldClear();
  trSync(); persist(); broadcastState(); if (['reveal', 'scoreboard'].includes(G.phase)) render();
}
function trPower({ kind, target, show }) {
  const t = G.tr.traitor; if (!['gift', 'block', 'dbl'].includes(kind)) return;
  if (!trWindow()) return trNo('Pick before the question starts, in the break.');
  if (powerNextPlain() < 0) return trNo('There is no everyone-answers question left to use it on.');
  if (target === null || target === undefined || target === '') { G.tr.set[kind] = null; trSync(); persist(); trLog(`↩ Took back the ${{ gift: 'free answer', block: 'block', dbl: 'double' }[kind]}`); return trTell(t, 'ok', { text: 'Taken back: it is not used.' }); }
  if (!G.players[target]) return;
  if (G.tr.powers[kind] <= 0) return trNo('You have none of those left.');
  for (const k of ['gift', 'block', 'dbl']) if (k !== kind && G.tr.set[k] === target) return trNo(`${pname(target)} already has something from you for the next question.`);
  if (kind === 'block' && target !== t && trShielded(target)) return trNo(`${pname(target)} has a 🛡 shield: you can't block them.`);
  trHoldClear(); G.tr.set[kind] = target; (G.tr.show = G.tr.show || {})[kind] = show === 'secret' ? 'secret' : 'screen'; trSync(); persist();
  trLog(`${{ gift: '🎁 Free answer', block: '🚫 Block', dbl: '✨ Double' }[kind]} lined up for ${target === t ? 'themselves (for show)' : pname(target)} on the next question · ${show === 'secret' ? '🤫 only they see the letter' : '📺 letter on the big screen after the question'}`);
  trTell(t, 'ok', { text: { gift: `🎁 ${target === t ? 'You' : pname(target)} will get a free answer on the next question.`, block: `🚫 ${target === t ? 'You' : pname(target)} will be blocked from the next question.`, dbl: `✨ ${target === t ? 'Your' : pname(target) + "'s"} points will be doubled on the next question.` }[kind] });
}
function trMsg({ to, text }) {
  const t = G.tr.traitor, msg = String(text || '').replace(/\s+/g, ' ').trim().slice(0, TR.MSG_LEN);
  if (!msg) return trNo('Write a message first.');
  if (G.tr.msgBreak >= TR.MSGS) return trNo(`That's ${TR.MSGS} messages for this break. Wait for the next question.`);
  if (to !== 'all' && (!G.players[to] || to === t)) return trNo('Pick someone to send it to.');
  G.tr.msgBreak++; G.tr.msgs++;
  if (to === 'all') { trPushNotice({ kind: 'notice', title: TR_LETTER_TITLE, letter: msg, afterIdx: 0, sound: 'whoosh' }, true); trLog(`📜 Message to EVERYONE (big screen): “${msg}”`); }
  else { trTell(to, 'msg', { text: msg }); trLog(`🤫 Secret message to ${pname(to)}: “${msg}”`); }
  trTell(t, 'ok', { text: to === 'all' ? '📜 Sent to everyone.' : `🤫 Sent to ${pname(to)}.` }); trHoldClear(); trSync(); persist();
}
function trList({ items }) {
  if (!Array.isArray(items)) return;
  const list = items.map((x, i) => ({ id: 'c' + (i + 1), text: String(x.text || '').trim().slice(0, 90), yes: !!x.yes, own: !!x.own })).filter((x) => x.text).slice(0, 90);
  if (list.filter((x) => x.yes).length < 3) return trNo('Tick at least 3 that are true of you.');
  G.tr.list = list; trLog(`📋 The Traitor's 20 Questions list is in (${list.length} questions)`); trTell(G.tr.traitor, 'ok', { text: '✅ Your list is saved. Honesty is the whole game!' }); trHoldClear(); trSync(); persist();
  if (G.phase === 'slide') render(); // the half-time button was waiting for it
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
  G.q.trshow = Object.assign({}, G.tr.show); G.tr.show = {};
  if (fx.gift && fx.gift !== G.tr.traitor) trTell(fx.gift, 'letter', { now: true, text: TR_SAY.gift2() });
  if (fx.block && fx.block !== G.tr.traitor) trTell(fx.block, 'letter', { now: true, text: TR_SAY.block2() });
  if (fx.dbl && fx.dbl !== G.tr.traitor) trTell(fx.dbl, 'letter', { now: true, text: TR_SAY.dbl2() });
  if (Object.keys(fx).length) { G.q.trfx = fx; trLog(`🎯 Used for this question: ${Object.entries(fx).map(([k, p]) => `${{ gift: 'free answer', block: 'block', dbl: 'double' }[k]} on ${pname(p)}`).join(', ')}`); }
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
    if (trShielded(pid) && !right && fx.block !== pid) { G.tr.shield[pid] = 0; trTell(pid, 'ping', { icon: '🛡', text: 'Wrong answer: your shield is gone. The traitor can touch you again.' }); }
    G.tr.streak[pid] = right ? (G.tr.streak[pid] || 0) + 1 : 0;
    if (G.tr.streak[pid] >= 3) { G.tr.streak[pid] = 0; if (!trShielded(pid)) { G.tr.shield[pid] = 1; trTell(pid, 'ping', { icon: '🛡', text: "Shield earned! The traitor can't touch you until you get one wrong." }); } }
  }
  const t = G.tr.traitor, own = t ? (byPlayer[t]?.points || 0) : 0;
  if (fx.block) { const r = byPlayer[fx.block] = byPlayer[fx.block] || blank(); r.points = 0; r.correct = false; r.partial = 0; r.blocked = true; partyNote(r, '🚫 The Traitor blocked you from this question'); }
  if (fx.gift) { const r = byPlayer[fx.gift] = byPlayer[fx.gift] || blank(); r.answered = true; r.points = Math.max(r.points || 0, full); r.correct = true; r.partial = 1; partyNote(r, '🎁 The Traitor gifted you full points!'); }
  if (fx.dbl) { const r = byPlayer[fx.dbl] = byPlayer[fx.dbl] || blank(); if (r.points > 0) { r.points *= 2; partyNote(r, '✨ The Traitor doubled your points!'); } else partyNote(r, '✨ Doubled… but double nothing is nothing'); }
  if (t && fx.block !== t && (fx.gift === t || fx.dbl === t)) { // what the Traitor gave themselves is only for show: it comes off again at the very end
    const extra = Math.max(0, (byPlayer[t]?.points || 0) - own);
    if (extra) { G.tr.fake = G.tr.fake || {}; G.tr.fake[t] = (G.tr.fake[t] || 0) + extra; trLog(`🎭 ${extra} points the Traitor gave themselves, for show only`); }
  }
  for (const k of ['gift', 'block', 'dbl']) if (fx[k] && (G.q.trshow || {})[k] !== 'secret') G.tr.notices.push({ kind: 'notice', title: TR_LETTER_TITLE, letter: TR_SAY[k](pname(fx[k])), afterIdx: 0, sound: 'whoosh' });
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
  G.tr.screen = { id: uid('s'), kind: 'notice', title: n.title, lines: n.lines || [], quote: n.quote || '', letter: n.letter || '', cont: !now };
  persist(); sound(n.sound || (n.letter ? 'whoosh' : 'gong')); render(); broadcastState();
  return true;
}
/** The host presses Next on a Traitors screen. */
function trScreenNext() {
  const sc = G.tr.screen; if (!sc) return false;
  if (sc.kind === 'notice') { G.tr.screen = null; persist(); broadcastState(); if (sc.cont) nextFrom(G.qIndex); else render(); return true; }
  if (sc.kind === 'table') { trLockVotes(); return true; }
  if (sc.kind === 'chosen') { trReveal(); return true; }
  if (sc.kind === 'verdict') { G.tr.screen = null; G.tr.tableDone = true; trHalfReset(); persist(); trSync(); trNudgeList(); broadcastState(); goTo(sc.next); return true; }
  if (sc.kind === 'final') { G.tr.screen = null; G.tr.revealed = true; persist(); broadcastState(); finish(); return true; }
  return false;
}

// ---------------------------------------------------------------- half time: the Round Table and the vote
/** Half time: the steals and powers all come back, for the same Traitor or a new one. */
function trHalfReset() {
  G.tr.powers = trFresh(); G.tr.stealsHalf = 0;
  trLog(`Half time: ${TR.STEALS} steals and ${TR.USES} of each power are back`);
  if (G.tr.traitor) trTell(G.tr.traitor, 'ok', { text: `✨ Half time: your ${TR.STEALS} steals and ${TR.USES} of each power are back for the second half.` });
}
/** Item index of half time: the first break slide, else the middle of the quiz. */
function trHalfIndex() { const qs = G.quiz.questions, b = qs.findIndex((x) => x.type === 'slide' && x.break); return b >= 0 ? b : Math.floor(qs.length / 2); }
const trWantsTable = (i) => trOn() && G.tr.traitor && !G.tr.tableDone && trHalfIndex() === i + 1 && i + 1 < G.quiz.questions.length;
/** Half time is over the Traitor's list: no list, no last round. True while a real Traitor has yet to save it (a bot Traitor can't, and the host can waive it). */
const trListPending = () => trOn() && !!G.tr.traitor && !!G.players[G.tr.traitor] && !G.tr.traitor.startsWith('p_bot') && G.tr.tableDone && !G.tr.list && !G.tr.listWaived;
/** The Traitor's phone opens the list and buzzes. */
const trNudgeList = () => { if (trListPending()) trTell(G.tr.traitor, 'listnow', { text: "Save your list! The quiz can't carry on without it." }); };
/** The host tried to leave half time with no list: hold them here unless they choose to drop the last round. */
function trHoldForList(i) {
  trNudgeList(); render();
  return ask('Waiting for the Traitor', `${pname(G.tr.traitor)} hasn't saved their list yet. Their phone has it open now. Without it there is no last round (the Traitor's 20 Questions).`, 'Keep waiting', 'Skip the last round').then((wait) => {
    if (wait) return;
    G.tr.listWaived = true; trLog('The host skipped the last round: no list from the Traitor'); persist(); render(); nextFrom(i);
  });
}
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
/** The votes are in: count them. The person chosen goes full screen on camera to say whether they are the Traitor; the points move when the host reveals the truth. */
function trLockVotes() {
  const sc = G.tr.screen; if (sc?.kind !== 'table' || sc.locked) return;
  sc.locked = true; clearInterval(trTickT); trTickT = null;
  const count = {}; for (const t of Object.values(G.tr.votes)) count[t] = (count[t] || 0) + 1;
  const rows = Object.entries(count).map(([pid, n]) => ({ pid, n })).sort((a, b) => b.n - a.n), tie = rows.length > 1 && rows[0].n === rows[1].n;
  const banished = rows.length && !tie ? rows[0].pid : null;
  Object.assign(sc, { rows, banished, tie });
  if (!banished) return trReveal(); // a tie or no votes: nobody to put on camera
  sc.kind = 'chosen'; sc.id = uid('s'); trLog(`The room chose ${pname(banished)}`);
  persist(); sound('gong'); render(); broadcastState();
}
/** The host reveals the truth: right, the Traitor is banished; wrong, the person chosen loses points for being wrongly accused. */
function trReveal() {
  const sc = G.tr.screen; if (!sc || !['table', 'chosen'].includes(sc.kind)) return;
  const { rows, banished, tie } = sc, traitor = G.tr.traitor, correct = banished && banished === traitor;
  let winners = [], wrongVoters = [];
  if (correct) {
    G.players[traitor].score -= TR.BANISH_LOSS;
    winners = Object.entries(G.tr.votes).filter(([v, t]) => t === traitor && v !== traitor).map(([v]) => v);
    for (const v of winners) G.players[v].score += TR.VOTER_BONUS;
    G.tr.banishedBefore.push(traitor); trLog(`${pname(traitor)} was banished (right!): -${TR.BANISH_LOSS}, ${winners.length} voters +${TR.VOTER_BONUS}`);
    trTell(traitor, 'banished', { text: `You were banished! You lose your power and ${TR.BANISH_LOSS.toLocaleString('en-GB')} points.` });
    const pool = Object.keys(G.players).filter((p) => p !== traitor); const next = pool[Math.floor(Math.random() * pool.length)];
    trSetTraitor(next, 'new');
  } else {
    G.tr.hidden += TR.SLIP_BONUS; trLog(`The vote missed (${banished ? pname(banished) : 'a tie'}): ${TR.SLIP_BONUS} held back for the Traitor`);
    if (banished && G.players[banished]) {
      G.players[banished].score -= TR.WRONG_LOSS; trLog(`${pname(banished)} was wrongly accused: -${TR.WRONG_LOSS}`); trTell(banished, 'ping', { icon: '😬', text: `You were wrongly accused! You lose ${TR.WRONG_LOSS.toLocaleString('en-GB')} points.` });
      wrongVoters = Object.entries(G.tr.votes).filter(([v, t]) => t === banished && v !== banished && G.players[v]).map(([v]) => v);
      for (const v of wrongVoters) { G.players[v].score -= TR.WRONG_LOSS; trTell(v, 'ping', { icon: '😬', text: `You voted for the wrong person: you lose ${TR.WRONG_LOSS.toLocaleString('en-GB')} points.` }); }
      if (wrongVoters.length) trLog(`${wrongVoters.length} voters for the wrong person: -${TR.WRONG_LOSS} each`);
    }
  }
  sc.kind = 'verdict'; sc.id = uid('s'); Object.assign(sc, { rows, banished, correct: !!correct, winners, wrongVoters, tie, locked: true, wrongLoss: !!banished && !correct });
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
  const fake = Object.values(G.tr.fake || {}).reduce((a, b) => a + b, 0);
  if (fake) lines.push(`The ${fake.toLocaleString('en-GB')} points they gave themselves were only for show: they come off now.`);
  if (G.tr.hidden && !f?.most) lines.push(`Their secret bonuses, ${G.tr.hidden.toLocaleString('en-GB')} points, are added now.`);
  G.tr.screen = { id: uid('s'), kind: 'final', traitor: t, lines };
  persist(); sound('fanfare'); render(); broadcastState(); confetti();
}

/** The Traitor's hidden bonuses are added to their score at the very end (finish() calls this, so ending the game early pays them too). */
function trPayHidden() {
  if (!trOn()) return; G.tr.screen = null;
  const t = G.tr.traitor; if (t && G.players[t] && G.tr.hidden) { G.players[t].score += G.tr.hidden; trLog(`Hidden bonuses paid out: ${G.tr.hidden}`); G.tr.hidden = 0; persist(); }
  for (const [pid, n] of Object.entries(G.tr.fake || {})) if (n && G.players[pid]) { G.players[pid].score -= n; trLog(`Points given to themselves, for show, taken off ${pname(pid)}: ${n}`); G.tr.fake[pid] = 0; persist(); }
}

// ---------------------------------------------------------------- the host screen
function trRenderScreen() {
  const sc = G.tr.screen;
  if (sc.kind === 'table' && !sc.locked && !trTickT) trStartTick();
  const wrap = (inner, btn) => { stage.innerHTML = `<div class="stage-top"><div class="pillbox"><span class="hpill">🗡 The Traitors</span><span class="hpill">${esc(G.quiz.title)}</span></div></div><div class="stage-main trstage">${inner}</div>${hostBar(`<button class="btn btn-ghost" data-act="end">End game</button>${btn}`)}`; bind(); };
  const nextBtn = (label) => `<button class="btn btn-primary" data-act="primary">${label}</button>`;
  if (sc.kind === 'notice' && sc.letter) return wrap(`<div class="trbig trletter-title">${esc(sc.title)}</div>${trLetterHtml(sc.letter)}${(sc.lines || []).map((l) => `<p class="trline small">${esc(l)}</p>`).join('')}`, nextBtn('Continue ▶'));
  if (sc.kind === 'notice') return wrap(`<div class="trbig">${esc(sc.title)}</div>${sc.quote ? `<div class="trquote">“${esc(sc.quote)}”</div>` : ''}${(sc.lines || []).map((l) => `<p class="trline">${esc(l)}</p>`).join('')}`, nextBtn('Continue ▶'));
  if (sc.kind === 'table') {
    const left = Math.max(0, sc.endsAt - Date.now()), n = Object.keys(G.tr.votes).length, all = Object.keys(G.players).length;
    return wrap(`<div class="trbig">🕯 THE ROUND TABLE</div><p class="trline">One of you is the Traitor. Talk it over, then vote on your phone for who to banish.</p>
      <div class="trclock" id="trClock">${Math.floor(left / 60000)}:${String(Math.floor(left / 1000) % 60).padStart(2, '0')}</div>
      <p class="trline small" id="trVoted">${n} of ${all} have voted</p>
      <div class="trfaces" style="--pf-live:${all <= 6 ? 21 : all <= 12 ? 15 : all <= 20 ? 11 : 8}vh">${Object.values(G.players).map((p) => `<span class="trface cam">${face(p.id, esc(p.emoji || '🙂'))}<span class="trfn">${esc(p.name)}</span></span>`).join('')}</div>
      <p class="trline small">The player with the most votes goes on camera and tells the room whether they are the Traitor. Right: the Traitor loses their power and 5,000 points, and everyone who voted for them wins 2,000. Wrong: the Traitor stays, and the person chosen and everyone who voted for them each lose ${TR.WRONG_LOSS.toLocaleString('en-GB')}.</p>`, nextBtn('Lock the votes ▶'));
  }
  if (sc.kind === 'chosen') {
    const who = sc.banished;
    return wrap(`<div class="trspot" data-pcam="${esc(who)}" data-pzoom="3.4"><div class="trspot-em">${esc(pem(who))}</div>
      <div class="trspot-cap"><div class="trsmall">THE ROOM HAS CHOSEN</div><div class="trbig trname">${esc(pname(who))}</div>
      <p class="trline">Look at the camera and tell everyone: <b>are you the Traitor?</b></p>
      <p class="trline small">Wrongly accused? You lose ${TR.WRONG_LOSS.toLocaleString('en-GB')} points, and so does everyone who voted for you.</p></div></div>`, nextBtn('Reveal the truth ▶'));
  }
  if (sc.kind === 'verdict') {
    const mx = Math.max(1, ...sc.rows.map((r) => r.n)), top = sc.banished;
    const head = sc.tie ? 'NO MAJORITY' : sc.correct ? `${esc(pname(top))} IS BANISHED!` : top ? `${esc(pname(top))} IS BANISHED…` : 'NOBODY VOTED';
    const verdict = sc.tie ? 'The votes were split. Nobody is banished. The Traitor lives on…' : !top ? 'Nobody voted, so nobody is banished.' : sc.correct ? `…and ${esc(pname(top))} WAS the Traitor! They lose their power and ${TR.BANISH_LOSS.toLocaleString('en-GB')} points. A new Traitor has been chosen, in secret.` : `…but ${esc(pname(top))} was NOT the Traitor. Wrongly accused: they lose ${TR.WRONG_LOSS.toLocaleString('en-GB')} points. The Traitor is still among you, and stays for the second half.`;
    return wrap(`<div class="trbig">${head}</div><div class="trbars">${sc.rows.map((r) => `<div class="trbar"><span class="trbn">${esc(pem(r.pid))} ${esc(pname(r.pid))}</span><i style="width:${Math.max(6, r.n / mx * 100)}%"></i><b>${r.n}</b></div>`).join('')}</div>
      <p class="trline">${verdict}</p>${sc.correct && sc.winners.length ? `<p class="trline">🏅 Right: ${esc(trNames(sc.winners))} win ${TR.VOTER_BONUS.toLocaleString('en-GB')} each.</p>` : ''}${sc.wrongLoss && sc.wrongVoters?.length ? `<p class="trline">😬 Wrong: ${esc(trNames(sc.wrongVoters))} voted for them, so ${sc.wrongVoters.length === 1 ? 'they lose' : 'they each lose'} ${TR.WRONG_LOSS.toLocaleString('en-GB')} too.</p>` : ''}`, nextBtn('On to half time ▶'));
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
  await trCtlSend(note, pw);
}
/** What the host's phone panel is shown: it is also pushed unasked when the Traitor asks for a hold. */
async function trCtlSend(note = '', pw = LQ.hostPassword()) {
  if (!pw || typeof G === 'undefined' || !G?.code) return;
  const t = trOn() ? G.tr : null;
  const reply = { ts: Date.now(), note, on: !!t, players: Object.values(G.players).map((p) => ({ pid: p.id, name: p.name, emoji: p.emoji || '', score: p.score, bot: p.id.startsWith('p_bot') })),
    traitor: t?.traitor || null, powers: t?.powers, qDone: t?.qDone, tableDone: t?.tableDone, hidden: t?.hidden, listIn: !!t?.list, hold: trHoldOn(), stealsLeft: t ? Math.max(0, TR.STEALS - (t.stealsHalf || 0)) : null, set: t?.set, phase: G.phase, log: (t?.log || []).slice(-40) };
  send('trctlr', { m: await LQ.seal(pw, G.code, reply) });
}
const trCtlPush = () => { trCtlSend().catch(() => {}); };
