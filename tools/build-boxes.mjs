// Builds a Box Clever quiz (the team gambling game, assets/boxes.js) from the topic files in bank/topics and saves it.
//   node tools/build-boxes.mjs --title "Box Clever · 14 Nov" [--save] [--update <quiz id>] [--no-media] [--avoid <dir-of-old-quizzes>]
// Writes the quiz to tools/boxes-last.json first (always), then saves it with --save (host password in LQ_PASSWORD).
// What it makes: ten categories of 16 questions (the game picks five at random when it starts, and uses 10 per row, or more
// when more than 15 people join), a pile of spares for Swap, a pile the host has never seen for "Make the host answer", and the
// bonus rounds that fall between the four parts: Blockbusters, The Race, Draw It and five Answer Smashes.
// --warmup builds the one-phone version instead (code BOXCLEVER unless --code): you against three bots, 25 boxes (5 categories of 5),
// a round of Hot Potato after the 12th, no teams, no bonus. It leaves out everything in tools/boxes-last.json (the real quiz's pool),
// writes tools/boxes-warmup-last.json and saves it as a replayable warm-up game with --save.
// Questions that appeared in any quiz json under --avoid (default: ../lqsql/review and ../lqsql/backup) are left out.
import fs from 'node:fs'; import path from 'node:path'; import url from 'node:url';
const { LQ, api, uid } = await import('./lq.mjs');
const here = path.dirname(url.fileURLToPath(import.meta.url)), BANK = path.join(here, '..', 'bank');
const args = process.argv.slice(2), arg = (k, d) => (args.includes(k) ? args[args.indexOf(k) + 1] : d);
const TITLE = arg('--title', 'Box Clever'), SAVE = args.includes('--save'), WARM = args.includes('--warmup'), CODE = arg('--code', 'BOXCLEVER');
const AVOID = (arg('--avoid', '') ? [arg('--avoid', '')] : [path.join(here, '..', '..', 'lqsql', 'review'), path.join(here, '..', '..', 'lqsql', 'backup')]);
const shuffle = (a) => { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
const norm = (s) => String(s || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[^a-z0-9]+/g, ' ').trim();

// ---- what has been played already
const seenText = new Set();
for (const dir of AVOID) if (fs.existsSync(dir)) for (const f of fs.readdirSync(dir).filter((x) => x.endsWith('.json'))) {
  try { const j = JSON.parse(fs.readFileSync(path.join(dir, f), 'utf8')); const qs = j.questions || j.quiz?.questions || []; for (const q of qs) { if (q.text) seenText.add(norm(q.text)); for (const b of q.bank || []) seenText.add(norm(b.text)); for (const r of q.rows || []) seenText.add(norm(r.text)); } } catch { /* not a quiz */ }
}
const OTHER = path.join(here, WARM ? 'boxes-last.json' : 'boxes-warmup-last.json'); // the real quiz and the warm-up share no question, whichever is built second
if (fs.existsSync(OTHER)) {
  const real = JSON.parse(fs.readFileSync(OTHER, 'utf8'));
  for (const q of real.questions) { if (q.text) seenText.add(norm(q.text)); for (const c of q.cats || []) for (const x of c.qs) seenText.add(norm(x.t)); for (const x of [...(q.reserve || []), ...(q.hostq || [])]) seenText.add(norm(x.t)); for (const b of q.bank || []) seenText.add(norm(b.text)); }
}
console.log('questions already played:', seenText.size);

// ---- the topic files
const topics = JSON.parse(fs.readFileSync(path.join(BANK, 'topics.json'), 'utf8'));
const byTopic = {};
for (const f of fs.readdirSync(path.join(BANK, 'topics')).filter((x) => x.endsWith('.json'))) {
  const slug = f.replace(/\.json$/, '').split('__')[0], arr = JSON.parse(fs.readFileSync(path.join(BANK, 'topics', f), 'utf8'));
  for (const q of Array.isArray(arr) ? arr : arr.items || arr.questions || []) (byTopic[slug] = byTopic[slug] || []).push({ ...q, topic: slug });
}
const DECOYS = fs.existsSync(path.join(BANK, 'boxes-decoys.json')) ? Object.fromEntries(Object.entries(JSON.parse(fs.readFileSync(path.join(BANK, 'boxes-decoys.json'), 'utf8'))).map(([k, v]) => [norm(k), v])) : {}; // question text -> a believable wrong answer, written by hand
const isNum = (a) => /^d{4}$/.test(a) || /^[d,.]+$/.test(a);
const BAD = /\b(this picture|the picture|this image|the image|this clip|photo|shown|pictured|on screen|these)\b/i;
const okQ = (q) => q.text && q.text.length <= 170 && !BAD.test(q.text) && !seenText.has(norm(q.text))
  && ((q.type === 'choice' && Array.isArray(q.options) && q.options.length === 4 && new Set(q.options.map(norm)).size === 4 && q.options.every((o) => String(o).length <= 40))
    || (q.type === 'text' && Array.isArray(q.answers) && q.answers.length && String(q.answers[0]).split(/\s+/).length <= 4 && String(q.answers[0]).length <= 32));

const CATS = [
  ['TV & Film', '🎬', ['british-sitcoms', 'soaps', 'reality-tv', 'quiz-shows', 'crime-dramas', 'friends', 'the-office', 'british-films', 'action-films', 'film-quotes', 'rom-coms', 'horror-films', 'us-tv', 'doctor-who', 'kids-tv']],
  ['Sport', '⚽', ['football', 'world-cup', 'olympics', 'cricket', 'rugby', 'tennis-golf', 'motorsport', 'boxing-combat', 'newcastle-v-sunderland']],
  ['In the news', '📰', ['covid-19', 'days-that-shook-the-world', 'the-2000s', 'the-2010s', 'famous-firsts', 'record-breakers']],
  ['History', '🏛️', ['british-history', 'tudors', 'world-wars', 'ancient-history', '20th-century', 'famous-people']],
  ['Disney', '🏰', ['disney', 'pixar-animation']],
  ['Science', '🔬', ['space', 'human-body', 'science-technology', 'animals', 'nature-environment', 'computers-internet', 'maths-numbers']],
  ['Celebrities', '⭐', ['royal-family', 'oscars', 'one-hit-wonders', 'boy-bands-girl-groups', 'reality-tv', 'pop-music']],
  ['Music', '🎵', ['pop-music', 'rock-music', 'the-beatles', 'number-ones', 'eurovision', 'music-lyrics', 'classical-music']],
  ['Geography', '🌍', ['uk-geography', 'world-geography', 'capital-cities', 'landmarks', 'flags', 'europe', 'usa']],
  ['Food & Drink', '🍔', ['food-drink', 'british-food', 'beer-wine-spirits', 'brands-logos']],
];
const taken = new Set();
const take = (q) => { taken.add(norm(q.text)); return q; };
/** n items with roughly 25% easy, 45% medium, 30% hard, taken from `pool` (shuffled). */
function mix(pool, n) {
  const want = { easy: Math.round(n * 0.25), medium: Math.round(n * 0.45) }; want.hard = n - want.easy - want.medium;
  const out = [], rest = shuffle(pool);
  for (const d of ['easy', 'medium', 'hard']) for (const q of rest.filter((x) => (x.difficulty || 'medium') === d).slice(0, want[d])) out.push(q);
  for (const q of rest) { if (out.length >= n) break; if (!out.includes(q)) out.push(q); }
  return shuffle(out.slice(0, n));
}
/** A believable wrong answer for a typed question: a nearby year or number, or another answer from the same topic of the same shape. */
function decoyFor(q) {
  const a = String(q.answers[0]);
  if (DECOYS[norm(q.text)]) return DECOYS[norm(q.text)];
  if (/^d{4}$/.test(a)) { const y = +a; const c = [y - 4, y - 3, y - 2, y - 1, y + 1, y + 2, y + 3, y + 5].filter((x) => x > 1000 && x <= 2026); return String(c[Math.floor(Math.random() * c.length)]); }
  const n = parseFloat(a.replace(/,/g, '')); const f = [0.5, 0.75, 1.25, 1.5, 2][Math.floor(Math.random() * 5)]; return String(Math.round(n * f));
}
const textOk = (q) => q.type !== 'text' || !!DECOYS[norm(q.text)] || isNum(String(q.answers[0]));
const toQ = (q, siblings) => q.type === 'choice' ? { t: q.text, o: q.options.map(String), d: q.difficulty || 'medium' } : { t: q.text, a: q.answers.map(String), w: decoyFor(q), d: q.difficulty || 'medium' };

// ---- pictures and tunes: a category's board is mixed up with "Who is this?" pictures and Name That Tune clips (--no-media leaves them out)
const PLAN = {
  'Music': { tune: 6, tt: ['pop-music', 'rock-music', 'the-beatles', 'number-ones', 'eurovision', 'one-hit-wonders', 'the-1980s', 'the-1990s', 'the-2000s', 'the-2010s', 'boy-bands-girl-groups'] },
  'TV & Film': { tune: 3, tt: ['james-bond', 'musicals', 'action-films', 'rom-coms', 'kids-tv', 'film-quotes', 'doctor-who', 'horror-films'], pic: 2, pt: ['james-bond', 'the-office', 'friends', 'doctor-who', 'oscars'], who: 'Who or what is this?' },
  'Celebrities': { pic: 6, pt: ['royal-family', 'oscars', 'boy-bands-girl-groups', 'pop-music', 'the-2010s', 'reality-tv'], who: 'Who is this?' },
  'Sport': { pic: 4, pt: ['football', 'olympics', 'rugby', 'tennis-golf', 'boxing-combat', 'motorsport', 'cricket'], who: 'Who is this?', tune: 2, tt: ['football', 'olympics', 'world-cup', 'newcastle-v-sunderland'] },
  'Geography': { pic: 5, pt: ['landmarks'], who: 'What is this?' },
  'History': { pic: 4, pt: ['famous-people', 'tudors', 'british-history', 'world-wars', 'ancient-history'], who: 'Who or what is this?' },
  'In the news': { pic: 3, pt: ['famous-firsts', 'covid-19', 'the-2010s'], who: 'Who is this?' },
  'Disney': { tune: 4, tt: ['disney', 'pixar-animation'] },
  'Science': { pic: 3, pt: ['space', 'animals', 'human-body', 'nature-environment'], who: 'Who or what is this?' },
  'Food & Drink': { pic: 4, pt: ['british-food', 'food-drink', 'beer-wine-spirits'], who: 'Who or what is this?' },
};
const NOMEDIA = args.includes('--no-media'), SCALE = WARM ? 0.55 : 1;
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
const cleanTitle = (t) => String(t).replace(/\s*[\(\[][^)\]]*[\)\]]/g, '').replace(/\s+-\s+.*$/, '').trim();
const surname = (n) => { const w = n.replace(/\s*\(.*\)/, '').split(/\s+/); return w.length > 1 && !/^(the|of|de|la|el)$/i.test(w[w.length - 1]) ? w[w.length - 1] : ''; };
let lastItunes = 0;
async function itunes(track, artist) {
  const bad = /karaoke|tribute|in the style of|cover|instrumental|made famous|originally performed|piano dreamers/i;
  for (let tries = 0; tries < 3; tries++) {
    const wait = 1700 - (Date.now() - lastItunes); if (wait > 0) await sleep(wait); lastItunes = Date.now();
    try {
      const r = await fetch(`https://itunes.apple.com/search?term=${encodeURIComponent(track + ' ' + artist)}&entity=song&country=GB&limit=10`);
      if (r.status === 403 || r.status === 429) { await sleep(8000); continue; }
      if (!r.ok) return null;
      const hits = ((await r.json()).results || []).filter((x) => x.previewUrl && !bad.test(`${x.trackName} ${x.artistName} ${x.collectionName}`));
      const sc = (x) => (norm(x.trackName) === norm(track) ? 4 : norm(x.trackName).startsWith(norm(track)) ? 2 : norm(x.trackName).includes(norm(track)) ? 1 : 0) + (norm(x.artistName) === norm(artist) ? 3 : norm(x.artistName).includes(norm(artist)) || norm(artist).includes(norm(x.artistName)) ? 2 : 0);
      const best = hits.map((x) => ({ x, s: sc(x) })).filter((y) => y.s >= 3).sort((a, b) => b.s - a.s)[0];
      return best ? best.x : null;
    } catch { await sleep(3000); }
  }
  return null;
}
const pickN = (arr, n, not) => shuffle(arr.filter((x) => !not.includes(x))).slice(0, n);
async function mediaFor(name, plan) {
  const out = [], nTune = Math.round((plan.tune || 0) * SCALE), nPic = Math.round((plan.pic || 0) * SCALE);
  if (nTune) {
    const items = shuffle((plan.tt || []).flatMap((sl) => (byTopic[sl] || []).filter((q) => q.type === 'tune' && ['artist', 'song', 'film'].includes(q.ask) && (q.ask !== 'film' || q.film) && !seenText.has(norm(q.track + ' ' + q.artist)))));
    const ans = (q) => q.ask === 'artist' ? q.artist : q.ask === 'film' ? q.film : cleanTitle(q.track);
    const pool = (ask) => [...new Set(items.filter((q) => q.ask === ask).map(ans))];
    const seenTrack = new Set(); let made = 0;
    for (const q of items) {
      if (made >= nTune) break; const key = norm(q.track); if (seenTrack.has(key) || taken.has(norm(q.track + ' ' + q.artist))) continue; seenTrack.add(key);
      const hit = await itunes(q.track, q.artist); if (!hit) { console.log('  no clip for', q.track, '/', q.artist); continue; }
      const right = ans(q), alts = q.ask === 'artist' ? [q.artist, q.artist.replace(/^The /i, ''), q.artist.split(/ (?:&|and|feat\.?|ft\.?|vs\.?) |, /i)[0]] : q.ask === 'song' ? [right, cleanTitle(hit.trackName)] : [right];
      const others = pool(q.ask).filter((x) => norm(x) !== norm(right));
      const t = q.ask === 'artist' ? 'Who is the artist?' : q.ask === 'song' ? 'Name this song' : 'Which film is this song from?';
      const m = { k: 'tune', url: hit.previewUrl, start: 0, len: 15, credit: 'Preview via Apple Music' };
      const d = q.difficulty || 'medium';
      if (others.length >= 3 && Math.random() < 0.5) out.push({ t, m, o: [right, ...pickN(others, 3, [])], d });
      else if (others.length >= 1) out.push({ t, m, a: [...new Set(alts.filter(Boolean))], w: others[Math.floor(Math.random() * others.length)], d });
      else continue;
      taken.add(norm(q.track + ' ' + q.artist)); made++; console.log('  tune:', name, '·', q.track, '→', right);
    }
  }
  if (nPic) {
    const items = shuffle((plan.pt || []).flatMap((sl) => (byTopic[sl] || []).filter((q) => q.type === 'smash' && q.pictureAnswer).map((q) => q.pictureAnswer)));
    const notPerson = /palace|castle|house|abbey|cathedral|tower|bridge|park|stadium|cup|trophy|crown|jewels|coach|corgi|ship|mary rose|hall|street|square|film|\(.*\)/i, people = /^Who is/.test(plan.who);
    const names = [...new Set(items)], pool = names.filter((n) => n.length <= 32 && !/\bfilm\b|\(.*\)/i.test(n) && (!people || (n.split(/\s+/).length >= 2 && !notPerson.test(n))));
    let made = 0;
    for (const nm of pool) {
      if (made >= nPic) break; if (taken.has(norm('pic ' + nm))) continue;
      let pic = null; try { pic = await api('picture', { title: nm }); } catch (e) { console.log('  no picture for', nm, String(e.message).slice(0, 60)); continue; }
      if (!pic?.url) continue;
      const m = { k: 'img', url: pic.url, credit: 'Wikipedia / Wikimedia Commons: ' + nm };
      const same = pool.filter((x) => x !== nm && x.split(/\s+/).length === nm.split(/\s+/).length), others = same.length >= 4 ? same : pool.filter((x) => x !== nm);
      if (Math.random() < 0.5) out.push({ t: plan.who, m, o: [nm, ...pickN(others, 3, [])], d: 'medium' });
      else out.push({ t: plan.who, m, a: [...new Set([nm, surname(nm)].filter(Boolean))], w: others[Math.floor(Math.random() * others.length)], d: 'medium' });
      taken.add(norm('pic ' + nm)); made++; console.log('  picture:', name, '·', nm);
    }
  }
  return out;
}
const MEDIA = {};
if (!NOMEDIA && !args.includes('--candidates')) for (const [name] of CATS) if (PLAN[name]) MEDIA[name] = await mediaFor(name, PLAN[name]);

