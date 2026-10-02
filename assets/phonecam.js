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
  const S = { state: 'off', error: '', room: '', pass: '', name: '', key: '', stream: null, pc: null, sessionId: null, published: [], supa: null, channel: null, micOn: false, camOn: true, retry: 0, audioSender: null, videoSender: null, fixFails: 0, micWatch: null, micState: 'live', micFixes: 0, fixing: false };
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
    await waitConnected(pc, 15000);
  }

  // The same presence entry a Gather caller has, so Gather pages and the host's camera corner treat it as one.
  const presence = () => ({ name: S.name, mic: S.micOn, cam: S.camOn, sessionId: S.state === 'live' ? S.sessionId : null, tracks: S.state === 'live' ? S.published.slice() : [], screen: null, shareKind: 'screen', hand: null, tv: false, tvFull: false, phone: true, micState: S.micState, micFixes: S.micFixes });
  const track = () => { if (S.channel) S.channel.track(presence()).catch(() => {}); };
  function announce() {
    S.supa = S.supa || LQ.client();
    S.channel = S.supa.channel('call-' + S.room, { config: { presence: { key: S.key } } });
    S.channel.subscribe((status) => { if (status === 'SUBSCRIBED') track(); });
  }

  // ---- push to talk, and keeping the camera and mic alive ----
  // Push to talk never switches the microphone track off. An iPhone answers a disabled mic by quietly closing it (to
  // clear its orange dot), and asking for it again then ends the camera too. So the mic keeps running and is simply
  // not sent while 🎤 is up: the sender carries no track (replaceTrack(null)), then the mic again while it is held.
  // A phone can still take its camera or mic back for its own reasons (a phone call, another app): the tracks are
  // watched, and after a couple of seconds like that both are asked for afresh together and slotted into the call,
  // with no new connection and no dropping the player.
  const micTrack = () => S.stream?.getAudioTracks()[0] || null;
  const camTrack = () => S.stream?.getVideoTracks()[0] || null;
  const bad = (t) => !t || t.readyState === 'ended' || t.muted;
  function micStateNow() { const t = micTrack(); return !t ? 'none' : t.readyState === 'ended' ? 'ended' : t.muted ? 'muted' : 'live'; }
  async function sendMic() { try { if (S.audioSender) await S.audioSender.replaceTrack(S.micOn ? micTrack() : null); } catch {} }
  async function fixMedia() {
    if (S.fixing || S.state !== 'live') return;
    S.fixing = true;
    try {
      const fresh = await media();
      const a = fresh.getAudioTracks()[0], v = fresh.getVideoTracks()[0];
      const oldA = micTrack(), oldV = camTrack();
      if (a) { S.stream.addTrack(a); watchTrack(a); if (oldA) { S.stream.removeTrack(oldA); try { oldA.stop(); } catch {} } }
      if (v) { v.enabled = S.camOn; S.stream.addTrack(v); watchTrack(v); if (oldV) { S.stream.removeTrack(oldV); try { oldV.stop(); } catch {} } if (S.videoSender) await S.videoSender.replaceTrack(v); }
      await sendMic();
      S.micFixes++; S.micState = micStateNow(); track(); emit();
    } catch (e) { S.fixFails = (S.fixFails || 0) + 1; if (S.fixFails >= 3) { stop(); set('error', 'The phone took the camera back. Tap Try again to start it again.'); } }
    finally { S.fixing = false; }
  }
  function watchTrack(t) { const note = () => { S.micState = micStateNow(); track(); }; t.addEventListener('mute', note); t.addEventListener('unmute', note); t.addEventListener('ended', note); }
  function watchMedia() {
    clearInterval(S.micWatch); let badSince = 0;
    S.micWatch = setInterval(() => {
      if (S.state !== 'live' || S.fixing) return;
      const st = micStateNow(); if (st !== S.micState) { S.micState = st; track(); }
      // the camera only counts while it is meant to be on (a camera switched off by the player is not broken)
      if (!bad(micTrack()) && !(S.camOn && bad(camTrack()))) { badSince = 0; S.fixFails = 0; return; }
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
  async function start({ room, pass, name, pid }) {
    if (S.state === 'joining' || S.state === 'live') return;
    Object.assign(S, { room, pass, name: String(name || 'Player').slice(0, 30), key: 'lqp-' + pid, retry: 0, micOn: false, camOn: true });
    set('joining');
    try {
      // Tell an iPhone this page records and plays at once, so playing a sound never takes the mic away (Safari 16.4+).
      try { if (navigator.audioSession) navigator.audioSession.type = 'play-and-record'; } catch {}
      S.stream = await media();
      S.stream.getTracks().forEach(watchTrack);
      await publish();
      await sendMic(); // nothing goes out until 🎤 is held (no echo from the TV)
      S.state = 'live'; S.micState = micStateNow(); S.fixFails = 0; emit();
      announce(); watchMedia();
    } catch (e) { stop(); set('error', e.message); }
  }
  function stop() {
    clearInterval(S.micWatch); S.micWatch = null; S.audioSender = null; S.videoSender = null;
    closePc();
    if (S.stream) S.stream.getTracks().forEach((t) => t.stop());
    S.stream = null;
    if (S.channel) { try { S.channel.untrack(); S.supa.removeChannel(S.channel); } catch {} S.channel = null; }
    set('off');
  }
  function setMic(on) { S.micOn = !!on; sendMic(); track(); emit(); }
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
