// BHB Training: "Disciplinary & Grievance for Managers", a two-hour session, built as a quiz with the BHB Training brand.
// Slides carry the teaching (assets/train-visuals.js draws the diagrams); questions go to the phones; "why" lines teach
// under each right answer. Run:  LQ_PASSWORD=… node tools/train-deck.mjs [--dry]
//   --dry  builds and checks it, prints the running order, saves nothing.
//   --json FILE  also writes the quiz to FILE (the headless test harness plays from it).
// The saved quiz id is kept in tools/train-deck.id so a re-run updates the same quiz instead of making another.
import fs from 'node:fs'; import path from 'node:path'; import url from 'node:url';
import { LQ, api, uid } from './lq.mjs';

const HERE = path.dirname(url.fileURLToPath(import.meta.url)), ROOT = path.join(HERE, '..');
const DRY = process.argv.includes('--dry');

// ------------------------------------------------------------------ helpers
let seed = 20261006;
const rnd = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
const shuf = (a) => { const x = a.slice(); for (let i = x.length - 1; i > 0; i--) { const j = Math.floor(rnd() * (i + 1)); [x[i], x[j]] = [x[j], x[i]]; } return x; };

// photographs (assets/train/<key>.jpg, credits in credits.json); a missing one is simply left out
const CREDITS = fs.existsSync(path.join(ROOT, 'assets/train/credits.json')) ? JSON.parse(fs.readFileSync(path.join(ROOT, 'assets/train/credits.json'), 'utf8')) : {};
const img = (k) => {
  if (!fs.existsSync(path.join(ROOT, `assets/train/${k}.jpg`))) return null;
  const c = CREDITS[k] || {}, lic = String(c.license || '').trim();
  const nice = /^cc/i.test(lic) ? lic : /^(by|sa)/i.test(lic) ? 'CC ' + lic.toUpperCase() : lic;
  const credit = !c.creator || /^(cc0|cc 0|pdm|public)/i.test(lic) ? '' : `Photo: ${c.creator} · ${nice}`;
  return { kind: 'image', url: `assets/train/${k}.jpg`, ...(credit ? { credit } : {}) };
};

const R = {}; // rounds, filled in order
const rounds = [];
const round = (key, title, intro) => { R[key] = 'r_' + key; rounds.push({ id: R[key], title, intro, practice: false }); };
const qs = [];
const add = (q) => { qs.push(q); return q; };

const slide = (r, o) => add({ id: uid('q'), type: 'slide', round: R[r], text: o.title || '', body: o.body || '', time: o.time || 20, media: o.img ? (img(o.img) || { kind: 'none' }) : { kind: 'none' },
  ...(o.layout ? { layout: o.layout } : {}), ...(o.kicker ? { kicker: o.kicker } : {}), ...(o.visual ? { visual: o.visual } : {}),
  ...(o.mins ? { break: true, breakMins: o.mins } : {}), ...(o.exercise ? { exercise: true } : {}) });
const base = (r, type, text, time, why) => ({ id: uid('q'), type, round: R[r], text, time, media: { kind: 'none' }, partial: false, edited: true, ...(why ? { why } : {}) });
const choice = (r, text, right, wrong, why, time = 30) => {
  const opts = shuf([{ t: right, ok: true }, ...wrong.map((t) => ({ t }))]).map((x) => ({ id: uid('o'), text: x.t, ok: !!x.ok }));
  const q = base(r, 'choice', text, time, why);
  q.options = opts.map(({ id, text }) => ({ id, text })); q.correct = opts.find((x) => x.ok).id;
  return add(q);
};
const tf = (r, text, answer, why, time = 20) => add({ ...base(r, 'tf', text, time, why), answer });
const order = (r, text, items, hint, why, time = 50) => add({ ...base(r, 'order', text, time, why), items: items.map((t) => ({ id: uid('i'), text: t })), hint, partial: true });
const sort = (r, text, cats, items, why, time = 60) => {
  const cs = cats.map((name) => ({ id: uid('c'), name }));
  return add({ ...base(r, 'sort', text, time, why), categories: cs, items: shuf(items).map(([t, c]) => ({ id: uid('i'), text: t, category: cs[c].id })), partial: true });
};
const match = (r, text, pairs, why, time = 55) => add({ ...base(r, 'match', text, time, why), pairs: pairs.map(([l, v]) => ({ id: uid('p'), left: l, right: { kind: 'text', value: v } })), partial: true });
const typed = (r, text, answers, why, time = 30) => add({ ...base(r, 'text', text, time, why), answers, ai: true });
const nearest = (r, text, answer, unit, spread, why, time = 25) => add({ ...base(r, 'nearest', text, time, why), answer: String(answer), unit, spread });
const survey = (r, text, time = 40) => add({ ...base(r, 'text', text, time), kind: 'survey', answers: [''], ai: false });

// ------------------------------------------------------------------ the sections
// Every section runs the same way: a title slide with what you will be able to do, the teaching slides, a discussion or
// group exercise with a clock, a debrief with model answers, three key takeaways, and then a knowledge check of three
// questions on the phones. The scoreboard shows after each knowledge check.
round('open', 'Welcome', 'Why we are here and how the session will run.');
round('prevent', 'Prevention is better than cure', 'Small things, said early, in private, are the cheapest fix there is.');
round('cantwont', "Can't or won't?", 'Conduct and competency: name which, then act on it.');
round('informal', 'Informal first', 'The rule of three and the Coaching & Advice record.');
round('invest', 'Facts first', 'Investigations, evidence, statements and when to ring Ward Hadaway.');
round('hearing', 'Hearings and warnings', 'The chair, the note-taker and the companion, and the ladder up to dismissal.');
round('grievance', 'Grievances', 'The lowest level that works: talk, mediate, then formal.');
round('wrap', 'Wrap-up', 'What you will do on Monday.');

const kc = (r, n = 3) => slide(r, { layout: 'plain', kicker: 'Knowledge check', title: `${n} questions on what we have just covered`, body: 'Phones out. No scores: these are here to keep us thinking, and to show what has stuck.', time: 8 });
const takeaways = (r, items) => slide(r, { layout: 'visual', kicker: 'Key takeaways', title: 'Remember these three', visual: { type: 'cards', cols: 3, items: items.map(([t, x], i) => ({ n: i + 1, title: t, text: x, tone: ['sage', 'slate', 'gold'][i] })), numbered: true } });
const cards3 = (...a) => a;

// ================================================================ OPENING (8 min)
slide('open', { layout: 'hero', img: 'welcome', kicker: 'BHB Training · Managers', title: 'Disciplinary & Grievance', body: 'Getting it right, getting it fair, and getting it early.' });
slide('open', { layout: 'visual', kicker: 'Why we are here', title: 'How we handle people problems defines us', visual: { type: 'cards', cols: 4, items: [
  { icon: '⚖️', title: 'Fairness', text: 'The same issue, handled the same way, whoever it is.', tone: 'sage' },
  { icon: '🛡️', title: 'Protection', text: 'A fair process protects the business, the team and you. Ignoring the Acas Code can add up to 25% to a tribunal award.', tone: 'slate' },
  { icon: '👥', title: 'The team is watching', text: 'Your best people judge us on how we deal with the worst.', tone: 'gold' },
  { icon: '🍽️', title: 'Standards', text: 'Guests feel it when a team is unhappy, or when a problem is left to fester.', tone: 'clay' }] } });
