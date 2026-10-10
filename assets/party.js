/* Let's Quiz host screen: the party pieces (October 2026).
 *  - Power cards: every player is dealt a hand (Steal 1000, Copycat, 5× points, Slow down, Freeze) to play from their
 *    phone between questions; Bounty: get a question right that the leader gets wrong and take 100 off them.
 *  - Play Your Cards Right: a row of number cards, higher or lower, out on a wrong call.
 *  - Taskmaster: a photo task on the phones; the host picks the best three and the worst.
 *  - Who Said That?: the warm-up's About You answers come back; whose was it?
 * Loaded before host.html's own script. Nothing here runs until a game is under way, by which time host.html's
 * globals (G, stage, the helpers) all exist. Names start pc / task / ws / power / party to stay clear of host.html's. */

// ---------------------------------------------------------------- shared
/** The everyone-answers types: the ones power cards and Bounty act on (not the group games, slides or tasks). */
const PARTY_PLAIN = ['choice', 'tf', 'text', 'order', 'match', 'sort', 'pin', 'smash', 'wheel', 'highlow', 'rhyme', 'club', 'dingbat', 'tune', 'nearest', 'whosaid'];
const partyPlain = (q) => !!q && PARTY_PLAIN.includes(q.type);
const partyPick = (arr) => arr[Math.floor(Math.random() * arr.length)];
const partyNote = (r, line) => { if (r) (r.party = r.party || []).push(line); };

/** The game leaves the lobby: deal the power cards and fetch the warm-up's About You answers. */
function partyGameStart() { powerDealAll(); wsLoad(); }

// ---------------------------------------------------------------- power cards + Bounty
const POWER = {
  steal: { icon: '💰', name: 'Steal 1000', how: 'Take 1,000 points off someone, right now', target: true },
  copy: { icon: '🪞', name: 'Copycat', how: "Your answer on the next question is whatever they answer", target: true },
  x5: { icon: '🔥', name: '5× points', how: 'Your points on the next question count five times. Played blind!', target: false },
  slow: { icon: '🐌', name: 'Slow down', how: 'Cut their time on the next question by 30%', target: true },
  freeze: { icon: '🥶', name: 'Freeze', how: 'They sit out the next question', target: true },
};
function powerOn() { return !!G?.quiz?.settings?.power?.on && !WARMUP && !PREVIEW; }
function powerDeal(pid) {
  if (!powerOn() || !G.players[pid]) return;
  G.hands = G.hands || {}; if (G.hands[pid]) return;
  const n = LQ.clamp(Math.round(+G.quiz.settings.power.hand || 3), 1, 5), kinds = shuffle(Object.keys(POWER));
  G.hands[pid] = Array.from({ length: n }, (_, i) => ({ id: uid('c'), kind: kinds[i % kinds.length] }));
}
function powerDealAll() { if (!powerOn()) return; for (const pid of Object.keys(G.players)) powerDeal(pid); persist(); }
/** Cards are played between questions: never while one is being answered. */
function powerWindow() { return powerOn() && ['round', 'slide', 'typecard', 'countdown', 'reveal', 'scoreboard'].includes(G.phase); }
/** The next everyone-answers question, the one a Copycat, 5×, Slow down or Freeze lands on (-1: none left). */
function powerNextPlain() { const from = ['reveal', 'scoreboard', 'grading'].includes(G.phase) ? G.qIndex + 1 : Math.max(0, G.qIndex); for (let i = from; i < G.quiz.questions.length; i++) if (partyPlain(G.quiz.questions[i])) return i; return -1; }
function onCard({ pid, id, target }) {
  if (!powerWindow() || !G.players[pid]) return;
  const hand = G.hands?.[pid] || [], card = hand.find((c) => c.id === id); if (!card) return;
  const P_ = POWER[card.kind], no = (why) => send('cardno', { pid, why });
  G.fxGap = G.fxGap || {}; G.fxPend = G.fxPend || [];
  if (G.fxGap[pid]) return no('One card per break: play another after the next question.');
  if (P_.target && (!G.players[target] || target === pid)) return no('Pick someone else to play it on.');
  if (card.kind !== 'steal' && powerNextPlain() < 0) return no('No questions left for that card to work on.');
  if (card.kind === 'freeze' && G.fxPend.some((f) => f.kind === 'freeze' && f.target === target)) return no(`${pname(target)} is already frozen for the next question!`);
  hand.splice(hand.indexOf(card), 1); G.fxGap[pid] = true;
  let text;
  if (card.kind === 'steal') {
    const amt = Math.min(1000, Math.max(0, G.players[target].score));
    G.players[target].score -= amt; G.players[pid].score += amt;
    text = amt ? `${pname(pid)} stole ${amt} points from ${pname(target)}!` : `${pname(pid)} tried to rob ${pname(target)}… who had nothing to steal!`;
  } else {
    G.fxPend.push({ kind: card.kind, by: pid, target: P_.target ? target : null });
    text = { copy: `${pname(pid)} is copying ${pname(target)}'s answer on the next question`, x5: `${pname(pid)} plays 5× points on the next question!`, slow: `${pname(pid)} cuts ${pname(target)}'s time on the next question`, freeze: `${pname(pid)} freezes ${pname(target)} out of the next question!` }[card.kind];
  }
  G.cardFlash = { n: (G.cardFlash?.n || 0) + 1, icon: P_.icon, name: P_.name, text, at: Date.now() };
  persist(); powerFlashShow(); partyDecorate(); sound(card.kind === 'steal' ? 'caught' : card.kind === 'freeze' ? 'whoosh' : 'ding');
  if (G.phase === 'scoreboard' && card.kind === 'steal') render();
  broadcastState();
}
/** The card just played, big on the screen for a few seconds. */
function powerFlashShow() {
  const f = G.cardFlash; if (!f) return;
  document.getElementById('cardflash')?.remove();
  const el = document.createElement('div'); el.id = 'cardflash'; el.className = 'cardflash';
  el.innerHTML = `<div class="cf-card"><div class="cf-icon">${f.icon}</div><div class="cf-name">${esc(f.name)}</div></div><div class="cf-text">${esc(f.text)}</div>`;
  document.body.appendChild(el); setTimeout(() => el.classList.add('out'), 4200); setTimeout(() => el.remove(), 5000);
}
/** A question starts: the cards played in the break land on it (if it is an everyone-answers one), and the break's
 *  one-card-each limit resets. */
