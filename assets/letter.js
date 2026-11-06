/* Let's Quiz: THE TRAITOR'S LETTER. A sheet of paper folded in three and sealed with wax: the seal cracks, the folds open,
 * and the message appears in blackletter. Pure CSS animation (see "The Traitor's letter" in style.css), so the host screen and
 * the phones show exactly the same thing: put trLetterHtml(text) in the page and it plays once, from the start.
 * Used by assets/traitors.js (the host screen) and assets/traitors-phone.js (phones). Loaded before both. */

const TR_LETTER_TITLE = '📜 THE TRAITOR HAS A MESSAGE FOR YOU!';
/** After half time the letters come from "the Traitors" (the number is never given away). */
const TR_LETTER_TITLE_PL = '📜 THE TRAITORS HAVE A MESSAGE FOR YOU!';
const trLetterEsc = (s) => String(s ?? '').replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
/** The Traitors crest: the arch with the lightning bolt, the same mark as on the letter. Gold by default (see .trcrest). */
const trCrestSvg = (cls = '') => `<svg class="trcrest ${cls}" viewBox="0 0 60 66" aria-hidden="true"><path d="M6 62 C6 28 18 8 30 3 C42 8 54 28 54 62 L46 62 C46 36 40 22 30 14 C20 22 14 36 14 62 Z" fill="currentColor"/><path d="M33 34 L37 30 L35 40 L40 38 L31 52 L32 42 L27 44 Z" fill="currentColor"/></svg>`;
/** Short notes are written big, long ones smaller, so a 140-character message still fits the page. */
const trLetterSize = (n) => (n <= 40 ? 0.24 : n <= 80 ? 0.2 : n <= 120 ? 0.17 : n <= 180 ? 0.14 : 0.115);

function trLetterSheet(text, i, o = {}) {
  const t = String(text || '');
  return `<div class="ltr-sheet" style="top:calc(var(--H) * -${i})"${i === 1 ? '' : ' aria-hidden="true"'}>
    <div class="ltr-frame"></div>
    <svg class="ltr-crest ltr-ink" viewBox="0 0 60 66" aria-hidden="true"><path d="M6 62 C6 28 18 8 30 3 C42 8 54 28 54 62 L46 62 C46 36 40 22 30 14 C20 22 14 36 14 62 Z" fill="currentColor"/><path d="M33 34 L37 30 L35 40 L40 38 L31 52 L32 42 L27 44 Z" fill="currentColor"/></svg>
    <div class="ltr-dear ltr-ink">${trLetterEsc(o.to || 'Dear Faithful,')}</div>
    <div class="ltr-msg ltr-ink" style="font-size:calc(var(--H) * ${trLetterSize(t.length)})"><span>${trLetterEsc(t)}</span></div>
    <div class="ltr-sign ltr-ink"><span>Signed,</span><b>${trLetterEsc(o.sign || 'The Traitors')}</b></div>
  </div>`;
}
/** The letter, closed to start with: seal, then the bottom fold opens, then the top, then the ink comes up. */
/** o.to is the greeting ("Dear Faithful," by default) and o.sign who signs it ("The Traitors" by default; Claudia for her own messages). */
function trLetterHtml(text, o = {}) {
  const seal = '<span class="ltr-wax"><svg viewBox="0 0 100 100" aria-hidden="true"><circle cx="50" cy="50" r="46" fill="none" stroke="rgba(60,0,0,.45)" stroke-width="3"/><circle cx="50" cy="50" r="38" fill="none" stroke="rgba(60,0,0,.3)" stroke-width="2"/><path d="M50 12 L57 43 L88 50 L57 57 L50 88 L43 57 L12 50 L43 43 Z M24 24 L46 46 M76 24 L54 46 M24 76 L46 54 M76 76 L54 54" fill="rgba(255,255,255,.1)" stroke="rgba(60,0,0,.5)" stroke-width="2.5" stroke-linejoin="round"/><circle cx="50" cy="50" r="7" fill="rgba(60,0,0,.35)"/></svg></span>';
  return `<div class="ltr" role="img" aria-label="A sealed letter from the Traitor: ${trLetterEsc(text)}"><div class="ltr-stage">
    <div class="ltr-panel ltr-top"><div class="ltr-f ltr-front">${trLetterSheet(text, 0, o)}</div><div class="ltr-f ltr-back"></div></div>
    <div class="ltr-panel ltr-mid"><div class="ltr-f ltr-front">${trLetterSheet(text, 1, o)}</div></div>
    <div class="ltr-panel ltr-bot"><div class="ltr-f ltr-front">${trLetterSheet(text, 2, o)}</div><div class="ltr-f ltr-back"><div class="ltr-seal"><i class="l">${seal}</i><i class="r">${seal}</i></div></div></div>
  </div></div>`;
}

