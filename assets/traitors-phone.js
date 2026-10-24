/* Let's Quiz phones: THE TRAITORS (October 2026), the phone half of assets/traitors.js.
 *  - Everyone: the rules open when you join, a 📖 button, your 🛡 shield, the host's Traitors screens (a notice, the Round Table vote, the verdict), pings.
 *  - The Traitor: the secret "you are the Traitor" screen, and a 🗡 menu (steal, gift / block / double, messages, and at half time the honest 20 Questions list).
 * Everything private for one phone arrives as a 'trs' message addressed to this pid and is acted on only here. Loaded after party-phone.js. */

const TRP = { traitor: false, sync: null, tab: 'steal', st: { amount: 300 }, msgs: [], screenId: '', vote: '', tableEnd: 0, listDraft: null, listPrompted: false, msgTo: '', tick: null };
const trpKey = () => 'lq_tr_' + (P.code || '');
const trpSeen = (k) => { try { return localStorage.getItem(trpKey() + k) === '1'; } catch { return false; } };
const trpMark = (k) => { try { localStorage.setItem(trpKey() + k, '1'); } catch {} };

/** Honest questions about the Traitor: the Traitor ticks the ones that are true of them; the room asks them in the last round. */
const TRP_QUESTIONS = [
  ['About them', ['Is the Traitor a man?', 'Is the Traitor a woman?', 'Is the Traitor under 30?', 'Is the Traitor over 50?', 'Is the Traitor married or living with a partner?', 'Does the Traitor have children?', 'Does the Traitor have grandchildren?', 'Is the Traitor left-handed?', 'Does the Traitor wear glasses?', 'Does the Traitor have a beard or moustache?', 'Does the Traitor have dark hair?', 'Does the Traitor have grey or white hair?', 'Does the Traitor have a tattoo?', 'Is the Traitor taller than 5ft 9in (175cm)?']],
  ['Right now', ['Is the Traitor wearing something blue?', 'Is the Traitor wearing something black?', 'Is the Traitor wearing something red?', 'Is the Traitor wearing a watch?', 'Is the Traitor wearing a necklace, ring or earrings?', 'Is the Traitor sitting down?', 'Is the Traitor having a drink right now?', 'Is the Traitor in a different room from the rest of their household?']],
  ['Where they live', ['Does the Traitor live in Newcastle?', 'Does the Traitor live in Sunderland?', 'Does the Traitor live in County Durham?', 'Was the Traitor born in the North East?', 'Does the Traitor live in a flat?', 'Does the Traitor live on their own?', 'Does the Traitor have a garden?', 'Does the Traitor live outside the UK?']],
  ['Pets, wheels and work', ['Does the Traitor have a dog?', 'Does the Traitor have a cat?', 'Does the Traitor have any pet at all?', 'Does the Traitor drive?', 'Does the Traitor own a bike?', 'Does the Traitor work from home?', 'Is the Traitor retired?', 'Does the Traitor work in hospitality?', 'Does the Traitor work in an office?', 'Is the Traitor a student?']],
  ['Likes and habits', ['Does the Traitor support Newcastle United?', 'Does the Traitor support Sunderland?', 'Does the Traitor like football?', 'Does the Traitor play a sport every week?', 'Does the Traitor go to the gym?', 'Does the Traitor drink tea more than coffee?', 'Does the Traitor drink alcohol?', 'Does the Traitor prefer wine to beer?', 'Is the Traitor vegetarian?', 'Does the Traitor like spicy food?', 'Does the Traitor like pineapple on pizza?', 'Does the Traitor like Marmite?', 'Does the Traitor play a musical instrument?', 'Does the Traitor play video games?', 'Does the Traitor watch the soaps?', 'Has the Traitor watched The Traitors on TV?', 'Is the Traitor a morning person?', 'Does the Traitor go to bed after midnight?']],
  ['Life so far', ['Has the Traitor been abroad this year?', 'Has the Traitor been on a cruise?', 'Can the Traitor speak another language?', 'Has the Traitor met a celebrity?', 'Has the Traitor been on TV?', 'Has the Traitor broken a bone?', 'Has the Traitor run a marathon?', 'Has the Traitor been to a festival?', 'Is the Traitor afraid of spiders?', 'Is the Traitor afraid of heights?', 'Can the Traitor swim?', 'Has the Traitor ever been in a pub quiz team that won?']],
];
const trpSitsOut = (s) => TRP.traitor && !!s.q?.trTwenty;
const trpMe = (s) => (s.tr?.players || []).find((p) => p.pid === P.pid);
const trpName = (s, pid) => (s.tr?.players || []).find((p) => p.pid === pid)?.name || 'someone';