slide('open', { layout: 'visual', kicker: 'Outcomes', title: 'By the end of this session you will be able to', visual: { type: 'steps', cols: 3, numbered: true, items: [
  { title: 'Prevent', text: 'Use 121s to catch small problems early.', tone: 'sage' },
  { title: 'Diagnose', text: "Tell conduct from competency, and respond to each.", tone: 'slate' },
  { title: 'Document', text: 'Hold the three-step informal process and complete a Coaching & Advice record.', tone: 'gold' },
  { title: 'Investigate', text: 'Gather facts, evidence and statements, and know when to call HR.', tone: 'clay' },
  { title: 'Run a hearing', text: 'Chair, take notes and handle companions fairly.', tone: 'sage' },
  { title: 'Handle grievances', text: 'Resolve them at the lowest level that works.', tone: 'slate' }] } });
slide('open', { layout: 'visual', kicker: 'Running order', title: 'Today', visual: { type: 'agenda', items: [
  { at: '0:00', title: 'Welcome', mins: 8 },
  { at: '0:08', title: 'Prevention is better than cure', mins: 11 },
  { at: '0:19', title: "Can't or won't?", mins: 14 },
  { at: '0:33', title: 'Informal first', text: 'incl. role play', mins: 20 },
  { at: '0:53', title: 'Break', mins: 10 },
  { at: '1:03', title: 'Facts first', text: 'incl. group case', mins: 14 },
  { at: '1:17', title: 'Hearings and warnings', mins: 20 },
  { at: '1:37', title: 'Grievances', text: 'incl. role play', mins: 16 },
  { at: '1:53', title: 'Wrap-up', mins: 7 }] },
  body: 'Each section: learn it, discuss it, then a quick three-question check on your phone. Nothing is scored.' });
slide('open', { layout: 'plain', kicker: 'House rules', title: 'How we will work today', body: `- Slides on the big screen, quick quizzes on your phone, and plenty of discussion
- Every scenario is made up. Keep real names and real cases out of the room
- Nothing personal said here goes outside it
- Challenge, question and disagree. It is how we get it right
- Nothing is scored. The questions are there to keep us thinking
- This is our way of working, not legal advice: **if in doubt, ring Ward Hadaway before you act, not after**` });
slide('open', { layout: 'exercise', exercise: true, mins: 3, kicker: 'Discussion · pairs', title: 'Warm-up',
  body: `Think of a time **a problem at work was handled really well, or really badly**. It does not have to be here.

With the person next to you:
- What happened?
- What did the manager do, or not do?
- How did it feel for everyone watching?` });
survey('open', 'In a word or two: what makes the difference between a problem handled well and one handled badly?', 40);

// ================================================================ 1 PREVENTION (11 min)
slide('prevent', { layout: 'hero', img: 'stitch', kicker: 'Part 2', title: 'Prevention is better than cure', body: `By the end of this section you can:
- Explain why early, informal action wins
- Run a simple, regular 121
- Spot the early warning signs` });
slide('prevent', { layout: 'visual', kicker: 'The cost of waiting', title: 'The later you leave it, the more it costs', visual: { type: 'bars', items: [
  { label: 'A quiet word', v: 6, note: 'Five minutes', tone: 'sage' },
  { label: 'Coaching & Advice', v: 18, note: 'Half an hour and a form', tone: 'slate' },
  { label: 'First written warning', v: 42, note: 'Investigation, hearing, letter', tone: 'gold' },
  { label: 'Final written warning', v: 62, note: 'All of that again, with more at stake', tone: 'clay' },
  { label: 'Dismissal and appeal', v: 82, note: 'Weeks of manager time', tone: 'ink' },
  { label: 'Tribunal claim', v: 100, note: 'Months, stress and money', tone: 'clay' }], caption: 'Illustrative: the size of the effort, not a measurement.' },
  body: '> Most problems are small, once. Our job is to catch them there.' });
slide('prevent', { layout: 'visual', kicker: 'The best tool you have', title: '121s: where small things get said while they are small', visual: { type: 'cards', cols: 3, items: [
  { icon: '📅', title: 'Regular', text: 'Same slot every month or fortnight. Not only when something is wrong.', tone: 'sage' },
  { icon: '🚪', title: 'Private', text: 'Door shut, phone away, never mid-service. Somewhere they can be honest.', tone: 'slate' },
  { icon: '👂', title: 'Two-way', text: 'They talk more than you do. You ask, listen, then agree what happens next.', tone: 'gold' }] },
  body: 'A 121 that only happens when there is a problem feels like a telling-off. One that is always cancelled tells them they do not matter.' });
slide('prevent', { layout: 'visual', kicker: 'A simple shape', title: 'Five questions for every 121', visual: { type: 'steps', cols: 5, items: [
  { title: 'How are you?', text: 'Really. Start with the person.' },
  { title: "What's going well?", text: 'Name something specific.', tone: 'slate' },
  { title: "What's getting in the way?", text: 'Tools, training, people, rota.', tone: 'gold' },
  { title: 'What do you need from me?', text: 'And what do I need from you?', tone: 'clay' },
  { title: 'Agree actions', text: 'Who, what, by when. Book the next one.', tone: 'sage' }] } });
slide('prevent', { layout: 'visual', kicker: 'Early warning signs', title: 'Spot it before it is a problem', visual: { type: 'cards', cols: 3, items: [
  { icon: '⏰', title: 'Time-keeping slips', text: 'A few minutes here and there, then more.', tone: 'gold' },
  { icon: '🤐', title: 'Quieter than usual', text: 'Less banter, less eye contact, withdrawn.', tone: 'slate' },
  { icon: '⚠️', title: 'More mistakes', text: 'Orders wrong, checks missed, things forgotten.', tone: 'clay' },
  { icon: '📉', title: 'Standards drop', text: 'Uniform, presentation, pace, attitude to guests.', tone: 'gold' },
  { icon: '⚡', title: 'Friction', text: 'Snapping at colleagues, cliques, short tempers.', tone: 'clay' },
  { icon: '🙈', title: 'Avoiding you', text: 'Swapping shifts, hiding in the back, off sick on busy days.', tone: 'slate' }] },
  body: '> Always ask before you judge. It may be health, family or stress.' });
slide('prevent', { layout: 'exercise', exercise: true, mins: 3, kicker: 'Discussion · pairs', title: 'What gets in the way of 121s?',
  body: `Be honest. In pairs:
- What stops us holding regular 121s in this business?
- What is the **one** change that would make them happen?

Be ready to share one answer with the room.` });
takeaways('prevent', [['Early beats late', 'A private word now costs minutes. The same issue left costs weeks.'], ['Make 121s a habit', 'Regular, private, two-way, and written down.'], ['Ask before you judge', 'Find out why. It is often not what you think.']]);
kc('prevent');
choice('prevent', 'A reliable team member is ten minutes late for the second time this month. What is your best first move?',
  'A private word today: ask what has changed, and note it down',
  ['Say nothing and see if it happens again', 'Send a written warning', 'Mention it in the team WhatsApp so everyone gets the message'],
  'Early, private and curious. Find out why before you decide what it is. A reason you did not know about changes the whole conversation.');