const cats = [], spare = [];
for (const [name, emoji, slugs] of CATS) {
  const all = []; const seen = new Set();
  for (const s of slugs) for (const q of byTopic[s] || []) if (okQ(q) && !seen.has(norm(q.text)) && !taken.has(norm(q.text))) { seen.add(norm(q.text)); all.push(q); }
  const ch = all.filter((q) => q.type === 'choice'), tx = all.filter((q) => q.type === 'text' && textOk(q));
  if (args.includes('--candidates')) { console.log('## ' + name); for (const q of shuffle(all.filter((x) => x.type === 'text' && !isNum(String(x.answers[0])) && !DECOYS[norm(x.text)] && x.difficulty !== 'hard')).slice(0, 14)) console.log(JSON.stringify(q.text) + ' => ' + q.answers[0]); continue; }
  const med = MEDIA[name] || [], N = WARM ? 10 : 16, nT = Math.max(0, (WARM ? 2 : 5) - Math.floor(med.length / 3)), nC = Math.max(0, N - nT - med.length);
  const board = [...mix(ch, nC), ...mix(tx, nT)].map(take);
  const left = all.filter((q) => !board.includes(q));
  spare.push(...left.map((q) => ({ q, siblings: tx })));
  cats.push({ name, emoji, qs: shuffle([...board.map((q) => toQ(q, tx)), ...med]) });
  console.log(name.padEnd(13), 'pool', ch.length + 'c/' + tx.length + 't', '-> board', board.length, '+ media', med.length);
}
if (args.includes('--candidates')) process.exit(0);
const spareQs = shuffle(spare).filter(({ q }) => !taken.has(norm(q.text)));
const reserve = [], hostq = [];
for (const { q, siblings } of spareQs) { if (taken.has(norm(q.text))) continue; if (reserve.length < 24 && (q.difficulty || 'medium') !== 'hard') { reserve.push(toQ(q, siblings)); take(q); } else if (hostq.length < 10) { hostq.push(toQ(q, siblings)); take(q); } if (reserve.length >= 24 && hostq.length >= 10) break; }
console.log('reserve', reserve.length, 'host', hostq.length);