// ---------------------------------------------------------------- private messages for this phone
function trpOnPrivate(m) {
  if (!m || m.to !== P.pid) return;
  if (m.kind === 'role') { TRP.traitor = true; const k = 'role' + (m.n ?? 0); if (!trpSeen(k)) { trpMark(k); trpRoleScreen(m); } trpRefresh(); }
  else if (m.kind === 'sync') { TRP.sync = m.d; if (!TRP.traitor) TRP.traitor = true; trpRefresh(); if (m.d.needList && !TRP.listPrompted) { TRP.listPrompted = true; TRP.tab = 'list'; trpMenu(); if (navigator.vibrate) try { navigator.vibrate([80, 50, 80]); } catch {} } if (!m.d.needList) TRP.listPrompted = false; }
  else if (m.kind === 'ok') toast(m.text || 'Done');
  else if (m.kind === 'no') toast(m.why || "That didn't work", true);
  else if (m.kind === 'ping') partyFlash({ icon: m.icon || '🗡', text: m.text });
  else if (m.kind === 'msg') { TRP.msgs.push(String(m.text || '')); trpMsgShow(); }
  else if (m.kind === 'banished') { TRP.traitor = false; TRP.sync = null; document.getElementById('trpMenu')?.remove(); trpFull('banished', `<div class="trp-big">🗡 BANISHED</div><p>${esc(m.text || 'You have been banished.')}</p><p class="trp-small">Keep quiet: the new Traitor is chosen in secret.</p><button class="btn btn-lg btn-block" data-trpx>OK</button>`); trpRefresh(); }
}
function trpFull(id, html) {
  document.getElementById('trpFull')?.remove();
  const el = document.createElement('div'); el.id = 'trpFull'; el.className = 'trp-full ' + id; el.innerHTML = `<div class="trp-in">${html}</div>`; document.body.appendChild(el);
  el.querySelector('[data-trpx]')?.addEventListener('click', () => el.remove());
  return el;
}
function trpRoleScreen(m) {
  const first = m.reason !== 'new';
  trpFull('role', `<div class="trp-dag">🗡</div><div class="trp-big">YOU ARE THE TRAITOR</div>
    <p>${first ? 'You were chosen in secret. Nobody else knows.' : 'The room banished the last Traitor. You have been chosen in secret to take over.'}</p>
    <ul class="trp-ul"><li><b>Steal</b> 100 to 1,000 points from a player (once every 5 questions, the same player only once every 15) and give them to someone else, never yourself.</li>
    <li><b>5 free answers</b> to gift, <b>5 blocks</b> to knock someone out of a question, <b>5 doubles</b>: use them on anyone, yourself included.</li>
    <li><b>Messages</b> to one person in secret, or to the whole room.</li>
    <li>Players earn a 🛡 with 3 right in a row: it keeps you off them for the next question.</li>
    <li>Your 🗡 button is always on your screen. Don't show anyone!</li></ul>
    <p class="trp-small">Be sneaky, but honest when you fill in your 20 Questions list at half time.</p><button class="btn btn-primary btn-lg btn-block" data-trpx>I understand ✓</button>`);
}
/** Secret messages wait for the break between questions. */
function trpMsgShow() {
  const s = P.state; if (!TRP.msgs.length || !s || s.phase === 'question' || s.phase === 'grading' || document.getElementById('trpFull')) return;
  const t = TRP.msgs.shift();
  const el = trpFull('msg', `<div class="trp-dag">🤫</div><div class="trp-big small">A SECRET MESSAGE</div><div class="trp-quote">“${esc(t)}”</div><p class="trp-small">From the Traitor. Or is it? 👀</p><button class="btn btn-primary btn-lg btn-block" data-trpx>OK</button>`);
  el.querySelector('[data-trpx]').addEventListener('click', () => setTimeout(trpMsgShow, 200));
  if (navigator.vibrate) try { navigator.vibrate([100, 60, 100]); } catch {}
}

