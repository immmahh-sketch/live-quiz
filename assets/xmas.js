/* Let's Quiz host screen: CHRISTMAS DAY (November 2026). The whole night is one Christmas Day, and everyone is building their Christmas dinner.
 *  - The plate: nine dishes, each tied to a question category (a question's `xi` says which), plus the tomato ketchup. Get a question right to collect its
 *    dish; the rarer the dish, the fewer right answers collect it (the quickest only). The ketchup is only for a full plate, and only a 1% question wins it.
 *  - The end: every dish missing costs 2,000; a full plate pays 5,000.
 *  - Stealing: every fourth dish question the quickest right answer gets a PINCH (nick a dish from a plate); the ELF visits now and then, and whoever spots him first
 *    chooses two plates to swap; Uncle Keith helps himself; the Monopoly argument swaps the top two scores; a doorbell doubles a question; the power cut hides one.
 *  - The family: everyone is dealt a character (Nan, the Dog, Mum...) with a quirk that always works and a power to use once.
 * Settings: settings.xmas = { on: true }. A question's dish is `q.xi`. State is G.xm. Loaded after party.js and traitors.js; host.html calls
 * xmGameStart / xmStartQuestion / xmAfterGrade / xmState / xmDecorate / xmInterlude / xmEnd / xmScreenNext / xmRenderScreen / xmFinal, and routes the 'xm' channel to onXm.
 * The phones' half is assets/xmas-phone.js; the data (dishes, family, ketchup puzzles) is assets/xmas-data.js. Names start xm to stay clear of host.html's. */

const XM = LQ.XMAS, XC = XM.CFG;
const xmOn = () => !!(G?.quiz?.settings?.xmas?.on && G.xm && !WARMUP && !PREVIEW);
const xmDish = (q) => (q?.xi && XM.item(q.xi) ? q.xi : null);
const xmPlate = (pid) => (G.xm.plates[pid] = G.xm.plates[pid] || {});
const xmHas = (pid, k) => !!G.xm.plates[pid]?.[k];
const xmCountAll = (pid) => XM.ITEMS.filter((i) => xmHas(pid, i.k)).length;
const xmFull9 = (pid) => XM.dishes().every((i) => xmHas(pid, i.k));
const xmName = (k) => { const i = XM.item(k); return i ? `${i.icon} ${i.name}` : k; };
let xmTimer = null;
const xmArm = (fn, ms) => { clearTimeout(xmTimer); xmTimer = setTimeout(fn, ms); };

// ---------------------------------------------------------------- setting up
function xmDishTotal() { return G.quiz.questions.filter((q) => xmDish(q) && xmDish(q) !== 'ketchup' && !LQ.isPractice(G.quiz, q)).length; }
/** The night's surprises, each at a share of the dish questions done (so they spread out however long the quiz is). */
function xmPlan() {
  const n = Math.max(4, xmDishTotal()), at = (f) => Math.max(1, Math.round(n * f));
  return [...[0.15, 0.3, 0.45, 0.6, 0.75, 0.88].map((f) => ({ kind: 'elf', at: at(f) })), { kind: 'uncle', at: at(0.25) }, { kind: 'uncle', at: at(0.68) }, { kind: 'monopoly', at: at(0.8) },
    { kind: 'bell', at: at(0.2) }, { kind: 'bell', at: at(0.55) }, { kind: 'dark', at: at(0.4) }, { kind: 'table', at: at(0.33) }, { kind: 'table', at: at(0.66) }].map((e, i) => ({ ...e, id: i, done: false }));
}
function xmEnsure() {
  if (!G?.quiz?.settings?.xmas?.on || WARMUP || PREVIEW) return;
  if (!G.xm) G.xm = { plates: {}, chars: {}, used: {}, shield: {}, armed: {}, spilled: {}, nanUsed: {}, done: 0, queue: [], screen: null, seq: 0, flash: null, waveN: 0, bellNext: false, darkNext: false, final: null, finalDone: false, plan: xmPlan(), log: [] };
  xmDealAll();
}
function xmDeal(pid) {
  if (G.xm.chars[pid]) return;
  // the least-used family member first, so nobody is Nan twice until everyone has been somebody
  const used = Object.values(G.xm.chars), n = (k) => used.filter((u) => u === k).length, low = Math.min(...XM.CHARS.map((c) => n(c.k)));
  G.xm.chars[pid] = partyPick(XM.CHARS.filter((c) => n(c.k) === low).map((c) => c.k));
}
function xmDealAll() { for (const pid of Object.keys(G.players)) { xmDeal(pid); xmPlate(pid); } }
function xmGameStart() { xmEnsure(); if (xmOn()) { persist(); } }

