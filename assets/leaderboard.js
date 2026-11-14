/* A social-post-ready leaderboard picture (1080 x 1350, the 4:5 Facebook feed shape), drawn on a canvas.
 *   LQLeader.draw({ title, rows: [{ name, emoji, score }], count, code, until, ended, link }, topN) -> Promise<canvas>
 *   LQLeader.caption({ ... same ... }, topN) -> the post text to paste under it
 * Rows must already be best first; equal scores share a place. Nothing here talks to the server. */
const LQLeader = (() => {
  const W = 1080, H = 1350, PURPLE = '#5b3df5', DEEP = '#1b1340', YELLOW = '#ffd60a', PINK = '#ff4f9a', CYAN = '#34d3ff';
  const HEAD = 'Impact, "Arial Black", "Helvetica Neue", sans-serif', BODY = '"Nunito", "Segoe UI", system-ui, Arial, sans-serif', EMO = '"Apple Color Emoji", "Segoe UI Emoji", "Noto Color Emoji", sans-serif';
  const fmt = (n) => (n < 0 ? '−' : '') + Math.abs(Math.round(n)).toLocaleString('en-GB');
  const rrect = (x, a, b, w, h, r) => { x.beginPath(); x.moveTo(a + r, b); x.arcTo(a + w, b, a + w, b + h, r); x.arcTo(a + w, b + h, a, b + h, r); x.arcTo(a, b + h, a, b, r); x.arcTo(a, b, a + w, b, r); x.closePath(); };
  const sparkle = (x, cx, cy, r, rot, col) => { x.save(); x.translate(cx, cy); x.rotate(rot); x.fillStyle = col; x.beginPath(); for (let i = 0; i < 4; i++) { const a = i * Math.PI / 2; x.lineTo(Math.cos(a) * r, Math.sin(a) * r); x.lineTo(Math.cos(a + Math.PI / 4) * r * .22, Math.sin(a + Math.PI / 4) * r * .22); } x.closePath(); x.fill(); x.restore(); };
  const seeded = (s) => () => { s = (s * 1664525 + 1013904223) % 4294967296; return s / 4294967296; };
  const closes = (iso) => { if (!iso) return ''; const d = new Date(iso); let h = d.getHours(); const m = d.getMinutes(), ap = h >= 12 ? 'pm' : 'am'; h = h % 12 || 12; return `${d.toLocaleDateString('en-GB', { weekday: 'long' })} ${h}${m ? ':' + String(m).padStart(2, '0') : ''}${ap}`; };
  const placeOf = (rows) => rows.map((r) => rows.filter((q) => q.score > r.score).length + 1);
  /** Fits a string into a width by shrinking the font, and cuts it with … if it is still too long. */
  function fit(x, txt, font, size, maxW) { x.font = `900 ${size}px ${font}`; let s = size; while (x.measureText(txt).width > maxW && s > size * 0.55) { s -= 2; x.font = `900 ${s}px ${font}`; } if (x.measureText(txt).width > maxW) { let t = txt; while (t.length > 1 && x.measureText(t + '…').width > maxW) t = t.slice(0, -1); return { text: t + '…', size: s }; } return { text: txt, size: s }; }
  function text(x, txt, cx, cy, size, o = {}) {
    x.save(); x.textAlign = o.a || 'center'; x.textBaseline = 'middle'; x.lineJoin = 'round';
    const f = o.maxW ? fit(x, txt, o.f || BODY, size, o.maxW) : { text: txt, size }; x.font = `${o.w || 900} ${f.size}px ${o.f || BODY}`;
    if (o.shadow) { x.shadowColor = 'rgba(0,0,0,.4)'; x.shadowBlur = o.shadow; x.shadowOffsetY = o.shadow / 2; }
    if (o.stroke) { x.lineWidth = o.sw || f.size * .14; x.strokeStyle = o.stroke; x.strokeText(f.text, cx, cy); }
    x.fillStyle = o.c || '#fff'; x.fillText(f.text, cx, cy); x.restore();
  }
  function wrap(x, txt, font, size, maxW, maxLines) { x.font = `800 ${size}px ${font}`; const words = txt.split(/\s+/), lines = []; let cur = ''; for (const w of words) { const t = cur ? cur + ' ' + w : w; if (x.measureText(t).width > maxW && cur) { lines.push(cur); cur = w; } else cur = t; } if (cur) lines.push(cur); if (lines.length > maxLines) { lines.length = maxLines; lines[maxLines - 1] = lines[maxLines - 1].replace(/\s*\S*$/, '') + '…'; } return lines; }
  function loadImage(src) { return new Promise((res) => { const i = new Image(); i.onload = () => res(i); i.onerror = () => res(null); i.src = src; }); }

  const cap1 = (t) => String(t || '').trim().replace(/^./, (ch) => ch.toUpperCase());
  /** The "drawers" style (d.style = 'drawers'): a filing cabinet, one drawer per player, the winner's pulled out and gold. Made for Box Clever. */
  async function drawDrawers(d, topN = 5) {
    const c = document.createElement('canvas'); c.width = W; c.height = H; const x = c.getContext('2d');
    const rows = (d.rows || []).slice(0, topN), places = placeOf(d.rows || []), n = rows.length;
    const bg = x.createLinearGradient(0, 0, 0, H); bg.addColorStop(0, '#08111f'); bg.addColorStop(1, '#17395f'); x.fillStyle = bg; x.fillRect(0, 0, W, H);
    const spot = x.createRadialGradient(W / 2, 700, 60, W / 2, 700, 780); spot.addColorStop(0, 'rgba(255,214,10,.14)'); spot.addColorStop(1, 'rgba(255,214,10,0)'); x.fillStyle = spot; x.fillRect(0, 0, W, H);
    const r = seeded(5); for (let i = 0; i < 60; i++) { x.globalAlpha = .15 + r() * .5; sparkle(x, r() * W, r() * H, 2 + r() * 5, r() * 3, '#cfe3ff'); } x.globalAlpha = 1;
    x.save(); x.translate(W / 2, 78); rrect(x, -165, -34, 330, 68, 34); x.fillStyle = YELLOW; x.fill(); x.restore(); text(x, "LET'S QUIZ!", W / 2, 80, 40, { c: DEEP });
    text(x, d.fixedHeading || (d.ended ? 'FINAL RESULTS' : d.heading || 'SCOREBOARD'), W / 2, 190, 124, { f: HEAD, w: 400, c: '#fff', stroke: '#08111f', shadow: 24, maxW: 980 });
    const sub = wrap(x, cap1(d.title), BODY, 40, 900, 2); sub.forEach((l, i) => text(x, l, W / 2, 275 + i * 48, 40, { c: '#9fc3ee', maxW: 940 }));
    const lead = rows[0]?.name || 'the leader', gap = n > 1 ? rows[0].score - rows[1].score : 0;
    const tag = !n ? 'Nobody has played yet' : d.ended ? (gap > 0 && gap <= 1000 ? `${lead} wins by just ${fmt(gap)}!` : `Congratulations ${lead}! 🎉`) : `Can anyone catch ${lead}? 👀`;
    text(x, tag, W / 2, sub.length > 1 ? 392 : 360, 54, { c: YELLOW, stroke: '#08111f', sw: 8, maxW: 940 });
    // the cabinet
    const gp = n > 5 ? 10 : 16, top0 = 440, zone = 610, dh = Math.max(56, Math.min(172, (zone - 48 - gp * Math.max(0, n - 1)) / Math.max(n, 1))), bodyH = n * dh + gp * Math.max(0, n - 1) + 48, cy0 = top0 + (zone - bodyH) / 2;
    x.save(); rrect(x, 62, cy0 - 4, W - 124, bodyH + 8, 34); x.fillStyle = '#10243b'; x.shadowColor = 'rgba(0,0,0,.6)'; x.shadowBlur = 40; x.shadowOffsetY = 18; x.fill(); x.restore();
    x.save(); rrect(x, 62, cy0 - 4, W - 124, bodyH + 8, 34); x.lineWidth = 6; x.strokeStyle = '#3d6a9c'; x.stroke(); x.restore();
    const FR = { 1: ['#ffe27a', '#d9a010', '#7a5200'], 2: ['#eef2f8', '#aab4c6', '#5d6a80'], 3: ['#f0b283', '#b86f38', '#6e3a14'] }, REST = ['#38597d', '#2a4666', '#8fb4dd'];
    rows.forEach((p, k) => {
      const pl = places[k], pal = FR[pl], first = pl === 1, x0 = 90 + (first ? 0 : 0), w = W - 180, y = cy0 + 24 + k * (dh + gp), out = first ? 0 : 0;
      x.save(); rrect(x, x0, y + out, w, dh, 20); const gr = x.createLinearGradient(0, y, 0, y + dh); gr.addColorStop(0, pal ? pal[0] : REST[0]); gr.addColorStop(1, pal ? pal[1] : REST[1]);
      x.fillStyle = gr; x.shadowColor = first ? 'rgba(255,214,10,.55)' : 'rgba(0,0,0,.45)'; x.shadowBlur = first ? 36 : 16; x.shadowOffsetY = first ? 8 : 6; x.fill(); x.shadowColor = 'transparent'; x.lineWidth = 5; x.strokeStyle = pal ? pal[2] : REST[2]; x.stroke(); x.restore();
      x.save(); rrect(x, x0 + 14, y + 12, w - 28, dh - 24, 12); x.lineWidth = 2; x.strokeStyle = pal ? 'rgba(0,0,0,.16)' : 'rgba(255,255,255,.12)'; x.stroke(); x.restore();
      const ink = pal ? '#1b1340' : '#fff', mid = y + dh * .46, big = Math.min(dh * .42, 74);
      // the number plate
      x.save(); x.beginPath(); x.arc(x0 + 20 + big * .8, mid, big * .72, 0, Math.PI * 2); x.fillStyle = pal ? pal[2] : '#173048'; x.fill(); x.lineWidth = 4; x.strokeStyle = pal ? '#fff8' : '#8fb4dd'; x.stroke(); x.restore();
      text(x, String(pl), x0 + 20 + big * .8, mid + 2, big * .86, { f: HEAD, w: 400, c: pal ? pal[0] : '#fff' });
      text(x, p.emoji || '🙂', x0 + 40 + big * 2.2, mid, big * 1.05, { f: EMO });
      text(x, p.name || 'Player', x0 + 40 + big * 3.0, mid, Math.min(dh * .4, 68), { a: 'left', c: ink, maxW: w - big * 3.0 - 330 });
      text(x, (p.display ?? fmt(p.score)), x0 + w - 36, mid, Math.min(dh * .5, 88), { a: 'right', f: HEAD, w: 400, c: p.score < 0 ? '#c0283f' : ink, maxW: 300 });
      // the brass handle
      x.save(); rrect(x, x0 + w / 2 - 70, y + dh - 26, 140, 14, 7); x.fillStyle = pal ? '#fff9' : 'rgba(255,255,255,.35)'; x.fill(); x.lineWidth = 2; x.strokeStyle = 'rgba(0,0,0,.25)'; x.stroke(); x.restore();
      if (first) text(x, '👑', x0 + 20 + big * .8, y - 4, 64, { f: EMO });
    });
    const cnt = d.count ?? (d.rows || []).length, plural = d.countText || `${cnt} player${cnt === 1 ? '' : 's'} played`;
    const cl = d.footer || (d.ended ? 'Thanks for playing!' : d.until ? `Still time to play · closes ${closes(d.until)}` : 'Play it free on your phone');
    const pill = (cy, w, h, fill, line, lw, label, size, col) => { x.save(); x.translate(W / 2, cy); rrect(x, -w / 2, -h / 2, w, h, h / 2); x.fillStyle = fill; x.shadowColor = 'rgba(0,0,0,.5)'; x.shadowBlur = 24; x.shadowOffsetY = 9; x.fill(); x.shadowColor = 'transparent'; x.lineWidth = lw; x.strokeStyle = line; x.stroke(); x.restore(); text(x, label, W / 2, cy + 3, size, { c: col, maxW: w - 60 }); };
    text(x, plural, W / 2, 1096, 38, { c: '#cfe3ff' });
    pill(1166, 800, 100, '#fff', YELLOW, 7, d.link || 'letsquiz.uk/play', 66, '#0c2a4d');
    pill(1254, 660, 80, YELLOW, '#08111f', 6, `Game code: ${d.code || 'WARMUP'}`, 50, '#08111f');
    text(x, cl, W / 2, 1318, 32, { c: '#9fc3ee', maxW: 980 });
    return c;
  }
  async function draw(d, topN = 5) {
    if (d.style === 'drawers') return drawDrawers(d, topN);
    const c = document.createElement('canvas'); c.width = W; c.height = H; const x = c.getContext('2d');
    const rows = (d.rows || []).slice(0, topN), places = placeOf(d.rows || []), compact = topN > 5;
    // background: the Let's Quiz purple, rays and stars
    const g = x.createLinearGradient(0, 0, 0, H); g.addColorStop(0, '#150e38'); g.addColorStop(.55, '#2b1a8a'); g.addColorStop(1, PURPLE); x.fillStyle = g; x.fillRect(0, 0, W, H);
    x.save(); x.translate(W / 2, 520); for (let i = 0; i < 16; i++) { x.rotate(Math.PI * 2 / 16); x.fillStyle = 'rgba(255,255,255,.05)'; x.beginPath(); x.moveTo(0, 0); x.lineTo(-90, -1500); x.lineTo(90, -1500); x.fill(); } x.restore();
    const rg = x.createRadialGradient(W / 2, 560, 40, W / 2, 560, 760); rg.addColorStop(0, 'rgba(255,214,10,.16)'); rg.addColorStop(1, 'rgba(255,214,10,0)'); x.fillStyle = rg; x.fillRect(0, 0, W, H);
    const r = seeded(11); for (let i = 0; i < 90; i++) { x.globalAlpha = .25 + r() * .6; sparkle(x, r() * W, r() * H, 3 + r() * 6, r() * 3, '#fff'); } x.globalAlpha = 1;
    // header
    x.save(); x.translate(W / 2, 78); rrect(x, -165, -34, 330, 68, 34); x.fillStyle = YELLOW; x.fill(); x.restore(); text(x, "LET'S QUIZ!", W / 2, 80, 40, { c: DEEP });
    text(x, d.fixedHeading || (d.ended ? 'FINAL SCOREBOARD' : d.heading || 'SCOREBOARD'), W / 2, 188, 118, { f: HEAD, w: 400, c: YELLOW, stroke: DEEP, shadow: 24, maxW: 980 });
    const sub = wrap(x, cap1(d.title), BODY, 42, 900, 2); sub.forEach((l, i) => text(x, l, W / 2, 275 + i * 50, 42, { c: '#fff', stroke: DEEP, sw: 6 }));
    // podium: 2nd, 1st, 3rd
    const top = rows.slice(0, 3), t1 = compact ? 405 : 420, t2 = compact ? 470 : 505, ph1 = compact ? 330 : 400, ph2 = compact ? 270 : 310;
    const slot = [{ i: 1, cx: 190, w: 300, top: t2, h: ph2, col: '#cfd6e6', medal: '🥈', av: 100, nm: 38, sc: 60 }, { i: 0, cx: 540, w: 400, top: t1, h: ph1, col: YELLOW, medal: '🥇', av: 140, nm: 48, sc: 84 }, { i: 2, cx: 890, w: 300, top: t2, h: ph2, col: '#e0a068', medal: '🥉', av: 100, nm: 38, sc: 60 }];
    for (const s of slot) {
      const p = top[s.i]; if (!p) continue;
      x.save(); rrect(x, s.cx - s.w / 2, s.top, s.w, s.h, 40); x.fillStyle = '#fff'; x.shadowColor = 'rgba(0,0,0,.45)'; x.shadowBlur = 36; x.shadowOffsetY = 14; x.fill(); x.shadowColor = 'transparent'; x.lineWidth = 10; x.strokeStyle = s.col; x.stroke(); x.restore();
      text(x, s.medal, s.cx - s.w / 2 + 44, s.top + 24, 64, { f: EMO });
      if (s.i === 0) text(x, '👑', s.cx, s.top - 24, 96, { f: EMO });
      text(x, p.emoji || '🙂', s.cx, s.top + s.h * .30, s.av, { f: EMO });
      text(x, p.name || 'Player', s.cx, s.top + s.h * .60, s.nm, { c: DEEP, maxW: s.w - 40 });
      text(x, (p.display ?? fmt(p.score)), s.cx, s.top + s.h * .82, s.sc, { f: HEAD, w: 400, c: p.score < 0 ? '#d94b5f' : PURPLE, maxW: s.w - 40 });
    }
    // the rest of the table
    const rest = rows.slice(3), y0 = compact ? 752 : 845, rh = compact ? 58 : 84, gap = compact ? 8 : 14;
    rest.forEach((p, k) => {
      const y = y0 + k * (rh + gap); rrect(x, 90, y, W - 180, rh, rh / 2); x.fillStyle = 'rgba(255,255,255,.96)'; x.fill();
      text(x, String(places[k + 3]), 150, y + rh / 2, rh * .6, { f: HEAD, w: 400, c: PURPLE });
      text(x, p.emoji || '🙂', 225, y + rh / 2, rh * .62, { f: EMO });
      text(x, p.name || 'Player', 275, y + rh / 2, rh * .5, { a: 'left', c: DEEP, maxW: 520 });
      text(x, (p.display ?? fmt(p.score)), W - 135, y + rh / 2, rh * .62, { a: 'right', f: HEAD, w: 400, c: p.score < 0 ? '#d94b5f' : PURPLE });
    });
    if (!rows.length) text(x, 'Nobody has played yet', W / 2, 700, 64, { c: '#fff', stroke: DEEP });
    else if (!rest.length) { // a short table leaves a gap: a line to fill it
      const lead = rows[0].name || 'the leader';
      text(x, d.ended ? `Congratulations ${lead}! 🎉` : `Can anyone catch ${lead}? 👀`, W / 2, compact ? 835 : 935, 62, { c: '#fff', stroke: DEEP, sw: 9, shadow: 14, maxW: 940, f: BODY });
      if (!d.ended) text(x, 'Have a go before it closes 👇', W / 2, compact ? 905 : 1010, 44, { c: YELLOW, stroke: DEEP, sw: 7, maxW: 940 });
    }
    // footer: how many, where to play, when it closes
    const n = d.count ?? (d.rows || []).length, plural = d.countText || `${n} player${n === 1 ? '' : 's'} so far`;
    const cl = d.footer || (d.ended ? 'Thanks for playing!' : d.until ? `Still time to play · closes ${closes(d.until)}` : 'Play it free on your phone');
    const pill = (cy, w, h, fill, line, lw, label, size, col) => { x.save(); x.translate(W / 2, cy); rrect(x, -w / 2, -h / 2, w, h, h / 2); x.fillStyle = fill; x.shadowColor = 'rgba(0,0,0,.4)'; x.shadowBlur = 24; x.shadowOffsetY = 9; x.fill(); x.shadowColor = 'transparent'; x.lineWidth = lw; x.strokeStyle = line; x.stroke(); x.restore(); text(x, label, W / 2, cy + 3, size, { c: col, maxW: w - 60 }); };
    if (compact) {
      pill(1140, 780, 84, '#fff', PINK, 6, d.link || 'letsquiz.uk/play', 56, PURPLE);
      pill(1228, 620, 66, YELLOW, DEEP, 5, `Game code: ${d.code || 'WARMUP'}`, 42, DEEP);
      text(x, `${plural} · ${cl}`, W / 2, 1308, 30, { c: '#fff', stroke: DEEP, sw: 6, maxW: 1000 });
    } else {
      text(x, plural, W / 2, 1085, 40, { c: '#fff', stroke: DEEP, sw: 6 });
      pill(1160, 800, 104, '#fff', PINK, 7, d.link || 'letsquiz.uk/play', 70, PURPLE);
      pill(1250, 660, 84, YELLOW, DEEP, 6, `Game code: ${d.code || 'WARMUP'}`, 52, DEEP);
      text(x, cl, W / 2, 1316, 34, { c: '#fff', stroke: DEEP, sw: 6, maxW: 980 });
    }
    return c;
  }
  /** The words to post with it. */
  function caption(d, topN = 5) {
    const rows = (d.rows || []).slice(0, topN), places = placeOf(d.rows || []), medal = ['🥇', '🥈', '🥉'];
    const lines = rows.map((p, i) => `${places[i] <= 3 ? medal[places[i] - 1] : places[i] + '.'} ${p.emoji ? p.emoji + ' ' : ''}${p.name} · ${(p.display ?? fmt(p.score))}`);
    return [d.captionIntro || `🏆 ${d.fixedHeading || (d.ended ? 'FINAL SCOREBOARD' : (d.heading || 'SCOREBOARD'))} · ${cap1(d.title)}`.trim(), '', ...lines, '', `${d.countText || (d.count ?? (d.rows || []).length) + ' players so far'}. ${d.ended ? 'Thanks for playing!' : d.until ? `Still time to play: it closes ${closes(d.until)}!` : 'Play it free on your phone!'}`, `👉 ${d.link || 'letsquiz.uk/play'} · game code ${d.code || 'WARMUP'}`].join('\n');
  }
  return { draw, caption, fmt, W, H };
})();
if (typeof window !== 'undefined') window.LQLeader = LQLeader;