// ---------------------------------------------------------------- every state
function trPhoneAfter(s) {
  const tr = s.tr;
  if (!tr || P.view || !tr.on) { for (const id of ['trpRules', 'trpBtn', 'trpShield', 'trpScreen', 'trpMenu']) document.getElementById(id)?.remove(); return; }
  if (!trpSeen('guide')) { trpMark('guide'); trpGuide(); }
  trpPills(s);
  trpScreen(s);
  trpMsgShow();
  const mk = JSON.stringify([tr.window, tr.players.map((p) => p.score + (p.shield ? 's' : ''))]); if (mk !== TRP.menuKey) { TRP.menuKey = mk; if (document.getElementById('trpMenu')) trpMenu(true); }
  if (TRP.traitor && s.phase === 'final') document.getElementById('trpBtn')?.remove();
  if (TRP.traitor && !TRP.sync && !TRP.syncAsked) { TRP.syncAsked = true; send('tr', { pid: P.pid, op: 'sync' }); }
}
function trpRefresh() { if (P.state) trpPills(P.state); const m = document.getElementById('trpMenu'); if (m) trpMenu(true); }
function trpPills(s) {
  const tr = s.tr, me = trpMe(s);
  let r = document.getElementById('trpRules');
  if (!r) { r = document.createElement('button'); r.id = 'trpRules'; r.className = 'trp-pill rules'; r.textContent = '📖 Rules'; r.onclick = trpGuide; document.body.appendChild(r); }
  let sh = document.getElementById('trpShield');
  if (me?.shield) { if (!sh) { sh = document.createElement('div'); sh.id = 'trpShield'; sh.className = 'trp-pill shield'; document.body.appendChild(sh); } sh.textContent = '🛡 Shield on'; }
  else sh?.remove();
  let b = document.getElementById('trpBtn');
  if (TRP.traitor && s.phase !== 'final') {
    if (!b) { b = document.createElement('button'); b.id = 'trpBtn'; b.className = 'trp-btn'; b.onclick = () => trpMenu(); document.body.appendChild(b); }
    const can = tr.window && TRP.sync?.canSteal;
    b.classList.toggle('live', !!(tr.window)); b.innerHTML = `🗡<small>${TRP.sync?.needList ? 'Your list' : tr.window ? (can ? 'Steal now' : 'Powers') : 'After this one'}</small>`;
  } else b?.remove();
}

