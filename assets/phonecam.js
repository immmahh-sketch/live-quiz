// Let's Quiz → Gather from a player's phone: puts this phone's camera and microphone on the quiz call, so someone
// watching the game on a TV (Gather on a Fire TV, which has no camera) is still seen and heard. The host screen's
// camera corner (assets/quizcam.js) features whoever is talking, so the TV shows them inside the quiz picture.
//
// It joins the way a Gather caller does (gather assets/call.js): one send-only connection to Cloudflare's SFU through
// the gather-rtc function, tracks named 'mic' and 'cam' (a phone's simulcast layers h and q), and a presence entry on
// the Supabase channel call-<room> naming them. It never plays the call: the TV does that. The pass comes from the host
// screen in the game state (s.call), signed with the host password; gather-rtc accepts it for the call routes only.
//
// Nothing shows on the phone but a slim bar (play.html syncCallBar): the game screen stays as it is. Camera and mic
// The camera starts on and the mic is push to talk (user's rule, 2 Oct 2026): open only while 🎤 is held in play.html's
// bar. A phone next to a TV playing the call would otherwise send the TV's sound back to everyone (they hear themselves,
// late), since its echo cancelling only knows what the phone itself plays.
window.PhoneCam = (() => {
  'use strict';
  const RTC = LQ.SUPABASE_URL + '/functions/v1/gather-rtc';
  const STUN = [{ urls: 'stun:stun.cloudflare.com:3478' }, { urls: ['stun:stun.l.google.com:19302'] }];
  const S = { state: 'off', error: '', room: '', pass: '', name: '', key: '', stream: null, pc: null, sessionId: null, published: [], supa: null, channel: null, micOn: false, camOn: true, retry: 0, audioSender: null, videoSender: null, fixFails: 0, pressedAt: 0, micWatch: null, presT: null, drops: 0, lastStop: null, micState: 'live', micFixes: 0, fixing: false };
  const listeners = new Set();
  const emit = () => listeners.forEach((fn) => { try { fn(S); } catch {} });
  const set = (state, error = '') => { S.state = state; S.error = error; emit(); };

  async function api(path, method = 'GET', body) {
    const ctl = new AbortController(), timer = setTimeout(() => ctl.abort(), 12000);
    let r;
    try {
      r = await fetch(RTC + path, { method, signal: ctl.signal, body: body ? JSON.stringify(body) : undefined, headers: { 'content-type': 'application/json', apikey: LQ.SUPABASE_KEY, Authorization: 'Bearer ' + LQ.SUPABASE_KEY, 'x-gather-key': S.pass } });
    } catch (e) { throw new Error(e.name === 'AbortError' ? 'The call took too long to answer' : 'Could not reach the call'); }
    finally { clearTimeout(timer); }
    let data = null; try { data = await r.json(); } catch {}
    if (r.status === 401) throw new Error('The call pass has run out: wait a moment for a fresh one, then try again');
    if (!r.ok || !data || data.errorCode) throw new Error((data && data.errorDescription) || 'Call error ' + r.status);
    return data;
  }

  async function media() {
    if (!navigator.mediaDevices?.getUserMedia) throw new Error('This browser cannot use the camera here');
    try {
      return await navigator.mediaDevices.getUserMedia({
        audio: { echoCancellation: true, noiseSuppression: true, autoGainControl: true },
        video: { width: { ideal: 640 }, height: { ideal: 480 }, frameRate: { ideal: 24, max: 30 }, facingMode: 'user' },
      });
    } catch (e) {
      throw new Error(e.name === 'NotAllowedError' ? 'The camera was not allowed. Allow camera and microphone for letsquiz.uk in your settings, then try again.' : 'The camera would not start: ' + (e.message || e.name));
    }
  }

  function waitConnected(pc, ms) {
    return new Promise((resolve, reject) => {
      if (pc.connectionState === 'connected') return resolve();
      const t = setTimeout(() => { pc.removeEventListener('connectionstatechange', h); reject(new Error('Timed out joining the call')); }, ms);
      function h() {
        if (pc.connectionState === 'connected') { clearTimeout(t); pc.removeEventListener('connectionstatechange', h); resolve(); }
        else if (pc.connectionState === 'failed') { clearTimeout(t); pc.removeEventListener('connectionstatechange', h); reject(new Error('Could not join the call')); }
      }
      pc.addEventListener('connectionstatechange', h);
    });
  }

  async function publish() {
    let ice = STUN; try { const d = await api('/ice'); ice = STUN.concat(d.iceServers || []); } catch {}
    const pc = new RTCPeerConnection({ iceServers: ice, bundlePolicy: 'max-bundle' });
    S.pc = pc;
    S.sessionId = (await api('/sessions/new', 'POST')).sessionId; // no body: Cloudflare rejects an empty {}
    const out = [];
    const a = S.stream.getAudioTracks()[0], v = S.stream.getVideoTracks()[0];
    if (a) { const tr = pc.addTransceiver(a, { direction: 'sendonly' }); S.audioSender = tr.sender; out.push({ tr, name: 'mic' }); }
    if (v) { const tr = pc.addTransceiver(v, { direction: 'sendonly', sendEncodings: [{ rid: 'h', maxBitrate: 500000 }, { rid: 'q', scaleResolutionDownBy: 2, maxBitrate: 150000 }] }); S.videoSender = tr.sender; out.push({ tr, name: 'cam' }); }
    const offer = await pc.createOffer();
    await pc.setLocalDescription(offer);
    const res = await api('/sessions/' + S.sessionId + '/tracks/new', 'POST', { sessionDescription: { type: 'offer', sdp: offer.sdp }, tracks: out.map((o) => ({ location: 'local', mid: o.tr.mid, trackName: o.name })) });
    await pc.setRemoteDescription(res.sessionDescription);
    const failed = new Set((res.tracks || []).filter((t) => t.errorCode).map((t) => t.trackName));
    S.published = out.map((o) => o.name).filter((n) => !failed.has(n));
    if (!S.published.length) throw new Error('The call would not take the camera');
    pc.onconnectionstatechange = () => { if (pc === S.pc && pc.connectionState === 'failed' && S.state === 'live') reconnect(); };
    // Push to talk holds on every connection, a reconnect's too: nothing goes out until 🎤 is held.
    sendMic();
    await waitConnected(pc, 15000);
  }

  // The same presence entry a Gather caller has, so Gather pages and the host's camera corner treat it as one.
  // mic: always true while on the call. Push to talk is not posted here: re-posting the entry on every press and
  // release got this phone dropped from the call's member list after a few goes (2 Oct 2026). Whether the player is
  // talking shows in the sound itself (silence while 🎤 is up), which is what the camera corner listens to anyway.
  const presence = () => ({ name: S.name, mic: true, cam: S.camOn, sessionId: S.state === 'live' ? S.sessionId : null, tracks: S.state === 'live' ? S.published.slice() : [], screen: null, shareKind: 'screen', hand: null, tv: false, tvFull: false, phone: true, micState: S.micState, micFixes: S.micFixes, drops: S.drops, lastStop: S.lastStop });
  const track = () => { if (S.channel) S.channel.track(presence()).catch(() => {}); };
  // On the call's member list, and kept there: if the link to it drops (a phone's network, the page asleep for a
  // moment) the entry is put back, so the call never loses this phone while its camera is still going.
  function announce() {
    S.supa = S.supa || LQ.client();
    if (S.channel) { try { S.supa.removeChannel(S.channel); } catch {} }
    const ch = S.channel = S.supa.channel('call-' + S.room, { config: { presence: { key: S.key } } });
    ch.subscribe((status) => {
      if (ch !== S.channel) return;
      if (status === 'SUBSCRIBED') track();
      else if ((status === 'CHANNEL_ERROR' || status === 'TIMED_OUT' || status === 'CLOSED') && S.state === 'live') { S.drops++; setTimeout(() => { if (ch === S.channel && S.state === 'live') announce(); }, 2000); }
    });
    clearInterval(S.presT);
    S.presT = setInterval(() => {
      if (S.state !== 'live' || !S.channel) return;
      const listed = !!S.channel.presenceState()[S.key];
      if (S.channel.state !== 'joined') { S.drops++; announce(); } else if (!listed) { S.drops++; track(); }
    }, 8000);
  }
  // Why the call stopped last time, kept on the phone and reported on the next join (a page the phone reloaded
  // leaves 'page closed'), so a drop can be diagnosed from the call.
  const LAST = 'lq_call_last';
  const noteStop = (why) => { try { localStorage.setItem(LAST, JSON.stringify({ why, at: new Date().toISOString() })); } catch {} };
  window.addEventListener('pagehide', () => { if (S.state === 'live') noteStop('page closed'); });

  // ---- push to talk, and keeping the camera and mic alive ----
  // Push to talk switches the mic track on while 🎤 is held and off when it is let go. That is what an iPhone expects:
  // a switched-off mic is closed by the phone (its orange dot goes) and comes back by itself when switched on again.
  // So a muted mic while 🎤 is up is normal and left alone. (Two things that did not work on an iPhone: treating that
  // mute as broken and asking for the mic again, which killed the camera; and leaving the mic on but unsent, which the
  // phone took for unused and shut down every minute or so, dropping the call.)
  // What is healed: the camera dying while it is meant to be on, or the mic still dead 2 s into a press. Both are then
  // asked for afresh together and swapped into the call, with no new connection and no dropping the player.
  const micTrack = () => S.stream?.getAudioTracks()[0] || null;
  const camTrack = () => S.stream?.getVideoTracks()[0] || null;
  const dead = (t) => !t || t.readyState === 'ended' || t.muted;
  function micStateNow() { const t = micTrack(); return !t ? 'none' : t.readyState === 'ended' ? 'ended' : t.muted ? 'muted' : 'live'; }
  function sendMic() { const t = micTrack(); if (t) t.enabled = S.micOn; }
  async function fixMedia() {
    if (S.fixing || S.state !== 'live') return;
    S.fixing = true;
    try {
      const fresh = await media();
      const a = fresh.getAudioTracks()[0], v = fresh.getVideoTracks()[0];
      const oldA = micTrack(), oldV = camTrack();
      if (a) { a.enabled = S.micOn; S.stream.addTrack(a); watchTrack(a); if (S.audioSender) await S.audioSender.replaceTrack(a); if (oldA) { S.stream.removeTrack(oldA); try { oldA.stop(); } catch {} } }
      if (v) { v.enabled = S.camOn; S.stream.addTrack(v); watchTrack(v); if (S.videoSender) await S.videoSender.replaceTrack(v); if (oldV) { S.stream.removeTrack(oldV); try { oldV.stop(); } catch {} } }
      S.micFixes++; S.micState = micStateNow(); track(); emit();
    } catch (e) { S.fixFails = (S.fixFails || 0) + 1; if (S.fixFails >= 3) { stop('camera taken back'); set('error', 'The phone took the camera back. Tap Try again to start it again.'); } }
    finally { S.fixing = false; }
  }
  // noted, not posted: the mic is muted and unmuted by the phone on every release and press (see presence)
  function watchTrack(t) { const note = () => { S.micState = micStateNow(); }; t.addEventListener('mute', note); t.addEventListener('unmute', note); t.addEventListener('ended', note); }
  function watchMedia() {
    clearInterval(S.micWatch); let badSince = 0;
    S.micWatch = setInterval(() => {
      if (S.state !== 'live' || S.fixing) return;
      S.micState = micStateNow();
      const m = micTrack(), c = camTrack();
      const broken = !m || m.readyState === 'ended' || (S.micOn && m.muted && Date.now() - S.pressedAt > 2000) || (S.camOn && dead(c));
      if (!broken) { badSince = 0; S.fixFails = 0; return; }
      if (!badSince) badSince = Date.now(); else if (Date.now() - badSince > 2000) { badSince = Date.now(); fixMedia(); }
    }, 1000);
  }

  function closePc() { if (S.pc) { try { S.pc.close(); } catch {} } S.pc = null; S.sessionId = null; S.published = []; }

  async function reconnect() {
    if (S.retry > 3) return set('error', 'Lost the call. Tap the camera to try again.');
    S.retry++; set('joining'); closePc(); track();
    try { await publish(); S.state = 'live'; S.retry = 0; emit(); track(); }
    catch (e) { setTimeout(() => { if (S.state !== 'off') reconnect(); }, 2000 * S.retry); }
  }

  /** Puts this phone on the call: { room, pass } from the host screen, the player's name and id. */
  async function start({ room, pass, name, pid, client }) {
    if (S.state === 'joining' || S.state === 'live') return;
    let last = null; try { last = JSON.parse(localStorage.getItem(LAST) || 'null'); } catch {}
    // the game's own connection when given (one link to the server rather than two)
    Object.assign(S, { room, pass, name: String(name || 'Player').slice(0, 30), key: 'lqp-' + pid, retry: 0, micOn: false, camOn: true, drops: 0, lastStop: last, supa: client || S.supa });
    set('joining');
    try {
      // Tell an iPhone this page records and plays at once, so playing a sound never takes the mic away (Safari 16.4+).
      try { if (navigator.audioSession) navigator.audioSession.type = 'play-and-record'; } catch {}
      S.stream = await media();
      S.stream.getTracks().forEach(watchTrack);
      await publish(); // (publish leaves the mic unsent until 🎤 is held: no echo from the TV)
      S.state = 'live'; S.micState = micStateNow(); S.fixFails = 0; emit();
      announce(); watchMedia();
    } catch (e) { stop('could not start: ' + e.message); set('error', e.message); }
  }
  function stop(why = 'stopped') {
    if (S.state === 'live' || S.state === 'joining') noteStop(why);
    clearInterval(S.micWatch); S.micWatch = null; clearInterval(S.presT); S.presT = null; S.audioSender = null; S.videoSender = null;
    closePc();
    if (S.stream) S.stream.getTracks().forEach((t) => t.stop());
    S.stream = null;
    const ch = S.channel; S.channel = null;
    if (ch) { try { ch.untrack(); S.supa.removeChannel(ch); } catch {} }
    set('off');
  }
  function setMic(on) { S.micOn = !!on; if (S.micOn) S.pressedAt = Date.now(); sendMic(); emit(); } // no presence post (see presence)
  function setCam(on) { S.camOn = !!on; if (S.stream) S.stream.getVideoTracks().forEach((t) => { t.enabled = S.camOn; }); track(); emit(); }
  /** A fresh pass from the host (they are good for 12 hours; the host sends a new one before then). */
  function refreshPass(pass) { if (pass) S.pass = pass; }
  function rename(name) { if (name && name !== S.name) { S.name = String(name).slice(0, 30); track(); } }

  return {
    start, stop, setMic, setCam, refreshPass, rename,
    onChange(fn) { listeners.add(fn); return () => listeners.delete(fn); },
    get state() { return S.state; }, get error() { return S.error; }, get stream() { return S.stream; },
    get micOn() { return S.micOn; }, get camOn() { return S.camOn; }, get micState() { return S.micState; }, get micFixes() { return S.micFixes; },
    supported: () => !!(navigator.mediaDevices?.getUserMedia && window.RTCPeerConnection),
  };
})();