function partyStartQuestion(q) {
  G.fxGap = {};
  if (partyPlain(q) && G.fxPend?.length) {
    const fx = { frozen: {}, copy: {}, x5: {}, slow: {} };
    for (const f of G.fxPend) { if (f.kind === 'freeze') fx.frozen[f.target] = f.by; if (f.kind === 'copy') fx.copy[f.by] = f.target; if (f.kind === 'x5') fx.x5[f.by] = true; if (f.kind === 'slow') fx.slow[f.target] = f.by; }
    G.q.fx = fx; G.fxPend = [];
  }
  if (q.type === 'whosaid') { G.q.ws = wsNow; G.q.author = wsNow?.author || null; if (wsNow?.i >= 0) (G.aboutUsed = G.aboutUsed || []).push(wsNow.i); if (!wsNow) G.q.deadline = Date.now() + 5000; }
}
/** An answer this player may not give: frozen, copying someone, out of (cut) time, or it's their own Who Said That. */
function partyBlocks(pid) {
  const fx = G.q?.fx;
  if (G.q?.author === pid) return true;
  if (!fx) return false;
  if (fx.frozen[pid] || fx.copy[pid]) return true;
  return !!fx.slow[pid] && Date.now() - G.q.startedAt > question().time * 700;
}
/** Not waited for before the question closes early (everyone else has answered). */
function partyExempt(pid) { return partyBlocks(pid); }
/** Before marking: a Copycat takes on their target's answer (and its speed). */
function partyBeforeGrade() {
  const fx = G.q?.fx; if (!fx) return;
  for (const [pid, t] of Object.entries(fx.copy)) if (!fx.frozen[pid] && G.q.answers[t]) G.q.answers[pid] = { ...G.q.answers[t], copied: t };
}
/** After marking (and double points): the cards' effects, then Bounty on the leader. */
function partyAfterGrade(byPlayer) {
  const q = question(), fx = G.q.fx, blank = () => ({ answered: false, correct: false, partial: 0, points: 0 });
  if (fx) {
    for (const [pid, by] of Object.entries(fx.frozen)) { const r = byPlayer[pid] = byPlayer[pid] || blank(); r.points = 0; r.frozen = true; partyNote(r, `🥶 Frozen out by ${pname(by)}`); }
    for (const [pid, t] of Object.entries(fx.copy)) { const r = byPlayer[pid] = byPlayer[pid] || blank(); partyNote(r, G.q.answers[t] ? `🪞 You copied ${pname(t)}` : `🪞 You copied ${pname(t)}… who didn't answer!`); }
    for (const [pid, by] of Object.entries(fx.slow)) partyNote(byPlayer[pid], `🐌 ${pname(by)} cut your time`);
    for (const pid of Object.keys(fx.x5)) { const r = byPlayer[pid]; if (!r) continue; if (r.points > 0 && !r.practice) { r.points *= 5; partyNote(r, '🔥 5× points!'); } else partyNote(r, '🔥 5× nothing is… nothing'); }
  }
  // Bounty: right when the leader was wrong (or didn't answer) takes 100 off them, the five quickest at most.
  if (G.quiz.settings.bounty && partyPlain(q) && !practiceQ() && !WARMUP) {
    const rk = ranked(), lead = rk[0];
    if (lead && lead.score > 0 && (!rk[1] || rk[1].score < lead.score) && !byPlayer[lead.id]?.correct) {
      const hunters = Object.entries(byPlayer).filter(([pid, r]) => pid !== lead.id && r.correct && G.players[pid]).sort((a, b) => (G.q.answers[a[0]]?.elapsed || 0) - (G.q.answers[b[0]]?.elapsed || 0)).slice(0, 5);
      if (hunters.length) {
        for (const [, r] of hunters) { r.points += 100; r.bounty = 100; partyNote(r, `🎯 Bounty! +100 off ${lead.name}`); }
        const l = byPlayer[lead.id] = byPlayer[lead.id] || blank(); l.points -= 100 * hunters.length; partyNote(l, `🎯 Bounty on your head: −${100 * hunters.length}`);
        G.q.bounty = { lead: lead.id, hunters: hunters.map(([pid]) => pid) };
      }
    }
  }
}
/** The phones' share of all this: hands, what's in play, the last card played; Play Your Cards Right and the task. */
function partyState(s) {
  if (powerOn()) {
    s.power = { window: powerWindow(), hands: G.hands || {}, gap: G.fxGap || {}, flash: G.cardFlash || null, pend: G.fxPend || [], fx: G.phase === 'question' && G.q?.fx ? G.q.fx : null, more: powerNextPlain() >= 0,
      players: Object.values(G.players).map((p) => ({ pid: p.id, name: p.name, emoji: p.emoji || '', score: p.score })) };
  }
  if (G.quiz.settings.bounty && !WARMUP) s.bounty = true;
  const nowT = G.paused ? G.pausedAt : Date.now();
  if (G.phase === 'question' && G.q?.pc?.v) {
    const g = G.q.pc, q = question(), over = g.step === 'over', best = Math.max(0, ...Object.values(g.pos));
    s.pc = { step: g.step, remainingMs: g.until ? Math.max(0, g.until - nowT) : 0, totalMs: g.total, cards: g.cards.map((c, i) => over || i <= best || Object.values(g.out).includes(i) ? c : { label: c.label }),
      pos: g.pos, out: g.out, done: Object.keys(g.done), winners: g.winners || [], perCard: q.perCard ?? 200, prize: q.prize ?? 500, pts: g.pts, banter: g.banter };
  }
  tmState(s); // Taskmaster on camera
  if (G.phase === 'question' && G.q?.task) {
    const g = G.q.task;
    s.task = { step: g.step, remainingMs: g.until ? Math.max(0, g.until - nowT) : 0, totalMs: g.total, code: G.code, key: question().id, got: Object.keys(g.photos), picks: g.step === 'show' ? g.picks : null };
  }
  if (s.pc || s.task) s.names = Object.fromEntries(Object.values(G.players).map((p) => [p.id, { name: p.name, emoji: p.emoji || '' }]));
  if (G.phase === 'question' && G.q?.author !== undefined) s.wsEmpty = !G.q.ws;
}
/** Over the screen: what the cards are doing to this question, and Bounty on the reveal. Test bots play cards too. */
function partyDecorate() {
  document.getElementById('fxstrip')?.remove();
  if (!G) return;
  const chips = [];
  const fx = G.phase === 'question' && G.q?.fx;
  if (fx) {
    for (const [pid, by] of Object.entries(fx.frozen)) chips.push(`🥶 ${esc(pname(pid))} frozen by ${esc(pname(by))}`);
    for (const [pid, t] of Object.entries(fx.copy)) chips.push(`🪞 ${esc(pname(pid))} copies ${esc(pname(t))}`);
    for (const [pid, by] of Object.entries(fx.slow)) chips.push(`🐌 ${esc(pname(pid))} slowed by ${esc(pname(by))}`);
    for (const pid of Object.keys(fx.x5)) chips.push(`🔥 ${esc(pname(pid))} on 5×`);
  }
  if (G.phase === 'reveal' && G.q?.bounty) chips.push(`🎯 Bounty! ${G.q.bounty.hunters.map((p) => esc(pname(p))).join(', ')} took ${100 * G.q.bounty.hunters.length} off ${esc(pname(G.q.bounty.lead))}`);
  if (powerWindow() && (G.fxPend || []).length) chips.push(`🃏 Waiting for the next question: ${(G.fxPend || []).map((f) => `${POWER[f.kind].icon} ${esc(pname(f.by))}${f.target ? ' → ' + esc(pname(f.target)) : ''}`).join(' · ')}`);
  if (chips.length) { const el = document.createElement('div'); el.id = 'fxstrip'; el.className = 'fxstrip'; el.innerHTML = chips.map((c) => `<span>${c}</span>`).join(''); document.body.appendChild(el); }
  if (G.phase === 'scoreboard' && G.test && powerOn() && G.botCardsAt !== G.qIndex) {
    G.botCardsAt = G.qIndex; const qi = G.qIndex;
    for (const b of G.bots || []) if ((G.hands?.[b.pid] || []).length && chance(0.25)) setTimeout(() => {
      if (G.phase !== 'scoreboard' || G.qIndex !== qi) return;
      const c = G.hands[b.pid]?.[0], others = Object.keys(G.players).filter((p) => p !== b.pid); if (!c || !others.length) return;
      onCard({ pid: b.pid, id: c.id, target: partyPick(others) });
    }, rnd(800, 4000));
  }
}

