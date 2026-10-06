/* Let's Quiz phones: the party pieces (October 2026), the phone half of assets/party.js.
 *  - Power cards: the hand in a 🃏 button, played between questions; what's been done to you on a question.
 *  - Play Your Cards Right: Higher / Lower.  - Taskmaster: take (or pick) a photo, shrink it, send it.
 *  - Who Said That?: the quote and the names (the author is told it's theirs).  - About You (warm-up): type an answer.
 * Loaded before play.html's own script; runs once a game is going, when play.html's globals (P, app, send…) exist. */

const PCARDS = {
  steal: { icon: '💰', name: 'Steal 1000', how: 'Take 1,000 points off someone, right now', target: true },
  copy: { icon: '🪞', name: 'Copycat', how: "Your answer on the next question is whatever they answer", target: true },
  x5: { icon: '🔥', name: '5× points', how: 'Your points on the next question count five times. Played blind!', target: false },
  slow: { icon: '🐌', name: 'Slow down', how: 'Cut their time on the next question by 30%', target: true },
  freeze: { icon: '🥶', name: 'Freeze', how: 'They sit out the next question', target: true },
};
const partyName = (s, pid) => s.power?.players?.find((p) => p.pid === pid)?.name || s.names?.[pid]?.name || 'someone';

// ---------------------------------------------------------------- power cards
/** Every state: the 🃏 button (with the hand), and the big banner when anyone plays a card. */
function partyPhoneAfter(s) {
  const pw = s.power, hand = (pw?.hands?.[P.pid] || []);
  let b = document.getElementById('pcardsBtn');
  if (!pw || P.view || !hand.length || s.phase === 'final') { b?.remove(); document.getElementById('pcardsSheet')?.remove(); }
  else {
    if (!b) { b = document.createElement('button'); b.id = 'pcardsBtn'; b.className = 'pcardsbtn'; b.onclick = () => partyCardsSheet(); document.body.appendChild(b); }
    const can = pw.window && !pw.gap?.[P.pid];
    b.classList.toggle('live', can); b.innerHTML = `🃏 <b>${hand.length}</b><small>${can ? 'Play a card' : pw.gap?.[P.pid] ? 'Played' : 'After this one'}</small>`;
    const sh = document.getElementById('pcardsSheet'); if (sh && sh.dataset.key !== partySheetKey(s)) partyCardsSheet(true);
  }
  // the banner when a card is played: from the first state on, any new card (never an old one, on joining or reloading)
  const f = pw?.flash;
  if (pw && P.flashN === undefined) P.flashN = f?.n ?? 0;
  else if (f && f.n !== P.flashN) { P.flashN = f.n; if ((s.now || Date.now()) - f.at < 9000) partyFlash(f); }
}
const partySheetKey = (s) => [s.power?.window, s.power?.gap?.[P.pid], (s.power?.hands?.[P.pid] || []).map((c) => c.id).join()].join('|');
function partyFlash(f) {
  document.getElementById('pcflash')?.remove();
  const el = document.createElement('div'); el.id = 'pcflash'; el.className = 'pcflash';
  el.innerHTML = `<div class="pf-icon">${f.icon}</div><div class="pf-text">${esc(f.text)}</div>`;
  document.body.appendChild(el); if (navigator.vibrate) try { navigator.vibrate([60, 40, 60]); } catch {}
  setTimeout(() => el.classList.add('out'), 3800); setTimeout(() => el.remove(), 4500);
}
/** The hand: tap a card, then (for most) who to play it on. */
function partyCardsSheet(refresh) {
  const s = P.state; if (!s?.power) return;
  const old = document.getElementById('pcardsSheet'); if (old && !refresh) { old.remove(); return; }
  const hand = s.power.hands?.[P.pid] || [], can = s.power.window && !s.power.gap?.[P.pid];
  const el = old || document.createElement('div'); el.id = 'pcardsSheet'; el.className = 'pcsheet'; el.dataset.key = partySheetKey(s);
  const why = !s.power.window ? 'Cards are played between questions: wait for the answer or the scores.' : s.power.gap?.[P.pid] ? "You've played a card this break. Another after the next question." : 'Tap a card to play it.';
  el.innerHTML = `<div class="pcs-in"><div class="pcs-head"><b>🃏 Your power cards</b><button class="btn btn-ghost btn-sm" data-pcx>Close</button></div><p class="small muted" style="margin:0 0 8px">${why}</p>
    <div class="pcs-cards">${hand.map((c) => { const k = PCARDS[c.kind]; return `<button class="pcs-card" data-pcc="${c.id}" ${can ? '' : 'disabled'}><span class="pcs-ic">${k.icon}</span><span><b>${esc(k.name)}</b><small>${esc(k.how)}</small></span></button>`; }).join('')}</div><div id="pcsWho"></div></div>`;
  if (!old) document.body.appendChild(el);
  el.querySelector('[data-pcx]').onclick = () => el.remove();
  el.onclick = (e) => { if (e.target === el) el.remove(); };
  el.querySelectorAll('[data-pcc]').forEach((btn) => btn.onclick = () => {
    const c = hand.find((x) => x.id === btn.dataset.pcc), k = PCARDS[c.kind];
    el.querySelectorAll('[data-pcc]').forEach((x) => x.classList.toggle('sel', x === btn));
    const go = (target) => { send('card', { pid: P.pid, id: c.id, target }); el.remove(); toast(`${k.icon} ${k.name} played!`); };
    if (!k.target) { el.querySelector('#pcsWho').innerHTML = `<button class="btn btn-primary btn-lg btn-block mt" data-pgo>Play ${k.icon} ${esc(k.name)}</button>`; el.querySelector('[data-pgo]').onclick = () => go(null); return; }
    const others = (s.power.players || []).filter((p) => p.pid !== P.pid).sort((a, b) => b.score - a.score);
    el.querySelector('#pcsWho').innerHTML = `<p class="small" style="font-weight:800;margin:12px 0 6px">${k.icon} ${esc(k.name)} on who?</p><div class="pcs-who">${others.map((p) => `<button class="btn" data-pt="${p.pid}">${esc(p.emoji || '🙂')} ${esc(p.name)} <small class="muted">${p.score}</small></button>`).join('')}</div>`;
    el.querySelectorAll('[data-pt]').forEach((x) => x.onclick = () => go(x.dataset.pt));
  });
}
/** A question someone played a card on you for: frozen out, or copying (nothing to answer). */
function partyBlockHtml(s) {
  const fx = s.power?.fx; if (!fx || s.phase !== 'question') return '';
  if (fx.frozen?.[P.pid]) { app.className = 'app'; return `<div class="state"><div class="em">🥶</div><h2>Frozen!</h2><p class="muted">${esc(partyName(s, fx.frozen[P.pid]))} froze you out of this question. Sit tight, you thaw out for the next one.</p></div>`; }
  if (fx.copy?.[P.pid]) return `<div class="state"><div class="em">🪞</div><h2>You're copying ${esc(partyName(s, fx.copy[P.pid]))}</h2><p class="muted">Whatever they answer, you answer. Fingers crossed they know it!</p></div>`;
  return '';
}
/** On the question bar: 5× on you, or your time cut. */
function partyBadges(s) {
  const fx = s.power?.fx; if (!fx || s.phase !== 'question') return '';
  const out = [];
  if (fx.x5?.[P.pid]) out.push('🔥 5× points on this one!');
  if (fx.slow?.[P.pid]) out.push(`🐌 ${esc(partyName(s, fx.slow[P.pid]))} cut your time!`);
  return out.length ? `<div class="practicebar partybar">${out.join(' · ')}</div>` : '';
}
/** Slowed: this phone's clock runs 30% short (the host turns away answers after that). */
function partyDeadline(s) { if (s.phase === 'question' && s.q && s.power?.fx?.slow?.[P.pid]) P.deadline -= (s.q.time || 20) * 1000 * 0.3; }

