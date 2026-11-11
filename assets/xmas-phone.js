/* Let's Quiz phones: CHRISTMAS DAY (November 2026), the phone half of assets/xmas.js.
 *  - 🍽 Your plate: the dishes greyed out until you collect them (each pops onto the plate), the ketchup beside it, what is still up for grabs, your family
 *    character with its quirk and power, and everyone else's plates.
 *  - The dish up for grabs on each question, in a chip under the top bar.
 *  - The surprises: PINCH (pick a dish to nick), SPOT THE ELF (tap him), the elf's swap, Uncle Keith, the Monopoly argument, the dinner table, the end.
 * Loaded before play.html's own script (after party-phone.js). Everything is drawn over the app (fixed layers), so the usual screens carry on underneath.
 * State arrives as s.xm; the phone sends {op: 'power' | 'pinch' | 'elf' | 'swap'} on the 'xm' channel event; the host answers a refusal on 'xmno'. */

const XPM = LQ.XMAS;
const XP = { prev: null, seq: -1, flashN: undefined, waveN: undefined, bellFor: '', hidden: '', screenKey: '', sel: {}, pw: {}, charSeen: false, elfAt: 0, gainT: null, tick: null };
const xpMe = () => P.state?.xm;
const xpHave = (s, pid = P.pid) => new Set(s.xm.plates?.[pid] || []);
const xpPl = (s, pid) => s.xm.players?.find((p) => p.pid === pid);
const xpNm = (s, pid) => xpPl(s, pid)?.name || 'someone';
const xpDishes = XPM.ITEMS.filter((i) => !i.ketchup && i.k !== 'turkey');
const xpSeenKey = () => 'lq_xm_' + (P.code || '') + '_char';
const xpSeen = () => { try { return localStorage.getItem(xpSeenKey()) === '1'; } catch { return false; } };
const xpMark = () => { try { localStorage.setItem(xpSeenKey(), '1'); } catch {} };
const xpCount = (s, pid = P.pid) => XPM.ITEMS.filter((i) => xpHave(s, pid).has(i.k)).length;

/** The plate: turkey in the middle, the eight other dishes round the rim, the ketchup beside it. `fresh`/`lost` are the keys that just came or went. */
function xpPlateHtml(s, pid = P.pid, fresh = [], lost = []) {
  const have = xpHave(s, pid), slot = (i, x, y, big) => `<div class="xpslot ${big ? 'big' : ''} ${have.has(i.k) ? 'got' : ''} ${fresh.includes(i.k) ? 'new' : ''} ${lost.includes(i.k) ? 'lost' : ''}" style="left:${x}%;top:${y}%" title="${esc(i.name)}">${i.icon}<small>${esc(i.name.split(' ')[0])}</small></div>`;
  const ring = xpDishes.map((i, n) => { const a = (-90 + n * 360 / xpDishes.length) * Math.PI / 180; return slot(i, (50 + 37 * Math.cos(a)).toFixed(1), (50 + 37 * Math.sin(a)).toFixed(1)); }).join('');
  const k = XPM.item('ketchup');
  return `<div class="xpplate"><div class="xprim"></div>${slot(XPM.item('turkey'), 50, 50, true)}${ring}</div>
    <div class="xpketchup"><span class="k ${have.has('ketchup') ? 'got' : ''} ${fresh.includes('ketchup') ? 'new' : ''}">${k.icon}</span><span>${have.has('ketchup') ? 'Ketchup: yours!' : 'Ketchup: only for a full plate, and only a 1% question wins it'}</span></div>`;
}
const xpMiniHtml = (s, skipMe) => `<div class="xpmini">${(s.xm.players || []).filter((p) => !(skipMe && p.pid === P.pid)).sort((a, b) => xpCount(s, b.pid) - xpCount(s, a.pid)).map((p) => `<div class="r"><span>${esc(p.emoji || '🙂')}</span><span class="n">${esc(p.name)}${p.pid === P.pid ? ' (you)' : ''}</span><span class="is">${XPM.ITEMS.map((i) => `<i class="${xpHave(s, p.pid).has(i.k) ? 'on' : ''}">${i.icon}</i>`).join('')}</span><b>${xpCount(s, p.pid)}</b></div>`).join('')}</div>`;

