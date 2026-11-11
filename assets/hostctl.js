/* Host controls for the Traitors panel (the phone pop-up in the builder, and the host panel window): the buttons that used to sit along the
 * bottom of the host screen once a game is running. Each press is a sealed message to the host screen ({op:'ctl', name}), which does it as if
 * its own button had been pressed. The host screen sends back what the buttons should say (d.bar). The host screen hides its own copies of
 * these buttons while a panel is talking to it (and shows them again if no panel has been heard from for 20 seconds).
 *   LQHostCtl.render(box, d, ask, confirmIt)  - draws the card into box from the host screen's latest report d */
const LQHostCtl = (() => {
  const esc = (s) => String(s ?? '').replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  function css() {
    if (document.getElementById('hcStyle')) return;
    const s = document.createElement('style'); s.id = 'hcStyle';
    s.textContent = `
      .hc { background: #1d2a2e; color: #f4e9d0; border-radius: 14px; padding: 10px; margin: 0 0 10px; }
      .hc-next { width: 100%; font: 900 1.25rem system-ui, sans-serif; padding: 16px 10px; border-radius: 12px; border: 0; background: #ffd60a; color: #1b1640; cursor: pointer; }
      .hc-next small { display: block; font: 700 .75rem system-ui, sans-serif; opacity: .6; margin-top: 3px; }
      .hc-main { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-top: 8px; }
      .hc-main .hc-btn { font-size: 1.05rem; padding: 15px 8px; }
      .hc-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-top: 8px; }
      .hc-grid .hc-btn { font-size: .85rem; padding: 10px 6px; opacity: .85; }
      .hc-btn { font: 800 .95rem system-ui, sans-serif; padding: 12px 8px; border-radius: 11px; border: 1px solid rgba(244,233,208,.25); background: rgba(244,233,208,.1); color: #f4e9d0; cursor: pointer; }
      .hc-btn.on { background: #8a1c26; border-color: #e8c46a; }
      .hc-btn.end { color: #ff9a9a; }
      .hc-btn:disabled { opacity: .4; cursor: default; }
      .hc-msg { margin-top: 8px; font-size: .85rem; color: #ffd60a; min-height: 1.1em; }`;
    document.head.appendChild(s);
  }
  let msgT = null, shown = '';
  function render(box, d, ask, confirmIt) {
    if (!box || !d) return; css();
    const b = d.bar || {};
    if (!b.game) { box.innerHTML = ''; box._hc = ''; return; } // the lobby: the host screen keeps its own buttons
    const callOn = b.callState === 'live' || b.callState === 'reconnecting';
    const ui = Array.isArray(b.ui) ? b.ui : ['skip', 'end', 'back', 'music', 'call', 'fs', 'audiofix']; // the buttons this quiz wants (Settings > Host panel)
    const def = {
      skip: { t: '⏭ Skip this question', dis: b.canSkip === false, big: true }, end: { t: '⏹ End the quiz', cls: 'end', big: true },
      back: { t: '◀ Back', dis: !b.canBack }, music: { t: b.music ? '🎵 Music: on' : '🔇 Music: off', on: b.music },
      call: { t: callOn ? '🔴 On the quiz call' : b.callState === 'starting' ? '📞 Joining…' : '📞 Launch the quiz call', on: callOn, dis: b.callOk === false },
      fs: { t: b.fs ? '⛶ Leave full screen' : '⛶ Full screen' }, audiofix: { t: '🎧 Reconnect audio' },
      pause: { t: b.paused ? '▶ Resume' : '⏸ Pause', on: b.paused }, cam: { t: b.cam ? '🎥 Camera: on' : '🎥 Camera: off', on: b.cam, dis: b.camOk === false },
      hurry: { t: '🤖 Hurry the bots up', dis: !b.bots }, brkplus: { t: '➕ Break: +1 min', dis: !b.brk }, brkminus: { t: '➖ Break: −1 min', dis: !b.brk },
    };
    const btn = (id) => { const d2 = def[id]; return d2 ? `<button class="hc-btn ${d2.on ? 'on' : ''} ${d2.cls || ''}" type="button" data-c="${id}" ${d2.dis ? 'disabled' : ''}>${d2.t}</button>` : ''; };
    const big = ui.filter((id) => def[id]?.big).map(btn).join(''), rest = ui.filter((id) => def[id] && !def[id].big).map(btn).join('');
    const html = `<div class="hc">
      <button class="hc-next" type="button" data-c="next">Next ▶${b.primary && !/^next/i.test(b.primary) ? `<small>${esc(b.primary)}</small>` : ''}</button>
      ${big ? `<div class="hc-main">${big}</div>` : ''}
      ${rest ? `<div class="hc-grid">${rest}</div>` : ''}<div class="hc-msg"></div></div>`;
    const say = (t) => { shown = t; const m = box.querySelector('.hc-msg'); if (m) m.textContent = t; clearTimeout(msgT); msgT = setTimeout(() => { shown = ''; const m2 = box.querySelector('.hc-msg'); if (m2) m2.textContent = ''; }, 6000); };
    if (box._hc === html) { if (d.ctlNote) say(d.ctlNote); return; } // unchanged: leave the buttons alone (a redraw between a touch's down and up would lose the tap)
    box._hc = html; box.innerHTML = html; if (shown) box.querySelector('.hc-msg').textContent = shown;
    if (d.ctlNote) say(d.ctlNote);
    box.querySelectorAll('[data-c]').forEach((el) => el.onclick = async () => {
      const n = el.dataset.c;
      if (n === 'end') { if (!(await confirmIt('End the quiz now?', 'The scores so far will be shown as the final result.', 'End the quiz'))) return; ask({ op: 'ctl', name: 'end' }); say('Ending the quiz…'); return; }
      if (n === 'skip') { if (!(await confirmIt('Skip this question?', 'Nobody scores for it, and the quiz carries straight on to what comes next.', 'Skip it'))) return; ask({ op: 'ctl', name: 'skip' }); return; }
      ask({ op: 'ctl', name: n });
      if (n === 'audiofix') say('Asked the call window to reset the microphone and speakers…');
    });
  }
  return { render };
})();
