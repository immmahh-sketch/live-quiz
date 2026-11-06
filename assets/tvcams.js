// Let's Quiz on the Fire TV: four cameras down the right of the screen, from the people in the room, rotating round
// so that everyone gets seen (the Traitor can be caught at it).
//
// A Fire Stick cannot decode a whole room, and the speaker-following corner tile (assets/quizcam.js) needs more than it
// has, so this pulls only FOUR cameras at a time, at the small layer, with no sound, and swaps one for the next person
// every few seconds. It uses the quiz call the TV is already on (assets/quizcall.js): the same presence and the same
// receive-only connection to Cloudflare's SFU that the corner tile uses.
//
// Swaps are make-before-break: the new camera is pulled first and takes its tile when its picture arrives; only then is
// the old one let go. A closed slot can't be reused, so after a few swaps the whole connection is rebuilt the same way:
// the new one pulls the four on screen and takes over once they are in.
window.TvCams = (() => {
  'use strict';
  const MAX = 4;             // cameras on screen
  const SWAP_EVERY = 4000;   // a tile changes hands this often while there are more people than tiles
  const ARRIVE_MS = 7000;    // a camera that has not shown a picture by now is dropped and left for 20 s
  const COOL_MS = 20000;
  const TIDY_AFTER = 8;      // idle (closed) slots before the connection is rebuilt
  const S = { on: false, enabled: true, people: new Map(), slots: [], link: null, nextLink: null, queue: Promise.resolve(), timer: null, unsub: null, ice: [], since: new Map(), seen: new Map(), cool: new Map(), lastSwap: 0, failures: 0 };
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
  const api = (...a) => QuizCall.rtc.api(...a);
  const enqueue = (fn) => { const run = S.queue.then(fn, fn); S.queue = run.catch(() => {}); return run; };
  const rid = () => ({ simulcast: { preferredRid: 'q', priorityOrdering: 'asciibetical', ridNotAvailable: 'asciibetical' } });
  const hue = (name) => { let h = 0; for (const ch of String(name)) h = (h * 31 + ch.charCodeAt(0)) >>> 0; return h % 360; };

  // ---------- the column ----------
  let col = null;
  function build() {
    if (col) return;
    col = document.createElement('div');
    col.className = 'tvcol'; col.setAttribute('aria-hidden', 'true');
    S.slots = Array.from({ length: MAX }, () => {
      const el = document.createElement('div'); el.className = 'tvcam';
      el.innerHTML = '<div class="tvcard"><b></b></div><video muted playsinline autoplay disablepictureinpicture></video><div class="tvname"></div>';
      col.appendChild(el);
      return { el, video: el.querySelector('video'), card: el.querySelector('.tvcard'), name: el.querySelector('.tvname'), pid: null, next: null, nextAt: 0 };
    });
    S.stat = document.createElement('div'); S.stat.className = 'tvstat'; col.appendChild(S.stat);
    document.body.appendChild(col);
  }
  function unbuild() { col?.remove(); col = null; S.slots = []; document.body.classList.remove('tvcams'); }
  /** Draws a tile: its person (or nobody), a letter card until their picture is in. */
  function paint(s, withVideo) {
    const p = s.pid ? S.people.get(s.pid) : null;
    s.el.classList.toggle('show', !!p && S.enabled);
    if (!p) { s.video.srcObject = null; return; }
    s.name.textContent = p.name;
    s.card.querySelector('b').textContent = (p.name.trim()[0] || '?').toUpperCase();
    s.card.style.background = `hsl(${hue(p.name)} 55% 40%)`;
    s.el.classList.toggle('novideo', !withVideo);
  }
  const layout = () => { document.body.classList.toggle('tvcams', S.enabled && S.slots.some((s) => s.pid)); status(); };
  /** While no picture is up, a small pill says what the cameras are waiting for (so an empty column is never a mystery). */
  function status() {
    if (!S.stat) return;
    const any = S.slots.some((s) => s.pid || s.next), n = S.people.size, c = eligible().length;
    S.stat.style.display = any ? 'none' : '';
    S.stat.textContent = !S.enabled ? '📷 Room cameras off (press C)' : !n ? '📷 Room cameras on · nobody else is on the call yet' : !c ? `📷 Room cameras on · ${n} on the call, nobody has their camera on` : `📷 Room cameras on · connecting to ${c} camera${c === 1 ? '' : 's'}…`;
  }

  // ---------- one receive-only connection to the SFU ----------
  function newLink() { return { pc: null, sessionId: null, pulls: new Map(), byMid: new Map(), idle: 0, dead: false }; }
  async function open(link) {
    if (link.pc) return;
    const pc = new RTCPeerConnection({ iceServers: S.ice || [], bundlePolicy: 'max-bundle' });
    pc.ontrack = (e) => { const pl = link.byMid.get(e.transceiver.mid); if (pl) { pl.track = e.track; arrived(link, pl); } };
    pc.onconnectionstatechange = () => { if (link === S.link && !link.dead && pc.connectionState === 'failed') tidy(true); };
    link.sessionId = (await api('/sessions/new', 'POST')).sessionId;
    link.pc = pc;
  }
  function shut(link) {
    link.dead = true;
    if (link.pc) { link.pc.ontrack = null; link.pc.onconnectionstatechange = null; try { link.pc.close(); } catch {} }
    link.pc = null; link.pulls.clear(); link.byMid.clear();
  }
  async function answerOffer(link, offer) {
    await link.pc.setRemoteDescription(offer);
    const answer = await link.pc.createAnswer();
    await link.pc.setLocalDescription(answer);
    await api('/sessions/' + link.sessionId + '/renegotiate', 'PUT', { sessionDescription: { type: 'answer', sdp: answer.sdp } });
  }
  /** Asks the SFU for these people's cameras on this connection. */
  async function pull(link, pids) {
    const want = pids.map((id) => S.people.get(id)).filter((p) => p && p.sessionId && !link.pulls.has(p.id));
    if (!want.length) return;
    await open(link);
    const res = await api('/sessions/' + link.sessionId + '/tracks/new', 'POST', { tracks: want.map((p) => Object.assign({ location: 'remote', sessionId: p.sessionId, trackName: 'cam' }, rid())) });
    (res.tracks || []).forEach((t, i) => {
      const p = want.find((x) => x.sessionId === t.sessionId) || want[i];
      if (!p) return;
      if (t.errorCode || !t.mid) { S.cool.set(p.id, Date.now() + COOL_MS); failSlot(p.id); return; } // not sending yet
      const pl = { pid: p.id, mid: t.mid, sessionId: p.sessionId, track: null };
      link.pulls.set(p.id, pl); link.byMid.set(t.mid, pl);
    });
    if (res.requiresImmediateRenegotiation && res.sessionDescription) await answerOffer(link, res.sessionDescription);
  }
  async function release(link, pids) {
    const list = pids.map((id) => link.pulls.get(id)).filter(Boolean);
    for (const pl of list) { link.pulls.delete(pl.pid); link.byMid.delete(pl.mid); link.idle++; }
    if (list.length && link.sessionId && !link.dead) await api('/sessions/' + link.sessionId + '/tracks/close', 'PUT', { tracks: list.map((pl) => ({ mid: pl.mid })), force: true }).catch(() => {});
  }

  /** A picture has arrived: it takes its tile (a new person replaces their old one, which is then let go). */
  function arrived(link, pl) {
    if (link !== S.link && link !== S.nextLink) return;
    const s = S.slots.find((x) => x.next === pl.pid) || S.slots.find((x) => x.pid === pl.pid);
    if (!s) return;
    const old = s.next === pl.pid ? s.pid : null;
    if (s.next === pl.pid) { s.pid = pl.pid; s.next = null; S.since.set(pl.pid, Date.now()); }
    S.seen.set(pl.pid, Date.now());
    s.video.srcObject = new MediaStream([pl.track]); s.video.play().catch(() => {});
    paint(s, true); layout();
    if (old && old !== pl.pid && !S.slots.some((x) => x.pid === old || x.next === old)) enqueue(() => release(S.link, [old]));
    // the card goes away once frames are really flowing (a track starts muted)
    const reveal = () => s.el.classList.remove('novideo');
    if (!pl.track.muted) reveal(); else pl.track.addEventListener('unmute', reveal, { once: true });
  }
  function failSlot(pid) { const s = S.slots.find((x) => x.next === pid); if (s) { s.next = null; paint(s, !!s.pid); } }

  // ---------- who is on the call ----------
  function onPresence(entries) {
    const seen = new Set();
    for (const { id, meta } of entries) {
      if (meta.tv === true) continue; // TVs and the quiz screen itself
      seen.add(id);
      const tracks = Array.isArray(meta.tracks) ? meta.tracks : [];
      const p = S.people.get(id) || {};
      S.people.set(id, Object.assign(p, { id, name: String(meta.name || 'Guest').slice(0, 24), sessionId: typeof meta.sessionId === 'string' ? meta.sessionId : null, cam: meta.cam !== false && tracks.includes('cam') }));
    }
    for (const id of [...S.people.keys()]) if (!seen.has(id)) S.people.delete(id);
    status(); step(true);
  }
  const eligible = () => [...S.people.values()].filter((p) => p.sessionId && p.cam && (S.cool.get(p.id) || 0) < Date.now()).map((p) => p.id);

  // ---------- rotating ----------
  /** Fills empty tiles, drops people who have gone, and (every SWAP_EVERY) swaps the longest-shown for whoever has waited longest. */
  function step(soon) {
    if (!S.on || S.nextLink) return;
    enqueue(async () => {
      if (!S.on) return;
      const el = eligible(), now = Date.now();
      // people who have left (or turned their camera off) lose their tile
      for (const s of S.slots) {
        if (s.pid && !el.includes(s.pid)) { const gone = s.pid; s.pid = null; paint(s, false); if (S.link) await release(S.link, [gone]); }
        if (s.next && (!el.includes(s.next) || now - s.nextAt > ARRIVE_MS)) { const bad = s.next; s.next = null; if (now - s.nextAt > ARRIVE_MS) S.cool.set(bad, now + COOL_MS); if (S.link) await release(S.link, [bad]); paint(s, !!s.pid); }
      }
      layout();
      const onScreen = new Set(S.slots.flatMap((s) => [s.pid, s.next]).filter(Boolean));
      const waiting = el.filter((id) => !onScreen.has(id)).sort((a, b) => (S.seen.get(a) || 0) - (S.seen.get(b) || 0));
      const jobs = [];
      for (const s of S.slots) if (!s.pid && !s.next && waiting.length) jobs.push([s, waiting.shift()]); // empty tiles first
      if (!jobs.length && waiting.length && now - S.lastSwap >= SWAP_EVERY && !S.slots.some((s) => s.next)) { // everyone has a tile but others are waiting: rotate
        const s = S.slots.filter((x) => x.pid).sort((a, b) => (S.since.get(a.pid) || 0) - (S.since.get(b.pid) || 0))[0];
        if (s) { jobs.push([s, waiting.shift()]); S.lastSwap = now; }
      }
      if (!jobs.length) return;
      S.link = S.link || newLink();
      for (const [s, pid] of jobs) { s.next = pid; s.nextAt = now; }
      try { await pull(S.link, jobs.map(([, pid]) => pid)); S.failures = 0; }
      catch (e) { console.warn('tv cameras', e && e.message); for (const [s] of jobs) s.next = null; S.failures++; return tidy(true); }
      if (S.link.idle >= TIDY_AFTER) tidy();
    });
  }

  /** A new connection takes over: it pulls the cameras on screen, and the old one is closed once they are in (or after ARRIVE_MS). */
  function tidy(hard) {
    if (!S.on || S.nextLink) return;
    enqueue(async () => {
      if (!S.on || S.nextLink) return;
      const old = S.link, nl = S.nextLink = newLink();
      const pids = S.slots.map((s) => s.pid).filter(Boolean);
      try {
        if (hard) { if (old) shut(old); S.link = nl; }
        await pull(nl, pids);
        if (!hard) await sleep(Math.min(ARRIVE_MS, 3500));
      } catch (e) { console.warn('tv cameras: rebuild', e && e.message); }
      S.link = nl; S.nextLink = null;
      if (old && !old.dead) shut(old);
      if (S.failures) setTimeout(() => step(true), Math.min(15000, 1000 * Math.pow(2, S.failures)));
    });
  }

  // ---------- on / off ----------
  async function start() {
    if (S.on || !window.QuizCall || !QuizCall.rtc) return;
    S.on = true; build();
    try { S.ice = await QuizCall.rtc.iceServers(); } catch { S.ice = []; }
    if (!S.on) return;
    S.unsub = QuizCall.onPresence(onPresence);
    S.timer = setInterval(() => step(), 1000);
  }
  function stop() {
    if (!S.on) return;
    S.on = false; clearInterval(S.timer); if (S.unsub) S.unsub(); S.unsub = null;
    for (const l of [S.link, S.nextLink]) if (l) shut(l);
    S.link = S.nextLink = null; S.people.clear(); S.since.clear(); S.seen.clear(); S.cool.clear();
    unbuild();
  }
  function toggle(on = !S.enabled) { S.enabled = on; for (const s of S.slots) paint(s, !s.el.classList.contains('novideo')); layout(); return S.enabled; }
  return {
    start, stop, toggle,
    get on() { return S.on; }, get enabled() { return S.enabled; },
    /** Names (lower case) of the people on the call whose camera is on: the confession round picks from them. */
    get camNames() { return [...S.people.values()].filter((p) => p.cam && p.sessionId).map((p) => String(p.name).toLowerCase()); },
    /** For testing and diagnosing: who is on each tile, and what is waiting. */
    get state() { return { tiles: S.slots.map((s) => ({ pid: s.pid, name: s.pid ? S.people.get(s.pid)?.name : null, next: s.next, video: !!s.video.srcObject })), eligible: eligible().length, idle: S.link?.idle || 0, failures: S.failures }; }
  };
})();
