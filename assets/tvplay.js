// Box Clever on a TV: play.html?tv=1 (inside tvbox.html). The phone game, drawn on a 960x540 stage that is scaled to fit the screen,
// moved with the Fire TV remote (assets/dpad.js sends the arrow keys and Enter), typed answers on an on-screen keyboard (a real keyboard works too).
// Nothing here changes the game: it re-arranges what boxes-phone.js draws and tells tvbox.html (the parent page) about Back and "Back to the menu".
(() => {
  const q = new URLSearchParams(location.search);
  if (q.get('tv') !== '1') return;
  window.LQ_TV = true;
  document.body.classList.add('tv', 'tvplay');
  window.confirm = () => true; window.alert = () => {}; // a TV has no mouse to dismiss a dialog
  const app = document.getElementById('app');
  const fit = () => document.documentElement.style.setProperty('--tvs', String(Math.min(innerWidth / 960, innerHeight / 540)));
  fit(); addEventListener('resize', fit);
  const tell = (m) => { try { parent.postMessage({ lqtv: m }, '*'); } catch {} };
  const el = (cls) => { const d = document.createElement('div'); d.className = cls; return d; };
  const PP = () => (typeof P !== 'undefined' ? P : null); // P is a top-level const in play.js, so it is not a window property
  const ROWS = ['1234567890', 'QWERTYUIOP', 'ASDFGHJKL', 'ZXCVBNM'];

  /** Wraps the game's own pieces (the two scores, the cabinet, the question or choice) into a landscape layout: scores on top, cabinet left, the rest right. */
  function layout() {
    const kids = [...app.children], rivals = kids.find((e) => e.classList.contains('bxrivals'));
    if (rivals && !app.querySelector(':scope > .bxtv')) {
      const root = el('bxtv'), h = el('bxtvh'), l = el('bxtvl'), r = el('bxtvr');
      kids.slice(0, kids.indexOf(rivals)).forEach((e) => e.classList.add('tvhide')); // the phone's own name bar: the two scores say it all
      kids.slice(kids.indexOf(rivals)).forEach((e) => { if (e === rivals || e.classList.contains('bxmeta')) h.append(e); else if (e.classList.contains('bxcab')) l.append(e); else r.append(e); });
      root.append(h); if (l.children.length) root.append(l); else root.classList.add('wide');
      root.append(r); app.append(root);
    }
    turn();
    keyboard();
    final();
  }

  /** Names the person whose go it is at the top of the right-hand panel, and says 'press OK' instead of 'tap'. */
  function turn() {
    const g = PP()?.state?.bx, r = app.querySelector('.bxtvr'); if (!g || !r || r.querySelector('.tvturn') || g.step === 'seg') return;
    const i = g.step === 'pick' ? g.pickTeam : g.step === 'stake' ? g.turn : g.cur ? (g.step === 'result' ? (g.cur.res?.team ?? g.cur.by) : g.cur.by) : g.turn, t = g.teams?.[i];
    if (t) r.insertAdjacentHTML('afterbegin', '<div class="tvturn" style="--tc:' + t.color + '">' + t.emoji + ' ' + String(t.name).replace(/[<>&]/g, '') + "'s go</div>");
    r.querySelectorAll('.muted').forEach((p) => { p.innerHTML = p.innerHTML.replace(/Tap a drawer, then lock it in./, 'Move to a drawer and press OK, then lock it in.').replace(/Tap a team/g, 'Choose a team'); });
  }
  /** A typed answer: the keyboard is a grid of buttons the remote can walk over. The phone's own text box stays hidden and is kept in step, so the game's own code sends the answer. */
  function keyboard() {
    const form = app.querySelector('#bxTxt'); if (!form || form.dataset.tv) return;
    form.dataset.tv = '1';
    const input = form.querySelector('#bxIn'), key = (PP()?.state?.bx?.cur?.num || '') + ':' + (PP()?.state?.bx?.cur?.at || '');
    const saved = window.__tvTyped && window.__tvTyped.key === key ? window.__tvTyped.val : '';
    input.value = saved;
    const ui = el('tvkbwrap');
    ui.innerHTML = `<div class="tvtxt"><span id="tvTxtV"></span><i class="tvcaret"></i></div>
      <div class="tvkb">${ROWS.map((r) => `<div class="tvkbrow">${[...r].map((c) => `<button type="button" class="tvk" data-k="${c}">${c}</button>`).join('')}</div>`).join('')}
        <div class="tvkbrow"><button type="button" class="tvk wide2" data-k=" ">SPACE</button><button type="button" class="tvk" data-k="'">'</button><button type="button" class="tvk" data-k="-">-</button><button type="button" class="tvk wide2" data-k="⌫">⌫ DELETE</button></div>
        <div class="tvkbrow"><button type="button" class="btn btn-primary btn-lg tvlock" id="tvLock" data-autofocus>Lock in answer</button></div></div>`;
    form.append(ui);
    const show = () => { ui.querySelector('#tvTxtV').textContent = input.value || ''; ui.querySelector('.tvtxt').classList.toggle('empty', !input.value); window.__tvTyped = { key, val: input.value }; };
    const add = (c) => { if (c === '⌫') input.value = input.value.slice(0, -1); else if (input.value.length < 60) input.value += c; show(); };
    ui.querySelectorAll('[data-k]').forEach((b) => { b.onclick = () => add(b.dataset.k); });
    ui.querySelector('#tvLock').onclick = () => { if (input.value.trim()) form.dispatchEvent(new Event('submit', { cancelable: true, bubbles: true })); };
    form.__tvAdd = add; show();
  }
  // a real keyboard (a Bluetooth one on the Fire Stick, or this computer) types straight in
  document.addEventListener('keydown', (e) => {
    const form = app.querySelector('#bxTxt'); if (!form || !form.__tvAdd || e.ctrlKey || e.metaKey || e.altKey) return;
    if (e.key === 'Backspace') { e.preventDefault(); form.__tvAdd('⌫'); }
    else if (e.key.length === 1 && /[A-Za-z0-9 '\-.&!,]/.test(e.key)) { e.preventDefault(); form.__tvAdd(e.key.toUpperCase()); }
  }, true);

  /** The end of the game: a button back to the menu (the game is then marked as played). */
  function final() {
    const done = PP()?.state?.phase === 'final';
    if (!done) return;
    app.querySelectorAll('.btn, .app-top').forEach((b) => { if (!b.closest('.tvfin')) b.classList.add('tvhide'); }); // the phone's own buttons (Join another game) make no sense here
    if (!app.querySelector('#tvMenu')) {
      app.insertAdjacentHTML('beforeend', '<div class="tvfin"><button type="button" class="btn btn-primary btn-lg" id="tvNext" data-autofocus>▶ Next game</button><button type="button" class="btn btn-lg" id="tvMenu">🏠 Menu</button></div>');
      app.querySelector('#tvMenu').onclick = () => tell('menu'); app.querySelector('#tvNext').onclick = () => tell('next');
    }
    tell('final');
  }

  // Re-arranged in the observer itself (a microtask, run before the screen is next painted), never in a timeout: otherwise the phone's own layout
  // shows for a frame after every press and the screen flashes.
  let busy = false;
  new MutationObserver(() => { if (busy) return; busy = true; try { layout(); } finally { Promise.resolve().then(() => { busy = false; }); } }).observe(app, { childList: true });
  document.body.insertAdjacentHTML('beforeend', '<div class="tvhint">◀ ▲ ▼ ▶ move · OK choose · Back to pause</div>');
  // Back on a remote that sends a key (the Silk browser uses its history instead, which tvbox.html catches)
  let keyedAt = 0; window.addEventListener("keydown", () => { if (Date.now() - keyedAt > 400) { keyedAt = Date.now(); tell("key"); } }, true); // tells tvbox.html a key was pressed (it adds its Back step then, and wakes the sound)
  window.addEventListener('keydown', (e) => { if (e.key === 'Escape' || e.key === 'GoBack' || e.key === 'BrowserBack') { e.preventDefault(); tell('back'); } }, true);
})();