// ---------------------------------------------------------------- plates
function xmGive(pid, k, from) { xmPlate(pid)[k] = { q: G.qIndex, from: from || null }; G.xm.seq++; }
function xmTakeAway(pid, k) { delete xmPlate(pid)[k]; G.xm.seq++; }
const xmLog = (text) => { G.xm.log.push({ t: Date.now(), text }); G.xm.log = G.xm.log.slice(-60); };
/** Nobody can be robbed twice by the same trick: a shield, or Nan's first save. '' means the plate is open. */
function xmProtected(pid, by) {
  if (by && G.xm.chars[by] === 'keith') return '';
  if (G.xm.shield[pid] > 0) return `${pname(pid)} is hiding in their room`;
  if (G.xm.chars[pid] === 'nan' && !G.xm.nanUsed[pid]) { G.xm.nanUsed[pid] = true; return `${pname(pid)} swatted them away: "Not on my watch!"`; }
  return '';
}
/** One dish moves from a plate to another. */
function xmSteal(thief, victim, k, o = {}) {
  if (!G.players[thief] || !G.players[victim] || thief === victim || !xmHas(victim, k) || xmHas(thief, k)) return { ok: false, line: `${pname(thief)} found nothing to take` };
  const who = G.xm.chars[thief] === 'dog' && !o.open ? 'Somebody' : pname(thief);
  const why = xmProtected(victim, thief);
  if (why) return { ok: false, line: `${who} went for ${pname(victim)}'s ${xmName(k)}… but ${why}` };
  xmTakeAway(victim, k); xmGive(thief, k, victim);
  xmLog(`${pname(thief)} stole ${XM.item(k).name} from ${pname(victim)}`);
  return { ok: true, line: `${who} nicked ${pname(victim)}'s ${xmName(k)}!`, thief, victim, k };
}
/** Two plates swap one dish each (the elf, or Mum). A side with nothing the other lacks just gives. */
function xmSwap(a, b, o = {}) {
  if (!G.players[a] || !G.players[b] || a === b) return { ok: false, line: 'Nobody to swap with' };
  if (o.elf && (G.xm.chars[a] === 'teen' || G.xm.chars[b] === 'teen')) { const t = G.xm.chars[a] === 'teen' ? a : b; return { ok: false, line: `🧒 ${pname(t)} has headphones in: the elf couldn't get near their plate` }; }
  const give = (x, y) => Object.keys(xmPlate(x)).filter((k) => !xmHas(y, k)), pa = give(a, b), pb = give(b, a);
  if (!pa.length && !pb.length) return { ok: false, line: `${pname(a)} and ${pname(b)} have nothing the other one is missing` };
  for (const [x, list] of [[a, pa], [b, pb]]) if (list.length) { const why = xmProtected(x, o.by); if (why) return { ok: false, line: `The swap failed: ${why}` }; }
  const ka = pa.length ? partyPick(pa) : null, kb = pb.length ? partyPick(pb) : null;
  if (ka) { xmTakeAway(a, ka); xmGive(b, ka, a); }
  if (kb) { xmTakeAway(b, kb); xmGive(a, kb, b); }
  xmLog(`${o.elf ? 'The elf' : pname(o.by)} swapped ${pname(a)} and ${pname(b)}`);
  return { ok: true, line: ka && kb ? `${pname(a)} gave up ${xmName(ka)} and got ${pname(b)}'s ${xmName(kb)}` : ka ? `${pname(a)}'s ${xmName(ka)} went to ${pname(b)}` : `${pname(b)}'s ${xmName(kb)} went to ${pname(a)}`, a, b, ka, kb };
}