sort('prevent', 'A good 121 habit, or a bad one?', ['Good habit', 'Bad habit'], [
  ['Same time every fortnight', 0], ['Asking "what do you need from me?"', 0], ['Writing down what was agreed', 0], ['Letting them talk first', 0],
  ['Cancelling when it gets busy', 1], ['Only holding one when there is a problem', 1], ['Doing it on the pass in the middle of service', 1], ['Telling more than asking', 1]],
  'The best 121s have nothing wrong to fix. That is what makes it safe to raise things early.');
tf('prevent', 'If you let a problem slide for months, you can still go straight to a written warning when you finally lose patience.', false,
  'If you have never told them, a written warning will look unfair. The standard has to be said out loud, early, before it can be enforced.');

// ================================================================ 2 CAN'T OR WON'T (14 min)
slide('cantwont', { layout: 'hero', img: 'crossroads', kicker: 'Part 3', title: "Can't or won't?", body: `By the end of this section you can:
- Tell conduct from competency
- Respond to each in the right way
- Spot when it is neither` });
slide('cantwont', { layout: 'visual', kicker: 'Two roots', title: 'When someone underperforms, it is usually one of two things', visual: { type: 'two',
  left: { title: "Conduct: they won't", tone: 'clay', icon: '🔥', items: ['Cannot be bothered', 'Does not want to be here', 'Does not care about the standard', 'Knows what good looks like and ignores it'] },
  right: { title: "Competency: they can't", tone: 'slate', icon: '🛠️', items: ['Has not been trained', 'Does not have the tools or the time', 'Was never told what good looks like', 'Is not (yet) capable of the standard we need'] } },
  body: 'Competency is about **ability**. Conduct is about **choice**. They need very different responses.' });
slide('cantwont', { layout: 'visual', kicker: 'Skill and will', title: 'Where does this person sit?', visual: { type: 'matrix', yAxis: 'Skill: can they do it?', xAxis: 'Will: do they want to?', cells: {
  tl: { title: 'Conduct', text: 'They can, but they will not. Challenge it clearly.', tone: 'clay' },
  tr: { title: 'Keep and grow', text: 'They can and they will. Look after them.', tone: 'sage' },
  bl: { title: 'Get good or get gone', text: 'They cannot and will not. Be clear, be quick, be fair.', tone: 'ink' },
  br: { title: 'Competency', text: 'They will, but they cannot yet. Train, equip, direct.', tone: 'slate' } } } });
slide('cantwont', { layout: 'visual', kicker: 'Competency', title: 'We owe them four things first', visual: { type: 'cards', cols: 4, items: [
  { icon: '🎯', title: 'Clear expectations', text: 'What good looks like, in words and by example.', tone: 'sage' },
  { icon: '🎓', title: 'Training', text: 'Shown, practised, and checked. Not "watch Sam".', tone: 'slate' },
  { icon: '🧰', title: 'The tools and time', text: 'Kit, access, systems, a rota that allows it.', tone: 'gold' },
  { icon: '🧭', title: 'Direction', text: 'Regular feedback, a review date, a visible finish line.', tone: 'clay' }] },
  body: 'Only when all four are in place can we honestly say they cannot do it. Until then it is on us.' });
slide('cantwont', { layout: 'plain', kicker: 'Conduct', title: 'Name it, then challenge it', body: `## How
- Be specific about the behaviour, with an example
- Explain the impact on guests, colleagues or the business
- Ask for their view, and listen
- Agree what changes, and by when
- Follow it up

> A conduct issue is a choice, so the consequences are fair. Do not soften it into a competency problem to avoid the conversation.` });
slide('cantwont', { layout: 'visual', kicker: 'A third cause', title: 'Sometimes it is neither', visual: { type: 'cards', cols: 3, items: [
  { icon: '🩺', title: 'Health', text: 'Physical or mental. Long-term conditions may be a disability.', tone: 'slate' },
  { icon: '🏠', title: 'Home life', text: 'Caring, bereavement, money, a relationship breaking down.', tone: 'gold' },
  { icon: '😮‍💨', title: 'Stress and workload', text: 'Too many hours, too little support, burnout.', tone: 'clay' }] },
  body: '> Ask first, judge later. If it could be health or disability, ring HR before you do anything formal.' });
slide('cantwont', { layout: 'photoright', img: 'exit', kicker: 'Our philosophy', title: 'Get them good, or get them gone', body: `We do not leave people struggling. We give them the **training**, the **tools** and the **direction** to be good.

We do not carry people who will not. We **cannot afford dead wood**, and our good people notice when we do.

> Either way, we act in good time and we act fairly.` });
slide('cantwont', { layout: 'exercise', exercise: true, mins: 5, kicker: 'Group work · tables of four', title: 'Three people, one question',
  body: `For each person: **conduct, competency, or neither?** What would you ask, and what is your first step?`,
  visual: { type: 'cards', cols: 3, items: [
    { icon: 'A', title: 'Kai', text: 'Four months in. Cannot carry three plates and keeps getting table numbers wrong. Has never had a proper floor induction.', tone: 'slate' },
    { icon: 'B', title: 'Mo', text: 'Six years in and once brilliant. Now ignores the dress code and says "you cannot sack me".', tone: 'clay' },
    { icon: 'C', title: 'Priya', text: 'Reliable for three years. Now late twice a week and quiet. Yesterday you found her crying in the stock room.', tone: 'gold' }] } });
slide('cantwont', { layout: 'visual', kicker: 'Debrief', title: 'What good looks like', visual: { type: 'cards', cols: 3, items: [
  { icon: 'A', title: 'Kai: competency, and it is on us', text: 'Check training, shadowing, tools and standards first. Then a structured plan with a review date.', tone: 'slate' },
  { icon: 'B', title: 'Mo: conduct', text: 'A direct, specific conversation. Skill is not the issue; choice is. Quiet word, then on paper if it continues.', tone: 'clay' },
  { icon: 'C', title: 'Priya: neither, yet', text: 'A private, caring chat. Ask what has changed and what would help. Take HR advice if it is health related.', tone: 'gold' }] } });
takeaways('cantwont', [["Ask: can't or won't?", 'Ability and choice need different responses.'], ['Competency is on us first', 'Expectations, training, tools and direction before judgement.'], ['Get them good or get them gone', 'Help the willing. Act fairly and in good time on the rest.']]);
kc('cantwont');
sort('cantwont', 'Conduct or competency?', ["Conduct: won't", "Competency: can't"], [
  ['Has never been shown how to use the new booking system', 1], ['Says "I don\'t care" when asked to restock the bar', 0],
  ['Was thrown on the pass in week one with no training', 1], ['Takes 20-minute breaks every shift, knowing the limit is 15', 0],
  ['Keeps ignoring the allergen process they were trained on last month', 0], ['Is willing but slow, and has never been given a standard to hit', 1],
  ['Rolls their eyes and walks off when given feedback', 0], ['Has no access to the till training account', 1]],
  'If we have not trained them, equipped them and told them the standard, it is on us first. Once we have, a choice not to meet it is conduct.');
