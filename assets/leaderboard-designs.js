/* The picture designs for "📣 Post scores". The first two (classic podium, filing cabinet) live in leaderboard.js; these add eighteen more,
 * so every click can be a different look. All of them draw the same 1080 x 1350 leaderboard from the same data, so the heading, the
 * game title, every score, the link and the game code are on every design.  Load after leaderboard.js. */
(() => {
  if (typeof LQLeader === 'undefined') return;
  const { rrect, sparkle, seeded, closes, placeOf, fit, text, wrap, cap1, fmt, W, H, PURPLE, DEEP, YELLOW, PINK, CYAN, HEAD, BODY, EMO } = LQLeader.kit;
  const SERIF = 'Georgia, "Times New Roman", serif', MONO = '"Courier New", Courier, monospace';
  const HAND = `"Segoe Print", "Bradley Hand", "Chalkboard SE", "Comic Sans MS", ${BODY}`;
  const NEON = ['#ffd60a', '#ff4fd8', '#34d3ff', '#7dff6b', '#ff8a3d', '#b18cff', '#ff5c7a', '#5cffd0'];

  // ── shared pieces ────────────────────────────────────────────────────────────────────────────
  const start = (d, topN) => { const c = document.createElement('canvas'); c.width = W; c.height = H; const all = d.rows || [], rows = all.slice(0, topN); return { c, x: c.getContext('2d'), rows, places: placeOf(all), n: rows.length, top: 440, zone: 610 }; };
  const headingOf = (d) => d.fixedHeading || (d.ended ? 'FINAL SCOREBOARD' : d.heading || 'SCOREBOARD');
  const leadOf = (rows) => rows[0]?.name || 'the leader';
  const tagOf = (d, rows) => !rows.length ? 'Nobody has played yet' : d.ended ? `Congratulations ${leadOf(rows)}! 🎉` : `Can anyone catch ${leadOf(rows)}? 👀`;
  const countOf = (d) => { const n = d.count ?? (d.rows || []).length; return d.countText || `${n} player${n === 1 ? '' : 's'} so far`; };
  const closeOf = (d) => d.footer || (d.ended ? 'Thanks for playing!' : d.until ? `Still time to play · closes ${closes(d.until)}` : 'Play it free on your phone');
  const val = (p) => p.display ?? fmt(p.score);
  const ord = (n) => { const s = ['th', 'st', 'nd', 'rd'], v = n % 100; return n + (s[(v - 20) % 10] || s[v] || s[0]); };
  const mw = (x, t, f, size, w = 900) => { x.font = `${w} ${size}px ${f}`; return x.measureText(t).width; };
  const clip = (s, n) => { const a = [...String(s || 'Player')]; return a.length > n ? a.slice(0, n - 1).join('') + '…' : a.join(''); };
  /** Row height and first row's y for n rows stacked down the body zone. */
  const geo = (b, maxH, gap, minH = 44) => { const n = Math.max(b.n, 1), dh = Math.max(minH, Math.min(maxH, (b.zone - gap * (n - 1)) / n)), tot = dh * n + gap * (n - 1); return { dh, gap, y0: b.top + Math.max(0, (b.zone - tot) / 2) }; };
  const burst = (x, cx, cy, r1, r2, pts, rot = 0) => { x.beginPath(); for (let i = 0; i < pts * 2; i++) { const a = rot + i * Math.PI / pts, r = i % 2 ? r1 : r2; x.lineTo(cx + Math.cos(a) * r, cy + Math.sin(a) * r); } x.closePath(); };
  /** Brand pill, big heading, game title and a line about the leader. o = { align, brandY, brand:{fill,ink,line}, head:{c,stroke,f,w,size,shadow,sw,y}, sub:{c,stroke,sw,f}, tag:{c,stroke,sw,f} | false } */
  function header(x, d, b, o = {}) {
    const left = o.align === 'left', X = left ? 70 : W / 2, A = left ? 'left' : 'center', br = o.brand || { fill: YELLOW, ink: DEEP }, h = o.head || {}, s = o.sub || {}, by = o.brandY || 78, bx = left ? 235 : W / 2;
    x.save(); rrect(x, bx - 165, by - 34, 330, 68, 34); x.fillStyle = br.fill; x.fill(); if (br.line) { x.lineWidth = 4; x.strokeStyle = br.line; x.stroke(); } x.restore();
    text(x, "LET'S QUIZ!", bx, by + 2, 40, { c: br.ink });
    text(x, headingOf(d), X, h.y || 190, h.size || 124, { a: A, f: h.f || HEAD, w: h.w || 400, c: h.c || '#fff', stroke: h.stroke, sw: h.sw, shadow: h.shadow, maxW: left ? 940 : 980 });
    const sub = wrap(x, cap1(d.title), s.f || BODY, 40, 900, 2); sub.forEach((l, i) => text(x, l, X, 275 + i * 48, 40, { a: A, c: s.c || '#fff', stroke: s.stroke, sw: s.sw, f: s.f, maxW: 940 }));
    if (o.tag !== false) { const t = o.tag || {}; text(x, tagOf(d, b.rows), X, sub.length > 1 ? 392 : 360, 54, { a: A, c: t.c || YELLOW, stroke: t.stroke, sw: t.sw || 8, f: t.f, maxW: 940 }); }
  }
  /** The count, the link pill, the game-code pill and the closing line. o = { link:{fill,ink,line,lw,glow}, code:{…}, count, countStroke, foot, f } */
  function footer(x, d, o) {
    const f = o.f, pill = (cy, w, h, p, label, size) => {
      x.save(); x.translate(W / 2, cy); rrect(x, -w / 2, -h / 2, w, h, h / 2); x.fillStyle = p.fill; x.shadowColor = p.glow || 'rgba(0,0,0,.45)'; x.shadowBlur = p.glow ? 30 : 22; x.shadowOffsetY = p.glow ? 0 : 8; x.fill(); x.shadowColor = 'transparent';
      if (p.line) { x.lineWidth = p.lw || 6; x.strokeStyle = p.line; x.stroke(); } x.restore(); text(x, label, W / 2, cy + 3, size, { c: p.ink, f, maxW: w - 60 });
    };
    text(x, countOf(d), W / 2, 1096, 38, { c: o.count || '#fff', stroke: o.countStroke, sw: 6, f, maxW: 980 });
    pill(1166, 800, 100, o.link, d.link || 'letsquiz.uk/play', 66);
    pill(1254, 660, 80, o.code, `Game code: ${d.code || 'WARMUP'}`, 50);
    text(x, closeOf(d), W / 2, 1318, 32, { c: o.foot || o.count || '#fff', stroke: o.countStroke, sw: 6, f, maxW: 980 });
  }
  /** Glowing neon text; col is the tube colour. */
  function neon(x, t, cx, cy, size, col, o = {}) {
    const font = o.f || HEAD, f = o.maxW ? fit(x, t, font, size, o.maxW) : { text: t, size }; x.save(); x.textAlign = o.a || 'center'; x.textBaseline = 'middle'; x.font = `${o.w || (font === HEAD ? 400 : 900)} ${f.size}px ${font}`;
    x.fillStyle = col; x.shadowColor = col; x.shadowBlur = 38; x.fillText(f.text, cx, cy); x.shadowBlur = 14; x.fillText(f.text, cx, cy); x.shadowBlur = 0; x.fillStyle = o.core || '#fff'; x.globalAlpha = .88; x.fillText(f.text, cx, cy); x.restore();
  }
  const neonRect = (x, a, b, w, h, r, col, lw = 6, fill = 'rgba(0,0,0,.42)') => { x.save(); rrect(x, a, b, w, h, r); x.fillStyle = fill; x.fill(); x.strokeStyle = col; x.lineWidth = lw; x.shadowColor = col; x.shadowBlur = 30; x.stroke(); x.shadowBlur = 12; x.stroke(); x.shadowBlur = 0; x.strokeStyle = '#fff'; x.globalAlpha = .75; x.lineWidth = lw * .35; x.stroke(); x.restore(); };

  // ── 3. Stage curtains: the leader on a gold card in the spotlight ────────────────────────────
  async function drawCurtain(d, topN) {
    const b = start(d, topN), { x, rows, places } = b;
    const g = x.createLinearGradient(0, 0, 0, H); g.addColorStop(0, '#2a050c'); g.addColorStop(1, '#5c0f1f'); x.fillStyle = g; x.fillRect(0, 0, W, H);
    const cone = x.createLinearGradient(0, 0, 0, 900); cone.addColorStop(0, 'rgba(255,236,170,.30)'); cone.addColorStop(1, 'rgba(255,236,170,0)'); x.fillStyle = cone; x.beginPath(); x.moveTo(490, 0); x.lineTo(590, 0); x.lineTo(960, 900); x.lineTo(120, 900); x.closePath(); x.fill();
    for (const side of [0, 1]) for (let i = 0; i < 4; i++) { const w = 20, xx = side ? W - (i + 1) * w : i * w, gg = x.createLinearGradient(xx, 0, xx + w, 0); gg.addColorStop(0, i % 2 ? '#7b1226' : '#b3203d'); gg.addColorStop(1, i % 2 ? '#b3203d' : '#5e0d1c'); x.fillStyle = gg; x.fillRect(xx, 0, w, H); }
    x.fillStyle = '#8f1730'; x.fillRect(0, 0, W, 24); for (let i = 0; i < 20; i++) { x.beginPath(); x.arc(28 + i * 56, 24, 28, 0, Math.PI); x.fillStyle = '#8f1730'; x.fill(); x.strokeStyle = '#e8b923'; x.lineWidth = 4; x.stroke(); }
    header(x, d, b, { brandY: 100, brand: { fill: '#e8b923', ink: '#2a050c' }, head: { c: '#ffe27a', stroke: '#2a050c', shadow: 24 }, sub: { c: '#ffe9c2', stroke: '#2a050c', sw: 6 }, tag: { c: '#fff', stroke: '#2a050c' } });
    const hero = rows[0], hh = b.n > 6 ? 200 : 250, hy = 436, hx = 130, hw = W - 260;
    if (hero) {
      x.save(); rrect(x, hx, hy, hw, hh, 36); const gg = x.createLinearGradient(0, hy, 0, hy + hh); gg.addColorStop(0, '#fff3b0'); gg.addColorStop(1, '#f2b81c'); x.fillStyle = gg; x.shadowColor = 'rgba(255,214,10,.55)'; x.shadowBlur = 50; x.fill(); x.shadowColor = 'transparent'; x.lineWidth = 8; x.strokeStyle = '#8a5a00'; x.stroke(); x.restore();
      const mid = hy + hh / 2 + 8;
      text(x, hero.emoji || '🙂', hx + 125, mid, hh * .5, { f: EMO }); text(x, '👑', hx + 125, hy + 4, 66, { f: EMO });
      text(x, d.ended ? 'CHAMPION' : 'IN THE LEAD', hx + 230, hy + hh * .2, hh * .12, { a: 'left', c: '#8a5a00', maxW: 300 });
      text(x, hero.name || 'Player', hx + 230, mid - hh * .06, hh * .3, { a: 'left', c: DEEP, maxW: hw - 270 });
      text(x, val(hero), hx + 230, mid + hh * .26, hh * .32, { a: 'left', f: HEAD, w: 400, c: '#7a1426', maxW: hw - 270 });
    }
    const rest = rows.slice(1), ry = hy + hh + 22, gp = 8, dh = Math.min(76, (b.top + b.zone - ry + 8 - gp * Math.max(0, rest.length - 1)) / Math.max(rest.length, 1));
    rest.forEach((p, k) => {
      const y = ry + k * (dh + gp), mid = y + dh / 2; x.save(); rrect(x, hx, y, hw, dh, dh / 2.4); x.fillStyle = 'rgba(255,248,230,.95)'; x.shadowColor = 'rgba(0,0,0,.4)'; x.shadowBlur = 14; x.shadowOffsetY = 5; x.fill(); x.restore();
      x.beginPath(); x.arc(hx + dh / 2 + 6, mid, dh * .36, 0, 7); x.fillStyle = '#8f1730'; x.fill(); text(x, String(places[k + 1]), hx + dh / 2 + 6, mid + 1, dh * .42, { f: HEAD, w: 400, c: '#ffe27a' });
      text(x, p.emoji || '🙂', hx + dh + 40, mid, dh * .56, { f: EMO }); text(x, p.name || 'Player', hx + dh + 82, mid, dh * .44, { a: 'left', c: DEEP, maxW: hw - dh - 300 });
      text(x, val(p), hx + hw - 28, mid, dh * .5, { a: 'right', f: HEAD, w: 400, c: p.score < 0 ? '#c0283f' : '#8f1730', maxW: 240 });
    });
    footer(x, d, { link: { fill: '#fff6d6', line: '#e8b923', ink: '#5c0f1f' }, code: { fill: '#e8b923', line: '#2a050c', ink: '#2a050c' }, count: '#ffe9c2', countStroke: '#2a050c' });
    return b.c;
  }

  // ── 4. Chalkboard ─────────────────────────────────────────────────────────────────────────────
  async function drawChalk(d, topN) {
    const b = start(d, topN), { x, rows, places } = b, r = seeded(21), CH = '#f4f1e6', CY = '#f7e27a';
    x.fillStyle = '#5a3a1e'; x.fillRect(0, 0, W, H);
    for (let i = 0; i < 130; i++) { x.globalAlpha = .08 + r() * .1; x.fillStyle = r() > .5 ? '#2e1c0a' : '#8a6238'; x.fillRect(r() * W, 0, 1 + r() * 3, H); } x.globalAlpha = 1;
    x.save(); rrect(x, 34, 34, W - 68, H - 68, 18); const g = x.createLinearGradient(0, 0, W, H); g.addColorStop(0, '#264638'); g.addColorStop(1, '#17302a'); x.fillStyle = g; x.shadowColor = 'rgba(0,0,0,.6)'; x.shadowBlur = 30; x.fill(); x.restore();
    for (let i = 0; i < 45; i++) { x.globalAlpha = .025 + r() * .04; x.fillStyle = '#fff'; x.beginPath(); x.ellipse(r() * W, r() * H, 80 + r() * 160, 20 + r() * 50, r() * 3, 0, 7); x.fill(); } x.globalAlpha = 1;
    const chalk = (t, cx, cy, size, o = {}) => { text(x, t, cx, cy, size, { f: HAND, ...o, c: o.c || CH }); x.globalAlpha = .45; text(x, t, cx + 1.5, cy + 1, size, { f: HAND, ...o, c: o.c || CH }); x.globalAlpha = 1; };
    x.save(); x.setLineDash([12, 8]); x.lineWidth = 4; x.strokeStyle = CY; rrect(x, W / 2 - 165, 44, 330, 68, 34); x.stroke(); x.restore(); chalk("LET'S QUIZ!", W / 2, 80, 38, { c: CY });
    chalk(headingOf(d), W / 2, 188, 108, { maxW: 920 });
    x.save(); x.strokeStyle = CY; x.lineWidth = 5; x.lineCap = 'round'; x.beginPath(); for (let i = 0; i <= 40; i++) { const px = 200 + i * 17, py = 252 + Math.sin(i * .9) * 6; i ? x.lineTo(px, py) : x.moveTo(px, py); } x.stroke(); x.restore();
    wrap(x, cap1(d.title), HAND, 38, 880, 2).forEach((l, i) => chalk(l, W / 2, 302 + i * 46, 38, { c: '#aee0ff', maxW: 900 }));
    chalk(tagOf(d, rows), W / 2, 394, 48, { c: CY, maxW: 900 });
    const { dh, gap, y0 } = geo(b, 96, 8);
    rows.forEach((p, k) => {
      const y = y0 + k * (dh + gap), mid = y + dh / 2, size = Math.min(dh * .56, 54), nm = String(p.name || 'Player'), sc = val(p), nmW = Math.min(mw(x, nm, HAND, size), 400), scW = mw(x, sc, HAND, size);
      if (k === 0) { x.save(); x.translate(W / 2, mid); x.rotate(-.006); x.strokeStyle = CY; x.lineWidth = 4; x.setLineDash([]); rrect(x, -440, -dh / 2 - 2, 880, dh + 4, dh / 2.2); x.stroke(); x.restore(); }
      chalk(places[k] + '.', 120, mid, size, { c: CY, a: 'left' }); text(x, p.emoji || '🙂', 215, mid, size * .95, { f: EMO }); chalk(nm, 265, mid, size, { a: 'left', maxW: 400 });
      x.save(); x.fillStyle = 'rgba(244,241,230,.55)'; for (let dx = 265 + nmW + 22; dx < 960 - scW - 24; dx += 14) { x.beginPath(); x.arc(dx, mid + size * .3, 2.2, 0, 7); x.fill(); } x.restore();
      chalk(sc, 960, mid, size, { a: 'right', c: p.score < 0 ? '#ff9a9a' : CY, maxW: 300 });
    });
    footer(x, d, { link: { fill: CH, line: CY, lw: 5, ink: '#17302a' }, code: { fill: CY, line: '#17302a', lw: 4, ink: '#17302a' }, count: CH, foot: '#aee0ff', f: HAND });
    return b.c;
  }

  // ── 5. Newspaper front page ───────────────────────────────────────────────────────────────────
  async function drawNews(d, topN) {
    const b = start(d, topN), { x, rows, places } = b, r = seeded(8), INK = '#1a1612', PAPER = '#f1e7cf';
    x.fillStyle = PAPER; x.fillRect(0, 0, W, H);
    for (let i = 0; i < 2600; i++) { x.globalAlpha = .04 + r() * .07; x.fillStyle = r() > .5 ? '#8a7448' : '#fff'; x.fillRect(r() * W, r() * H, 1 + r() * 2, 1 + r() * 2); } x.globalAlpha = 1;
    text(x, 'THE QUIZ GAZETTE', W / 2, 108, 98, { f: SERIF, c: INK, maxW: 940 });
    x.fillStyle = INK; x.fillRect(60, 164, W - 120, 5); x.fillRect(60, 175, W - 120, 2);
    text(x, `${new Date().toLocaleDateString('en-GB', { weekday: 'long', day: 'numeric', month: 'long', year: 'numeric' }).toUpperCase()}  ·  LET'S QUIZ!  ·  FREE ON YOUR PHONE`, W / 2, 204, 23, { f: SERIF, w: 700, c: INK, maxW: 960 });
    x.fillRect(60, 226, W - 120, 2);
    const lead = clip(leadOf(rows), 14).toUpperCase(), hl = !rows.length ? 'NOBODY HAS PLAYED YET' : d.ended ? `${lead} TAKES THE CROWN` : `${lead} LEADS THE WAY`;
    text(x, hl, W / 2, 300, Math.max(44, Math.min(84, 960 / (hl.length * .7))), { f: SERIF, c: INK, maxW: 960 });
    text(x, `${headingOf(d)}  ·  ${cap1(d.title).toUpperCase()}`, W / 2, 372, 30, { f: SERIF, w: 700, c: '#5a4a30', maxW: 960 });
    x.fillRect(60, 404, W - 120, 3);
    // the "photo" and a pull quote on the left
    if (rows[0]) {
      x.save(); x.fillStyle = '#d9cdb0'; x.fillRect(60, 440, 340, 340); x.beginPath(); x.rect(60, 440, 340, 340); x.clip(); x.fillStyle = 'rgba(26,22,18,.22)'; for (let gy = 450; gy < 780; gy += 14) for (let gx = 60 + ((gy / 14) % 2 ? 7 : 0); gx < 400; gx += 14) { x.beginPath(); x.arc(gx, gy, 3.2, 0, 7); x.fill(); } x.restore();
      text(x, rows[0].emoji || '🙂', 230, 612, 190, { f: EMO }); x.strokeStyle = INK; x.lineWidth = 4; x.strokeRect(60, 440, 340, 340);
      text(x, `${rows[0].name}, ${d.ended ? 'the winner' : 'in front'}`, 230, 806, 24, { f: SERIF, w: 700, c: INK, maxW: 340 });
      const gap = rows.length > 1 ? rows[0].score - rows[1].score : 0, q = !rows.length ? '' : rows.length > 1 && gap > 0 ? `“Can anyone get within ${fmt(gap)} of ${rows[0].name}?”` : `“Can you beat ${val(rows[0])}?”`;
      x.fillRect(60, 836, 340, 3); wrap(x, q, SERIF, 36, 330, 5).forEach((l, i) => text(x, l, 230, 884 + i * 46, 36, { f: SERIF, c: INK, maxW: 340 })); x.fillRect(60, 1052, 340, 3);
    }
    // the table
    const { dh, y0 } = geo(b, 82, 0, 56);
    rows.forEach((p, k) => {
      const y = y0 + k * dh, mid = y + dh / 2, size = Math.min(dh * .5, 42), nm = String(p.name || 'Player'), sc = val(p), nmW = Math.min(mw(x, nm, SERIF, size), 290), scW = mw(x, sc, SERIF, size);
      if (k) { x.fillStyle = 'rgba(26,22,18,.35)'; x.fillRect(440, y, 580, 1.5); }
      text(x, String(places[k]), 462, mid, size * 1.1, { f: SERIF, c: INK }); text(x, p.emoji || '🙂', 526, mid, size * .95, { f: EMO }); text(x, nm, 572, mid, size, { a: 'left', f: SERIF, c: INK, maxW: 290 });
      x.fillStyle = 'rgba(26,22,18,.5)'; for (let dx = 572 + nmW + 14; dx < 1010 - scW - 16; dx += 11) x.fillRect(dx, mid + size * .3, 2.2, 2.2);
      text(x, sc, 1010, mid, size, { a: 'right', f: SERIF, c: p.score < 0 ? '#9b1c1c' : INK, maxW: 250 });
    });
    footer(x, d, { link: { fill: INK, line: INK, lw: 3, ink: PAPER }, code: { fill: PAPER, line: INK, lw: 5, ink: INK, noShadow: true }, count: INK, f: SERIF });
    return b.c;
  }

  // ── 6. Arcade high-score table ───────────────────────────────────────────────────────────────
  async function drawArcade(d, topN) {
    const b = start(d, topN), { x, rows, places } = b, r = seeded(33);
    x.fillStyle = '#07010f'; x.fillRect(0, 0, W, H);
    const gl = x.createRadialGradient(W / 2, 640, 40, W / 2, 640, 820); gl.addColorStop(0, 'rgba(120,40,200,.35)'); gl.addColorStop(1, 'rgba(120,40,200,0)'); x.fillStyle = gl; x.fillRect(0, 0, W, H);
    x.strokeStyle = 'rgba(180,90,255,.16)'; x.lineWidth = 2; for (let gx = 0; gx <= W; gx += 60) { x.beginPath(); x.moveTo(gx, 0); x.lineTo(gx, H); x.stroke(); } for (let gy = 0; gy <= H; gy += 60) { x.beginPath(); x.moveTo(0, gy); x.lineTo(W, gy); x.stroke(); }
    for (let i = 0; i < 50; i++) { x.globalAlpha = .3 + r() * .6; sparkle(x, r() * W, r() * H, 3 + r() * 6, 0, NEON[i % NEON.length]); } x.globalAlpha = 1;
    neonRect(x, W / 2 - 165, 44, 330, 68, 34, '#ffd60a', 5); neon(x, "LET'S QUIZ!", W / 2, 80, 38, '#ffd60a', { f: MONO, w: 900 });
    neon(x, headingOf(d), W / 2, 190, 118, '#ff4fd8', { maxW: 960 });
    wrap(x, cap1(d.title).toUpperCase(), MONO, 36, 900, 2).forEach((l, i) => text(x, l, W / 2, 272 + i * 44, 36, { f: MONO, c: '#fff', maxW: 940 }));
    neon(x, !rows.length ? 'INSERT COIN' : d.ended ? 'GAME OVER · THANKS FOR PLAYING' : 'CAN YOU BEAT THE TOP SCORE?', W / 2, 372, 42, '#34d3ff', { f: MONO, w: 900, maxW: 940 });
    const { dh, gap, y0 } = geo(b, 84, 10);
    rows.forEach((p, k) => {
      const y = y0 + k * (dh + gap), mid = y + dh / 2, size = Math.min(dh * .6, 50), col = NEON[(places[k] - 1) % NEON.length], nm = clip(String(p.name || 'Player').toUpperCase(), 14), sc = val(p);
      const nmW = mw(x, nm, MONO, size), scW = mw(x, sc, MONO, size);
      neon(x, ord(places[k]).toUpperCase(), 80, mid, size, col, { a: 'left', f: MONO, w: 900 }); text(x, p.emoji || '🙂', 230, mid, size * .95, { f: EMO }); neon(x, nm, 280, mid, size, col, { a: 'left', f: MONO, w: 900, maxW: 440, core: '#fff' });
      x.fillStyle = col; x.globalAlpha = .6; for (let dx = 280 + Math.min(nmW, 440) + 16; dx < 1000 - scW - 16; dx += 16) x.fillRect(dx, mid + size * .28, 5, 5); x.globalAlpha = 1;
      neon(x, sc, 1000, mid, size, p.score < 0 ? '#ff5c7a' : col, { a: 'right', f: MONO, w: 900, maxW: 330 });
    });
    x.fillStyle = 'rgba(0,0,0,.22)'; for (let sy = 0; sy < H; sy += 4) x.fillRect(0, sy, W, 1.5);
    footer(x, d, { link: { fill: '#0a0620', line: '#34d3ff', ink: '#fff', glow: '#34d3ff' }, code: { fill: '#ffd60a', line: '#07010f', lw: 4, ink: '#07010f', glow: '#ffd60a' }, count: '#cfa8ff', f: MONO });
    return b.c;
  }

  // ── 7. Split-flap board ───────────────────────────────────────────────────────────────────────
  function flap(x, ch, cx, cy, w, h, col = '#f4f0e4') {
    x.save(); rrect(x, cx - w / 2, cy - h / 2, w, h, Math.min(8, w / 5)); const g = x.createLinearGradient(0, cy - h / 2, 0, cy + h / 2); g.addColorStop(0, '#3d414b'); g.addColorStop(.5, '#2a2d34'); g.addColorStop(.5, '#202329'); g.addColorStop(1, '#2d3138'); x.fillStyle = g; x.shadowColor = 'rgba(0,0,0,.55)'; x.shadowBlur = 8; x.shadowOffsetY = 3; x.fill(); x.restore();
    if (ch.trim()) text(x, ch, cx, cy + h * .03, h * .68, { f: HEAD, w: 400, c: col }); x.fillStyle = 'rgba(0,0,0,.7)'; x.fillRect(cx - w / 2, cy - 1.3, w, 2.6);
  }
  async function drawFlap(d, topN) {
    const b = start(d, topN), { x, rows, places } = b;
    const g = x.createLinearGradient(0, 0, 0, H); g.addColorStop(0, '#202329'); g.addColorStop(1, '#101215'); x.fillStyle = g; x.fillRect(0, 0, W, H);
    for (const [bx, by] of [[34, 34], [W - 34, 34], [34, H - 34], [W - 34, H - 34]]) { x.beginPath(); x.arc(bx, by, 9, 0, 7); x.fillStyle = '#4a4f5a'; x.fill(); }
    x.save(); rrect(x, W / 2 - 165, 44, 330, 68, 34); x.fillStyle = YELLOW; x.fill(); x.restore(); text(x, "LET'S QUIZ!", W / 2, 80, 40, { c: '#101215' });
    const hd = [...headingOf(d).toUpperCase()], tw = Math.min(70, 960 / hd.length), th = Math.min(100, tw * 1.4), full = hd.reduce((s, ch) => s + (ch === ' ' ? tw * .5 : tw + 4), 0); let hx = (W - full) / 2;
    for (const ch of hd) { if (ch === ' ') { hx += tw * .5; continue; } flap(x, ch, hx + tw / 2, 190, tw, th, YELLOW); hx += tw + 4; }
    wrap(x, cap1(d.title).toUpperCase(), BODY, 36, 900, 2).forEach((l, i) => text(x, l, W / 2, 292 + i * 44, 36, { c: '#c9ccd4', maxW: 940 }));
    text(x, tagOf(d, rows), W / 2, 380, 48, { c: YELLOW, maxW: 940 });
    const { dh, gap, y0 } = geo(b, 84, 10), fh = dh * .88;
    rows.forEach((p, k) => {
      const mid = y0 + k * (dh + gap) + dh / 2, rk = String(places[k]), nm = [...clip(String(p.name || 'Player').toUpperCase(), 12)], sc = [...val(p)];
      const nw = Math.min(46, 400 / Math.max(nm.length, 1)), sw = Math.min(46, 330 / sc.length);
      rk.split('').forEach((ch, i) => flap(x, ch, 92 + i * 54, mid, 50, fh, k === 0 ? YELLOW : '#f4f0e4')); text(x, p.emoji || '🙂', 196 + (rk.length - 1) * 27, mid, fh * .8, { f: EMO });
      nm.forEach((ch, i) => flap(x, ch, 260 + (rk.length - 1) * 27 + nw / 2 + i * (nw + 3), mid, nw, fh * .96));
      sc.forEach((ch, i) => flap(x, ch, 1020 - sw / 2 - (sc.length - 1 - i) * (sw + 3), mid, sw, fh, p.score < 0 ? '#ff7a7a' : k === 0 ? YELLOW : '#f4f0e4'));
    });
    footer(x, d, { link: { fill: '#f4f0e4', line: YELLOW, ink: '#101215' }, code: { fill: YELLOW, line: '#101215', ink: '#101215' }, count: '#c9ccd4' });
    return b.c;
  }

  // ── 8. Race track ─────────────────────────────────────────────────────────────────────────────
  async function drawRace(d, topN) {
    const b = start(d, topN), { x, rows, places } = b, r = seeded(14);
    const sky = x.createLinearGradient(0, 0, 0, 420); sky.addColorStop(0, '#5db8f0'); sky.addColorStop(1, '#cdeeff'); x.fillStyle = sky; x.fillRect(0, 0, W, H);
    for (let i = 0; i < 6; i++) { const cx = 80 + r() * 920, cy = 40 + r() * 330; x.fillStyle = 'rgba(255,255,255,.8)'; for (const [dx, dy, rr] of [[0, 0, 34], [38, -10, 42], [80, 4, 32], [40, 14, 34]]) { x.beginPath(); x.arc(cx + dx, cy + dy, rr, 0, 7); x.fill(); } }
    for (let i = 0; i < 12; i++) { x.fillStyle = i % 2 ? '#3f9b45' : '#4aa84a'; x.fillRect(0, 410 + i * 60, W, 60); }
    x.fillStyle = '#2d7a39'; x.fillRect(0, 1066, W, H - 1066);
    header(x, d, b, { brand: { fill: '#fff', ink: '#12406e' }, head: { c: '#fff', stroke: '#12406e', shadow: 20 }, sub: { c: '#12406e' }, tag: false });
    text(x, tagOf(d, rows), W / 2, 372, 50, { c: '#fff', stroke: '#12406e', sw: 9, maxW: 940 });
    const { dh, gap, y0 } = geo(b, 100, 8), max = Math.max(...rows.map((p) => p.score), 1), x0 = 380, x1 = 925;
    rows.forEach((p, k) => {
      const y = y0 + k * (dh + gap), mid = y + dh / 2, size = dh * .7;
      x.save(); rrect(x, 60, y, 960, dh, dh / 2.6); x.fillStyle = '#c96a3b'; x.shadowColor = 'rgba(0,0,0,.35)'; x.shadowBlur = 12; x.shadowOffsetY = 5; x.fill(); x.restore();
      x.save(); x.setLineDash([22, 18]); x.strokeStyle = 'rgba(255,255,255,.55)'; x.lineWidth = 3; x.beginPath(); x.moveTo(350, y + dh - 6); x.lineTo(955, y + dh - 6); x.stroke(); x.restore();
      x.save(); rrect(x, 66, y + 6, 280, dh - 12, (dh - 12) / 2.4); x.fillStyle = '#fff'; x.fill(); x.restore();
      text(x, String(places[k]), 100, mid, dh * .5, { f: HEAD, w: 400, c: '#c96a3b' }); text(x, p.name || 'Player', 138, mid, dh * .4, { a: 'left', c: '#12406e', maxW: 196 });
      for (let q = 0; q < Math.ceil(dh / 14); q++) for (let s = 0; s < 3; s++) { x.fillStyle = (q + s) % 2 ? '#111' : '#fff'; x.fillRect(965 + s * 14, y + q * 14, 14, Math.min(14, dh - q * 14)); }
      const px = x0 + (Math.max(0, p.score) / max) * (x1 - x0), sc = val(p), sw = mw(x, sc, HEAD, dh * .46, 400);
      const onLeft = px - 30 - sw > 360; text(x, sc, onLeft ? px - dh * .45 : px + dh * .45, mid, dh * .46, { a: onLeft ? 'right' : 'left', f: HEAD, w: 400, c: '#fff', stroke: '#6b2d14', sw: 7 });
      text(x, p.emoji || '🙂', px, mid + 2, size, { f: EMO }); if (k === 0) text(x, '🏆', Math.min(px + 4, 920), y - 4, dh * .42, { f: EMO });
    });
    text(x, '🏁', 980, b.top - 8, 52, { f: EMO });
    footer(x, d, { link: { fill: '#fff', line: '#ffd60a', ink: '#12406e' }, code: { fill: '#ffd60a', line: '#12406e', ink: '#12406e' }, count: '#fff', countStroke: '#1b4d27' });
    return b.c;
  }

  // ── 9. Bar chart ──────────────────────────────────────────────────────────────────────────────
  async function drawBars(d, topN) {
    const b = start(d, topN), { x, rows, places } = b, COL = ['#5b3df5', '#ff4fd8', '#34b7f1', '#ff9f1c', '#2fbf71', '#ff6b4a', '#9b6bff', '#17a2a2'];
    x.fillStyle = '#fff7e6'; x.fillRect(0, 0, W, H); x.fillStyle = 'rgba(91,61,245,.06)'; x.beginPath(); x.arc(W, 0, 520, 0, 7); x.fill(); x.beginPath(); x.arc(0, H, 460, 0, 7); x.fill();
    header(x, d, b, { brand: { fill: PURPLE, ink: '#fff' }, head: { c: '#2b1a8a' }, sub: { c: '#5a4f93' }, tag: { c: '#e0457b', sw: 0 } });
    const base = 1000, maxH = 420, n = Math.max(b.n, 1), slot = Math.min(180, 960 / n), cw = slot * .74, left = (W - slot * n) / 2, max = Math.max(...rows.map((p) => p.score), 1);
    x.strokeStyle = '#eadbb8'; x.lineWidth = 2; x.setLineDash([10, 10]); for (let i = 1; i <= 4; i++) { const gy = base - (maxH * i) / 4; x.beginPath(); x.moveTo(60, gy); x.lineTo(W - 60, gy); x.stroke(); } x.setLineDash([]);
    x.fillStyle = '#c9b78a'; x.fillRect(50, base, W - 100, 5);
    rows.forEach((p, k) => {
      const cx = left + slot * k + slot / 2, h = 46 + (Math.max(0, p.score) / max) * (maxH - 46), top = base - h;
      x.save(); rrect(x, cx - cw / 2, top, cw, h + 8, 18); const g = x.createLinearGradient(0, top, 0, base); const c = k === 0 ? ['#ffe14d', '#f5a800'] : [COL[k % COL.length], COL[k % COL.length]]; g.addColorStop(0, c[0]); g.addColorStop(1, c[1]); x.fillStyle = g; x.shadowColor = 'rgba(40,20,100,.25)'; x.shadowBlur = 18; x.shadowOffsetY = 8; x.fill(); x.restore();
      x.save(); x.beginPath(); x.rect(cx - cw / 2, top, cw, h); x.clip(); x.fillStyle = 'rgba(255,255,255,.18)'; x.fillRect(cx - cw / 2 + 10, top, cw * .16, h); x.restore();
      text(x, String(places[k]), cx, base - 34, Math.min(66, cw * .55), { f: HEAD, w: 400, c: k === 0 ? '#7a4a00' : 'rgba(255,255,255,.95)' });
      text(x, val(p), cx, top - 26, Math.min(44, slot * .3), { f: HEAD, w: 400, c: p.score < 0 ? '#d94b5f' : '#2b1a8a', maxW: slot + 10 });
      text(x, p.emoji || '🙂', cx, top - 82, Math.min(70, slot * .46), { f: EMO }); if (k === 0) text(x, '👑', cx, top - 138, 56, { f: EMO });
      text(x, p.name || 'Player', cx, base + 34, Math.min(32, slot * .22), { c: '#2b1a8a', maxW: slot - 4 });
    });
    footer(x, d, { link: { fill: PURPLE, line: PINK, ink: '#fff' }, code: { fill: YELLOW, line: DEEP, ink: DEEP }, count: '#5a4f93' });
    return b.c;
  }

  // ── 10. League table ──────────────────────────────────────────────────────────────────────────
  async function drawLeague(d, topN) {
    const b = start(d, topN), { x, rows, places } = b;
    for (let i = 0; i < 23; i++) { x.fillStyle = i % 2 ? '#1b6f37' : '#217d3f'; x.fillRect(0, i * 60, W, 60); }
    x.strokeStyle = 'rgba(255,255,255,.16)'; x.lineWidth = 5; x.beginPath(); x.arc(W / 2, 745, 210, 0, 7); x.stroke(); x.beginPath(); x.moveTo(0, 745); x.lineTo(W, 745); x.stroke();
    header(x, d, b, { brand: { fill: '#fff', ink: '#0f3d22' }, head: { c: '#fff', stroke: '#0f3d22', shadow: 20 }, sub: { c: '#eaffef', stroke: '#0f3d22', sw: 6 }, tag: { c: '#ffe14d', stroke: '#0f3d22' } });
    const hh = 58, rh = Math.min(86, (b.zone - hh) / Math.max(b.n, 1)), tot = hh + rh * b.n, y0 = b.top + (b.zone - tot) / 2 + 6;
    x.save(); rrect(x, 60, y0, 960, tot, 24); x.fillStyle = '#fff'; x.shadowColor = 'rgba(0,0,0,.45)'; x.shadowBlur = 30; x.shadowOffsetY = 12; x.fill(); x.restore();
    x.save(); rrect(x, 60, y0, 960, tot, 24); x.clip(); x.fillStyle = '#0f3d22'; x.fillRect(60, y0, 960, hh);
    rows.forEach((p, k) => { const y = y0 + hh + k * rh; x.fillStyle = k % 2 ? '#eef6f0' : '#fff'; x.fillRect(60, y, 960, rh); x.fillStyle = k === 0 ? '#f2b81c' : places[k] <= 3 ? '#2e7dff' : 'rgba(0,0,0,0)'; x.fillRect(60, y, 14, rh); }); x.restore();
    text(x, 'POS', 120, y0 + hh / 2, 26, { c: '#9fe3b5' }); text(x, 'PLAYER', 250, y0 + hh / 2, 26, { a: 'left', c: '#9fe3b5' }); text(x, 'POINTS', 990, y0 + hh / 2, 26, { a: 'right', c: '#9fe3b5' });
    rows.forEach((p, k) => {
      const mid = y0 + hh + k * rh + rh / 2, size = Math.min(rh * .5, 44);
      text(x, String(places[k]), 120, mid, size * 1.1, { f: HEAD, w: 400, c: '#0f3d22' }); text(x, p.emoji || '🙂', 200, mid, size * .95, { f: EMO }); text(x, p.name || 'Player', 250, mid, size, { a: 'left', c: '#0f3d22', maxW: 520 });
      text(x, val(p), 990, mid, size * 1.1, { a: 'right', f: HEAD, w: 400, c: p.score < 0 ? '#c0283f' : '#0f3d22', maxW: 260 });
    });
    footer(x, d, { link: { fill: '#fff', line: '#ffe14d', ink: '#0f3d22' }, code: { fill: '#ffe14d', line: '#0f3d22', ink: '#0f3d22' }, count: '#fff', countStroke: '#0f3d22' });
    return b.c;
  }

  // ── 11. Cinema tickets ────────────────────────────────────────────────────────────────────────
  async function drawTickets(d, topN) {
    const b = start(d, topN), { x, rows, places } = b, r = seeded(5);
    const g = x.createLinearGradient(0, 0, 0, H); g.addColorStop(0, '#25060d'); g.addColorStop(1, '#4d101e'); x.fillStyle = g; x.fillRect(0, 0, W, H);
    const bm = x.createLinearGradient(0, 0, 0, 900); bm.addColorStop(0, 'rgba(255,220,140,.22)'); bm.addColorStop(1, 'rgba(255,220,140,0)'); x.fillStyle = bm; x.beginPath(); x.moveTo(380, 0); x.lineTo(700, 0); x.lineTo(1000, 900); x.lineTo(80, 900); x.closePath(); x.fill();
    for (let i = 0; i < 40; i++) { x.globalAlpha = .3 + r() * .5; sparkle(x, 70 + r() * 940, r() * H, 3 + r() * 5, 0, '#ffe27a'); } x.globalAlpha = 1;
    for (const side of [0, 1]) { x.fillStyle = '#12030a'; x.fillRect(side ? W - 40 : 0, 0, 40, H); x.fillStyle = '#f3dcab'; for (let y = 14; y < H; y += 44) { rrect(x, (side ? W - 40 : 0) + 11, y, 18, 26, 4); x.fill(); } }
    header(x, d, b, { brand: { fill: '#e8b923', ink: '#25060d' }, head: { c: '#ffe27a', stroke: '#25060d', shadow: 24 }, sub: { c: '#f6e7c4', stroke: '#25060d', sw: 6 }, tag: { c: '#fff', stroke: '#25060d' } });
    const { dh, gap, y0 } = geo(b, 104, 14, 50), a = 80, w = 920;
    rows.forEach((p, k) => {
      const y = y0 + k * (dh + gap), mid = y + dh / 2, nr = dh * .2, stub = w * .23, first = k === 0;
      x.save(); x.translate(W / 2, mid); x.rotate(k % 2 ? .008 : -.008); x.translate(-W / 2, -mid);
      x.beginPath(); x.moveTo(a, y); x.lineTo(a + w, y); x.lineTo(a + w, mid - nr); x.arc(a + w, mid, nr, -Math.PI / 2, Math.PI / 2, true); x.lineTo(a + w, y + dh); x.lineTo(a, y + dh); x.lineTo(a, mid + nr); x.arc(a, mid, nr, Math.PI / 2, -Math.PI / 2, true); x.closePath();
      const gg = x.createLinearGradient(0, y, 0, y + dh); gg.addColorStop(0, first ? '#ffe98a' : '#f8ecd0'); gg.addColorStop(1, first ? '#e0a010' : '#e3cf9f'); x.fillStyle = gg; x.shadowColor = 'rgba(0,0,0,.5)'; x.shadowBlur = 16; x.shadowOffsetY = 8; x.fill(); x.shadowColor = 'transparent';
      x.setLineDash([7, 7]); x.strokeStyle = 'rgba(80,40,20,.45)'; x.lineWidth = 3; x.beginPath(); x.moveTo(a + w - stub, y + 10); x.lineTo(a + w - stub, y + dh - 10); x.stroke(); x.setLineDash([]);
      const ink = first ? '#4a2a00' : '#4d101e', size = Math.min(dh * .46, 50);
      text(x, String(places[k]), a + 66, mid, dh * .62, { f: HEAD, w: 400, c: first ? '#8a5a00' : '#b3203d' }); text(x, p.emoji || '🙂', a + 150, mid, dh * .56, { f: EMO }); text(x, p.name || 'Player', a + 200, mid, size, { a: 'left', c: ink, maxW: w - stub - 230 });
      text(x, 'ADMIT ONE', a + w - stub / 2, y + dh * .22, Math.max(13, dh * .15), { c: first ? '#8a5a00' : '#9a7a5a' }); text(x, val(p), a + w - stub / 2, mid + dh * .1, dh * .44, { f: HEAD, w: 400, c: p.score < 0 ? '#c0283f' : ink, maxW: stub - 24 });
      x.restore();
    });
    footer(x, d, { link: { fill: '#f8ecd0', line: '#e8b923', ink: '#4d101e' }, code: { fill: '#e8b923', line: '#25060d', ink: '#25060d' }, count: '#f3d9a0', countStroke: '#25060d' });
    return b.c;
  }

  // ── 12. Comic pop-art ─────────────────────────────────────────────────────────────────────────
  async function drawComic(d, topN) {
    const b = start(d, topN), { x, rows, places } = b, lead = rows[0], POW = ['POW!', 'WOW!', 'ZAP!', 'BAM!', 'BOOM!'];
    x.fillStyle = '#ffd60a'; x.fillRect(0, 0, W, H); x.fillStyle = '#ff9f0a';
    for (let gy = 0; gy < H + 30; gy += 30) for (let gx = (gy / 30) % 2 ? 15 : 0; gx < W + 30; gx += 30) { const rr = Math.max(0, 12 * (1 - Math.hypot(gx - W, gy - H) / 1500)); if (rr > .8) { x.beginPath(); x.arc(gx, gy, rr, 0, 7); x.fill(); } }
    x.fillStyle = '#ff4f9a'; for (let gy = 0; gy < 500; gy += 30) for (let gx = (gy / 30) % 2 ? 15 : 0; gx < 600; gx += 30) { const rr = Math.max(0, 10 * (1 - Math.hypot(gx, gy) / 640)); if (rr > .8) { x.beginPath(); x.arc(gx, gy, rr, 0, 7); x.fill(); } }
    x.save(); rrect(x, W / 2 - 165, 44, 330, 68, 12); x.fillStyle = '#111'; x.fill(); x.restore(); text(x, "LET'S QUIZ!", W / 2, 80, 40, { c: '#ffd60a' });
    const hd = headingOf(d), f = fit(x, hd, HEAD, 128, 960); x.save(); x.font = `400 ${f.size}px ${HEAD}`; x.textAlign = 'center'; x.textBaseline = 'middle'; x.lineJoin = 'round'; x.fillStyle = '#111'; x.fillText(f.text, W / 2 + 9, 199); x.lineWidth = f.size * .14; x.strokeStyle = '#111'; x.strokeText(f.text, W / 2, 190); x.fillStyle = '#fff'; x.fillText(f.text, W / 2, 190); x.restore();
    x.save(); x.translate(W / 2, 286); x.rotate(-.012); rrect(x, -440, -34, 880, 68, 6); x.fillStyle = '#fff'; x.fill(); x.lineWidth = 6; x.strokeStyle = '#111'; x.stroke(); x.restore(); text(x, cap1(d.title), W / 2, 288, 38, { c: '#111', maxW: 840 });
    text(x, tagOf(d, rows), 440, 372, 50, { c: '#ff2d6f', stroke: '#111', sw: 10, maxW: 740 });
    const { dh, gap, y0 } = geo(b, 108, 16, 50), cols = ['#ff2d6f', '#34d3ff', '#7dff6b', '#b18cff', '#ff8a3d', '#ffd60a'];
    rows.forEach((p, k) => {
      const mid = y0 + k * (dh + gap) + dh / 2, size = Math.min(dh * .5, 52);
      x.save(); x.translate(W / 2, mid); x.rotate(k % 2 ? .005 : -.005);
      rrect(x, -464, -dh / 2 + 9, 940, dh, 14); x.fillStyle = '#111'; x.fill(); rrect(x, -470, -dh / 2, 940, dh, 14); x.fillStyle = '#fff'; x.fill(); x.lineWidth = 7; x.strokeStyle = '#111'; x.stroke();
      burst(x, -470 + dh * .62, 0, dh * .3, dh * .5, 10, .2); x.fillStyle = cols[k % cols.length]; x.fill(); x.lineWidth = 5; x.stroke(); text(x, String(places[k]), -470 + dh * .62, 2, dh * .46, { f: HEAD, w: 400, c: '#111' });
      text(x, p.emoji || '🙂', -470 + dh * 1.5, 0, size * 1.05, { f: EMO }); text(x, p.name || 'Player', -470 + dh * 2, 0, size, { a: 'left', c: '#111', maxW: 560 });
      text(x, val(p), 440, 2, size * 1.15, { a: 'right', f: HEAD, w: 400, c: p.score < 0 ? '#d90429' : '#ff2d6f', stroke: '#111', sw: size * .12, maxW: 300 }); x.restore();
    });
    if (lead) { x.save(); x.translate(925, 362); x.rotate(.2); burst(x, 0, 0, 46, 70, 12); x.fillStyle = '#ff2d6f'; x.fill(); x.lineWidth = 6; x.strokeStyle = '#111'; x.stroke(); text(x, POW[(lead.name || 'x').length % POW.length], 0, 3, 36, { f: HEAD, w: 400, c: '#fff', stroke: '#111', sw: 8 }); x.restore(); }
    footer(x, d, { link: { fill: '#fff', line: '#111', lw: 7, ink: '#111' }, code: { fill: '#ff2d6f', line: '#111', lw: 6, ink: '#fff' }, count: '#111', countStroke: '#fff', foot: '#111' });
    return b.c;
  }

  // ── 13. Beer mats on a pub table ──────────────────────────────────────────────────────────────
  async function drawMats(d, topN) {
    const b = start(d, topN), { x, rows, places } = b, r = seeded(17), RING = ['#d99a00', '#9aa6b8', '#b8662d', '#2f7d4f', '#b3203d', '#2b5fa8', '#7a3d9b', '#c2570c'];
    for (let i = 0; i < 9; i++) { x.fillStyle = i % 2 ? '#8a5a2b' : '#7d5126'; x.fillRect(0, i * 150, W, 150); x.fillStyle = 'rgba(0,0,0,.35)'; x.fillRect(0, i * 150, W, 4); }
    for (let i = 0; i < 220; i++) { x.globalAlpha = .08 + r() * .1; x.fillStyle = r() > .5 ? '#3a2410' : '#b98a55'; x.fillRect(r() * W, r() * H, 60 + r() * 220, 1 + r() * 2); } x.globalAlpha = 1;
    const vg = x.createRadialGradient(W / 2, H / 2, 300, W / 2, H / 2, 900); vg.addColorStop(0, 'rgba(0,0,0,0)'); vg.addColorStop(1, 'rgba(0,0,0,.45)'); x.fillStyle = vg; x.fillRect(0, 0, W, H);
    header(x, d, b, { brand: { fill: '#f6ead0', ink: '#3b2410' }, head: { c: '#f6ead0', stroke: '#3b2410', shadow: 22 }, sub: { c: '#f6ead0', stroke: '#3b2410', sw: 6 }, tag: { c: '#ffd979', stroke: '#3b2410' } });
    const mat = (cx, cy, rad, k, p, big) => {
      x.save(); x.beginPath(); x.arc(cx, cy, rad, 0, 7); x.fillStyle = '#f6ead0'; x.shadowColor = 'rgba(0,0,0,.55)'; x.shadowBlur = 24; x.shadowOffsetY = 12; x.fill(); x.restore();
      x.beginPath(); x.arc(cx, cy, rad * .84, 0, 7); x.lineWidth = rad * .1; x.strokeStyle = RING[k % RING.length]; x.stroke();
      text(x, p.emoji || '🙂', cx, cy - rad * .3, rad * .5, { f: EMO }); text(x, p.name || 'Player', cx, cy + rad * .22, rad * .24, { c: '#3b2410', maxW: rad * 1.4 }); text(x, val(p), cx, cy + rad * .52, rad * .3, { f: HEAD, w: 400, c: p.score < 0 ? '#c0283f' : RING[k % RING.length], maxW: rad * 1.3 });
      x.beginPath(); x.arc(cx - rad * .7, cy - rad * .7, rad * .2, 0, 7); x.fillStyle = k === 0 ? '#e8b923' : '#3b2410'; x.fill(); x.lineWidth = 3; x.strokeStyle = '#f6ead0'; x.stroke(); text(x, String(places[k]), cx - rad * .7, cy - rad * .7 + 2, rad * .22, { f: HEAD, w: 400, c: k === 0 ? '#3b2410' : '#f6ead0' });
      if (big) text(x, '👑', cx, cy - rad - 8, 64, { f: EMO });
    };
    const many = b.n > 5, R1 = many ? 120 : 150, cy1 = many ? 570 : 610; if (rows[0]) mat(W / 2, cy1, R1, 0, rows[0], true);
    const rest = rows.slice(1), perRow = Math.min(4, rest.length) || 1, rad = many ? 84 : Math.min(112, 960 / perRow / 2 - 10);
    const place = (list, cy, off) => list.forEach((p, i) => mat(W / 2 + (i - (list.length - 1) / 2) * (rad * 2 + 22), cy, rad, off + i + 1, p, false));
    if (many) { place(rest.slice(0, 4), cy1 + R1 + rad + 8, 0); place(rest.slice(4), cy1 + R1 + rad * 3 + 16, 4); } else place(rest, cy1 + R1 + rad + 24, 0);
    footer(x, d, { link: { fill: '#f6ead0', line: '#e8b923', ink: '#3b2410' }, code: { fill: '#2f7d4f', line: '#f6ead0', ink: '#f6ead0' }, count: '#f6ead0', countStroke: '#3b2410' });
    return b.c;
  }

  // ── 14. Winter: snow and festive ribbons ──────────────────────────────────────────────────────
  async function drawWinter(d, topN) {
    const b = start(d, topN), { x, rows, places } = b, r = seeded(12), LIGHT = ['#ff4d4d', '#ffd60a', '#4cd964', '#4aa8ff'];
    const g = x.createLinearGradient(0, 0, 0, H); g.addColorStop(0, '#0b1f3a'); g.addColorStop(1, '#1d4f73'); x.fillStyle = g; x.fillRect(0, 0, W, H);
    const au = x.createRadialGradient(W * .8, 300, 20, W * .8, 300, 600); au.addColorStop(0, 'rgba(90,255,200,.16)'); au.addColorStop(1, 'rgba(90,255,200,0)'); x.fillStyle = au; x.fillRect(0, 0, W, H);
    x.strokeStyle = '#1a2a22'; x.lineWidth = 3; x.beginPath(); for (let i = 0; i <= 60; i++) { const px = i * 18, py = 22 + Math.abs(Math.sin(i / 60 * Math.PI * 3)) * 22; i ? x.lineTo(px, py) : x.moveTo(px, py); } x.stroke();
    for (let i = 0; i < 28; i++) { const px = 20 + i * 38.5, py = 22 + Math.abs(Math.sin((px / W) * Math.PI * 3)) * 22 + 6, c = LIGHT[i % 4]; x.save(); x.shadowColor = c; x.shadowBlur = 22; x.fillStyle = c; x.beginPath(); x.ellipse(px, py + 8, 6, 9, 0, 0, 7); x.fill(); x.restore(); }
    for (let i = 0; i < 150; i++) { x.globalAlpha = .35 + r() * .6; x.fillStyle = '#fff'; x.beginPath(); x.arc(r() * W, r() * H, 1.5 + r() * 4, 0, 7); x.fill(); } x.globalAlpha = 1;
    header(x, d, b, { brandY: 98, brand: { fill: '#c4162a', ink: '#fff', line: '#fff' }, head: { c: '#fff', stroke: '#c4162a', shadow: 22 }, sub: { c: '#dff1ff', stroke: '#0b1f3a', sw: 6 }, tag: { c: '#ffe27a', stroke: '#0b1f3a' } });
    const { dh, gap, y0 } = geo(b, 92, 14, 50), a = 80, w = 920;
    rows.forEach((p, k) => {
      const y = y0 + k * (dh + gap), mid = y + dh / 2, first = k === 0, col = first ? '#e8b923' : k % 2 ? '#1f7a4d' : '#c4162a', ink = first ? '#5c0f1f' : '#fff', size = Math.min(dh * .5, 48);
      x.save(); rrect(x, a, y, w, dh, 16); x.fillStyle = col; x.shadowColor = 'rgba(0,0,0,.45)'; x.shadowBlur = 16; x.shadowOffsetY = 7; x.fill(); x.restore();
      x.save(); rrect(x, a, y, w, dh, 16); x.clip(); x.fillStyle = first ? '#fff3b0' : 'rgba(255,230,150,.9)'; x.fillRect(a, y + dh * .78, w, 4); x.fillStyle = '#fff'; x.beginPath(); x.moveTo(a, y + 4); for (let sx = a; sx <= a + w; sx += 46) { x.quadraticCurveTo(sx + 12, y + 20, sx + 23, y + 9); x.quadraticCurveTo(sx + 35, y - 4, sx + 46, y + 8); } x.lineTo(a + w, y - 10); x.lineTo(a, y - 10); x.closePath(); x.fill(); x.restore();
      x.beginPath(); x.arc(a + dh * .6, mid + 4, dh * .34, 0, 7); x.fillStyle = first ? '#5c0f1f' : '#ffe27a'; x.fill(); text(x, String(places[k]), a + dh * .6, mid + 6, dh * .42, { f: HEAD, w: 400, c: first ? '#ffe27a' : '#7a1426' });
      text(x, p.emoji || '🙂', a + dh * 1.5, mid + 4, size * 1.05, { f: EMO }); text(x, p.name || 'Player', a + dh * 2, mid + 4, size, { a: 'left', c: ink, maxW: w - dh * 2 - 270 });
      text(x, val(p), a + w - 30, mid + 4, size * 1.1, { a: 'right', f: HEAD, w: 400, c: p.score < 0 ? '#ffb3b3' : ink, maxW: 250 }); if (first) text(x, '🎄', a + w + 6, y + 6, dh * .6, { f: EMO });
    });
    footer(x, d, { link: { fill: '#fff', line: '#c4162a', ink: '#0b1f3a' }, code: { fill: '#c4162a', line: '#ffe27a', ink: '#fff' }, count: '#dff1ff', countStroke: '#0b1f3a' });
    return b.c;
  }

  // ── 15. Planets ───────────────────────────────────────────────────────────────────────────────
  async function drawPlanets(d, topN) {
    const b = start(d, topN), { x, rows, places } = b, r = seeded(44);
    const g = x.createLinearGradient(0, 0, 0, H); g.addColorStop(0, '#070a1f'); g.addColorStop(1, '#1a0f3a'); x.fillStyle = g; x.fillRect(0, 0, W, H);
    for (const [px, py, rad, c] of [[180, 520, 420, '255,79,216'], [930, 930, 440, '52,211,255'], [600, 260, 380, '120,80,255']]) { const n = x.createRadialGradient(px, py, 10, px, py, rad); n.addColorStop(0, `rgba(${c},.28)`); n.addColorStop(1, `rgba(${c},0)`); x.fillStyle = n; x.fillRect(0, 0, W, H); }
    for (let i = 0; i < 120; i++) { x.globalAlpha = .25 + r() * .7; if (i % 6 === 0) sparkle(x, r() * W, r() * H, 3 + r() * 6, 0, '#fff'); else { x.fillStyle = '#fff'; x.beginPath(); x.arc(r() * W, r() * H, .8 + r() * 1.8, 0, 7); x.fill(); } } x.globalAlpha = 1;
    header(x, d, b, { brand: { fill: '#34d3ff', ink: '#070a1f' }, head: { c: '#fff', stroke: '#6a3df5', shadow: 30 }, sub: { c: '#cfd4ff' }, tag: { c: '#ffe27a', stroke: '#070a1f' } });
    const PL = [['#ffe27a', '#c98a00'], ['#dbe7ff', '#5f78c0'], ['#ffc59a', '#b4561e'], ['#7be0ff', '#1f78b4'], ['#ff9ad1', '#a3236a'], ['#b8ff9a', '#2f8f3a'], ['#e0b3ff', '#6a2fa8'], ['#ffd1a0', '#c2570c']], max = Math.max(...rows.map((p) => p.score), 1), sq = (p) => Math.sqrt(Math.max(0, p.score) / max);
    const planet = (cx, cy, rad, k) => { const gg = x.createRadialGradient(cx - rad * .35, cy - rad * .4, rad * .1, cx, cy, rad); gg.addColorStop(0, PL[k % 8][0]); gg.addColorStop(1, PL[k % 8][1]); x.save(); x.beginPath(); x.arc(cx, cy, rad, 0, 7); x.fillStyle = gg; x.shadowColor = PL[k % 8][0]; x.shadowBlur = 44; x.fill(); x.restore(); };
    const chip = (cx, cy, rad, k) => { x.beginPath(); x.arc(cx - rad * .72, cy - rad * .72, 26, 0, 7); x.fillStyle = '#fff'; x.fill(); text(x, String(places[k]), cx - rad * .72, cy - rad * .72 + 2, 32, { f: HEAD, w: 400, c: '#1a0f3a' }); };
    const A = [[1, 540], [0, 190], [2, 890]].filter(([k]) => rows[k]), cyA = b.n > 3 ? 620 : 700;
    A.forEach(([k, cx]) => {
      const p = rows[k], rad = 72 + 80 * sq(p), big = k === 0;
      if (big) { x.save(); x.translate(cx, cyA); x.rotate(-.35); x.strokeStyle = 'rgba(255,226,122,.65)'; x.lineWidth = 9; x.beginPath(); x.ellipse(0, 0, rad * 1.45, rad * .32, 0, 0, 7); x.stroke(); x.restore(); }
      planet(cx, cyA, rad, k);
      text(x, p.emoji || '🙂', cx, cyA - rad * .34, rad * .55, { f: EMO }); text(x, p.name || 'Player', cx, cyA + rad * .16, rad * .24, { c: '#fff', stroke: '#0b0b2a', sw: 6, maxW: rad * 1.6 }); text(x, val(p), cx, cyA + rad * .5, rad * .32, { f: HEAD, w: 400, c: '#fff', stroke: '#0b0b2a', sw: 7, maxW: rad * 1.6 });
      chip(cx, cyA, rad, k); if (big) text(x, '👑', cx, cyA - rad - 6, 62, { f: EMO });
    });
    const rest = rows.slice(3), cyB = 915;
    rest.forEach((p, i) => {
      const cx = W / 2 + (i - (rest.length - 1) / 2) * 190, k = i + 3, rad = 44 + 28 * sq(p); planet(cx, cyB, rad, k); text(x, p.emoji || '🙂', cx, cyB, rad * .9, { f: EMO }); chip(cx, cyB, rad * .9, k);
      text(x, p.name || 'Player', cx, cyB + rad + 24, 26, { c: '#fff', maxW: 180 }); text(x, val(p), cx, cyB + rad + 56, 32, { f: HEAD, w: 400, c: p.score < 0 ? '#ff9a9a' : '#ffe27a', maxW: 180 });
    });
    footer(x, d, { link: { fill: '#fff', line: '#34d3ff', ink: '#1a0f3a' }, code: { fill: '#34d3ff', line: '#070a1f', ink: '#070a1f' }, count: '#bfb6ff' });
    return b.c;
  }

  // ── 16. Minimal light card ────────────────────────────────────────────────────────────────────
  async function drawMinimal(d, topN) {
    const b = start(d, topN), { x, rows, places } = b, INK = '#1b1544', MUTE = '#7a74ad';
    x.fillStyle = '#f6f4ff'; x.fillRect(0, 0, W, H); x.fillStyle = '#ece7ff'; x.beginPath(); x.arc(W + 40, 60, 360, 0, 7); x.fill();
    rrect(x, 70, 56, 30, 30, 8); x.fillStyle = PURPLE; x.fill(); text(x, "LET'S QUIZ!", 116, 72, 34, { a: 'left', c: PURPLE });
    text(x, headingOf(d), 70, 170, 100, { a: 'left', f: HEAD, w: 400, c: INK, maxW: 940 }); rrect(x, 70, 232, 130, 10, 5); x.fillStyle = PURPLE; x.fill();
    wrap(x, cap1(d.title), BODY, 38, 900, 2).forEach((l, i) => text(x, l, 70, 290 + i * 46, 38, { a: 'left', c: MUTE, maxW: 940 }));
    const lead = rows[0];
    if (lead) {
      text(x, '1', 880, 520, 440, { f: HEAD, w: 400, c: 'rgba(91,61,245,.09)' });
      text(x, `${d.ended ? 'WINNER' : 'LEADING'}  ·  ${countOf(d).toUpperCase()}`, 70, 396, 24, { a: 'left', c: PURPLE, maxW: 940 });
      text(x, lead.emoji || '🙂', 118, 478, 96, { f: EMO }); text(x, lead.name || 'Player', 200, 466, 96, { a: 'left', c: INK, maxW: 810 });
      text(x, `${val(lead)} points`, 200, 540, 44, { a: 'left', c: PURPLE, maxW: 700 });
    }
    const rest = rows.slice(1), top = 586, rh = Math.min(92, 470 / Math.max(rest.length, 1));
    rest.forEach((p, i) => {
      const y = top + i * rh, mid = y + rh / 2, size = Math.min(rh * .46, 42); x.fillStyle = '#ddd8f5'; x.fillRect(70, y, 940, 2);
      text(x, String(places[i + 1]), 100, mid, size * 1.1, { f: HEAD, w: 400, c: MUTE }); text(x, p.emoji || '🙂', 180, mid, size, { f: EMO }); text(x, p.name || 'Player', 240, mid, size, { a: 'left', c: INK, maxW: 520 });
      text(x, val(p), 1010, mid, size * 1.1, { a: 'right', f: HEAD, w: 400, c: p.score < 0 ? '#d94b5f' : PURPLE, maxW: 260 });
    });
    if (!rest.length && lead) text(x, d.ended ? 'Thanks for playing! 🎉' : 'Have a go before it closes 👇', 70, 700, 50, { a: 'left', c: INK, maxW: 940 });
    footer(x, d, { link: { fill: PURPLE, line: PURPLE, lw: 2, ink: '#fff', glow: 'rgba(91,61,245,.35)' }, code: { fill: YELLOW, line: INK, lw: 4, ink: INK, glow: 'rgba(27,21,68,.18)' }, count: MUTE });
    return b.c;
  }

  // ── 17. Word tiles on a wooden table ──────────────────────────────────────────────────────────
  const SV = { A: 1, E: 1, I: 1, O: 1, U: 1, L: 1, N: 1, S: 1, T: 1, R: 1, D: 2, G: 2, B: 3, C: 3, M: 3, P: 3, F: 4, H: 4, V: 4, W: 4, Y: 4, K: 5, J: 8, X: 8, Q: 10, Z: 10 };
  function tile(x, ch, cx, cy, s, o = {}) {
    x.save(); rrect(x, cx - s / 2, cy - s / 2, s, s, s * .14); const g = x.createLinearGradient(0, cy - s / 2, 0, cy + s / 2); g.addColorStop(0, o.a || '#f8e6b8'); g.addColorStop(1, o.b || '#e8c987'); x.fillStyle = g; x.shadowColor = 'rgba(0,0,0,.5)'; x.shadowBlur = 8; x.shadowOffsetY = 4; x.fill(); x.shadowColor = 'transparent'; x.lineWidth = 2; x.strokeStyle = o.line || '#b98a3e'; x.stroke(); x.restore();
    text(x, ch, cx - s * .02, cy - s * .02, s * .62, { c: o.ink || '#2a1a08' }); if (o.v && SV[ch.toUpperCase()]) text(x, String(SV[ch.toUpperCase()]), cx + s * .3, cy + s * .32, s * .2, { c: o.ink || '#2a1a08' });
  }
  async function drawTiles(d, topN) {
    const b = start(d, topN), { x, rows, places } = b, r = seeded(9);
    for (let i = 0; i < 9; i++) { x.fillStyle = i % 2 ? '#74502a' : '#6b4623'; x.fillRect(0, i * 150, W, 150); x.fillStyle = 'rgba(0,0,0,.4)'; x.fillRect(0, i * 150, W, 4); }
    for (let i = 0; i < 240; i++) { x.globalAlpha = .07 + r() * .1; x.fillStyle = r() > .5 ? '#2e1c0a' : '#b98a55'; x.fillRect(r() * W, r() * H, 60 + r() * 240, 1 + r() * 2); } x.globalAlpha = 1;
    const vg = x.createRadialGradient(W / 2, H / 2, 300, W / 2, H / 2, 900); vg.addColorStop(0, 'rgba(0,0,0,0)'); vg.addColorStop(1, 'rgba(0,0,0,.5)'); x.fillStyle = vg; x.fillRect(0, 0, W, H);
    header(x, d, b, { brand: { fill: '#f8e6b8', ink: '#2a1a08' }, head: { c: '#f8e6b8', stroke: '#2a1a08', shadow: 22 }, sub: { c: '#f8e6b8', stroke: '#2a1a08', sw: 6 }, tag: { c: '#ffd979', stroke: '#2a1a08' } });
    const { dh, gap, y0 } = geo(b, 84, 10, 46);
    rows.forEach((p, k) => {
      const mid = y0 + k * (dh + gap) + dh / 2, s = Math.min(dh * .9, 62), nm = [...clip(String(p.name || 'Player'), 11)], sc = [...val(p)], ts = Math.min(s, 380 / Math.max(nm.length, 1)), ds = Math.min(s * .85, 300 / sc.length);
      x.beginPath(); x.arc(96, mid, dh * .34, 0, 7); x.fillStyle = k === 0 ? '#e8b923' : '#2e5e3a'; x.fill(); text(x, String(places[k]), 96, mid + 2, dh * .42, { f: HEAD, w: 400, c: k === 0 ? '#2a1a08' : '#f8e6b8' });
      text(x, p.emoji || '🙂', 175, mid, s * .85, { f: EMO }); let cx = 232 + ts / 2; for (const ch of nm) { if (ch === ' ') { cx += ts * .45; continue; } tile(x, ch.toUpperCase(), cx, mid, ts, { v: true }); cx += ts + 4; }
      sc.forEach((ch, i) => tile(x, ch, 1030 - ds / 2 - (sc.length - 1 - i) * (ds + 4), mid, ds, p.score < 0 ? { a: '#7d1f1f', b: '#5a1414', line: '#2a0a0a', ink: '#f8e6b8' } : { a: '#d9453a', b: '#a82a22', line: '#6a1410', ink: '#fff2d6' }));
    });
    footer(x, d, { link: { fill: '#f8e6b8', line: '#2a1a08', ink: '#2a1a08' }, code: { fill: '#2e5e3a', line: '#f8e6b8', ink: '#f8e6b8' }, count: '#f8e6b8', countStroke: '#2a1a08' });
    return b.c;
  }

  // ── 18. Stage podium blocks with confetti ─────────────────────────────────────────────────────
  async function drawStage(d, topN) {
    const b = start(d, topN), { x, rows, places } = b, r = seeded(27);
    const g = x.createLinearGradient(0, 0, 0, H); g.addColorStop(0, '#06242b'); g.addColorStop(1, '#0b4a55'); x.fillStyle = g; x.fillRect(0, 0, W, H);
    for (const [bx, bw, ex] of [[200, 90, 60], [540, 110, 540], [880, 90, 1020]]) { const cn = x.createLinearGradient(0, 0, 0, 900); cn.addColorStop(0, 'rgba(180,255,245,.26)'); cn.addColorStop(1, 'rgba(180,255,245,0)'); x.fillStyle = cn; x.beginPath(); x.moveTo(bx - bw / 2, 0); x.lineTo(bx + bw / 2, 0); x.lineTo(ex + 160, 900); x.lineTo(ex - 160, 900); x.closePath(); x.fill(); }
    const CF = ['#ffd60a', '#ff4fd8', '#34d3ff', '#7dff6b', '#ff8a3d']; for (let i = 0; i < 70; i++) { x.save(); x.translate(r() * W, r() * 900); x.rotate(r() * 6); x.globalAlpha = .55 + r() * .4; x.fillStyle = CF[i % 5]; x.fillRect(-6, -3, 12 + r() * 6, 6); x.restore(); }
    header(x, d, b, { brand: { fill: '#ffd60a', ink: '#06242b' }, head: { c: '#fff', stroke: '#06242b', shadow: 24 }, sub: { c: '#bff3f6' }, tag: { c: '#ffe27a', stroke: '#06242b' } });
    const base = 880, SL = [{ k: 1, cx: 215, w: 270, h: 250, c: ['#eef2f8', '#9aa6bb'], ink: '#4a5870' }, { k: 0, cx: 540, w: 300, h: 330, c: ['#ffe27a', '#d99a00'], ink: '#7a4a00' }, { k: 2, cx: 865, w: 270, h: 200, c: ['#f0b283', '#b0672d'], ink: '#6e3a14' }];
    for (const s of SL) {
      const p = rows[s.k]; if (!p) continue; const top = base - s.h, first = s.k === 0;
      x.save(); const gg = x.createLinearGradient(0, top, 0, base); gg.addColorStop(0, s.c[0]); gg.addColorStop(1, s.c[1]); rrect(x, s.cx - s.w / 2, top, s.w, s.h + 10, 14); x.fillStyle = gg; x.shadowColor = first ? 'rgba(255,214,10,.5)' : 'rgba(0,0,0,.5)'; x.shadowBlur = first ? 40 : 20; x.shadowOffsetY = 10; x.fill(); x.restore();
      x.fillStyle = 'rgba(255,255,255,.35)'; x.fillRect(s.cx - s.w / 2 + 10, top + 6, s.w - 20, 8);
      text(x, String(places[s.k]), s.cx, top + s.h * .3, s.h * .42, { f: HEAD, w: 400, c: 'rgba(0,0,0,.22)' }); text(x, p.name || 'Player', s.cx, top + s.h * .6, Math.min(36, s.h * .13), { c: DEEP, maxW: s.w - 30 }); text(x, val(p), s.cx, top + s.h * .82, Math.min(56, s.h * .2), { f: HEAD, w: 400, c: p.score < 0 ? '#c0283f' : s.ink, maxW: s.w - 30 });
      text(x, p.emoji || '🙂', s.cx, top - 62, first ? 130 : 112, { f: EMO }); if (first) text(x, '👑', s.cx, top - 150, 64, { f: EMO });
    }
    x.fillStyle = '#04171c'; x.fillRect(40, base + 10, W - 80, 8);
    rows.slice(3).forEach((p, i) => {
      const col = i % 2, row = Math.floor(i / 2), cw = 460, cx0 = col ? 560 : 60, y = 910 + row * 50, mid = y + 22;
      x.save(); rrect(x, cx0, y, cw, 44, 22); x.fillStyle = 'rgba(255,255,255,.93)'; x.fill(); x.restore();
      text(x, String(places[i + 3]), cx0 + 30, mid + 1, 28, { f: HEAD, w: 400, c: '#0b4a55' }); text(x, p.emoji || '🙂', cx0 + 76, mid, 30, { f: EMO }); text(x, p.name || 'Player', cx0 + 108, mid, 28, { a: 'left', c: DEEP, maxW: 200 }); text(x, val(p), cx0 + cw - 18, mid + 1, 30, { a: 'right', f: HEAD, w: 400, c: p.score < 0 ? '#c0283f' : '#0b4a55', maxW: 130 });
    });
    footer(x, d, { link: { fill: '#fff', line: '#ffd60a', ink: '#06242b' }, code: { fill: '#ffd60a', line: '#06242b', ink: '#06242b' }, count: '#bff3f6' });
    return b.c;
  }

  // ── 19. Neon sign on a brick wall ─────────────────────────────────────────────────────────────
  async function drawNeonSign(d, topN) {
    const b = start(d, topN), { x, rows, places } = b, r = seeded(61);
    x.fillStyle = '#1a0c0b'; x.fillRect(0, 0, W, H);
    for (let row = 0; row * 30 < H + 30; row++) for (let bx = -(row % 2) * 45; bx < W; bx += 90) { const t = r(); x.fillStyle = `rgb(${70 + t * 38},${30 + t * 16},${26 + t * 12})`; x.fillRect(bx + 3, row * 30 + 3, 84, 24); }
    x.fillStyle = 'rgba(0,0,0,.4)'; x.fillRect(0, 0, W, H); const vg = x.createRadialGradient(W / 2, 640, 200, W / 2, 640, 900); vg.addColorStop(0, 'rgba(0,0,0,0)'); vg.addColorStop(1, 'rgba(0,0,0,.7)'); x.fillStyle = vg; x.fillRect(0, 0, W, H);
    neonRect(x, W / 2 - 165, 44, 330, 68, 34, '#34d3ff', 5); neon(x, "LET'S QUIZ!", W / 2, 80, 38, '#34d3ff', { f: BODY, w: 900 });
    neon(x, headingOf(d), W / 2, 190, 124, '#ff3d9a', { maxW: 960 });
    wrap(x, cap1(d.title), BODY, 40, 900, 2).forEach((l, i) => text(x, l, W / 2, 275 + i * 48, 40, { c: '#ffe8f4', maxW: 940 }));
    neon(x, tagOf(d, rows), W / 2, 372, 50, '#ffd60a', { f: BODY, w: 900, maxW: 940 });
    const { dh, gap, y0 } = geo(b, 86, 12, 48);
    rows.forEach((p, k) => {
      const y = y0 + k * (dh + gap), mid = y + dh / 2, col = k === 0 ? '#ffd60a' : NEON[(k + 1) % NEON.length], size = Math.min(dh * .52, 48);
      neonRect(x, 80, y, 920, dh, dh / 2.6, col, k === 0 ? 8 : 6); neon(x, String(places[k]), 140, mid, size * 1.15, col, { f: HEAD }); text(x, p.emoji || '🙂', 220, mid, size, { f: EMO });
      text(x, p.name || 'Player', 270, mid, size, { a: 'left', c: '#fff', maxW: 470 }); neon(x, val(p), 960, mid, size * 1.1, p.score < 0 ? '#ff5c7a' : col, { a: 'right', f: HEAD, maxW: 260 }); if (k === 0) text(x, '⭐', 1010, y + 4, 44, { f: EMO });
    });
    footer(x, d, { link: { fill: 'rgba(10,4,12,.88)', line: '#fff', ink: '#fff', glow: '#ff3d9a' }, code: { fill: 'rgba(10,4,12,.88)', line: '#ffd60a', ink: '#ffd60a', glow: '#ffd60a' }, count: '#ffd1ec' });
    return b.c;
  }

  // ── 20. Retro seventies ───────────────────────────────────────────────────────────────────────
  async function drawRetro(d, topN) {
    const b = start(d, topN), { x, rows, places } = b, BAND = ['#e8590c', '#f08c00', '#8fa31e', '#6b4423', '#c92a2a'], CREAM = '#fff3d6', BROWN = '#5a2410';
    x.fillStyle = '#f6e3b4'; x.fillRect(0, 0, W, H);
    ['#e8590c', '#f08c00', '#fcc419', '#8fa31e', '#6b4423'].forEach((c, i) => { x.beginPath(); x.arc(0, H, 1650 - i * 125, 0, 7); x.fillStyle = c; x.globalAlpha = .3; x.fill(); }); x.globalAlpha = 1;
    x.save(); rrect(x, W / 2 - 165, 44, 330, 68, 34); x.fillStyle = BROWN; x.fill(); x.restore(); text(x, "LET'S QUIZ!", W / 2, 80, 40, { c: '#fcc419' });
    const hd = headingOf(d), f = fit(x, hd, HEAD, 124, 960); x.save(); x.font = `400 ${f.size}px ${HEAD}`; x.textAlign = 'center'; x.textBaseline = 'middle'; x.lineJoin = 'round'; x.fillStyle = '#e8590c'; x.fillText(f.text, W / 2 + 8, 198); x.lineWidth = f.size * .12; x.strokeStyle = CREAM; x.strokeText(f.text, W / 2, 190); x.fillStyle = BROWN; x.fillText(f.text, W / 2, 190); x.restore();
    wrap(x, cap1(d.title), BODY, 40, 900, 2).forEach((l, i) => text(x, l, W / 2, 275 + i * 48, 40, { c: BROWN, stroke: CREAM, sw: 6, maxW: 940 }));
    text(x, tagOf(d, rows), W / 2, 372, 52, { c: '#e8590c', stroke: CREAM, sw: 10, maxW: 940 });
    const { dh, gap, y0 } = geo(b, 92, 12, 48);
    rows.forEach((p, k) => {
      const y = y0 + k * (dh + gap), mid = y + dh / 2, first = k === 0, col = first ? '#fcc419' : BAND[(k - 1) % BAND.length], ink = first ? BROWN : CREAM, size = Math.min(dh * .5, 48);
      x.save(); rrect(x, 70, y, 940, dh, dh / 2); x.fillStyle = col; x.shadowColor = 'rgba(90,36,16,.4)'; x.shadowBlur = 14; x.shadowOffsetY = 7; x.fill(); x.restore();
      x.save(); rrect(x, 70, y, 940, dh, dh / 2); x.clip(); x.fillStyle = 'rgba(255,243,214,.38)'; x.fillRect(70, y + dh * .72, 940, 4); x.fillRect(70, y + dh * .82, 940, 2); x.restore();
      x.beginPath(); x.arc(70 + dh / 2, mid, dh * .36, 0, 7); x.fillStyle = CREAM; x.fill(); text(x, String(places[k]), 70 + dh / 2, mid + 2, dh * .46, { f: HEAD, w: 400, c: first ? BROWN : col });
      text(x, p.emoji || '🙂', 70 + dh * 1.35, mid, size * 1.05, { f: EMO }); text(x, p.name || 'Player', 70 + dh * 1.85, mid, size, { a: 'left', c: ink, maxW: 580 - dh }); text(x, val(p), 970 - dh * .2, mid, size * 1.1, { a: 'right', f: HEAD, w: 400, c: p.score < 0 && !first ? '#ffd0d0' : ink, maxW: 260 });
      if (first) text(x, '🌟', 1010, y + 2, dh * .5, { f: EMO });
    });
    footer(x, d, { link: { fill: BROWN, line: '#e8590c', ink: CREAM }, code: { fill: '#e8590c', line: BROWN, ink: CREAM }, count: BROWN, countStroke: CREAM });
    return b.c;
  }

  [['curtain', 'Stage curtains', drawCurtain], ['chalk', 'Chalkboard', drawChalk], ['news', 'Newspaper', drawNews], ['arcade', 'Arcade', drawArcade], ['flap', 'Split-flap board', drawFlap],
   ['race', 'Race track', drawRace], ['bars', 'Bar chart', drawBars], ['league', 'League table', drawLeague], ['tickets', 'Cinema tickets', drawTickets], ['comic', 'Comic book', drawComic],
   ['mats', 'Beer mats', drawMats], ['winter', 'Winter', drawWinter], ['planets', 'Planets', drawPlanets], ['minimal', 'Clean and simple', drawMinimal], ['tiles', 'Word tiles', drawTiles],
   ['stage', 'Stage blocks', drawStage], ['neon', 'Neon sign', drawNeonSign], ['retro', 'Retro seventies', drawRetro]].forEach(([id, name, draw]) => LQLeader.designs.push({ id, name, draw }));
})();
