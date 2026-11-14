/* Box Clever hands-free (phones): the phone reads the game out loud and listens for your choices, for a passenger or a parked car.
 * It uses the browser's own speech: speechSynthesis to talk, SpeechRecognition (webkitSpeechRecognition on iPhone and Chrome) to listen.
 * Every choice is read back and needs a "yes" before it is sent, because a mis-heard word costs real points.
 * Hooked in at the end of bxBind (boxes-phone.js); the button appears on the Box Clever screens of a game played on phones. */
const BV = { on: false, tok: 0, key: '', rec: null, told: {}, voice: null, listening: false };
try { BV.on = localStorage.getItem('lq_handsfree') === '1'; } catch {}
const BV_TTS = typeof speechSynthesis !== 'undefined' && typeof SpeechSynthesisUtterance !== 'undefined';
const BV_SR = typeof window !== 'undefined' && (window.SpeechRecognition || window.webkitSpeechRecognition);

// ---------------------------------------------------------------- understanding what was said (pure, tested apart)
const BVP = (() => {
  const UNITS = { zero: 0, oh: 0, one: 1, two: 2, three: 3, four: 4, five: 5, six: 6, seven: 7, eight: 8, nine: 9, ten: 10, eleven: 11, twelve: 12, thirteen: 13, fourteen: 14, fifteen: 15, sixteen: 16, seventeen: 17, eighteen: 18, nineteen: 19 };
  const TENS = { twenty: 20, thirty: 30, forty: 40, fifty: 50, sixty: 60, seventy: 70, eighty: 80, ninety: 90 };
  const ORD = { first: 1, second: 2, third: 3, fourth: 4, fifth: 5, sixth: 6, seventh: 7, eighth: 8, ninth: 9, tenth: 10 };
  const norm = (s) => String(s || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/&/g, ' and ').replace(/[^a-z0-9 ]+/g, ' ').replace(/\s+/g, ' ').trim();
  const toks = (s) => norm(s).split(' ').filter(Boolean);
  /** "14", "fourteen", "twenty one", "five hundred", "1,500" -> a number, or null. */
  function number(text) {
    const d = String(text).replace(/(\d),(\d{3})/g, '$1$2').match(/\d+/);
    if (d) return +d[0];
    let total = 0, cur = 0, seen = false;
    for (const t of toks(text)) {
      if (t in UNITS) { cur += UNITS[t]; seen = true; } else if (t in TENS) { cur += TENS[t]; seen = true; }
      else if (t === 'hundred') { cur = (cur || 1) * 100; seen = true; } else if (t === 'thousand') { total += (cur || 1) * 1000; cur = 0; seen = true; }
    }
    return seen ? total + cur : null;
  }
  const STOP = new Set(['the', 'and', 'of', 'a']);
  /** Which box: a number ("box 14"), or a category and a place in its row ("traitors three"). cats: [{n}], cols per row, board: ['open'|...]. */
  function box(text, cats, cols, board) {
    const t = new Set(toks(text));
    for (let r = 0; r < cats.length; r++) {
      const w = toks(cats[r].n).filter((x) => !STOP.has(x)), long = w.filter((x) => x.length >= 4);
      const hit = long.length ? long.some((x) => t.has(x)) : w.every((x) => t.has(x));
      if (!hit) continue;
      let pos = null; for (const x of toks(text)) if (x in ORD) pos = ORD[x];
      if (pos == null) { const rest = toks(text).filter((x) => !w.includes(x)).join(' '); pos = number(rest); }
      if (pos >= 1 && pos <= cols) { const n = r * cols + pos; return board[n - 1] === 'open' ? { n } : { gone: n }; }
      return { cat: r };
    }
    const n = number(text);
    if (n >= 1 && n <= board.length) return board[n - 1] === 'open' ? { n } : { gone: n };
    return null;
  }
  const LETTERS = [['a', 'ay', 'eh', 'hey'], ['b', 'be', 'bee', 'bea'], ['c', 'see', 'sea', 'si', 'cee'], ['d', 'dee']];
  /** Which option: "B", "option c", "bee", "the second one", or the words of the option itself. Returns an index or -1. */
  function letter(text, opts) {
    const w = toks(text), n = opts.length;
    if (w.length <= 3) for (let i = 0; i < n; i++) if (w.some((x) => LETTERS[i].includes(x))) return i;
    for (const x of w) if (x in ORD && ORD[x] <= n) return ORD[x] - 1;
    let best = -1, bs = 0, tie = false; const sp = new Set(w);
    opts.forEach((o, i) => { const ot = toks(o); if (!ot.length) return; const sc = ot.filter((x) => sp.has(x)).length / ot.length; if (sc > bs) { bs = sc; best = i; tie = false; } else if (sc === bs && sc > 0) tie = true; });
    if (bs >= 0.6 && !tie) return best;
    const hits = opts.map((o, i) => (toks(o).some((x) => x.length >= 4 && sp.has(x)) ? i : -1)).filter((i) => i >= 0); // one name out of several: only one option has it
    return hits.length === 1 ? hits[0] : -1;
  }
  /** "yes" / "no" / null. */
  function yesno(text) {
    const w = toks(text);
    if (w.some((x) => ['no', 'nope', 'nah', 'wrong', 'cancel', 'change', 'back'].includes(x))) return 'no';
    if (w.some((x) => ['yes', 'yeah', 'yep', 'yup', 'okay', 'ok', 'sure', 'correct', 'right', 'confirm', 'lock'].includes(x))) return 'yes';
    return null;
  }
  /** How much to gamble: "all in", or any amount up to the pot. */
  function stake(text, pot) {
    if (/\b(all in|everything|the lot|the maximum|max)\b/.test(norm(text))) return pot;
    const n = number(text);
    return n >= 1 ? Math.min(n, pot) : null;
  }
  const go = (text) => /\b(go|start|ready|begin|yes|yeah|okay|ok|lets)\b/.test(norm(text));
  const pass = (text) => /\bpass\b/.test(norm(text));
  return { number, box, letter, yesno, stake, go, pass, norm };
})();