choice('cantwont', 'In week three a new waiter keeps mixing up table numbers and orders. What do you check first?',
  'Whether they have been trained, shadowed and given the system and tools',
  ['Whether they are really cut out for hospitality', 'Whether they have been warned about it yet', 'Whether the other waiters are covering for them'],
  'Competency starts with us: training, tools, clarity. Until those are in place you cannot say they cannot do it.');
typed('cantwont', 'Finish our motto: get them good, or get them…', ['gone', 'get them gone'], 'Fair, early and clear. We invest in people who want to improve, and we act when they will not.', 20);

// ================================================================ 3 INFORMAL FIRST (20 min)
slide('informal', { layout: 'hero', img: 'one2one', kicker: 'Part 4', title: 'Informal first', body: `By the end of this section you can:
- Use the rule of three
- Complete a Coaching & Advice record
- Write SMART actions` });
slide('informal', { layout: 'visual', kicker: 'The rule of three', title: 'Once, twice, then on paper', visual: { type: 'steps', cols: 3, items: [
  { icon: '💬', title: 'First time', text: 'Have a quiet word. Find out why. Make a note in your 121 notes.', tone: 'sage' },
  { icon: '🔁', title: 'Second time', text: '"We have already discussed this." Be clear it is a repeat. Note it again.', tone: 'slate' },
  { icon: '📝', title: 'Third time', text: 'Coaching & Advice record: on paper, with actions and expectations.', tone: 'gold' }] },
  body: '> Still no change after that? It moves into the formal disciplinary route.' });
slide('informal', { layout: 'visual', kicker: 'The ladder', title: 'You can step in at the level the issue deserves', visual: { type: 'ladder', items: [
  { title: 'A quiet word', text: 'First time. Informal', tone: 'sage', band: 'Informal' },
  { title: '"We have already discussed this"', text: 'Second time. Informal', tone: 'sage', band: 'Informal' },
  { title: 'Coaching & Advice record', text: 'Third time. On paper, not disciplinary', tone: 'slate', band: 'Documented' },
  { title: 'First written warning', tone: 'gold', band: 'Formal' },
  { title: 'Final written warning', tone: 'clay', band: 'Formal' },
  { title: 'Dismissal', tone: 'ink', band: 'Formal' }],
  side: { title: 'Any step, any time', text: 'The ladder is not a queue. Serious misconduct can start at the written-warning steps. **Gross misconduct** can go straight to a dismissal hearing. The seriousness decides, and it is always investigated first.', tone: 'clay' } } });
slide('informal', { layout: 'visual', kicker: 'Our form', title: 'The Coaching & Advice record', visual: { type: 'form', title: 'COACHING & ADVICE RECORD', top: [{ k: 'Team Member Name' }, { k: 'Date' }], fields: [
  { n: 1, label: 'What has been discussed?', tip: 'Facts: what happened, when, how often, and the impact.', hi: true },
  { n: 2, label: 'Colleague response / explanation', tip: 'Their words, not yours.' },
  { n: 3, label: 'Action Plan', hint: 'Agree SMART actions and a suitable review date where appropriate. Identify what implications there could be if the actions are not met.', tip: 'Specific actions, a date to review, and what happens if nothing changes.' }], sign: true },
  body: 'It is a documented informal conversation, **not** a disciplinary warning. It shows the issue was raised, what support was offered and what was agreed.' });
slide('informal', { layout: 'plain', kicker: 'Filling it in', title: 'Five rules for the record', body: `✔ **Facts**: dates, times, examples and the impact
✔ Their response, **in their words**
✔ **SMART** actions and a review date
✔ What happens if the actions are not met
✔ Both of you sign, and they get a copy
✘ Opinions about their character
✘ "Bad attitude" with no examples
✘ Writing it up days later from memory

> Write it the same day, while it is fresh and accurate.` });
slide('informal', { layout: 'visual', kicker: 'A good one', title: 'Example: a record that does its job', visual: { type: 'form', title: 'COACHING & ADVICE RECORD', top: [{ k: 'Team Member Name', v: 'Charlie (bar)' }, { k: 'Date', v: '12 October' }], fields: [
  { n: 1, label: 'What has been discussed?', text: 'Phone use behind the bar during service on 3 Oct, 14 Oct and 19 Oct. Two guests waited over five minutes on the 19th while the phone was in use.' },
  { n: 2, label: 'Colleague response / explanation', text: 'Said they were checking a message from childcare and did not realise guests were waiting. Agreed it should not happen during service.' },
  { n: 3, label: 'Action Plan', text: 'Phone stays in the staff room during shifts; family can ring the main line. Review in four weeks (9 Nov). If it continues, this may move to the formal disciplinary procedure.' }], sign: true } });
slide('informal', { layout: 'visual', kicker: 'The actions', title: 'Make the actions SMART', visual: { type: 'cards', cols: 5, items: [
  { icon: 'S', title: 'Specific', text: 'Exactly what, in plain words.', tone: 'sage' },
  { icon: 'M', title: 'Measurable', text: 'How will we both know?', tone: 'slate' },
  { icon: 'A', title: 'Achievable', text: 'Within their power and training.', tone: 'gold' },
  { icon: 'R', title: 'Relevant', text: 'Linked to the issue we discussed.', tone: 'clay' },
  { icon: 'T', title: 'Time-bound', text: 'By when? When do we review?', tone: 'ink' }] },
  body: '✘ "Try harder to be on time"   ✔ "Be at your station in full uniform at the start of every shift, reviewed on 9 November"' });
slide('informal', { layout: 'exercise', exercise: true, mins: 9, kicker: 'Role play 1 · groups of three', title: 'Hold the conversation',
  body: `**Charlie**, a bar team member, has been on their phone behind the bar three times this month. You had a quiet word on the 3rd and a reminder on the 14th. It happened again last night while two guests waited.

Hold the conversation (about five minutes), then agree **two SMART actions** and what happens if they are not met.`,
  visual: { type: 'cards', cols: 3, items: [
    { icon: '🧑‍💼', title: 'Manager', text: 'Open kindly. Facts first, then listen. End with two SMART actions and a review date.', tone: 'sage' },
    { icon: '🍸', title: 'Charlie', text: 'Embarrassed and a bit defensive: "everyone does it". Soften if you are listened to.', tone: 'gold' },
    { icon: '👀', title: 'Observer', text: 'Note: facts or opinions? Who talked most? Were the actions SMART? Review date? Consequence said?', tone: 'slate' }] } });
slide('informal', { layout: 'plain', kicker: 'Debrief', title: 'What did we notice?', body: `## Observers first
- Did the manager give facts before feelings?
- Did Charlie get to say their side?
- Were the two actions SMART, with a review date?
- Was the consequence stated calmly?

## Common slips
- Rescuing the silence instead of waiting
- Sounding like a lecture
- Vague actions: "be more careful"
- Forgetting the review date` });
takeaways('informal', [['Once, twice, then paper', 'Quiet word, "we have already discussed this", then a Coaching & Advice record.'], ['Facts, their words, SMART', 'Specific actions, a review date and the consequence.'], ['Same day, signed, copied', 'Accurate, fair, and both of you hold it.']]);
kc('informal');
order('informal', 'Put the escalation ladder in order, informal first.', [
  'A quiet word', '"We have already discussed this"', 'Coaching & Advice record', 'First written warning', 'Final written warning', 'Dismissal'],
  'lowest step first', 'Each step is more formal than the last. Skipping steps is only for serious misconduct, never for convenience.', 55);
