/* Let's Quiz host screen: Taskmaster on camera (October 2026). A Taskmaster question with mode 'spin' runs several
 * tasks: for each, the wheel spins (three times) to pick who does it, then an envelope opens with the task. 90 seconds:
 * the clock shows up 5 seconds after the envelope opens, at 85. When time's up the host marks 1st / 2nd / 3rd / didn't
 * try (1000 / 200 / 0 / −1000 by default), and the wheel spins for the next task. Mode 'all' is one task for everybody
 * at once (no wheel). Everything is done on the quiz call's cameras; nothing is sent from the phones.
 * How many tasks: under 9 players two per question, otherwise three, or more if that's what it takes for everyone to be
 * picked at least once across the night's spin questions. The wheel picks people not yet picked tonight first, and no
 * task is used twice in a night. Loaded with party.js before host.html's own script; names start tm. */

const TM_SPIN_MS = 4800, TM_HOLD_MS = 1700, TM_READY_MS = 3500, TM_PEEK_MS = 5000, TM_SHOW_MS = 6000;
const TM_PLACES = { 1: '🥇', 2: '🥈', 3: '🥉', x: '❌' };
/** Is this question played on camera (the wheel, or everyone at once)? A warm-up's task is always a photo. */
const tmMode = (q) => q?.type === 'task' && !WARMUP && (q.mode === 'spin' || q.mode === 'all');
const tmTasksOf = (q) => (Array.isArray(q?.tasks) ? q.tasks : []).map((t) => String(t || '').trim()).filter(Boolean);
const tmPrizes = (q) => { const p = Array.isArray(q.prizes) ? q.prizes : []; return [p[0] ?? 1000, p[1] ?? 200, p[2] ?? 0]; };
const tmFail = (q) => q.mode === 'all' ? 0 : Math.abs(+(q.fail ?? 1000) || 0);
function tmPoints(q, v) { const p = tmPrizes(q); return v === 'x' ? -tmFail(q) : ['1', '2', '3'].includes(v) ? (+p[+v - 1] || 0) : 0; }
/** The unused tasks for this question: its own first, then any other spin question's (so a big room never runs dry). */
function tmPool(q) {
  const used = new Set(G.tmUsed || []);
  const rest = G.quiz.questions.filter((x) => x !== q && x.type === 'task' && x.mode === 'spin').flatMap(tmTasksOf);
  return { own: tmTasksOf(q).filter((t) => !used.has(t)), rest: [...new Set(rest)].filter((t) => !used.has(t) && !tmTasksOf(q).includes(t)) };
}
const tmPlayers = () => livePids().filter((p) => G.players[p] && !G.viewers?.[p]);

