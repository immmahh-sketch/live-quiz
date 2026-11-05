/* Let's Quiz host screen: THE TRAITORS (October 2026).
 *
 * One player is secretly the Traitor, picked from the host's own phone (the 🗡 Traitors button on the quiz's card in the builder).
 * The Traitor gets a secret menu on their phone: steal points (100-1000, up to 3 times a half, the same person once every 15 questions),
 * gift a free answer, block someone from a question, double someone's points (3 of each per half: they all come back at half time), and send secret or whole-group messages.
 * Everyone earns a 🛡 shield by getting 3 in a row (the Traitor's steals and blocks fail against them until they get one wrong). Points the Traitor
 * gives themselves (free answer, double) are only for show: taken off again at the very end. After the last question
 * before half time, 3 minutes at the Round Table, then a vote to banish the Traitor. At half time the Traitor ticks a 20 Questions
 * list about themselves, which becomes the last round: find the Traitor. See docs/traitors-guide.html (also the PDF the players get).
 *
 * Secrets never go in the shared game state: a private message ('trs') goes out for the one phone it is for. The host's phone control
 * panel talks to this screen with sealed ('trctl') messages. Hooks into host.html and party.js are small and named tr*.
 * Loaded after party.js; runs once a game exists. */

const TR = { PROMPT_EVERY: 20, RECRUIT_REFUSE: 2000, PROP_MAX: 4, STEALS: 3, SAME_VICTIM: 15, MIN: 100, MAX: 1000, USES: 3, TABLE_MS: 180000, BANISH_LOSS: 5000, WRONG_LOSS: 3000, VOTER_BONUS: 2000, SLIP_BONUS: 2000, FINDER_BONUS: 3000, CAUGHT_LOSS: 2000, AWAY_BONUS: 5000, MSGS: 3, MSG_LEN: 140 };
const trFresh = () => ({ gift: TR.USES, block: TR.USES, dbl: TR.USES });
const trNames = (pids) => pids.map((p) => pname(p)).join(' and ').replace(/, ([^,]*)$/, ' and $1');
let trPushT = null;
const trCtlPushSoon = () => { clearTimeout(trPushT); trPushT = setTimeout(() => { try { trCtlPush(); } catch {} }, 250); }; // the host's phone panel sees every entry as it happens
const trLog = (text) => { if (G.tr) { G.tr.log.push({ t: Date.now(), q: G.tr.qDone, text }); G.tr.log = G.tr.log.slice(-80); trCtlPushSoon(); } };
const trOn = () => !!G?.tr?.on;
/** What the letters say. The Traitor signs them all, and never names themselves. */
const trPick = (a) => a[Math.floor(Math.random() * a.length)];
/** Said under a secret message, so the reader knows it was sent to them alone. */
const TR_SECRET_NOTES = [
  'Read into that what you will.',
  'This was sent to you, and to nobody else. Make of that what you will.',
  'A message for your eyes only. Draw your own conclusions.',
  'Why you? That is for you to work out.',
  'Only you have seen this. Trust it… or don\'t.',
  'A little secret, just between us. Or is it?',
  'You were chosen to read this. Read into that what you will.'
];
const TR_SAY = {
  // read out on the big screen, about somebody. Each one has several versions, picked at random.
  steal: (v, to, n) => trPick(!to ? [
    `${v}, ${n} of your points are no longer yours. I thought I deserved them more!`,
    `I looked at my score and felt a bit sad. ${v}, I took ${n} of yours!`,
    `${v}, ${n} of your points are now mine. Sleep well.`,
    `I took ${n} points from ${v} and kept every one. Who will be next?`,
    `${v}, did you really think your ${n} points were safe? They are mine now.`,
    `Everyone needs a little treat. ${v}, mine was ${n} of your points.`
  ] : [
    `${n} of your points are no longer yours, ${v}. I thought ${to} deserved them more!`,
    `${to} looks like they will cry if they do not get some points. ${v}, I gave them ${n} of yours!`,
    `${v}, I took ${n} of your points and gave them to ${to}. Call it charity.`,
    `${to} was looking a bit sad, so I gave them ${n} of ${v}'s points. You are welcome, ${to}.`,
    `Somebody had to look after ${to}. ${v}, that somebody was you: ${n} points.`,
    `I felt ${to} needed ${n} points more than ${v} did. Do not take it personally.`,
    `${v}, consider ${n} of your points a donation to ${to}. I did not ask.`,
    `${n} points have left ${v} and gone to ${to}. Did anyone see who did it?`
  ]),
  // Power letters go out the moment the Traitor chooses, so they are all about the next question.
  // Power letters go out the moment the Traitor chooses, so they are all about the next question.
  gift: (v) => trPick([
    `${v} has been handed a free answer on the next question: full points, whatever they say. A gift from me… for now.`,
    `A little present for ${v}: full points on the next question. Ask yourselves why.`,
    `${v} looked like they needed a hand, so on the next question they get a free answer. You are welcome.`,
    `Full points for ${v} on the next question, whatever they answer. I am feeling generous. Suspicious, isn't it?`,
    `${v} will not even need to try on the next question: a free answer, courtesy of someone in this room.`
  ]),
  block: (v) => trPick([
    `${v} has been silenced for the next question. Sit back and watch.`,
    `${v}, not a word from you on the next question. Sit it out.`,
    `${v} will not be answering the next question. Somebody wanted a bit of peace and quiet.`,
    `I am taking ${v}'s phone away for the next question. Do not ask why.`,
    `${v}, you have been blocked from the next question. Make yourself a cup of tea instead.`
  ]),
  dbl: (v) => trPick([
    `${v}'s points are doubled on the next question. Enjoy it… while it lasts.`,
    `Double points for ${v} on the next question, courtesy of me. You are welcome.`,
    `${v} gets twice the points on the next question. I would not get used to it.`,
    `I have decided ${v} deserves double on the next question. Do not ask me why. Just answer.`,
    `Every point ${v} wins on the next question counts twice. Somebody likes you.`
  ]),
  // whispered to the person it happened to
  steal2: (to, n) => trPick(!to ? [
    `${n} of your points are no longer yours: I thought I deserved them more!`,
    `I took ${n} of your points and kept them. Better luck next time.`,
    `${n} of your points are now mine. Did you see it coming?`,
    `I felt a bit sad, so I borrowed ${n} of your points. I will not be giving them back.`
  ] : [
    `${n} of your points are no longer yours: I thought ${to} deserved them more!`,
    `${to} looked like they might cry, so I gave them ${n} of yours. Better luck next time.`,
    `I took ${n} of your points and gave them to ${to}. Did you see it coming?`,
    `${n} of your points now belong to ${to}, who sends their thanks.`
  ]),
  gift2: () => trPick([
    'A gift: full points on your next question, whatever you answer. Ask yourself why.',
    'I have given you a free answer for your next question. Full points, no questions asked. For now.',
    'You looked like you needed a hand, so your next question comes with a free answer. You are welcome.',
    'Full points for you on your next question. I am feeling generous. Suspicious, isn’t it?'
  ]),
  block2: () => trPick([
    'I have silenced you for your next question. Sit back and watch.',
    'Not a word from you on your next question. You are blocked.',
    'You will not be answering your next question. Somebody wanted a bit of peace and quiet.',
    'Your phone is mine for your next question. Make yourself a cup of tea.'
  ]),
  dbl2: () => trPick([
    'Your points are doubled on your next question. Do not trust a gift.',
    'Double points for you on your next question. You are welcome.',
    'Twice the points on your next question. I would not get used to it.',
    'I have decided you deserve double on your next question. Do not ask me why.'
  ])
};
const trShielded = (pid) => !!G.tr?.shield?.[pid]; // earned with 3 right in a row, kept until the next wrong answer

