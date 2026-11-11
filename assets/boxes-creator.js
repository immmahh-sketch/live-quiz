// Box Clever creator for the quiz portal (index.html): make a game without a script.
// Choose the categories, the boxes in each, the bots (how much they know, how much they gamble) and the game code; the server
// (boxes_pool) picks the questions from the bank, this file puts them into a quiz and saves it.
window.LQBX = (() => {
  'use strict';
  const { $, $$, esc, uid } = LQ;
  const api = (...a) => LQ.api(...a);
  const shuffle = (a) => { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };

  // Each category is one or more of the bank's own categories, so a game can be made of anything the bank holds.
  const PRESETS = [
    { name: 'TV & Film', emoji: '🎬', banks: ['British sitcoms', 'Soaps', 'Reality TV', 'Quiz and game shows', 'Crime dramas', 'Friends', 'The Office and workplace comedies', 'British films', 'Action and blockbusters', 'Film quotes', 'Romantic comedies', 'Horror films', 'American TV', 'Doctor Who', "Children's TV", 'Television', 'Film'] },
    { name: 'Sport', emoji: '⚽', banks: ['Football', 'The football World Cup', 'The Olympics', 'Cricket', 'Rugby', 'Tennis and golf', 'Motorsport', 'Boxing and combat sports', 'Horse racing and darts', 'Sport'] },
    { name: 'In the news', emoji: '📰', banks: ['Covid-19', 'Days that shook the world', 'The 2010s', 'The 2000s', 'Famous firsts and records', 'Record breakers'] },
    { name: 'History', emoji: '🏛️', banks: ['British history', 'The Tudors', 'The World Wars', 'Ancient history', 'The 20th century', 'Famous people in history'] },
    { name: 'Disney', emoji: '🏰', banks: ['Disney films', 'Animated films'] },
    { name: 'Science', emoji: '🔬', banks: ['Space and astronomy', 'The human body', 'Science and technology', 'Animals', 'Nature and the environment', 'Computers and the internet', 'Maths and numbers', 'Science'] },
    { name: 'Celebrities', emoji: '⭐', banks: ['The Royal Family', 'The Oscars and award winners', 'One-hit wonders', 'Boy bands and girl groups', 'Reality TV', 'Pop music'] },
    { name: 'Music', emoji: '🎵', banks: ['Pop music', 'Rock music', 'The Beatles', 'UK number ones', 'Eurovision', 'Song lyrics', 'Classical music', 'Music'] },
    { name: 'Geography', emoji: '🌍', banks: ['UK geography', 'World geography', 'Capital cities', 'Famous landmarks', 'Flags of the world', 'Europe', 'The United States', 'Geography'] },
    { name: 'Food & Drink', emoji: '🍔', banks: ['Food and drink', 'British food', 'Beer, wine and spirits', 'Brands and logos'] },
    { name: 'QI', emoji: '🤔', banks: ['No Such Thing As a Fish facts', 'Famous firsts and records', 'Record breakers', 'Words and language', 'Mythology and legends', "Ripley's Believe It or Not"] },
    { name: 'Friends', emoji: '📺', banks: ['Friends'] },
    { name: 'The decades', emoji: '📼', banks: ['The 1960s', 'The 1970s', 'The 1980s', 'The 1990s', 'The 2000s', 'The 2010s'] },
    { name: 'Games & toys', emoji: '🎮', banks: ['Games and toys', 'Video games'] },
    { name: 'Local', emoji: '🏴', banks: ['Newcastle v Sunderland', 'The North East of England', 'Scotland', 'Wales', 'Ireland'] },
  ];
  const BOTS = [['Rex', '🐶', 80, 85, false], ['Max', '🦁', 60, 20, false], ['Ada', '🦉', 70, 50, true], ['Bo', '👾', 50, 65, false], ['Cy', '🐙', 90, 35, false], ['Dee', '🦖', 40, 75, true], ['Eli', '🐸', 65, 25, false], ['Fen', '🐼', 55, 55, false]];
  const knowLabel = (v) => (v >= 88 ? 'Quizmaster' : v >= 70 ? 'Sharp' : v >= 50 ? 'Average' : v >= 30 ? 'Rusty' : 'Clueless');
  const riskLabel = (v) => (v >= 80 ? 'Gambler' : v >= 60 ? 'Bold' : v >= 40 ? 'Middling' : v >= 20 ? 'Careful' : 'Plays safe');
  const fmt = (n) => Math.round(n).toLocaleString('en-GB');

  /** The next Friday-night style title, e.g. "Box Clever · 14 Nov". */
  const defaultTitle = () => 'Box Clever · ' + new Date().toLocaleDateString('en-GB', { day: 'numeric', month: 'short' });

  async function open() {
    let taken = new Set(), extraCats = [];
    try { const l = await api('list', {}); taken = new Set((l.quizzes || []).map((q) => q.gameCode).filter(Boolean)); } catch { /* the code is checked again when it is saved */ }
    try { const b = await api('bank_status', {}); extraCats = Object.entries(b.categories || {}).map(([n, c]) => [n, (c.types?.choice?.unused || 0) + (c.types?.text?.unused || 0)]).filter((x) => x[1] >= 25).sort((a, b) => a[0].localeCompare(b[0])); } catch { /* the presets still work */ }
    const st = { mode: 'hosted', cats: ['TV & Film', 'Sport', 'History', 'Science', 'Music'].map((n) => PRESETS.find((p) => p.name === n)), cols: 10, typed: 0.2, start: 10000, bonus: true, nbots: 2, bots: BOTS.map((b) => ({ name: b[0], emoji: b[1], know: b[2], risk: b[3], swing: b[4] })), autoBots: true, codeAuto: true, code: '', wu: false, wuCode: 'WARMUP' };
    const m = modal(`<h2 style="margin-top:0">📦 Make a Box Clever game</h2>
      <div class="field"><label>Title</label><input type="text" id="bx_title" value="${esc(defaultTitle())}"></div>
      <div class="field"><label>How it is played</label>
        <label class="check"><input type="radio" name="bx_mode" value="hosted" checked> Hosted: teams on the call, you run it from the big screen</label>
        <label class="check" style="margin-top:6px"><input type="radio" name="bx_mode" value="solo"> One phone: each player against the bots, on their own phone</label></div>
      <div class="field"><label>Categories <span class="muted" id="bx_catcount"></span></label><div id="bx_cats" class="row" style="flex-wrap:wrap;gap:6px"></div>
        <div class="row" style="margin-top:8px;gap:8px"><select id="bx_more" style="max-width:320px"><option value="">+ Add any other category from the bank…</option>${extraCats.map(([n, c]) => `<option value="${esc(n)}">${esc(n)} (${c})</option>`).join('')}</select></div>
        <div class="help">Two to seven. Each is a row of drawers; its questions are mixed easy, medium and hard, and never repeat an earlier Box Clever game.</div></div>
      <div class="row" style="gap:14px;flex-wrap:wrap">
        <div class="field" style="width:200px;margin:0"><label>Boxes in each category</label><input type="number" id="bx_cols" min="3" max="15" value="10"></div>
        <div class="field" style="width:220px;margin:0"><label>Typed answers (years, numbers)</label><select id="bx_typed"><option value="0">None: all multiple choice</option><option value="0.2" selected>A few</option><option value="0.35">More</option></select></div>
        <div class="field" style="width:200px;margin:0"><label>Everyone starts on</label><input type="number" id="bx_start" min="100" step="100" value="10000"></div></div>
      <div class="help" id="bx_size" style="margin-bottom:10px"></div>
      <label class="check" id="bx_bonusrow"><input type="checkbox" id="bx_bonus" checked> Bonus rounds between the four parts: Blockbusters, The Race, Draw It, and five Answer Smashes at the end</label>
      <div class="field mt"><label>🤖 Bots <span class="muted">(they join by themselves; each has its own knowledge and nerve)</span></label>
        <div class="row" style="gap:10px;align-items:center"><div class="field" style="width:110px;margin:0"><input type="number" id="bx_nbots" min="0" max="8" value="2"></div>
          <button class="btn btn-ghost btn-sm" data-pre="mixed">Mixed bag</button><button class="btn btn-ghost btn-sm" data-pre="safe">All careful</button><button class="btn btn-ghost btn-sm" data-pre="bold">All gamblers</button><button class="btn btn-ghost btn-sm" data-pre="sharp">All sharp</button></div>
        <div id="bx_botrows" style="margin-top:8px"></div>
        <label class="check" style="margin-top:6px"><input type="checkbox" id="bx_auto" checked> Add the bots to the lobby automatically</label></div>
      <div class="field mt"><label>🔑 Game code</label>
        <label class="check"><input type="radio" name="bx_code" value="auto" checked> Make a new code each time the game is hosted</label>
        <div class="row" style="margin-top:6px;gap:8px;align-items:center"><label class="check" style="margin:0"><input type="radio" name="bx_code" value="fixed"> Use this code every time:</label><input type="text" id="bx_codein" maxlength="10" style="width:150px;text-transform:uppercase" placeholder="e.g. BOXES7"><button class="btn btn-ghost btn-sm" id="bx_codemake">🎲 Create a code</button></div></div>
      <div class="field mt" id="bx_wurow" style="display:none"><label class="check"><input type="checkbox" id="bx_wu"> Open it as a warm-up game too: anyone with this code plays on their own phone, one go each</label>
        <div class="row" id="bx_wucodes" style="display:none;margin-top:6px;gap:8px"><div class="field" style="width:170px;margin:0"><label>Warm-up code</label><input type="text" id="bx_wucode" maxlength="12" value="WARMUP" style="text-transform:uppercase"></div></div></div>
      <div id="bx_msg" class="small" style="margin-top:10px"></div>
      <div class="row" style="justify-content:flex-end;gap:8px;margin-top:14px"><button class="btn btn-ghost" data-x>Cancel</button><button class="btn btn-primary btn-lg" id="bx_make">📦 Make the game</button></div>`);
    m.querySelector('.modal').style.maxWidth = '760px';
    const msg = (t, bad) => { const el = $('#bx_msg', m); el.className = 'small ' + (bad ? 'error' : 'muted'); el.textContent = t || ''; };

    const drawCats = () => {
      const on = new Set(st.cats.map((c) => c.name));
      $('#bx_cats', m).innerHTML = [...PRESETS, ...st.cats.filter((c) => !PRESETS.some((p) => p.name === c.name))].map((c) => `<button class="btn btn-sm ${on.has(c.name) ? 'btn-primary' : 'btn-ghost'}" data-cat="${esc(c.name)}">${c.emoji || '📦'} ${esc(c.name)}</button>`).join('');
      $$('[data-cat]', m).forEach((b) => b.onclick = () => {
        const i = st.cats.findIndex((c) => c.name === b.dataset.cat);
        if (i >= 0) st.cats.splice(i, 1); else if (st.cats.length >= 7) return msg('Seven categories at the most.', true); else st.cats.push(PRESETS.find((p) => p.name === b.dataset.cat) || { name: b.dataset.cat, emoji: '📦', banks: [b.dataset.cat] });
        msg(''); drawCats(); size();
      });
      $('#bx_catcount', m).textContent = `· ${st.cats.length} chosen`;
    };
    const size = () => {
      st.cols = Math.max(3, Math.min(15, Math.round(+$('#bx_cols', m).value || 10)));
      const total = st.cols * st.cats.length, parts = st.mode === 'hosted' && st.bonus ? [0.24, 0.5, 0.74, 1].map((f) => Math.round(total * f)) : [total];
      $('#bx_size', m).textContent = `${st.cats.length} categories × ${st.cols} boxes = ${total} boxes${parts.length > 1 ? `, played in four parts, with a bonus round after box ${parts.slice(0, 3).join(', ')} and then the finish` : ''}. The board stays this size however many people play.`;
    };
    const drawBots = () => {
      st.nbots = Math.max(0, Math.min(8, Math.round(+$('#bx_nbots', m).value || 0)));
      $('#bx_botrows', m).innerHTML = st.bots.slice(0, st.nbots).map((b, i) => `<div class="row" style="gap:10px;align-items:center;flex-wrap:wrap;margin-bottom:6px" data-bot="${i}">
        <span style="font-size:1.4rem">${esc(b.emoji)}</span><input type="text" data-bn="${i}" value="${esc(b.name)}" maxlength="12" style="width:110px">
        <label class="small" style="min-width:210px">Knowledge <b data-kl="${i}">${knowLabel(b.know)} · ${b.know}%</b><br><input type="range" min="10" max="95" step="5" value="${b.know}" data-bk="${i}" style="width:100%"></label>
        <label class="small" style="min-width:210px">Risk-taking <b data-rl="${i}">${riskLabel(b.risk)} · ${b.risk}%</b><br><input type="range" min="0" max="100" step="5" value="${b.risk}" data-br="${i}" style="width:100%"></label>
        <label class="check small" title="A mixer changes its mind: sometimes it bets big, sometimes small"><input type="checkbox" data-bs="${i}" ${b.swing ? 'checked' : ''}> Mixer</label></div>`).join('') || '<div class="help">No bots: only the people playing.</div>';
      $$('[data-bn]', m).forEach((el) => el.oninput = () => { st.bots[+el.dataset.bn].name = el.value; });
      $$('[data-bk]', m).forEach((el) => el.oninput = () => { const b = st.bots[+el.dataset.bk]; b.know = +el.value; $(`[data-kl="${el.dataset.bk}"]`, m).textContent = `${knowLabel(b.know)} · ${b.know}%`; });
      $$('[data-br]', m).forEach((el) => el.oninput = () => { const b = st.bots[+el.dataset.br]; b.risk = +el.value; $(`[data-rl="${el.dataset.br}"]`, m).textContent = `${riskLabel(b.risk)} · ${b.risk}%`; });
      $$('[data-bs]', m).forEach((el) => el.onchange = () => { st.bots[+el.dataset.bs].swing = el.checked; });
    };
    const preset = (kind) => {
      st.bots.forEach((b, i) => { const base = BOTS[i]; if (kind === 'mixed') Object.assign(b, { know: base[2], risk: base[3], swing: base[4] }); else if (kind === 'safe') Object.assign(b, { know: 60, risk: 15, swing: false }); else if (kind === 'bold') Object.assign(b, { know: 60, risk: 90, swing: false }); else if (kind === 'sharp') Object.assign(b, { know: 90, risk: 55, swing: false }); });
      if (!st.nbots) $('#bx_nbots', m).value = 2; drawBots();
    };
    const mode = () => {
      st.mode = $('[name=bx_mode]:checked', m).value;
      $('#bx_bonusrow', m).style.display = st.mode === 'hosted' ? '' : 'none';
      $('#bx_wurow', m).style.display = st.mode === 'solo' ? '' : 'none';
      const s = $('#bx_start', m); if (+s.value === 10000 && st.mode === 'solo') s.value = 1000; else if (+s.value === 1000 && st.mode === 'hosted') s.value = 10000;
      if (st.mode === 'solo' && st.cols === 10 && +$('#bx_cols', m).value === 10) $('#bx_cols', m).value = 5;
      size();
    };
    $$('[name=bx_mode]', m).forEach((r) => r.onchange = mode);
    $('#bx_cols', m).oninput = size;
    $('#bx_bonus', m).onchange = (e) => { st.bonus = e.target.checked; size(); };
    $('#bx_nbots', m).oninput = drawBots;
    $$('[data-pre]', m).forEach((b) => b.onclick = () => preset(b.dataset.pre));
    $('#bx_more', m).onchange = (e) => { const n = e.target.value; e.target.value = ''; if (!n || st.cats.some((c) => c.name === n)) return; if (st.cats.length >= 7) return msg('Seven categories at the most.', true); st.cats.push({ name: n.slice(0, 24), emoji: '📦', banks: [n] }); msg(''); drawCats(); size(); };
    $('#bx_wu', m).onchange = (e) => { $('#bx_wucodes', m).style.display = e.target.checked ? 'flex' : 'none'; };
    $('#bx_codemake', m).onclick = () => {
      let c; do { c = LQ.newCode(); } while (taken.has(c));
      $('#bx_codein', m).value = c; $('[name=bx_code][value=fixed]', m).checked = true; msg('');
    };
    $('#bx_codein', m).oninput = (e) => { e.target.value = e.target.value.toUpperCase().replace(/[^A-Z0-9]/g, ''); $('[name=bx_code][value=fixed]', m).checked = true; };
    drawCats(); drawBots(); mode();
    $('[data-x]', m).onclick = () => m.remove();

    $('#bx_make', m).onclick = async () => {
      const btn = $('#bx_make', m);
      const title = $('#bx_title', m).value.trim() || defaultTitle(), solo = st.mode === 'solo', cols = st.cols, rows = st.cats.length;
      const typed = +$('#bx_typed', m).value, start = Math.max(100, Math.round(+$('#bx_start', m).value || (solo ? 1000 : 10000)));
      const fixed = $('[name=bx_code]:checked', m).value === 'fixed', code = $('#bx_codein', m).value.trim().toUpperCase();
      if (rows < 2) return msg('Pick at least two categories.', true);
      if (fixed && !/^[A-Z0-9]{4,10}$/.test(code)) return msg('A game code is 4 to 10 letters or numbers.', true);
      if (fixed && /^(TEST|VIEW)/.test(code)) return msg('A game code cannot start with TEST or VIEW.', true);
      if (fixed && taken.has(code)) return msg(`The code ${code} already belongs to another game.`, true);
      const wantWu = solo && $('#bx_wu', m).checked, wuCode = $('#bx_wucode', m).value.toUpperCase().replace(/[^A-Z0-9]/g, '').slice(0, 12);
      if (wantWu && wuCode.length < 3) return msg('A warm-up code is 3 to 12 letters or numbers.', true);
      const withBonus = !solo && $('#bx_bonus', m).checked;
      btn.disabled = true; msg('Picking the questions from the bank…');
      try {
        const pool = await api('boxes_pool', { cats: st.cats.map((c) => ({ name: c.name, emoji: c.emoji, banks: c.banks })), cols, typed, bonus: withBonus }, { timeout: 90000 });
        msg('Putting the game together…');
        const total = cols * rows, cuts = withBonus ? [0.24, 0.5, 0.74, 1].map((f) => Math.round(total * f)) : [total];
        const settings = { ...LQ.DEFAULT_SETTINGS };
        const rounds = [], questions = [];
        const round = (t, intro, items) => { const id = uid('r'), mix = {}; for (const q of items) { q.round = id; mix[q.type] = (mix[q.type] || 0) + 1; } rounds.push({ id, title: t, intro, brief: '', mix, count: items.length, types: Object.keys(mix), practice: false }); questions.push(...items); return rounds[rounds.length - 1]; };
        const slide = (text, body) => ({ id: uid('q'), type: 'slide', text, body, time: 20, media: { kind: 'none' } });
        const box = (part, extra) => ({ id: uid('q'), type: 'boxes', text: 'Box Clever', time: 0, media: { kind: 'none' }, partial: false, part, ...extra });
        const nq = (type, extra) => ({ ...LQ.newQuestion(type, settings), ...extra });
        const first = { cats: pool.cats.map((c) => ({ name: c.name, emoji: c.emoji, qs: c.qs })), reserve: pool.reserve, hostq: pool.hostq, rows, cols, cuts, start, finish: withBonus && (pool.bonus?.smash || []).length ? 'On to the Answer Smashes ▶' : 'See the result ▶', ...(solo ? { solo: true } : {}) };
        if (!solo) round('Welcome', '', [slide('📦 Box Clever', `Tonight you play in teams.\n\n${total} boxes. ${rows} categories. One big gamble.\n\nGrab your phone: you will be put on a team.`),
          slide('How it works', `Every team starts with ${fmt(start)} points.\n\nYour captain picks a box and decides how much to gamble.\n\nRight: you win the stake. Wrong: you lose it.\n\nNot sure? Pass for half the stake, but everyone sees the question.\n\nFive powers, once each. Use them wisely.`)]);
        round('Box Clever' + (withBonus ? ' 1' : ''), solo ? `You against ${st.nbots ? 'the bots' : 'the clock'}. ${total} boxes.` : 'The first dozen boxes.', [box(1, first)]);
        let smashRound = null;
        if (withBonus) {
          const bonus = pool.bonus || {};
          const bank = (list) => (list || []).map((x) => ({ id: uid('b'), text: x.text, options: x.options, difficulty: x.difficulty }));
          round('Blockbusters', 'Everyone plays. Your points go into your team pot.', [nq('blockbusters', { text: 'Blockbusters: General knowledge', bank: bank(bonus.bb), category: 'General knowledge', difficulty: 'medium' })]);
          round('Box Clever 2', 'Back to the boxes.', [box(2)]);
          round('The Race', 'Everyone races. Your points go into your team pot.', [nq('race', { text: 'The Race: general knowledge', bank: bank(bonus.race).map(({ difficulty, ...r }) => r), category: 'General knowledge', difficulty: 'medium' })]);
          round('Box Clever 3', 'Three quarters of the way through.', [box(3)]);
          round('Draw It', 'Everyone guesses. Your points go into your team pot.', [nq('draw', { text: 'Draw It', words: shuffle(LQ.DRAW_WORDS).slice(0, 15), category: 'Draw It', difficulty: 'easy' })]);
          round('Box Clever 4', 'Every last box.', [box(4)]);
          if ((bonus.smash || []).length) { smashRound = round('Double Points: Answer Smash', 'Double points! Every right answer counts twice, and goes into your team pot.', bonus.smash); smashRound.double = true; }
        }
        const problems = []; questions.forEach((q, i) => { const p = LQ.validate(q); if (p.length) problems.push(`${i + 1} ${q.type}: ${p.join('; ')}`); });
        if (problems.length) throw new Error('Something was not finished: ' + problems.slice(0, 3).join(' | '));
        settings.boxes = { rows, cols, start, autoBots: $('#bx_auto', m).checked, bots: st.bots.slice(0, st.nbots).map((b) => ({ name: (b.name || 'Bot').trim().slice(0, 12), emoji: b.emoji, skill: b.know / 100, risk: b.risk / 100, swing: b.swing ? 0.6 : 0.2 })) };
        if (fixed) settings.gameCode = { auto: false, code };
        if (wantWu) settings.warmup = { code: wuCode, open: true, fun: true, replay: false, bots: st.nbots, forQuiz: null, from: null, until: null, season: 's-boxclever-' + new Date().toISOString().slice(0, 10) };
        settings.rounds = rounds;
        msg('Saving…');
        const saved = await api('save', { quiz: { title, settings, questions } });
        const id = saved.quiz?.id;
        let marked = 0; try { if (id) marked = (await api('boxes_mark', { quizId: id, ids: pool.ids }, { timeout: 60000 })).marked || 0; } catch (e) { console.warn('boxes_mark', e); }
        m.remove();
        const short = (pool.warnings || []).join(' ');
        toast(`📦 ${title} is ready: ${total} boxes${st.nbots ? `, ${st.nbots} bot${st.nbots === 1 ? '' : 's'}` : ''}${fixed ? `, code ${code}` : ''}.${short ? ' ' + short : ''}`);
        try { S.quizzes = (await api('list')).quizzes; renderList(); } catch { location.reload(); }
      } catch (e) { btn.disabled = false; msg(e.message || String(e), true); }
    };
  }
  return { open, PRESETS };
})();