function tmStart() {
  const q = question(), live = tmPlayers();
  const g = G.q.tm = { step: 'spin', until: 0, total: 0, round: 0, count: 1, per: Math.min(3, live.length), pts: {}, done: [], cur: null, spin: null };
  if (q.mode === 'all') { g.count = 1; g.all = true; return tmNextTask(); }
  // how many tasks this time: the house rule (2 under 9 players, else 3), or enough to reach everyone not yet picked
  const n = live.length, base = n < 9 ? 2 : 3;
  const left = Math.max(1, G.quiz.questions.slice(G.qIndex).filter((x) => x.type === 'task' && x.mode === 'spin').length);
  const unpicked = live.filter((p) => !(G.tmPicked || []).includes(p)).length;
  const pool = tmPool(q);
  g.count = Math.max(1, Math.min(Math.max(base, Math.ceil(unpicked / (left * Math.max(1, g.per)))), pool.own.length + pool.rest.length));
  tmNextTask();
}
function tmNextTask() {
  const q = question(), g = G.q.tm; g.round++;
  let task;
  if (g.all) task = tmTasksOf(q)[0] || q.text;
  else { const pool = tmPool(q); task = pool.own.length ? pool.own[0] : partyPick(pool.rest); }
  if (!task) return endQuestion();
  if (!g.all) G.tmUsed = [...(G.tmUsed || []), task];
  g.cur = { task, picks: g.all ? tmPlayers() : [], places: {} };
  g.spin = null;
  if (g.all) return tmOpen();
  tmSpin();
}
/** One spin of the wheel: it lands on someone not yet doing this task, preferring people not picked yet tonight. */
function tmSpin() {
  const g = G.q.tm, live = tmPlayers();
  const free = live.filter((p) => !g.cur.picks.includes(p));
  if (!free.length) return tmReady();
  const fresh = free.filter((p) => !(G.tmPicked || []).includes(p));
  const target = partyPick(fresh.length ? fresh : free);
  g.spin = { order: live.slice(), target, at: Date.now(), n: g.cur.picks.length + 1 };
  stepTo(g, 'spin', TM_SPIN_MS + TM_HOLD_MS); g.total = 0; sound('whoosh'); // no clock on the wheel
  setTimeout(() => { if (G.q?.tm === g && g.spin?.target === target && g.step === 'spin') { sound('ding'); tmRender(); } }, TM_SPIN_MS);
  persist(); tmRender(); broadcastState();
}
function tmLanded() {
  const g = G.q.tm, pid = g.spin?.target; if (!pid) return;
  if (!g.cur.picks.includes(pid)) g.cur.picks.push(pid);
  G.tmPicked = [...new Set([...(G.tmPicked || []), pid])];
}
function tmReady() { const g = G.q.tm; g.spin = null; stepTo(g, 'ready', TM_READY_MS); g.total = 0; sound('drumroll'); persist(); tmRender(); broadcastState(); }
/** The envelope opens: the clock starts now, and shows itself 5 seconds in. */
function tmOpen() {
  const g = G.q.tm, ms = LQ.clamp(+question().time || 90, 20, 600) * 1000;
  g.openAt = Date.now(); g.spin = null;
  stepTo(g, 'envelope', ms); g.total = 0; // the clock stays hidden for the first 5 seconds
  sound('go'); persist(); tmRender(); broadcastState();
  // once the opening has played, draw it again without the animation: the card is there even if animations stalled
  const at = g.openAt; setTimeout(() => { if (G.q?.tm === g && g.step === 'envelope' && g.openAt === at) tmRender(); }, 1900);
}
/** Ten times a second: 5 seconds after the envelope opens, the clock appears (at 85 seconds of 90). */
function tmTick(now) {
  const g = G.q.tm;
  if (g?.step === 'envelope' && !g.total && g.openAt && now - g.openAt >= TM_PEEK_MS) { g.total = Math.max(1000, g.until - g.openAt - TM_PEEK_MS); persist(); paintClock(); broadcastState(); }
}
function tmStepDone() {
  const g = G.q.tm;
  if (g.step === 'spin') { tmLanded(); return g.cur.picks.length < g.per ? tmSpin() : tmReady(); }
  if (g.step === 'ready') return tmOpen();
  if (g.step === 'envelope') { stepTo(g, 'judge', 0); sound('claxon'); persist(); tmRender(); broadcastState(); return; }
  if (g.step === 'show') return g.round < g.count ? tmNextTask() : endQuestion();
}
/** The host marks a player: on the wheel tasks each place goes to one player (clicking a taken place takes it over). */
function tmPlace(pid, v) {
  const g = G.q.tm; if (!g || g.step !== 'judge' || !g.cur.picks.includes(pid)) return;
  const was = g.cur.places[pid];
  if (was === v) delete g.cur.places[pid];
  else { if (['1', '2', '3'].includes(v)) for (const [p, x] of Object.entries(g.cur.places)) if (x === v) delete g.cur.places[p]; g.cur.places[pid] = v; }
  persist(); tmRender();
}
function tmAward() {
  const q = question(), g = G.q.tm; if (!g || g.step !== 'judge') return;
  const got = {};
  for (const pid of g.cur.picks) { const pts = tmPoints(q, g.cur.places[pid] || ''); got[pid] = pts; g.pts[pid] = (g.pts[pid] || 0) + pts; }
  g.done.push({ task: g.cur.task, picks: g.cur.picks.slice(), places: { ...g.cur.places }, got });
  stepTo(g, 'show', TM_SHOW_MS); g.total = 0; sound(Object.values(got).some((x) => x > 0) ? 'fanfare' : 'trombone');
  persist(); tmRender(); broadcastState();
}