// ---------------------------------------------------------------- every state
function xmPhoneAfter(s) {
  const x = s.xm;
  if (!x || P.view || P.teamRole === 'act') { document.body.classList.remove('xpchip-on'); for (const id of ['xpbtn', 'xpchip', 'xpsheet', 'xpfull', 'xpgain', 'xpelf']) document.getElementById(id)?.remove(); XP.prev = null; return; }
  xpWatchPlate(s); xpButton(s); xpChip(s); xpScreen(s); xpEvents(s);
  const sh = document.getElementById('xpsheet'); if (sh && sh.dataset.key !== xpSheetKey(s)) xpSheet(true);
}
/** My plate changed: dishes won pop on (a full-screen moment), dishes lost shake off. */
function xpWatchPlate(s) {
  const now = [...xpHave(s)];
  if (XP.prev === null) { XP.prev = now; XP.seq = s.xm.seq; return; }
  const gained = now.filter((k) => !XP.prev.includes(k)), lost = XP.prev.filter((k) => !now.includes(k));
  XP.prev = now;
  if (!gained.length && !lost.length) return;
  XP.fresh = gained; XP.lost = lost;
  if (document.getElementById('xpsheet')) { xpSheet(true); return; }
  xpGain(s, gained, lost);
  if (!s.xm.screen) { XP.fresh = []; XP.lost = []; } // with a surprise on screen, its plate does the popping
}
function xpGain(s, gained, lost) {
  document.getElementById('xpgain')?.remove(); clearTimeout(XP.gainT);
  const el = document.createElement('div'); el.id = 'xpgain'; el.className = 'xpgain';
  const names = gained.map((k) => XPM.item(k)).filter(Boolean), gone = lost.map((k) => XPM.item(k)).filter(Boolean), n = xpCount(s), tot = XPM.ITEMS.length;
  const msg = gained.includes('ketchup') ? '🍅 THE KETCHUP IS YOURS!' : names.length ? `${names.map((i) => i.icon + ' ' + i.name).join(' and ')} collected!` : '';
  const lostMsg = gone.length ? `😱 ${gone.map((i) => i.icon + ' ' + i.name).join(' and ')} ${gone.length > 1 ? 'have' : 'has'} gone from your plate!${s.xm.screen?.line ? '<br><small>' + esc(s.xm.screen.line) + '</small>' : ''}` : '';
  el.innerHTML = `<div class="xpin"><div class="xpbig">${gained.length ? (n === tot ? '🎄 A FULL PLATE!' : 'Yum!') : 'Oh no!'}</div>${xpPlateHtml(s, P.pid, gained, lost)}<div class="xpmsg">${msg}${msg && lostMsg ? '<br>' : ''}${lostMsg}</div><div class="xpmeter">${n} of ${tot} on your plate</div><div class="xpsmall">Tap to carry on</div></div>`;
  el.onclick = () => { el.remove(); clearTimeout(XP.gainT); };
  document.body.appendChild(el);
  if (gained.length) for (let i = 0; i < 12; i++) { const sp = document.createElement('span'); sp.className = 'xpspark'; sp.textContent = ['✨', '⭐', '🎉'][i % 3]; sp.style.left = 30 + Math.random() * 40 + '%'; sp.style.top = '42%'; sp.style.setProperty('--dx', (Math.random() * 240 - 120) + 'px'); sp.style.setProperty('--dy', (Math.random() * -200 - 20) + 'px'); el.querySelector('.xpin').appendChild(sp); }
  if (navigator.vibrate) try { navigator.vibrate(gained.length ? [60, 40, 120] : [200]); } catch {}
  XP.gainT = setTimeout(() => el.remove(), 4200);
}
function xpButton(s) {
  const x = s.xm, me = x.chars?.[P.pid], can = x.win && !x.used?.[P.pid];
  let b = document.getElementById('xpbtn');
  if (!b) { b = document.createElement('button'); b.id = 'xpbtn'; b.className = 'xpbtn'; b.onclick = () => xpSheet(); document.body.appendChild(b); }
  b.classList.toggle('pow', !!can && !!me);
  b.innerHTML = `🍽 <b>${xpCount(s)}/${XPM.ITEMS.length}</b><small>${can && me ? 'Power ready!' : 'Your plate'}</small>`;
}
function xpChip(s) {
  const x = s.xm, k = x.cur, show = k && ['typecard', 'countdown', 'question'].includes(s.phase) && !x.screen;
  let el = document.getElementById('xpchip');
  document.body.classList.toggle('xpchip-on', !!show);
  if (!show) { el?.remove(); return; }
  const it = XPM.item(k), R = XPM.RARITY[it.rar], left = x.left?.[k] ?? 0, have = xpHave(s).has(k);
  let html;
  if (it.ketchup) { const full = XPM.dishes().every((i) => xpHave(s).has(i.k)), n = XPM.dishes().filter((i) => xpHave(s).has(i.k)).length; html = `🍅 <b>THE KETCHUP QUESTION</b><small>${have ? 'You already have it!' : full ? "You've a full plate: get this right and the ketchup is yours!" : `You need all nine dishes first (you have ${n}). Answer for points anyway.`}</small>`; }
  else html = `${it.icon} <b>Win the ${esc(it.name)}</b><small>${esc(it.cat)} · ${R.stars} ${R.label}${it.rar > 1 ? ' · only the quickest right answers collect' : ''} · ${left} chance${left === 1 ? '' : 's'} left${have ? ' · you already have it' : ''}</small>`;
  if (!el) { el = document.createElement('div'); el.id = 'xpchip'; document.body.appendChild(el); }
  el.className = 'xpchip' + (it.ketchup ? ' ketchup' : ''); if (el.dataset.h !== html) { el.dataset.h = html; el.innerHTML = html; }
}
/** The doorbell, the family's powers being played, the elf waving. */
function xpEvents(s) {
  const x = s.xm;
  if (XP.flashN === undefined) XP.flashN = x.flash?.n ?? 0;
  else if (x.flash && x.flash.n !== XP.flashN) { XP.flashN = x.flash.n; if ((s.now || Date.now()) - x.flash.at < 9000) partyFlash({ icon: x.flash.icon, text: `${x.flash.name}: ${x.flash.text}` }); }
  if (XP.waveN === undefined) XP.waveN = x.wave ?? 0;
  else if (x.wave !== XP.waveN) { XP.waveN = x.wave; const e = document.createElement('div'); e.className = 'xpmini-elf'; e.textContent = '🧝'; e.style.right = (8 + Math.random() * 60) + 'vw'; document.body.appendChild(e); setTimeout(() => e.remove(), 4000); }
  const bk = x.bell ? s.q?.id || 'q' : '';
  if (bk && bk !== XP.bellFor) { XP.bellFor = bk; partyFlash({ icon: '🔔', text: 'Ding dong! Auntie Maureen is at the door: DOUBLE POINTS on this question!' }); }
  if (!bk) XP.bellFor = '';
}

