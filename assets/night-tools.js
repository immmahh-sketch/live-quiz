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

  // ------------------------------------------------------------------ Christmas Day (assets/xmas.js)
  /** A question's dish (Christmas Day): which item a right answer collects. Only shown when the quiz has Christmas Day on. */
  function xmHtml(q) {
    if (!S.quiz?.settings?.xmas?.on || q.type === 'slide') return '';
    const X = LQ.XMAS;
    return `<div class="field" style="max-width:340px"><label>🎄 Christmas Day: the item a right answer collects</label><select id="xm_dish"><option value="">None: plain question</option>${X.ITEMS.map((i) => `<option value="${i.k}" ${q.xi === i.k ? 'selected' : ''}>${i.icon} ${esc(i.name)} (${esc(i.cat)})</option>`).join('')}</select></div>`;
  }
  function xmBind(root, q, touch) { const el = $('#xm_dish', root); if (el) el.onchange = () => { if (el.value) q.xi = el.value; else delete q.xi; touch(); }; }
  /** The mix of question types for a round of n, in the chosen style. */
  const xmMix = (style, n) => { const sum = Object.values(style).reduce((a, b) => a + b, 0), mix = {}; let left = n; Object.entries(style).forEach(([t, w], i, arr) => { const k = i === arr.length - 1 ? left : Math.round(n * w / sum); mix[t] = Math.max(0, k); left -= k; }); return mix; };
  /** Items in a shuffled order with no item twice running (as far as the numbers allow). */
  function xmInterleave(counts) {
    const bag = []; for (const [k, n] of Object.entries(counts)) for (let i = 0; i < n; i++) bag.push(k);
    const pool = shuffle(bag), out = []; let last = null;
    while (pool.length) { let i = pool.findIndex((k) => k !== last); if (i < 0) i = 0; last = pool.splice(i, 1)[0]; out.push(last); }
    return out;
  }
  async function xmasNight() {
    const X = LQ.XMAS;
    let extra = [];
    try { const b = await api('bank_status', {}); extra = Object.entries(b.categories || {}).map(([n, c]) => [n, (c.types?.choice?.unused || 0) + (c.types?.text?.unused || 0)]).filter((x) => x[1] >= 20).sort((a, b) => a[0].localeCompare(b[0])); } catch { /* the usual list still works */ }
    const catList = [...new Set(['Christmas', ...NIGHT_CATS, ...extra.map((e) => e[0])])];
    const st = { dishes: X.dishes().map((i) => ({ k: i.k, cat: i.cat, n: i.n })), games: ['potato', 'blockbusters', 'race'] };
    const m = modal(`<h2 style="margin-top:0">🎄 Make a Christmas Day night</h2>
      <p class="muted" style="margin-top:0">The whole night is one Christmas Day, from stockings at 7am to midnight. Everyone builds a Christmas dinner: each item is tied to a question category, and a right answer collects it. The rarer the item, the fewer questions it comes up in and the fewer right answers collect it (only the quickest). The tomato ketchup needs a full dish and a 1% question. Every item missing at the end costs 2,000; a full dish pays 5,000. Everyone is dealt a family character with a power; the elf, Uncle Keith, the doorbell and a power cut cause trouble. Questions come from the bank, with no AI.</p>
      <div class="field"><label>Title</label><input type="text" id="xn_title" value="${esc('Christmas Day · ' + new Date().toLocaleDateString('en-GB', { day: 'numeric', month: 'short' }))}"></div>
      <div class="field"><label>The items <span class="muted">(category, and how many questions carry it)</span></label><div id="xn_dishes"></div>
        <div class="help">Fewer questions make an item harder to get: the rare ones also ask harder questions. Around 60 to 80 item questions in all fills an evening.</div></div>
      <div class="row" style="gap:12px;flex-wrap:wrap"><div class="field" style="width:230px"><label>🍅 Ketchup questions (1% Club style)</label><input type="number" id="xn_k" min="1" max="4" value="3"></div>
        <div class="field" style="width:270px"><label>Question style</label><select id="xn_style"><option value="mixed" selected>Mixed: choice, typed, true or false</option><option value="choice">All multiple choice</option><option value="wide">Wider: adds ordering</option></select></div>
        <div class="field" style="width:200px"><label>Half-time break (minutes)</label><input type="number" id="xn_brk" min="1" max="60" value="15"></div></div>
      <div class="field"><label>Party games between the courses <span class="muted">(each is one round)</span></label><div id="xn_games" class="row" style="flex-wrap:wrap;gap:6px"></div></div>
      <label class="check"><input type="checkbox" id="xn_fin" checked> Finish with Double Points Answer Smash, then The Final Chase</label>
      <div id="xn_msg" class="small error" style="min-height:1.2em;margin-top:8px"></div>
      <div class="row" style="justify-content:flex-end;gap:8px"><button class="btn btn-ghost" data-x>Cancel</button><button class="btn btn-primary btn-lg" id="xn_make">🎄 Make the night</button></div>`);
    $('.modal', m).style.maxWidth = '820px';
    const msg = (t) => { $('#xn_msg', m).textContent = t || ''; };
    const draw = () => {
      $('#xn_dishes', m).innerHTML = st.dishes.map((d, i) => { const it = X.item(d.k), R = X.RARITY[it.rar]; return `<div class="row" style="gap:8px;align-items:center;margin-bottom:4px"><span style="min-width:2em;text-align:center;font-size:1.3rem">${it.icon}</span><span style="width:150px"><b>${esc(it.name)}</b><br><span class="muted small">${R.stars} ${R.label}</span></span><select data-dc="${i}" style="max-width:220px">${catList.map((c) => `<option value="${esc(c)}" ${c === d.cat ? 'selected' : ''}>${esc(c)}</option>`).join('')}</select><input type="number" data-dn="${i}" min="2" max="12" value="${d.n}" style="width:70px"><span class="muted small">questions</span></div>`; }).join('');
      $$('[data-dc]', m).forEach((el) => el.onchange = () => { st.dishes[+el.dataset.dc].cat = el.value; });
      $$('[data-dn]', m).forEach((el) => el.oninput = () => { st.dishes[+el.dataset.dn].n = LQ.clamp(Math.round(+el.value || 2), 2, 12); });
      $('#xn_games', m).innerHTML = GAMES.map(([id, n]) => `<button class="btn btn-sm ${st.games.includes(id) ? 'btn-primary' : 'btn-ghost'}" data-g="${id}">${n}</button>`).join('');
      $$('[data-g]', m).forEach((b) => b.onclick = () => { const g = b.dataset.g; st.games = st.games.includes(g) ? st.games.filter((x) => x !== g) : [...st.games, g]; draw(); });
    };
    $('[data-x]', m).onclick = () => m.remove();
    draw();
    $('#xn_make', m).onclick = async () => {
      const title = $('#xn_title', m).value.trim() || 'Christmas Day', mins = LQ.clamp(Math.round(+$('#xn_brk', m).value || 15), 1, 60), nk = LQ.clamp(Math.round(+$('#xn_k', m).value || 3), 1, Math.min(4, X.KETCHUP_QS.length));
      const style = STYLES[$('#xn_style', m).value] || STYLES.mixed, fin = $('#xn_fin', m).checked;
      if (st.dishes.reduce((a, d) => a + d.n, 0) < 20) return msg('That is too few item questions: aim for at least 40.');
      const settings = { ...LQ.DEFAULT_SETTINGS, xmas: { on: true }, hostPanel: true };
      const rounds = [], questions = [];
      const slide = (text, body, extra = {}) => ({ ...LQ.newQuestion('slide', settings), id: uid('q'), text, body, ...extra });
      const mkRound = (t, intro, extra = {}) => ({ id: uid('r'), title: t, intro: intro || '', brief: '', mix: {}, count: 0, types: [], practice: false, ...extra });
      const welcome = mkRound('Welcome', ''); rounds.push(welcome);
      const fam = X.CHARS.map((c) => `${c.icon} ${c.name}: ${c.power}`).join('\n');
      questions.push(
        slide('Welcome to Christmas Day!', 'Join on your phone at letsquiz.uk/play. Tonight is one long Christmas Day, from stockings at 7am to midnight, and everybody is building a Christmas dinner.', { round: welcome.id }),
        slide('🎄 Build your Christmas dinner', `Every question belongs to a category, and every category is a dish: ${X.dishes().map((i) => `${i.icon} ${i.name}`).join(', ')}. Get a question right and the item goes on your dish. The rarer items turn up less often, and only the quickest right answers collect them.\n\nThe last item is 🍅 tomato ketchup. You need a full dish first, and then you must beat a 1% question.\n\nBeware: the quickest finger every few questions can PINCH an item off someone else's dish, the elf swaps dishes, and Uncle Keith helps himself.\n\nAt the end, every item missing costs you 2,000 points. A full dish pays 5,000.`, { round: welcome.id }),
        slide('👨‍👩‍👧 Meet the family', `Everyone has been dealt a family member, with a quirk that always works and one power to play between questions. Tap 🍽 on your phone to see yours.\n\n${fam}`, { round: welcome.id }));
      // phase one: a round for each item's category (filled from the bank), then the games, then the Smash and the Chase
      const dishRounds = st.dishes.map((d) => { const it = X.item(d.k), r = mkRound(d.cat, '', { source: 'bankonly', difficulty: X.RARITY[it.rar].diff, mix: xmMix(style, d.n), count: d.n, _xm: d.k }); r.types = Object.keys(r.mix).filter((t) => r.mix[t] > 0); rounds.push(r); return r; });
      const gameRounds = st.games.map((g) => { const label = GAMES.find((x) => x[0] === g)[1]; const r = mkRound(label, '', { mix: { [g]: 1 }, count: 1, types: [g], source: 'bankonly' }); rounds.push(r); return r; });
      let smashR = null, chaseR = null;
      if (fin) { smashR = mkRound('Double Points: Answer Smash', '', { mix: { smash: 5 }, count: 5, types: ['smash'], source: 'bankonly', double: true }); chaseR = mkRound('The Final Chase', '', { mix: { chase: 1 }, count: 1, types: ['chase'], source: 'bankonly' }); rounds.push(smashR, chaseR); }
      settings.rounds = rounds;
      m.remove();
      S.quiz = normalizeQuiz({ title, settings, rounds, questions }); S.sel = 0; S.planner = false; S.undo = []; S.unconfirmed = false; renderEditor();
      toast('Setting the night up, then filling the rounds from the bank…');
      try { await save(); await writeAllRounds(); } catch (e) { toast(e.message || String(e), true); return; }
      // phase two: dissolve the item rounds into courses with the items mixed up, and lay the night out
      const ids = (rs) => rs.filter(Boolean).map((r) => r.id), dm = Object.fromEntries(dishRounds.map((r) => [r.id, r._xm]));
      try { xmLayout({ dishIds: dm, gameIds: ids(gameRounds), smashId: smashR?.id, chaseId: chaseR?.id, welcomeId: welcome.id, nk, mins }); } catch (e) { toast('The night was filled but could not be laid out: ' + (e.message || e), true); return; }
      try { await save(); } catch { /* the editor keeps trying */ }
      toast('Your Christmas Day night is made. Read it through, then host it. Each item question is tagged: check or change one in the editor under 🎄.');
    };
  }
  /** After the bank has filled the rounds: tag each question with its item, mix them into four courses, and place the games, ketchup questions and break. */
  function xmLayout({ dishIds, gameIds, smashId, chaseId, welcomeId, nk, mins }) {
    const X = LQ.XMAS, qz = S.quiz, settings = qz.settings, byRound = (id) => qz.questions.filter((q) => q.round === id), roundOf_ = (id) => qz.rounds.find((r) => r.id === id);
    const slide = (text, body, extra = {}) => ({ ...LQ.newQuestion('slide', settings), id: uid('q'), text, body, ...extra });
    const mk = (t, intro, items, extra = {}) => { const r = { id: uid('r'), title: t, intro: intro || '', brief: '', mix: {}, count: 0, types: [], practice: false, ...extra }; for (const q of items) { q.round = r.id; if (q.type !== 'slide') r.mix[q.type] = (r.mix[q.type] || 0) + 1; } r.count = Object.values(r.mix).reduce((a, b) => a + b, 0); r.types = Object.keys(r.mix); return { r, items }; };
    const taken = {}, counts = {};
    for (const [rid, k] of Object.entries(dishIds)) { const list = byRound(rid); for (const q of list) q.xi = k; taken[k] = list; counts[k] = list.length; }
    const order = xmInterleave(counts), seq = order.map((k) => taken[k].shift()).filter(Boolean);
    if (seq.length < 20) throw new Error('the bank gave only ' + seq.length + ' questions for the items');
    // four courses, the first and last a little shorter
    const names = [['🧦 Stockings and presents', 'Morning has broken. Time to start collecting.'], ['🍳 Cooking the dinner', 'The kitchen is a war zone.'], ['🍽 The big dinner', 'Everybody to the table!'], ['📺 Telly and the board games', 'The King has spoken. Now the arguing begins.']];
    const w = [0.22, 0.28, 0.28, 0.22], courses = []; let from = 0;
    names.forEach(([t, intro], i) => { const n = i === 3 ? seq.length - from : Math.round(seq.length * w[i]); courses.push(mk(t, intro, seq.slice(from, from + n))); from += n; });
    // the ketchup questions
    const kq = shuffle(X.KETCHUP_QS).slice(0, nk).sort((a, b) => b.pct - a.pct).map((kd, i) => { const q = { ...LQ.newQuestion('club', settings), id: uid('q'), text: kd.text, answers: kd.answers.slice(), pct: kd.pct, why: kd.why, handMade: true, category: 'The 1% question', difficulty: 'hard', media: { kind: 'none' }, partial: false, xi: 'ketchup', time: 60 }; return mk(`🍅 The Ketchup Question${nk > 1 ? ' ' + (i + 1) : ''}`, 'You need a full dish of nine items. Beat the 1% question and the ketchup is yours.', [q]); });
    const games = gameIds.map((id) => ({ r: roundOf_(id), items: byRound(id) })).filter((g) => g.r);
    const out = [{ r: roundOf_(welcomeId), items: byRound(welcomeId) }];
    const gapAfter = { 1: [], 2: [], 3: [], 4: [] }; [1, 3, 4, 2].forEach((c, i) => { if (games[i]) gapAfter[c].push(games[i]); }); games.slice(4).forEach((g) => gapAfter[2].push(g));
    const kSlots = nk >= 3 ? [2, 3, 4] : nk === 2 ? [2, 4] : [4];
    courses.forEach((c, i) => {
      out.push(c); (gapAfter[i + 1] || []).forEach((g) => out.push(g));
      const ki = kSlots.indexOf(i + 1); if (ki >= 0 && kq[ki]) out.push(kq[ki]);
      if (i === 1) out.push(mk('Half-time', '', [slide('Half-time!', 'Top up your drinks, stretch your legs and check your dish. The dinner is only half cooked.', { break: true, breakMins: mins })]));
    });
    if (smashId && roundOf_(smashId)) out.push({ r: roundOf_(smashId), items: byRound(smashId) });
    if (chaseId && roundOf_(chaseId)) out.push({ r: roundOf_(chaseId), items: byRound(chaseId) });
    qz.rounds = out.map((x) => x.r); qz.questions = out.flatMap((x) => x.items);
    for (const r of qz.rounds) delete r._xm;
    touch(); S.sel = 0; renderEditor();
  }
  return { hostUiHtml, hostUiBind, hostUiRead, cueHtml, cueBind, iljty, traitorsNight, xmasNight, xmHtml, xmBind, IDEAS };
})();
