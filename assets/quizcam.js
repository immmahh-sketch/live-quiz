// Let's Quiz: the camera in the corner of the host screen.
//
// While the quiz screen is on the quiz call (assets/quizcall.js), this pulls
// everyone's camera and microphone from the call (Cloudflare's SFU, the same
// way a Gather page does) and shows whoever is talking in a tile at the top
// right. The quizmaster first: their Gather window says quizHost in presence.
// When nobody is talking the tile fades away; it comes back when someone does.
//
// Sound is only measured, never played. This tab's sound is what goes into the
// call, so playing people's voices here would send them straight back as an echo.
//
// The corner is kept clear for as long as the camera is on (body.camlayer, see
// style.css): the top bar grows to the tile's height and everything in it moves
// left. It does not come and go with the tile, or the game would jump about
// every time someone spoke.
//
// ?camdebug=1 shows everyone's level and the speech threshold.
window.QuizCam = (() => {
  'use strict';
  const DEBUG = new URLSearchParams(location.search).get('camdebug') === '1';

  // ---------- who is talking: the numbers ----------
  const TICK = 100;            // ms between level readings
  const MIN_DB = -50;          // never speech below this (dBFS)
  const OVER_FLOOR = 12;       // dB above a person's own background noise
  const FLOOR_FRAMES = 80;     // background = quietest reading of the last 8 s
  const START = [3, 4];        // speech starts after 3 of the last 4 readings
  const HANG = 1200;           // still talking through pauses this long
  const HOST_TAKE = 400;       // the host takes the tile after this much talking
  const HOST_HOLD = 1500;      // and keeps it until quiet this long
  const MIN_SHOW = 2500;       // each person stays up at least this long
  const LOUDER_DB = 6;         // a player takes over a talking player only this much louder…
  const LOUDER_FOR = 1500;     // …for this long
  const FADE_AFTER = 4000;     // tile fades after everyone has been quiet this long
  const NOISY_DB = 10;         // host threshold raised while the quiz plays music

  const S = {
    on: false, enabled: true, people: new Map(), featured: null, featuredSince: 0, lastSpeech: 0, visible: false, louder: null,
    pc: null, sessionId: null, pulls: new Map(), byMid: new Map(), idle: 0, queue: Promise.resolve(),
    failures: 0, retryTimer: null, retryCount: 0, coolOff: new Map(), coolTimer: null, pullTimer: null,
    actx: null, tick: null, ridTimer: null, unsub: null, ice: null
  };
  let opts = { noisy: () => false };
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

  // ---------- the tile ----------
  let tile = null, layers = [], front = 0, label = null, dbg = null;
  function buildTile() {
    if (tile) return;
    tile = document.createElement('div');
    tile.className = 'camtile';
    tile.setAttribute('aria-hidden', 'true');
    tile.innerHTML = '<div class="camlayer-v"><video muted autoplay playsinline></video><div class="camcard"><b></b></div></div><div class="camlayer-v"><video muted autoplay playsinline></video><div class="camcard"><b></b></div></div><div class="camname"></div>';
    layers = [...tile.querySelectorAll('.camlayer-v')].map((el) => ({ el, video: el.querySelector('video'), card: el.querySelector('.camcard'), who: null }));
    label = tile.querySelector('.camname');
    document.body.appendChild(tile);
    if (DEBUG) { dbg = document.createElement('div'); dbg.className = 'camdebug'; document.body.appendChild(dbg); }
  }
  function removeTile() {
    if (tile) { layers.forEach((l) => { l.video.srcObject = null; }); tile.remove(); }
    tile = null; layers = []; label = null;
    if (dbg) { dbg.remove(); dbg = null; }
  }
  const hue = (name) => { let h = 0; for (const ch of String(name)) h = (h * 31 + ch.charCodeAt(0)) >>> 0; return h % 360; };
  const hasVideo = (p) => p && p.cam && p.camStream.getVideoTracks().some((t) => t.readyState === 'live' && !t.muted);

  // Puts person p on the front layer; a new face fades in over the old one.
  function paint() {
    if (!tile) return;
    const p = S.featured ? S.people.get(S.featured) : null;
    const show = !!p && S.visible && S.enabled;
    tile.classList.toggle('show', show);
    if (!p) return;
    const cur = layers[front];
    if (cur.who !== p.id || cur.vid !== hasVideo(p)) {
      const next = cur.who === p.id ? cur : layers[1 - front];
      next.who = p.id; next.vid = hasVideo(p);
      next.card.querySelector('b').textContent = (p.name.trim()[0] || '?').toUpperCase();
      next.card.style.background = `hsl(${hue(p.name)} 55% 40%)`;
      next.el.classList.toggle('novideo', !next.vid);
      if (next.vid) { if (next.video.srcObject !== p.camStream) next.video.srcObject = p.camStream; next.video.play().catch(() => {}); }
      else next.video.srcObject = null;
      if (next !== cur) {
        front = layers.indexOf(next);
        next.el.classList.add('front'); cur.el.classList.remove('front');
      }
    }
    label.textContent = p.name;
    tile.classList.toggle('host', !!p.host);
  }

  // ---------- presence: who is on the call ----------
  function onPresence(entries) {
    const seen = new Set();
    for (const { id, meta } of entries) {
      if (meta.tv === true) continue; // TVs and the quiz screen itself
      seen.add(id);
      let p = S.people.get(id);
      if (!p) { p = { id, camStream: new MediaStream(), micStream: null, meter: null, hist: [], levels: [], floor: -70, db: -100, loud: -100, speaking: false, speakStart: 0, lastSpeech: 0 }; S.people.set(id, p); }
      const session = typeof meta.sessionId === 'string' ? meta.sessionId : null;
      if (p.sessionId && p.sessionId !== session) { p.camStream = new MediaStream(); dropMeter(p); }
      Object.assign(p, {
        name: String(meta.name || 'Guest').slice(0, 30), host: meta.quizHost === true,
        mic: meta.mic !== false, cam: meta.cam !== false, sessionId: session,
        tracks: Array.isArray(meta.tracks) ? meta.tracks.filter((t) => t === 'mic' || t === 'cam') : []
      });
    }
    for (const [id, p] of S.people) if (!seen.has(id)) { dropMeter(p); S.people.delete(id); if (S.featured === id) S.featured = null; }
    syncPulls();
    paint();
  }

  // ---------- Cloudflare: one receive-only session ----------
  function enqueue(fn) { const run = S.queue.then(fn, fn); S.queue = run.catch(() => {}); return run; }
  const api = (...a) => QuizCall.rtc.api(...a);

  function wanted() {
    const out = new Map(), now = Date.now();
    for (const p of S.people.values()) {
      if (!p.sessionId || (S.coolOff.get(p.sessionId) || 0) > now) continue;
      for (const name of p.tracks) out.set(p.sessionId + '/' + name, { key: p.sessionId + '/' + name, personId: p.id, sessionId: p.sessionId, trackName: name, media: name === 'mic' ? 'audio' : 'video' });
    }
    return out;
  }
  // The person on the tile arrives at half size (plenty for a corner at 1080p); everyone else at a quarter.
  const ridFor = (personId) => personId === S.featured ? 'h' : 'q';
  const simulcast = (rid) => ({ simulcast: { preferredRid: rid, priorityOrdering: 'asciibetical', ridNotAvailable: 'asciibetical' } });

  async function ensurePull() {
    if (S.pc) return;
    const pc = new RTCPeerConnection({ iceServers: S.ice || [], bundlePolicy: 'max-bundle' });
    pc.ontrack = (e) => { const pl = S.byMid.get(e.transceiver.mid); if (pl) { pl.track = e.track; attach(pl); } };
    pc.onconnectionstatechange = () => onPcState(pc);
    S.sessionId = (await api('/sessions/new', 'POST')).sessionId;
    S.pc = pc;
  }
  function onPcState(pc) {
    if (pc !== S.pc) return;
    const st = pc.connectionState;
    if (st === 'connected') { clearTimeout(S.pullTimer); S.pullTimer = null; }
    else if (st === 'failed') rebuild(new Error('connection failed'));
    else if (st === 'disconnected' && !S.pullTimer) S.pullTimer = setTimeout(() => { S.pullTimer = null; if (S.pc === pc && pc.connectionState !== 'connected') rebuild(new Error('connection lost')); }, 8000);
  }
  function resetPull() {
    const pc = S.pc;
    if (pc) { pc.ontrack = null; pc.onconnectionstatechange = null; try { pc.close(); } catch {} }
    S.pc = null; S.sessionId = null; S.pulls.clear(); S.byMid.clear(); S.idle = 0;
    clearTimeout(S.pullTimer); S.pullTimer = null;
    for (const p of S.people.values()) { p.camStream = new MediaStream(); dropMeter(p); }
  }
  function rebuild(e, tidy) {
    if (!S.on) return;
    console.warn('quiz camera: rebuilding', e && e.message);
    if (!tidy) S.failures++;
    const delay = Math.min(15000, 500 * Math.pow(2, Math.max(0, S.failures - 1)));
    enqueue(async () => resetPull()).then(() => { paint(); clearTimeout(S.retryTimer); S.retryTimer = setTimeout(syncPulls, delay); });
  }

  function syncPulls() {
    if (!S.on) return;
    enqueue(async () => {
      if (!S.on) return;
      const want = wanted();
      const gone = [...S.pulls.values()].filter((pl) => !want.has(pl.key));
      if (gone.length) await release(gone);
      const missing = [...want.values()].filter((w) => !S.pulls.has(w.key));
      if (!missing.length) return;
      await ensurePull();
      let failed = false, res;
      try {
        res = await api('/sessions/' + S.sessionId + '/tracks/new', 'POST', {
          tracks: missing.map((w) => Object.assign({ location: 'remote', sessionId: w.sessionId, trackName: w.trackName }, w.media === 'video' ? simulcast(ridFor(w.personId)) : {}))
        });
      } catch (e) {
        // A hang usually means someone in the batch has a dead connection: leave them for 15 s.
        if (/too long/.test(e && e.message)) { for (const w of missing) S.coolOff.set(w.sessionId, Date.now() + 15000); clearTimeout(S.coolTimer); S.coolTimer = setTimeout(syncPulls, 16000); }
        throw e;
      }
      (res.tracks || []).forEach((t, i) => {
        const w = missing.find((x) => x.trackName === t.trackName && (!t.sessionId || x.sessionId === t.sessionId)) || missing[i];
        if (!w) return;
        if (t.errorCode || !t.mid) { failed = true; return; } // not sending yet: try again shortly
        const pl = Object.assign({}, w, { mid: t.mid, rid: w.media === 'video' ? ridFor(w.personId) : null, track: null });
        S.pulls.set(w.key, pl); S.byMid.set(t.mid, pl);
      });
      if (res.requiresImmediateRenegotiation && res.sessionDescription) {
        await S.pc.setRemoteDescription(res.sessionDescription);
        const answer = await S.pc.createAnswer();
        await S.pc.setLocalDescription(answer);
        await api('/sessions/' + S.sessionId + '/renegotiate', 'PUT', { sessionDescription: { type: 'answer', sdp: answer.sdp } });
      }
      S.failures = 0;
      clearTimeout(S.retryTimer);
      if (failed) S.retryTimer = setTimeout(syncPulls, Math.min(30000, 2500 * Math.pow(2, S.retryCount++)));
      else S.retryCount = 0;
    }).then(() => { if (S.idle > 30 && S.on) rebuild(new Error('tidying up'), true); }).catch((e) => rebuild(e));
  }

  // Gone tracks: stop Cloudflare sending them and leave the slots idle (closing a
  // slot by renegotiation breaks Chrome; see the Gather notes).
  async function release(list) {
    for (const pl of list) {
      S.pulls.delete(pl.key); S.byMid.delete(pl.mid); S.idle++;
      const p = S.people.get(pl.personId);
      if (p && pl.track) { if (pl.media === 'video') p.camStream.removeTrack(pl.track); else dropMeter(p); }
    }
    if (S.sessionId) await api('/sessions/' + S.sessionId + '/tracks/close', 'PUT', { tracks: list.map((pl) => ({ mid: pl.mid })), force: true }).catch(() => {});
  }

  function attach(pl) {
    const p = S.people.get(pl.personId);
    if (!p || !pl.track) return;
    if (pl.media === 'video') {
      p.camStream.getVideoTracks().forEach((t) => { if (t !== pl.track) p.camStream.removeTrack(t); });
      if (!p.camStream.getTracks().includes(pl.track)) p.camStream.addTrack(pl.track);
      if (!pl.track._lqcam) { pl.track._lqcam = true; pl.track.addEventListener('mute', paint); pl.track.addEventListener('unmute', paint); }
      paint();
    } else meter(p, pl.track);
  }

  // Layers: whoever is on the tile at half size, the rest at a quarter.
  function scheduleRids() { clearTimeout(S.ridTimer); S.ridTimer = setTimeout(updateRids, 300); }
  function updateRids() {
    if (!S.sessionId) return;
    const changes = [...S.pulls.values()].filter((pl) => pl.media === 'video' && pl.rid !== ridFor(pl.personId));
    if (!changes.length) return;
    changes.forEach((pl) => { pl.rid = ridFor(pl.personId); });
    enqueue(() => api('/sessions/' + S.sessionId + '/tracks/update', 'PUT', {
      tracks: changes.map((pl) => Object.assign({ location: 'remote', sessionId: pl.sessionId, trackName: pl.trackName, mid: pl.mid }, simulcast(pl.rid)))
    })).catch((e) => console.warn('quiz camera: layer', e && e.message));
  }

  // ---------- levels ----------
  function audioCtx() {
    try { S.actx = S.actx || new (window.AudioContext || window.webkitAudioContext)(); if (S.actx.state === 'suspended') S.actx.resume().catch(() => {}); } catch {}
    return S.actx;
  }
  function meter(p, track) {
    if (p.meter && p.meter.track === track) return;
    dropMeter(p);
    const ctx = audioCtx();
    if (!ctx) return;
    const stream = new MediaStream([track]);
    // Chrome only lets Web Audio hear a call's sound once it is playing in a media element. Muted: never heard here.
    const el = new Audio(); el.muted = true; el.srcObject = stream; el.play().catch(() => {});
    try {
      const src = ctx.createMediaStreamSource(stream), an = ctx.createAnalyser();
      an.fftSize = 1024; src.connect(an);
      p.meter = { track, el, src, an, buf: new Float32Array(an.fftSize) };
    } catch { el.srcObject = null; }
  }
  function dropMeter(p) {
    if (!p.meter) return;
    try { p.meter.src.disconnect(); } catch {}
    p.meter.el.srcObject = null;
    p.meter = null; p.speaking = false; p.hist = []; p.levels = [];
  }

  function read(p, now, noisy) {
    if (!p.meter || !p.mic) { p.speaking = false; p.db = -100; return; }
    p.meter.an.getFloatTimeDomainData(p.meter.buf);
    let sum = 0; for (const v of p.meter.buf) sum += v * v;
    const db = p.db = 20 * Math.log10(Math.sqrt(sum / p.meter.buf.length) + 1e-9);
    p.levels.push(db); if (p.levels.length > FLOOR_FRAMES) p.levels.shift();
    p.floor = Math.min(-40, Math.max(-90, Math.min(...p.levels)));
    const thr = p.thr = Math.max(MIN_DB, p.floor + OVER_FLOOR) + (p.host && noisy ? NOISY_DB : 0);
    const on = db > thr;
    p.hist.push(on); if (p.hist.length > START[1]) p.hist.shift();
    if (on) p.lastSpeech = now;
    if (!p.speaking && p.hist.filter(Boolean).length >= START[0]) { p.speaking = true; p.speakStart = now; p.loud = db; }
    else if (p.speaking && now - p.lastSpeech > HANG) p.speaking = false;
    if (p.speaking && on) p.loud += (db - p.loud) * 0.065; // about 1.5 s of smoothing
  }

  // ---------- who goes on the tile ----------
  function choose(now) {
    const cur = S.featured ? S.people.get(S.featured) : null;
    const talking = [...S.people.values()].filter((p) => p.speaking);
    if (talking.length) S.lastSpeech = now;
    const host = talking.find((p) => p.host && now - p.speakStart >= HOST_TAKE);
    let next = cur;
    if (host) next = host;
    else if (cur && cur.host && cur.speaking) next = cur;
    else if (cur && cur.host && now - cur.lastSpeech < HOST_HOLD) next = cur;
    else {
      const players = talking.filter((p) => !p.host).sort((a, b) => a.speakStart - b.speakStart); // longest talking first
      if (!cur || !cur.speaking || cur.host) next = players[0] || cur;
      else if (now - S.featuredSince >= MIN_SHOW) {
        // A louder voice only takes over once it has been clearly louder for a while.
        const rival = players.filter((p) => p !== cur).sort((a, b) => b.loud - a.loud)[0];
        if (rival && rival.loud - cur.loud >= LOUDER_DB) { if (S.louder?.id !== rival.id) S.louder = { id: rival.id, since: now }; if (now - S.louder.since >= LOUDER_FOR) next = rival; }
        else S.louder = null;
      }
    }
    // Nobody jumps in within MIN_SHOW of the last change, except the host.
    if (next && next !== cur && cur && cur.speaking && !next.host && now - S.featuredSince < MIN_SHOW) next = cur;
    if (next && next !== cur) { S.featured = next.id; S.featuredSince = now; S.louder = null; scheduleRids(); }
    const vis = !!S.featured && now - S.lastSpeech < FADE_AFTER;
    if (vis !== S.visible || next !== cur) { S.visible = vis; paint(); }
  }

  function tick() {
    const now = Date.now(), noisy = !!opts.noisy();
    for (const p of S.people.values()) read(p, now, noisy);
    choose(now);
    if (dbg) dbg.innerHTML = [...S.people.values()].map((p) => `<div class="${p.speaking ? 'on' : ''}"><b>${p.host ? '★ ' : ''}${LQ.esc(p.name)}</b> <i style="width:${Math.max(0, 100 + p.db)}%"></i><u style="left:${Math.max(0, 100 + (p.thr || -50))}%"></u>${p.meter ? '' : ' no mic'}${hasVideo(p) ? '' : ' · no cam'}</div>`).join('') || '<div>nobody on the call yet</div>';
  }

  // ---------- on / off ----------
  function layout() { document.body.classList.toggle('camlayer', S.on && S.enabled); }
  async function start() {
    if (S.on || !window.QuizCall || !QuizCall.rtc) return;
    S.on = true;
    buildTile(); layout(); audioCtx();
    try { S.ice = await QuizCall.rtc.iceServers(); } catch { S.ice = []; }
    if (!S.on) return;
    S.unsub = QuizCall.onPresence(onPresence);
    S.tick = setInterval(tick, TICK);
    document.addEventListener('pointerdown', audioCtx);
  }
  function stop() {
    if (!S.on) return;
    S.on = false;
    clearInterval(S.tick); clearTimeout(S.retryTimer); clearTimeout(S.coolTimer); clearTimeout(S.ridTimer);
    if (S.unsub) S.unsub(); S.unsub = null;
    document.removeEventListener('pointerdown', audioCtx);
    resetPull();
    S.people.clear(); S.featured = null; S.visible = false; S.coolOff.clear();
    removeTile(); layout();
  }
  function toggle(on = !S.enabled) { S.enabled = on; layout(); paint(); return S.enabled; }

  return {
    start, stop, toggle,
    config(o) { opts = Object.assign(opts, o); },
    get on() { return S.on; }, get enabled() { return S.enabled; },
    get state() { return { featured: S.featured, visible: S.visible, people: [...S.people.values()].map((p) => ({ name: p.name, host: p.host, speaking: p.speaking, db: Math.round(p.db), video: hasVideo(p), mic: !!p.meter })) }; }
  };
})();