// ---------------------------------------------------------------- Play Your Cards Right
// Every card is on screen from the start. Each player runs the row on their own phone against one 30-second clock:
// call higher or lower and, if it's right, the next card turns over at once (no countdown between turns). One wrong
// call ends your run; get to the end of the row for the bonus. (User, 10 Oct 2026.)
const PC_GAME_MS = 30000;
const PC_BANTER = {
  play: ['Higher or lower?', "Don't be shy, shout it out!", 'Make your mind up!', 'Have a word with yourself…', 'Higher! Lower! Somebody say something!'],
  over: ['What do points make? PRIZES!', 'Good game, good game!', "Didn't they do well?", 'Nice to see you, to see you… nice!'],
};
function pcStart() {
  const pos = {}; for (const pid of livePids()) pos[pid] = 0;
  G.q.pc = { v: 2, cards: LQ.cardsOf(question()), step: 'play', until: 0, total: 0, pos, out: {}, done: {}, pts: {}, winners: [], banter: partyPick(PC_BANTER.play), t0: Date.now() };
  stepTo(G.q.pc, 'play', PC_GAME_MS); sound('go');
  persist(); pcRender(); broadcastState();
  for (const b of G.bots || []) if (b.pid in G.q.pc.pos) pcBotTurn(b);
}
/** Still running the row: not out, not finished. */
const pcPlaying = (g, pid) => pid in g.pos && !(pid in g.out) && !(pid in g.done);
function pcAnswer(pid, a) {
  const g = G.q.pc; if (!g || !g.v || g.step !== 'play' || !a || !['h', 'l'].includes(a.call)) return;
  if (!(pid in g.pos) && G.players[pid]) g.pos[pid] = 0; // joined after the start
  if (!pcPlaying(g, pid)) return;
  const at = g.pos[pid]; if (a.at != null && +a.at !== at) return; // a double tap on a card that has already turned
  const q = question(), cur = g.cards[at], nxt = g.cards[at + 1]; if (!nxt) return;
  const up = nxt.n > cur.n;
  if ((a.call === 'h') === up) {
    g.pos[pid] = at + 1; g.pts[pid] = (g.pts[pid] || 0) + (q.perCard ?? 200);
    if (g.pos[pid] >= g.cards.length - 1) { g.done[pid] = Date.now() - g.t0; g.winners.push(pid); g.pts[pid] += (q.prize ?? 500); sound('fanfare'); }
    else sound('ding');
  } else { g.out[pid] = at + 1; sound('wrong'); }
  if (!Object.keys(g.pos).some((p) => pcPlaying(g, p))) return pcOver();
  persist(); pcRender(); broadcastState();
  const b = (G.bots || []).find((x) => x.pid === pid); if (b && pcPlaying(g, pid)) pcBotTurn(b);
}
function pcOver() {
  const g = G.q.pc; if (g.step === 'over') return;
  g.banter = partyPick(PC_BANTER.over); stepTo(g, 'over', 6000); sound(g.winners.length ? 'fanfare' : 'trombone');
  persist(); pcRender(); broadcastState();
}
function pcStepDone() {
  const g = G.q.pc;
  if (g.step === 'play') return pcOver();
  if (g.step === 'over') return endQuestion();
  return endQuestion(); // a game saved by the old version
}
function pcBotTurn(b) {
  const g = G.q.pc, at = g.pos[b.pid], cur = g.cards[at], nxt = g.cards[at + 1]; if (!nxt) return;
  botLater(() => { if (G.q?.pc === g && g.step === 'play' && g.pos[b.pid] === at) pcAnswer(b.pid, { call: chance(b.skill) === (nxt.n > cur.n) ? 'h' : 'l', at }); }, rnd(900, 2600));
}
const pcCardHtml = (c, up, cls = '') => `<div class="pccard ${up ? 'up' : 'down'} ${cls}"><div class="pcin"><div class="pcface"><div class="pclabel">${esc(c.label)}</div><div class="pcval">${esc(c.show || '')}</div></div><div class="pcbackf"><div class="pclabel">${esc(c.label)}</div><div class="pcq">?</div></div></div></div>`;
/** One player's run as a strip of pips: green for each right call, red where they went out. */
function pcTrack(g, pid) {
  const n = g.cards.length - 1, got = g.pos[pid] || 0;
  const pips = Array.from({ length: n }, (_, i) => `<i class="${i < got ? 'ok' : g.out[pid] === i + 1 ? 'no' : ''}"></i>`).join('');
  const tag = pid in g.done ? `🏆 ${(g.done[pid] / 1000).toFixed(1)}s` : pid in g.out ? '❌ out' : '';
  return `<div class="pctrack ${pid in g.done ? 'won' : pid in g.out ? 'lost' : ''}"><span class="pcwho">${pem(pid)} ${esc(pname(pid))}</span><span class="pcpips">${pips}</span><span class="pctag">${tag}</span></div>`;
}
function pcRender() {
  const q = question(), g = G.q.pc; if (!g) return;
  if (!g.v) { g.v = 2; g.step = 'over'; g.until = 0; g.pos = g.pos || {}; g.out = g.outAt || {}; g.done = {}; g.winners = g.winners || []; g.banter = g.banter || ''; } // saved by the old version: just let it finish
  const over = g.step === 'over', best = Math.max(0, ...Object.values(g.pos));
  const row = g.cards.map((c, i) => pcCardHtml(c, over || i === 0, !over && i === best + 1 ? 'next' : '')).join('');
  const pids = Object.keys(g.pos).filter((p) => G.players[p]).sort((a, b) => (b in g.done) - (a in g.done) || (g.done[a] ?? 0) - (g.done[b] ?? 0) || (g.pos[b] || 0) - (g.pos[a] || 0));
  const still = pids.filter((p) => pcPlaying(g, p)).length;
  const sub = over
    ? (g.winners.length ? `<div class="pcbig up">🏆 ${g.winners.map((p) => esc(pname(p))).join(', ')}</div><div class="pcbanter">“${esc(g.banter)}” · +${q.prize ?? 500} for reaching the end</div>` : `<div class="pcbig down">Nobody made it to the end!</div><div class="pcbanter">“${esc(g.banter)}”</div>`)
    : `<div class="pcask">Higher or lower? Get through every card in ${Math.round(PC_GAME_MS / 1000)} seconds on your phone!</div><div class="pcbanter">“${esc(g.banter)}”</div>`;
  stage.innerHTML = `${topBar(`<div class="pillbox"><span class="hpill">🃏 ${over ? `${g.winners.length} made it` : `${still} still going`}</span><div class="timer ${g.until ? '' : 'hidden'}" id="timer" data-s="${Math.ceil((g.total || 0) / 1000)}" style="--p:100%"></div></div>`)}
    <div class="stage-main pcstage"><h1 class="qtext" style="font-size:clamp(1.3rem,2.6vw,2.2rem)">${esc(q.text)}</h1><div class="pcrow">${row}</div>${sub}<div class="pctracks">${pids.map((p) => pcTrack(g, p)).join('')}</div></div>
    ${hostBar(`<button class="btn btn-ghost" data-act="end">End game</button><button class="btn btn-ghost" data-act="stopgame">Stop the game ■</button><button class="btn btn-primary" id="pcNext">${over ? 'Finish ▶' : 'Stop the clock ■'}</button>`)}`;
  bind(); $('#pcNext').onclick = () => { if (G.q?.pc) { G.q.pc.until = 0; pcStepDone(); } };
}

