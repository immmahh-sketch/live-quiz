/* Box Clever on the phones (the phone half of assets/boxes.js). Everyone on a team can vote on every decision; the captain sees how
 * the team is voting and has the deciding say. Messages go out as answers: { bx: 'v', k, v, go, dbl, target }. */
const bxName = (s, pid) => s.bx.names?.[pid]?.name || 'someone', bxEm = (s, pid) => s.bx.names?.[pid]?.emoji || '🙂';
const bxFmt = (n) => Math.round(n).toLocaleString('en-GB');
const BXP = { double: ['⚡', 'Double bet'], swap: ['🔄', 'Swap question'], make: ['👉', 'Make them answer'], host: ['🎤', 'Make the host answer'], fifty: ['✂️', '50:50'], pickfor: ['👈', 'Pick their box'] };
const BXC = ['#e21b3c', '#1368ce', '#d89e00', '#26890c'];
const bxSel = () => (P.bxSel = P.bxSel && P.bxSel.k === (P.state?.bx?.step + ':' + (P.state?.bx?.cur?.num || '') + ':' + (P.state?.bx?.cur?.q?.t || '')) ? P.bxSel : { k: P.state.bx.step + ':' + (P.state.bx.cur?.num || '') + ':' + (P.state.bx.cur?.q?.t || ''), v: null, dbl: false, text: '', power: null });
function bxSend(k, v, extra) { send('answer', { pid: P.pid, qId: P.state.q.id, answer: { bx: 'v', k, v, ...(extra || {}) } }); }
function bxMe(s) { const g = s.bx, ti = g.teams.findIndex((t) => t.members.includes(P.pid)); return { ti, t: g.teams[ti], cap: g.teams[ti]?.captain === P.pid }; }
const bxTeamHead = (t) => `<div class="bxph" style="--tc:${t.color}"><span>${t.emoji} ${esc(t.name)}${t.loan ? ` <small>🏦 owes ${bxFmt(t.loan)}</small>` : ''}</span><b>${bxFmt(t.pot)}</b></div>`;
let bxPaperDone = '';
function bxBoardHtml(s, canPick, votes, sel) {
  const g = s.bx;
  return `<div class="bxpboard">${g.cats.map((c, r) => `<div class="bxprow"><div class="bxpcat">${c.e} ${esc(c.n)}</div><div class="bxpcells">${Array.from({ length: g.cols }, (_, k) => { const n = r * g.cols + k + 1, st = g.board[n - 1], open = st === 'open' && canPick;
    const cnt = Object.values(votes || {}).filter((x) => x === n).length;
    const gone = st === 'won' || st === 'lost' || st === 'void';
    return `<button type="button" class="bxpb ${gone ? 'gone' : st} ${sel === n ? 'sel' : ''} ${(votes || {})[P.pid] === n ? 'mine' : ''}" data-bxn="${n}" ${open ? '' : 'disabled'}>${gone ? '' : n}${cnt && st === 'open' ? `<i>${cnt}</i>` : ''}</button>`; }).join('')}</div></div>`).join('')}</div>`;
}
function bxKey(s) {
  const g = s.bx, me = bxMe(s), c = g.cur, v = g.votes || {}, sel = P.bxSel;
  return ['bx', g.step, g.turn, g.pickTeam, JSON.stringify(g.forcedBy), g.asked, g.part, c?.num, c?.q?.t, c?.q?.opts?.length, c?.locked ? 1 : 0, c?.by, c?.mode, c?.sub, c?.dbl ? 1 : 0, c?.stake, c?.at, g.closing ? 1 : 0, c?.res?.delta, me.cap ? 'C' : 'm', me.t?.pot, me.t?.loan, me.t ? Object.values(me.t.powers).join('') : '',
    me.t?.captain, sel ? [sel.v, sel.dbl, sel.power].join() : '', me.cap || g.step === 'vote' ? JSON.stringify(v) : (v[P.pid] ?? '') + (v.ans?.[P.pid] ?? '') + (v.pow?.[P.pid] ?? '') + (v.pass?.[P.pid] ?? ''), g.teams.map((t) => t.pot).join()].join('|');
}
function bxPhoneHtml(s) { app.className = 'app'; return s.bx.solo ? bxSoloHtml(s) : bxPhoneBody(s); }
function bxPhoneBody(s) {
  const g = s.bx, me = bxMe(s), c = g.cur, A = g.solo ? ['is', 'has'] : ['are', 'have'];
  if (me.ti < 0) return `<div class="state"><div class="em">📦</div><h2>Box Clever</h2><p class="muted">You'll be put on a team in a moment…</p></div>`;
  const t = me.t, sel = bxSel(), head = g.solo ? '' : bxTeamHead(t) + (me.cap ? '<div class="bxcapbadge">👑 You are the captain</div>' : '');
  const mates = t.members.filter((m) => m !== P.pid).map((m) => bxEm(s, m) + ' ' + esc(bxName(s, m))).join(', ');
  if (g.step === 'teams') return `${head}<div class="state"><div class="em">${t.emoji}</div><h2>You're on ${esc(t.name)}</h2><p class="muted">${mates ? 'With ' + mates : 'On your own'}.<br>Watch the big screen…</p></div>`;
  if (g.step === 'vote') {
    const mine = g.votes[P.pid];
    return `${head}<h2 class="bxh">👑 Who should be captain?</h2><p class="muted">The captain has the deciding say on everything. Tap a teammate.</p>
      <div class="bxlist">${t.members.map((m) => `<button type="button" class="bxcand ${mine === m ? 'sel' : ''}" data-bxcap="${m}">${bxEm(s, m)} ${esc(bxName(s, m))}${m === P.pid ? ' (you)' : ''}</button>`).join('')}</div>${mine ? '<p class="muted">Vote in. You can change it until the host counts them.</p>' : ''}`;
  }
  if (g.step === 'captains') return `${head}<div class="state"><div class="em">${me.cap ? '👑' : '🙌'}</div><h2>${me.cap ? "You're the captain!" : esc(bxName(s, t.captain)) + ' is your captain'}</h2>${t.spin?.tie ? '<p class="muted">It was a tie, so the spinner chose.</p>' : ''}<p class="muted">${me.cap ? 'You make the final call. Your team can vote to help you.' : 'Vote on your phone, and the captain decides.'}</p></div>`;
  if (g.step === 'seg' && g.solo) {
    const d = (g.absorb || {})[me.ti] || 0, others = g.teams.length - 1;
    return g.part === 1
      ? `<div class="state"><div class="em">📦</div><h2>Box Clever</h2><p>You against ${others} bot${others === 1 ? '' : 's'}. ${g.total} boxes, ${bxFmt(t.pot)} points each to start.</p><p class="muted">Pick a box and choose how much to gamble. Right and you win your stake; wrong and you lose it. Not sure? Pass and lose half, but the box stays open for the next player. Use each power once.</p><button type="button" class="btn btn-primary btn-lg btn-block" id="bxNext">Let's go ▶</button></div>`
      : `<div class="state"><div class="em">💰</div><h2>Bonus round points are in</h2><p>${d ? `<b>${d > 0 ? '+' : '−'}${bxFmt(Math.abs(d))}</b> for you. ` : ''}You now have <b>${bxFmt(t.pot)}</b>.</p><button type="button" class="btn btn-primary btn-lg btn-block" id="bxNext">Back to the boxes ▶</button></div>`;
  }
  if (g.step === 'seg') return `${head}<div class="state"><div class="em">💰</div><h2>${g.part === 1 ? 'Get ready' : 'Bonus points are in'}</h2><p class="muted">Your pot: ${bxFmt(t.pot)}</p></div>`;
  const mineTurn = g.turn === me.ti;
  if (g.step === 'pick') {
    const at = g.teams[g.turn], picker = g.teams[g.pickTeam], mePick = g.pickTeam === me.ti;
    if (!mePick) return `${head}<div class="state" style="flex:0 0 auto;padding:6px"><h2>${picker.emoji} ${esc(picker.name)} ${g.pickTeam === g.turn ? `${A[0]} choosing a box…` : `${A[0]} choosing ${at.emoji} ${esc(at.name)}'s box…`}</h2></div>${g.solo ? '' : bxBoardHtml(s, false, {}, null)}`;
    const votes = g.votes, chosen = sel.v, forced = g.pickTeam !== g.turn;
    // Pick their box: on the team's own turn, before its box is chosen
    let pw = '';
    if (!forced && t.powers.pickfor) {
      const pv = g.votes.pow || {}, n = Object.values(pv).filter((x) => x === 'pickfor').length;
      pw = `<button type="button" class="bxpow ${sel.power === 'pickfor' ? 'sel' : ''}" data-bxp="pickfor" style="width:100%">👈 Pick their box${n ? `<i>${n}</i>` : ''}</button>`;
      if (sel.power === 'pickfor') pw += `<p class="muted">Choose a team. You pick the box they must play next:</p><div class="bxlist">${g.teams.filter((x) => x.i !== me.ti && g.forcedBy[x.i] === undefined).map((x) => `<button type="button" class="bxcand" data-bxtarget="${x.i}">${x.emoji} ${esc(x.name)}</button>`).join('')}</div>`;
    }
    return `${head}<h2 class="bxh">${forced ? `Pick ${at.emoji} ${esc(at.name)}'s box!` : 'Pick a box'}</h2><p class="muted">${forced ? 'You played Pick their box: they still decide how much to bet.<br>' : ''}${g.solo ? 'Tap a drawer, then lock it in.' : me.cap ? 'Tap a box, then lock it in. Numbers show your team\'s votes.' : 'Tap the box you want. Your captain decides.'}</p>${g.solo ? '' : bxBoardHtml(s, true, votes, me.cap ? chosen : votes[P.pid])}
      ${me.cap ? `<button type="button" class="btn btn-primary btn-lg btn-block bxlock" id="bxLock" ${chosen ? '' : 'disabled'}>${chosen ? 'Lock in box ' + chosen : 'Tap a box'}</button>` : ''}${pw}`;
  }
  if (g.step === 'stake') {
    const at = g.teams[g.turn];
    if (!mineTurn) return `${head}<div class="state"><div class="em">🎲</div><h2>${at.emoji} ${esc(at.name)} ${A[0]} deciding how much to gamble…</h2><p class="muted">Box ${c.num} · ${esc(g.cats[c.cat].n)}</p></div>`;
    const votes = g.votes, my = votes[P.pid], chosen = me.cap ? sel.v : my?.amt, chips = t.stakes || [];
    const dbl = me.cap ? sel.dbl : !!my?.dbl, cnt = (amt) => Object.values(votes).filter((x) => x && x.amt === amt).length;
    return `${head}<h2 class="bxh">🎲 How much will you gamble?</h2><p class="muted">Box ${c.num} · ${esc(g.cats[c.cat].n)}. Right: you get double back. Wrong: it's gone.</p>
      <div class="bxchips">${chips.map((x, i) => `<button type="button" class="bxchip ${chosen === x ? 'sel' : ''}" data-bxs="${x}">${i === chips.length - 1 ? 'ALL IN ' : ''}${bxFmt(x)}${cnt(x) ? `<i>${cnt(x)}</i>` : ''}</button>`).join('')}</div>
      <form id="bxCust" class="bxform"><input type="number" id="bxCustIn" inputmode="numeric" min="1" max="${t.pot}" placeholder="Or type your own stake" autocomplete="off" value="${esc(sel.cust || '')}"><button class="btn btn-primary" type="submit">Use</button></form>
      ${t.powers.double ? `<button type="button" class="bxpow ${dbl ? 'sel' : ''}" id="bxDbl">⚡ Double bet: 4× back if right ${dbl ? '(on)' : ''}</button>` : ''}
      ${me.cap ? `<button type="button" class="btn btn-primary btn-lg btn-block bxlock" id="bxLockS" ${chosen ? '' : 'disabled'}>${chosen ? 'Gamble ' + bxFmt(chosen) + (dbl ? ' with Double bet' : '') : 'Pick an amount'}</button>` : ''}`;
  }
  // the question
  if (!c) return `<div class="state"><div class="em">📦</div></div>`;
  const ans = g.teams[c.by], mineAns = c.by === me.ti, org = g.teams[c.origin];
  const tags = `<div class="bxtags"><span>Box ${c.num}</span><span>🎲 ${bxFmt(c.stake)}${c.dbl ? ' ⚡×4' : ''}</span>${c.mode === 'made' ? `<span>👉 ${esc(ans.name)} must answer</span>` : ''}${c.mode === 'host' ? '<span>🎤 Host answers</span>' : ''}</div>`;
  const q = `<h2 class="bxqph">${esc(c.q.t)}</h2>${bxMediaPhone(s)}`;
  if (g.step === 'open') return `${head}${tags}<div class="state"><div class="em">🗄️</div><h2>Opening box ${c.num}…</h2><p class="muted">${esc(g.cats[c.cat].e)} ${esc(g.cats[c.cat].n)}${g.solo ? '' : ' · the host is pulling out the drawer'}</p></div>`;
  if (g.step === 'result') {
    const r = c.res, rt = g.teams[r.team];
    if (r.passed) return `${head}${tags}${q}<div class="bxres pass"><div class="bxbig">🏳️ Passed</div><p>The box goes back, and the next team to take it can't pass.</p><p><b>${rt.emoji} ${esc(rt.name)} −${bxFmt(Math.abs(r.delta))}</b></p>${bxBrokeP(g, r)}<p class="muted">Remember this question!</p>${bxNextBtn(g)}</div>`;
    return `${head}${tags}${q}<div class="bxres ${r.ok ? 'ok' : 'no'}"><div class="bxbig">${r.ok ? '✅ Correct!' : '❌ Wrong'}</div><p>${esc(r.right)}</p><p><b>${rt.emoji} ${esc(rt.name)} ${r.delta >= 0 ? '+' : '−'}${bxFmt(Math.abs(r.delta))}</b></p>${bxBrokeP(g, r)}${bxNextBtn(g)}</div>`;
  }
  if (c.mode === 'host') return `${head}${tags}${q}<div class="state" style="padding:8px"><div class="em">🎤</div><h2>The host has to answer this one!</h2><p class="muted">It counts for ${org.emoji} ${esc(org.name)}.</p></div>`;
  if (!mineAns) return `${head}${tags}${q}<div class="state" style="padding:8px"><h2>${ans.emoji} ${esc(ans.name)} ${c.locked ? `${A[1]} locked in an answer` : `${A[0]} answering`}…</h2></div>${c.q.opts ? `<div class="bxwatch">${c.q.opts.map((o) => `<div>${esc(o)}</div>`).join('')}</div>` : ''}`;
  if (c.locked) return `${head}${tags}${q}<div class="state" style="padding:8px"><div class="em">🔒</div><h2>Locked in</h2><p class="muted">${c.q.opts ? esc(c.q.opts[c.lockedAs]) : esc(String(c.lockedAs))}</p><p class="muted">${g.solo ? 'Revealing…' : 'Waiting for the host to reveal it…'}</p></div>`;
  const votes = g.votes.ans || {}, my = votes[P.pid], vals = Object.entries(votes);
  let body = '';
  if (c.q.opts) {
    body = `<div class="bxoptsp">${c.q.opts.map((o, i) => { const n = vals.filter(([, v]) => v === i).length, chosen = me.cap ? sel.v === i : my === i; return `<button type="button" class="bxop ${chosen ? 'sel' : ''}" style="--oc:${BXC[i % 4]}" data-bxa="${i}"><span>${esc(o)}</span>${me.cap && n ? `<i>${n}</i>` : (my === i ? '<i>✓</i>' : '')}</button>`; }).join('')}</div>`;
  } else {
    const typed = {}; for (const [pid, v] of vals) { const k = String(v).toLowerCase(); (typed[k] = typed[k] || { t: v, n: 0, who: [] }).n++; typed[k].who.push(bxName(s, pid)); }
    body = `<form id="bxTxt" class="bxform"><input type="text" id="bxIn" maxlength="60" placeholder="Type your answer" autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false" value="${esc(me.cap ? sel.text : (typeof my === 'string' ? my : ''))}"><button class="btn btn-primary" type="submit">${g.solo ? 'Lock in' : me.cap ? 'Use this' : 'Send'}</button></form>
      ${me.cap && !g.solo && Object.keys(typed).length ? `<p class="muted">Your team said (tap to use):</p><div class="bxlist">${Object.values(typed).map((x) => `<button type="button" class="bxcand ${sel.v === x.t ? 'sel' : ''}" data-bxt="${esc(x.t)}">${esc(x.t)} <i>${x.n}</i></button>`).join('')}</div>` : (my ? `<p class="muted">Sent: ${esc(String(my))}</p>` : '')}`;
  }
  const lockVal = me.cap ? (c.q.opts ? sel.v : sel.v) : null;
  const lock = me.cap ? `<button type="button" class="btn btn-primary btn-lg btn-block bxlock" id="bxLockA" ${lockVal !== null && lockVal !== '' && lockVal !== undefined ? '' : 'disabled'}>${lockVal !== null && lockVal !== '' && lockVal !== undefined ? 'Lock in: ' + esc(c.q.opts ? c.q.opts[lockVal] : String(lockVal)) : 'Choose an answer'}</button>` : '<p class="muted center">Your captain decides.</p>';
  // powers: the team that asked, before an answer is locked in and while they are still the ones answering
  let pw = '';
  if (c.canPass) {
    const pn = Object.keys(g.votes.pass || {}).length, half = Math.min(Math.floor(c.stake / 2), t.pot);
    pw += `<button type="button" class="bxpow bxpass" id="bxPass">🏳️ Pass: lose ${bxFmt(half)}, keep the box shut${pn ? `<i>${pn}</i>` : ''}</button>`;
  } else if (c.mode === 'own') pw += `<p class="muted center">👀 This box was passed earlier, so you have to answer it.</p>`;
  if (c.mode === 'own' && c.origin === me.ti) {
    const pv = g.votes.pow || {};
    pw += `<div class="bxpows">${['fifty', 'swap', 'make', 'host', 'pickfor'].filter((k) => t.powers[k] !== undefined).map((k) => { const have = t.powers[k], n = Object.values(pv).filter((x) => x === k).length, on = sel.power === k; return `<button type="button" class="bxpow ${have ? '' : 'gone'} ${on ? 'sel' : ''}" data-bxp="${k}" ${have ? '' : 'disabled'}>${BXP[k][0]} ${BXP[k][1]}${n ? `<i>${n}</i>` : ''}</button>`; }).join('')}</div>`;
    if (sel.power === 'make' || sel.power === 'pickfor') pw += `<p class="muted">${sel.power === 'make' ? 'Which team must answer?' : 'Whose next box will you pick?'}</p><div class="bxlist">${g.teams.filter((x) => x.i !== me.ti && (sel.power === 'make' || g.forcedBy[x.i] === undefined)).map((x) => `<button type="button" class="bxcand" data-bxtarget="${x.i}">${x.emoji} ${esc(x.name)}</button>`).join('')}</div>`;
    else if (sel.power && me.cap) pw += `<button type="button" class="btn btn-ghost btn-block" id="bxUse">Use ${BXP[sel.power][1]}</button>`;
  } else if (c.mode === 'made') pw += `<p class="muted center">👉 ${esc(org.name)} made you answer! Your points change, not theirs.</p>`;
  return `${head}${tags}${q}${body}${lock}${pw}`;
}
function bxBind(s) {
  const g = s.bx, me = bxMe(s), sel = bxSel(), redo = () => { P.viewKey = ''; render(); };
  $$('[data-bxcap]').forEach((b) => b.onclick = () => { bxSend('cap', b.dataset.bxcap); });
  $$('[data-bxn]').forEach((b) => b.onclick = () => { const n = +b.dataset.bxn; bxSend('pick', n); sel.v = n; redo(); });
  if ($('#bxLock')) $('#bxLock').onclick = () => { if (sel.v) { bxSend('pick', sel.v, { go: true }); $('#bxLock').disabled = true; } };
  $$('[data-bxs]').forEach((b) => b.onclick = () => { sel.v = +b.dataset.bxs; sel.cust = ''; bxSend('stake', sel.v, { dbl: sel.dbl }); redo(); });
  if ($('#bxCust')) { $('#bxCustIn').oninput = (e) => { sel.cust = e.target.value; }; $('#bxCust').onsubmit = (e) => { e.preventDefault(); let n = Math.round(+$('#bxCustIn').value); if (!(n >= 1) || !me.t) return; n = Math.min(n, me.t.pot); sel.v = n; sel.cust = String(n); bxSend('stake', n, { dbl: sel.dbl }); redo(); }; }
  const tune = $('#ptuneAgain'); // Name That Tune: on one phone the clip plays here (a hosted game plays it on the host's screen)
  if (tune && g.cur?.q?.m) { const m = g.cur.q.m, qid = 'bx' + g.cur.num + ':' + g.cur.at, go = () => playPhoneTune({ url: m.url, start: m.start || 0, len: m.len || 15, backwards: false }, qid); tune.onclick = go; if (g.step === 'result') { if (P.bxTuned) { P.bxTuned = ''; try { stopPhoneTune(); } catch {} } } else if (P.bxTuned !== qid) { P.bxTuned = qid; go(); } }
  else if (P.bxTuned) { P.bxTuned = ''; try { stopPhoneTune(); } catch {} }
  if ($('#bxNext')) $('#bxNext').onclick = () => { $('#bxNext').disabled = true; bxSend('next', 1); };
  const paper = $('.bxpaper.fresh'); // the paper comes out of the drawer and unfolds the first time it is drawn
  if (paper) { const drawer = $('.bxdr.out'); if (drawer) { const a = drawer.getBoundingClientRect(), o = paper.getBoundingClientRect(); paper.style.setProperty('--dx', (a.left + a.width / 2 - (o.left + o.width / 2)) + 'px'); paper.style.setProperty('--dy', (a.top + a.height / 2 - (o.top + o.height / 2)) + 'px'); } paper.style.animationPlayState = 'running'; bxPaperDone = paper.dataset.key; try { window.scrollTo(0, 0); } catch {} }
  if ($('#bxDbl')) $('#bxDbl').onclick = () => { sel.dbl = !sel.dbl; if (sel.v) bxSend('stake', sel.v, { dbl: sel.dbl }); redo(); };
  if ($('#bxLockS')) $('#bxLockS').onclick = () => { if (sel.v) { bxSend('stake', sel.v, { dbl: sel.dbl, go: true }); $('#bxLockS').disabled = true; } };
  $$('[data-bxa]').forEach((b) => b.onclick = () => { const i = +b.dataset.bxa; bxSend('ans', i); sel.v = i; redo(); });
  $$('[data-bxt]').forEach((b) => b.onclick = () => { sel.v = b.dataset.bxt; redo(); });
  if ($('#bxTxt')) $('#bxTxt').onsubmit = (e) => { e.preventDefault(); const t = $('#bxIn').value.trim(); if (!t) return; if (g.solo) { bxSend('ans', t, { go: true }); sel.text = t; sel.v = t; return; } bxSend('ans', t); sel.text = t; sel.v = t; redo(); };
  if ($('#bxPass')) $('#bxPass').onclick = () => {
    if (me.cap) { if (confirm(g.solo ? 'Pass? You lose half your stake. The box stays open, and anyone who takes it later has seen the question.' : 'Pass on this question? You lose half your stake, the box goes back, and everyone has seen the question.')) bxSend('pass', 1, { go: true }); }
    else { bxSend('pass', 1); }
  };
  if ($('#bxLockA')) $('#bxLockA').onclick = () => { if (sel.v !== null && sel.v !== '' && sel.v !== undefined) { bxSend('ans', sel.v, { go: true }); $('#bxLockA').disabled = true; } };
  $$('[data-bxp]').forEach((b) => b.onclick = () => { const k = b.dataset.bxp; sel.power = sel.power === k ? null : k; bxSend('pow', k); redo(); });
  if ($('#bxUse')) $('#bxUse').onclick = () => { bxSend('pow', sel.power, { go: true }); sel.power = null; $('#bxUse').disabled = true; };
  $$('[data-bxtarget]').forEach((b) => b.onclick = () => { bxSend('pow', sel.power || 'make', { go: true, target: +b.dataset.bxtarget }); sel.power = null; });
}