// ---------------------------------------------------------------- the plate sheet
const xpSheetKey = (s) => [s.xm.seq, s.xm.win, s.xm.used?.[P.pid], s.xm.chars?.[P.pid], s.xm.cur || '', s.xm.screen ? 1 : 0, s.phase === 'question' ? 'q' : ''].join('|');
function xpSheet(refresh) {
  const s = P.state; if (!s?.xm) return;
  const old = document.getElementById('xpsheet'); if (old && !refresh) { old.remove(); return; }
  const x = s.xm, have = xpHave(s), me = XPM.char(x.chars?.[P.pid]), el = old || document.createElement('div');
  el.id = 'xpsheet'; el.className = 'xpsheet'; el.dataset.key = xpSheetKey(s);
  const miss = XPM.ITEMS.filter((i) => !have.has(i.k));
  const list = miss.length ? miss.map((i) => { const R = XPM.RARITY[i.rar], left = x.left?.[i.k] ?? 0; return `<div class="xpli"><span class="ic">${i.icon}</span><span class="nm">${esc(i.name)}<br><small>${esc(i.cat)}</small></span><span class="st">${R.stars}<br>${i.ketchup ? 'needs all 9' : `${left} chance${left === 1 ? '' : 's'} left`}</span></div>`; }).join('') : '<div class="xpli">🎄 Nothing missing: a full plate!</div>';
  const used = x.used?.[P.pid], pwHtml = me ? `<div class="xpchar"><div class="t"><span class="ic">${me.icon}</span><div><b>You are ${esc(me.name)}</b></div></div>
      <p><b>Quirk:</b> ${esc(me.quirk)}</p><p><b>Power:</b> ${esc(me.power)}. ${esc(me.how)}</p>${xpArmed(s)}
      ${used ? '<p class="xpsmall">✅ Power used.</p>' : `<div id="xpPw"></div>`}</div>` : '';
  const cl = x.clock;
  el.innerHTML = `<div class="xpin"><div class="xphead"><b>🍽 Your Christmas dinner</b><button class="xpclose" data-xc>Close</button></div>
    ${cl ? `<div class="xpday">${cl.icon} ${cl.time} · ${esc(cl.scene)}</div>` : ''}
    ${xpPlateHtml(s, P.pid, XP.fresh || [], XP.lost || [])}
    <div class="xpmeter" style="text-align:center">${xpCount(s)} of ${XPM.ITEMS.length} · every dish missing costs 2,000, a full plate pays 5,000</div>
    <div class="xplist">${list}</div>${pwHtml}
    <p class="xpsmall" style="margin-top:10px"><b>Everyone's plates</b></p>${xpMiniHtml(s)}</div>`;
  XP.fresh = []; XP.lost = [];
  if (!old) document.body.appendChild(el);
  el.querySelector('[data-xc]').onclick = () => el.remove();
  el.onclick = (e) => { if (e.target === el) el.remove(); };
  if (me && !used) xpPowerUi(el, s, me);
}
const xpArmed = (s) => { const a = s.xm.armed?.[P.pid]; return a ? `<p class="xpsmall">⏳ Armed: ${a === 'wake' ? 'double points and a guaranteed dish on the next dish question' : 'insured on the next dish question'}.</p>` : s.xm.shield?.[P.pid] ? `<p class="xpsmall">🚪 In your room: safe from thieves and the elf for ${s.xm.shield[P.pid]} more dish question${s.xm.shield[P.pid] === 1 ? '' : 's'}.</p>` : ''; };
/** The power button, and whatever it needs: a dish, a player, or both. */
function xpPowerUi(el, s, me) {
  const box = el.querySelector('#xpPw'); if (!box) return;
  const can = s.xm.win, others = (s.xm.players || []).filter((p) => p.pid !== P.pid), st = XP.pw;
  const send_ = () => { send('xm', { pid: P.pid, op: 'power', target: st.target || null, k: st.k || null }); XP.pw = {}; XP.pwKey = ''; el.remove(); };
  const why = can ? '' : '<p class="xpsmall">Powers are used between questions: wait for the answer or the scores.</p>';
  const draw = () => {
    let h = why;
    if (me.need === 'item') { const miss = XPM.ITEMS.filter((i) => i.rar === 1 && !xpHave(s).has(i.k)); h += miss.length ? `<div class="xpitems">${miss.map((i) => `<button class="xpitem ${st.k === i.k ? 'sel' : ''}" data-k="${i.k}" ${can ? '' : 'disabled'}>${i.icon}</button>`).join('')}</div>` : '<p class="xpsmall">You have every common dish already.</p>'; }
    if (me.need === 'target' || me.need === 'steal') h += `<div class="xpwho">${others.map((p) => `<button data-t="${p.pid}" class="${st.target === p.pid ? 'sel' : ''}" ${can ? '' : 'disabled'}>${esc(p.emoji || '🙂')} ${esc(p.name)}</button>`).join('')}</div>`;
    if (me.need === 'steal' && st.target) { const ks = (s.xm.plates?.[st.target] || []).filter((k) => !xpHave(s).has(k)); h += ks.length ? `<div class="xpitems">${ks.map((k) => `<button class="xpitem ${st.k === k ? 'sel' : ''}" data-k="${k}" ${can ? '' : 'disabled'}>${XPM.item(k).icon}</button>`).join('')}</div>` : '<p class="xpsmall">They have nothing you are missing.</p>'; }
    const ready = can && (me.need === '' || (me.need === 'item' && st.k) || (me.need === 'target' && st.target) || (me.need === 'steal' && st.target && st.k));
    h += `<button class="xpgo" data-go ${ready ? '' : 'disabled'}>Use ${esc(me.power)}</button>`;
    box.innerHTML = h;
    box.querySelectorAll('[data-t]').forEach((b) => b.onclick = () => { st.target = b.dataset.t; st.k = null; XP.pwKey = 't' + st.target; draw(); });
    box.querySelectorAll('[data-k]').forEach((b) => b.onclick = () => { st.k = b.dataset.k; XP.pwKey = (st.target || '') + st.k; draw(); });
    box.querySelector('[data-go]').onclick = send_;
  };
  draw();
}

