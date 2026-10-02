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
// The camera starts on and the mic starts muted (user's choice, 2 Oct 2026): a phone next to a TV playing the call
// would send the TV's sound back to everyone, since its echo cancelling only knows what the phone itself plays. Each
// has its own on/off button, so a player taps 🎤 to talk.
window.PhoneCam = (() => {
  'use strict';
  const RTC = LQ.SUPABASE_URL + '/functions/v1/gather-rtc';
  const STUN = [{ urls: 'stun:stun.cloudflare.com:3478' }, { urls: ['stun:stun.l.google.com:19302'] }];
  const S = { state: 'off', error: '', room: '', pass: '', name: '', key: '', stream: null, pc: null, sessionId: null, published: [], supa: null, channel: null, micOn: false, camOn: true, retry: 0 };
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
    if (a) out.push({ tr: pc.addTransceiver(a, { direction: 'sendonly' }), name: 'mic' });
    if (v) out.push({ tr: pc.addTransceiver(v, { direction: 'sendonly', sendEncodings: [{ rid: 'h', maxBitrate: 500000 }, { rid: 'q', scaleResolutionDownBy: 2, maxBitrate: 150000 }] }), name: 'cam' });
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
  const presence = () => ({ name: S.name, mic: S.micOn, cam: S.camOn, sessionId: S.state === 'live' ? S.sessionId : null, tracks: S.state === 'live' ? S.published.slice() : [], screen: null, shareKind: 'screen', hand: null, tv: false, tvFull: false, phone: true });
  const track = () => { if (S.channel) S.channel.track(presence()).catch(() => {}); };
  function announce() {
    S.supa = S.supa || LQ.client();
    S.channel = S.supa.channel('call-' + S.room, { config: { presence: { key: S.key } } });
    S.channel.subscribe((status) => { if (status === 'SUBSCRIBED') track(); });
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
      S.stream = await media();
      S.stream.getAudioTracks().forEach((t) => { t.enabled = false; }); // muted until they tap 🎤 (no echo from the TV)
      // If the phone takes the camera back (a call, the app sent to the background), say so and offer to restart.
      S.stream.getVideoTracks().forEach((t) => t.addEventListener('ended', () => { if (S.state === 'live') { stop(); set('error', 'The camera stopped. Tap the camera to start it again.'); } }));
      await publish();
      S.state = 'live'; emit();
      announce();
    } catch (e) { stop(); set('error', e.message); }
  }
  function stop() {
    closePc();
    if (S.stream) S.stream.getTracks().forEach((t) => t.stop());
    S.stream = null;
    if (S.channel) { try { S.channel.untrack(); S.supa.removeChannel(S.channel); } catch {} S.channel = null; }
    set('off');
  }
  function setMic(on) { S.micOn = !!on; if (S.stream) S.stream.getAudioTracks().forEach((t) => { t.enabled = S.micOn; }); track(); emit(); }
  function setCam(on) { S.camOn = !!on; if (S.stream) S.stream.getVideoTracks().forEach((t) => { t.enabled = S.camOn; }); track(); emit(); }
  /** A fresh pass from the host (they are good for 12 hours; the host sends a new one before then). */
  function refreshPass(pass) { if (pass) S.pass = pass; }
  function rename(name) { if (name && name !== S.name) { S.name = String(name).slice(0, 30); track(); } }

  return {
    start, stop, setMic, setCam, refreshPass, rename,
    onChange(fn) { listeners.add(fn); return () => listeners.delete(fn); },
    get state() { return S.state; }, get error() { return S.error; }, get stream() { return S.stream; },
    get micOn() { return S.micOn; }, get camOn() { return S.camOn; },
    supported: () => !!(navigator.mediaDevices?.getUserMedia && window.RTCPeerConnection),
  };
})();