if (WARM) {
  const settings = { ...LQ.DEFAULT_SETTINGS }, items = [], rounds = [];
  const choiceBank = (n) => { const out = []; for (const sl of ['general-knowledge', 'british-history', 'world-geography', 'science-technology', 'food-drink', 'animals', 'pop-music', 'british-sitcoms', 'the-1990s', 'uk-geography', 'space', 'film-quotes']) for (const q of byTopic[sl] || []) if (q.type === 'choice' && okQ(q) && !taken.has(norm(q.text)) && ['easy', 'medium'].includes(q.difficulty || 'medium')) out.push(q); return mix(out, n).map(take).map((q) => ({ id: uid('b'), text: q.text, options: q.options.map(String) })); };
  const solo = { solo: true, cols: 5, cuts: [12, 25], start: 1000 };
  const round = (title, intro, it) => { const id = uid('r'), m = {}; for (const q of it) { q.round = id; m[q.type] = (m[q.type] || 0) + 1; } rounds.push({ id, title, intro, brief: '', mix: m, count: it.length, types: Object.keys(m), practice: false }); items.push(...it); };
  const box = (part, extra) => ({ id: uid('q'), type: 'boxes', text: 'Box Clever', time: 0, media: { kind: 'none' }, partial: false, part, ...solo, ...extra });
  round('Box Clever', 'You against three bots. Twenty-five boxes.', [box(1, { cats, reserve: reserve.slice(0, 14) })]);
  round('Hot Potato', 'Pass the bomb. Your points go into your pot.', [{ ...LQ.newQuestion('potato', settings), text: 'Hot Potato', bank: choiceBank(24), category: 'General knowledge', difficulty: 'medium' }]);
  round('Box Clever: the rest', 'Back to the boxes.', [box(2)]);
  const problems = []; items.forEach((q, i) => { const p = LQ.validate(q); if (p.length) problems.push(i + 1 + ' ' + q.type + ': ' + p.join('; ')); });
  console.log('problems:', problems.length ? problems.join(' | ') : 'none');
  const stamp = new Date().toISOString().slice(0, 10);
  settings.warmup = { code: CODE, open: true, fun: true, replay: true, bots: 3, forQuiz: null, from: null, until: null, season: 's-boxclever-' + stamp };
  const quiz = { title: TITLE, settings: { ...settings, rounds }, questions: items };
  fs.writeFileSync(path.join(here, 'boxes-warmup-last.json'), JSON.stringify(quiz, null, 1));
  console.log(`warm-up: ${cats.length} categories, board pool ${cats.reduce((a, c) => a + c.qs.length, 0)} (${cats.reduce((a, c) => a + c.qs.filter((q) => q.a).length, 0)} typed), potato ${items[1].bank.length}`);
  if (SAVE && !problems.length) { const r = await api('save', { quiz }); console.log('SAVED', r.id || JSON.stringify(r)); } else console.log('(dry run: tools/boxes-warmup-last.json written, nothing saved)');
  process.exit(0);
}