choice('informal', 'Which of these is a SMART action?',
  'Be at your station in full uniform by the start of every shift, reviewed on 9 November',
  ['Try harder to be on time', 'Improve your attitude', 'Stop being so late'],
  'It says what, how we will know, and by when. The others are wishes, not actions.');
tf('informal', 'A Coaching & Advice record is a formal disciplinary warning.', false,
  'It is a documented informal conversation. It shows the issue was raised, what support was offered and what was agreed. It is what the formal route builds on if nothing changes.');
slide('informal', { layout: 'plain', kicker: 'Half-time', title: 'Break', mins: 10, body: 'Ten minutes. Scores so far are on the screen.' });

// ================================================================ 4 FACTS FIRST (14 min)
slide('invest', { layout: 'hero', img: 'evidence', kicker: 'Part 5', title: 'Facts first', body: `By the end of this section you can:
- Follow the route from concern to outcome
- Gather evidence and statements
- Know when to ring Ward Hadaway` });
slide('invest', { layout: 'visual', kicker: 'The route', title: 'From concern to outcome', visual: { type: 'steps', cols: 4, items: [
  { icon: '❗', title: 'Concern raised', text: 'A report, a complaint, something you saw.', tone: 'sage' },
  { icon: '☎️', title: 'Call the GM and HR', text: 'Before you act. Secure evidence.', tone: 'slate' },
  { icon: '🔍', title: 'Fact-find', text: 'Statements, records, a fact-finding meeting.', tone: 'gold' },
  { icon: '⚖️', title: 'Case to answer?', text: 'Is there enough to go to a hearing?', tone: 'clay' },
  { icon: '✉️', title: 'Invitation letter', text: 'Allegation, evidence, date, companion.', tone: 'sage' },
  { icon: '🗣️', title: 'Hearing', text: 'Chair, note-taker, employee, companion.', tone: 'slate' },
  { icon: '📄', title: 'Decision in writing', text: 'Outcome, reasons, right of appeal.', tone: 'gold' },
  { icon: '🔁', title: 'Appeal', text: 'Heard by someone not involved.', tone: 'clay' }] },
  body: 'The Acas Code: establish the facts, tell them in writing, hold a meeting, allow a companion, decide, and allow an appeal. Where possible the investigator and the decision-maker are different people.' });
slide('invest', { layout: 'visual', kicker: 'Fact-finding meeting', title: 'It is not a hearing', visual: { type: 'two',
  left: { title: 'It is', tone: 'sage', mark: 'tick', items: ['A chance to hear their side', 'Open questions: "tell me what happened"', 'Calm, private and confidential', 'Noted by a second person', 'Part of finding the facts'] },
  right: { title: 'It is not', tone: 'clay', mark: 'cross', items: ['Where you decide what happened', 'Where you give an outcome', 'Where you share your opinion', 'The same as a hearing'] } },
  body: 'The statutory right to be accompanied applies to hearings, not fact-finding meetings. Check our policy and ask HR before you refuse or allow.' });
slide('invest', { layout: 'visual', kicker: 'Evidence', title: 'Gather it all, then weigh it', visual: { type: 'cards', cols: 4, items: [
  { icon: '🗒️', title: 'Statements', text: 'From anyone who saw or heard something first-hand.', tone: 'sage' },
  { icon: '📹', title: 'CCTV', text: 'Secure it the same day. It gets overwritten.', tone: 'clay' },
  { icon: '🕒', title: 'Rotas and clocking', text: 'Who was working, and when.', tone: 'slate' },
  { icon: '🧾', title: 'Till and EPOS records', text: 'Voids, discounts, logins, times.', tone: 'gold' },
  { icon: '💬', title: 'Messages and emails', text: 'Texts, WhatsApp, emails that are relevant.', tone: 'slate' },
  { icon: '🎓', title: 'Training records', text: 'Were they trained? Did they sign for it?', tone: 'sage' },
  { icon: '📝', title: 'Earlier notes', text: '121 notes and Coaching & Advice records.', tone: 'gold' },
  { icon: '📘', title: 'Policies', text: 'The handbook rule and what was communicated.', tone: 'clay' }] },
  body: '**Fact**: "I saw", "the till shows", "the rota says". **Opinion**: "he is dodgy", "everyone knows". Only facts go in the case.' });
slide('invest', { layout: 'visual', kicker: 'Witness statements', title: 'What a good statement looks like', visual: { type: 'form', title: 'WITNESS STATEMENT', top: [{ k: 'Name and job title' }, { k: 'Date' }], fields: [
  { n: 1, label: 'In their own words', text: 'On Saturday 4 July at about 21:30 I was collecting glasses by the bar when I saw...', tip: 'First person, their own words. Not yours.', hi: true },
  { n: 2, label: 'What they saw or heard themselves', tip: 'Facts, times, places. Anything second-hand is marked "I was told".' },
  { n: 3, label: 'Who else was there', tip: 'Names, so you can check.' },
  { n: 4, label: 'Signed and dated', tip: '"This is a true record." Keep the original.' }] } });
slide('invest', { layout: 'plain', kicker: 'Suspension', title: 'Only if you must', body: `✔ A **neutral act**, not a punishment
✔ Only when needed: risk to people, to evidence or to the business
✔ As **short as possible**, reviewed often
✔ Normally on **full pay**, confirmed in writing
✔ Speak to HR **before** you do it
✘ Not a reflex, and not a way to "show we are serious"` });
slide('invest', { layout: 'visual', kicker: 'Ring early', title: 'When to call Ward Hadaway', visual: { type: 'cards', cols: 3, items: [
  { icon: '☎️', title: 'Before you suspend', text: 'It is rarely the right first move.', tone: 'sage' },
  { icon: '✉️', title: 'Before you send a hearing letter', text: 'Check the allegation and the evidence pack.', tone: 'slate' },
  { icon: '🛑', title: 'Before a final warning or dismissal', text: 'Check the process, the evidence and the outcome.', tone: 'gold' },
  { icon: '🛡️', title: 'Anything protected', text: 'Discrimination, whistleblowing, pregnancy or maternity, health or disability.', tone: 'clay' },
  { icon: '❓', title: 'If you are unsure', text: 'An hour on the phone costs far less than a claim.', tone: 'sage' },
  { icon: '👔', title: 'Always tell the GM first', text: 'They hold the contact details and the history.', tone: 'slate' }] } });