// ---------------------------------------------------------------- the host's Traitors screens (notice, Round Table, verdict, reveal)
function trpScreen(s) {
  const sc = s.tr.screen; let el = document.getElementById('trpScreen');
  if (!sc) { el?.remove(); TRP.screenId = ''; clearInterval(TRP.tick); return; }
  const key = sc.id + '|' + (sc.kind === 'table' ? (sc.voted || []).includes(P.pid) + '|' + TRP.vote + '|' + sc.locked : '');
  if (el && el.dataset.key === key) return;
  if (sc.id !== TRP.screenId) { TRP.screenId = sc.id; TRP.vote = ''; if (sc.kind === 'table') TRP.tableEnd = Date.now() + (sc.left || 0); if (navigator.vibrate) try { navigator.vibrate([120, 60, 120]); } catch {} }
  if (!el) { el = document.createElement('div'); el.id = 'trpScreen'; el.className = 'trp-full screen'; document.body.appendChild(el); }
  el.dataset.key = key;
  let h = '';
  if (sc.kind === 'notice') h = `<div class="trp-big">${esc(sc.title)}</div>${sc.quote ? `<div class="trp-quote">“${esc(sc.quote)}”</div>` : ''}${(sc.lines || []).map((l) => `<p>${esc(l)}</p>`).join('')}<p class="trp-small">Watch the big screen…</p>`;
  if (sc.kind === 'table') {
    const others = (s.tr.players || []).filter((p) => p.pid !== P.pid);
    h = `<div class="trp-big">🕯 THE ROUND TABLE</div><div class="trp-clock" id="trpClock">3:00</div><p>Talk it over. Who is the Traitor? Vote for who to banish. You can change your mind until the votes are locked.</p>
      <div class="trp-vote">${others.map((p) => `<button class="btn ${TRP.vote === p.pid ? 'btn-primary' : ''}" data-trpv="${p.pid}">${esc(p.emoji || '🙂')} ${esc(p.name)}</button>`).join('')}</div>
      <p class="trp-small">${TRP.vote ? `You voted for ${esc(trpName(s, TRP.vote))}.` : 'You have not voted yet.'} ${(sc.voted || []).length} of ${(s.tr.players || []).length} have voted.</p>`;
    if (sc.locked) h = h.replace(/<div class="trp-vote">[\s\S]*?<\/div>/, '<p><b>Votes are locked!</b></p>');
  }
  if (sc.kind === 'verdict') {
    const top = sc.banished, me = P.pid, voted = sc.rows?.length;
    h = `<div class="trp-big">${sc.tie ? 'NO MAJORITY' : top ? `${esc(trpName(s, top))} IS BANISHED${sc.correct ? '!' : '…'}` : 'NOBODY VOTED'}</div>
      <div class="trp-bars">${(sc.rows || []).map((r) => `<div><span>${esc(trpName(s, r.pid))}</span><i style="width:${Math.max(8, r.n / Math.max(1, sc.rows[0].n) * 100)}%"></i><b>${r.n}</b></div>`).join('')}</div>
      <p>${sc.tie ? 'The votes were split. The Traitor lives on…' : !top ? 'Nobody is banished.' : sc.correct ? `…and they WERE the Traitor! ${(sc.winners || []).includes(me) ? 'You voted right: +2,000!' : ''}` : '…but they were NOT the Traitor. The Traitor is still among you.'}</p>`;
  }
  if (sc.kind === 'final') h = `<div class="trp-small">THE TRAITOR WAS…</div><div class="trp-big">${esc(trpName(s, sc.traitor))}</div>${(sc.lines || []).map((l) => `<p>${esc(l)}</p>`).join('')}`;
  el.innerHTML = `<div class="trp-in">${h}</div>`;
  el.querySelectorAll('[data-trpv]').forEach((b) => b.onclick = () => { TRP.vote = b.dataset.trpv; send('tr', { pid: P.pid, op: 'vote', target: TRP.vote }); toast('Vote cast'); trpScreen({ ...s, tr: { ...s.tr, screen: { ...sc } } }); });
  clearInterval(TRP.tick);
  if (sc.kind === 'table' && !sc.locked) { const c = () => { const e = document.getElementById('trpClock'); if (!e) return; const l = Math.max(0, TRP.tableEnd - Date.now()); e.textContent = `${Math.floor(l / 60000)}:${String(Math.floor(l / 1000) % 60).padStart(2, '0')}`; e.classList.toggle('low', l < 30000); }; c(); TRP.tick = setInterval(c, 500); }
}

// ---------------------------------------------------------------- the rules
function trpGuide() {
  document.getElementById('trpGuide')?.remove();
  const el = document.createElement('div'); el.id = 'trpGuide'; el.className = 'trp-guide';
  el.innerHTML = `<div class="trp-gbar"><b>🗡 The Traitors: how it works</b><span><a class="btn btn-sm" href="assets/Traitors-Guide.pdf" target="_blank" rel="noopener">📄 PDF</a> <button class="btn btn-primary btn-sm" data-g>Close</button></span></div><iframe src="assets/traitors-guide.html" title="How the Traitors works"></iframe>`;
  document.body.appendChild(el); el.querySelector('[data-g]').onclick = () => el.remove();
}