// ---------------------------------------------------------------- the questions
function xmLeft(k) {
  const qs = G.quiz.questions, from = G.phase === 'lobby' ? 0 : ['reveal', 'scoreboard'].includes(G.phase) ? G.qIndex + 1 : G.qIndex;
  let n = 0; for (let i = from; i < qs.length; i++) if (xmDish(qs[i]) === k && !LQ.isPractice(G.quiz, qs[i])) n++; return n;
}
function xmStartQuestion(q) {
  if (!xmOn()) return;
  xmDealAll();
  const k = xmDish(q); G.q.xk = k || null;
  if (k && partyPlain(q)) { G.q.xarm = G.xm.armed; G.xm.armed = {}; }
  if (partyPlain(q) && G.xm.bellNext) { G.q.xbell = true; G.xm.bellNext = false; xmBellShow(); }
  if (partyPlain(q) && G.xm.darkNext) { G.q.xdark = true; G.xm.darkNext = false; }
  if (k === 'ketchup') G.q.xelig = Object.keys(G.players).filter((p) => xmFull9(p) && !xmHas(p, 'ketchup'));
  xmArmAuto();
}
/** After marking (before the points are added): who collects the dish, the family's quirks, and what the night does next. */
function xmAfterGrade(byPlayer) {
  if (!xmOn() || practiceQ()) return;
  const q = question(), k = xmDish(q), x = G.xm;
  if (G.q.xbell) for (const r of Object.values(byPlayer)) if (r.points > 0) { r.points *= 2; partyNote(r, "🔔 Auntie Maureen's bonus: double points!"); }
  if (!k || !partyPlain(q)) return;
  const item = XM.item(k), arm = G.q.xarm || {}, got = [], slow = [];
  const rights = Object.entries(byPlayer).filter(([pid, r]) => G.players[pid] && r.correct && !r.frozen && !r.blocked).sort((a, b) => (G.q.answers[a[0]]?.elapsed ?? 1e9) - (G.q.answers[b[0]]?.elapsed ?? 1e9)).map(([pid]) => pid);
  const take = (pid, how) => { xmGive(pid, k, null); got.push({ pid, k }); const r = byPlayer[pid] = byPlayer[pid] || { answered: false, correct: false, partial: 0, points: 0 }; partyNote(r, `${item.icon} ${how || `You collected the ${item.name}!`}`); if (G.xm.chars[pid] === 'grandad' && item.rar >= 3) { r.points += XC.WAKE_RARE; partyNote(r, `👴 Grandad wakes up for the good stuff: +${XC.WAKE_RARE}`); } };
  if (item.ketchup) {
    for (const pid of rights) {
      if (xmHas(pid, 'ketchup')) continue;
      if (xmFull9(pid)) take(pid, 'THE KETCHUP IS YOURS! Your plate is complete!'); else partyNote(byPlayer[pid], `🍅 Right, but you need all nine dishes before the ketchup can be yours (you have ${XM.dishes().filter((i) => xmHas(pid, i.k)).length})`);
    }
    for (const pid of G.q.xelig || []) if (!xmHas(pid, 'ketchup') && !rights.includes(pid)) partyNote(byPlayer[pid] = byPlayer[pid] || { answered: false, correct: false, partial: 0, points: 0 }, '🍅 So close: the ketchup stays out of reach' + (xmLeft('ketchup') > 0 ? ' until the next ketchup question' : ''));
  } else {
    const cand = rights.filter((pid) => !xmHas(pid, k) && !x.spilled[pid]);
    const quota = Math.max(1, Math.round(cand.length * XM.share(item.rar)));
    cand.forEach((pid, i) => { if (i < quota || arm[pid] === 'wake') take(pid); else { slow.push(pid); partyNote(byPlayer[pid], `${item.icon} Right, but not quick enough: the ${item.name} went to quicker fingers`); } });
    for (const pid of rights) if (xmHas(pid, k) && !got.some((g) => g.pid === pid) && !cand.includes(pid)) partyNote(byPlayer[pid], `${item.icon} You already have the ${item.name}`);
    for (const pid of rights) if (x.spilled[pid] && !xmHas(pid, k)) partyNote(byPlayer[pid], `🥣 The gravy was spilled on your plate: no ${item.name} this time`);
    for (const pid of Object.keys(arm)) {
      if (arm[pid] === 'insure' && !rights.includes(pid) && G.players[pid] && !xmHas(pid, k) && !x.spilled[pid]) take(pid, `Insurance paid out: the ${item.name} is yours even though you missed it!`);
      if (arm[pid] === 'wake' && byPlayer[pid]?.points > 0) { byPlayer[pid].points *= 2; partyNote(byPlayer[pid], '👴 Wake Up! Double points'); }
    }
    for (const [pid, r] of Object.entries(byPlayer)) if (G.players[pid] && r.answered && !r.correct && x.chars[pid] === 'cousin') { r.points += XC.COUSIN_WRONG; partyNote(r, `🧠 Well, actually… +${XC.COUSIN_WRONG}`); }
    x.spilled = {};
    for (const pid of Object.keys(x.shield)) { x.shield[pid]--; if (x.shield[pid] <= 0) delete x.shield[pid]; }
    x.done++;
    if (x.done % XC.PINCH_EVERY === 0 && rights.length) { // the quickest right answer who has not had a pinch lately, so one fast player does not get them all
      const recent = (x.pinchBy = x.pinchBy || []).slice(-Math.max(1, Math.floor(xmPlayers().length / 3))), by = rights.find((pid) => !recent.includes(pid)) || rights[0];
      x.pinchBy.push(by); x.queue.push({ kind: 'pinch', by });
    }
    for (const e of x.plan) if (!e.done && e.at <= x.done) { e.done = true; if (e.kind === 'bell') x.bellNext = true; else if (e.kind === 'dark') x.darkNext = true; else x.queue.push({ kind: e.kind }); }
  }
  G.q.xgot = got; G.q.xslow = slow;
  persist();
}