slide('invest', { layout: 'exercise', exercise: true, mins: 5, kicker: 'Group work · tables of four', title: 'The first hour',
  body: `**Saturday night.** The bar till is £60 short at close. A colleague tells you quietly, "It is always the new bar person, they have been giving drinks away."

As a table, write down **the first five things you do, in order**, and who you would call.` });
slide('invest', { layout: 'visual', kicker: 'Debrief', title: 'A model answer', visual: { type: 'steps', cols: 5, numbered: true, items: [
  { title: 'Do not confront', text: 'No accusations, no gossip, no action yet.', tone: 'clay' },
  { title: 'Secure the evidence', text: 'Till and EPOS records, the till roll, CCTV, the rota.', tone: 'slate' },
  { title: 'Tell the GM and HR', text: 'Before you speak to the new bar person.', tone: 'gold' },
  { title: 'Record the report', text: 'What the colleague said, when, in their words.', tone: 'sage' },
  { title: 'Plan the fact-finding', text: 'Statements first, then a meeting with a note-taker.', tone: 'ink' }] } });
takeaways('invest', [['Facts before action', 'Secure evidence, hear their side, and decide nothing until you know.'], ['Fact, not opinion', 'Statements are first-hand, in their own words, signed and dated.'], ['Ring early', 'Before you suspend, invite, or issue a final warning or dismissal.']]);
kc('invest');
choice('invest', 'On Friday night a till is £60 short, and someone says "it is always the new bar person". What do you do first?',
  'Secure the till records and CCTV, and speak to the GM and HR before talking to anyone',
  ['Confront the new bar person straight away', 'Tell the team to keep an eye on them', 'Send them a warning letter'],
  'Secure the evidence and get advice first. Everything else waits until you know what the records actually show.');
sort('invest', 'Fact, or opinion?', ['Fact', 'Opinion or rumour'], [
  ['I saw Alex carry two bottles out of the back door at 22:40', 0], ['The till shows a void at 21:15 under Sam\'s login', 0], ['Table 12 waited 40 minutes for starters', 0], ['The rota shows Robin was off that night', 0],
  ['Alex is dodgy', 1], ['Everyone knows Sam has been fiddling', 1], ['The kitchen are useless', 1], ['Robin never pulls their weight', 1]],
  'A fact can be checked. How someone seems to you is opinion, and what everyone knows is rumour.');
tf('invest', 'Where possible, the person who investigates should also be the person who decides the outcome.', false,
  'Separate them if you can. A different decision-maker is fairer, harder to challenge, and has not already formed a view.');

// ================================================================ 5 HEARINGS AND WARNINGS (20 min)
slide('hearing', { layout: 'hero', img: 'scales', kicker: 'Part 6', title: 'Hearings and warnings', body: `By the end of this section you can:
- Chair a hearing fairly
- Brief the note-taker and handle a companion
- Use the ladder, including gross misconduct` });
slide('hearing', { layout: 'plain', kicker: 'The invitation letter', title: 'It must say', body: `✔ **What the allegation is**, specifically
✔ **The evidence**: copies enclosed
✔ **Date, time and place**, with reasonable notice to prepare
✔ **Who will chair** and who will take notes
✔ **Their right to be accompanied**
✔ What the **outcome could be**, including dismissal if that is possible

> Never spring evidence on someone in the room.` });
slide('hearing', { layout: 'visual', kicker: 'The room', title: 'Who is there, and where', visual: { type: 'seating', seats: [
  { role: 'Chair', who: 'Runs it and decides', at: 'tl', tone: 'sage' }, { role: 'Note-taker', who: 'Records, takes no part', at: 'tr', tone: 'slate' },
  { role: 'Employee', who: 'Responds and explains', at: 'bl', tone: 'gold' }, { role: 'Companion', who: 'Colleague or union rep', at: 'br', tone: 'clay' }],
  notes: ['Private room, no interruptions', 'Phones off, door shut, a sign outside', 'Water and tissues on the table', 'Evidence pack in front of everyone'] } });
slide('hearing', { layout: 'visual', kicker: 'Three jobs', title: 'The chair, the note-taker and the companion', visual: { type: 'cards', cols: 3, items: [
  { icon: '⚖️', title: 'Chair', text: 'Runs the meeting and makes the decision. Explains the process, keeps it calm and fair, asks the questions, and does not pre-judge.', tone: 'sage' },
  { icon: '✍️', title: 'Note-taker', text: 'Writes down who said what, as close to word for word as possible. Takes no part, gives no opinion, and keeps it confidential. The notes are typed up and the employee gets a copy.', tone: 'slate' },
  { icon: '🤝', title: 'Companion', text: 'A colleague or trade union representative or official. Can address the hearing, put the case, sum up and confer. Cannot answer questions for the employee.', tone: 'gold' }] } });
slide('hearing', { layout: 'visual', kicker: 'Who can come', title: 'Who can be the companion', visual: { type: 'two',
  left: { title: 'The law gives the right to', tone: 'sage', mark: 'tick', items: ['A work colleague', 'A trade union representative', 'A trade union official'] },
  right: { title: 'Your call: ask HR first', tone: 'gold', items: ['A family member', 'A friend', 'A solicitor or legal adviser'] } },
  body: 'The right applies at a disciplinary or grievance **hearing** that could result in a warning or other action, and at an appeal. The employee must make a reasonable request. If the companion cannot attend, the employee can propose another time **within five working days** of the original, and you must postpone. Be consistent in the choices you make.' });
slide('hearing', { layout: 'visual', kicker: 'Running order', title: 'How the hearing runs', visual: { type: 'steps', cols: 3, items: [
  { title: 'Introductions and roles', text: 'Who is here, why, and how it will run. Confirm the companion.', tone: 'sage' },
  { title: 'The allegation and evidence', text: 'Chair sets out the management case and the evidence.', tone: 'slate' },
  { title: 'The employee responds', text: 'Their side, any mitigation, their questions and evidence.', tone: 'gold' },
  { title: 'Questions', text: 'Both ways, calmly and openly. Nobody interrupts.', tone: 'sage' },
  { title: 'Adjourn and decide', text: 'Take time to weigh all of it. Do not decide in the room.', tone: 'clay' },
  { title: 'Outcome and appeal', text: 'In writing, with reasons and the right to appeal.', tone: 'ink' }] } });
slide('hearing', { layout: 'exercise', exercise: true, mins: 5, kicker: 'Discussion · pairs', title: 'Spot the mistakes',
  body: `Six lines from a hearing. In pairs, mark each as **fine** or **a problem**, and say what you would do instead.

1. Chair: "I have already made up my mind, but go ahead."
2. Note-taker: "That is not what I heard. Let me say what happened."
3. Companion: "I will answer that for them, they are too upset."
4. Chair, at the end: "You are dismissed. That is all."
5. Chair: "I had a quick word with the witness at lunch. It is all fine."
6. Chair: "Here is the CCTV, you have not seen it before."` });
slide('hearing', { layout: 'visual', kicker: 'Debrief', title: 'Every one of those is a problem', visual: { type: 'cards', cols: 3, items: [
  { icon: '1', title: 'Pre-judged', text: 'Open mind or it is not a hearing.', tone: 'clay' },
  { icon: '2', title: 'Note-taker takes part', text: 'They record. They do not give evidence.', tone: 'clay' },
  { icon: '3', title: 'Companion answers', text: 'They can support and speak to the case, not answer for them.', tone: 'clay' },
  { icon: '4', title: 'No reasons, no appeal', text: 'The outcome goes in writing, with reasons and the right to appeal.', tone: 'clay' },
  { icon: '5', title: 'Private chat with a witness', text: 'Anything you hear goes in the notes and is shared.', tone: 'clay' },
  { icon: '6', title: 'Evidence sprung on them', text: 'They must see it beforehand, with time to prepare.', tone: 'clay' }] } });