// ---------------------------------------------------------------- the surprises (full-screen layers)
function xpScreen(s) {
  const sc = s.xm.screen;
  let el = document.getElementById('xpfull');
  if (!sc) { if (el) { el.remove(); } XP.screenKey = ''; XP.hidden = ''; clearInterval(XP.tick); document.getElementById('xpelf')?.remove(); if (!xpSeen() && s.phase !== 'lobby' && s.xm.chars?.[P.pid]) xpCharCard(s); return; }
  document.getElementById('xpgain')?.remove(); document.getElementById('xpsheet')?.remove(); document.getElementById('xpchar')?.remove();
  if (XP.hidden === sc.id) { el?.remove(); return; }
  const key = [sc.id, sc.step, sc.spotter || '', sc.line, XP.sel.a || '', XP.sel.b || '', XP.sel.k || '', XP.sel.t || ''].join('|');
  if (el && XP.screenKey === key) return;
  XP.screenKey = key;
  if (!el) { el = document.createElement('div'); el.id = 'xpfull'; el.className = 'xpfull'; document.body.appendChild(el); }
  const me = s.xm.chars?.[P.pid], c = XPM.CHARS.find((x) => x.k === me);
  const fr = XP.fresh || [], lo = XP.lost || []; XP.fresh = []; XP.lost = [];
  const close = `<button class="xpclose" data-hide style="margin-top:10px">Hide this</button>`;
  let body = '', spot = false;
  const secs = () => `<div class="xpsmall">⏱ <b id="xpCount">${Math.ceil((sc.ms || 0) / 1000)}</b>s</div>`;
  XP.countEnd = Date.now() + (sc.ms || 0);
  if (sc.kind === 'pinch') {
    if (sc.step === 'pick' && sc.by === P.pid) {
      const groups = {}; for (const o of sc.opts || []) (groups[o.pid] = groups[o.pid] || []).push(o.k);
      body = `<div class="xpbig">🤚 PINCH!</div><div class="xpmsg">You were the quickest finger! Nick a dish from somebody's plate.</div>${secs()}` + Object.entries(groups).map(([pid, ks]) => `<div class="xpli" style="margin:4px 0"><span class="nm">${esc(xpNm(s, pid))}</span>${ks.map((k) => `<button class="xpitem" data-p="${pid}|${k}">${XPM.item(k).icon}</button>`).join('')}</div>`).join('');
    } else if (sc.step === 'pick') body = `<div class="xpbig">🤚 PINCH!</div><div class="xpmsg">${esc(xpNm(s, sc.by))} was the quickest finger and is choosing what to nick…</div>${secs()}${xpMiniHtml(s)}`;
    else body = `<div class="xpbig">${sc.ok ? '🤚 GOTCHA!' : '🛡 FOILED!'}</div><div class="xpmsg">${esc(sc.line)}</div>${xpPlateHtml(s, P.pid, fr, lo)}${close}`;
  } else if (sc.kind === 'elf') {
    if (sc.step === 'spot') { spot = true; body = `<div class="xpbig">🧝 SPOT THE ELF!</div><div class="xpmsg">He's hiding somewhere on your screen. Tap him first and you choose two plates for him to swap!</div>${secs()}`; }
    else if (sc.step === 'choose' && sc.spotter === P.pid) {
      const a = XP.sel.a, b = XP.sel.b, ps = s.xm.players || [];
      body = `<div class="xpbig">🧝 YOU SPOTTED HIM!</div><div class="xpmsg">Pick two plates for the elf to swap (one dish each way).</div>${secs()}<div class="xpwho">${ps.map((p) => `<button data-s="${p.pid}" class="${a === p.pid || b === p.pid ? 'sel' : ''}">${esc(p.emoji || '🙂')} ${esc(p.name)}${p.pid === P.pid ? ' (you)' : ''}</button>`).join('')}</div><button class="xpgo" data-swap ${a && b ? '' : 'disabled'}>Swap them!</button>`;
    } else if (sc.step === 'choose') body = `<div class="xpbig">🧝 SPOTTED!</div><div class="xpmsg">${esc(xpNm(s, sc.spotter))} spotted the elf first and is choosing two plates to swap…</div>${secs()}`;
    else body = `<div class="xpbig">🧝 ${sc.ok ? 'THE ELF HAS STRUCK!' : 'NOTHING HAPPENED'}</div><div class="xpmsg">${esc(sc.line)}</div>${xpPlateHtml(s, P.pid, fr, lo)}${close}`;
  } else if (sc.kind === 'uncle') body = `<div class="xpbig">🧔 UNCLE KEITH</div><div class="xpmsg">${esc(sc.line)}</div>${xpPlateHtml(s, P.pid, fr, lo)}${close}`;
  else if (sc.kind === 'monopoly') body = `<div class="xpbig">🎲 THE MONOPOLY ARGUMENT</div><div class="xpmsg">${esc(sc.line)}</div>${close}`;
  else if (sc.kind === 'table') body = `<div class="xpbig">🍽 THE DINNER TABLE</div>${xpPlateHtml(s, P.pid, fr, lo)}${xpMiniHtml(s)}${close}`;
  else if (sc.kind === 'final') {
    const f = s.xm.final?.[P.pid];
    body = `<div class="xpbig">🎄 THE DINNER IS SERVED</div>${xpPlateHtml(s, P.pid, fr, lo)}<div class="xpmsg">${f ? (f.full ? `A FULL PLATE! +${f.delta.toLocaleString('en-GB')} points` : `${f.missing} dish${f.missing === 1 ? '' : 'es'} missing: ${f.delta.toLocaleString('en-GB')} points`) : ''}</div>${xpMiniHtml(s)}${close}`;
  }
  el.className = 'xpfull'; el.innerHTML = `<div class="xpin">${body}</div>`;
  el.querySelector('[data-hide]')?.addEventListener('click', () => { XP.hidden = sc.id; el.remove(); });
  el.querySelectorAll('[data-p]').forEach((b) => b.onclick = () => { const [pid, k] = b.dataset.p.split('|'); send('xm', { pid: P.pid, op: 'pinch', target: pid, k }); b.disabled = true; });
  el.querySelectorAll('[data-s]').forEach((b) => b.onclick = () => { const id = b.dataset.s; if (XP.sel.a === id) XP.sel.a = null; else if (XP.sel.b === id) XP.sel.b = null; else if (!XP.sel.a) XP.sel.a = id; else if (!XP.sel.b) XP.sel.b = id; else { XP.sel.a = XP.sel.b; XP.sel.b = id; } XP.screenKey = ''; xpScreen(P.state); });
  el.querySelector('[data-swap]')?.addEventListener('click', () => { send('xm', { pid: P.pid, op: 'swap', a: XP.sel.a, b: XP.sel.b }); XP.sel = {}; });
  clearInterval(XP.tick); XP.tick = setInterval(() => { const c = document.getElementById('xpCount'); if (c) c.textContent = Math.max(0, Math.ceil((XP.countEnd - Date.now()) / 1000)); }, 500);
  if (spot) xpElf(s, sc);
  else document.getElementById('xpelf')?.remove();
}
/** The elf pops up in a random place on this phone (Auntie Maureen sees him three seconds before anyone else). */
function xpElf(s, sc) {
  const me = s.xm.chars?.[P.pid], wait = Math.max(0, (me === 'maureen' ? 0 : XPM.CFG.MAUREEN_HEAD_START_MS) - (sc.age || 0)) + 300 + Math.random() * 900;
  document.getElementById('xpelf')?.remove();
  setTimeout(() => {
    const cur = P.state?.xm?.screen; if (!cur || cur.id !== sc.id || cur.step !== 'spot') return;
    const b = document.createElement('button'); b.id = 'xpelf'; b.className = 'xpelf'; b.textContent = '🧝';
    b.style.left = (8 + Math.random() * 70) + 'vw'; b.style.top = (22 + Math.random() * 58) + 'vh';
    b.onclick = () => { send('xm', { pid: P.pid, op: 'elf' }); b.remove(); if (navigator.vibrate) try { navigator.vibrate(80); } catch {} };
    document.body.appendChild(b);
  }, wait);
}
/** The first time: who you are in the family. */
function xpCharCard(s) {
  if (document.getElementById('xpchar')) return;
  const c = XPM.char(s.xm.chars?.[P.pid]); if (!c) return;
  const el = document.createElement('div'); el.id = 'xpchar'; el.className = 'xpfull';
  el.innerHTML = `<div class="xpin"><div class="xpsmall">It's Christmas Day. You are…</div><div style="font-size:5rem;line-height:1.1">${c.icon}</div><div class="xpbig">${esc(c.name)}</div>
    <div class="xpchar" style="text-align:left"><p><b>Your quirk (always on):</b> ${esc(c.quirk)}</p><p><b>Your power (once):</b> ${esc(c.power)}. ${esc(c.how)}</p></div>
    <p class="xpsmall">Build your Christmas dinner by getting questions right: each dish belongs to a category. Every dish missing at the end costs 2,000, and a full plate pays 5,000. Tap 🍽 any time to see your plate and use your power.</p><button class="xpgo" data-ok>Let's go!</button></div>`;
  el.querySelector('[data-ok]').onclick = () => { xpMark(); el.remove(); };
  document.body.appendChild(el);
}