// ---------------------------------------------------------------- interludes: pinch, the elf, Uncle Keith, the argument, the table, the end
const xmPlayers = () => Object.keys(G.players);
const xmRealBots = () => (G.bots || []).map((b) => b.pid);
/** After a question (host presses Next): the next surprise in the queue, if there is one. */
function xmInterlude() {
  if (!xmOn() || G.xm.screen || !G.xm.queue.length || G.phase === 'lobby') return false;
  return xmOpen(G.xm.queue.shift());
}
function xmOpen(e) {
  const x = G.xm, now = Date.now(), id = uid('s');
  if (e.kind === 'pinch') {
    const opts = xmPinchOptions(e.by);
    x.screen = { id, kind: 'pinch', step: opts.length ? 'pick' : 'done', by: e.by, t0: now, until: now + XC.PINCH_MS, res: opts.length ? null : { ok: false, line: `${pname(e.by)} was quickest, but there is nothing on any plate they don't already have!` } };
    if (opts.length) { xmArm(() => { if (x.screen?.id === id && x.screen.step === 'pick') xmPinchAuto(); }, XC.PINCH_MS); if (xmRealBots().includes(e.by)) setTimeout(() => { if (x.screen?.id === id && x.screen.step === 'pick') xmPinchAuto(); }, rnd(2500, 6000)); }
    sound('whoosh');
  } else if (e.kind === 'elf') {
    x.screen = { id, kind: 'elf', step: 'spot', t0: now, until: now + XC.ELF_SPOT_MS, spotter: null, res: null };
    xmArm(() => { if (x.screen?.id === id && x.screen.step === 'spot') xmElfSpotEnd(); }, XC.ELF_SPOT_MS);
    for (const pid of xmRealBots()) if (chance(0.3)) setTimeout(() => { if (x.screen?.id === id && x.screen.step === 'spot') xmElfTap(pid); }, rnd(2500, XC.ELF_SPOT_MS - 1500));
    sound('whoosh');
  } else if (e.kind === 'uncle') { x.screen = { id, kind: 'uncle', step: 'done', t0: now, res: xmUncle() }; sound('caught'); }
  else if (e.kind === 'monopoly') { x.screen = { id, kind: 'monopoly', step: 'done', t0: now, res: xmMonopoly() }; sound('gong'); }
  else if (e.kind === 'table') { x.screen = { id, kind: 'table', step: 'done', t0: now }; sound('ding'); }
  else return false;
  persist(); render(); broadcastState();
  return true;
}
function xmPinchOptions(by) {
  const out = [];
  for (const v of xmPlayers()) if (v !== by) for (const k of Object.keys(xmPlate(v))) if (!xmHas(by, k)) out.push({ pid: v, k });
  return out;
}
function xmPinchDo(by, victim, k) {
  const sc = G.xm.screen; if (!sc || sc.kind !== 'pinch' || sc.step !== 'pick') return;
  clearTimeout(xmTimer);
  sc.res = xmSteal(by, victim, k); sc.step = 'done';
  if (sc.res.ok) { sc.hit = { victim, k, by: G.xm.chars[by] === 'dog' ? null : by }; }
  sound(sc.res.ok ? 'caught' : 'whoosh'); persist(); render(); broadcastState();
}
function xmPinchAuto() {
  const sc = G.xm.screen; if (!sc || sc.kind !== 'pinch' || sc.step !== 'pick') return;
  const o = xmPinchOptions(sc.by);
  if (!o.length) { clearTimeout(xmTimer); sc.res = { ok: false, line: 'There was nothing left worth taking.' }; sc.step = 'done'; persist(); render(); broadcastState(); return; }
  const p = partyPick(o); xmPinchDo(sc.by, p.pid, p.k);
}
/** Uncle Keith takes a dish from the fullest plate that is not shielded and slips it to someone with an emptier one. */
function xmUncle() {
  const x = G.xm, cands = xmPlayers().filter((p) => Object.keys(xmPlate(p)).length && !(x.shield[p] > 0)).sort((a, b) => Object.keys(xmPlate(b)).length - Object.keys(xmPlate(a)).length);
  if (!cands.length) return { ok: false, line: 'He looked at every plate… and found nothing worth pinching.' };
  const top = Object.keys(xmPlate(cands[0])).length, victim = partyPick(cands.filter((p) => Object.keys(xmPlate(p)).length === top)), ks = Object.keys(xmPlate(victim));
  const k = partyPick(ks), rcv = xmPlayers().filter((p) => p !== victim && !xmHas(p, k)).sort((a, b) => Object.keys(xmPlate(a)).length - Object.keys(xmPlate(b)).length);
  if (!rcv.length) return { ok: false, line: `He eyed ${pname(victim)}'s ${xmName(k)}, but everybody already had one.` };
  const low = Object.keys(xmPlate(rcv[0])).length, to = partyPick(rcv.filter((p) => Object.keys(xmPlate(p)).length === low));
  xmTakeAway(victim, k); xmGive(to, k, victim); xmLog(`Uncle Keith moved ${XM.item(k).name} from ${pname(victim)} to ${pname(to)}`);
  return { ok: true, line: `He pinched ${pname(victim)}'s ${xmName(k)} and slipped it to ${pname(to)}!`, victim, to, k };
}
/** The Monopoly argument: the top two swap places on the scoreboard (their scores swap). */
function xmMonopoly() {
  const rk = ranked(); if (rk.length < 2) return { ok: false, line: 'Nobody to argue with.' };
  const a = rk[0], b = rk[1];
  if (a.score === b.score) return { ok: false, line: `${a.name} and ${b.name} argued for ages… and ended up exactly level.` };
  const t = a.score; a.score = b.score; b.score = t;
  xmLog(`Monopoly argument: ${a.name} and ${b.name} swapped scores`);
  return { ok: true, line: `${a.name} ends up on ${a.score.toLocaleString('en-GB')} and ${b.name} takes top spot on ${b.score.toLocaleString('en-GB')}!`, a: a.id, b: b.id };
}
function xmElfTap(pid) {
  const sc = G.xm.screen; if (!sc || sc.kind !== 'elf' || sc.step !== 'spot' || sc.spotter || !G.players[pid]) return;
  clearTimeout(xmTimer);
  sc.spotter = pid; sc.step = 'choose'; sc.until = Date.now() + XC.ELF_CHOOSE_MS; sound('ding');
  const id = sc.id; xmArm(() => { if (G.xm.screen?.id === id && G.xm.screen.step === 'choose') xmElfRandom(); }, XC.ELF_CHOOSE_MS);
  if (xmRealBots().includes(pid)) setTimeout(() => { if (G.xm.screen?.id === id && G.xm.screen.step === 'choose') xmElfRandom(); }, rnd(2000, 5000));
  persist(); render(); broadcastState();
}
function xmElfSpotEnd() { const sc = G.xm.screen; if (!sc || sc.kind !== 'elf' || sc.step !== 'spot') return; if (sc.spotter) return; xmElfRandom(true); }
function xmElfSwap(a, b, how) {
  const sc = G.xm.screen; if (!sc || sc.kind !== 'elf') return;
  clearTimeout(xmTimer);
  sc.res = xmSwap(a, b, { elf: true, by: sc.spotter || null }); sc.a = a; sc.b = b; sc.step = 'done'; sc.how = how || 'chosen';
  sound(sc.res.ok ? 'caught' : 'whoosh'); persist(); render(); broadcastState();
}
/** Nobody spotted him, or the spotter dithered: the elf picks two plates himself. */
function xmElfRandom(unspotted) {
  const ids = shuffle(xmPlayers());
  for (let i = 0; i < ids.length; i++) for (let j = i + 1; j < ids.length; j++) {
    const a = ids[i], b = ids[j]; if (G.xm.chars[a] === 'teen' || G.xm.chars[b] === 'teen') continue;
    if (Object.keys(xmPlate(a)).some((k) => !xmHas(b, k)) || Object.keys(xmPlate(b)).some((k) => !xmHas(a, k))) return xmElfSwap(a, b, unspotted ? 'nobody' : 'dithered');
  }
  const sc = G.xm.screen; if (!sc) return; clearTimeout(xmTimer); sc.res = { ok: false, line: 'The elf looked at every plate and found nothing to swap.' }; sc.step = 'done'; persist(); render(); broadcastState();
}
/** The host presses Next on one of these screens. */
function xmScreenNext() {
  const sc = G.xm?.screen; if (!sc) return false;
  if (sc.kind === 'pinch' && sc.step === 'pick') { xmPinchAuto(); return true; }
  if (sc.kind === 'elf' && sc.step === 'spot') { xmElfSpotEnd(); return true; }
  if (sc.kind === 'elf' && sc.step === 'choose') { xmElfRandom(); return true; }
  clearTimeout(xmTimer); G.xm.screen = null; persist(); broadcastState();
  if (sc.kind === 'final') { G.xm.finalDone = true; finish(); return true; }
  nextFrom(G.qIndex); return true;
}