// ---------------------------------------------------------------- talking and listening
function bvStatus(t) { const el = document.getElementById('bvstat'); if (el) el.textContent = t || ''; }
function bvAbort() { try { if (BV_TTS) speechSynthesis.cancel(); } catch {} try { BV.rec && BV.rec.abort(); } catch {} BV.rec = null; bvStatus(''); }
function bvPickVoice() {
  if (!BV_TTS || BV.voice) return;
  const vs = speechSynthesis.getVoices() || [];
  BV.voice = vs.find((v) => /en-GB/i.test(v.lang) && /daniel|serena|kate|google uk|female/i.test(v.name)) || vs.find((v) => /en-GB/i.test(v.lang)) || vs.find((v) => /^en/i.test(v.lang)) || null;
}
function bvSay(text) {
  return new Promise((res) => {
    if (!BV_TTS || !text) return res();
    bvPickVoice(); bvStatus('🔊 ' + text);
    const u = new SpeechSynthesisUtterance(text); u.lang = 'en-GB'; if (BV.voice) u.voice = BV.voice;
    let done = false; const fin = () => { if (!done) { done = true; clearTimeout(t); res(); } };
    u.onend = fin; u.onerror = fin; const t = setTimeout(fin, 5000 + text.length * 95);
    try { speechSynthesis.speak(u); } catch { fin(); }
  });
}
/** Listens once; resolves with the alternatives heard (best first), or [] when nothing was heard. */
function bvListen(ms) {
  return new Promise((res) => {
    if (!BV_SR) return res([]);
    const r = new BV_SR(); let got = [], done = false;
    r.lang = 'en-GB'; r.interimResults = false; r.continuous = false; r.maxAlternatives = 4;
    const fin = () => { if (done) return; done = true; clearTimeout(t); BV.listening = false; try { r.stop(); } catch {} if (BV.rec === r) BV.rec = null; res(got); };
    r.onresult = (e) => { const last = e.results[e.results.length - 1]; got = [...last].map((a) => String(a.transcript || '').trim()).filter(Boolean); fin(); };
    r.onerror = fin; r.onend = fin;
    const t = setTimeout(fin, ms || 7000);
    BV.rec = r; BV.listening = true; bvStatus('🎙️ Listening…');
    try { r.start(); } catch { fin(); }
  });
}
const bvWait = (ms) => new Promise((r) => setTimeout(r, ms));