// ---------------------------------------------------------------- the games: Play Your Cards Right, the quiz-night task
function partyGameKey(s) {
  if (s.pc) { const g = s.pc; return ['pc', g.step, g.i, g.alive.includes(P.pid), g.called.includes(P.pid)].join('|'); }
  if (s.tm) { const g = s.tm; return ['tm', g.step, g.round, g.picks.join(), g.spinning ? 's' : '', g.totalMs ? 'c' : ''].join('|'); }
  if (s.task) { const g = s.task; return ['task', g.step, g.got.includes(P.pid), P.work.taskBusy || '', P.work.taskPrev ? 'p' : '', P.work.taskErr || ''].join('|'); }
  return '';
}
const pcMini = (c, up) => `<div class="pcmini ${up ? 'up' : 'down'}"><div class="pclabel">${esc(c.label)}</div><div class="pcval">${up ? esc(c.show) : '?'}</div></div>`;
function pcPhoneHtml(s) {
  const g = s.pc, me = P.pid, cur = g.cards[g.i], nxt = g.cards[g.i + 1], mine = g.pts?.[me] || 0;
  app.className = 'app';
  const foot = mine ? `<p class="center small muted mt">You've won ${mine} so far</p>` : '';
  if (g.step === 'over') { const won = g.winners.includes(me); return `<div class="state"><div class="em">${won ? '🏆' : '🃏'}</div><h2>${won ? 'You made it to the end!' : g.winners.length ? `${esc(g.winners.map((p) => partyName(s, p)).join(', '))} made it` : 'Nobody made it to the end'}</h2><p class="muted">“${esc(g.banter || '')}”</p></div>${foot}`; }
  if (g.step === 'flip') {
    const r = g.last.right.includes(me), w = g.last.wrong.includes(me);
    if (r && navigator.vibrate) try { navigator.vibrate(80); } catch {}
    return `<div class="pcpair">${pcMini(g.cards[g.i - 1], true)}${pcMini(cur, true)}</div><div class="state" style="padding-top:6px"><div class="em">${r ? '✅' : w ? '❌' : g.last.up ? '⬆' : '⬇'}</div><h2>${g.last.up ? 'Higher!' : 'Lower!'} ${r ? `+${g.perCard}` : w ? "You're out" : ''}</h2><p class="muted">“${esc(g.banter || '')}”</p></div>${foot}`;
  }
  if (!g.alive.includes(me)) return `<div class="pcpair">${pcMini(cur, true)}${nxt ? pcMini(nxt, false) : ''}</div><div class="state" style="padding-top:6px"><div class="em">👀</div><h2>You're out</h2><p class="muted">Watch the others sweat…</p></div>${foot}`;
  if (g.called.includes(me)) { const c = P.work.pcCall?.k === s.q.id + g.i ? P.work.pcCall.c : ''; return `<div class="pcpair">${pcMini(cur, true)}${pcMini(nxt, false)}</div><div class="state" style="padding-top:6px"><div class="em">🔒</div><h2>${c === 'h' ? 'You said HIGHER' : c === 'l' ? 'You said LOWER' : 'Locked in'}</h2><p class="muted">Waiting for the flip…</p></div>${foot}`; }
  return `<div class="pq">${esc(nxt.label)}: higher or lower than ${esc(cur.show)}?</div><div class="pcpair">${pcMini(cur, true)}${pcMini(nxt, false)}</div>
    <div class="pchl"><button class="btn pch" data-pc="h">⬆ HIGHER</button><button class="btn pcl" data-pc="l">⬇ LOWER</button></div>${foot}`;
}
function taskCapHtml(text) {
  const prev = P.work.taskPrev, busy = P.work.taskBusy;
  return `<div class="pq">📸 ${esc(text)}</div>${prev ? `<div class="taskprev"><img src="${prev}" alt=""></div>` : ''}${P.work.taskErr ? `<p class="center small" style="color:var(--bad);font-weight:800">${esc(P.work.taskErr)}</p>` : ''}
    ${busy ? `<div class="state"><div class="spinner"></div><p class="muted">${esc(busy)}</p></div>` : prev
      ? `<button class="btn btn-primary btn-lg btn-block" data-tsend>Send it ✓</button><label class="btn btn-ghost btn-block mt">↺ Take another<input type="file" accept="image/*" capture="environment" hidden data-tfile></label>`
      : `<label class="btn btn-primary btn-lg btn-block">📸 Take the photo<input type="file" accept="image/*" capture="environment" hidden data-tfile></label><label class="btn btn-ghost btn-block mt">🖼 Choose from my photos<input type="file" accept="image/*" hidden data-tfile></label>`}`;
}
function taskPhoneHtml(s) {
  const g = s.task, me = P.pid;
  app.className = 'app';
  if (g.step === 'snap') return g.got.includes(me) && !P.work.taskPrev ? `<div class="state"><div class="em">✅</div><h2>Photo in!</h2><p class="muted">It's on its way to the Taskmaster. Changed your mind? You can send another until the time's up.</p><label class="btn btn-ghost btn-block mt">↺ Send a different one<input type="file" accept="image/*" capture="environment" hidden data-tfile></label></div>` : taskCapHtml(s.q.text);
  if (g.step === 'show') { const v = g.picks?.[me], m = { 1: '🥇', 2: '🥈', 3: '🥉', w: '💩' }[v]; return `<div class="state"><div class="em">${m || '📸'}</div><h2>${v === 'w' ? 'The worst photo… yours!' : v ? `The Taskmaster put yours ${v === '1' ? 'FIRST' : v === '2' ? 'second' : 'third'}!` : g.got.includes(me) ? 'Not in the top three this time' : 'No photo from you this time'}</h2></div>`; }
  return `<div class="state"><div class="em">⚖️</div><h2>The Taskmaster is judging…</h2><p class="muted">${g.got.length} photo${g.got.length === 1 ? '' : 's'} in. Watch the screen!</p></div>`;
}
/** Taskmaster on camera: the wheel picks who does it; whoever's picked gets the task on their phone too. */
function tmPhoneHtml(s) {
  const g = s.tm, me = P.pid, mine = g.all || g.picks.includes(me), who = g.picks.map((p) => esc(nm(s, p))).join(', ');
  app.className = 'app';
  const tot = g.pts?.[me] || 0, foot = tot ? `<p class="center small muted mt">Taskmaster points so far: ${tot > 0 ? '+' : ''}${tot}</p>` : '';
  if (g.step === 'spin' || g.step === 'ready') {
    if (g.picks.includes(me)) { if (navigator.vibrate) try { navigator.vibrate([100, 50, 100]); } catch {} return `<div class="state"><div class="em">🎯</div><h2>You've been picked!</h2><p class="muted">Get near your camera. The task is coming…</p>${g.picks.length > 1 ? `<p class="small muted">With: ${g.picks.filter((p) => p !== me).map((p) => esc(nm(s, p))).join(', ')}</p>` : ''}</div>${foot}`; }
    return `<div class="state"><div class="em">🎡</div><h2>${g.spinning ? 'The wheel is spinning…' : 'Picked!'}</h2><p class="muted">${g.picks.length ? `So far: <b>${who}</b>` : 'Who will it be?'}</p><p class="small muted">Task ${g.round} of ${g.count}</p></div>${foot}`;
  }
  if (g.step === 'envelope') return mine
    ? `<div class="tmphone"><div class="tmphone-k">✉️ YOUR TASK</div><div class="tmphone-t">${esc(g.task)}</div><div class="tmphone-f">Do it on camera! Your time started when you opened this task.</div></div>${foot}`
    : `<div class="state"><div class="em">📺</div><h2>Watch the screen!</h2><p class="muted"><b>${who}</b> ${g.picks.length === 1 ? 'is' : 'are'} on a task:</p><p style="font-weight:800">${esc(g.task)}</p></div>${foot}`;
  if (g.step === 'judge') return `<div class="state"><div class="em">⚖️</div><h2>The Taskmaster is deciding…</h2><p class="muted">${esc(g.task)}</p></div>${foot}`;
  if (g.step === 'show') { const got = g.got?.[me]; return `<div class="state"><div class="em">${got > 0 ? '🏆' : got < 0 ? '❌' : mine ? '😬' : '📞'}</div><h2>${got === undefined ? 'Results are on the screen' : got > 0 ? `+${got}!` : got < 0 ? `${got}: you didn't even try!` : 'No points this time'}</h2></div>${foot}`; }
  return `<div class="state"><div class="em">📞</div><h2>Taskmaster</h2></div>${foot}`;
}
/** A photo, shrunk to at most 1280 px and under about 1 MB, as a JPEG data URL (the server takes JPEGs only). */
async function partyShrink(file) {
  const url = URL.createObjectURL(file), img = new Image();
  await new Promise((res, rej) => { img.onload = res; img.onerror = () => rej(new Error("That photo couldn't be opened. Try another.")); img.src = url; });
  const k = Math.min(1, 1280 / Math.max(img.naturalWidth || 1, img.naturalHeight || 1)), c = document.createElement('canvas');
  c.width = Math.max(1, Math.round(img.naturalWidth * k)); c.height = Math.max(1, Math.round(img.naturalHeight * k));
  const ctx = c.getContext('2d'); ctx.fillStyle = '#fff'; ctx.fillRect(0, 0, c.width, c.height); ctx.drawImage(img, 0, 0, c.width, c.height); URL.revokeObjectURL(url);
  let qual = 0.8, data = c.toDataURL('image/jpeg', qual);
  while (data.length > 1_500_000 && qual > 0.35) { qual -= 0.15; data = c.toDataURL('image/jpeg', qual); }
  return data;
}
/** Wires the photo picker and the Send button. done() runs once the photo is safely uploaded. */
function taskBind(code, key, done) {
  const redraw = () => { P.viewKey = ''; render(); };
  $$('[data-tfile]').forEach((inp) => inp.onchange = async () => {
    const f = inp.files?.[0]; if (!f) return;
    P.work.taskErr = ''; P.work.taskBusy = 'Getting it ready…'; redraw();
    try { P.work.taskPrev = await partyShrink(f); } catch (e) { P.work.taskErr = e.message; }
    P.work.taskBusy = ''; redraw();
  });
  const sendB = $('[data-tsend]');
  if (sendB) sendB.onclick = async () => {
    P.work.taskBusy = 'Sending it to the Taskmaster…'; P.work.taskErr = ''; redraw();
    try { await LQ.api('task_photo', { code, key, pid: P.pid, image: P.work.taskPrev }, { password: '', timeout: 40000 }); P.work.taskPrev = null; P.work.taskBusy = ''; done(); }
    catch (e) { P.work.taskBusy = ''; P.work.taskErr = 'It didn\'t send: ' + e.message + '. Try again.'; }
    redraw();
  };
}
function partyBindGame(s) {
  const qId = s.q.id;
  $$('[data-pc]').forEach((b) => b.onclick = () => { P.work.pcCall = { k: qId + s.pc.i, c: b.dataset.pc }; send('answer', { pid: P.pid, qId, answer: { call: b.dataset.pc } }); $$('[data-pc]').forEach((x) => x.disabled = true); b.classList.add('on'); if (navigator.vibrate) try { navigator.vibrate(40); } catch {} });
  if (s.task) { if (P.work.taskFor !== qId) { P.work.taskFor = qId; P.work.taskPrev = null; P.work.taskErr = ''; } taskBind(s.task.code, s.task.key, () => send('answer', { pid: P.pid, qId, answer: { photo: true } })); }
}

// ---------------------------------------------------------------- everyone-answers: Who Said That?, About You, a warm-up task
function partyQuestionHtml(q) {
  if (q.type === 'whosaid') {
    if (q.empty) return `<div class="state"><div class="em">🗣️</div><h2>Nothing to play this time</h2><p class="muted">Nobody here answered the warm-up's About You questions.</p></div>`;
    const mine = q.mine ? drawSecret(q.mine) : null;
    if (mine?.mine) return `<div class="wsq">“${esc(q.quote)}”</div><div class="state"><div class="em">🤐</div><h2>That's yours!</h2><p class="muted">Keep a straight face while everyone else guesses…</p></div>`;
    return `<div class="wsq">“${esc(q.quote)}”</div><p class="center small muted" style="margin:0 0 8px">${esc(q.prompt || '')}</p><div class="ans-grid">${q.options.map((o) => `<button class="abtn" data-k="${o.k}" style="background:${COLORS[o.c].hex}"><span class="shape">${esc(o.emoji || COLORS[o.c].shape)}</span>${esc(o.text)}</button>`).join('')}</div><button type="button" class="btn btn-ghost btn-block mt" id="skipQ" style="color:var(--ink-3)">Skip — no idea ⏭</button>`;
  }
  if (q.type === 'about') return `<div class="pq">🙋 ${esc(q.text)}</div><p class="center small muted">Be honest, or at least funny. It might come up on quiz night!</p><form id="textForm" class="state" style="justify-content:flex-start;padding-top:0"><input type="text" id="textIn" maxlength="140" placeholder="Your answer" autocomplete="off" autocorrect="on" autocapitalize="sentences" style="font-size:1.15rem;text-align:center"><button class="btn btn-primary btn-lg btn-block">Send</button></form><button type="button" class="btn btn-ghost btn-block mt" id="skipQ" style="color:var(--ink-3)">Skip ⏭</button>`;
  if (q.type === 'task') return taskCapHtml(q.text) + `<button type="button" class="btn btn-ghost btn-block mt" id="skipQ" style="color:var(--ink-3)">Skip this task ⏭</button>`;
  return '';
}
function partyBindQuestion(q) {
  if (!['whosaid', 'about', 'task'].includes(q.type)) return false;
  if ($('#skipQ')) $('#skipQ').onclick = () => { P.skipped[q.id] = true; submit(q, 'skip'); };
  if (q.type === 'whosaid') $$('.abtn').forEach((b) => b.onclick = () => submit(q, b.dataset.k));
  if (q.type === 'about' && $('#textForm')) { $('#textForm').onsubmit = (e) => { e.preventDefault(); const t = $('#textIn').value.trim(); if (t) submit(q, t); }; setTimeout(() => $('#textIn')?.focus(), 50); }
  if (q.type === 'task' && q.upload) { if (P.work.taskFor !== q.id) { P.work.taskFor = q.id; P.work.taskPrev = null; P.work.taskErr = ''; } taskBind(q.upload.code, q.upload.key, () => submit(q, { photo: true })); }
  return true;
}
/** The result card's extra lines: power cards, Bounty, Who Said That. */
function partyResultLines(r) { return r?.party?.length ? `<div class="partynotes">${r.party.map((x) => `<div>${esc(x)}</div>`).join('')}</div>` : ''; }