// ---------------------------------------------------------------- the end of the night
/** Every dish missing costs 2,000 (1,500 for Mum); a full plate pays 5,000. Done once. */
function xmApplyFinal() {
  if (!G.xm || G.xm.final) return;
  const out = {};
  for (const pid of xmPlayers()) {
    const have = xmCountAll(pid), missing = XM.ITEMS.length - have, per = G.xm.chars[pid] === 'mum' ? 1500 : Math.abs(XC.MISSING), full = missing === 0, delta = full ? XC.FULL : -missing * per;
    G.players[pid].score += delta; out[pid] = { have, missing, delta, full, per };
  }
  G.xm.final = out; persist();
}
function xmFinal() { if (xmOn()) xmApplyFinal(); }
function xmEnd() {
  if (!xmOn() || G.xm.finalDone) return false;
  xmApplyFinal();
  G.xm.screen = { id: uid('s'), kind: 'final', step: 'done', t0: Date.now() };
  sound('fanfare'); persist(); render(); broadcastState(); confetti();
  return true;
}

// ---------------------------------------------------------------- the family's powers (phones: 'xm' on the channel)
const xmNo = (pid, why) => send('xmno', { pid, why });
const xmWindow = () => xmOn() && !G.xm.screen && ['round', 'slide', 'typecard', 'countdown', 'reveal', 'scoreboard'].includes(G.phase);
function xmFlash(icon, name, text) { G.xm.flash = { n: (G.xm.flash?.n || 0) + 1, icon, name, text, at: Date.now() }; xmFlashShow(); }
function xmFlashShow() {
  const f = G.xm?.flash; if (!f) return;
  document.getElementById('xmflash')?.remove();
  const el = document.createElement('div'); el.id = 'xmflash'; el.className = 'xmflash';
  el.innerHTML = `<div class="xmf-icon">${f.icon}</div><div class="xmf-name">${esc(f.name)}</div><div class="xmf-text">${esc(f.text)}</div>`;
  document.body.appendChild(el); setTimeout(() => el.classList.add('out'), 4200); setTimeout(() => el.remove(), 5000);
}
function onXm(m) {
  if (!xmOn() || !G.players[m.pid]) return;
  const pid = m.pid, x = G.xm;
  if (m.op === 'pinch') { const sc = x.screen; if (sc?.kind === 'pinch' && sc.step === 'pick' && sc.by === pid && xmPinchOptions(pid).some((o) => o.pid === m.target && o.k === m.k)) xmPinchDo(pid, m.target, m.k); return; }
  if (m.op === 'elf') return xmElfTap(pid);
  if (m.op === 'swap') { const sc = x.screen; if (sc?.kind === 'elf' && sc.step === 'choose' && sc.spotter === pid && G.players[m.a] && G.players[m.b] && m.a !== m.b) xmElfSwap(m.a, m.b, 'chosen'); return; }
  if (m.op === 'power') return xmPower(pid, m);
}
function xmPower(pid, m) {
  const x = G.xm, ch = x.chars[pid], C = XM.char(ch);
  if (!C) return;
  if (!xmWindow()) return xmNo(pid, 'Powers are used between questions: wait for the answer or the scores.');
  if (x.used[pid]) return xmNo(pid, 'You have already used your power tonight.');
  const done = (text) => { x.used[pid] = true; xmFlash(C.icon, `${pname(pid)}: ${C.power}`, text); persist(); sound('ding'); render(); broadcastState(); };
  const tgt = G.players[m.target] && m.target !== pid ? m.target : null;
  if (ch === 'nan') {
    const it = XM.item(m.k); if (!it || it.rar !== 1 || it.ketchup) return xmNo(pid, 'Pick a missing common dish.');
    if (xmHas(pid, it.k)) return xmNo(pid, `You already have the ${it.name}.`);
    xmGive(pid, it.k, null); return done(`${pname(pid)} pulled the ${it.icon} ${it.name} out of their handbag!`);
  }
  if (ch === 'grandad') { x.armed[pid] = 'wake'; return done(`${pname(pid)} woke up: double points on the next dish question!`); }
  if (ch === 'cousin') { x.armed[pid] = 'insure'; return done(`${pname(pid)} took out insurance on the next dish question.`); }
  if (ch === 'teen') { x.shield[pid] = XC.HIDE_Q; return done(`${pname(pid)} has gone to their room. Nobody can touch their plate for a while.`); }
  if (ch === 'maureen') { if (!tgt) return xmNo(pid, 'Pick someone else.'); x.spilled[tgt] = true; return done(`${pname(pid)} spilled the gravy on ${pname(tgt)}'s plate!`); }
  if (ch === 'mum') {
    if (!tgt) return xmNo(pid, 'Pick someone to swap with.');
    const r = xmSwap(pid, tgt, { by: pid }); if (!r.ok) return xmNo(pid, r.line);
    return done(`${pname(pid)} swapped seats with ${pname(tgt)}: ${r.line}`);
  }
  if (ch === 'dog') {
    if (!tgt || !xmHas(tgt, m.k)) return xmNo(pid, 'Pick someone and a dish from their plate.');
    const r = xmSteal(pid, tgt, m.k, { open: true }); if (!r.ok && !/swatted|hiding/.test(r.line)) return xmNo(pid, r.line);
    return done(r.ok ? `Something went missing from ${pname(tgt)}'s plate… and the dog looks very pleased with itself.` : r.line.replace(pname(pid), 'The dog'));
  }
  if (ch === 'keith') {
    const cands = xmPlayers().filter((p) => p !== pid && Object.keys(xmPlate(p)).some((k) => !xmHas(pid, k))).sort((a, b) => Object.keys(xmPlate(b)).length - Object.keys(xmPlate(a)).length);
    if (!cands.length) return xmNo(pid, "There is nothing on any plate you don't already have.");
    const top = Object.keys(xmPlate(cands[0])).length, v = partyPick(cands.filter((p) => Object.keys(xmPlate(p)).length === top)), k = partyPick(Object.keys(xmPlate(v)).filter((k) => !xmHas(pid, k)));
    const r = xmSteal(pid, v, k, { open: true }); return done(`${pname(pid)} did a dodgy deal: ${r.line}`);
  }
}
/** Test bots play their power now and then, between questions. */
function xmBotPlay() {
  if (!G.test || G.xm.botAt === G.qIndex || !xmWindow()) return;
  G.xm.botAt = G.qIndex; const qi = G.qIndex;
  for (const pid of xmRealBots()) if (!G.xm.used[pid] && chance(0.2)) setTimeout(() => {
    if (!xmWindow() || G.qIndex !== qi || G.xm.used[pid]) return;
    const others = xmPlayers().filter((p) => p !== pid), ch = G.xm.chars[pid];
    const t = others.length ? partyPick(others) : null, keys = t ? Object.keys(xmPlate(t)).filter((k) => !xmHas(pid, k)) : [];
    const common = XM.ITEMS.filter((i) => i.rar === 1 && !xmHas(pid, i.k));
    onXm({ pid, op: 'power', target: t, k: ch === 'dog' ? partyPick(keys.length ? keys : ['x']) : common[0]?.k });
  }, rnd(1000, 5000));
}

