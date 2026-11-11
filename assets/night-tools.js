// Tools for hosting a quiz night, for the quiz portal (index.html):
//   hostUi*   Settings > Host screen / Host panel: choose the buttons on the host screen's bottom bar and on the host's phone panel.
//   cue*      a stunt prompt on any item: pops up on the host panel as the item comes up (the "I Literally Just Told You" cues).
//   iljty()   the "Add I Literally Just Told You" form: stunts to plant, when to do them, and the questions to ask about them later.
//   traitorsNight()  the "Make a Traitors night" form: a whole quiz with the Traitors set up, built from the bank.
// It uses the portal's own globals (S, modal, toast, snap, touch, renderQList, ...) when its functions are called.
window.LQNT = (() => {
  'use strict';
  const { $, $$, esc, uid } = LQ;
  const shuffle = (a) => { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
  const typeLabel = (q) => (q.type === 'slide' ? (q.break ? 'Break' : 'Slide') : (TYPES[q.kind || q.type]?.label || q.type));

  // ------------------------------------------------------------------ host screen and host panel settings
  const sameList = (a, b) => a.length === b.length && a.every((x, i) => x === b[i]);
  /** The two sections for the Settings pop-up. Draw them with hostUiBind(m, s) once they are on the page; hostUiRead(s) writes the choice back. */
  function hostUiHtml() {
    return `<div class="field mt" id="hui"><label>🖥 Host screen settings</label>
        <div class="help" style="margin-top:0">The buttons along the bottom of the host screen. Tick the ones you want. "End game" and the buttons for the item on screen are always there.</div>
        <div id="hui_screen" class="row" style="flex-wrap:wrap;gap:4px 16px"></div>
        <button class="btn btn-ghost btn-sm" type="button" id="hui_sreset" style="margin-top:6px">Back to the usual buttons</button></div>
      <div class="field mt"><label>📱 Host panel settings</label>
        <div class="help" style="margin-top:0">The panel on your phone while you host (📱 Host panel on the quiz's card). "Next" is always the big button on top; stunt prompts pop up over it. Add, remove and reorder the rest.</div>
        <div id="hui_panel"></div>
        <div class="row" style="gap:8px;margin-top:6px"><select id="hui_add" style="max-width:300px"></select><button class="btn btn-sm" type="button" id="hui_addgo">+ Add this button</button><button class="btn btn-ghost btn-sm" type="button" id="hui_preset">Back to the usual buttons</button></div></div>`;
  }
  function hostUiBind(m, s) {
    const st = { screen: LQ.HOSTUI.list(s, 'screen').slice(), panel: LQ.HOSTUI.list(s, 'panel').slice() };
    m._hui = st;
    const info = (kind, id) => LQ.HOSTUI[kind].find((x) => x.id === id);
    const draw = () => {
      $('#hui_screen', m).innerHTML = LQ.HOSTUI.screen.map((b) => `<label class="check" style="margin:0"><input type="checkbox" data-hs="${b.id}" ${st.screen.includes(b.id) ? 'checked' : ''}> ${b.icon} ${esc(b.label)}</label>`).join('');
      $$('[data-hs]', m).forEach((el) => el.onchange = () => { st.screen = LQ.HOSTUI.screen.map((b) => b.id).filter((id) => (id === el.dataset.hs ? el.checked : st.screen.includes(id))); });
      $('#hui_panel', m).innerHTML = st.panel.length ? st.panel.map((id, i) => { const b = info('panel', id); return `<div class="row" style="gap:6px;align-items:center;margin-bottom:4px"><span style="min-width:2em;text-align:center">${b.icon}</span><span class="grow">${esc(b.label)}${b.big ? ' <span class="muted small">(big button)</span>' : ''}</span><button class="btn btn-ghost btn-sm" type="button" data-hu="${i}" ${i ? '' : 'disabled'} title="Move up">↑</button><button class="btn btn-ghost btn-sm" type="button" data-hd="${i}" ${i < st.panel.length - 1 ? '' : 'disabled'} title="Move down">↓</button><button class="btn btn-ghost btn-sm" type="button" data-hx="${i}" title="Take it off the panel" style="color:var(--bad)">✕</button></div>`; }).join('') : '<div class="help">Only the Next button.</div>';
      const free = LQ.HOSTUI.panel.filter((b) => !st.panel.includes(b.id));
      $('#hui_add', m).innerHTML = free.length ? free.map((b) => `<option value="${b.id}">${b.icon} ${esc(b.label)}</option>`).join('') : '<option value="">Every button is on the panel</option>';
      $('#hui_addgo', m).disabled = !free.length;
      $$('[data-hu]', m).forEach((el) => el.onclick = () => { const i = +el.dataset.hu; [st.panel[i - 1], st.panel[i]] = [st.panel[i], st.panel[i - 1]]; draw(); });
      $$('[data-hd]', m).forEach((el) => el.onclick = () => { const i = +el.dataset.hd; [st.panel[i + 1], st.panel[i]] = [st.panel[i], st.panel[i + 1]]; draw(); });
      $$('[data-hx]', m).forEach((el) => el.onclick = () => { st.panel.splice(+el.dataset.hx, 1); draw(); });
    };
    $('#hui_addgo', m).onclick = () => { const id = $('#hui_add', m).value; if (id && !st.panel.includes(id)) { st.panel.push(id); draw(); } };
    $('#hui_preset', m).onclick = () => { st.panel = LQ.HOSTUI.defaults.panel.slice(); draw(); };
    $('#hui_sreset', m).onclick = () => { st.screen = LQ.HOSTUI.defaults.screen.slice(); draw(); };
    draw();
  }
  /** Writes the chosen buttons into settings (nothing is stored for a list that is just the usual one). */
  function hostUiRead(m, s) {
    const st = m._hui; if (!st) return;
    const ui = { ...(s.hostUi || {}) };
    for (const k of ['screen', 'panel']) { if (sameList(st[k], LQ.HOSTUI.defaults[k])) delete ui[k]; else ui[k] = st[k]; }
    if (Object.keys(ui).length) s.hostUi = ui; else delete s.hostUi;
  }

  // ------------------------------------------------------------------ a stunt prompt on one item
  function cueHtml(q) {
    const c = q.cue, brk = q.type === 'slide' && q.break;
    return `<div class="field" id="cueBox"><label class="check"><input type="checkbox" id="cue_on" ${c ? 'checked' : ''}> 🎬 Show me a stunt prompt on my phone when this comes up</label>
      <div id="cue_f" style="${c ? '' : 'display:none'}"><div class="row"><div class="field grow"><label>Prompt title</label><input type="text" id="cue_title" value="${esc(c?.title || '')}" placeholder="e.g. Stunt 2: the hotel call"></div>
        ${brk ? `<div class="field" style="width:230px"><label>Show it with this many seconds of the break left</label><input type="number" id="cue_bl" min="10" max="3600" value="${c?.breakLeft || 180}"></div>` : ''}</div>
        <div class="field"><label>What to do or say</label><textarea id="cue_say" rows="3" placeholder="e.g. Take a fake call from the hotel on camera: a guest in room 23 says the people next door have been singing since six.">${esc(c?.say || '')}</textarea></div>
        <div class="help">It appears big and green on the host panel as this item comes up (the item is next, or on screen), until you press Done. Open the panel with 📱 Host panel on the quiz's card while it is hosted.</div></div></div>`;
  }
  function cueBind(root, q, touch) {
    const on = $('#cue_on', root); if (!on) return;
    const read = () => { q.cue = { ...(q.cue || {}), n: q.cue?.n || nextCueN(), title: $('#cue_title', root).value.trim(), say: $('#cue_say', root).value }; if ($('#cue_bl', root)) q.cue.breakLeft = LQ.clamp(+$('#cue_bl', root).value || 180, 10, 3600); else delete q.cue.breakLeft; S.quiz.settings.hostPanel = true; touch(); };
    on.onchange = () => { $('#cue_f', root).style.display = on.checked ? '' : 'none'; if (on.checked) read(); else { delete q.cue; touch(); } };
    ['#cue_title', '#cue_say', '#cue_bl'].forEach((sel) => { const el = $(sel, root); if (el) el.oninput = read; });
  }
  const nextCueN = () => Math.max(0, ...S.quiz.questions.map((q) => +q.cue?.n || 0)) + 1;

  // ------------------------------------------------------------------ I Literally Just Told You
  // Each starter is a stunt to plant, a question about it for later, and the answers. Everything is editable.
  const IDEAS = [
    { name: 'A fake call from the hotel', title: 'The hotel call', say: 'Take a fake call on camera, in your own words: a guest in room 23 says the people next door have been singing since six. Say the room number clearly, twice, and sound fed up.', q: 'I took a call from the hotel. Which room was the guest complaining from?', type: 'text', right: '23', alts: 'room 23, twenty-three' },
    { name: 'Eat something noisy', title: 'The snack', say: 'Eat a sausage roll while you read the next question, as if nothing is odd. Do not mention it. If anybody asks, say you were hungry.', q: 'What was I eating during that last round?', type: 'text', right: 'A sausage roll', alts: 'sausage roll, a sausage roll' },
    { name: 'A made-up number', title: 'The step count', say: 'Say, as if it just occurred to you: "My watch says I have done 14,286 steps today." Say the number clearly.', q: 'How many steps did I say my watch said I had done today?', type: 'nearest', right: '14286', unit: 'steps', spread: '5000' },
    { name: 'A Post-it behind you', title: 'The Post-it', say: 'Before this round, stick a Post-it with the number 37 on the wall behind you. Do not point at it.', q: 'What number was on the Post-it note on the wall behind me?', type: 'nearest', right: '37', unit: '', spread: '30' },
    { name: 'Hum a theme tune', title: 'The humming', say: 'Quietly hum the Match of the Day theme under your breath during the whole round.', q: 'Which TV theme tune was I humming?', type: 'choice', right: 'Match of the Day', wrong: ['Countdown', 'EastEnders', 'Grandstand'] },
    { name: 'A story about a relative', title: 'The nana story', say: 'While they answer, say: "My nana was convinced that was real. She rang the police to report it."', q: 'Who did I say rang the police?', type: 'choice', right: 'My nana', wrong: ['My mam', 'My auntie Pat', 'My next-door neighbour'] },
    { name: 'Something odd on camera', title: 'The bow tie', say: 'Put on a red bow tie before this round and say nothing about it.', q: 'What was I wearing that was out of the ordinary?', type: 'choice', right: 'A red bow tie', wrong: ['A pirate hat', 'Novelty glasses', 'A false moustache'] },
    { name: 'A word you keep slipping in', title: 'The word', say: 'Work the word "flamingo" into three of your lines in this round, and carry on as if you had said nothing odd.', q: 'Which animal did I keep mentioning?', type: 'text', right: 'Flamingo', alts: 'flamingos, a flamingo' },
  ];
  function iljty() {
    const qz = S.quiz; if (!qz) return;
    const items = qz.questions.map((q, i) => ({ i, q, label: `${i + 1}. ${(qz.rounds.find((r) => r.id === q.round)?.title || 'Round')} · ${typeLabel(q)}${q.text ? ': ' + String(q.text).replace(/\s+/g, ' ').slice(0, 48) : ''}` }));
    const stunts = [], fb = qz.rounds.findIndex((r) => qz.questions.some((q) => q.round === r.id && q.break));
    // the default place: straight before the first break, or before the Round Table that comes just ahead of it (the vote follows the questions)
    let dflt = fb; if (fb > 0) { const its = qz.questions.filter((q) => q.round === qz.rounds[fb - 1].id); if (its.length && its.every((q) => q.type === 'slide' && q.theme === 'traitors')) dflt = fb - 1; }
    const firstBreak = dflt >= 0 ? qz.rounds[dflt] : null;
    const m = modal(`<h2 style="margin-top:0">🎬 Add "I Literally Just Told You"</h2>
      <p class="muted" style="margin-top:0">Plant something during the night, then ask about it later. You choose what you will do and when; the prompt pops up on your phone's host panel at that moment, and the questions go in a round of their own. Players cannot look the answers up: they have to have been listening.</p>
      <div class="field"><label>Ideas to start from <span class="muted">(tap one, then change it to suit you)</span></label><div id="il_ideas" class="row" style="flex-wrap:wrap;gap:6px"></div></div>
      <div id="il_list"></div>
      <div class="row" style="gap:8px;margin:6px 0 12px"><button class="btn btn-sm" id="il_add">+ A blank stunt</button></div>
      <div class="row" style="gap:12px;flex-wrap:wrap"><div class="field grow" style="min-width:220px"><label>Round title</label><input type="text" id="il_title" value="I Literally Just Told You"></div>
        <div class="field grow" style="min-width:240px"><label>Ask the questions</label><select id="il_where"><option value="">At the very end</option>${qz.rounds.map((r, i) => `<option value="${r.id}" ${firstBreak && r.id === firstBreak.id ? 'selected' : ''}>Straight before round ${i + 1}: ${esc(r.title || 'Untitled')}</option>`).join('')}</select></div></div>
      <div class="field"><label>Intro on the screen</label><input type="text" id="il_intro" value="Questions about things that happened earlier tonight. Were you listening?"></div>
      <div id="il_msg" class="small error" style="min-height:1.2em"></div>
      <div class="row" style="justify-content:flex-end;gap:8px"><button class="btn btn-ghost" data-x>Cancel</button><button class="btn btn-primary btn-lg" id="il_make">Add to the quiz</button></div>`);
    $('.modal', m).style.maxWidth = '820px';
    const msg = (t) => { $('#il_msg', m).textContent = t || ''; };
    const when = (s) => `<select data-k="at">${items.map((x) => `<option value="${x.i}" ${s.at === x.i ? 'selected' : ''}>${esc(x.label)}</option>`).join('')}</select>`;
    const draw = () => {
      $('#il_ideas', m).innerHTML = IDEAS.map((d, i) => `<button class="btn btn-ghost btn-sm" data-idea="${i}">${esc(d.name)}</button>`).join('');
      $$('[data-idea]', m).forEach((b) => b.onclick = () => { const d = IDEAS[+b.dataset.idea]; stunts.push({ ...d, wrong: (d.wrong || ['', '', '']).slice(), alts: d.alts || '', at: defaultAt(), bl: 180 }); draw(); });
      $('#il_list', m).innerHTML = stunts.length ? stunts.map((s, n) => `<div class="card" data-s="${n}" style="margin-bottom:10px;padding:12px">
        <div class="row" style="align-items:center"><b>Stunt ${n + 1}</b><div class="grow"></div><button class="btn btn-ghost btn-sm" data-del="${n}" style="color:var(--bad)">Remove</button></div>
        <div class="row" style="gap:10px;flex-wrap:wrap"><div class="field grow" style="min-width:200px"><label>Name (the pop-up's title)</label><input type="text" data-k="title" value="${esc(s.title)}"></div>
          <div class="field grow" style="min-width:260px"><label>When I do it: as this comes up</label>${when(s)}</div>${items[s.at]?.q.break ? `<div class="field" style="width:190px"><label>Seconds of break left</label><input type="number" data-k="bl" min="10" max="3600" value="${s.bl}"></div>` : ''}</div>
        <div class="field"><label>What I will do or say</label><textarea data-k="say" rows="3">${esc(s.say)}</textarea></div>
        <div class="field"><label>The question to ask later</label><input type="text" data-k="q" value="${esc(s.q)}"></div>
        <div class="row" style="gap:10px;flex-wrap:wrap"><div class="field" style="width:200px"><label>Answered by</label><select data-k="type"><option value="choice" ${s.type === 'choice' ? 'selected' : ''}>Choosing from four</option><option value="text" ${s.type === 'text' ? 'selected' : ''}>Typing it</option><option value="nearest" ${s.type === 'nearest' ? 'selected' : ''}>A number: nearest wins</option></select></div>
          <div class="field grow" style="min-width:180px"><label>The right answer</label><input type="text" data-k="right" value="${esc(s.right)}"></div>
          ${s.type === 'choice' ? [0, 1, 2].map((k) => `<div class="field grow" style="min-width:140px"><label>Wrong answer ${k + 1}</label><input type="text" data-w="${k}" value="${esc(s.wrong?.[k] || '')}"></div>`).join('') : ''}
          ${s.type === 'text' ? `<div class="field grow" style="min-width:220px"><label>Also accept (commas between)</label><input type="text" data-k="alts" value="${esc(s.alts || '')}"></div>` : ''}
          ${s.type === 'nearest' ? `<div class="field" style="width:120px"><label>Unit</label><input type="text" data-k="unit" value="${esc(s.unit || '')}"></div><div class="field" style="width:160px"><label>Full marks within</label><input type="number" data-k="spread" value="${esc(s.spread || '')}"></div>` : ''}</div></div>`).join('') : '<p class="muted small">Tap an idea above, or add a blank stunt.</p>';
      $$('[data-s]', m).forEach((card) => {
        const s = stunts[+card.dataset.s];
        $$('[data-k]', card).forEach((el) => { el.onchange = el.oninput = () => { s[el.dataset.k] = el.dataset.k === 'at' ? +el.value : el.value; if (['type', 'at'].includes(el.dataset.k)) { const keep = $('#il_title', m).value; draw(); $('#il_title', m).value = keep; } }; });
        $$('[data-w]', card).forEach((el) => el.oninput = () => { s.wrong[+el.dataset.w] = el.value; });
        $('[data-del]', card).onclick = () => { stunts.splice(+card.dataset.s, 1); draw(); };
      });
    };
    // by default a stunt happens during the first question of the quiz that is not a slide
    const defaultAt = () => Math.max(0, items.findIndex((x) => x.q.type !== 'slide'));
    $('#il_add', m).onclick = () => { stunts.push({ name: '', title: '', say: '', q: '', type: 'choice', right: '', wrong: ['', '', ''], alts: '', unit: '', spread: '', at: defaultAt(), bl: 180 }); draw(); };
    $('[data-x]', m).onclick = () => m.remove();
    $('#il_make', m).onclick = () => {
      if (!stunts.length) return msg('Add at least one stunt first.');
      const R = { id: uid('r'), title: $('#il_title', m).value.trim() || 'I Literally Just Told You', intro: $('#il_intro', m).value.trim(), brief: '', practice: false, iljty: Math.max(0, ...qz.rounds.map((r) => +r.iljty || 0)) + 1 };
      const made = [];
      for (const [n, s] of stunts.entries()) {
        const text = s.q.trim(), right = String(s.right).trim();
        if (!text || !right) return msg(`Stunt ${n + 1} needs a question and a right answer.`);
        if (!s.say.trim()) return msg(`Stunt ${n + 1}: write down what you will do or say, so the prompt has something to show.`);
        const base = { ...LQ.newQuestion(s.type, qz.settings), id: uid('q'), round: R.id, text, handMade: true, category: R.title, difficulty: 'medium', media: { kind: 'none' }, partial: false };
        let q;
        if (s.type === 'choice') {
          const wrong = (s.wrong || []).map((x) => x.trim()).filter(Boolean);
          if (wrong.length < 1) return msg(`Stunt ${n + 1}: give at least one wrong answer.`);
          const opts = shuffle([right, ...wrong].map((t) => ({ id: uid('o'), text: t })));
          q = { ...base, options: opts, correct: opts.find((o) => o.text === right).id };
        } else if (s.type === 'text') q = { ...base, answers: [right, ...String(s.alts || '').split(',').map((x) => x.trim()).filter(Boolean)] };
        else {
          if (!Number.isFinite(LQ.parseNum ? LQ.parseNum(right) : +right)) return msg(`Stunt ${n + 1}: the right answer has to be a number.`);
          q = { ...base, answer: String(LQ.parseNum ? LQ.parseNum(right) : +right), unit: (s.unit || '').trim(), spread: +s.spread || 0 };
        }
        const bad = LQ.validate(q); if (bad.length) return msg(`Stunt ${n + 1}: ${bad.join('; ')}`);
        made.push(q);
      }
      const u = snap('add I Literally Just Told You');
      // the questions: a round of their own, before the round chosen (or at the end)
      const at = $('#il_where', m).value, ri = at ? qz.rounds.findIndex((r) => r.id === at) : -1;
      R.types = [...new Set(made.map((q) => q.type))]; R.mix = {}; for (const q of made) R.mix[q.type] = (R.mix[q.type] || 0) + 1; R.count = made.length;
      if (ri >= 0) qz.rounds.splice(ri, 0, R); else qz.rounds.push(R);
      const qi = at ? qz.questions.findIndex((q) => q.round === at) : -1;
      if (qi >= 0) qz.questions.splice(qi, 0, ...made); else qz.questions.push(...made);
      // the prompts: on the items each stunt happens during (a second stunt there is added under the first)
      const base0 = nextCueN();
      stunts.forEach((s, n) => {
        const target = qz.questions.find((q) => q.id === items[s.at].q.id); if (!target) return;
        const cue = { n: base0 + n, title: `Stunt ${base0 + n}: ${s.title.trim() || 'do it now'}`, say: s.say.trim() };
        if (target.type === 'slide' && target.break) cue.breakLeft = LQ.clamp(+s.bl || 180, 10, 3600);
        if (target.cue && !target.cue.breakLeft === !cue.breakLeft) { target.cue = { ...target.cue, title: `${target.cue.title} + ${cue.title}`, say: `${target.cue.say}\n\n${cue.say}` }; } else target.cue = cue;
      });
      qz.settings.hostPanel = true;
      touch(); m.remove(); renderQList(); renderQForm();
      toast(`Added ${made.length} question${made.length === 1 ? '' : 's'} and ${stunts.length} stunt prompt${stunts.length === 1 ? '' : 's'}. Host with 📱 Host panel open on your phone: each prompt pops up when its moment comes.`, false, undoAct(u));
    };
    draw();
  }

  // ------------------------------------------------------------------ Make a Traitors night
  const NIGHT_CATS = ['General knowledge', 'TV & Film', 'Music', 'Sport', 'History', 'Science', 'Geography', 'Food & Drink', 'Celebrities', 'Disney', 'Friends', 'The 1990s', 'The 2000s', 'Animals', 'Games and toys'];
  const GAMES = [['potato', 'Hot Potato'], ['chase', 'The Chase'], ['koth', 'King of the Hill'], ['blockbusters', 'Blockbusters'], ['race', 'The Race']];
  const STYLES = { choice: { choice: 1 }, mixed: { choice: 5, text: 2, tf: 1 }, wide: { choice: 4, text: 2, tf: 1, order: 1 } };
  async function traitorsNight() {
    let extra = [];
    try { const b = await api('bank_status', {}); extra = Object.entries(b.categories || {}).map(([n, c]) => [n, (c.types?.choice?.unused || 0) + (c.types?.text?.unused || 0)]).filter((x) => x[1] >= 25 && !NIGHT_CATS.includes(x[0])).sort((a, b) => a[0].localeCompare(b[0])); } catch { /* the usual list still works */ }
    const st = { cats: ['General knowledge', 'TV & Film', 'Music', 'Sport', 'History', 'Science'], games: ['potato', 'chase'] };
    const m = modal(`<h2 style="margin-top:0">🗡 Make a Traitors night</h2>
      <p class="muted" style="margin-top:0">A whole quiz with the Traitors set up: a secret Traitor, the Round Table vote before half time, a final Round Table, and the Traitor's 20 Questions at the end. The questions come from the bank (no AI), a round for each category you pick. Read it through, then add stunts with <b>🎬 Add "I Literally Just Told You"</b>.</p>
      <div class="field"><label>Title</label><input type="text" id="tn_title" value="${esc('Traitors Night · ' + new Date().toLocaleDateString('en-GB', { day: 'numeric', month: 'short' }))}"></div>
      <div class="field"><label>Question rounds <span class="muted" id="tn_count"></span></label><div id="tn_cats" class="row" style="flex-wrap:wrap;gap:6px"></div>
        <div class="row" style="margin-top:8px"><select id="tn_more" style="max-width:320px"><option value="">+ Any other category from the bank…</option>${extra.map(([n, c]) => `<option value="${esc(n)}">${esc(n)} (${c})</option>`).join('')}</select></div>
        <div class="help">The first half of them come before half time, the rest after. Two to ten rounds.</div></div>
      <div class="row" style="gap:12px;flex-wrap:wrap"><div class="field" style="width:200px"><label>Questions in each round</label><input type="number" id="tn_n" min="4" max="16" value="8"></div>
        <div class="field" style="width:270px"><label>Question style</label><select id="tn_style"><option value="mixed" selected>Mixed: choice, typed, true or false</option><option value="choice">All multiple choice</option><option value="wide">Wider: adds ordering</option></select></div>
        <div class="field" style="width:200px"><label>Half-time break (minutes)</label><input type="number" id="tn_brk" min="1" max="60" value="15"></div></div>
      <div class="field"><label>Party games between the rounds <span class="muted">(each is one round)</span></label><div id="tn_games" class="row" style="flex-wrap:wrap;gap:6px"></div></div>
      <label class="check"><input type="checkbox" id="tn_power" checked> Power cards: everyone gets a hand to play between questions</label>
      <label class="check" style="margin-top:6px"><input type="checkbox" id="tn_bounty" checked> Bounty: take 100 off the leader by getting right what they get wrong</label>
      <div id="tn_msg" class="small error" style="min-height:1.2em;margin-top:8px"></div>
      <div class="row" style="justify-content:flex-end;gap:8px"><button class="btn btn-ghost" data-x>Cancel</button><button class="btn btn-primary btn-lg" id="tn_make">🗡 Make the night</button></div>`);
    $('.modal', m).style.maxWidth = '780px';
    const msg = (t) => { $('#tn_msg', m).textContent = t || ''; };
    const draw = () => {
      const all = [...NIGHT_CATS, ...st.cats.filter((c) => !NIGHT_CATS.includes(c))];
      $('#tn_cats', m).innerHTML = all.map((c) => `<button class="btn btn-sm ${st.cats.includes(c) ? 'btn-primary' : 'btn-ghost'}" data-c="${esc(c)}">${esc(c)}</button>`).join('');
      $$('[data-c]', m).forEach((b) => b.onclick = () => { const c = b.dataset.c; if (st.cats.includes(c)) st.cats = st.cats.filter((x) => x !== c); else if (st.cats.length >= 10) return msg('Ten rounds at the most.'); else st.cats.push(c); msg(''); draw(); });
      $('#tn_count', m).textContent = `· ${st.cats.length} chosen`;
      $('#tn_games', m).innerHTML = GAMES.map(([id, n]) => `<button class="btn btn-sm ${st.games.includes(id) ? 'btn-primary' : 'btn-ghost'}" data-g="${id}">${n}</button>`).join('');
      $$('[data-g]', m).forEach((b) => b.onclick = () => { const g = b.dataset.g; st.games = st.games.includes(g) ? st.games.filter((x) => x !== g) : [...st.games, g]; draw(); });
    };
    $('#tn_more', m).onchange = (e) => { const n = e.target.value; e.target.value = ''; if (n && !st.cats.includes(n)) { if (st.cats.length >= 10) return msg('Ten rounds at the most.'); st.cats.push(n); draw(); } };
    $('[data-x]', m).onclick = () => m.remove();
    draw();
    $('#tn_make', m).onclick = async () => {
      if (st.cats.length < 2) return msg('Pick at least two question rounds.');
      const title = $('#tn_title', m).value.trim() || 'Traitors Night', n = LQ.clamp(Math.round(+$('#tn_n', m).value || 8), 4, 16), mins = LQ.clamp(Math.round(+$('#tn_brk', m).value || 15), 1, 60);
      const style = STYLES[$('#tn_style', m).value] || STYLES.mixed, sum = Object.values(style).reduce((a, b) => a + b, 0);
      const settings = { ...LQ.DEFAULT_SETTINGS, traitors: { on: true }, hostPanel: true };
      if ($('#tn_power', m).checked) settings.power = { on: true, hand: 3 }; if ($('#tn_bounty', m).checked) settings.bounty = true;
      const rounds = [], questions = [];
      const slide = (text, body, extra = {}) => ({ ...LQ.newQuestion('slide', settings), id: uid('q'), text, body, ...extra });
      const addRound = (t, intro, items, extra = {}) => { const id = uid('r'), mix = {}; for (const q of items) { q.round = id; if (q.type !== 'slide') mix[q.type] = (mix[q.type] || 0) + 1; } rounds.push({ id, title: t, intro, brief: '', mix, count: Object.values(mix).reduce((a, b) => a + b, 0), types: Object.keys(mix), practice: false, ...extra }); questions.push(...items); return rounds[rounds.length - 1]; };
      const qRound = (c) => { // a round of questions from the bank, filled in after the quiz is saved
        const mix = {}; let left = n; Object.entries(style).forEach(([t, w], i, arr) => { const k = i === arr.length - 1 ? left : Math.round(n * w / sum); mix[t] = k; left -= k; });
        const id = uid('r'); rounds.push({ id, title: c, intro: '', brief: '', mix, count: n, types: Object.keys(mix).filter((t) => mix[t] > 0), practice: false, source: 'bankonly' });
      };
      const gRound = (g) => { const label = GAMES.find((x) => x[0] === g)[1]; const id = uid('r'); rounds.push({ id, title: label, intro: '', brief: '', mix: { [g]: 1 }, count: 1, types: [g], practice: false, source: 'bankonly' }); };
      const half = Math.ceil(st.cats.length / 2), games = st.games.slice(), g1 = games.splice(0, Math.ceil(games.length / 2));
      addRound('Welcome', '', [slide('Welcome to Traitors Night!', 'Join on your phone at letsquiz.uk/play. Fastest right answers score most. Tonight there is a Traitor hiding among you.'), slide('🗡 Tonight: The Traitors', 'One of you has been chosen in secret to be the Traitor. They can steal points, gift DOUBLE points, block answers and send messages, and nobody knows who they are. Everyone else: watch the scores and work out who it is. Earn a 🛡 shield by getting three right in a row. Tap 📖 Rules on your phone to read it all. There is a Round Table at half time and another at the very end, and you vote.', { theme: 'traitors' })]);
      st.cats.slice(0, half).forEach((c, i) => { qRound(c); if (g1[i]) gRound(g1[i]); });
      g1.slice(half).forEach(gRound);
      addRound('The Round Table', '', [slide('🗡 The Round Table', 'Time to name the Traitor. Three minutes to talk, accuse and defend, then everyone votes on their phone. The player with the most votes goes full screen on camera and tells the room whether they are the Traitor. If they are, they are banished: they lose their power and 5,000 points, and everyone who voted for them wins 2,000. If they are innocent, they lose 3,000 points for being wrongly accused, and so does everyone who voted for them. A Traitor who is not found stays, and may well recruit… There is one more Round Table at the end.', { theme: 'traitors' })]);
      addRound('Half-time', '', [slide('Half-time!', 'Top up your drinks, stretch your legs and check the scores. Back in a few minutes.', { break: true, breakMins: mins })]);
      st.cats.slice(half).forEach((c, i) => { qRound(c); if (games[i]) gRound(games[i]); });
      games.slice(st.cats.length - half).forEach(gRound);
      addRound('The Final Round Table', '', [slide('🗡 The Final Round Table', 'One last vote to catch the Traitors. Three minutes to talk, then everyone votes. The same rules apply: the most votes goes on camera, a Traitor is banished (they lose 5,000, their voters win 2,000), and anyone wrongly accused loses 3,000, with everyone who voted for them. If there were two Traitors at half time, whoever is still standing faces the 20 Questions: find them and win 3,000.', { theme: 'traitors' })]);
      settings.rounds = rounds;
      m.remove();
      S.quiz = normalizeQuiz({ title, settings, rounds, questions }); S.sel = 0; S.planner = false; S.undo = []; S.unconfirmed = false; renderEditor();
      toast('Setting the night up, then filling the rounds from the bank…');
      try { await save(); await writeAllRounds(); } catch (e) { toast(e.message || String(e), true); }
      toast('Your Traitors night is made. Read it through, add stunts with 🎬, then host it and pick the Traitor from the 🗡 Traitors button on the quiz card.');
    };
  }
  return { hostUiHtml, hostUiBind, hostUiRead, cueHtml, cueBind, iljty, traitorsNight, IDEAS };
})();
