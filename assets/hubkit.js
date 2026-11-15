/* Shared by the "Choose your quiz" page (choose.html), Best of 15 (best15.html) and Bridge of Lies (bridge.html), and read by Box Clever's own pages.
 * One place for: the two players' names, the game points (carried through whatever is played; they reset at 3am, or on a button), the 960x540
 * stage (540x960 on a portrait phone) scaled to the screen, the on-screen keyboard the TV remote walks over, and the shared pool of 50 games
 * (pool_state / pool_claim / pool_done in quiz-api) that stops a game being played twice on any device. */
window.HUB = (() => {
  const KEY = 'lq_hub';
  const P = new URLSearchParams(location.search);
  const test = P.get('test') === '1';   // ?test=1: a test run (a fixed short game, nothing used up, no game points)
  const mode = { tv: P.get('tv') === '1' || /LetsQuizTV/.test(navigator.userAgent), car: P.get('car') === '1' };
  if (mode.car) { try { localStorage.setItem('lq_handsfree', '1'); } catch {} } // the car: hands-free is on, as in the warm-up's car mode
  const read = (k) => { try { return JSON.parse(localStorage.getItem(k) || 'null'); } catch { return null; } };
  const write = (k, v) => { try { localStorage.setItem(k, JSON.stringify(v)); } catch {} };

  /** The day the game points belong to: a new one starts at 3am, so an evening that runs past midnight stays one day. */
  const dayKey = () => { const d = new Date(Date.now() - 3 * 3600e3); return d.getFullYear() + '-' + String(d.getMonth() + 1).padStart(2, '0') + '-' + String(d.getDate()).padStart(2, '0'); };
  let S = null;
  function load() {
    S = read(KEY) || {};
    if (!Array.isArray(S.names) || S.names.length < 2) { // first visit: the names Box Clever already knows
      const tv = read('lq_tvbox') || {}, pl = read('lq_player') || {}, lo = read('lq_locals') || [];
      S.names = (tv.names && tv.names.length > 1 ? tv.names : [pl.name || 'Player 1', lo[0] || 'Player 2']).slice(0, 2);
      S.emojis = tv.emojis && tv.emojis.length > 1 ? tv.emojis.slice(0, 2) : null;
      S.named = !!(tv.namesSet || (pl.name && lo[0]));
    }
    if (!S.emojis) { const e = (window.LQ && LQ.EMOJIS) || ['🦊', '🐼', '🐸', '🦄', '🐙', '🦁']; const a = e[Math.floor(Math.random() * e.length)]; let b = e[Math.floor(Math.random() * e.length)]; if (b === a) b = e[(e.indexOf(a) + 1) % e.length]; S.emojis = [a, b]; }
    if (S.day !== dayKey()) { S.day = dayKey(); S.gp = [0, 0]; S.log = []; }
    if (!Array.isArray(S.gp)) S.gp = [0, 0];
    return S;
  }
  const save = () => write(KEY, S);
  load(); save();
  const fresh = () => { load(); return S; }; // reload from storage (another page may have changed it) and apply the 3am reset

  const names = () => fresh().names.slice();
  const emojis = () => fresh().emojis.slice();
  /** Names are kept for the hub and handed to Box Clever (its own storage) so every game uses the same two. */
  function setName(i, v) {
    fresh(); S.names[i] = (v || '').trim().slice(0, 14) || 'Player ' + (i + 1); S.named = true; save();
    const tv = read('lq_tvbox') || {}; tv.names = S.names.slice(); tv.emojis = S.emojis.slice(); tv.namesSet = true; write('lq_tvbox', tv);
    const pl = read('lq_player') || {}; if (i === 0) { pl.name = S.names[0]; pl.emoji = S.emojis[0]; write('lq_player', pl); }
    try { localStorage.setItem('lq_locals', JSON.stringify([S.names[1]])); } catch {}
  }
  const points = () => fresh().gp.slice();
  function award(i, game) { if (test) return S.gp.slice(); fresh(); S.gp[i] = (S.gp[i] || 0) + 1; (S.log = S.log || []).push({ w: S.names[i], game: game || '', at: new Date().toISOString() }); save(); return S.gp.slice(); }
  function resetPoints() { fresh(); S.gp = [0, 0]; S.log = []; save(); }
  /** Box Clever ends: the highest pot (less any loan) takes the game point. teams: [{ n: name, v: value }]. Counted once per key (a reload must not award it twice). */
  function awardBox(key, teams) {
    if (test) return { win: -1, text: 'Test game: no game point.' };
    fresh(); S.boxAwards = S.boxAwards || {};
    if (S.boxAwards[key]) return S.boxAwards[key];
    const vals = teams.map((t) => +t.v || 0), max = Math.max(...vals), at = vals.indexOf(max); let win = -1;
    if (vals.length > 1 && vals.filter((v) => v === max).length === 1) { const nm = String(teams[at].n || '').trim().toLowerCase(); win = S.names.findIndex((x) => x.trim().toLowerCase() === nm); if (win < 0 && at < 2) win = at; }
    if (win >= 0) { S.gp[win] = (S.gp[win] || 0) + 1; (S.log = S.log || []).push({ w: S.names[win], game: 'Box Clever', at: new Date().toISOString() }); }
    const r = { win, text: win >= 0 ? '🏆 ' + S.names[win] + ' wins a game point!  ' + S.names[0] + ' ' + S.gp[0] + ' – ' + S.gp[1] + ' ' + S.names[1] : 'A draw: no game point.  ' + S.names[0] + ' ' + S.gp[0] + ' – ' + S.gp[1] + ' ' + S.names[1] };
    S.boxAwards[key] = r; const keys = Object.keys(S.boxAwards); if (keys.length > 20) delete S.boxAwards[keys[0]];
    save(); return r;
  }
  const pointsText = () => { const n = names(), g = points(); return `${n[0]} ${g[0]} – ${g[1]} ${n[1]}`; };

  // ------------------------------------------------------------ the stage
  function stage() {
    const el = document.documentElement;
    const fit = () => {
      const portrait = innerHeight > innerWidth * 1.05 && !mode.tv, W = portrait ? 540 : 960, H = portrait ? 960 : 540;
      el.style.setProperty('--s', String(Math.min(innerWidth / W, innerHeight / H))); el.style.setProperty('--W', W + 'px'); el.style.setProperty('--H', H + 'px');
      el.classList.toggle('portrait', portrait);
    };
    fit(); addEventListener('resize', fit); addEventListener('orientationchange', fit);
    if (mode.tv) document.body.classList.add('tv');
  }
  /** Where "Choose another quiz" goes, keeping the TV / car flags. */
  const hubUrl = () => 'choose' + (mode.tv ? '?tv=1' : mode.car ? '?car=1' : '');
  const goHub = () => { location.href = hubUrl(); };
  /** The link a game tile follows (Box Clever has a TV page and a phone page). */
  const gameUrl = { box: () => (mode.tv ? 'tvbox?auto=1&hub=1&tv=1' : 'warmup?pool=1&hub=1' + (mode.car ? '&car=1' : '')), best15: () => 'best15' + (mode.tv ? '?tv=1' : mode.car ? '?car=1' : ''), bridge: () => 'bridge' + (mode.tv ? '?tv=1' : mode.car ? '?car=1' : '') };

  // ------------------------------------------------------------ overlays and the on-screen keyboard
  const $ = (s, r = document) => r.querySelector(s);
  const esc = (s) => String(s ?? '').replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  function overlay(html) { let o = $('#hubOver'); if (!o) { o = document.createElement('div'); o.id = 'hubOver'; document.body.appendChild(o); } o.innerHTML = `<div class="modal-bg"><div class="modal hubpop">${html}</div></div>`; return o; }
  const close = () => { const o = $('#hubOver'); if (o) o.innerHTML = ''; };
  const focusFirst = () => setTimeout(() => { try { DPAD.focusFirst(); } catch {} }, 40);
  function confirmBox(title, text, yes, fn) {
    overlay(`<h2>${esc(title)}</h2><p>${esc(text)}</p><button class="btn primary" id="hubYes" data-autofocus>${esc(yes)}</button><button class="btn" id="hubNo">Cancel</button>`);
    $('#hubYes').onclick = () => { close(); fn(); }; $('#hubNo').onclick = () => { close(); focusFirst(); }; focusFirst();
    if (window.HV && HV.on()) HV.screen({ prompt: title + ' Say yes or no.', dom: false, hint: 'Say yes, or no.', items: [{ words: ['yes', 'yeah', 'yep', 'yup', 'confirm', 'ok', 'okay', 'sure'], fn: () => $('#hubYes') && $('#hubYes').click() }, { words: ['no', 'nope', 'cancel', 'back'], fn: () => $('#hubNo') && $('#hubNo').click() }] });
  }
  /** A keyboard the remote can walk over (also tapped on a phone). opts: { value, max, onChange(v), onEnter(v), enter: 'Done', punct } -> { get, set }. */
  function keyboard(root, opts = {}) {
    let v = opts.value || '';
    const rows = ['1234567890', 'QWERTYUIOP', 'ASDFGHJKL' + (opts.punct ? "'" : ''), 'ZXCVBNM' + (opts.punct ? '-.' : '')];
    root.innerHTML = `<div class="hkb">${rows.map((r) => `<div class="hkrow">${[...r].map((c) => `<button type="button" class="hk" data-k="${c}">${c}</button>`).join('')}</div>`).join('')}<div class="hkrow"><button type="button" class="hk w" data-k=" ">SPACE</button><button type="button" class="hk w" data-k="⌫">⌫ DELETE</button><button type="button" class="hk w go" data-k="⏎" data-autofocus>${esc(opts.enter || '✔ Done')}</button></div></div>`;
    const set = (x) => { v = x; opts.onChange && opts.onChange(v); };
    const add = (c) => {
      if (c === '⌫') return set(v.slice(0, -1));
      if (c === '⏎') return opts.onEnter && opts.onEnter(v);
      if (v.length >= (opts.max || 40)) return;
      set(v + (opts.caps === 'name' ? (v && v.slice(-1) !== ' ' ? c.toLowerCase() : c) : c.toLowerCase()));
    };
    root.querySelectorAll('[data-k]').forEach((b) => { b.onclick = () => add(b.dataset.k); });
    return { get: () => v, set: (x) => { v = x; opts.onChange && opts.onChange(v); } };
  }
  /** Ask for a name on the keyboard. */
  function rename(i, done) {
    let cur = names()[i] === 'Player ' + (i + 1) ? '' : names()[i];
    overlay(`<h2>Player ${i + 1}'s name</h2><div class="kbtxt" id="hubKbv"></div><div id="hubKb"></div>`);
    const show = () => { const e = $('#hubKbv'); e.textContent = cur; e.classList.toggle('empty', !cur); };
    keyboard($('#hubKb'), { value: cur, max: 14, caps: 'name', onChange: (x) => { cur = x; show(); }, onEnter: (x) => { setName(i, x); close(); done && done(); } });
    show(); focusFirst();
  }

  // ------------------------------------------------------------ the shared pool of games
  const devId = () => { let d = ''; try { d = localStorage.getItem('lq_pooldev') || ''; if (!d) { d = 'd' + Math.random().toString(36).slice(2, 10); localStorage.setItem('lq_pooldev', d); } } catch {} return d || 'd0'; };
  function pool(name) {
    const api = (action, game) => LQ.api(action, { pool: name, game, dev: devId() }, { timeout: 6000 }).catch(() => null);
    return {
      async state() { const r = await api('pool_state'); return r ? { ok: true, played: new Set(r.played || []), others: new Set((r.claimed || []).filter((c) => c.dev !== devId()).map((c) => c.game)) } : { ok: false, played: new Set(), others: new Set() }; },
      claim: (id) => api('pool_claim', id), done: (id) => api('pool_done', id),
    };
  }
  return { test, mode, names, emojis, setName, points, award, awardBox, resetPoints, pointsText, stage, hubUrl, goHub, gameUrl, overlay, close, focusFirst, confirmBox, keyboard, rename, pool, devId, esc, $, dayKey };
})();