// ---------------------------------------------------------------- the phones' share of all this
function xmPublicScreen() {
  const sc = G.xm.screen; if (!sc) return null;
  const now = Date.now(), out = { id: sc.id, kind: sc.kind, step: sc.step, by: sc.by || null, spotter: sc.spotter || null, ms: sc.until ? Math.max(0, sc.until - now) : 0, age: sc.t0 ? now - sc.t0 : 0, line: sc.res?.line || '', ok: sc.res?.ok ?? null, a: sc.a || null, b: sc.b || null };
  if (sc.kind === 'pinch' && sc.step === 'pick') out.opts = xmPinchOptions(sc.by);
  return out;
}
function xmClock() { const t = G.quiz.questions.length, i = G.phase === 'lobby' ? 0 : Math.min(G.qIndex + (['reveal', 'scoreboard'].includes(G.phase) ? 1 : 0), t); return LQ.XMAS.clock(t ? i / t : 0); }
function xmState(s) {
  if (!xmOn()) return;
  const x = G.xm, q = question(), cur = ['typecard', 'countdown', 'question', 'grading', 'reveal'].includes(G.phase) ? xmDish(q) : null;
  const left = {}; for (const i of XM.ITEMS) left[i.k] = xmLeft(i.k);
  s.xm = { plates: Object.fromEntries(xmPlayers().map((p) => [p, Object.keys(xmPlate(p))])), chars: x.chars, used: x.used, shield: x.shield, armed: x.armed, spilled: x.spilled, left, cur, win: xmWindow(), flash: x.flash, wave: x.waveN, seq: x.seq,
    screen: xmPublicScreen(), clock: xmClock(), dark: !!(G.phase === 'question' && G.q?.xdark), bell: !!(G.phase === 'question' && G.q?.xbell), elig: cur === 'ketchup' ? (G.q?.xelig || xmPlayers().filter((p) => xmFull9(p))) : null,
    players: Object.values(G.players).map((p) => ({ pid: p.id, name: p.name, emoji: p.emoji || '', score: p.score })), final: x.final || null, qty: xmPlayers().length };
}