// ---- drawing it
const TM_COLS = ['#e21b3c', '#1368ce', '#d89e00', '#26890c', '#8e44ad', '#ff7a1a', '#00a3a3', '#c2185b'];
/** The wheel: one slice per player, turned so the pointer (at the top) lands on the target. */
function tmWheelHtml(order, target, landed) {
  const n = Math.max(1, order.length), seg = 360 / n, R = 200, t = Math.max(0, order.indexOf(target));
  const slice = (i) => { const a0 = (i * seg - 90) * Math.PI / 180, a1 = ((i + 1) * seg - 90) * Math.PI / 180, big = seg > 180 ? 1 : 0;
    return n === 1 ? `<circle cx="0" cy="0" r="${R}" fill="${TM_COLS[0]}"/>` : `<path d="M0 0 L${(R * Math.cos(a0)).toFixed(1)} ${(R * Math.sin(a0)).toFixed(1)} A${R} ${R} 0 ${big} 1 ${(R * Math.cos(a1)).toFixed(1)} ${(R * Math.sin(a1)).toFixed(1)} Z" fill="${TM_COLS[i % TM_COLS.length]}" stroke="#fff" stroke-width="3"/>`; };
  const label = (i) => { const mid = (i + 0.5) * seg; const nm = pname(order[i]); const fs = Math.max(11, Math.min(26, 260 / Math.max(6, nm.length) * (n > 12 ? 0.75 : 1))); return `<g transform="rotate(${mid - 90})"><text x="${R * 0.92}" y="0" text-anchor="end" dominant-baseline="middle" font-size="${fs}" font-weight="900" fill="#fff">${esc(nm.slice(0, 16))}</text></g>`; };
  const finalDeg = 360 * 6 - (t + 0.5) * seg;
  return `<div class="tmwheel"><div class="tmpointer">▼</div><svg viewBox="-210 -210 420 420"><g class="tmspin" data-final="${finalDeg}" style="transform:rotate(${landed ? finalDeg : 0}deg)">${order.map((_, i) => slice(i)).join('')}${order.map((_, i) => label(i)).join('')}</g><circle r="34" fill="#1b1650" stroke="#fff" stroke-width="5"/><text y="9" text-anchor="middle" font-size="26" fill="#ffd60a" font-weight="900">TM</text></svg></div>`;
}
const tmChip = (pid, extra = '') => `<span class="tmchip">${face(pid)}<b>${esc(pname(pid))}</b>${extra}</span>`;
function tmRender() {
  const q = question(), g = G.q?.tm; if (!g || G.phase !== 'question') return;
  const head = g.all ? '🎭 Everyone, all at once!' : `Task ${g.round} of ${g.count}`;
  let main = '', btn = '';
  if (g.step === 'spin' && g.spin) {
    const landed = Date.now() - g.spin.at >= TM_SPIN_MS;
    main = `<div class="tmhead"><div class="ri-kicker">📞 Taskmaster · ${head}</div><h1 class="qtext">Spin ${g.spin.n} of ${g.per}: who's doing it?</h1></div>
      <div class="tmspinrow">${tmWheelHtml(g.spin.order, g.spin.target, landed)}<div class="tmpicked">${g.cur.picks.map((p) => tmChip(p)).join('')}${landed ? `<div class="tmland">🎯 ${esc(pname(g.spin.target))}!</div>` : ''}</div></div>`;
    btn = '<button class="btn btn-primary" id="tmGo">Next ▶</button>';
  } else if (g.step === 'ready') {
    main = `<div class="tmhead"><div class="ri-kicker">📞 Taskmaster · ${head}</div><h1 class="big">Your task, should you choose to accept it…</h1></div><div class="tmpicked big">${g.cur.picks.map((p) => tmChip(p)).join('')}</div>`;
    btn = '<button class="btn btn-primary" id="tmGo">Open the envelope ✉️</button>';
  } else if (g.step === 'envelope') {
    // the envelope opens and fades, and the task card takes its place (only animated just after opening; a later redraw
    // shows the card straight away, and so does a screen where animations don't run)
    const fresh = Date.now() - g.openAt < 1800;
    main = `<div class="tmletter ${fresh ? 'fresh' : ''}"><div class="tmcard"><div class="tmcard-k">TASK ${g.all ? '' : g.round}</div><div class="tmcard-t">${esc(g.cur.task)}</div><div class="tmcard-f">You have ${Math.round((g.until - g.openAt) / 1000)} seconds. Your time started when you opened this task.</div></div><div class="tmenv2"><div class="tme-body"></div><div class="tme-flap"></div><div class="tmseal">TM</div></div></div>
      ${g.all ? '<div class="tmpicked row"><span class="tmchip"><b>🎭 Everyone!</b></span></div>' : `<div class="tmpicked row">${g.cur.picks.map((p) => tmChip(p)).join('')}</div>`}`;
    btn = '<button class="btn btn-primary" id="tmGo">Time\'s up ■</button>';
  } else if (g.step === 'judge') {
    const p = tmPrizes(q), fail = tmFail(q);
    const places = g.all ? ['1', '2', '3'] : ['1', '2', '3', 'x'];
    const lab = (v) => v === 'x' ? `❌ Didn't try${fail ? ` −${fail}` : ''}` : `${TM_PLACES[v]} ${p[+v - 1] > 0 ? '+' : ''}${p[+v - 1]}`;
    main = `<div class="tmhead"><div class="ri-kicker">⚖️ The Taskmaster decides</div><div class="tmtask-sm">${esc(g.cur.task)}</div></div>
      <div class="tmjudge ${g.all ? 'all' : ''}">${g.cur.picks.map((pid) => `<div class="tmj ${g.cur.places[pid] ? 'set' : ''}"><div class="tmj-who">${face(pid)}<b>${esc(pname(pid))}</b>${g.cur.places[pid] ? `<span class="tmj-medal">${TM_PLACES[g.cur.places[pid]]}</span>` : ''}</div><div class="tmj-btns">${places.map((v) => `<button class="btn btn-sm ${g.cur.places[pid] === v ? 'btn-primary' : 'btn-ghost'}" data-tmp="${pid}" data-v="${v}">${lab(v)}</button>`).join('')}</div></div>`).join('')}</div>`;
    btn = '<button class="btn btn-primary" id="tmGo">Award the points ▶</button>';
  } else if (g.step === 'show') {
    const last = g.done[g.done.length - 1];
    const order = Object.keys(last.got).sort((a, b) => last.got[b] - last.got[a]);
    main = `<div class="tmhead"><div class="ri-kicker">📞 Taskmaster · ${head}</div><div class="tmtask-sm">${esc(last.task)}</div></div>
      <div class="tmresults">${order.filter((pid) => last.places[pid] || last.got[pid]).map((pid) => `<div class="tmres ${last.got[pid] < 0 ? 'neg' : ''}">${last.places[pid] ? `<span class="tmj-medal">${TM_PLACES[last.places[pid]]}</span>` : ''}${face(pid)}<b>${esc(pname(pid))}</b><span class="tmres-pts">${last.got[pid] > 0 ? '+' : ''}${last.got[pid]}</span></div>`).join('') || '<div class="item">No points this time!</div>'}</div>
      ${g.round < g.count ? '<p class="uqrule">Spinning again in a moment…</p>' : ''}`;
    btn = `<button class="btn btn-primary" id="tmGo">${g.round < g.count ? 'Spin again 🎡' : 'Finish ▶'}</button>`;
  }
  stage.innerHTML = `${topBar(`<div class="pillbox"><span class="hpill">📞 ${head}</span><div class="timer hidden" id="timer" data-s="0" style="--p:100%"></div></div>`)}
    <div class="stage-main tmstage">${main}</div>${hostBar(`<button class="btn btn-ghost" data-act="end">End game</button><button class="btn btn-ghost" data-act="stopgame">Stop the game ■</button>${btn}`)}`;
  bind();
  // the wheel turns from 0 to its landing spot over what's left of the spin (a redraw mid-spin carries on from 0, quicker)
  const spinG = stage.querySelector('.tmspin');
  if (spinG && g.spin && Date.now() - g.spin.at < TM_SPIN_MS) {
    const left = Math.max(300, TM_SPIN_MS - (Date.now() - g.spin.at));
    requestAnimationFrame(() => requestAnimationFrame(() => { spinG.style.transition = `transform ${left}ms cubic-bezier(.12,.6,.12,1)`; spinG.style.transform = `rotate(${spinG.dataset.final}deg)`; }));
  }
  $$('[data-tmp]').forEach((b) => b.onclick = () => tmPlace(b.dataset.tmp, b.dataset.v));
  const go = $('#tmGo');
  if (go) go.onclick = () => {
    const s = G.q?.tm?.step;
    if (s === 'judge') return tmAward();
    if (s === 'envelope') { G.q.tm.until = 0; return tmStepDone(); }
    if (s === 'spin' && Date.now() - G.q.tm.spin.at < TM_SPIN_MS) return; // let the wheel finish
    G.q.tm.until = 0; tmStepDone();
  };
}
/** The phones' share: the step, who's picked so far (only once the wheel has landed), the task once it's open. */
function tmState(s) {
  const g = G.q?.tm; if (!g || G.phase !== 'question') return;
  const nowT = G.paused ? G.pausedAt : Date.now();
  const landed = g.spin && nowT - g.spin.at >= TM_SPIN_MS ? g.spin.target : null;
  s.tm = { step: g.step, remainingMs: g.until ? Math.max(0, g.until - nowT) : 0, totalMs: g.total, round: g.round, count: g.count, all: !!g.all,
    picks: [...(g.cur?.picks || []), ...(landed && !g.cur.picks.includes(landed) ? [landed] : [])], spinning: g.step === 'spin' && !landed,
    task: ['envelope', 'judge', 'show'].includes(g.step) ? g.cur?.task : '', got: g.step === 'show' ? g.done[g.done.length - 1]?.got : null, pts: g.pts };
  s.names = Object.fromEntries(Object.values(G.players).map((p) => [p.id, { name: p.name, emoji: p.emoji || '' }]));
}
function tmGrade(q, byPlayer, PL, stats) {
  const g = G.q.tm || { pts: {}, done: [] };
  const took = new Set(g.done.flatMap((d) => d.picks));
  for (const pid of new Set([...tmPlayers(), ...Object.keys(g.pts)])) {
    if (!PL[pid]) continue;
    const pts = g.pts[pid] || 0, mine = g.done.filter((d) => d.picks.includes(pid));
    const best = mine.map((d) => d.places[pid]).find((v) => v === '1') || mine.map((d) => d.places[pid]).find(Boolean) || '';
    byPlayer[pid] = { answered: took.has(pid), correct: pts > 0, partial: pts > 0 ? 1 : 0, points: pts,
      note: !took.has(pid) ? '📞 Not picked for this one' : best === 'x' ? "❌ You didn't even try!" : best ? `${TM_PLACES[best]} The Taskmaster put you ${best === '1' ? 'FIRST' : best === '2' ? 'second' : 'third'}!` : '📞 No points from the Taskmaster this time' };
    if (pts > 0) stats.right++;
  }
  stats.answered = took.size;
}
function tmRevealHtml(q) {
  const g = G.q.tm || { done: [] };
  return `<div class="tmdone">${g.done.map((d, i) => `<div class="tmdone-row"><div class="tmtask-sm"><b>${g.all ? 'Everyone' : 'Task ' + (i + 1)}:</b> ${esc(d.task)}</div><div class="textlist">${Object.keys(d.got).filter((pid) => d.places[pid] || d.got[pid]).sort((a, b) => d.got[b] - d.got[a]).map((pid) => `<span class="tl ${d.got[pid] < 0 ? 'no' : 'ok'}">${d.places[pid] ? TM_PLACES[d.places[pid]] + ' ' : ''}${pem(pid)} ${esc(pname(pid))} ${d.got[pid] > 0 ? '+' : ''}${d.got[pid]}</span>`).join('') || '<span class="tl">No points</span>'}</div></div>`).join('')}</div>`;
}
