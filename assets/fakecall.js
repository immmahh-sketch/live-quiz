/* Fake call: "📞 Call me in 20 s" for the host's phone. After the countdown a full-screen incoming-call screen comes up with a
 * ringtone and buzzes, until it is cleared with Accept or Decline. The ringtone is a YouTube video's sound played as media, so it
 * is heard even with the phone on silent (the silent switch mutes web sounds but not media). The player is started muted by the
 * tap on the button, when the phone allows it, and unmuted from the start when the call comes. If that does not work, a
 * synthesised marimba tone (Web Audio, which does obey the silent switch) plays instead.
 * The countdown and the call live on the page, not in the pop-up that holds the button, so closing that pop-up does not cancel it. */
(() => {
  const DELAY = 20, NAME_KEY = 'lq_fakecall_name', VIDEO = 'MKODR8q2iys';
  let ac = null, t0 = 0, tick = null, ring = null, vib = null, el = null, mounts = [], yt = null, ytReady = false, ytApi = null, ytWant = false, ytCheck = null;
  const getName = () => { try { return localStorage.getItem(NAME_KEY) || 'Hotel Reception'; } catch { return 'Hotel Reception'; } };

  /* The fallback tone: a bright marimba note is a sine plus a quiet overtone four times higher, with a fast decay.
   * One phrase of 16 quick notes, a short gap, then again until stopped. */
  const NOTES = [76, 80, 76, 80, 83, 80, 76, 80, 76, 80, 76, 80, 83, 80, 88, 83]; // MIDI numbers
  const STEP = 0.125, PHRASE = NOTES.length * STEP + 1.1;
  function note(when, midi) {
    const f = 440 * Math.pow(2, (midi - 69) / 12);
    for (const [mul, vol, len] of [[1, 0.34, 0.5], [4, 0.1, 0.12]]) {
      const o = ac.createOscillator(), g = ac.createGain();
      o.type = 'sine'; o.frequency.value = f * mul;
      g.gain.setValueAtTime(0.0001, when); g.gain.exponentialRampToValueAtTime(vol, when + 0.006); g.gain.exponentialRampToValueAtTime(0.0001, when + len);
      o.connect(g); g.connect(ac.destination); o.start(when); o.stop(when + len + 0.02);
    }
  }
  function phrase() { const now = ac.currentTime + 0.05; NOTES.forEach((m, i) => note(now + i * STEP, m)); }
  function startTone() {
    clearInterval(ring);
    try { ac = ac || new (window.AudioContext || window.webkitAudioContext)(); ac.resume(); phrase(); ring = setInterval(phrase, PHRASE * 1000); } catch {}
  }
  function startBuzz() {
    clearInterval(vib);
    const buzz = () => { try { navigator.vibrate?.([700, 300, 700]); } catch {} };
    buzz(); vib = setInterval(buzz, PHRASE * 1000);
  }
  function stopRing() { clearInterval(ring); clearInterval(vib); ring = vib = null; try { navigator.vibrate?.(0); } catch {} }

  /* The ringtone as media: a hidden YouTube player, started by the tap, kept muted until the call comes, then unmuted from the start. */
  function loadApi() {
    if (window.YT?.Player) return Promise.resolve();
    return ytApi = ytApi || new Promise((res, rej) => {
      const prev = window.onYouTubeIframeAPIReady; window.onYouTubeIframeAPIReady = () => { res(); if (prev) prev(); };
      const sc = document.createElement('script'); sc.src = 'https://www.youtube.com/iframe_api'; sc.onerror = () => rej(new Error('no YouTube')); document.head.appendChild(sc);
    });
  }
  function ytPrepare() {
    if (yt) { if (ytReady) { try { yt.mute(); yt.seekTo(0, true); yt.playVideo(); } catch {} } return; }
    const box = document.createElement('div'); box.id = 'fcYt';
    box.style.cssText = 'position:fixed;left:0;bottom:0;width:160px;height:90px;opacity:.02;pointer-events:none;z-index:1';
    box.innerHTML = '<div id="fcYtp"></div>'; document.body.appendChild(box);
    loadApi().then(() => {
      yt = new YT.Player('fcYtp', { width: 160, height: 90, videoId: VIDEO, host: 'https://www.youtube-nocookie.com',
        playerVars: { playsinline: 1, controls: 0, rel: 0, modestbranding: 1, disablekb: 1, fs: 0 },
        events: {
          onReady: () => { ytReady = true; try { yt.mute(); yt.playVideo(); } catch {} if (ytWant) ytRing(); },
          onStateChange: (e) => { if (e.data === 0) { try { yt.seekTo(0, true); yt.playVideo(); } catch {} } }, // it loops while it rings
        } });
    }).catch(() => {});
  }
  /** The call is here: unmute and play from the start. False if the player is not ready. */
  function ytRing() {
    ytWant = true;
    if (!yt || !ytReady) return false;
    try { yt.unMute(); yt.setVolume(100); yt.seekTo(0, true); yt.playVideo(); } catch { return false; }
    return true;
  }
  const ytPlaying = () => { try { return !!yt && ytReady && yt.getPlayerState() === 1 && !yt.isMuted(); } catch { return false; } };
  function ytStop() { ytWant = false; clearTimeout(ytCheck); try { yt?.pauseVideo(); yt?.mute(); } catch {} }

  function css() {
    if (document.getElementById('fcStyle')) return;
    const s = document.createElement('style'); s.id = 'fcStyle';
    s.textContent = `
      #fcCall { position: fixed; inset: 0; z-index: 10000; display: flex; flex-direction: column; align-items: center; justify-content: space-between; padding: 14vh 24px 12vh; background: linear-gradient(#3a3d47, #14151a); color: #fff; font-family: -apple-system, system-ui, "Segoe UI", sans-serif; text-align: center; }
      #fcCall .who { font-size: clamp(2rem, 9vw, 2.8rem); font-weight: 400; line-height: 1.15; margin: 0; }
      #fcCall .sub { font-size: 1.2rem; opacity: .7; margin-top: 8px; }
      #fcCall .btns { display: flex; justify-content: space-around; width: min(360px, 100%); }
      #fcCall .b { display: flex; flex-direction: column; align-items: center; gap: 10px; font-size: .95rem; background: none; border: 0; color: #fff; cursor: pointer; font-family: inherit; }
      #fcCall .b i { width: 74px; height: 74px; border-radius: 50%; display: grid; place-items: center; font-style: normal; font-size: 2rem; }
      #fcCall .b.no i { background: #ff3b30; } #fcCall .b.yes i { background: #34c759; animation: fcShake 1s ease-in-out infinite; }
      @keyframes fcShake { 0%, 100% { transform: rotate(0); } 15% { transform: rotate(-14deg); } 30% { transform: rotate(14deg); } 45% { transform: rotate(-10deg); } 60% { transform: rotate(10deg); } 75% { transform: rotate(0); } }
      .fcbar { display: flex; gap: 8px; align-items: center; flex-wrap: wrap; margin-top: 12px; padding: 10px 12px; border-radius: 12px; background: rgba(0,0,0,.06); }
      .fcbar input { flex: 1; min-width: 120px; font: inherit; padding: 6px 8px; border-radius: 8px; border: 2px solid var(--line, #ccc); }
      .fcbar .fcgo { flex: none; }`;
    document.head.appendChild(s);
  }

  function show() {
    stopTick(); css(); el?.remove();
    el = document.createElement('div'); el.id = 'fcCall';
    el.innerHTML = `<div><p class="who"></p><div class="sub">mobile</div></div><div class="btns"><button class="b no" type="button"><i>✕</i>Decline</button><button class="b yes" type="button"><i>📞</i>Accept</button></div>`;
    el.querySelector('.who').textContent = getName();
    document.body.appendChild(el);
    const clear = () => { stopRing(); ytStop(); el?.remove(); el = null; paint(); };
    el.querySelector('.no').onclick = clear; el.querySelector('.yes').onclick = clear;
    startBuzz();
    if (!ytRing()) startTone();
    else ytCheck = setTimeout(() => { if (el && !ytPlaying()) startTone(); }, 3000); // the video did not start: the synthesised tone instead
  }
  function stopTick() { clearInterval(tick); tick = null; t0 = 0; }
  function start() {
    // pressing the button is the tap that lets the phone play sound later, so the players are woken here
    try { ac = ac || new (window.AudioContext || window.webkitAudioContext)(); ac.resume(); } catch {}
    ytPrepare();
    t0 = Date.now() + DELAY * 1000;
    tick = setInterval(() => { if (Date.now() >= t0) show(); else paint(); }, 250);
    paint();
  }
  function cancel() { stopTick(); ytStop(); paint(); }
  function paint() {
    mounts = mounts.filter((m) => m.isConnected);
    const left = t0 ? Math.max(0, Math.ceil((t0 - Date.now()) / 1000)) : 0;
    for (const m of mounts) {
      const b = m.querySelector('.fcgo'); if (!b) continue;
      b.textContent = t0 ? `✕ Cancel the call (${left} s)` : `📞 Call me in ${DELAY} s`;
      b.classList.toggle('btn-primary', !t0);
    }
  }

  /** Puts the button (and a box for who is "calling") into the given element. */
  window.LQFakeCall = {
    mount(host) {
      css();
      host.classList.add('fcbar');
      host.innerHTML = `<button type="button" class="btn fcgo"></button><input class="fcname" maxlength="40" aria-label="Who is calling" placeholder="Who is calling">`;
      const inp = host.querySelector('.fcname'); inp.value = getName();
      inp.oninput = () => { try { localStorage.setItem(NAME_KEY, inp.value.trim() || 'Hotel Reception'); } catch {} };
      host.querySelector('.fcgo').onclick = () => (t0 ? cancel() : start());
      mounts.push(host); paint();
    },
    // for a test: ring now
    ringNow: show,
    debug: () => { try { return { ready: ytReady, state: yt?.getPlayerState?.(), muted: yt?.isMuted?.(), t: yt?.getCurrentTime?.(), dur: yt?.getDuration?.() }; } catch (e) { return String(e); } },
  };
})();