// ---- bonus rounds
const choicePool = (slugs, n, diff) => { const out = []; for (const s of slugs) for (const q of byTopic[s] || []) if (q.type === 'choice' && okQ(q) && !taken.has(norm(q.text)) && (!diff || diff.includes(q.difficulty || 'medium'))) out.push(q); return mix(out, n).map(take); };
const bbBank = choicePool(['general-knowledge', 'british-history', 'world-geography', 'science-technology', 'food-drink', 'animals', 'pop-music', 'british-sitcoms', 'football', 'the-1990s'], 26, ['easy', 'medium']).map((q) => ({ id: uid('b'), text: q.text, options: q.options, difficulty: q.difficulty || 'medium' }));
const raceBank = choicePool(['general-knowledge', 'uk-geography', 'space', 'the-1980s', 'film-quotes', 'landmarks', 'human-body', 'pop-music', 'olympics', 'brands-logos'], 22, ['easy', 'medium']).map((q) => ({ id: uid('b'), text: q.text, options: q.options }));
const smashes = shuffle(['smash-1', 'smash-2', 'smash-3'].flatMap((f) => JSON.parse(fs.readFileSync(path.join(BANK, f + '.json'), 'utf8')))).filter((x) => x.pictureAnswer && x.clueAnswer && LQ.smashOf(x.pictureAnswer, x.clueAnswer).smash && !seenText.has(norm(x.text)));