// ---------------------------------------------------------------- the Traitor's menu
function trpMenu(refresh) {
  const s = P.state, old = document.getElementById('trpMenu'); if (!s?.tr) return;
  if (old && !refresh) { old.remove(); return; }
  if (old && old.contains(document.activeElement) && /^(TEXTAREA|INPUT)$/.test(document.activeElement.tagName)) return; // never rebuild under someone's typing
  const d = TRP.sync; const el = old || document.createElement('div'); el.id = 'trpMenu'; el.className = 'pcsheet trp-sheet';
  if (!d) { el.innerHTML = `<div class="pcs-in"><p>Loading…</p></div>`; if (!old) document.body.appendChild(el); send('tr', { pid: P.pid, op: 'sync' }); return; }
  const tabs = [['steal', '💰 Steal'], ['power', '🎁 Powers'], ['msg', '📜 Messages']].concat(d.needList || d.list ? [['list', '📋 My list']] : []);
  if (!tabs.some(([k]) => k === TRP.tab)) TRP.tab = 'steal';
  const win = s.tr.window;
  let body = '';
  if (TRP.tab === 'steal') body = trpSteal(d, win);
  if (TRP.tab === 'power') body = trpPowers(d, win);
  if (TRP.tab === 'msg') body = trpMessages(d);
  if (TRP.tab === 'list') body = trpList(d);
  el.innerHTML = `<div class="pcs-in"><div class="pcs-head"><b>🗡 The Traitor's menu</b><button class="btn btn-ghost btn-sm" data-pcx>Close</button></div>
    <div class="trp-tabs">${tabs.map(([k, l]) => `<button class="${TRP.tab === k ? 'on' : ''}" data-tab="${k}">${l}${k === 'list' && d.needList ? ' ❗' : ''}</button>`).join('')}</div>${body}</div>`;
  if (!old) document.body.appendChild(el);
  el.querySelector('[data-pcx]').onclick = () => el.remove(); el.onclick = (e) => { if (e.target === el) el.remove(); };
  el.querySelectorAll('[data-tab]').forEach((b) => b.onclick = () => { TRP.tab = b.dataset.tab; trpMenu(true); });
  trpBind(el, d);
}
const trpWho = (d, extra = {}) => (d.players || []).filter((p) => !extra.not || !extra.not.includes(p.pid));
function trpSteal(d, win) {
  const st = TRP.st;
  if (!win) return `<p class="muted">Steals happen in the break between questions. Wait for the answer or the scores.</p>`;
  if (!d.canSteal) return `<div class="state" style="padding:16px 0"><div class="em">⏳</div><h3>Not yet</h3><p class="muted">You can steal once every 5 questions: ${d.stealWait} more to go.</p></div>`;
  const now = P.state?.tr?.players || [], vics = trpWho(d).map((p) => ({ ...p, ...(d.victims?.[p.pid] || {}), score: now.find((x) => x.pid === p.pid)?.score ?? d.victims?.[p.pid]?.score ?? 0 }));
  const v = st.victim && d.victims?.[st.victim] ? st.victim : '';
  const ok = (p) => !p.shield && !p.wait && p.score > 0;
  let h = `<p class="small" style="margin:6px 0">1. Pick who to steal from</p><div class="pcs-who">${vics.map((p) => `<button class="btn ${v === p.pid ? 'btn-primary' : ''}" data-sv="${p.pid}" ${ok(p) ? '' : 'disabled'}>${esc(p.emoji || '🙂')} ${esc(p.name)}<small class="muted">${p.shield ? '🛡 shield' : p.wait ? `in ${p.wait} q` : p.score > 0 ? p.score : '0'}</small></button>`).join('')}</div>`;
  if (v) {
    h += `<p class="small" style="margin:12px 0 4px">2. How much? <b id="trpAmt">${st.amount}</b></p><input type="range" min="100" max="1000" step="100" value="${st.amount}" id="trpRange" style="width:100%">
      <p class="small" style="margin:12px 0 6px">3. Give it to… (not yourself)</p><div class="pcs-who">${vics.filter((p) => p.pid !== v).map((p) => `<button class="btn ${st.to === p.pid ? 'btn-primary' : ''}" data-st="${p.pid}">${esc(p.emoji || '🙂')} ${esc(p.name)}</button>`).join('')}</div>`;
    if (st.to && st.to !== v) h += `<button class="btn btn-primary btn-lg btn-block mt" data-go>🗡 Steal ${st.amount} from ${esc(vics.find((p) => p.pid === v)?.name || '')}</button>`;
  }
  return h;
}
function trpPowers(d, win) {
  const defs = [['gift', '🎁', 'Free answer', 'full points for them on the next question', d.powers.gift], ['block', '🚫', 'Block', 'they sit the next question out', d.powers.block], ['dbl', '✨', 'Double points', 'their points count twice on the next question', d.powers.dbl]];
  const pick = TRP.st.power;
  let h = `<p class="small muted" style="margin:6px 0">${win ? (d.nextPlain ? 'Choose before the next question starts. The target is pinged when it begins, and the host screen shows it afterwards.' : 'There is no everyone-answers question left to use these on.') : 'Wait for the break between questions.'}</p>`;
  h += `<div class="pcs-cards">${defs.map(([k, ic, nm, how, left]) => { const t = d.set?.[k]; return `<button class="pcs-card ${pick === k ? 'sel' : ''}" data-pw="${k}" ${win && d.nextPlain && left > 0 ? '' : 'disabled'}><span class="pcs-ic">${ic}</span><span><b>${nm} <small style="display:inline">· ${left} left</small></b><small>${how}</small>${t ? `<small style="color:var(--brand);font-weight:800">Set for: ${t === P.pid ? 'you' : esc(trpWho(d).find((p) => p.pid === t)?.name || '')}</small>` : ''}</span></button>`; }).join('')}</div>`;
  if (pick && win) {
    h += `<p class="small" style="margin:12px 0 6px">${defs.find((x) => x[0] === pick)[1]} Who gets it?</p><div class="pcs-who"><button class="btn" data-pt="${P.pid}">🫵 Me</button>${trpWho(d).map((p) => `<button class="btn" data-pt="${p.pid}">${esc(p.emoji || '🙂')} ${esc(p.name)}</button>`).join('')}</div>${d.set?.[pick] ? `<button class="btn btn-ghost btn-block mt" data-pundo>Take it back</button>` : ''}`;
  }
  return h;
}
function trpMessages(d) {
  const to = TRP.msgTo;
  return `<p class="small muted" style="margin:6px 0">${d.msgsLeft} message${d.msgsLeft === 1 ? '' : 's'} left this break. A secret message reaches one phone between questions. A message to everyone goes up on the big screen as “a message from the Traitor”.</p>
    <div class="pcs-who"><button class="btn ${to === 'all' ? 'btn-primary' : ''}" data-mt="all">📜 Everyone</button>${trpWho(d).map((p) => `<button class="btn ${to === p.pid ? 'btn-primary' : ''}" data-mt="${p.pid}">${esc(p.emoji || '🙂')} ${esc(p.name)}</button>`).join('')}</div>
    <textarea id="trpText" rows="3" maxlength="140" placeholder="Write your message (140 characters)…" style="width:100%;margin-top:10px;font:inherit;padding:10px;border-radius:12px;border:2px solid var(--line)"></textarea>
    <button class="btn btn-primary btn-lg btn-block mt" data-msend ${to && d.msgsLeft > 0 ? '' : 'disabled'}>Send ✉</button>`;
}
function trpList(d) {
  if (d.list && !TRP.listDraft) return `<p><b>✅ Your list is saved.</b> ${d.list.filter((x) => x.yes).length} of ${d.list.length} are true of you. It becomes the last round: the room asks these about you to find you.</p><button class="btn btn-block" data-lredo>Change my answers</button>`;
  if (!TRP.listDraft) TRP.listDraft = { yes: new Set((d.list || []).filter((x) => x.yes && !x.own).map((x) => x.text)), own: (d.list || []).filter((x) => x.own).map((x) => ({ text: x.text, yes: x.yes })) };
  const D = TRP.listDraft;
  return `<p class="small" style="margin:6px 0"><b>Be honest!</b> Tick every question that is <b>true of you</b>. In the last round the room asks these to find you out. Untick = the answer is no. You can add your own at the bottom.</p>
    ${TRP_QUESTIONS.map(([h, qs]) => `<div class="trp-lh">${h}</div>${qs.map((t) => `<label class="trp-li"><input type="checkbox" data-lq="${esc(t)}" ${D.yes.has(t) ? 'checked' : ''}> ${esc(t.replace(/^(Is|Does|Has|Can|Was) the Traitor /, (m, v) => v + ' the Traitor '))}</label>`).join('')}`).join('')}
    <div class="trp-lh">Your own</div>${D.own.map((o, i) => `<label class="trp-li"><input type="checkbox" data-lo="${i}" ${o.yes ? 'checked' : ''}> ${esc(o.text)} <small>(tick = yes)</small></label>`).join('')}
    <div class="row" style="gap:6px;margin-top:6px"><input id="trpOwn" maxlength="90" placeholder="Your own yes/no question about the Traitor…" style="flex:1;font:inherit;padding:8px;border-radius:10px;border:2px solid var(--line)"><button class="btn btn-sm" data-ladd>Add</button></div>
    <button class="btn btn-primary btn-lg btn-block mt" data-lsave>Save my list (${D.yes.size + D.own.filter((o) => o.yes).length} ticked)</button>`;
}
function trpBind(el, d) {
  const st = TRP.st, re = () => trpMenu(true);
  el.querySelectorAll('[data-sv]').forEach((b) => b.onclick = () => { st.victim = b.dataset.sv; if (st.to === st.victim) st.to = ''; re(); });
  el.querySelectorAll('[data-st]').forEach((b) => b.onclick = () => { st.to = b.dataset.st; re(); });
  const range = el.querySelector('#trpRange'); if (range) range.oninput = () => { st.amount = +range.value; el.querySelector('#trpAmt').textContent = st.amount; const g = el.querySelector('[data-go]'); if (g) g.textContent = g.textContent.replace(/Steal \d+/, 'Steal ' + st.amount); };
  el.querySelector('[data-go]')?.addEventListener('click', () => { send('tr', { pid: P.pid, op: 'steal', victim: st.victim, amount: st.amount, to: st.to }); st.victim = ''; st.to = ''; el.remove(); });
  el.querySelectorAll('[data-pw]').forEach((b) => b.onclick = () => { st.power = b.dataset.pw; re(); });
  el.querySelectorAll('[data-pt]').forEach((b) => b.onclick = () => { send('tr', { pid: P.pid, op: 'power', kind: st.power, target: b.dataset.pt }); st.power = ''; });
  el.querySelector('[data-pundo]')?.addEventListener('click', () => { send('tr', { pid: P.pid, op: 'power', kind: st.power, target: null }); st.power = ''; });
  el.querySelectorAll('[data-mt]').forEach((b) => b.onclick = () => { const t = el.querySelector('#trpText')?.value || ''; TRP.msgTo = b.dataset.mt; re(); const x = el.querySelector('#trpText'); if (x) x.value = t; });
  el.querySelector('[data-msend]')?.addEventListener('click', () => { const x = el.querySelector('#trpText'); send('tr', { pid: P.pid, op: 'msg', to: TRP.msgTo, text: x.value }); x.value = ''; });
  const D = TRP.listDraft;
  el.querySelector('[data-lredo]')?.addEventListener('click', () => { TRP.listDraft = { yes: new Set((d.list || []).filter((x) => x.yes && !x.own).map((x) => x.text)), own: (d.list || []).filter((x) => x.own).map((x) => ({ text: x.text, yes: x.yes })) }; re(); });
  el.querySelectorAll('[data-lq]').forEach((c) => c.onchange = () => { c.checked ? D.yes.add(c.dataset.lq) : D.yes.delete(c.dataset.lq); const b = el.querySelector('[data-lsave]'); if (b) b.textContent = `Save my list (${D.yes.size + D.own.filter((o) => o.yes).length} ticked)`; });
  el.querySelectorAll('[data-lo]').forEach((c) => c.onchange = () => { D.own[+c.dataset.lo].yes = c.checked; });
  el.querySelector('[data-ladd]')?.addEventListener('click', () => { const x = el.querySelector('#trpOwn'), t = x.value.trim(); if (t.length < 8) return toast('Write a proper question first.', true); D.own.push({ text: t.endsWith('?') ? t : t + '?', yes: true }); re(); });
  el.querySelector('[data-lsave]')?.addEventListener('click', () => {
    const items = TRP_QUESTIONS.flatMap(([, qs]) => qs).map((t) => ({ text: t, yes: D.yes.has(t) })).concat(D.own.map((o) => ({ text: o.text, yes: o.yes, own: true })));
    if (items.filter((x) => x.yes).length < 3) return toast('Tick at least 3 that are true of you.', true);
    send('tr', { pid: P.pid, op: 'list', items }); TRP.listDraft = null;
  });
}