/** Message starters for the Traitor: tap one, then fill in the "…" (it is selected for you). */
const TR_PROMPTS = [
  "That's what you get for …",
  'The next person to … gets double points on a question.',
  'I think someone might be on to me… maybe I should punish them?',
  'I saw that, … Did you really think I would not?',
  'Someone in this room is not who they say they are.',
  'Trust no one. Not even …',
  'Whoever is winning, enjoy it while it lasts.',
  '… you have been very quiet. What are you hiding?',
  'One of you will regret answering that question.',
  'Nice answer, … A pity about what comes next.',
  'Do not look at me. Look at …',
  'I am feeling generous tonight… or am I?',
  'The next person to … might just lose something.',
  'Points are only numbers. Friends are only … for now.'
];

/** THE TASKMASTER LETTER: the same folded, wax-sealed sheet as the Traitor's letter (same animation, see .tmltr in style.css), in the
 *  Taskmaster look: grey typed paper and a red TN seal. The seal cracks, the folds open, the details are typed in.
 *  o = { kicker, sub, body, foot }. Used for the Taskmaster round card and task cards on the host screen and on phones. */
const tmLetterSize = (n, big, small) => (n <= 120 ? big : n <= 190 ? big * 0.88 : n <= 270 ? big * 0.76 : small);
function tmLetterSheet(o, i) {
  const sub = String(o.sub || ''), mid = sub || String(o.kicker || ''), top = sub ? String(o.kicker || '') : '', body = String(o.body || ''), foot = String(o.foot || '');
  return `<div class="ltr-sheet" style="top:calc(var(--H) * -${i})"${i === 1 ? '' : ' aria-hidden="true"'}>
    <div class="tm-head ltr-ink">TASKMASTER</div>${top ? `<div class="tm-kick ltr-ink">${trLetterEsc(top)}</div>` : ''}
    <div class="tm-sub ltr-ink" style="font-size:calc(var(--H) * ${sub ? (mid.length <= 12 ? 0.36 : mid.length <= 22 ? 0.28 : 0.22) : 0.2})">${trLetterEsc(mid)}</div>
    ${body ? `<div class="tm-body ltr-ink" style="font-size:calc(var(--H) * ${tmLetterSize(body.length, 0.115, 0.07)})">${trLetterEsc(body)}</div>` : ''}
    ${foot ? `<div class="tm-foot ltr-ink">${trLetterEsc(foot)}</div>` : ''}
  </div>`;
}
function tmLetterHtml(o = {}) {
  const seal = '<span class="tm-wax"><b>TN</b></span>';
  const label = [o.kicker, o.sub, o.body, o.foot].filter(Boolean).join('. ');
  return `<div class="ltr tmltr" role="img" aria-label="Taskmaster: ${trLetterEsc(label)}"><div class="ltr-stage">
    <div class="ltr-panel ltr-top"><div class="ltr-f ltr-front">${tmLetterSheet(o, 0)}</div><div class="ltr-f ltr-back"></div></div>
    <div class="ltr-panel ltr-mid"><div class="ltr-f ltr-front">${tmLetterSheet(o, 1)}</div></div>
    <div class="ltr-panel ltr-bot"><div class="ltr-f ltr-front">${tmLetterSheet(o, 2)}</div><div class="ltr-f ltr-back"><div class="tm-closed">TASKMASTER</div><div class="ltr-seal"><i class="l">${seal}</i><i class="r">${seal}</i></div></div></div>
  </div></div>`;
}