/** The mode switched on in the quiz's settings: build the traitor state once. Not in warm-ups, previews or the demo. */
function trEnsure() {
  if (G.tr || !G.quiz?.settings?.traitors?.on || WARMUP || PREVIEW || DEMO) return;
  G.tr = { on: true, traitor: null, history: [], qDone: 0, lastStealQ: -99, victimQ: {}, stolen: 0, steals: 0, stealsHalf: 0, powers: trFresh(), set: { gift: null, block: null, dbl: null }, used: { gift: 0, block: 0, dbl: 0 },
    streak: {}, shield: {}, notices: [], screen: null, hidden: 0, hiddenMate: 0, act: { steal: 0, power: 0, msg: 0 }, fake: {}, show: {}, hold: null, team: null, teams: {}, mate: null, prop: null, chat: [], recruit: null, recruitOffered: false, lists: {}, roster: [], needTwo: false, twoAtHalf: false, finalDone: false, banishedFinal: [], tableDone: false, votes: {}, list: null, twentyAdded: false, revealed: false, log: [], msgBreak: 0, msgs: 0, stealShown: false, banishedBefore: [] };
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
  if (sc.kind === 'table') Object.assign(o, { final: !!sc.final, endsAt: sc.endsAt, total: sc.total, left: Math.max(0, sc.endsAt - (G.paused ? G.pausedAt : Date.now())), voted: Object.keys(G.tr.votes), locked: !!sc.locked });
  if (sc.kind === 'chosen') Object.assign(o, { rows: sc.rows, banished: sc.banished });
  if (sc.kind === 'verdict') Object.assign(o, { rows: sc.rows, banished: sc.banished, correct: sc.correct, winners: sc.winners, wrongVoters: sc.wrongVoters || [], tie: !!sc.tie, wrongLoss: !!sc.wrongLoss });
  if (sc.kind === 'final') Object.assign(o, { traitor: sc.traitor, roster: sc.roster || [], lines: sc.lines });
  return o;
}
// ---------------------------------------------------------------- "Hold on": the Traitor asks the host not to rush the next question
const TR_HOLD_MS = 60000; // the Traitor's phone repeats it every 20 s while the menu is open; if it goes quiet the hold lets go by itself
const trHoldOn = () => !!(trOn() && G.tr.hold && Date.now() - G.tr.hold.at < TR_HOLD_MS);
function trHold(on, what) {
  if (!trOn() || !G.tr.traitor) return;
  const was = trHoldOn(); G.tr.hold = on ? { at: Date.now(), what: what || '' } : null;
  if (was !== trHoldOn()) trLog(on ? '✋ The Traitor opened their menu: HOLD ON' : '✋ The Traitor is out of their menu');
  trHoldUI(); trSync(); persist(); trCtlPush();
}
/** Whatever the Traitor sends lifts the hold: the host is free to carry on. */
function trHoldClear() { if (!G.tr?.hold) return; G.tr.hold = null; trHoldUI(); trCtlPush(); }
/** A hold shows on the host's phone panel and nowhere else: nothing on the big screen, so nobody looks for the Traitor. A game on auto does not move on while one is up. */
function trHoldUI() { document.getElementById('trHoldBar')?.remove(); }
setInterval(() => { try { if (typeof G === 'undefined' || !G?.tr) return; if (G.tr.hold && !trHoldOn()) { G.tr.hold = null; trSync(); trCtlPush(); } trHoldUI(); } catch {} }, 1000);

// ---------------------------------------------------------------- Claudia: letters from the host's side of the game, and the recruit
/** A letter from Claudia to one phone (the phone shows it signed by her, with any buttons below). */
const trClaudia = (to, text, o = {}) => trTell(to, 'claudia', { id: o.id || uid('c'), text, ...o });
/** The host writes to the Traitor from their own phone: 'traitor', 'mate' or 'both'. */
function trTellTraitors(text, to) {
  const msg = text.replace(/\s+/g, ' ').trim().slice(0, 280); if (!msg) return 'Write something first.';
  const who = to === 'mate' ? [G.tr.mate] : to === 'both' ? trTraitors() : [G.tr.traitor];
  const ok = who.filter((p) => p && G.players[p]); if (!ok.length) return 'There is nobody to send that to yet.';
  for (const p of ok) trClaudia(p, msg, { greet: 'Dear Traitor,' });
  trLog(`✉ You (as Claudia) wrote to ${ok.map(pname).join(' and ')}: “${msg}”`); return '';
}
/** The vote missed, the first time: the Traitor is offered a recruit. */
function trOfferRecruit() {
  const t = G.tr.traitor; if (!t || G.tr.recruitOffered || G.tr.mate || String(t).startsWith('p_bot')) return;
  G.tr.recruitOffered = true; const id = uid('c'); G.tr.recruit = { stage: 'offer', id, target: null };
  trLog('✉ Claudia offered the Traitor a recruit'); persist();
  trClaudia(t, 'Traitors - you live to Murder another day! As you were not Banished, maybe its time to recruit?', { id, greet: 'Dear Traitor,', buttons: [{ k: 'yes', label: '🗡 Recruit: YES' }, { k: 'no', label: 'No' }] });
}
/** An answer to one of Claudia's letters: the Traitor's yes or no, their pick, or the recruit's join or refuse. */
function trClaudiaReply(pid, { id, k, target }) {
  const r = G.tr.recruit; if (!r || r.id !== id) return;
  if (r.stage === 'offer' && pid === G.tr.traitor) {
    if (k === 'no') { G.tr.recruit = { stage: 'done' }; trLog('✉ The Traitor said no to recruiting'); persist(); return; }
    if (k !== 'yes') return;
    const pool = Object.values(G.players).filter((p) => p.id !== pid && !p.id.startsWith('p_bot')).map((p) => ({ pid: p.id, name: p.name, emoji: p.emoji || '' }));
    if (!pool.length) { G.tr.recruit = { stage: 'done' }; return trTell(pid, 'ok', { text: 'There is nobody to recruit.' }); }
    r.stage = 'pick'; r.id = uid('c'); trLog('✉ The Traitor said YES to recruiting: choosing who'); persist();
    return trClaudia(pid, 'Who will you recruit? They may say no, and it will cost them.', { id: r.id, greet: 'Dear Traitor,', pick: pool });
  }
  if (r.stage === 'pick' && pid === G.tr.traitor) {
    if (k === 'none') { G.tr.recruit = { stage: 'done' }; trLog('✉ The Traitor changed their mind about recruiting'); persist(); return; }
    if (k !== 'pick' || !G.players[target] || target === pid || String(target).startsWith('p_bot')) return;
    r.stage = 'invite'; r.target = target; r.id = uid('c'); trLog(`✉ The Traitor chose ${pname(target)} to recruit; Claudia has asked them`); persist();
    trTell(pid, 'ok', { text: `✉ Claudia has asked ${pname(target)}. You will hear what they say.` });
    return trClaudia(target, `The Traitors want you. Join, and learn who they are and share their powers. Refuse, and lose ${TR.RECRUIT_REFUSE.toLocaleString('en-GB')} points.`, { id: r.id, greet: `Dear ${pname(target)},`, buttons: [{ k: 'join', label: '🗡 Join the Traitors' }, { k: 'refuse', label: `Refuse (lose ${TR.RECRUIT_REFUSE.toLocaleString('en-GB')} points)` }] });
  }
  if (r.stage === 'invite' && pid === r.target) {
    const t = G.tr.traitor;
    if (k === 'refuse') {
      G.players[pid].score -= TR.RECRUIT_REFUSE; G.tr.recruit = { stage: 'done' }; trLog(`✉ ${pname(pid)} refused to join and lost ${TR.RECRUIT_REFUSE}`); persist(); broadcastState();
      trTell(t, 'ok', { text: `✉ ${pname(pid)} said no, and lost ${TR.RECRUIT_REFUSE.toLocaleString('en-GB')} points.` }); trTell(pid, 'ping', { icon: '😬', text: `You refused, and lose ${TR.RECRUIT_REFUSE.toLocaleString('en-GB')} points.` });
      return;
    }
    if (k !== 'join') return;
    G.tr.mate = pid; G.tr.recruit = { stage: 'done' }; G.tr.chat = []; G.tr.prop = null; G.tr.twoAtHalf = true; (G.tr.roster = G.tr.roster || []).includes(pid) || G.tr.roster.push(pid);
    trLog(`🗡 ${pname(pid)} JOINED the Traitors (recruited by ${pname(t)})`); persist();
    trTell(pid, 'role', { reason: 'recruited', recruited: true, mate: trWho(t), n: G.tr.history.length });
    trTell(t, 'mate', { mate: trWho(pid) }); trSync(); trNudgeList(); broadcastState();
  }
}
// ---------------------------------------------------------------- two Traitors: private chat, and steals and powers that both must agree
const trDescribe = (a) => {
  const how = a.show === 'secret' ? 'only they see the letter' : 'letter on the big screen';
  if (a.op === 'steal') return `Steal ${(+a.amount || 0).toLocaleString('en-GB')} from ${pname(a.victim)} and give it to ${trIsTraitor(a.to) ? pname(a.to) + ' (for show)' : pname(a.to)} (${how})`;
  return `${{ gift: '🎁 Free answer', block: '🚫 Block', dbl: '✨ Double' }[a.kind] || a.kind} for ${pname(a.target)} on the next question (${how})`;
};
/** What a Traitor sees of the series in progress (null if none): whose turn it is and what has been said. */
function trPropFor(pid) {
  const p = G.tr?.prop; if (!p) return null;
  return { id: p.id, n: p.n, by: trWho(p.by), mine: p.by === pid, turn: p.to === pid, final: p.n >= TR.PROP_MAX, text: trDescribe(p.action), hist: p.hist.map((h) => ({ by: pname(h.by), n: h.n, text: h.text })) };
}
function trChat(pid, text) {
  const msg = String(text || '').replace(/\s+/g, ' ').trim().slice(0, 200), other = trOther(pid); if (!msg || !other) return;
  G.tr.chat = [...(G.tr.chat || []), { by: pid, text: msg, t: Date.now() }].slice(-60);
  trLog(`🤝 ${pname(pid)} to ${pname(other)}: “${msg}”`); trSync(); persist();
}
/** One Traitor suggests a steal or a power: the other must confirm it or suggest something else, up to 4 messages in all. */
function trPropose(by, op, a) {
  const other = trOther(by), prev = G.tr.prop;
  if (op === 'power' && (a.target === null || a.target === undefined || a.target === '')) return trPower({ ...a, who: by }); // taking one back needs no agreement
  if (prev && prev.to !== by) return trTell(by, 'no', { why: `Still waiting for ${pname(prev.to)} to answer your suggestion.` });
  if (prev && prev.n >= TR.PROP_MAX) return trTell(by, 'no', { why: 'That was the last suggestion: do it, or lose 1 power.' });
  if (!trWindow()) return trTell(by, 'no', { why: 'Not right now: the vote is on.' });
  const action = op === 'steal' ? { op, victim: a.victim, amount: a.amount, to: a.to, show: a.show } : { op, kind: a.kind, target: a.target, show: a.show };
  const n = prev ? prev.n + 1 : 1;
  G.tr.prop = { id: prev?.id || uid('x'), n, by, to: other, action, hist: [...(prev?.hist || []), { by, n, text: trDescribe(action) }] };
  trLog(`🤝 ${pname(by)} suggests to ${pname(other)} (message ${n} of ${TR.PROP_MAX}): ${trDescribe(action)}`);
  trTell(by, 'ok', { text: `🤝 Sent to ${pname(other)}: they confirm, or suggest something else.` }); trHoldClear(); trSync(); persist();
}
/** The Traitor whose turn it is answers: 'yes' (do it), 'lose' (on the last message: lose 1 power instead) or 'cancel' (the one who suggested takes it back). */
function trPropReply(pid, k) {
  const p = G.tr.prop; if (!p) return;
  if (k === 'cancel' && p.by === pid) { G.tr.prop = null; trLog(`🤝 ${pname(pid)} took their suggestion back`); trSync(); persist(); return; }
  if (p.to !== pid) return;
  const by = p.by, other = pid;
  if (k === 'yes') {
    G.tr.prop = null; trLog(`🤝 ${pname(pid)} agreed: ${trDescribe(p.action)}`); trTell(pid, 'ok', { text: '🤝 Agreed. Doing it now.' });
    return p.action.op === 'steal' ? trSteal({ ...p.action, who: by }) : trPower({ ...p.action, who: by });
  }
  if (k === 'lose' && p.n >= TR.PROP_MAX) {
    G.tr.prop = null; const lost = trLosePower();
    trLog(`🤝 No agreement after ${TR.PROP_MAX} messages: ${lost ? 'one ' + lost + ' was lost' : 'there was no power left to lose'}`);
    for (const x of trTraitors()) trTell(x, 'ok', { text: lost ? `⚠ No agreement: you lose 1 ${lost}.` : '⚠ No agreement, and no power left to lose.' });
    trSync(); persist();
  }
}
/** Takes one use away from a random power (free answer, block or double) that still has some. Returns what was lost. */
function trLosePower() {
  const live = ['gift', 'block', 'dbl'].filter((k) => G.tr.powers[k] > 0); if (!live.length) return '';
  const k = live[Math.floor(Math.random() * live.length)]; G.tr.powers[k]--; return { gift: 'free answer', block: 'block', dbl: 'double' }[k];
}