const bxBrokeP = (g, r) => r.broke ? `<p class="bxbroke">💸 <b>Bankrupt!</b> The bank lends you ${bxFmt(1000)} to carry on. It comes off your score at the end.</p>` : '';
const bxNextBtn = (g) => g.solo ? '<button type="button" class="btn btn-primary btn-lg btn-block" id="bxNext">Next ▶</button>' : '';

// ---------------------------------------------------------------- the warm-up: everything on this one phone
/** The cabinet on the phone: a drawer for every box. The chosen one glows; an answered one is pulled out while its question is open, then shuts with the number gone. */
function bxPhoneCab(s, canPick) {
  const g = s.bx, c = g.cur, st = g.step, sel = bxSel(), inQ = c && ['ask', 'locked', 'result'].includes(st), inSel = c && ['stake', 'open'].includes(st);
  return `<div class="bxcab ph ${inQ ? 'mini' : ''}" style="--cols:${g.cols}">${g.cats.map((cat, r) => `<div class="bxcabrow"><div class="bxcat">${cat.e} ${esc(cat.n)}</div><div class="bxdrawers">${Array.from({ length: g.cols }, (_, k) => {
    const n = r * g.cols + k + 1, stt = g.board[n - 1], cur = c && c.num === n, done = stt === 'won' || stt === 'lost' || stt === 'void', can = canPick && stt === 'open';
    const cls = cur && inQ ? 'out' : cur && inSel ? 'sel' : can && sel.v === n ? 'sel' : done ? 'done' : '';
    const by = g.boardBy?.[n - 1], tc = done && by >= 0 ? `--tc:${g.teams[by]?.color}` : '';
    return `<div class="bxdr ${cls}${cur && inQ && g.closing ? ' shut' : ''}${can ? ' pk' : ''}" ${can ? `data-bxn="${n}"` : ''} style="${tc}"><div class="bxdrface"><span class="bxplate">${done ? '' : n}</span><i class="bxhandle"></i></div></div>`; }).join('')}</div></div>`).join('')}</div>`;
}
function bxSoloHtml(s) {
  const g = s.bx, me = bxMe(s), c = g.cur, st = g.step; if (me.ti < 0) return bxPhoneBody(s);
  const act = c && st !== 'pick' ? c.by : g.turn;
  const strip = `<div class="bxrivals">${g.teams.map((t) => `<div class="bxrv ${st !== 'seg' && t.i === act ? 'on' : ''} ${t.i === me.ti ? 'me' : ''}" style="--tc:${t.color}"><span>${t.emoji}</span><i>${t.i === me.ti ? 'You' : esc(t.name)}</i><b>${bxFmt(t.pot)}</b>${t.loan ? '<em title="Borrowed from the bank">🏦</em>' : ''}</div>`).join('')}</div>`;
  const pw = Object.entries(me.t.powers).map(([k, v]) => `<span class="${v ? '' : 'gone'}" title="${BXP[k][1]}">${BXP[k][0]}</span>`).join('');
  const head = `${strip}${st === 'seg' ? '' : `<div class="bxmeta"><span class="bxmp">${pw}</span><span>📦 ${g.asked} of ${g.total}</span></div>`}`;
  const body = bxPhoneBody(s);
  if (st === 'seg') return head + body;
  const inQ = c && ['ask', 'locked', 'result'].includes(st), cab = bxPhoneCab(s, st === 'pick' && g.pickTeam === me.ti);
  if (!inQ) return `${head}${cab}${body}`;
  const key = c.num + ':' + (c.at || 0);
  return `${head}${cab}<div class="bxpaper ph ${bxPaperDone !== key ? 'fresh' : ''} ${g.closing ? 'fold' : ''}" data-key="${key}">${body}</div>`;
}

/** The picture of a question (blurred at first, clearing over 20 seconds: it keeps its place when the screen redraws) or its tune player. */
function bxMediaPhone(s) {
  const g = s.bx, c = g.cur, m = c?.q?.m; if (!m) return '';
  const key = c.num + ':' + (c.at || 0) + ':' + m.url;
  if (!P.bxSeen || P.bxSeen.key !== key) P.bxSeen = { key, t: Date.now() };
  if (m.k === 'img') return `<div class="bxpic"><img src="${esc(m.url)}" alt="" style="animation-delay:-${g.step === 'result' ? 99 : ((Date.now() - P.bxSeen.t) / 1000).toFixed(1)}s"></div>`;
  if (m.k === 'tune') return g.solo ? `<div class="bxtune"><span class="bxvinyl" id="pvinyl"></span><div class="bxtbar"><i id="pbar"></i></div><button type="button" class="btn btn-ghost btn-sm" id="ptuneAgain">▶ Play</button></div>` : '<p class="muted center">🎵 Listen to the screen</p>';
  return '';
}