// ---------------------------------------------------------------- the host screen
const xmRowHtml = (pid, fin) => {
  const n = xmCountAll(pid), f = fin?.[pid];
  return `<div class="xmrow ${f?.full ? 'full' : ''}"><span class="xmrn">${esc(pem(pid))} ${esc(pname(pid))}</span><span class="xmris">${XM.ITEMS.map((i) => `<i class="xmi ${xmHas(pid, i.k) ? 'on' : ''}" title="${esc(i.name)}">${i.icon}</i>`).join('')}</span><b class="xmrc">${n}/${XM.ITEMS.length}</b>${f ? `<b class="xmrd ${f.delta < 0 ? 'neg' : 'pos'}">${f.delta > 0 ? '+' : ''}${f.delta.toLocaleString('en-GB')}</b>` : ''}</div>`;
};
const xmTableHtml = (fin) => `<div class="xmtable ${xmPlayers().length > 10 ? 'two' : ''}">${xmPlayers().sort((a, b) => xmCountAll(b) - xmCountAll(a) || G.players[b].score - G.players[a].score).map((p) => xmRowHtml(p, fin)).join('')}</div>`;
let xmCountT = null;
function xmRenderScreen() {
  const sc = G.xm.screen, cl = xmClock();
  clearInterval(xmCountT); xmCountT = setInterval(() => { const c = document.getElementById('xmCount'); if (!c) return clearInterval(xmCountT); c.textContent = Math.max(0, Math.ceil((+c.dataset.end - Date.now()) / 1000)); }, 500);
  const wrap = (inner, btn) => { stage.innerHTML = `<div class="stage-top"><div class="pillbox"><span class="hpill">🎄 Christmas Day</span><span class="hpill">${cl.icon} ${cl.time} · ${esc(cl.scene)}</span></div></div><div class="stage-main xmstage">${inner}</div>${hostBar(`<button class="btn btn-ghost" data-act="end">End game</button>${btn}`)}`; bind(); };
  const next = (label) => `<button class="btn btn-primary" data-act="primary">${label}</button>`;
  const secs = (ms) => `<div class="xmclock" id="xmCount" data-end="${Date.now() + Math.max(0, ms)}">${Math.max(0, Math.ceil(ms / 1000))}</div>`;
  if (sc.kind === 'pinch') {
    if (sc.step === 'pick') return wrap(`<div class="xmbig">🤚 PINCH!</div><p class="xmline"><b>${esc(pem(sc.by))} ${esc(pname(sc.by))}</b> was the quickest finger on that question. They may nick any dish they haven't got from another plate, and they are choosing on their phone right now…</p>${secs(sc.until - Date.now())}${xmTableHtml()}`, next('Pick for them ▶'));
    return wrap(`<div class="xmbig">🤚 ${sc.res?.ok ? 'GOTCHA!' : 'FOILED!'}</div><p class="xmline big">${esc(sc.res?.line || '')}</p>${xmTableHtml()}`, next('Continue ▶'));
  }
  if (sc.kind === 'elf') {
    if (sc.step === 'spot') return wrap(`<div class="xmelfrun">🧝</div><div class="xmbig">SPOT THE ELF!</div><p class="xmline">He is hiding on your phone! Tap him first and you choose two plates for him to swap.</p>${secs(sc.until - Date.now())}`, next('Skip ▶'));
    if (sc.step === 'choose') return wrap(`<div class="xmelfwave">🧝</div><div class="xmbig">${esc(pname(sc.spotter))} SPOTTED HIM!</div><p class="xmline">${esc(pem(sc.spotter))} ${esc(pname(sc.spotter))} is choosing two plates for the elf to swap…</p>${secs(sc.until - Date.now())}${xmTableHtml()}`, next('Let the elf choose ▶'));
    return wrap(`<div class="xmelfwave">🧝</div><div class="xmbig">${sc.res?.ok ? 'THE ELF HAS STRUCK!' : 'THE ELF IS DISAPPOINTED'}</div><p class="xmline big">${esc(sc.res?.line || '')}</p>${sc.spotter ? '' : '<p class="xmline small">Nobody spotted him, so he chose for himself.</p>'}${xmTableHtml()}`, next('Continue ▶'));
  }
  if (sc.kind === 'uncle') return wrap(`<div class="xmbig">🧔 UNCLE KEITH IS UP TO NO GOOD</div><p class="xmline big">${esc(sc.res?.line || '')}</p>${xmTableHtml()}`, next('Continue ▶'));
  if (sc.kind === 'monopoly') return wrap(`<div class="xmbig">🎲 THE MONOPOLY ARGUMENT</div><p class="xmline">Somebody landed on Mayfair and somebody else won't accept the rules…</p><p class="xmline big">${esc(sc.res?.line || '')}</p>`, next('Continue ▶'));
  if (sc.kind === 'table') return wrap(`<div class="xmbig">🍽 THE DINNER TABLE</div><p class="xmline small">${XM.ITEMS.map((i) => `${i.icon} ${i.name} · ${xmLeft(i.k)} left`).join(' &nbsp;·&nbsp; ')}</p>${xmTableHtml()}`, next('Carry on ▶'));
  if (sc.kind === 'final') {
    const fin = G.xm.final || {}, full = xmPlayers().filter((p) => fin[p]?.full);
    return wrap(`<div class="xmbig">🎄 THE DINNER IS SERVED</div><p class="xmline">${full.length ? `A full plate: ${esc(full.map(pname).join(', '))}. +${XC.FULL.toLocaleString('en-GB')} each!` : 'Nobody completed their plate.'} Every missing dish costs ${Math.abs(XC.MISSING).toLocaleString('en-GB')}.</p>${xmTableHtml(fin)}`, next('Final results 🏆'));
  }
  return wrap('', next('Continue ▶'));
}
let xmWaveAt = 0;
/** Over the stage: the clock, the dish up for grabs, who collected it, the power cut, and the elf waving now and then. */
function xmDecorate() {
  ['xmclock', 'xmchip', 'xmgot', 'xmdark'].forEach((id) => document.getElementById(id)?.remove());
  if (!G || !xmOn() || G.phase === 'lobby' || G.phase === 'final') return;
  const add = (id, cls, html) => { const el = document.createElement('div'); el.id = id; el.className = cls; el.innerHTML = html; document.body.appendChild(el); return el; };
  if (!G.xm.screen) { const cl = xmClock(); add('xmclock', 'xmclock-pill', `<span>${cl.icon}</span><b>${cl.time}</b><small>${esc(cl.scene)}</small>`); }
  const q = question(), k = !G.xm.screen && ['typecard', 'countdown', 'question'].includes(G.phase) ? xmDish(q) : null;
  if (k) {
    const it = XM.item(k), R = XM.RARITY[it.rar], left = xmLeft(k);
    if (it.ketchup) { const el = G.phase === 'question' ? (G.q?.xelig || []) : xmPlayers().filter((p) => xmFull9(p)); add('xmchip', 'xmchip ketchup', `🍅 <b>THE KETCHUP QUESTION</b><span>Only a full plate can win it. ${el.length ? 'In the running: ' + esc(el.map(pname).join(', ')) : 'Nobody has a full plate yet'}</span>`); }
    else add('xmchip', 'xmchip', `${it.icon} <b>Win the ${esc(it.name)}</b><span>${esc(it.cat)} · ${R.stars} ${R.label}${it.rar > 1 ? ' · only the quickest right answers collect it' : ''} · ${left} chance${left === 1 ? '' : 's'} left</span>`);
  }
  if (['reveal', 'scoreboard'].includes(G.phase) && G.q?.xgot && !G.xm.screen) {
    const by = {}; for (const g of G.q.xgot) (by[g.k] = by[g.k] || []).push(g.pid);
    const bits = Object.entries(by).map(([kk, ps]) => `${XM.item(kk).icon} ${esc(XM.item(kk).name)}: ${esc(ps.map(pname).join(', '))}`);
    const slow = (G.q.xslow || []).length ? `<span>😬 Right but too slow: ${esc(G.q.xslow.map(pname).join(', '))}</span>` : '';
    if (bits.length || slow) add('xmgot', 'xmgot', `${bits.length ? `<b>🍽 Collected</b> ${bits.join(' · ')}` : '<b>🍽 Nobody collected anything</b>'}${slow}`);
  }
  if (G.phase === 'question' && G.q?.xdark) add('xmdark', 'xmdark', '<div class="xmcandle">🕯</div><div class="xmdark-t">POWER CUT!</div><div class="xmdark-s">The lights have gone out. Read the question on your phone… the host will read it out.</div>');
  if (['reveal', 'scoreboard'].includes(G.phase) && Date.now() - xmWaveAt > 90000 && chance(0.3)) { xmWaveAt = Date.now(); xmElfWave(); G.xm.waveN++; broadcastState(); }
  xmBotPlay();
}
function xmElfWave() {
  document.getElementById('xmelf')?.remove();
  const el = document.createElement('div'); el.id = 'xmelf'; el.className = 'xmelf ' + partyPick(['run', 'peek', 'peek-r']); el.textContent = '🧝';
  document.body.appendChild(el); setTimeout(() => el.remove(), 7000);
}
function xmBellShow() {
  const el = document.createElement('div'); el.className = 'xmbell'; el.innerHTML = '<div class="xmbell-i">🔔</div><div class="xmbell-t">DING DONG!</div><div class="xmbell-s">Auntie Maureen is at the door with a bonus: DOUBLE POINTS on this question!</div>';
  document.body.appendChild(el); sound('ding'); setTimeout(() => el.classList.add('out'), 3600); setTimeout(() => el.remove(), 4400);
}
/** In auto mode the host's clicks come from the phones, so a screen waiting for a choice must not be skipped by the auto-advance. */
function xmArmAuto() { /* nothing: scheduleAuto already stands down while a screen is up (host.html) */ }