// ---------------------------------------------------------------- Taskmaster
let taskPollT = null;
function taskStart() {
  if (tmMode(question())) return tmStart(); // on camera: the wheel picks who does it (assets/taskmaster.js)
  G.q.task = { step: 'snap', until: 0, total: 0, photos: {}, picks: {}, sent: {} };
  stepTo(G.q.task, 'snap', LQ.clamp(+question().time || 120, 20, 600) * 1000); sound('go');
  persist(); taskRender(); broadcastState(); taskPoll(); taskBots();
}
/** Fetches the photos sent so far (signed links from the private bucket). */
async function taskPoll(final) {
  clearTimeout(taskPollT);
  const g = G.q?.task, qid = question()?.id; if (!g || G.phase !== 'question') return;
  try { const r = await api('task_photos', { code: G.code, key: qid }); for (const p of r.photos || []) if (G.players[p.pid] && !G.viewers?.[p.pid]) g.photos[p.pid] = { url: p.url, at: p.at }; } catch {}
  if (G.q?.task !== g) return;
  persist(); if (!final) { taskRender(); broadcastState(); }
  const live = livePids();
  if (g.step === 'snap' && live.length && live.every((pid) => g.photos[pid])) return taskJudge();
  if (g.step === 'snap') taskPollT = setTimeout(taskPoll, 4000);
}
function taskAnswer(pid, a) { const g = G.q.task; if (!g || g.step !== 'snap' || !a?.photo) return; g.sent[pid] = Date.now(); taskPoll(); }
async function taskJudge() {
  const g = G.q.task; if (!g || g.step !== 'snap') return;
  g.until = 0; g.step = 'judging'; await taskPoll(true);
  if (G.q?.task !== g) return;
  if (!Object.keys(g.photos).length) { g.step = 'judge'; persist(); return endQuestion(); }
  stepTo(g, 'judge', 0); sound('gong'); persist(); taskRender(); broadcastState();
}
/** Click a photo to move it round the places still free: 1st → 2nd → 3rd → worst → nothing. Each place goes to one
 *  photo, so a place another photo already has is skipped (click that one off first to give it to this one). */