/** A demo slide that plays a sample letter: on the big screen and every phone, or ('phones') only on the real players' phones. */
function trDemoLetter(q) {
  if (!trOn() || !q.letter) return;
  if (q.letterMode === 'phones') { for (const p of Object.values(G.players)) if (!p.id.startsWith('p_bot')) trTell(p.id, 'letter', { now: true, text: q.letter }); return; }
  const at = G.qIndex;
  setTimeout(() => { if (G.qIndex === at && G.phase === 'slide' && !G.tr.screen) trPushNotice({ kind: 'notice', title: TR_LETTER_TITLE, letter: q.letter, afterIdx: 0, sound: 'whoosh' }, true); }, 500);
}
// ---------------------------------------------------------------- the Traitor's team: a second phone, secretly the same player
const trTeamFresh = () => ({ open: 0, pending: null, linked: false, traitorDev: '', partnerDev: '', answerDev: '', actDev: '' });
/** What a Traitor's phones are told about their team (pending is the second phone knocking; nobody else ever sees any of this). */
function trTeamPublic(pid) {
  const t = G.tr?.teams?.[pid]; if (!t) return { linked: false, open: false, pending: null };
  return { linked: !!t.linked, open: t.open > Date.now(), pending: t.pending ? { dev: t.pending.dev, name: t.pending.name } : null, answerDev: t.answerDev, actDev: t.actDev, traitorDev: t.traitorDev, partnerDev: t.partnerDev };
}
/** From a phone with TEAM in front of the code ('ask') or from a Traitor's own phone (everything else). */
function onTeam({ op, pid, tmp, dev, name, ...a }) {
  if (!trOn()) return;
  if (op === 'ask') { // a second phone knocks: it is not a player, and has no say until a Traitor lets it in
    if (typeof tmp !== 'string' || !trTraitors().length) return;
    const doors = trTraitors().map((x) => [x, trTeam(x)]).filter(([, t]) => !t.linked && t.open > Date.now()).sort((p, q) => p[1].open - q[1].open);
    if (!doors.length) return trTell(tmp, 'teamno', { why: 'Your teammate has not opened the door yet. Ask them to tap “Open the door for them” on their phone, then try again.' });
    const [, t] = doors[0], nm = String(name || '').replace(/\s+/g, ' ').trim().slice(0, 20) || 'A';
    if (!t.pending || t.pending.tmp !== tmp) { t.pending = { tmp, dev: String(dev || '').slice(0, 24), name: nm }; trLog(`👥 ${nm}'s phone is asking to join a Traitor's team`); trSync(); persist(); }
    return trTell(tmp, 'teamwait', {});
  }
  if (!trIsTraitor(pid)) return; // everything below is a Traitor's own phone
  const tr = pid, t = trTeam(pid);
  if (op === 'open') { t.open = Date.now() + 300000; trSync(); persist(); return; }
  if (op === 'decline') { if (t.pending) trTell(t.pending.tmp, 'teamno', { why: 'Your teammate said no.' }); t.pending = null; trSync(); persist(); return; }
  if (op === 'accept') {
    if (!t.pending) return;
    Object.assign(t, { linked: true, partnerDev: t.pending.dev, traitorDev: String(dev || '').slice(0, 24), open: 0, answerDev: '', actDev: '' });
    trTell(t.pending.tmp, 'teamlinked', { pid: tr, name: G.players[tr]?.name || '', emoji: G.players[tr]?.emoji || '' });
    trLog(`👥 A second phone joined ${pname(tr)}'s team (still one player)`); t.pending = null;
    trSync(); persist(); return trTell(tr, 'teamroles', {});
  }
  if (op === 'roles') {
    if (!t.linked) return; const ans = String(a.answerDev || '');
    if (ans !== t.traitorDev && ans !== t.partnerDev) return;
    t.answerDev = ans; t.actDev = ans === t.traitorDev ? t.partnerDev : t.traitorDev;
    trLog(`👥 ${pname(tr)}'s team chose which phone answers and which does the Traitor actions`);
    trSync(); persist(); return trTell(tr, 'ok', { text: '👥 Done: one phone answers, the other does the Traitor actions. The answering phone gets an alert for each decision.' });
  }
  if (op === 'end') { G.tr.teams[pid] = trTeamFresh(); trLog(`👥 ${pname(tr)}'s second phone was unlinked`); trTell(tr, 'teamended', {}); trSync(); persist(); }
}
/** Counts what the Traitors do (steals, powers set, messages sent) so a quiet stretch can be nudged. */
const trAct = (kind) => { G.tr.act = G.tr.act || { steal: 0, power: 0, msg: 0 }; G.tr.act[kind]++; };
/** Every 20 questions: if the Traitors have not been using what they have, nudge them. Steals and powers but no messages: ask for a message. */
function trPromptActivity() {
  const a = G.tr.act || { steal: 0, power: 0, msg: 0 }, used = a.steal + a.power; let text = '';
  if (!a.msg && !used) text = 'It has gone very quiet. Use a power, steal some points or send a message to keep the game live.';
  else if (!a.msg) text = 'You have been busy with steals and powers, but you have not sent a message. Send one to keep the game live.';
  else if (!used) text = 'You have sent messages, but no steals or powers. Use one to keep the game live.';
  G.tr.act = { steal: 0, power: 0, msg: 0 };
  if (!text) return;
  const who = trTraitors(); if (!who.length) return;
  for (const x of who) { trTell(x, 'ping', { icon: '🗡', text }); }
  trLog(`💬 Prompted the Traitor${who.length > 1 ? 's' : ''}: “${text}”`); persist();
}
/** A clock is running: a question is about to start, is on, or is being marked. */
const trTimerOn = () => ['countdown', 'question', 'grading'].includes(G.phase);
/** A letter for one phone. While a question's clock is running it waits (a letter in the middle of a question costs people time), and goes out as soon as the clock has stopped. */
function trLetterTo(to, text, extra = {}, kind = 'letter') {
  if (!G.players[to]) return;
  if (trTimerOn()) { (G.tr.held = G.tr.held || []).push({ to, text, extra, kind }); persist(); return; }
  trTell(to, kind, { text, ...extra });
}
function trFlushLetters() {
  if (!G.tr?.held?.length || trTimerOn()) return;
  const h = G.tr.held; G.tr.held = [];
  for (const l of h) trTell(l.to, l.kind || 'letter', { text: l.text, ...(l.extra || {}) });
  persist();
}
/** A private word to one phone (or all of them, for ping-style banners). Only the phone it is for acts on it. */
const trTell = (to, kind, data = {}) => send('trs', { to, kind, ...data });
// With a recruit there are two Traitors (G.tr.traitor and G.tr.mate) sharing one set of steals and powers.
const trTraitors = () => [G.tr?.traitor, G.tr?.mate].filter((p) => p && G.players[p]);
const trIsTraitor = (pid) => !!pid && (pid === G.tr?.traitor || pid === G.tr?.mate);
const trOther = (pid) => (pid === G.tr.traitor ? G.tr.mate : pid === G.tr.mate ? G.tr.traitor : null) || null;
const trTeam = (pid) => { G.tr.teams = G.tr.teams || {}; return G.tr.teams[pid] = G.tr.teams[pid] || trTeamFresh(); };
const trWho = (pid) => (G.players[pid] ? { pid, name: G.players[pid].name, emoji: G.players[pid].emoji || '' } : null);
function trSync() { for (const t of trTraitors()) trSyncOne(t); }
function trSyncOne(t) {
  if (!t || !G.players[t]) return;
  const qd = G.tr.qDone, victims = {};
  for (const p of Object.keys(G.players)) if (!trIsTraitor(p)) victims[p] = { wait: Math.max(0, TR.SAME_VICTIM - (qd - (G.tr.victimQ[p] ?? -99))), score: G.players[p].score };
  trTell(t, 'sync', { d: { powers: G.tr.powers, set: G.tr.set, canSteal: (G.tr.stealsHalf || 0) < TR.STEALS, stealsLeft: Math.max(0, TR.STEALS - (G.tr.stealsHalf || 0)), victims, window: trWindow(), nextPlain: powerNextPlain() >= 0, msgsLeft: Math.max(0, TR.MSGS - G.tr.msgBreak), hold: trHoldOn(), team: trTeamPublic(t), me: t, mate: trWho(trOther(t)), prop: trPropFor(t), chat: (G.tr.chat || []).slice(-30), recruited: t === G.tr.mate,
    needList: !!(G.tr.tableDone && G.tr.twoAtHalf && !G.tr.lists?.[t]), list: G.tr.lists?.[t] || null, qDone: qd, players: Object.values(G.players).filter((p) => p.id !== t).map((p) => ({ pid: p.id, name: p.name, emoji: p.emoji || '' })) } });
}
/** A phone says hello (joining, or coming back after a drop): a Traitor is reminded who they are. */
function trOnHello(pid) { if (trOn() && trIsTraitor(pid)) { trTell(pid, 'role', { again: true, reason: G.tr.history.at(-1)?.reason, n: G.tr.history.length, recruited: pid === G.tr.mate, mate: trWho(trOther(pid)) }); trSync(); } }

