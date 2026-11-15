/* The passenger screen, sending side. The CarPlay screen can only show Apple's voice indicator, so the game is played by voice on the phone and this sends a live copy of
 * the phone's screen to a second device (letsquiz.uk/watch) for the passenger to look at. It copies what is on screen (the page's own styles, and the page's HTML a couple of
 * times a second), over a Supabase realtime channel named after a short code that this phone keeps for good (lq_watch). It only sends while a watcher is there, and the watcher
 * can only look: nothing it does reaches the game. On in the car (?car=1), or with ?mirror=1 once (then remembered in lq_mirror).
 *   MIRROR.start(getDoc)   getDoc() returns the document to copy (default: this page). Box Clever's phone screen is in a frame, so warmup.html passes a function. */
const MIRROR = (() => {
  const Q = new URLSearchParams(location.search);
  const enabled = () => { try { if (Q.get('mirror') === '0') localStorage.removeItem('lq_mirror'); if (Q.get('mirror') === '1') localStorage.setItem('lq_mirror', '1'); return Q.get('car') === '1' || Q.get('mirror') === '1' || localStorage.getItem('lq_mirror') === '1'; } catch { return Q.get('car') === '1'; } };
  const code = () => { let c = ''; try { c = localStorage.getItem('lq_watch') || ''; if (!/^[A-Z2-9]{5}$/.test(c)) { c = Array.from({ length: 5 }, () => 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789'[Math.floor(Math.random() * 32)]).join(''); localStorage.setItem('lq_watch', c); } } catch { c = c || 'ZZZZZ'; } return c; };
  let ch = null, watchers = 0, getDoc = () => document, obsDoc = null, obs = null, timer = null, lastHtml = '', lastFrame = '', poll = null;
  function snapshot() {
    let d = null; try { d = getDoc(); } catch {} if (!d || !d.body) return null;
    const v = d.defaultView || window, root = d.documentElement;
    const frame = { hrefs: [...d.querySelectorAll('link[rel=stylesheet]')].map((l) => l.href), css: [...d.querySelectorAll('style')].map((s) => s.textContent).join('\n'), htmlClass: root.className || '', htmlStyle: root.getAttribute('style') || '', bodyClass: d.body.className || '', bodyStyle: d.body.getAttribute('style') || '', w: v.innerWidth || 390, h: v.innerHeight || 800, title: d.title || '' };
    const b = d.body.cloneNode(true); b.querySelectorAll('script,iframe,video,audio,noscript,#bvbtn,#hvbtn,#vrOver').forEach((x) => x.remove());
    return { frame, html: b.innerHTML };
  }
  function send(full) {
    timer = null; if (!ch || !watchers) return;
    const s = snapshot(); if (!s) return;
    const f = JSON.stringify(s.frame);
    if (full || f !== lastFrame) { lastFrame = f; lastHtml = ''; ch.send({ type: 'broadcast', event: 'frame', payload: s.frame }); }
    if (s.html !== lastHtml && s.html.length < 220000) { lastHtml = s.html; ch.send({ type: 'broadcast', event: 'screen', payload: { html: s.html } }); }
  }
  const later = (full) => { if (full) { lastFrame = ''; lastHtml = ''; } if (!timer) timer = setTimeout(() => send(false), 350); };
  function watch() { // follow the document being copied (it can change: a frame loads)
    let d = null; try { d = getDoc(); } catch {} if (!d || !d.body || d === obsDoc) return;
    try { obs && obs.disconnect(); } catch {} obsDoc = d;
    obs = new MutationObserver(() => later(false)); obs.observe(d.documentElement, { subtree: true, childList: true, attributes: true, characterData: true }); later(true);
  }
  function start(fn) {
    if (!enabled() || ch || typeof LQ === 'undefined' || !LQ.client) return null;
    if (fn) getDoc = fn;
    try {
      const sb = LQ.client(); ch = sb.channel('watch-' + code(), { config: { broadcast: { self: false }, presence: { key: 'src' } } });
      ch.on('presence', { event: 'sync' }, () => { const n = Object.keys(ch.presenceState()).filter((k) => k.startsWith('w_')).length; if (n && n !== watchers) { watchers = n; later(true); } else watchers = n; });
      ch.on('broadcast', { event: 'hello' }, () => { watchers = Math.max(1, watchers); later(true); });
      ch.subscribe((st) => { if (st === 'SUBSCRIBED') ch.track({ role: 'src' }); });
      poll = setInterval(() => { watch(); if (watchers) { later(false); try { ch.send({ type: 'broadcast', event: 'ping', payload: {} }); } catch {} } }, 1200); watch();
    } catch { ch = null; }
    return code();
  }
  /** A line for the page to show, so the passenger knows where to go. */
  const hint = () => (enabled() ? `📺 Passenger screen: open letsquiz.uk/watch and enter ${code()}` : '');
  return { start, code, hint, enabled };
})();