slide('hearing', { layout: 'visual', kicker: 'Warnings', title: 'The ladder, with the way in', visual: { type: 'ladder', items: [
  { title: 'Quiet word / Coaching & Advice', text: 'Everyday conduct and performance', tone: 'sage', band: 'Informal' },
  { title: 'First written warning', text: 'Repeated or more serious misconduct', tone: 'gold', band: 'Formal' },
  { title: 'Final written warning', text: 'Serious misconduct, or a repeat after a first warning', tone: 'clay', band: 'Formal' },
  { title: 'Dismissal', text: 'Failure after a final warning, or gross misconduct', tone: 'ink', band: 'Formal' }],
  side: { title: 'Gross misconduct', text: 'So serious it destroys trust. It can come in at **any step**, up to dismissal, without a warning first. But only after a fair investigation and hearing.', tone: 'clay' } },
  body: 'Warnings have a stated length, in the outcome letter and our policy, and then lapse. They are not for ever.' });
slide('hearing', { layout: 'plain', kicker: 'Gross misconduct', title: 'So serious it breaks trust', body: `## Typical examples
- Theft, fraud or dishonesty
- Violence, threats or serious aggression
- Serious harassment or discrimination
- Being unfit through drink or drugs on duty
- Knowingly selling alcohol to under-18s
- Falsifying food safety, health and safety or financial records
- Serious breaches of health and safety

> It can lead to dismissal without notice. Always after a proper investigation and hearing. Check the handbook for our own list.` });
slide('hearing', { layout: 'visual', kicker: 'Fair dismissal', title: 'What a tribunal looks for', visual: { type: 'stats', items: [
  { big: '1', label: 'A genuine belief', tone: 'sage' }, { big: '2', label: 'On reasonable grounds', tone: 'slate' }, { big: '3', label: 'After a reasonable investigation', tone: 'gold' }] },
  body: `> Not "are we certain?" but "was our process fair?" Appeals go to someone not involved, ideally more senior. Always follow a fair process, whatever someone's length of service: the qualifying period is changing, some claims need no service at all, and fairness and consistency matter regardless. Ask HR if unsure.` });
takeaways('hearing', [['Right people, right room', 'Chair decides, note-taker records, companion supports.'], ['Open mind, in writing', 'Evidence in advance, reasons in the outcome, appeal offered.'], ['Ladder, with entry points', 'Seriousness sets where you start. Gross misconduct still needs a fair process.']]);
kc('hearing');
match('hearing', 'Match the person to the job.', [
  ['Chair', 'Runs the meeting and makes the decision'],
  ['Note-taker', 'Records what is said and takes no part'],
  ['Companion', 'Supports and speaks for the case, but cannot answer for them'],
  ['Employee', 'Responds to the allegations and gives their side']],
  'Each role has a job, and mixing them up is where hearings go wrong.');
choice('hearing', 'Sam asks to bring their dad to the disciplinary hearing. What is the position?',
  'It is not a legal right, so it is our call: take advice and be consistent',
  ['We must allow it', 'We must refuse it', 'We can allow it only if their dad works here'],
  'The statutory right covers a colleague or a trade union rep or official. Anyone else is discretionary, so decide it the same way you would for anyone, and take HR advice.');
tf('hearing', 'With gross misconduct you can dismiss on the spot and skip the hearing.', false,
  'The seriousness changes where you start and what the outcome can be. It does not remove the need to investigate, hold a hearing and listen to their side.');

// ================================================================ 6 GRIEVANCES (16 min)
slide('grievance', { layout: 'hero', img: 'mediation', kicker: 'Part 7', title: 'Grievances', body: `By the end of this section you can:
- Resolve issues at the lowest level that works
- Explain a written grievance and mediation
- Know when it must go straight to HR` });
slide('grievance', { layout: 'visual', kicker: 'The route', title: 'From a quiet word to a formal grievance', visual: { type: 'steps', cols: 3, items: [
  { icon: '🗣️', title: 'They talk it through', text: 'Ideally the two of them, directly and kindly.', tone: 'sage' },
  { icon: '🤝', title: 'Informal help from you', text: 'Listen, advise, maybe sit in or facilitate.', tone: 'slate' },
  { icon: '✍️', title: 'Put it in writing', text: 'If it did not work or they are not comfortable.', tone: 'gold' },
  { icon: '🧭', title: 'Mediation?', text: 'An impartial person helps both agree a way forward.', tone: 'sage' },
  { icon: '🔍', title: 'Formal investigation', text: 'Meeting, statements, evidence. Management decides.', tone: 'clay' },
  { icon: '📄', title: 'Outcome and appeal', text: 'In writing, with reasons. Possible disciplinary as a result.', tone: 'ink' }] } });
slide('grievance', { layout: 'visual', kicker: 'When someone brings you a problem', title: 'Do and do not', visual: { type: 'two',
  left: { title: 'Do', tone: 'sage', mark: 'tick', items: ['Listen, do not take sides', 'Ask what they would like to happen', 'Encourage them to talk to each other first', 'Offer to help set it up', 'Make brief notes and follow up'] },
  right: { title: 'Do not', tone: 'clay', mark: 'cross', items: ['Promise confidentiality you cannot keep', 'Promise an outcome', 'Decide before you have heard both sides', 'Gossip about it', 'Let it drift'] } },
  body: '> Harassment, discrimination, whistleblowing and health and safety concerns are serious. Do not fix them quietly: take advice the same day.' });
slide('grievance', { layout: 'visual', kicker: 'In writing', title: 'What a written grievance covers', visual: { type: 'cards', cols: 4, items: [
  { icon: '📍', title: 'What happened', text: 'The issue, with dates and examples.', tone: 'sage' },
  { icon: '💭', title: 'How it affects them', text: 'How it makes them feel and what it is doing to their work.', tone: 'slate' },
  { icon: '👥', title: 'Who saw it', text: 'Witnesses who could back it up.', tone: 'gold' },
  { icon: '🙋', title: 'What they have tried', text: 'Any attempt to sort it informally.', tone: 'clay' }] },
  body: 'And what they would like to happen. If they struggle to write it, help them, but it must be **their** words.' });
slide('grievance', { layout: 'visual', kicker: 'Mediation', title: 'A third person helps the two agree', visual: { type: 'steps', cols: 3, items: [
  { icon: '👂', title: 'Listen separately', text: 'The mediator hears each person on their own.', tone: 'sage' },
  { icon: '🪑', title: 'Meet together', text: 'A calm, structured conversation, led by the mediator.', tone: 'slate' },
  { icon: '✅', title: 'Agree and write it down', text: 'They decide the outcome themselves. It is confidential.', tone: 'gold' }] },
  body: 'Voluntary, impartial and confidential. **Good for** broken working relationships and clashes. **Not for** harassment, discrimination or serious allegations, or when someone needs a decision.' });