// ---------------------------------------------------------------- picking the Traitor
function trSetTraitor(pid, reason = 'picked') {
  trEnsure(); if (!trOn() || !G.players[pid]) return false;
  for (const x of trTraitors()) { if (G.tr.teams?.[x]?.linked) trTell(x, 'teamended', {}); if (x !== pid) trTell(x, 'unrecruited', {}); } // old Traitors' second phones are just second phones now
  Object.assign(G.tr, { teams: {}, mate: null, prop: null, chat: [] });
  G.tr.traitor = pid; G.tr.history.push({ pid, at: G.tr.qDone, reason }); (G.tr.roster = G.tr.roster || []).includes(pid) || G.tr.roster.push(pid);
  Object.assign(G.tr, { powers: trFresh(), set: { gift: null, block: null, dbl: null }, used: { gift: 0, block: 0, dbl: 0 }, lastStealQ: -99, stealsHalf: 0, victimQ: {}, lists: {}, needTwo: false, twoAtHalf: false, msgBreak: 0, hold: null });
  trLog(`${pname(pid)} is the Traitor (${reason})`);
  trTell(pid, 'role', { reason, n: G.tr.history.length }); trSync(); persist(); broadcastState();
  if (G.phase === 'lobby') render(); // the lobby says a Traitor is picked
  return true;
}