// ---------------------------------------------------------------- the game, step by step
const bvPlaces = (n) => n.toLocaleString('en-GB');
async function bvStep(s, my) {
  const live = () => BV.tok === my && BV.on;
  const g = s.bx, me = bxMe(s), c = g.cur, T = (i) => g.teams[i], car = lqLocalPids().length > 0, turnOf = car ? `${me.t.name}, your go. ` : '', catName = (n) => g.cats[Math.floor((n - 1) / g.cols)].n;
  /** Say `prompt`, listen, and let `handle(alternatives)` return a result (or null to try again with `retry`). */
  const ask = async (prompt, retry, handle) => {
    for (let i = 0; i < 4 && live(); i++) {
      await bvSay(i ? retry : prompt); if (!live()) return null;
      const alts = await bvListen(i ? 8000 : 9000); if (!live()) return null;
      if (!alts.length) { retry = 'I did not hear anything. ' + (retry || prompt); continue; }
      const r = handle(alts); if (r !== null && r !== undefined) return r;
    }
    if (live()) { await bvSay('Tap the microphone button when you are ready to try again.'); bvStatus('Tap 🎙 to try again'); }
    return null;
  };
  const confirm = async (text) => { // true / false / null
    const r = await ask(text, 'Say yes, or no.', (alts) => { for (const a of alts) { const y = BVP.yesno(a); if (y) return y; } return null; });
    return r === 'yes' ? true : r === 'no' ? false : null;
  };
  const first = (alts, f) => { for (const a of alts) { const r = f(a); if (r !== null && r !== undefined && r !== -1 && r !== false) return r; } return null; };

  if (g.step === 'seg' && s.bx.solo) {
    if (g.part !== 1) return;
    const rows = g.cats.map((x) => x.n).join(', ');
    const go = await ask(`Box Clever. ${g.total} boxes in ${g.cats.length} rows: ${rows}. Everyone starts on ${bxFmt(me.t.pot)}. Say go when you are ready.`, 'Say go to start.', (alts) => (first(alts, (a) => BVP.go(a)) ? true : null));
    if (go && live()) bxSend('next', 1);
    return;
  }
  if (g.step === 'pick') {
    const picker = T(g.pickTeam), mine = g.pickTeam === me.ti;
    if (!mine) return void (await bvSay(`${picker.name} is choosing a box.`));
    const rowsTold = BV.told.rows; BV.told.rows = true;
    const rows = g.cats.map((x, r) => `${x.n}, boxes ${r * g.cols + 1} to ${(r + 1) * g.cols}`).join('. ');
    let prompt = rowsTold ? `${turnOf}Your pick. Which box?` : `${turnOf}Your pick. ${rows}. Which box? Say a number, or a row and a place, like ${g.cats[g.cats.length - 1].n} three.`;
    for (let round = 0; round < 3 && live(); round++) {
      let note = '';
      const n = await ask(prompt, 'Say a box number, or a row and a place in it.', (alts) => {
        for (const a of alts) { const b = BVP.box(a, g.cats, g.cols, P.state.bx.board); if (b?.n) return b.n; if (b?.gone) note = `Box ${b.gone} has gone. `; if (b?.cat !== undefined) note = 'Which place in the row? '; }
        return note ? (void bvSay(note), null) : null;
      });
      if (!n || !live()) return;
      const ok = await confirm(`Box ${n}, ${catName(n)}. Say yes to lock it in.`);
      if (ok && live()) return void bxSend('pick', n, { go: true });
      if (ok === null) return;
      prompt = 'Which box instead?';
    }
    return;
  }
  if (g.step === 'stake') {
    const at = T(g.turn);
    if (g.turn !== me.ti) return void (await bvSay(`${at.name} is deciding how much to gamble.`));
    const t = me.t, chips = t.stakes || [], pot = t.pot;
    const opts = chips.slice(0, -1).map(bvPlaces).join(', ');
    let prompt = `${turnOf}Box ${c.num}, ${catName(c.num)}. You have ${bvPlaces(pot)}. How much to gamble? Say ${opts ? opts + ', ' : ''}any amount, or all in, which is ${bvPlaces(pot)}.`;
    for (let round = 0; round < 3 && live(); round++) {
      const amt = await ask(prompt, 'Say an amount, or all in.', (alts) => first(alts, (a) => BVP.stake(a, pot)));
      if (!amt || !live()) return;
      const ok = await confirm(amt >= pot ? `All in, ${bvPlaces(pot)}. Say yes to gamble it.` : `Gamble ${bvPlaces(amt)}. Say yes to lock it in.`);
      if (ok && live()) return void bxSend('stake', amt, { go: true });
      if (ok === null) return;
      prompt = 'How much instead?';
    }
    return;
  }
  if (g.step === 'ask' && c && c.mode !== 'host' && !c.locked) {
    const q = c.q, opts = q.opts, L = 'ABCD', mineAns = c.by === me.ti, who = T(c.by).name;
    if (q.m && q.m.k === 'tune') { await bvSay('Listen to the clip.'); for (let i = 0; i < 17 && live(); i++) await bvWait(1000); if (!live()) return; }
    const read = `${q.t}${opts ? ' ' + opts.map((o, i) => `${L[i]}: ${o}.`).join(' ') : ''}`;
    if (!mineAns) return void (await bvSay(`${read} ${who} is answering.`));
    if (opts) {
      const prompt = `${turnOf}${read} Say ${opts.map((_, i) => L[i]).join(', ')}${c.canPass ? ', or pass' : ''}.`;
      for (let round = 0; round < 3 && live(); round++) {
        const r = await ask(round ? 'Which one?' : prompt, `Say ${opts.map((_, i) => L[i]).join(', ')}${c.canPass ? ', or pass' : ''}.`, (alts) => {
          if (c.canPass && alts.some((a) => BVP.pass(a))) return 'pass';
          return first(alts, (a) => { const i = BVP.letter(a, opts); return i >= 0 ? i : null; });
        });
        if (r === null || !live()) return;
        if (r === 'pass') { const ok = await confirm(`Pass and lose half your stake. Say yes to pass.`); if (ok && live()) return void bxSend('pass', 1, { go: true }); if (ok === null) return; continue; }
        const ok = await confirm(`${L[r]}: ${opts[r]}. Say yes to lock it in.`);
        if (ok && live()) return void bxSend('ans', r, { go: true });
        if (ok === null) return;
      }
      return;
    }
    let prompt = `${turnOf}${read} Say your answer${c.canPass ? ', or pass' : ''}.`;
    for (let round = 0; round < 3 && live(); round++) {
      const said = await ask(prompt, 'Say your answer.', (alts) => (c.canPass && alts.some((a) => BVP.pass(a)) ? { pass: true } : { text: alts[0] }));
      if (!said || !live()) return;
      if (said.pass) { const ok = await confirm('Pass and lose half your stake. Say yes to pass.'); if (ok && live()) return void bxSend('pass', 1, { go: true }); if (ok === null) return; continue; }
      const ok = await confirm(`I heard: ${said.text}. Say yes to lock it in, or no to say it again.`);
      if (ok && live()) return void bxSend('ans', said.text, { go: true });
      if (ok === null) return;
      prompt = 'Say your answer again.';
    }
    return;
  }
  if (g.step === 'result' && c?.res) {
    const r = c.res, rt = T(r.team);
    const verdict = r.passed ? 'Passed.' : r.ok ? 'Correct!' : `Wrong. The answer was ${r.right}.`;
    await bvSay(`${verdict} ${rt.name} ${r.delta >= 0 ? 'plus' : 'minus'} ${bvPlaces(Math.abs(r.delta))}. ${rt.name} now has ${bvPlaces(rt.pot)}.`);
    if (!live()) return;
    await bvWait(900); if (live() && !P.state.bx.closing) bxSend('next', 1);
  }
}
/** Called at the end of bxBind: start the spoken part of a new step (once per step). */
function bxVoiceTick(s) {
  if (!s?.bx?.solo) return; // only the games played on phones (a team game on a host screen has captains and votes)
  bvButton();
  if (!BV.on) return;
  const g = s.bx, c = g.cur;
  const key = [g.step, g.turn, g.pickTeam, g.asked, c?.num, c?.q?.t, c?.q?.opts?.length, c?.locked ? 1 : 0, c?.by, c?.res ? 1 : 0].join('|');
  if (key === BV.key) return;
  BV.key = key; bvAbort(); const my = ++BV.tok;
  bvStep(s, my).catch(() => {});
}
/** The end of a game: the scores, read out. */
function bxVoiceFinal(s) {
  if (!s?.bx?.solo) return;
  bvButton();
  if (!BV.on || BV.key === 'final') return;
  BV.key = 'final'; bvAbort(); ++BV.tok;
  const t = (s.bx?.teams || []).map((x) => ({ n: x.name, v: Math.max(0, x.pot) - (x.loan || 0) })).sort((a, b) => b.v - a.v);
  if (t.length) bvSay(`Game over. ${t.map((x) => `${x.n} ${bvPlaces(x.v)}`).join('. ')}. ${t[0].n} wins!`);
}
function bvButton() {
  if (document.getElementById('bvbtn')) return;
  const wrap = document.createElement('div');
  wrap.id = 'bvbtn';
  wrap.style.cssText = 'position:fixed;left:0;right:0;bottom:0;z-index:50;display:flex;flex-direction:column;align-items:center;gap:4px;padding:6px 10px calc(6px + env(safe-area-inset-bottom,0px));pointer-events:none';
  wrap.innerHTML = '<div id="bvstat" style="max-width:100%;font-size:.8rem;color:#fff;background:rgba(20,16,50,.82);border-radius:10px;padding:3px 10px;display:none"></div><button type="button" id="bvtog" style="pointer-events:auto;border:0;border-radius:999px;padding:9px 16px;font:700 .9rem system-ui;background:#1b1544;color:#fff;box-shadow:0 2px 10px rgba(0,0,0,.35)"></button>';
  document.body.appendChild(wrap); document.body.style.paddingBottom = '70px'; // so the button never sits over the game's own buttons
  const tog = wrap.querySelector('#bvtog'), stat = wrap.querySelector('#bvstat');
  const paint = () => { tog.textContent = BV.on ? '🎙️ Hands-free: ON (tap to turn off)' : '🎙️ Hands-free'; tog.style.background = BV.on ? '#2e9d57' : '#1b1544'; };
  new MutationObserver(() => { stat.style.display = stat.textContent ? 'block' : 'none'; }).observe(stat, { childList: true, characterData: true, subtree: true });
  paint();
  tog.onclick = () => {
    BV.on = !BV.on; try { localStorage.setItem('lq_handsfree', BV.on ? '1' : '0'); } catch {}
    paint(); BV.key = ''; ++BV.tok; bvAbort();
    if (BV.on) {
      try { if (BV_TTS) { speechSynthesis.cancel(); speechSynthesis.speak(new SpeechSynthesisUtterance('')); } } catch {} // a tap is what lets the phone start talking
      if (!BV_TTS) toast('This browser cannot read aloud.', true);
      else if (!BV_SR) toast("This browser can read the game out but can't listen. Tap your answers.", false);
      if (P.state?.bx) { if (P.state.phase === 'final') { BV.key = ''; bxVoiceFinal(P.state); } else bxVoiceTick(P.state); }
    }
  };
}