const settings = { ...LQ.DEFAULT_SETTINGS };
const rounds = [], questions = [];
const round = (title, intro, items) => { const id = uid('r'), mixc = {}; for (const q of items) { q.round = id; mixc[q.type] = (mixc[q.type] || 0) + 1; } rounds.push({ id, title, intro, brief: '', mix: mixc, count: items.length, types: Object.keys(mixc), practice: false }); questions.push(...items); };
const slide = (text, body) => ({ id: uid('q'), type: 'slide', text, body, time: 20, media: { kind: 'none' } });
const box = (part, extra) => ({ id: uid('q'), type: 'boxes', text: 'Box Clever', time: 0, media: { kind: 'none' }, partial: false, part, ...extra });
const nq = (type, extra) => ({ ...LQ.newQuestion(type, settings), ...extra });

round('Welcome', '', [slide('📦 Box Clever', 'Tonight you play in teams.\n\nFifty boxes. Five categories. One big gamble.\n\nGrab your phone: you will be put on a team.'),
  slide('How it works', 'Every team starts with 10,000 points.\n\nYour captain picks a box and decides how much to gamble.\n\nRight: you win the stake. Wrong: you lose it.\n\nNot sure? Pass for half the stake, but everyone sees the question.\n\nFive powers, once each. Use them wisely.')]);