// ---------------------------------------------------------------- the Traitor's actions (from their phone)
/** Between questions: the same break the power cards are played in. Not while a vote or a notice is up. */
/** The Traitor can act at any time, before or during a question (not in the lobby, the final results, or while the Round Table vote is up). A power set while a question is running counts on the next one. */
function trWindow() { return trOn() && !['lobby', 'final'].includes(G.phase) && !(G.tr.screen && ['table', 'chosen', 'verdict', 'final'].includes(G.tr.screen.kind)); }
const trNo = (why, who) => trTell(who || G.tr.traitor, 'no', { why });
function onTr({ pid, op, ...a }) {
  if (!trOn() || !G.players[pid]) return;
  if (op === 'sync') { if (trIsTraitor(pid)) trSync(); return; }
  if (op === 'vote') return trVote(pid, a.target);
  if (op === 'claudia') return trClaudiaReply(pid, a);
  if (!trIsTraitor(pid)) return;
  if (op === 'hold') return trHold(!!a.on, a.what);
  if (op === 'msg') return trMsg({ ...a, who: pid });
  if (op === 'tchat') return trChat(pid, a.text);
  if (op === 'prop') return trPropReply(pid, a.k);
  if (op === 'steal' || op === 'power') return G.tr.mate ? trPropose(pid, op, a) : (op === 'steal' ? trSteal({ ...a, who: pid }) : trPower({ ...a, who: pid }));
  if (op === 'list') return trList({ ...a, who: pid });
}
function trSteal({ victim, amount, to, show, who }) {
  const t = who || G.tr.traitor, qd = G.tr.qDone, trNo = (why) => trTell(t, 'no', { why });
  if (!trWindow()) return trNo('Not right now: the vote is on.');
  if ((G.tr.stealsHalf || 0) >= TR.STEALS) return trNo(`You have used all ${TR.STEALS} steals for this half. They come back at half time.`);
  if (!G.players[victim] || trIsTraitor(victim)) return trNo('Pick someone else to steal from.');
  if (!G.players[to] || to === victim) return trNo('Give the points to someone other than the player you took them from (you can keep them yourself, but they only count for show).');
  const wait = TR.SAME_VICTIM - (qd - (G.tr.victimQ[victim] ?? -99)); if (wait > 0) return trNo(`You can only steal from ${pname(victim)} once every ${TR.SAME_VICTIM} questions: ${wait} more to go.`);
  const want = Math.round((+amount || 0) / 100) * 100; if (want < TR.MIN || want > TR.MAX) return trNo(`Steal between ${TR.MIN} and ${TR.MAX}.`);
  const amt = Math.min(want, Math.max(0, G.players[victim].score)); if (amt <= 0) return trNo(`${pname(victim)} has no points to steal.`);
  if (trShielded(victim)) return trShieldHeld('steal', { t, victim, to, amt }); // the Traitor only finds out by trying
  G.players[victim].score -= amt; G.players[to].score += amt;
  if (trIsTraitor(to)) { G.tr.fake = G.tr.fake || {}; G.tr.fake[to] = (G.tr.fake[to] || 0) + amt; } // kept by a Traitor: only for show, it comes off again at the very end
  G.tr.lastStealQ = qd; G.tr.victimQ[victim] = qd; G.tr.stolen += amt; G.tr.steals++; G.tr.stealsHalf = (G.tr.stealsHalf || 0) + 1;
  const afterIdx = ['reveal', 'scoreboard', 'slide'].includes(G.phase) ? G.qIndex + 1 : G.qIndex; // the question that comes next: the notice follows it
  if (show === 'secret') trLetterTo(victim, TR_SAY.steal2(trIsTraitor(to) ? null : pname(to), amt.toLocaleString('en-GB')));
  else {
    G.tr.notices.push({ kind: 'notice', title: TR_LETTER_TITLE, letter: TR_SAY.steal(pname(victim), trIsTraitor(to) ? null : pname(to), amt.toLocaleString('en-GB')), afterIdx, sound: 'whoosh',
      lines: G.tr.stealShown ? [] : ['At half time you will have the chance to "banish" who you think the Traitor is. If you are right, they lose their power and 5,000 points, and everyone who voted for them wins 2,000.'] });
    G.tr.stealShown = true;
  }
  trLog(`💰 Stole ${amt} from ${pname(victim)} and gave it to ${trIsTraitor(to) ? (to === t ? 'themselves' : 'their teammate') + ' (for show)' : pname(to)} · ${show === 'secret' ? '🤫 only ' + pname(victim) + ' sees the letter' : '📺 letter on the big screen'}`);
  trAct('steal'); trTell(t, 'ok', { text: `🗡 Done: ${amt} points taken from ${pname(victim)} and ${to === t ? 'kept for yourself (only for show: they come off at the end)' : 'given to ' + pname(to)}.` }); trHoldClear();
  trSync(); persist(); broadcastState(); if (['reveal', 'scoreboard'].includes(G.phase)) render();
}
/** A steal or a block aimed at someone with a shield. The Traitor is never told who has one: they find out by trying, and the attempt is still used up.
 *  The Traitor hears it failed because of a shield; the player is told exactly what was tried, and that sharing it is up to them. */
function trShieldHeld(kind, { t, victim, to, amt }) {
  const qd = G.tr.qDone, who = pname(victim), steal = kind === 'steal';
  if (steal) { G.tr.lastStealQ = qd; G.tr.victimQ[victim] = qd; G.tr.stealsHalf = (G.tr.stealsHalf || 0) + 1; }
  else { G.tr.powers.block = Math.max(0, G.tr.powers.block - 1); G.tr.used.block++; }
  trTell(t, 'ping', { icon: '🛡', text: steal ? `Your steal from ${who} failed: they had a shield. It still counts as one of your steals.` : `Your block on ${who} failed: they had a shield. It still counts as one of your blocks.` });
  trLetterTo(victim, steal ? `The Traitor tried to steal ${amt.toLocaleString('en-GB')} of your points and ${trIsTraitor(to) ? 'keep them' : 'give them to ' + pname(to)}. Your shield stopped it.` : 'The Traitor tried to block you from the next question. Your shield stopped it.', {}, 'shielded');
  trLog(`🛡 ${steal ? `Steal of ${amt} from ${who}` : `Block on ${who}`} FAILED: they had a shield (both sides have been told)`);
  trAct(steal ? 'steal' : 'power'); trHoldClear(); trSync(); persist();
}
function trPower({ kind, target, show, who }) {
  const t = who || G.tr.traitor, trNo = (why) => trTell(t, 'no', { why }); if (!['gift', 'block', 'dbl'].includes(kind)) return;
  if (!trWindow()) return trNo('Not right now: the vote is on.');
  if (powerNextPlain() < 0) return trNo('There is no everyone-answers question left to use it on.');
  if (G.tr.said?.[kind]) return trNo('That one has already been announced for the next question, so it can not be changed now.');
  if (target === null || target === undefined || target === '') { G.tr.set[kind] = null; trSync(); persist(); trLog(`↩ Took back the ${{ gift: 'free answer', block: 'block', dbl: 'double' }[kind]}`); return trTell(t, 'ok', { text: 'Taken back: it is not used.' }); }
  if (!G.players[target]) return;
  if (G.tr.powers[kind] <= 0) return trNo('You have none of those left.');
  for (const k of ['gift', 'block', 'dbl']) if (k !== kind && G.tr.set[k] === target) return trNo(`${pname(target)} already has something from you for the next question.`);
  if (kind === 'block' && !trIsTraitor(target) && trShielded(target)) return trShieldHeld('block', { t, victim: target });
  trAct('power'); trHoldClear(); G.tr.set[kind] = target; (G.tr.show = G.tr.show || {})[kind] = show === 'secret' ? 'secret' : 'screen'; (G.tr.said = G.tr.said || {})[kind] = true;
  // the letter goes out now, before the question it is about, so there is time to read it (held until the clock stops if a question is on)
  if (show === 'secret') { if (!trIsTraitor(target)) trLetterTo(target, TR_SAY[kind + '2']()); }
  else trPushNotice({ kind: 'notice', title: TR_LETTER_TITLE, letter: TR_SAY[kind](pname(target)), afterIdx: 0, sound: 'whoosh' }, true);
  trSync(); persist();
  trLog(`${{ gift: '🎁 Free answer', block: '🚫 Block', dbl: '✨ Double' }[kind]} lined up for ${target === t ? 'themselves (for show)' : pname(target)} on the next question · ${show === 'secret' ? '🤫 only they see the letter' : '📺 letter on the big screen before it'}`);
  trTell(t, 'ok', { text: { gift: `🎁 ${target === t ? 'You' : pname(target)} will get a free answer on the next question.`, block: `🚫 ${target === t ? 'You' : pname(target)} will be blocked from the next question.`, dbl: `✨ ${target === t ? 'Your' : pname(target) + "'s"} points will be doubled on the next question.` }[kind] });
}
function trMsg({ to, text, who }) {
  const t = who || G.tr.traitor, trNo = (why) => trTell(t, 'no', { why }), msg = String(text || '').replace(/\s+/g, ' ').trim().slice(0, TR.MSG_LEN);
  if (!msg) return trNo('Write a message first.');
  if (G.tr.msgBreak >= TR.MSGS) return trNo(`That's ${TR.MSGS} messages for this break. Wait for the next question.`);
  if (to !== 'all' && (!G.players[to] || trIsTraitor(to))) return trNo('Pick someone to send it to.');
  G.tr.msgBreak++; G.tr.msgs++;
  if (to === 'all') { trPushNotice({ kind: 'notice', title: TR_LETTER_TITLE, letter: msg, afterIdx: 0, sound: 'whoosh' }, true); trLog(`📜 Message to EVERYONE (big screen): “${msg}”`); }
  else { trLetterTo(to, msg, { note: trPick(TR_SECRET_NOTES) }, 'msg'); trLog(`🤫 Secret message to ${pname(to)}: “${msg}”`); }
  trAct('msg'); trTell(t, 'ok', { text: to === 'all' ? '📜 Sent to everyone.' : `🤫 Sent to ${pname(to)}.` }); trHoldClear(); trSync(); persist();
}
function trList({ items, who }) {
  if (!Array.isArray(items) || !trIsTraitor(who)) return;
  const trNo = (why) => trTell(who, 'no', { why });
  const list = items.map((x, i) => ({ id: 'c' + (i + 1), text: String(x.text || '').trim().slice(0, 90), yes: !!x.yes, own: !!x.own })).filter((x) => x.text).slice(0, 90);
  if (list.filter((x) => x.yes).length < 3) return trNo('Tick at least 3 that are true of you.');
  (G.tr.lists = G.tr.lists || {})[who] = list; trLog(`📋 ${pname(who)}'s 20 Questions list is in (${list.length} questions)`); trTell(who, 'ok', { text: '✅ Your list is saved. Honesty is the whole game!' }); trHoldClear(); trSync(); persist();
  if (G.phase === 'slide') render(); // the half-time button was waiting for it
}
/** A notice for the screen (and the phones). It waits for the host's NEXT CLICK (primaryAction): it never appears in the middle of a screen that is being shown. */
function trPushNotice(n) {
  G.tr.notices.push(n);
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
  G.tr.said = {}; // the next ones can be chosen
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
  if (G.tr.qDone % TR.PROMPT_EVERY === 0) trPromptActivity();
  if (!partyPlain(q)) return trSync();
  const fx = G.q.trfx || {}, full = Math.round(+G.quiz.settings.maxPoints || 1000);
  // streaks and shields count what people really answered, before the Traitor's gifts
  for (const pid of Object.keys(G.players)) {
    const r = byPlayer[pid], right = !!r?.correct && !r.frozen && fx.block !== pid;
    if (trShielded(pid) && !right && fx.block !== pid) { G.tr.shield[pid] = 0; trTell(pid, 'ping', { icon: '🛡', text: "Wrong answer: your shield is gone. The Traitor's steals and blocks can work on you again." }); }
    G.tr.streak[pid] = right ? (G.tr.streak[pid] || 0) + 1 : 0;
    if (G.tr.streak[pid] >= 3) { G.tr.streak[pid] = 0; if (!trShielded(pid)) { G.tr.shield[pid] = 1; trTell(pid, 'ping', { icon: '🛡', text: "Shield earned! The Traitor's steals and blocks will fail against you until you get one wrong." }); } }
  }
  const owns = {}; for (const x of trTraitors()) owns[x] = byPlayer[x]?.points || 0;
  if (fx.block) { const r = byPlayer[fx.block] = byPlayer[fx.block] || blank(); r.points = 0; r.correct = false; r.partial = 0; r.blocked = true; partyNote(r, '🚫 The Traitor blocked you from this question'); }
  if (fx.gift) { const r = byPlayer[fx.gift] = byPlayer[fx.gift] || blank(); r.answered = true; r.points = Math.max(r.points || 0, full); r.correct = true; r.partial = 1; partyNote(r, '🎁 The Traitor gifted you full points!'); }
  if (fx.dbl) { const r = byPlayer[fx.dbl] = byPlayer[fx.dbl] || blank(); if (r.points > 0) { r.points *= 2; partyNote(r, '✨ The Traitor doubled your points!'); } else partyNote(r, '✨ Doubled… but double nothing is nothing'); }
  for (const t of trTraitors()) if (fx.block !== t && (fx.gift === t || fx.dbl === t)) { // what a Traitor is given by their own side is only for show: it comes off again at the very end
    const extra = Math.max(0, (byPlayer[t]?.points || 0) - (owns[t] || 0));
    if (extra) { G.tr.fake = G.tr.fake || {}; G.tr.fake[t] = (G.tr.fake[t] || 0) + extra; trLog(`🎭 ${extra} points ${pname(t)} was given by the Traitors, for show only`); }
  }
  trSync();
}

