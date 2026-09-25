// Let's Quiz → Gather: puts this quiz screen into the quiz night video call
// (https://gathercall.uk/quiz, room "lets-quiz") without opening Gather.
//
// It joins the call the same way a Gather page does: one sending connection to
// Cloudflare's SFU through the gather-rtc function, and a presence entry on the
// Supabase channel call-lets-quiz naming the published tracks. Gather pages then
// pull the screen onto their stage (full screen on TVs). This page only sends;
// it never pulls anyone's camera or sound.
//
// Capture: a browser shares this tab (preferCurrentTab, so the only choice is
// "Share"); the Windows app answers the request itself with this window and its
// sound, so there is no picker at all; the Fire TV app hands over frames from
// Android's screen capture (window.LetsQuizApp.startCapture).
window.QuizCall = (() => {
  'use strict';
  const RTC = LQ.SUPABASE_URL + '/functions/v1/gather-rtc';
  const ROOM = new URLSearchParams(location.search).get('callroom') || 'lets-quiz'; // ?callroom= for testing
  const NAME = "Let's Quiz";
  const STUN = [{ urls: 'stun:stun.cloudflare.com:3478' }, { urls: ['stun:stun.l.google.com:19302'] }];
  const S = { state: 'off', error: '', people: 0, stream: null, pc: null, sessionId: null, published: [], supa: null, channel: null, subscribed: false, retry: null, keep: null, stopCapture: null };
  const id = 'lq-' + Math.random().toString(36).slice(2, 10);
  const listeners = new Set();
  const emit = () => listeners.forEach((fn) => { try { fn(S); } catch {} });
  const set = (state, error = '') => { S.state = state; S.error = error; emit(); };

  const nativeCapture = () => !!(window.LetsQuizApp && window.LetsQuizApp.startCapture);
  const supported = () => nativeCapture() || !!(navigator.mediaDevices && navigator.mediaDevices.getDisplayMedia);

  async function api(path, method = 'GET', body) {
    const ctl = new AbortController(), timer = setTimeout(() => ctl.abort(), 12000);
    let r;
    try {
      r = await fetch(RTC + path, { method, signal: ctl.signal, body: body ? JSON.stringify(body) : undefined, headers: { 'content-type': 'application/json', apikey: LQ.SUPABASE_KEY, Authorization: 'Bearer ' + LQ.SUPABASE_KEY, 'x-gather-key': LQ.hostPassword() } });
    } catch (e) { throw new Error(e.name === 'AbortError' ? 'The call server took too long to answer' : 'Could not reach the call server'); }
    finally { clearTimeout(timer); }
    let data = null;
    try { data = await r.json(); } catch {}
    if (r.status === 401) throw new Error('The call server did not accept the host password');
    if (!r.ok || !data || data.errorCode) throw new Error((data && data.errorDescription) || 'Call server error ' + r.status);
    return data;
  }

  // ---------- capture ----------
  async function capture() {
    if (nativeCapture()) return FireTvCapture.start();
    const s = await navigator.mediaDevices.getDisplayMedia({
      video: { frameRate: { ideal: 20, max: 30 }, width: { ideal: 1920 }, height: { ideal: 1080 } },
      audio: { echoCancellation: false, noiseSuppression: false, autoGainControl: false, suppressLocalAudioPlayback: false },
      preferCurrentTab: true, selfBrowserSurface: 'include', surfaceSwitching: 'exclude', systemAudio: 'exclude', monitorTypeSurfaces: 'exclude'
    });
    return { stream: s, stop: () => s.getTracks().forEach((t) => t.stop()) };
  }

  // A tab only produces frames when something on it changes, and Cloudflare drops
  // a track that sends nothing for 30 seconds. A dot that never stops changing
  // keeps the picture flowing on a still screen.
  function keepAlive(on) {
    if (on && !S.keep) {
      const d = document.createElement('div');
      d.id = 'callKeepAlive';
      d.style.cssText = 'position:fixed;right:0;bottom:0;width:2px;height:2px;pointer-events:none;z-index:2147483647;animation:callKeep 1s steps(2) infinite';
      const st = document.createElement('style');
      st.textContent = '@keyframes callKeep{0%{background:rgba(0,0,0,.02)}100%{background:rgba(255,255,255,.02)}}';
      d.appendChild(st);
      document.body.appendChild(d);
      S.keep = d;
    } else if (!on && S.keep) { S.keep.remove(); S.keep = null; }
  }

  // ---------- Cloudflare ----------
  async function iceServers() {
    try { const d = await api('/ice'); return STUN.concat(d.iceServers || []); } catch { return STUN; }
  }

  function waitConnected(pc, ms) {
    return new Promise((resolve, reject) => {
      if (pc.connectionState === 'connected') return resolve();
      const t = setTimeout(() => { pc.removeEventListener('connectionstatechange', h); reject(new Error('Timed out connecting to the call')); }, ms);
      function h() {
        if (pc.connectionState === 'connected') { clearTimeout(t); pc.removeEventListener('connectionstatechange', h); resolve(); }
        else if (pc.connectionState === 'failed') { clearTimeout(t); pc.removeEventListener('connectionstatechange', h); reject(new Error('Could not connect to the call')); }
      }
      pc.addEventListener('connectionstatechange', h);
    });
  }

  async function publish() {
    const pc = new RTCPeerConnection({ iceServers: await iceServers(), bundlePolicy: 'max-bundle' });
    S.pc = pc;
    S.sessionId = (await api('/sessions/new', 'POST')).sessionId;
    const screen = 'screen-' + (Date.now() % 1e6) + '-' + id.slice(3, 7);
    const out = S.stream.getTracks().map((t) => {
      if (t.kind === 'video') t.contentHint = 'detail';
      return { tr: pc.addTransceiver(t, Object.assign({ direction: 'sendonly' }, t.kind === 'video' ? { sendEncodings: [{ maxBitrate: 3000000 }] } : {})), name: t.kind === 'video' ? screen : screen + '-audio' };
    });
    const offer = await pc.createOffer();
    await pc.setLocalDescription(offer);
    const res = await api('/sessions/' + S.sessionId + '/tracks/new', 'POST', {
      sessionDescription: { type: 'offer', sdp: offer.sdp },
      tracks: out.map((o) => ({ location: 'local', mid: o.tr.mid, trackName: o.name }))
    });
    await pc.setRemoteDescription(res.sessionDescription);
    const failed = new Set((res.tracks || []).filter((t) => t.errorCode).map((t) => t.trackName));
    S.published = out.map((o) => o.name).filter((n) => !failed.has(n));
    S.screenName = S.published.includes(screen) ? screen : null;
    if (!S.screenName) throw new Error('The call would not take the picture');
    pc.onconnectionstatechange = () => onPcState(pc);
    await waitConnected(pc, 15000);
  }

  function onPcState(pc) {
    if (pc !== S.pc || S.state === 'off') return;
    const st = pc.connectionState;
    if (st === 'connected') { clearTimeout(S.retry); S.retry = null; if (S.state !== 'live') set('live'); track(); }
    else if (st === 'failed') reconnect();
    else if (st === 'disconnected' && !S.retry) {
      set('reconnecting');
      S.retry = setTimeout(() => { S.retry = null; if (S.pc === pc && pc.connectionState !== 'connected') reconnect(); }, 8000);
    }
  }

  function closePc() {
    const pc = S.pc;
    S.pc = null; S.sessionId = null; S.published = []; S.screenName = null;
    if (pc) { pc.onconnectionstatechange = null; try { pc.close(); } catch {} }
  }

  let reconnecting = false;
  async function reconnect() {
    if (reconnecting || S.state === 'off') return;
    reconnecting = true;
    set('reconnecting');
    closePc();
    track();
    for (let wait = 2000; S.state !== 'off'; wait = Math.min(wait * 2, 30000)) {
      try { await publish(); set('live'); track(); break; }
      catch (e) { console.warn('quiz call reconnect', e); closePc(); await new Promise((r) => setTimeout(r, wait)); }
    }
    reconnecting = false;
  }

  // ---------- presence ----------
  // Shaped like a Gather caller's entry. tv:true keeps Gather from giving this
  // screen a camera tile of its own; quiz:true lets it say who arrived.
  function payload() {
    const live = !!(S.pc && S.pc.connectionState === 'connected');
    return { name: NAME, mic: false, cam: false, sessionId: live ? S.sessionId : null, tracks: live ? S.published.slice() : [], screen: live ? S.screenName : null, shareKind: 'screen', hand: null, tv: true, quiz: true, tvFull: true };
  }
  function track() { if (S.channel && S.subscribed) S.channel.track(payload()).catch(() => {}); }

  function joinPresence() {
    S.supa = S.supa || LQ.client();
    S.subscribed = false;
    S.channel = S.supa.channel('call-' + ROOM, { config: { presence: { key: id } } });
    S.channel
      .on('presence', { event: 'sync' }, () => {
        const st = S.channel.presenceState();
        S.people = Object.entries(st).filter(([k, m]) => k !== id && !(m[m.length - 1] || {}).tv).length;
        emit();
      })
      .subscribe((status) => {
        if (status === 'SUBSCRIBED') { S.subscribed = true; track(); }
      });
  }

  // ---------- start / stop ----------
  async function start() {
    if (S.state !== 'off' && S.state !== 'error') return;
    if (!supported()) return set('error', 'This device cannot share its screen');
    if (!LQ.hostPassword()) return set('error', 'Sign in as the host first');
    set('starting');
    let cap;
    try { cap = await capture(); }
    catch (e) { return set(e && e.name === 'NotAllowedError' ? 'off' : 'error', e && e.name === 'NotAllowedError' ? '' : 'Could not share the screen: ' + ((e && e.message) || e)); }
    S.stream = cap.stream; S.stopCapture = cap.stop;
    const vt = S.stream.getVideoTracks()[0];
    if (vt) vt.addEventListener('ended', () => stop());
    if (!nativeCapture()) keepAlive(true);
    try {
      joinPresence();
      await publish();
      set('live');
      track();
    } catch (e) {
      console.warn('quiz call', e);
      const msg = (e && e.message) || String(e);
      stop();
      set('error', msg);
    }
  }

  function stop() {
    if (S.state === 'off') return;
    S.state = 'off';
    clearTimeout(S.retry); S.retry = null;
    if (S.channel) { try { S.channel.untrack(); } catch {} try { S.supa.removeChannel(S.channel); } catch {} }
    S.channel = null; S.subscribed = false; S.people = 0;
    closePc();
    if (S.stopCapture) { try { S.stopCapture(); } catch {} }
    S.stream = null; S.stopCapture = null;
    keepAlive(false);
    set('off');
  }

  window.addEventListener('pagehide', () => { if (S.channel) { try { S.channel.untrack(); } catch {} } });

  // ---------- Fire TV: frames from Android's screen capture ----------
  // The Fire TV app captures the screen natively and posts each frame as a JPEG
  // data URL to window.__lqFrame; they are painted onto a canvas that is sent as
  // the picture. Its sound comes from the quiz's own sound effects.
  const FireTvCapture = {
    canvas: null, ctx: null, img: null, busy: false, pending: null, resolve: null, reject: null, timer: null,
    start() {
      return new Promise((resolve, reject) => {
        const c = this.canvas = document.createElement('canvas');
        c.width = 1280; c.height = 720;
        this.ctx = c.getContext('2d');
        this.ctx.fillStyle = '#000'; this.ctx.fillRect(0, 0, c.width, c.height);
        this.resolve = resolve; this.reject = reject;
        window.__lqFrame = (url) => this.frame(url);
        window.__lqCaptureState = (st, msg) => this.onState(st, msg);
        this.timer = setTimeout(() => this.onState('error', 'The Fire TV did not start sharing'), 60000);
        window.LetsQuizApp.startCapture();
      });
    },
    onState(st, msg) {
      if (st === 'started' && this.resolve) {
        clearTimeout(this.timer);
        const stream = this.canvas.captureStream(15);
        const audio = LQ.soundStream ? LQ.soundStream() : null;
        if (audio) audio.getAudioTracks().forEach((t) => stream.addTrack(t));
        // A canvas repaints only when a frame arrives; nudge it so the track never goes quiet.
        this.nudge = setInterval(() => { const x = this.ctx.getImageData(0, 0, 1, 1); this.ctx.putImageData(x, 0, 0); }, 1000);
        const r = this.resolve; this.resolve = this.reject = null;
        r({ stream, stop: () => this.stop() });
      } else if (st === 'denied' || st === 'error') {
        clearTimeout(this.timer);
        if (this.reject) { const j = this.reject; this.resolve = this.reject = null; const e = new Error(msg || 'Screen sharing was not allowed'); if (st === 'denied') e.name = 'NotAllowedError'; j(e); }
        else if (S.state !== 'off') stop();
      } else if (st === 'stopped' && S.state !== 'off') stop();
    },
    frame(url) {
      if (this.busy) { this.pending = url; return; }
      this.busy = true;
      const img = this.img = this.img || new Image();
      img.onload = () => {
        const c = this.canvas, s = Math.min(c.width / img.width, c.height / img.height), w = img.width * s, h = img.height * s;
        this.ctx.drawImage(img, (c.width - w) / 2, (c.height - h) / 2, w, h);
        this.busy = false;
        if (this.pending) { const p = this.pending; this.pending = null; this.frame(p); }
      };
      img.onerror = () => { this.busy = false; };
      img.src = url;
    },
    stop() {
      clearInterval(this.nudge);
      try { window.LetsQuizApp.stopCapture(); } catch {}
      window.__lqFrame = null;
    }
  };

  return {
    start, stop, supported,
    get state() { return S.state; }, get error() { return S.error; }, get people() { return S.people; },
    onChange(fn) { listeners.add(fn); return () => listeners.delete(fn); }
  };
})();
