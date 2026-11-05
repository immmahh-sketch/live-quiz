/* Let's Quiz phones: TEAM MODE (November 2026), the phone half of assets/team.js. Loaded after traitors-phone.js, before play.js.
 * Every player has a team code (TEAM + game code + three characters). A teammate types it where the game code goes, the player lets them
 * in, and that phone is then the same player: same screens, the quickest answer counts, and each phone can be on the quiz call. */

const TM = { tag: '', members: [], pending: [], open: false, asked: false };
const teamCode = () => 'TEAM' + TM.tag;
/** What goes under an answer on the team's other phones: “Sam answered: Paris”. */
function teamSay(q, answer) {
  if (answer === 'skip') return 'skipped: no idea';
  if (q.type === 'choice' || q.type === 'tf') return (q.options || []).find((o) => o.k === answer)?.text || 'an answer';
  if (typeof answer === 'string') return answer;
  if (q.type === 'order' && Array.isArray(answer)) return answer.map((k) => (q.items || []).find((i) => i.k === k)?.text || '').filter(Boolean).join(' → ') || 'an order';
  if (q.type === 'pin') return 'a pin on the picture';
  if (q.type === 'sort') return 'their sort';
  if (q.type === 'match') return 'their matches';
  return 'an answer';
}
const teamMe = () => P.me || P.name;

/** A phone that typed TEAM + 4 characters: it does not know the game yet, so it asks every host on a shared channel; the one with that team code answers with the game code, and the phone goes on to knock at the player's door. */
function teamFind(tag) {
  app.innerHTML = '<div class="state"><span class="spinner"></span><h2>Looking for your team…</h2></div>';
  sb = sb || LQ.client();
  const c = sb.channel('lq-teamfind', { config: { broadcast: { self: false } } }), rid = uid('f'); let done = false, t = null;
  const stop = () => { done = true; clearInterval(t); try { sb.removeChannel(c); } catch {} };
  c.on('broadcast', { event: 'found' }, ({ payload }) => { if (done || payload?.rid !== rid) return; stop(); P.code = String(payload.code || ''); P.partner = true; P.teamTag = tag; connect(); });
  c.subscribe((st) => {
    if (st !== 'SUBSCRIBED' || t) return;
    const ask = () => { if (!done) c.send({ type: 'broadcast', event: 'find', payload: { tag, rid } }); };
    ask(); t = setInterval(ask, 1500);
    setTimeout(() => { if (!done) { stop(); P.partner = false; renderJoin('No team has that code. Check it, and that the game is open on the big screen.'); } }, 9000);
  });
}
/** From the host: the code, the team and anyone knocking (to this player's id, so every phone of the team hears it). */
function teamOnMsg(m) {
  if (!m || m.to !== P.pid) return;
  if (m.kind === 'team') {
    const had = TM.pending.length;
    TM.tag = m.tag || TM.tag; TM.members = m.members || []; TM.pending = m.pending || [];
    teamBtnSync(); if (TM.open) teamModal();
    if (TM.pending.length > had && !P.member) { teamModal(true); if (navigator.vibrate) try { navigator.vibrate([100, 60, 100]); } catch {} }
  }
}
/** Ask the host for this player's code, once the phone is in a game. */
function teamAsk() { if (P.joined && ch) send('team', { op: 'code', pid: P.pid }); }
/** The 👥 Team button, when this phone is in a live game (not watching, not a warm-up, not training). */
function teamBtnSync() {
  const s = P.state, want = !!s && P.joined && !P.view && !BHB && !s.roster && !s.preview && !P.partner;
  let b = document.getElementById('teamBtn');
  if (!want) { b?.remove(); return; }
  if (!TM.asked) { TM.asked = true; teamAsk(); }
  if (!b) { b = document.createElement('button'); b.id = 'teamBtn'; b.type = 'button'; b.className = 'teambtn'; b.onclick = () => teamModal(true); document.body.appendChild(b); }
  const n = TM.pending.length, label = P.member ? '👥 My team' : `👥 Team${TM.members.length ? ' · ' + (TM.members.length + 1) : ''}`;
  if (b.dataset.l !== label + n) { b.dataset.l = label + n; b.innerHTML = label + (n ? `<i class="teamdot">${n}</i>` : ''); }
}
/** The team sheet: the code to give out, who is on the team, who is knocking. */
function teamModal(show) {
  if (show) TM.open = true; if (!TM.open) return;
  let el = document.getElementById('teamModal');
  if (!el) { el = document.createElement('div'); el.id = 'teamModal'; el.className = 'team-modal'; document.body.appendChild(el); }
  const owner = P.name, mem = TM.members, pend = TM.pending;
  el.innerHTML = `<div class="team-in"><button type="button" class="team-x" data-tx aria-label="Close">✕</button>
    ${P.member ? `<h2>👥 You're on ${esc(owner)}'s team</h2><p>You see the same screens and can answer. The quickest answer in the team is the one that counts, and everyone on the team is told who answered.</p><button class="btn btn-block" data-tleave>Leave the team</button>`
      : `<h2>👥 Play as a team</h2><p>Give this code to the people on your team. They type it on their own phone, where the game code goes, with their own name.</p>
      <div class="team-code">${esc(TM.tag ? teamCode() : '…')}</div>
      <p class="small muted">Everyone on the team sees the same screens and can answer. The <b>quickest answer</b> is the one that counts for the team, and the rest are told who answered what. In King of the Hill only you play.</p>
      ${pend.length ? `<div class="team-pend"><b>Waiting to join</b>${pend.map((p) => `<div class="team-row"><span>${esc(p.name)}</span><span><button class="btn btn-primary" data-tyes="${esc(p.dev)}">Let in</button> <button class="btn btn-ghost" data-tno="${esc(p.dev)}">No</button></span></div>`).join('')}</div>` : ''}
      ${mem.length ? `<div class="team-mem"><b>On your team</b>${mem.map((p) => `<div class="team-row"><span>👤 ${esc(p.name)}</span></div>`).join('')}</div>` : '<p class="small muted">Nobody else is on your team yet.</p>'}`}
    <button class="btn btn-primary btn-lg btn-block" data-tx>Done</button></div>`;
  el.querySelectorAll('[data-tx]').forEach((b) => b.onclick = () => { TM.open = false; el.remove(); });
  el.querySelectorAll('[data-tyes]').forEach((b) => b.onclick = () => send('team', { op: 'accept', pid: P.pid, dev: DEVID, who: b.dataset.tyes }));
  el.querySelectorAll('[data-tno]').forEach((b) => b.onclick = () => send('team', { op: 'decline', pid: P.pid, dev: DEVID, who: b.dataset.tno }));
  el.querySelector('[data-tleave]')?.addEventListener('click', () => { send('team', { op: 'leave', pid: P.pid, dev: DEVID }); teamForget(); TM.open = false; el.remove(); leave(); P.code = ''; renderJoin(); });
}
/** This phone stops being a teammate (it left, or it joined a game of its own). */
function teamForget() {
  const was = P.member; P.member = false; P.me = ''; P.owner = ''; unstore('lq_member' + SLOT); document.getElementById('teamBtn')?.remove();
  if (was) { P.pid = uid('p'); P.name = ''; unstore('lq_player' + SLOT); } // a phone that was on a team is nobody's player now: a new id of its own
}
/** A phone that was a teammate and reloads: it is still one. */
function teamRestore() { const m = store('lq_member' + SLOT); if (m && m.pid === P.pid) { P.member = true; P.me = m.me || ''; P.owner = m.owner || ''; } }