// ---------------------------------------------------------------- the game pauses: notices up on the host screen and the phones
/** After a question (reveal, scoreboard): a waiting notice goes up. Returns true if it did. */
function trInterlude(now, resume) {
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
  G.tr.screen = { id: uid('s'), kind: 'notice', title: n.title, lines: n.lines || [], quote: n.quote || '', letter: n.letter || '', cont: !now && !resume }; // resume: the click that brought it up is given back once it is read, so the screen underneath carries on from where it was
  persist(); sound(n.sound || (n.letter ? 'whoosh' : 'gong')); render(); broadcastState();
  return true;
}
/** The host presses Next on a Traitors screen. */
function trScreenNext() {
  const sc = G.tr.screen; if (!sc) return false;
  if (sc.kind === 'notice') { G.tr.screen = null; persist(); broadcastState(); if (sc.cont) nextFrom(G.qIndex); else render(); return true; }
  if (sc.kind === 'table') { trLockVotes(); return true; }
  if (sc.kind === 'chosen') { trReveal(); return true; }
  if (sc.kind === 'verdict' && sc.final) { G.tr.screen = null; G.tr.finalDone = true; persist(); trSync(); broadcastState(); nextFrom(G.qIndex); return true; } // the last vote is over: on to the 20 Questions, or the reveal
  if (sc.kind === 'verdict') { G.tr.screen = null; G.tr.tableDone = true; trHalfReset(); persist(); trSync(); trNudgeList(); broadcastState(); goTo(sc.next); return true; }
  if (sc.kind === 'final') { G.tr.screen = null; G.tr.revealed = true; persist(); broadcastState(); finish(); return true; }
  return false;
}

