/* Fake call: "📞 Call me in 20 s" for the host's phone. After the countdown a full-screen incoming-call screen comes up with a
 * ringtone and buzzes, until it is cleared with Accept or Decline. The ringtone is an ordinary audio file (ringtone.mp3, the iPhone
 * tone), played through an <audio> element: a phone treats that as media, so it is heard with the phone on silent (the silent switch
 * mutes web sounds made with Web Audio, but not media). The tap on the button starts the element playing, muted, so the phone lets
 * it play later without another tap; when the call comes it is unmuted and restarted. If it will not play, a synthesised marimba
 * tone plays instead, and the bar under the button says which of the two was used on the last call.
 * The countdown and the call live on the page, not in the pop-up that holds the button, so closing that pop-up does not cancel it. */
(() => {
  const DELAY = 20, NAME_KEY = 'lq_fakecall_name', FILE = new URL('ringtone.mp3', document.currentScript?.src || location.href).href;
  let ac = null, t0 = 0, tick = null, ring = null, vib = null, el = null, mounts = [], au = null, last = '';
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

  /* The ringtone as media: an audio element, started muted by the tap, then unmuted from the start when the call comes. */
  function auPrepare() {
    if (!au) { au = new Audio(FILE); au.loop = true; au.preload = 'auto'; au.setAttribute('playsinline', ''); }
    au.muted = true; try { au.currentTime = 0; } catch {}
    au.play().catch(() => {});
  }
  /** The call is here: unmute and play from the start. Resolves true if it is really playing. */
  async function auRing() {
    if (!au) return false;
    try { au.muted = false; au.volume = 1; au.currentTime = 0; await au.play(); } catch { return false; }
    await new Promise((r) => setTimeout(r, 600));
    return !au.paused && !au.muted; // (a phone can be slow to report the time moving, so only play() failing or pausing counts as not playing)
  }
  function auStop() { try { au?.pause(); if (au) au.muted = true; } catch {} }

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
    const clear = () => { stopRing(); auStop(); el?.remove(); el = null; paint(); };
    el.querySelector('.no').onclick = clear; el.querySelector('.yes').onclick = clear;
    startBuzz();
    auRing().then((ok) => { last = ok ? 'the ringtone file played' : 'the backup tone played (the file would not start)'; if (!ok && el) startTone(); paint(); });
  }
  function stopTick() { clearInterval(tick); tick = null; t0 = 0; }
  function start() {
    // pressing the button is the tap that lets the phone play sound later, so the players are woken here
    try { ac = ac || new (window.AudioContext || window.webkitAudioContext)(); ac.resume(); } catch {}
    auPrepare();
    t0 = Date.now() + DELAY * 1000;
    tick = setInterval(() => { if (Date.now() >= t0) show(); else paint(); }, 250);
    paint();
  }
  function cancel() { stopTick(); auStop(); paint(); }
  function paint() {
    mounts = mounts.filter((m) => m.isConnected);
    const left = t0 ? Math.max(0, Math.ceil((t0 - Date.now()) / 1000)) : 0;
    for (const m of mounts) {
      const b = m.querySelector('.fcgo'); if (!b) continue;
      b.textContent = t0 ? `✕ Cancel the call (${left} s)` : `📞 Call me in ${DELAY} s`;
      b.classList.toggle('btn-primary', !t0);
      const n = m.querySelector('.fcnote'); if (n) n.textContent = last && !t0 ? 'Last call: ' + last : '';
    }
  }

  /** Puts the button (and a box for who is "calling") into the given element. */
  window.LQFakeCall = {
    mount(host) {
      css();
      host.classList.add('fcbar');
      host.innerHTML = `<button type="button" class="btn fcgo"></button><input class="fcname" maxlength="40" aria-label="Who is calling" placeholder="Who is calling"><div class="fcnote" style="flex-basis:100%;font-size:.8rem;opacity:.7"></div>`;
      const inp = host.querySelector('.fcname'); inp.value = getName();
      inp.oninput = () => { try { localStorage.setItem(NAME_KEY, inp.value.trim() || 'Hotel Reception'); } catch {} };
      host.querySelector('.fcgo').onclick = () => (t0 ? cancel() : start());
      mounts.push(host); paint();
    },
    // for a test: ring now
    ringNow: show,
    debug: () => ({ paused: au?.paused, muted: au?.muted, t: au?.currentTime, last }),
  };
})();
