/* Is the natural voice's speech for a quiz all saved? The speech bank (quiz-api tts_bank) makes every line a game will say ahead of time; before a hands-free quiz starts this asks the
 * server which of the quiz's lines are kept (tts_ready). If some are not, a pop-up says how complete the quiz is: play anyway (the rest is made as you play, so there can be a pause), or
 * choose another quiz. boxLines / bridgeLines build the same lines as the server's boxGameLines / bridgeGameLines (keep the three in step). */
const VR = (() => {
  const places = (n) => n.toLocaleString('en-GB');
  const on = () => { try { return localStorage.getItem('lq_handsfree') === '1' && localStorage.getItem('lq_nvoice') !== 'off'; } catch { return false; } };
  function boxLines(game) {
    const out = [], q0 = (game && game.questions && game.questions[0]) || {}, cats = q0.cats || [], cols = q0.cols || 1, rows = cats.length, names = cats.map((c) => c.name);
    if (rows) {
      out.push(`Box Clever. ${rows * cols} boxes in ${rows} rows: ${names.join(', ')}.`, `Everyone starts on ${places(q0.start || 1000)}. Let's go!`, `You have ${places(q0.start || 1000)} points in the pot.`);
      out.push(`The rows are: ${names.map((n, r) => `${n}, boxes ${r * cols + 1} to ${(r + 1) * cols}`).join('. ')}.`, `Say a box number and your stake, like ${names[rows - 1]} three, one thousand.`);
      for (let n = 1; n <= rows * cols; n++) out.push(`Box ${n}, ${names[Math.floor((n - 1) / cols)]}.`);
    }
    for (const row of cats) for (const q of row.qs || []) {
      if (q.t) out.push(q.t);
      for (const o of q.o || []) out.push(`${o}.`);
      for (const o of q.a || []) out.push(`${o}.`);
      if (q.w) out.push(`${q.w}.`);
      const right = q.o ? q.o[0] : (q.a || [])[0]; if (right) out.push(`The answer was ${right}.`);
    }
    return out;
  }
  function bridgeLines(g) {
    const out = [];
    if (g && g.cat) out.push(`The category is: ${g.cat}.`, `The shortest way across is ${g.n + g.m - 3} correct answers. You have three lives.`);
    for (const t of (g && g.tiles) || []) if (!t.pad && t.t) { out.push(`${t.t}.`); if (!t.ok) out.push(`${t.t} is not one.`); }
    return out;
  }
  const SAY = 'This quiz is not fully voiced yet. Some lines will pause while they are made. Say play anyway, or choose another quiz.';
  /** Resolves true to carry on, false to go back and choose another quiz. `what` is the quiz's name ("Box Clever"), `note` an extra line for quizzes that always make some speech as they go. */
  async function check(lines, what, note) {
    if (!on() || typeof LQ === 'undefined') return true;
    let r = null; try { r = await LQ.api('tts_ready', { lines }, { timeout: 9000 }); } catch {}
    if (!r || !r.total || (r.have >= r.total && r.basics)) return true;
    const pct = Math.floor((100 * r.have) / r.total);
    return new Promise((done) => {
      const el = document.createElement('div'); el.id = 'vrOver';
      el.style.cssText = 'position:fixed;inset:0;z-index:99999;display:flex;align-items:center;justify-content:center;padding:18px;background:rgba(10,30,29,.88);font-family:Nunito,system-ui,sans-serif';
      const esc = (x) => String(x).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
      el.innerHTML = `<div style="max-width:460px;background:#fff;color:#1b1544;border-radius:20px;padding:22px 20px;box-shadow:0 10px 40px rgba(0,0,0,.5)">
        <div style="font-size:2rem">🎙️</div><h2 style="margin:6px 0 8px;font-size:1.35rem">Not fully voiced yet</h2>
        <p style="margin:0 0 8px;line-height:1.35"><b>${esc(what)}</b> is <b>${pct}%</b> voiced${r.basics ? '' : ', and the usual phrases and scores are still being saved'}. The rest is made as you play, so there may be a short pause now and then.</p>
        ${note ? `<p style="margin:0 0 8px;line-height:1.35;opacity:.8">${esc(note)}</p>` : ''}
        <div style="display:flex;gap:10px;flex-wrap:wrap;margin-top:14px"><button id="vrGo" type="button" style="flex:1;min-width:140px;padding:12px;border:0;border-radius:14px;background:#2e9d57;color:#fff;font:900 1rem Nunito,system-ui,sans-serif">▶ Play anyway</button><button id="vrBack" type="button" style="flex:1;min-width:140px;padding:12px;border:3px solid #1b1544;border-radius:14px;background:#fff;color:#1b1544;font:900 1rem Nunito,system-ui,sans-serif">Choose another quiz</button></div></div>`;
      document.body.appendChild(el);
      let fin = false; const end = (v) => { if (fin) return; fin = true; try { if (typeof HV !== 'undefined' && HV.stop) HV.stop(); } catch {} el.remove(); done(v); };
      el.querySelector('#vrGo').onclick = () => end(true); el.querySelector('#vrBack').onclick = () => end(false);
      try { if (typeof HV !== 'undefined' && HV.screen && typeof BV !== 'undefined' && BV.on) HV.screen({ prompt: SAY, hint: 'Say play anyway, or choose another quiz.', dom: false, items: [
        { words: ['play anyway', 'play', 'go', 'carry on', 'yes', 'ok', 'okay', 'start'], fn: () => end(true) }, { words: ['choose another quiz', 'another quiz', 'another', 'back', 'no', 'menu'], fn: () => end(false) }] }); } catch {}
    });
  }
  return { on, boxLines, bridgeLines, check, SAY };
})();