// ---------------------------------------------------------------- half time: the Round Table and the vote
/** Half time: the steals and powers all come back, for the same Traitor or a new one. */
function trHalfReset() {
  G.tr.powers = trFresh(); G.tr.stealsHalf = 0;
  trLog(`Half time: ${TR.STEALS} steals and ${TR.USES} of each power are back`);
  for (const x of trTraitors()) trTell(x, 'ok', { text: `✨ Half time: your ${TR.STEALS} steals and ${TR.USES} of each power are back for the second half.` });
}
/** Item index of half time: the first break slide, else the middle of the quiz. */
function trHalfIndex() { const qs = G.quiz.questions, b = qs.findIndex((x) => x.type === 'slide' && x.break); return b >= 0 ? b : Math.floor(qs.length / 2); }
const trWantsTable = (i) => trOn() && G.tr.traitor && !G.tr.tableDone && trHalfIndex() === i + 1 && i + 1 < G.quiz.questions.length;
/** Half time is over the Traitor's list: no list, no last round. True while a real Traitor has yet to save it (a bot Traitor can't, and the host can waive it). */
/** What half time is still waiting for: the Traitor's answer about a recruit, the host picking two new Traitors, and (once there are two Traitors) each one's honest list. Empty when nothing is. */
function trWaitingFor() {
  if (!trOn() || !G.tr.tableDone || G.tr.listWaived) return [];
  const out = [], rc = G.tr.recruit?.stage;
  if (G.tr.needTwo) out.push('you to pick the two new Traitors (on your phone)');
  if (['offer', 'pick', 'invite'].includes(rc) && G.tr.traitor && !String(G.tr.traitor).startsWith('p_bot')) out.push(`${pname(G.tr.traitor)} to answer Claudia about recruiting`);
  if (G.tr.twoAtHalf) for (const x of trTraitors()) if (!String(x).startsWith('p_bot') && !G.tr.lists?.[x]) out.push(`${pname(x)}'s list`);
  return out;
}
const trListPending = () => trWaitingFor().length > 0;
/** The Traitors' phones open the list and buzz. */
const trNudgeList = () => { if (G.tr.twoAtHalf && G.tr.tableDone) for (const x of trTraitors()) if (!String(x).startsWith('p_bot') && !G.tr.lists?.[x]) trTell(x, 'listnow', { text: "Save your list! The quiz can't carry on without it." }); };
/** The host tried to leave half time while something is outstanding: hold them here unless they choose to carry on without. */
function trHoldForList(i) {
  trNudgeList(); render();
  const w = trWaitingFor();
  return ask('Waiting at half time', `Still waiting for ${w.join(', ')}. Without that, the last round (the 20 Questions) will not happen.`, 'Keep waiting', 'Carry on without').then((wait) => {
    if (wait) return;
    G.tr.listWaived = true; G.tr.needTwo = false; trLog('The host carried on without waiting: no 20 Questions'); persist(); render(); nextFrom(i);
  });
}
/** The host picks two new Traitors (after a Traitor was caught at half time). */
function trPickTwo(a, b) {
  if (!trOn() || a === b || !G.players[a] || !G.players[b]) return false;
  G.tr.traitor = null; G.tr.mate = null;
  trSetTraitor(a, 'new'); G.tr.mate = b; (G.tr.roster = G.tr.roster || []).includes(b) || G.tr.roster.push(b);
  Object.assign(G.tr, { recruitOffered: true, recruit: { stage: 'done' }, twoAtHalf: true, needTwo: false, chat: [] });
  trLog(`🗡 You picked two new Traitors: ${pname(a)} and ${pname(b)}`);
  trTell(b, 'role', { reason: 'picked2', recruited: true, mate: trWho(a), n: G.tr.history.length }); trTell(a, 'mate', { mate: trWho(b) });
  trSync(); trNudgeList(); persist(); broadcastState(); return true;
}
let trTickT = null;
function trTable(i, final) {
  clearInterval(tickT); clearInterval(countT);
  G.tr.votes = {}; G.tr.screen = { id: uid('s'), kind: 'table', endsAt: Date.now() + TR.TABLE_MS, total: TR.TABLE_MS, next: i + 1, final: !!final };
  persist(); sound('drumroll'); render(); broadcastState(); trStartTick();
  for (const b of G.bots || []) botLater(() => { const sc = G.tr?.screen; if (sc?.kind !== 'table' || sc.locked) return; const others = Object.keys(G.players).filter((p) => p !== b.pid); trVote(b.pid, chance(0.45) && !trIsTraitor(b.pid) && trTraitors()[0] ? trTraitors()[0] : others[Math.floor(Math.random() * others.length)]); }, rnd(15000, 150000));
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
  const { rows, banished, tie } = sc, final = !!sc.final, correct = !!banished && trIsTraitor(banished), traitor = banished;
  let winners = [], wrongVoters = [];
  if (correct) {
    G.players[traitor].score -= TR.BANISH_LOSS;
    winners = Object.entries(G.tr.votes).filter(([v, t]) => t === traitor && v !== traitor).map(([v]) => v);
    for (const v of winners) G.players[v].score += TR.VOTER_BONUS;
    (final ? G.tr.banishedFinal : G.tr.banishedBefore).push(traitor); trLog(`${pname(traitor)} was banished${final ? ' at the FINAL Round Table' : ''} (right!): -${TR.BANISH_LOSS}, ${winners.length} voters +${TR.VOTER_BONUS}`);
    trTell(traitor, 'banished', { text: `You were banished! You lose your power and ${TR.BANISH_LOSS.toLocaleString('en-GB')} points.` });
    if (!final) { // the first vote: that Traitor is out, and the host picks two new ones
      for (const x of trTraitors()) if (x !== traitor) trTell(x, 'banished', { text: 'The room found your team.' });
      Object.assign(G.tr, { traitor: null, mate: null, teams: {}, prop: null, chat: [], needTwo: true, twoAtHalf: false, lists: {} });
      trLog('🎲 The host picks two new Traitors (on your phone)');
    } else { // the last vote: that Traitor is out; the other one, if there is one, carries on to the 20 Questions
      const left = trOther(traitor); if (G.tr.teams) delete G.tr.teams[traitor];
      G.tr.traitor = left || null; G.tr.mate = null; G.tr.prop = null; G.tr.chat = [];
      if (left) trTell(left, 'unrecruited', {});
    }
  } else {
    G.tr.hidden += TR.SLIP_BONUS; if (G.tr.mate) G.tr.hiddenMate = (G.tr.hiddenMate || 0) + TR.SLIP_BONUS; trLog(`The vote missed (${banished ? pname(banished) : 'a tie'}): ${TR.SLIP_BONUS} held back for the Traitor${G.tr.mate ? 's' : ''}`);
    if (banished && G.players[banished]) {
      G.players[banished].score -= TR.WRONG_LOSS; trLog(`${pname(banished)} was wrongly accused: -${TR.WRONG_LOSS}`); trTell(banished, 'ping', { icon: '😬', text: `You were wrongly accused! You lose ${TR.WRONG_LOSS.toLocaleString('en-GB')} points.` });
      wrongVoters = Object.entries(G.tr.votes).filter(([v, t]) => t === banished && v !== banished && G.players[v]).map(([v]) => v);
      for (const v of wrongVoters) { G.players[v].score -= TR.WRONG_LOSS; trTell(v, 'ping', { icon: '😬', text: `You voted for the wrong person: you lose ${TR.WRONG_LOSS.toLocaleString('en-GB')} points.` }); }
      if (wrongVoters.length) trLog(`${wrongVoters.length} voters for the wrong person: -${TR.WRONG_LOSS} each`);
    }
  }
  sc.kind = 'verdict'; sc.id = uid('s'); Object.assign(sc, { rows, banished, correct: !!correct, winners, wrongVoters, tie, locked: true, wrongLoss: !!banished && !correct, final });
  persist(); sound(correct ? 'fanfare' : 'trombone'); render(); broadcastState(); if (correct) confetti();
  if (!correct && !final) trOfferRecruit(); // not found, at half time: Claudia has a word with the Traitor
}

// ---------------------------------------------------------------- the last round: the Traitor's 20 Questions
/** The 20 Questions happen only if there were two Traitors at half time and one is still in (and its list is in). */
const trTwentyOn = () => !!G.tr.twoAtHalf && !G.tr.listWaived && trTraitors().some((x) => G.tr.lists?.[x]?.length);
/** nextFrom's turn, after the last item: the FINAL Round Table, then the 20 Questions (if there are any), then the reveal. Returns true if it took over. */
function trEnd() {
  if (!trOn() || !(G.tr.roster || []).length) return false;
  if (!G.tr.finalDone && trTraitors().length && !G.tr.screen) { trTable(G.quiz.questions.length - 1, true); return true; }
  if (!G.tr.twentyAdded && trTwentyOn()) {
    G.tr.twentyAdded = true;
    const withList = trTraitors().filter((x) => G.tr.lists?.[x]?.length), rem = trTraitors(), last = G.quiz.questions[G.quiz.questions.length - 1], q = LQ.newQuestion('twenty', G.quiz.settings);
    const live = withList[Math.floor(Math.random() * withList.length)]; // two lists would contradict each other: one Traitor's questions go live, for everyone
    const names = rem.flatMap((x) => [pname(x), pname(x).split(/\s+/)[0]]);
    trLog(`🗡 20 Questions: ${pname(live)}'s questions are live${rem.length > 1 ? ' (finding either Traitor wins)' : ''}`);
    Object.assign(q, { text: rem.length === 1 ? '🗡 The Traitor\'s 20 Questions: who is the Traitor?' : '🗡 The Traitors\' 20 Questions: who are the Traitors?', answers: names, what: 'c_kind', customKind: { text: 'Is it one of tonight\'s players?' }, skipKind: true, trTwenty: true, trBonus: TR.FINDER_BONUS,
      custom: G.tr.lists[live].map((x) => ({ ...x })), prize: 0, prize2: 0, prize3: 0, penalty: 0, maxQ: 20, time: 600, round: last?.round });
    G.quiz.questions.push(q); persist();
    return goTo(G.quiz.questions.length - 1), true;
  }
  if (!G.tr.revealed && !G.tr.screen) { trShowFinal(); return true; }
  return false;
}
function trAfterTwenty(byPlayer) {
  const tq = G.q.tq?.players || {}, others = Object.keys(G.players).filter((p) => !trIsTraitor(p));
  const right = others.filter((p) => tq[p]?.done), most = right.length > others.length / 2;
  for (const t of trTraitors()) {
    const r = byPlayer[t] = byPlayer[t] || { answered: false, correct: false, partial: 0, points: 0 };
    if (most) { r.points -= TR.CAUGHT_LOSS; partyNote(r, `🗡 Found out by most of the room: −${TR.CAUGHT_LOSS.toLocaleString('en-GB')}`); }
  }
  if (!most) { G.tr.hidden += TR.AWAY_BONUS; if (G.tr.mate) G.tr.hiddenMate = (G.tr.hiddenMate || 0) + TR.AWAY_BONUS; }
  G.tr.found = { right, most };
  trLog(`20 Questions: ${right.length} of ${others.length} found the Traitor. ${most ? 'Caught' : 'Got away with it'}`);
}
function trShowFinal() {
  const t = G.tr.traitor, f = G.tr.found, lines = [];
  lines.push(`Over the night: ${G.tr.steals} steal${G.tr.steals === 1 ? '' : 's'}, ${G.tr.stolen.toLocaleString('en-GB')} points taken in all.`);
  const u = G.tr.used; lines.push(`🎁 ${u.gift} free answer${u.gift === 1 ? '' : 's'} · 🚫 ${u.block} block${u.block === 1 ? '' : 's'} · ✨ ${u.dbl} double${u.dbl === 1 ? '' : 's'} · 📜 ${G.tr.msgs} message${G.tr.msgs === 1 ? '' : 's'}.`);
  if (G.tr.banishedBefore.length) lines.push(`${trNames(G.tr.banishedBefore)} ${G.tr.banishedBefore.length === 1 ? 'was' : 'were'} banished at half time.`);
  if (G.tr.banishedFinal?.length) lines.push(`${trNames(G.tr.banishedFinal)} ${G.tr.banishedFinal.length === 1 ? 'was' : 'were'} banished at the final Round Table.`);
  if (f) lines.push(f.most ? `Most of the room worked it out: caught, and they lose ${TR.CAUGHT_LOSS.toLocaleString('en-GB')}.` : `Most of the room never worked it out: they get away with it, plus a ${TR.AWAY_BONUS.toLocaleString('en-GB')} bonus.`);
  const fake = Object.values(G.tr.fake || {}).reduce((a, b) => a + b, 0);
  if (fake) lines.push(`The ${fake.toLocaleString('en-GB')} points they gave themselves were only for show: they come off now.`);
  if (G.tr.hidden && !f?.most) lines.push(`Their secret bonuses, ${G.tr.hidden.toLocaleString('en-GB')} points, are added now.`);
  G.tr.screen = { id: uid('s'), kind: 'final', traitor: t, roster: (G.tr.roster || []).slice(), lines };
  persist(); sound('fanfare'); render(); broadcastState(); confetti();
}

