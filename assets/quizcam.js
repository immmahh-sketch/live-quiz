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
// Pictures are face-framed (assets/facecam.js): head and shoulders in the tile. Quiz players linked to a camera on
// the call (by name, or by the host in the lobby) also get a round close-up in place of their emoji wherever the
// screen has a spot for it (`<span class="pface" data-pcam="<player id>">`): head-to-heads, podiums, the Race's
// points-lost screen, winners.
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
  const START = [2, 3];        // speech starts after 2 of the last 3 readings (about 0.2 s; was 3 of 4)
  const HANG = 700;            // still talking through pauses this long (was 1.2 s: the next speaker waited)
  const HOST_TAKE = 400;       // the host takes the tile after this much talking
  const HOST_HOLD = 600;       // and keeps it until quiet this long (was 1.5 s: a player answering the host waited)
  const MIN_SHOW = 1500;       // each person stays up at least this long (was 2.5 s)
  const LOUDER_DB = 6;         // a player takes over a talking player only this much louder…
  const LOUDER_FOR = 1500;     // …for this long
  const FADE_AFTER = 4000;     // tile fades after everyone has been quiet this long
  const NOISY_DB = 10;         // host threshold raised while the quiz plays music

  const S = {
    on: false, enabled: true, people: new Map(), featured: null, featuredSince: 0, lastSpeech: 0, visible: false, louder: null,
    pc: null, sessionId: null, pulls: new Map(), byMid: new Map(), idle: 0, queue: Promise.resolve(),
    failures: 0, retryTimer: null, retryCount: 0, coolOff: new Map(), coolTimer: null, pullTimer: null,
    actx: null, tick: null, ridTimer: null, unsub: null, ice: null, onScreen: new Set(), raf: 0, recent: new Map()
  };
  // noisy(): quiz music is playing. playerName(pid) and links() (the host's player → call-name choices) find a quiz
  // player's camera.
  let opts = { noisy: () => false, playerName: () => '', links: () => ({}) };
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

  // ---------- the tile ----------
  let tile = null, layers = [], front = 0, label = null, dbg = null;
  function buildTile() {
    if (tile) return;
    tile = document.createElement('div');
    tile.className = 'camtile';
    tile.setAttribute('aria-hidden', 'true');
    tile.innerHTML = '<div class="camlayer-v"><canvas></canvas><div class="camcard"><b></b></div></div><div class="camlayer-v"><canvas></canvas><div class="camcard"><b></b></div></div><div class="camname"></div>';
    layers = [...tile.querySelectorAll('.camlayer-v')].map((el) => ({ el, canvas: el.querySelector('canvas'), card: el.querySelector('.camcard'), who: null }));
    label = tile.querySelector('.camname');
    document.body.appendChild(tile);
    if (DEBUG) { dbg = document.createElement('div'); dbg.className = 'camdebug'; document.body.appendChild(dbg); }
  }
  function removeTile() {
    if (tile) tile.remove();
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
      if (next !== cur) {
        front = layers.indexOf(next);
        next.el.classList.add('front'); cur.el.classList.remove('front');
      }
    }
    label.textContent = p.name;
    tile.classList.toggle('host', !!p.host);
  }

  // ---------- painting: the tile and the player bubbles, every frame ----------
  const norm = (x) => String(x || '').toLowerCase().normalize('NFKD').replace(/[^a-z0-9]/g, '');
  /** The call person whose camera belongs to quiz player `pid`: the host's choice if made, else the same name
   *  (or one name starting with the other, when only one person fits). */
  function personFor(pid) {
    const pick = (opts.links() || {})[pid];
    if (pick === '-') return null;
    const want = norm(pick || opts.playerName(pid)); if (!want) return null;
    const people = [...S.people.values()];
    const exact = people.find((p) => norm(p.name) === want); if (exact) return exact;
    if (pick) return null;
    const near = people.filter((p) => { const n = norm(p.name); return n && want.length >= 3 && n.length >= 3 && (n.startsWith(want) || want.startsWith(n)); });
    return near.length === 1 ? near[0] : null;
  }
  // Animation frames stop when the window is hidden (say, behind the call window), so a timer takes over then.
  const nextFrame = () => { S.raf = document.hidden ? setTimeout(frame, 66) : requestAnimationFrame(frame); };
  function frame() {
    if (!S.on) return;
    nextFrame();
    if (!window.FaceCam) return;
    FaceCam.tick();
    // the corner tile: head and shoulders
    if (tile && tile.classList.contains('show')) for (const l of layers) if (l.who && l.vid && (l.el.classList.contains('front') || getComputedStyle(l.el).opacity > 0.01)) FaceCam.paint(l.canvas, l.who, 2.7);
    // the round player bubbles: a close-up
    const seen = new Set(); let changed = false;
    for (const el of document.querySelectorAll('[data-pcam]')) {
      const p = S.enabled ? personFor(el.dataset.pcam) : null;
      let ok = false;
      if (p && hasVideo(p)) {
        seen.add(p.id);
        let c = el.querySelector('canvas'); if (!c) { c = document.createElement('canvas'); el.appendChild(c); }
        ok = FaceCam.paint(c, p.id, 1.9);
      }
      if (el.classList.contains('live') !== ok) { el.classList.toggle('live', ok); changed = true; }
    }
    if (changed && typeof window.fitStage === 'function') window.fitStage();
    const now = Date.now(); for (const id of seen) S.recent.set(id, now); if (S.featured && S.visible) S.recent.set(S.featured, now);
    if (seen.size !== S.onScreen.size || [...seen].some((x) => !S.onScreen.has(x))) { S.onScreen = seen; scheduleRids(); }
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
      if (p.sessionId && p.sessionId !== session) { p.camStream = new MediaStream(); dropMeter(p); window.FaceCam?.drop(id); }
      Object.assign(p, {
        name: String(meta.name || 'Guest').slice(0, 30), host: meta.quizHost === true,
        mic: meta.mic !== false, cam: meta.cam !== false, sessionId: session,
        tracks: Array.isArray(meta.tracks) ? meta.tracks.filter((t) => t === 'mic' || t === 'cam') : []
      });
    }
    for (const [id, p] of S.people) if (!seen.has(id)) { dropMeter(p); window.FaceCam?.drop(id); S.people.delete(id); if (S.featured === id) S.featured = null; }
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
  // Every camera at half size (640×360, about 400 kbps each): the round tile and the player bubbles need it, and
  // Cloudflare keeps one layer per camera per connection, so it can't be raised when someone comes on screen.
  const ridFor = () => 'h';
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
    for (const p of S.people.values()) { p.camStream = new MediaStream(); dropMeter(p); window.FaceCam?.drop(p.id); }
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
      if (res.requiresImmediateRenegotiation && res.sessionDescription) await answerOffer(res.sessionDescription);
      S.failures = 0;
      clearTimeout(S.retryTimer);
      if (failed) S.retryTimer = setTimeout(syncPulls, Math.min(30000, 2500 * Math.pow(2, S.retryCount++)));
      else S.retryCount = 0;
    }).then(() => { if (S.idle > 30 && S.on) rebuild(new Error('tidying up'), true); }).catch((e) => rebuild(e));
  }

  async function answerOffer(offer) {
    await S.pc.setRemoteDescription(offer);
    const answer = await S.pc.createAnswer();
    await S.pc.setLocalDescription(answer);
    await api('/sessions/' + S.sessionId + '/renegotiate', 'PUT', { sessionDescription: { type: 'answer', sdp: answer.sdp } });
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
      if (window.FaceCam) FaceCam.setStream(p.id, p.camStream);
      if (!pl.track._lqcam) { pl.track._lqcam = true; pl.track.addEventListener('mute', paint); pl.track.addEventListener('unmute', paint); }
      paint();
    } else meter(p, pl.track);
  }

  // Layers: should a pull ever need another layer than it has (see ridFor), the camera is pulled again at that
  // layer; Cloudflare does not reliably switch in place. The old picture stays up until the new one is in.
  function scheduleRids() { clearTimeout(S.ridTimer); S.ridTimer = setTimeout(updateRids, 300); }
  function updateRids() {
    if (!S.sessionId || !S.pc) return;
    const redo = [...S.pulls.values()].filter((pl) => pl.media === 'video' && pl.track && pl.rid !== ridFor(pl.personId));
    if (!redo.length) return;
    enqueue(async () => {
      if (!S.pc || !S.sessionId) return;
      const res = await api('/sessions/' + S.sessionId + '/tracks/new', 'POST', {
        tracks: redo.map((pl) => Object.assign({ location: 'remote', sessionId: pl.sessionId, trackName: pl.trackName }, simulcast(ridFor(pl.personId))))
      });
      const old = [];
      (res.tracks || []).forEach((t, i) => {
        const pl = redo.find((x) => x.trackName === t.trackName && (!t.sessionId || x.sessionId === t.sessionId)) || redo[i];
        if (!pl || t.errorCode || !t.mid || S.pulls.get(pl.key) !== pl) return;
        const np = Object.assign({}, pl, { mid: t.mid, rid: ridFor(pl.personId), track: null });
        S.pulls.set(pl.key, np); S.byMid.set(t.mid, np); old.push(pl);
      });
      if (res.requiresImmediateRenegotiation && res.sessionDescription) await answerOffer(res.sessionDescription);
      // attach() swaps the new picture in as it arrives; the old slots go a few seconds later
      setTimeout(() => enqueue(async () => {
        for (const pl of old) { S.byMid.delete(pl.mid); S.idle++; }
        if (S.sessionId && old.length) await api('/sessions/' + S.sessionId + '/tracks/close', 'PUT', { tracks: old.map((pl) => ({ mid: pl.mid })), force: true }).catch(() => {});
      }), 4000);
    }).catch((e) => rebuild(e));
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

  let ridCheck = 0;
  function tick() {
    const now = Date.now(), noisy = !!opts.noisy();
    if (++ridCheck % 50 === 0) scheduleRids();
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
    nextFrame();
    document.addEventListener('pointerdown', audioCtx);
  }
  function stop() {
    if (!S.on) return;
    S.on = false;
    clearInterval(S.tick); cancelAnimationFrame(S.raf); clearTimeout(S.raf); clearTimeout(S.retryTimer);
    for (const el of document.querySelectorAll('[data-pcam].live')) el.classList.remove('live'); clearTimeout(S.coolTimer); clearTimeout(S.ridTimer);
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
    /** Everyone on the call, for the host's camera links. */
    /** For diagnosing: the receiving connection. */
    get pc() { return S.pc; },
    /** For diagnosing: each video pull, the layer asked for, and who is on screen. */
    get pulls() { return { onScreen: [...S.onScreen], featured: S.featured, pulls: [...S.pulls.values()].filter((p) => p.media === 'video').map((p) => ({ who: S.people.get(p.personId)?.name, rid: p.rid, want: ridFor(p.personId) })) }; },
    get callNames() { return [...S.people.values()].map((p) => ({ name: p.name, host: !!p.host, video: hasVideo(p) })); },
    linkedName(pid) { return personFor(pid)?.name || ''; },
    get state() { return { featured: S.featured, visible: S.visible, people: [...S.people.values()].map((p) => ({ name: p.name, host: p.host, speaking: p.speaking, db: Math.round(p.db), video: hasVideo(p), mic: !!p.meter })) }; }
  };
})();