round('Box Clever 1', 'The first dozen boxes.', [box(1, { cats, reserve, hostq })]);
round('Blockbusters', 'Everyone plays. Your points go into your team pot.', [nq('blockbusters', { text: 'Blockbusters: General knowledge', bank: bbBank, category: 'General knowledge', difficulty: 'medium' })]);
round('Box Clever 2', 'Back to the boxes.', [box(2)]);
round('The Race', 'Everyone races. Your points go into your team pot.', [nq('race', { text: 'The Race: general knowledge', bank: raceBank, category: 'General knowledge', difficulty: 'medium' })]);
round('Box Clever 3', 'Three quarters of the way through.', [box(3)]);
round('Draw It', 'Everyone guesses. Your points go into your team pot.', [nq('draw', { text: 'Draw It', words: shuffle(LQ.DRAW_WORDS).slice(0, 15), category: 'Draw It', difficulty: 'easy' })]);
round('Box Clever 4', 'Every last box.', [box(4)]);
const smashItems = [];
for (const s of smashes.slice(0, 5)) {
  let pic = null; if (SAVE || args.includes('--pictures')) { try { pic = await api('picture', { title: s.pictureAnswer }); } catch (e) { console.log('  no picture for', s.pictureAnswer, e.message); } }
  smashItems.push(nq('smash', { text: s.text, time: 25, smash: LQ.smashOf(s.pictureAnswer, s.clueAnswer).smash, pictureAnswer: s.pictureAnswer, clueAnswer: s.clueAnswer, category: s.category || 'Wordplay', difficulty: s.difficulty || 'medium', ai: false, media: pic ? { kind: 'image', url: pic.url, credit: 'Wikipedia / Wikimedia Commons: ' + s.pictureAnswer, source: pic.source } : { kind: 'image', url: '' } }));
}
round('Double Points: Answer Smash', 'Double points! Every right answer counts twice, and goes into your team pot.', smashItems);
rounds[rounds.length - 1].double = true;

const quiz = { ...(arg('--update', '') ? { id: arg('--update', '') } : {}), title: TITLE, settings: { ...settings, rounds }, questions };
fs.writeFileSync(path.join(here, 'boxes-last.json'), JSON.stringify(quiz, null, 1));
const n = cats.reduce((a, c) => a + c.qs.length, 0), tx = cats.reduce((a, c) => a + c.qs.filter((q) => q.a).length, 0);
console.log(`board pool ${n} (${tx} typed), items ${questions.length}, smash ${smashItems.length}, pictures ${smashItems.filter((x) => x.media.url).length}`);
if (SAVE) { const r = await api('save', { quiz }); console.log('SAVED', r.id || JSON.stringify(r)); } else console.log('(dry run: tools/boxes-last.json written, nothing saved)');