/** The Traitor's hidden bonuses are added to their score at the very end (finish() calls this, so ending the game early pays them too). */
function trPayHidden() {
  if (!trOn()) return; G.tr.screen = null;
  const t = G.tr.traitor; if (t && G.players[t] && G.tr.hidden) { G.players[t].score += G.tr.hidden; trLog(`Hidden bonuses paid out: ${G.tr.hidden}`); G.tr.hidden = 0; persist(); }
  const m = G.tr.mate; if (m && G.players[m] && G.tr.hiddenMate) { G.players[m].score += G.tr.hiddenMate; trLog(`Hidden bonus paid out to ${pname(m)}: ${G.tr.hiddenMate}`); G.tr.hiddenMate = 0; persist(); }
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
    return wrap(`<div class="trbig">🕯 THE ${sc.final ? 'FINAL ' : ''}ROUND TABLE</div><p class="trline">${sc.final ? 'This is your last chance to catch them.' : 'One of you is the Traitor.'} Talk it over, then vote on your phone for who to banish.</p>
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
    const verdict = sc.tie ? 'The votes were split. Nobody is banished. The Traitor lives on…' : !top ? 'Nobody voted, so nobody is banished.' : sc.correct ? `…and ${esc(pname(top))} WAS the Traitor! They lose their power and ${TR.BANISH_LOSS.toLocaleString('en-GB')} points. Two new Traitors will be chosen, in secret.` : `…but ${esc(pname(top))} was NOT the Traitor. Wrongly accused: they lose ${TR.WRONG_LOSS.toLocaleString('en-GB')} points. The Traitor is still among you, and stays for the second half.`;
    return wrap(`<div class="trbig">${head}</div><div class="trbars">${sc.rows.map((r) => `<div class="trbar"><span class="trbn">${esc(pem(r.pid))} ${esc(pname(r.pid))}</span><i style="width:${Math.max(6, r.n / mx * 100)}%"></i><b>${r.n}</b></div>`).join('')}</div>
      <p class="trline">${verdict}</p>${sc.correct && sc.winners.length ? `<p class="trline">🏅 Right: ${esc(trNames(sc.winners))} win ${TR.VOTER_BONUS.toLocaleString('en-GB')} each.</p>` : ''}${sc.wrongLoss && sc.wrongVoters?.length ? `<p class="trline">😬 Wrong: ${esc(trNames(sc.wrongVoters))} voted for them, so ${sc.wrongVoters.length === 1 ? 'they lose' : 'they each lose'} ${TR.WRONG_LOSS.toLocaleString('en-GB')} too.</p>` : ''}`, nextBtn('On to half time ▶'));
  }
  if (sc.kind === 'final') return wrap(`<div class="trsmall">THE TRAIT${(sc.roster || []).length > 1 ? 'ORS WERE' : 'OR WAS'}…</div><div class="trbig trname">${(sc.roster || [sc.traitor]).map((x) => `${esc(pem(x))} ${esc(pname(x))}`).join(' and ')}</div>${sc.lines.map((l) => `<p class="trline">${esc(l)}</p>`).join('')}`, nextBtn('Final results 🏆'));
}

// ---------------------------------------------------------------- the host's phone: the control panel (sealed messages)
/** A message from the builder's 🗡 Traitors panel: sealed with the host password, so the players on the same channel can't read or fake it. */
async function onTrCtl(payload) {
  const pw = LQ.hostPassword(); if (!pw || !payload?.m) return;
  let m; try { m = await LQ.unseal(pw, G.code, payload.m); } catch { return; }
  if (!m || Math.abs(Date.now() - (+m.ts || 0)) > 120000 || (G.trCtlNonce && +m.ts <= G.trCtlNonce)) return;
  G.trCtlNonce = +m.ts; trEnsure();
  let note = '';
  if (m.op === 'cuedone') { (G.cueDone = G.cueDone || {})[String(m.id)] = 1; persist(); }
  else if (!trOn()) note = 'Traitors mode is not switched on for this quiz (Settings).';
  else if (m.op === 'pick') note = trSetTraitor(m.pid, 'picked') ? '' : 'That player is not in the game.';
  else if (m.op === 'pick2') { note = trPickTwo(m.a, m.b) ? '' : 'Choose two different players who are in the game.'; }
  else if (m.op === 'random2') { const pool = Object.keys(G.players).filter((p) => !p.startsWith('p_bot')); if (pool.length >= 2) { const a = pool.splice(Math.floor(Math.random() * pool.length), 1)[0], b = pool[Math.floor(Math.random() * pool.length)]; trPickTwo(a, b); } else note = 'Need at least two real players.'; }
  else if (m.op === 'tell') { note = trTellTraitors(String(m.text || ''), m.to); }
  else if (m.op === 'random') { const pool = Object.keys(G.players); if (pool.length) trSetTraitor(pool[Math.floor(Math.random() * pool.length)], 'picked'); else note = 'Nobody has joined yet.'; }
  await trCtlSend(note, pw);
}
/** "I Literally Just Told You" stunts: a question can carry q.cue = { n, title, say }. The host's phone panel shows it as a big green pop-up once it is due: the item is next (we are between questions or on a slide) or on (the round card, countdown, or the question itself). It goes when the host taps Done or the game moves past it. */
function ilCueDue() {
  if (typeof G === 'undefined' || !G?.quiz?.questions || G.qIndex == null || G.qIndex < 0 || ['lobby', 'final'].includes(G.phase)) return null;
  const qs = G.quiz.questions, i = ['round', 'typecard', 'countdown', 'question'].includes(G.phase) ? G.qIndex : ['reveal', 'scoreboard', 'grading', 'slide'].includes(G.phase) ? G.qIndex + 1 : -1;
  const q = qs[i], c = q?.cue; if (!c || G.cueDone?.[q.id]) return null;
  return { id: q.id, n: c.n || 0, title: String(c.title || 'Stunt'), say: String(c.say || ''), item: i + 1 };
}
let ilCueKey = '';
/** Called with every state broadcast: when a cue becomes due (or stops being due) the phone panel is told at once. */
function ilCuePush() { const c = ilCueDue(), k = c ? c.id : ''; if (k === ilCueKey) return; ilCueKey = k; trCtlPushSoon(); }
/** What the host's phone panel is shown: it is also pushed unasked when the Traitor asks for a hold. */
async function trCtlSend(note = '', pw = LQ.hostPassword()) {
  if (!pw || typeof G === 'undefined' || !G?.code) return;
  const t = trOn() ? G.tr : null;
  const reply = { ts: Date.now(), note, cue: ilCueDue(), on: !!t, players: Object.values(G.players).map((p) => ({ pid: p.id, name: p.name, emoji: p.emoji || '', score: p.score, bot: p.id.startsWith('p_bot') })),
    traitor: t?.traitor || null, mate: t?.mate || null, needTwo: !!t?.needTwo, powers: t?.powers, qDone: t?.qDone, tableDone: t?.tableDone, hidden: t?.hidden, listIn: !!t?.list, hold: trHoldOn(), stealsLeft: t ? Math.max(0, TR.STEALS - (t.stealsHalf || 0)) : null, set: t?.set, phase: G.phase, log: (t?.log || []).slice(-40) };
  send('trctlr', { m: await LQ.seal(pw, G.code, reply) });
}
const trCtlPush = () => { trCtlSend().catch(() => {}); };