function taskCycle(pid) {
  const g = G.q.task; if (!g || g.step !== 'judge') return;
  const order = ['1', '2', '3', 'w', ''], cur = g.picks[pid] || '';
  const taken = new Set(Object.entries(g.picks).filter(([p]) => p !== pid).map(([, v]) => v));
  let i = order.indexOf(cur), nxt = '';
  for (let n = 0; n < order.length; n++) { i = (i + 1) % order.length; if (!order[i] || !taken.has(order[i])) { nxt = order[i]; break; } }
  if (nxt) g.picks[pid] = nxt; else delete g.picks[pid];
  persist(); taskRender();
}
function taskAward() { const g = G.q.task; if (!g || g.step !== 'judge') return; stepTo(g, 'show', 9000); sound('fanfare'); persist(); taskRender(); broadcastState(); }
function taskStepDone() { const g = G.q.task; if (g.step === 'snap') return taskJudge(); if (g.step === 'show') return endQuestion(); }
function taskBots() {
  const g = G.q.task, cols = ['#e21b3c', '#1368ce', '#26890c', '#d89e00', '#8e44ad', '#ff7ab6'];
  for (const b of G.bots || []) botLater(() => {
    if (G.q?.task !== g || g.step !== 'snap') return;
    const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="400" height="300"><rect width="400" height="300" fill="${partyPick(cols)}"/><text x="200" y="190" font-size="150" text-anchor="middle">${b.emoji}</text></svg>`;
    g.photos[b.pid] = { url: 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svg), at: new Date().toISOString(), bot: true };
    persist(); taskRender(); broadcastState();
  }, rnd(3000, 15000));
}
const TASK_MEDAL = { 1: '🥇', 2: '🥈', 3: '🥉', w: '💩' };
function taskPrize(q, v) { const p = Array.isArray(q.prizes) ? q.prizes : [1000, 600, 300]; return v === 'w' ? -(q.worst ?? 300) : ['1', '2', '3'].includes(v) ? (+p[+v - 1] || 0) : 0; }
function taskRender() {
  const q = question(), g = G.q.task; if (!g || G.phase !== 'question') return;
  const ids = Object.keys(g.photos), live = livePids();
  let main;
  if (g.step === 'snap' || g.step === 'judging') main = `<div class="taskhead"><div class="ri-kicker">📸 Taskmaster</div><h1 class="qtext">${esc(q.text)}</h1><p class="uqrule">${ids.length} of ${live.length} photos in · snap it on your phone and send it!</p></div>
      <div class="taskchips">${live.map((pid) => `<span class="tl ${g.photos[pid] ? 'ok' : ''}">${pem(pid)} ${esc(pname(pid))} ${g.photos[pid] ? '📸' : '…'}</span>`).join('')}</div>`;
  else if (g.step === 'judge') main = `<div class="taskhead"><h1 class="qtext" style="font-size:clamp(1.2rem,2.4vw,2rem)">${esc(q.text)}</h1><p class="uqrule">Click a photo: 🥇 → 🥈 → 🥉 → 💩 worst → none · 🔍 for a closer look</p></div>
      <div class="taskgrid">${ids.map((pid) => { const v = g.picks[pid] || ''; return `<div class="taskph ${v ? 'pick' + v : ''}" data-tp="${pid}"><img src="${esc(g.photos[pid].url)}" alt=""><div class="tpname">${pem(pid)} ${esc(pname(pid))}</div>${v ? `<div class="tpmedal">${TASK_MEDAL[v]}<small>${taskPrize(q, v) > 0 ? '+' : ''}${taskPrize(q, v)}</small></div>` : ''}<button class="tpzoom" data-tz="${pid}" title="Look closer">🔍</button></div>`; }).join('')}</div>`;
  else {
    const at = (v) => Object.keys(g.picks).find((p) => g.picks[p] === v);
    const slot = (v) => { const pid = at(v); return pid ? `<div class="taskpod p${v}"><div class="tpmedal big">${TASK_MEDAL[v]}</div><img src="${esc(g.photos[pid]?.url || '')}" alt=""><div class="tpname">${pem(pid)} ${esc(pname(pid))} · ${taskPrize(q, v) > 0 ? '+' : ''}${taskPrize(q, v)}</div></div>` : ''; };
    main = `<div class="taskhead"><div class="ri-kicker">📸 The Taskmaster has spoken</div></div><div class="taskpodium">${slot('2')}${slot('1')}${slot('3')}${slot('w')}</div>`;
  }
  const btn = g.step === 'snap' ? '<button class="btn btn-primary" id="taskGo">Time\'s up: judge them ▶</button>' : g.step === 'judge' ? '<button class="btn btn-primary" id="taskGo">Award the points ▶</button>' : g.step === 'show' ? '<button class="btn btn-primary" id="taskGo">Finish ▶</button>' : '';
  stage.innerHTML = `${topBar(`<div class="pillbox"><span class="hpill">📸 ${ids.length} photo${ids.length === 1 ? '' : 's'}</span><div class="timer ${g.until ? '' : 'hidden'}" id="timer" data-s="${Math.ceil((g.total || 0) / 1000)}" style="--p:100%"></div></div>`)}
    <div class="stage-main taskstage">${main}</div>${hostBar(`<button class="btn btn-ghost" data-act="end">End game</button>${btn}`)}`;
  bind();
  $$('[data-tp]').forEach((el) => el.onclick = (e) => { if (e.target.closest('[data-tz]')) return; taskCycle(el.dataset.tp); });
  $$('[data-tz]').forEach((b) => b.onclick = (e) => { e.stopPropagation(); const ph = g.photos[b.dataset.tz]; if (!ph) return; const m = document.createElement('div'); m.className = 'modal-bg taskzoom'; m.innerHTML = `<img src="${esc(ph.url)}" alt=""><div class="tpname">${pem(b.dataset.tz)} ${esc(pname(b.dataset.tz))}</div>`; m.onclick = () => m.remove(); document.body.appendChild(m); });
  const go = $('#taskGo'); if (go) go.onclick = () => { const s = G.q?.task?.step; if (s === 'snap') taskJudge(); else if (s === 'judge') taskAward(); else if (s === 'show') endQuestion(); };
}

// ---------------------------------------------------------------- Who Said That? (and the warm-up's About You)
let wsNow = null;
async function wsLoad() {
  if (G.about || WARMUP || PREVIEW || DEMO || !G.quiz.questions.some((q) => q.type === 'whosaid')) return;
  G.about = [];
  try { const r = await api('warmup_about', { quizId: G.quizId }); G.about = r.about || []; } catch { G.about = []; }
  persist();
}
const WS_FAKE = [['Tell us: your worst ever job?', 'Dressing up as a giant sausage outside a butcher\'s'], ['Tell us: your most embarrassing moment?', 'Waved back at someone who was waving at the person behind me'], ['Tell us: a secret talent?', 'I can name every Eurovision winner since 1990'], ['Tell us: your guilty pleasure?', 'Crisp sandwiches. Every day.'], ['Tell us: the worst gift you ever got?', 'A framed photo of the person who gave it to me']];
/** Picks this question's quote: an About You answer from someone in the game (by device, else by name), each answer
 *  used once and everyone's turn coming round before anyone's second. A test game with bots borrows made-up ones. */
function wsPick() {
  const here = livePids(), key = (s) => LQ.normText(String(s || '')), byName = new Map(here.map((pid) => [key(pname(pid)), pid]));
  const used = new Set(G.aboutUsed || []), count = {};
  for (const i of used) { const a = (G.about || [])[i]; if (a) count[a.pid] = (count[a.pid] || 0) + 1; }
  let pool = (G.about || []).map((a, i) => ({ ...a, i, who: G.players[a.pid] ? a.pid : byName.get(key(a.name)) })).filter((a) => a.who && here.includes(a.who) && !used.has(a.i));
  if (pool.length) { const least = Math.min(...pool.map((a) => count[a.pid] || 0)); pool = pool.filter((a) => (count[a.pid] || 0) === least); const a = partyPick(pool); return { author: a.who, prompt: a.prompt, answer: a.answer, i: a.i }; }
  if (G.test && (G.bots || []).length) { const [prompt, answer] = partyPick(WS_FAKE); return { author: partyPick(G.bots).pid, prompt, answer, i: -1 }; }
  return null;
}
/** The question as the phones get it (buildView): the quote and four names, never which is right. */
function partyView(q, v, tok) {
  if (q.type === 'task' && WARMUP && q.mode === 'live') v.live = { by: q.liveBy || 'quiz night' }; // a live task: done before quiz night, shown on camera, scored by the host there
  else if (q.type === 'task' && WARMUP) v.upload = { code: String(WARMUP).toUpperCase(), key: q.id }; // a warm-up has no host to judge live: the photo is kept for later
  if (q.type !== 'whosaid') return;
  wsNow = wsPick();
  if (!wsNow) { v.empty = true; v.options = []; return; }
  const others = shuffle(livePids().filter((p) => p !== wsNow.author && !G.viewers?.[p]));
  const real = others.filter((p) => !p.startsWith('p_bot')), pool = [...real, ...others.filter((p) => p.startsWith('p_bot'))];
  v.quote = wsNow.answer; v.prompt = wsNow.prompt;
  v.options = shuffle([wsNow.author, ...pool.slice(0, 3)]).map((pid, i) => ({ k: tok('A:' + pid), text: pname(pid), emoji: pem(pid), c: i }));
  v.mine = drawSecret(wsNow.author, { mine: 1 });
}
function partyIntroSub(q) {
  if (q.type === 'cards') return `${LQ.cardsOf(q).length} cards · 30 seconds to get through the lot on your phone · ${q.perCard ?? 200} for each right call · one wrong call and you're out · reach the end for ${q.prize ?? 500} more`;
  if (tmMode(q) && q.mode === 'all') { const p = tmPrizes(q); return `Everybody does it, all at once, on camera · ${q.time || 90} seconds · best three win ${p.join(', ')}`; }
  if (tmMode(q)) { const p = tmPrizes(q); return `The wheel picks who does each task · bring it to the camera · ${q.time || 90} seconds · 1st ${p[0]}, 2nd ${p[1]}, 3rd ${p[2]} · don't even try: −${tmFail(q)}`; }
  if (q.type === 'task') { const p = q.prizes || [1000, 600, 300]; return `Take the photo on your phone and send it in · best three win ${p.join(', ')} · the worst loses ${q.worst ?? 300}`; }
  return '';
}

// ---------------------------------------------------------------- the host screen
function partyRenderQuestion() {
  const q = question();
  if (q.type === 'cards') { if (G.q.pc) pcRender(); return true; }
  if (q.type === 'task' && G.q.tm) { tmRender(); return true; }
  if (q.type === 'task' && G.q.task) { taskRender(); return true; }
  if (q.type === 'whosaid') {
    const v = G.q.view;
    const body = v.empty ? `<div class="item" style="justify-content:center">Nobody here answered the warm-up's About You questions, so there's nothing to play. On we go!</div>`
      : `<div class="wsquote">“${esc(v.quote)}”</div><div class="wsprompt">${esc(v.prompt)}</div><div class="answers">${v.options.map((o) => `<div class="ans" style="background:${COLORS[o.c].hex}"><span class="shape">${o.emoji || COLORS[o.c].shape}</span>${esc(o.text)}</div>`).join('')}</div>`;
    stage.innerHTML = `${topBar(`<div class="pillbox"><span class="hpill" id="answered">0 of ${players().length} answered</span><div class="timer" id="timer" data-s="${q.time}" style="--p:100%"></div></div>`)}
      <div class="stage-main"><h1 class="qtext" style="font-size:clamp(1.2rem,2.4vw,2rem)">🗣️ ${esc(q.text)}</h1>${body}</div>
      ${hostBar(`<button class="btn btn-ghost" data-act="end">End game</button><button class="btn btn-primary" data-act="primary">Stop the clock ■</button>`)}`;
    renderAnswered(); bind(); return true;
  }
  if (q.type === 'about' || q.type === 'task') {
    stage.innerHTML = `${topBar(`<div class="pillbox"><span class="hpill" id="answered">0 of ${players().length} answered</span><div class="timer" id="timer" data-s="${q.time}" style="--p:100%"></div></div>`)}
      <div class="stage-main"><h1 class="qtext">${esc(q.text)}</h1><div class="item" style="justify-content:center">${q.type === 'task' ? '📸 Take the photo on your phone and send it in' : '🙋 Answer on your phone'}</div></div>
      ${hostBar(`<button class="btn btn-ghost" data-act="end">End game</button><button class="btn btn-primary" data-act="primary">Stop the clock ■</button>`)}`;
    renderAnswered(); bind(); return true;
  }
  return false;
}
function partyReveal() {
  const q = question(), R = G.q?.results; if (!R) return false;
  if (!['cards', 'task', 'whosaid', 'about'].includes(q.type)) return false;
  let body = '', pill = '';
  if (q.type === 'cards') {
    const g = G.q.pc || { cards: LQ.cardsOf(q), i: 0, winners: [], pts: {} };
    body = `<div class="pcrow">${g.cards.map((c) => pcCardHtml(c, true)).join('')}</div><div class="pcbig ${g.winners.length ? 'up' : 'down'}">${g.winners.length ? '🏆 ' + g.winners.map((p) => esc(pname(p))).join(', ') + ' made it to the end' : 'Nobody made it to the end'}</div>
      <div class="textlist mt">${Object.entries(g.pts).sort((a, b) => b[1] - a[1]).map(([pid, v]) => `<span class="tl ok">${pem(pid)} ${esc(pname(pid))} +${v}</span>`).join('')}</div>`;
    pill = `🃏 ${g.winners.length} made it`;
  }
  if (q.type === 'task' && G.q.tm) { body = tmRevealHtml(q); pill = `📞 ${G.q.tm.done.length} task${G.q.tm.done.length === 1 ? '' : 's'}`; }
  else if (q.type === 'task') {
    const g = G.q.task || { photos: {}, picks: {} }, at = (v) => Object.keys(g.picks).find((p) => g.picks[p] === v);
    const slot = (v) => { const pid = at(v); return pid ? `<div class="taskpod p${v}"><div class="tpmedal big">${TASK_MEDAL[v]}</div><img src="${esc(g.photos[pid]?.url || '')}" alt=""><div class="tpname">${pem(pid)} ${esc(pname(pid))} · ${taskPrize(q, v) > 0 ? '+' : ''}${taskPrize(q, v)}</div></div>` : ''; };
    body = WARMUP && q.mode === 'live' ? `<div class="item" style="justify-content:center">🎬 Challenge accepted! Show it on camera on ${esc(q.liveBy || 'quiz night')}: scored live.</div>` : WARMUP ? '<div class="item" style="justify-content:center">📸 Photos in! The Taskmaster judges them before quiz night.</div>' : `<div class="taskpodium">${slot('2')}${slot('1')}${slot('3')}${slot('w')}</div>`;
    pill = `📸 ${Object.keys(g.photos).length} photos`;
  }
  if (q.type === 'whosaid') {
    const v = G.q.view, ws = G.q.ws;
    if (!ws) body = '<div class="item" style="justify-content:center">Nothing to play this time.</div>';
    else {
      const max = Math.max(1, ...Object.values(R.stats.counts || {}));
      body = `<div class="wsquote">“${esc(ws.answer)}”</div><div class="wsit">It was ${face(ws.author)} <b>${esc(pname(ws.author))}</b>!</div>
        <div class="answers">${v.options.map((o) => { const id = G.q.keys[o.k], c = (R.stats.counts || {})[id] || 0, ok = id === 'A:' + ws.author; return `<div class="ans ${ok ? '' : 'dim'}" style="background:${COLORS[o.c].hex}"><div class="bar" style="width:${(c / max) * 100}%"></div><span class="shape" style="position:relative">${o.emoji}</span><span style="position:relative">${esc(o.text)}</span><span class="count" style="position:relative">${c}</span>${ok ? '<span class="tick" style="position:relative">✔</span>' : ''}</div>`; }).join('')}</div>`;
    }
    pill = `${R.stats.right} guessed right`;
  }
  if (q.type === 'about') { body = `<div class="textlist mt">${(R.stats.texts || []).map((t) => `<span class="tl">${esc(t.text)} <span style="opacity:.7;font-size:.85em">· ${esc(t.name)}</span></span>`).join('')}</div>`; pill = `🙋 ${(R.stats.texts || []).length} answers`; }
  stage.innerHTML = `${topBar(`<span class="hpill">${pill}</span>`)}<div class="stage-main"><h1 class="qtext" style="font-size:clamp(1.3rem,2.6vw,2.2rem)">${esc(q.text)}</h1>${body}</div>
    ${hostBar(`<button class="btn btn-ghost" data-act="end">End game</button><button class="btn btn-primary" data-act="primary">${practiceQ() ? (G.qIndex + 1 < G.quiz.questions.length ? 'Next ▶' : 'Final results 🏆') : 'Scores ▶'}</button>`)}`;
  bind();
  if (q.type === 'whosaid' && G.q.ws && !G.q.wsSound) { G.q.wsSound = true; persist(); sound('ding'); }
  return true;
}
/** Marking (inside grade): the new types. */
function partyGrade(q, byPlayer, PL, stats, entries, res, keys) {
  if (q.type === 'cards') {
    const g = G.q.pc || { pts: {}, out: {}, winners: [], cards: [] };
    for (const pid of new Set([...livePids(), ...Object.keys(g.pts)])) {
      if (!PL[pid]) continue;
      const pts = g.pts[pid] || 0, won = g.winners.includes(pid), out = (g.out || g.outAt || {})[pid];
      byPlayer[pid] = { answered: true, correct: won, partial: won ? 1 : pts > 0 ? 0.5 : 0, points: pts, note: won ? `🃏 You made it to the end of the row${g.done?.[pid] ? ` in ${(g.done[pid] / 1000).toFixed(1)}s` : ''}!` : out ? `🃏 Out on card ${out + 1}${pts ? ` · +${pts}` : ''}` : `🃏 Time ran out${pts ? ` · +${pts}` : ''}` };
      if (won) stats.right++;
    }
    stats.answered = Object.keys(byPlayer).length;
  }
  if (q.type === 'task' && G.q.tm) tmGrade(q, byPlayer, PL, stats);
  else if (q.type === 'task' && !WARMUP) {
    const g = G.q.task || { photos: {}, picks: {} };
    for (const pid of new Set([...livePids(), ...Object.keys(g.photos)])) {
      if (!PL[pid]) continue;
      const v = g.picks[pid] || '', pts = taskPrize(q, v), sent = !!g.photos[pid];
      byPlayer[pid] = { answered: sent, correct: pts > 0, partial: pts > 0 ? 1 : 0, points: pts, note: v ? `${TASK_MEDAL[v]} ${v === 'w' ? 'The Taskmaster picked yours as the worst!' : `The Taskmaster put yours ${v === '1' ? 'FIRST' : v === '2' ? 'second' : 'third'}!`}` : sent ? '📸 Not in the top three this time' : '📸 No photo sent' };
      if (pts > 0) stats.right++;
    }
  }
  if (q.type === 'task' && WARMUP) for (const [pid] of entries) byPlayer[pid] = { answered: true, correct: true, partial: 1, points: 0, note: q.mode === 'live' ? `🎬 You're in! Get it ready and show it on camera on ${q.liveBy || 'quiz night'}: the best ones win points live.` : '📸 Photo in! The Taskmaster judges them before quiz night: the best three win points.' };
  if (q.type === 'about') {
    stats.texts = [];
    for (const [pid, a] of entries) { const t = String(a.answer ?? '').trim().slice(0, 200); if (!t) continue; byPlayer[pid] = { answered: true, correct: true, partial: 1, points: q.points ?? 200, note: '🙋 Thanks! Watch out: it might come up on quiz night…' }; stats.right++; stats.texts.push({ name: PL[pid].name, text: t, ok: true }); }
  }
  if (q.type === 'whosaid') {
    const author = G.q.author;
    for (const [pid, a] of entries) {
      if (pid === author) continue;
      const id = keys[a.answer]; stats.counts[id] = (stats.counts[id] || 0) + 1;
      res(pid, !!author && id === 'A:' + author, 0, a.elapsed, { choice: id });
    }
    if (author && PL[author]) { byPlayer[author] = { answered: true, correct: false, partial: 0, points: 0, note: '🤐 That was yours!' }; partyNote(byPlayer[author], '🤐 That was you! No points, but a well kept straight face'); }
  }
}
function partyAnswerText(q) {
  if (q.type === 'cards') { const w = G.q?.pc?.winners || []; return w.length ? `🏆 ${w.map(pname).join(', ')} made it to the end` : 'Nobody made it to the end'; }
  if (q.type === 'task' && G.q?.tm) { const w = Object.entries(G.q.tm.pts).filter(([, v]) => v > 0).sort((a, b) => b[1] - a[1]).map(([p]) => pname(p)); return w.length ? `📞 Top of the tasks: ${w.slice(0, 3).join(', ')}` : ''; }
  if (q.type === 'task') { const g = G.q?.task, w = g ? Object.keys(g.picks).find((p) => g.picks[p] === '1') : null; return WARMUP ? '' : w ? `🥇 ${pname(w)}'s photo won` : ''; }
  if (q.type === 'whosaid') return G.q?.ws ? `It was ${pname(G.q.ws.author)}` : '';
  if (q.type === 'about') return '';
  return null;
}
function partyAnswerDisplay(q, pid) {
  if (q.type === 'cards') { const g = G.q.pc, out = g && (g.out || g.outAt || {})[pid]; return !g ? '—' : g.winners.includes(pid) ? 'made it to the end 🏆' : out ? `out on card ${out + 1}` : g.pos?.[pid] ? `${g.pos[pid]} right when time ran out` : '—'; }
  if (q.type === 'task' && G.q.tm) { const d = G.q.tm.done.filter((x) => x.picks.includes(pid)); return d.length ? d.map((x) => `${x.places[pid] ? TM_PLACES[x.places[pid]] : '·'} ${x.got[pid] > 0 ? '+' : ''}${x.got[pid]}`).join(', ') : 'not picked'; }
  if (q.type === 'task') { const g = G.q.task; if (WARMUP) return G.q.answers[pid] ? (q.mode === 'live' ? '🎬 in' : '📸 photo sent') : '—'; return !g ? '—' : g.picks[pid] ? `${TASK_MEDAL[g.picks[pid]]} photo` : g.photos[pid] ? '📸 photo sent' : '—'; }
  if (q.type === 'whosaid') { const a = G.q.answers[pid]; if (pid === G.q.author) return 'it was theirs'; if (!a) return '—'; if (a.answer === 'skip') return 'skipped'; const id = G.q.keys[a.answer]; return id ? pname(id.slice(2)) : '—'; }
  return null;
}
function partyBotAnswer(b, q, v) {
  if (q.type === 'about') return partyPick(['Fell asleep at my own birthday party', 'I once met Ant but not Dec', 'Crisp sandwiches', 'I can lick my elbow', 'Got lost in IKEA for three hours', 'Sang Bohemian Rhapsody at a funeral']);
  if (q.type === 'task') return { photo: true };
  if (q.type === 'whosaid') { if (!v.options?.length) return 'skip'; const right = v.options.find((o) => G.q.keys[o.k] === 'A:' + G.q.author); return (chance(b.skill * 0.6) && right ? right : partyPick(v.options)).k; }
  return undefined;
}
