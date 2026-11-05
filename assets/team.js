/* Let's Quiz: TEAM MODE (November 2026), the host half. Loaded after traitors.js, which it borrows trTell, trTeam and the Traitor's own
 * two-phone door from.
 * Every player has a team code of their own: TEAM + the game code + three characters. A teammate types it where the game code goes,
 * knocks, and the player lets them in. From then on that phone is the same player (same id, same score): it sees the same screens and
 * can answer, and the quickest answer is the one taken (onAnswer already keeps only the first answer for a player). Everything a
 * team's phones need from the host arrives as a 'tms' message addressed to the player's id.
 * A Traitor's code works the same way, but goes through the Traitor's own team (assets/traitors.js) so the secret two-phone roles still apply. */

const TEAM_MAX = 5; // other phones beside the player's own
const TEAM_CHARS = 'ABCDEFGHJKMNPQRSTUVWXYZ23456789'; // no 0/O or 1/I
const tmClean = (s, n) => String(s || '').replace(/\s+/g, ' ').trim().slice(0, n);
const tmTell = (to, kind, data = {}) => send('tms', { to, kind, ...data });
const tmIsTraitor = (pid) => typeof trIsTraitor === 'function' && trIsTraitor(pid);

/** This player's team record, made (with a code no one else has) the first time it is wanted. */
function teamOf(pid) {
  G.team = G.team || {};
  if (!G.team[pid]) {
    const used = new Set(Object.values(G.team).map((t) => t.tag));
    let tag = ''; do { tag = Array.from({ length: 3 }, () => TEAM_CHARS[Math.floor(Math.random() * TEAM_CHARS.length)]).join(''); } while (used.has(tag));
    G.team[pid] = { tag, members: [], pending: [] };
    persist();
  }
  return G.team[pid];
}
/** What every phone of this player is told: the code, who is on the team, and who is knocking. */
function teamTell(pid) {
  if (!G.players?.[pid]) return;
  const t = teamOf(pid);
  tmTell(pid, 'team', { tag: t.tag, members: t.members.map((m) => ({ name: m.name, dev: m.dev })), pending: tmIsTraitor(pid) ? [] : t.pending.map((p) => ({ name: p.name, dev: p.dev })) });
}
/** Every team message from a phone ('team' on the channel). The Traitor's own ops fall through to onTeam. */
function teamHandle(m) {
  if (m.op === 'code') { if (typeof m.pid === 'string') teamTell(m.pid); return; }
  if (m.op === 'ask' && m.tag) return teamAsk(m);
  if (m.op === 'accept' && !tmIsTraitor(m.pid) && m.who) return teamAccept(m);
  if (m.op === 'decline' && !tmIsTraitor(m.pid) && m.who) return teamDecline(m);
  if (m.op === 'leave') return teamLeave(m);
  if (typeof onTeam === 'function') onTeam(m);
}
/** A phone typed someone's team code. */
function teamAsk({ tmp, dev, name, tag }) {
  if (typeof tmp !== 'string') return;
  const pid = Object.keys(G.team || {}).find((p) => G.team[p].tag === String(tag).toUpperCase() && G.players[p]);
  if (!pid) return trTell(tmp, 'teamno', { why: 'No team has that code. Check the letters and numbers on your teammate’s phone.' });
  const nm = tmClean(name, 20) || 'A player', dv = tmClean(dev, 24);
  if (tmIsTraitor(pid)) { // the Traitor's own team: the door, the roles and the secret stay as they were
    const t = trTeam(pid);
    if (t.linked) return t.partnerDev === dv ? trTell(tmp, 'teamlinked', { pid, name: G.players[pid].name, emoji: G.players[pid].emoji || '', member: true }) : trTell(tmp, 'teamno', { why: 'That team is full.' });
    if (!t.pending || t.pending.tmp !== tmp) { t.pending = { tmp, dev: dv, name: nm }; if (typeof trLog === 'function') trLog(`👥 ${nm}'s phone is asking to join a Traitor's team`); trSync(); persist(); }
    return trTell(tmp, 'teamwait', {});
  }
  const T = teamOf(pid);
  if (T.members.some((x) => x.dev === dv)) return trTell(tmp, 'teamlinked', { pid, name: G.players[pid].name, emoji: G.players[pid].emoji || '', member: true }); // back again
  if (T.members.length >= TEAM_MAX) return trTell(tmp, 'teamno', { why: 'That team is full.' });
  if (!T.pending.some((p) => p.dev === dv)) { T.pending.push({ tmp, dev: dv, name: nm }); persist(); tmTell(pid, 'knock', { dev: dv, name: nm }); teamTell(pid); }
  else T.pending.find((p) => p.dev === dv).tmp = tmp;
  trTell(tmp, 'teamwait', {});
}
function teamAccept({ pid, who }) {
  const T = G.team?.[pid]; if (!T || !G.players[pid]) return;
  const i = T.pending.findIndex((p) => p.dev === who); if (i < 0) return;
  const [p] = T.pending.splice(i, 1);
  if (!T.members.some((x) => x.dev === p.dev)) T.members.push({ dev: p.dev, name: p.name, at: Date.now() });
  trTell(p.tmp, 'teamlinked', { pid, name: G.players[pid].name, emoji: G.players[pid].emoji || '', member: true });
  persist(); teamTell(pid);
}
function teamDecline({ pid, who }) {
  const T = G.team?.[pid]; if (!T) return;
  const i = T.pending.findIndex((p) => p.dev === who); if (i < 0) return;
  const [p] = T.pending.splice(i, 1);
  trTell(p.tmp, 'teamno', { why: 'Your teammate said no.' });
  persist(); teamTell(pid);
}
function teamLeave({ pid, dev }) {
  const T = G.team?.[pid]; if (!T) return;
  T.members = T.members.filter((x) => x.dev !== dev); persist(); teamTell(pid);
}
/** The fields a phone adds to an answer, cleaned, to pass on to the player's other phones. */
const teamAnswerInfo = ({ by, dev, say }) => ({ by: tmClean(by, 20), dev: tmClean(dev, 24), say: tmClean(say, 90) });
