/* Fake call: "📞 Call me in 20 s" for the host's phone. After the countdown a full-screen incoming-call screen comes up with a
 * phone-style ringtone (made here with the Web Audio API, no sound file) and buzzes, until it is cleared with Accept or Decline.
 * The countdown and the call live on the page, not in the pop-up that holds the button, so closing that pop-up does not cancel it. */
(() => {
  const DELAY = 20, NAME_KEY = 'lq_fakecall_name';
  let ac = null, t0 = 0, tick = null, ring = null, vib = null, el = null, mounts = [];
  const getName = () => { try { return localStorage.getItem(NAME_KEY) || 'Hotel Reception'; } catch { return 'Hotel Reception'; } };

  /* Marimba-style ringtone: a bright marimba note is a sine plus a quiet overtone four times higher, with a fast decay.
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
  function startRing() {
    stopRing();
    try { ac = ac || new (window.AudioContext || window.webkitAudioContext)(); ac.resume(); phrase(); ring = setInterval(phrase, PHRASE * 1000); } catch {}
    const buzz = () => { try { navigator.vibrate?.([700, 300, 700]); } catch {} };
    buzz(); vib = setInterval(buzz, PHRASE * 1000);
  }
  function stopRing() { clearInterval(ring); clearInterval(vib); ring = vib = null; try { navigator.vibrate?.(0); } catch {} }

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
    const clear = () => { stopRing(); el?.remove(); el = null; paint(); };
    el.querySelector('.no').onclick = clear; el.querySelector('.yes').onclick = clear;
    startRing();
  }
  function stopTick() { clearInterval(tick); tick = null; t0 = 0; }
  function start() {
    // pressing the button is the tap that lets the phone play sound later, so the audio is woken here
    try { ac = ac || new (window.AudioContext || window.webkitAudioContext)(); ac.resume(); } catch {}
    t0 = Date.now() + DELAY * 1000;
    tick = setInterval(() => { if (Date.now() >= t0) show(); else paint(); }, 250);
    paint();
  }
  function cancel() { stopTick(); paint(); }
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
  };
})();