slide('grievance', { layout: 'visual', kicker: 'The formal route', title: 'When it goes formal', visual: { type: 'steps', cols: 5, items: [
  { title: 'Written grievance', text: 'Received and acknowledged.', tone: 'sage' },
  { title: 'Invited to a meeting', text: 'Reasonable notice. Right to be accompanied.', tone: 'slate' },
  { title: 'Investigate', text: 'Statements and evidence, as with discipline.', tone: 'gold' },
  { title: 'Decide', text: 'Upheld, partly upheld or not upheld, in writing.', tone: 'clay' },
  { title: 'Appeal', text: 'Heard by someone not involved.', tone: 'ink' }] },
  body: '> If it shows the other person did something wrong, that becomes a **separate** disciplinary process. Nobody hears a grievance about themselves.' });
slide('grievance', { layout: 'exercise', exercise: true, mins: 6, kicker: 'Role play 2 · groups of three', title: 'The first conversation',
  body: `**Sam** tells you that **Alex** keeps making jokes about their weight and gives them the worst jobs on the shift. Sam is upset and has not spoken to Alex.

You hear this for the first time. Listen, ask good questions, explain the options and agree next steps. **Do not promise an outcome.**`,
  visual: { type: 'cards', cols: 3, items: [
    { icon: '🧑‍💼', title: 'Manager', text: 'Listen. Ask what happened and what Sam wants. Explain: talk, mediation, or write it down.', tone: 'sage' },
    { icon: '😔', title: 'Sam', text: 'Hurt and wary: "I do not want to cause trouble". Open up if you feel heard.', tone: 'gold' },
    { icon: '👀', title: 'Observer', text: 'Did they listen first? Promise anything? Explain the options? Note safe next steps?', tone: 'slate' }] } });
slide('grievance', { layout: 'plain', kicker: 'Debrief', title: 'What did we notice?', body: `## What good looks like
- They listened without interrupting or fixing
- They asked what happened and what Sam would like
- They explained the options: talk, mediation, formal
- They said what they could and could not keep confidential
- They agreed a next step and a time to check in

> Comments about someone's body or appearance can be harassment. That one goes to the GM and HR the same day.` });
takeaways('grievance', [['Lowest level that works', 'Talk first, then help, then mediation, then formal.'], ['Listen, do not promise', 'No outcomes, no confidentiality you cannot keep.'], ['Serious means HR today', 'Harassment, discrimination, whistleblowing, safety.']]);
kc('grievance');
choice('grievance', 'Two bar staff have fallen out over cover. Alex comes to you upset. What do you do first?',
  'Ask whether they have spoken to the colleague, and encourage a direct conversation with your support',
  ['Move one of them to another section', 'Tell them to grow up and get on with it', 'Start a formal investigation'],
  'Lowest level that works. Most issues melt when two people actually talk. Be ready to help them do it.');
sort('grievance', 'Informal chat, or straight to the GM and HR?', ['Try an informal chat', 'GM and HR now'], [
  ['Two colleagues bickering over who clears the bar', 0], ['Someone upset about a rota swap', 0], ['Annoyed that the kitchen was left messy again', 0],
  ['Repeated unwanted comments about someone\'s body, after being asked to stop', 1], ['Concerns that unsafe food storage is being ignored', 1], ['A team member says they are being treated worse because of their religion', 1]],
  'Informal is for everyday friction. Anything involving harassment, discrimination, health and safety or whistleblowing is serious: do not try to fix it quietly, take advice at once.');
tf('grievance', 'If a grievance is about you, you can hear it yourself as long as you stay objective.', false,
  'Someone else should hear it: the GM or another manager. Nobody can be both the subject and the judge.');

// ================================================================ WRAP-UP (7 min)
slide('wrap', { layout: 'visual', kicker: 'Take it with you', title: 'Ten rules', visual: { type: 'steps', cols: 5, items: [
  { title: 'Hold your 121s', text: 'Prevention is better than cure.', tone: 'sage' },
  { title: 'Quiet word first', text: 'Early, private, curious.', tone: 'sage' },
  { title: 'Say it twice', text: '"We have already discussed this."', tone: 'slate' },
  { title: 'Third time on paper', text: 'Coaching & Advice, with SMART actions.', tone: 'slate' },
  { title: "Can't or won't?", text: 'Train and equip, or challenge.', tone: 'gold' },
  { title: 'Facts first', text: 'Evidence, statements, no rumour.', tone: 'gold' },
  { title: 'Ring Ward Hadaway early', text: 'Before you act, not after.', tone: 'clay' },
  { title: 'Right roles, right room', text: 'Chair, note-taker, companion.', tone: 'clay' },
  { title: 'Lowest level for grievances', text: 'Talk, mediate, then formal.', tone: 'ink' },
  { title: 'Fair, consistent, quick', text: 'Treat the same things the same way.', tone: 'ink' }] } });
slide('wrap', { layout: 'exercise', exercise: true, mins: 2, kicker: 'On your own', title: 'Your three commitments',
  body: `Write down **three things you will do in the next two weeks**. Be specific.

- Which 121s will you book, and with whom?
- Which conversation have you been putting off?
- What will you check with the GM or HR?` });
survey('wrap', 'In a few words: one thing you will do differently on Monday.', 45);
slide('wrap', { layout: 'hero', img: 'handshake', kicker: 'Thank you', title: 'Hold the 121. Have the quiet word.', body: 'Book your next 121s this week, and ring Ward Hadaway before you act, not after.' });

// ------------------------------------------------------------------ save
const quiz = LQ.normalizeQuiz({ title: 'Disciplinary & Grievance: Managers Training', settings: { brand: 'bhb', noTypeCards: true, noRoundCards: true, noScores: true, showAnswersOnPhones: true, maxPoints: 1000, minPoints: 500, rounds }, questions: qs });
const idFile = path.join(HERE, 'train-deck.id');
if (fs.existsSync(idFile)) quiz.id = fs.readFileSync(idFile, 'utf8').trim();

let bad = 0;
for (const q of quiz.questions) { const p = LQ.validate(q); if (p.length) { bad++; console.log('PROBLEM:', q.type, (q.text || '').slice(0, 60), '→', p.join(' ')); } }
const nq = quiz.questions.filter((q) => q.type !== 'slide').length, ns = quiz.questions.length - nq;
console.log(`${quiz.rounds.length} parts, ${ns} slides, ${nq} questions, ${bad} problems`);
for (const r of quiz.rounds) { const items = quiz.questions.filter((q) => q.round === r.id); console.log(`  ${r.title}: ${items.filter((q) => q.type === 'slide').length} slides, ${items.filter((q) => q.type !== 'slide').length} questions`); }
if (bad) process.exit(1);
const jsonOut = process.argv.indexOf('--json'); if (jsonOut > 0) fs.writeFileSync(process.argv[jsonOut + 1], JSON.stringify(quiz)); // for the test harness
if (DRY) process.exit(0);
const saved = await api('save', { quiz: LQ.quizForSave(quiz) });
const id = saved.id || saved.quiz?.id;
if (id) fs.writeFileSync(idFile, id);
console.log('saved', id);
