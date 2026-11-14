// Builds the pool of Box Clever games for the TV (tvbox.html): N games of five mixed categories, 30 boxes, two players, no bots, two typed
// questions in each category (there is no timer, so there is time to use the Fire TV keyboard). No question appears twice across the whole pool, or in anything played before (build-boxes.mjs's own rules).
//   node tools/build-tvbox.mjs [--games 50] [--from 1]      writes tvbox/games/gNN.json and tvbox/index.json
// The games are static files the TV page loads; nothing is saved to the quiz database.
import fs from 'node:fs'; import path from 'node:path'; import url from 'node:url'; import { spawnSync } from 'node:child_process';
const here = path.dirname(url.fileURLToPath(import.meta.url)), root = path.join(here, '..'), OUT = path.join(root, 'tvbox'), GAMES = path.join(OUT, 'games');
const args = process.argv.slice(2), arg = (k, d) => (args.includes(k) ? args[args.indexOf(k) + 1] : d);
const N = +arg('--games', 50), FROM = +arg('--from', 1);
fs.mkdirSync(GAMES, { recursive: true });

// name, emoji, topic slugs, how many games it can appear in at most (its pool is about 55% usable at ten questions a go)
const CATS = [
  ['TV & Film', '🎬', ['british-sitcoms', 'soaps', 'quiz-shows', 'crime-dramas', 'the-office', 'british-films', 'action-films', 'film-quotes', 'rom-coms', 'horror-films', 'us-tv', 'doctor-who', 'james-bond', 'musicals', 'friends', 'reality-tv'], 14],
  ['Disney & Kids', '🏰', ['disney', 'pixar-animation', 'kids-tv', 'childrens-books'], 8],
  ['Sport', '⚽', ['football', 'world-cup', 'olympics', 'cricket', 'rugby', 'tennis-golf', 'motorsport', 'boxing-combat', 'horse-racing'], 12],
  ['History', '🏛️', ['british-history', 'tudors', 'world-wars', 'ancient-history', '20th-century', 'famous-people', 'days-that-shook-the-world'], 14],
  ['Science & Space', '🔬', ['space', 'science-technology', 'computers-internet', 'maths-numbers'], 14],
  ['Animals', '🐾', ['animals'], 6],
  ['Body & Nature', '🌿', ['human-body', 'nature-environment'], 9],
  ['Music', '🎵', ['pop-music', 'rock-music', 'the-beatles', 'number-ones', 'eurovision', 'music-lyrics', 'classical-music', 'one-hit-wonders', 'boy-bands-girl-groups'], 14],
  ['UK & Ireland', '🇬🇧', ['uk-geography', 'scotland', 'wales', 'ireland', 'london'], 11],
  ['The World', '🌍', ['world-geography', 'capital-cities', 'flags', 'europe', 'usa', 'australia', 'landmarks'], 12],
  ['Food & Drink', '🍔', ['food-drink', 'british-food', 'beer-wine-spirits'], 13],
  ['Brands & Cars', '🚗', ['brands-logos', 'cars-motoring', 'fashion'], 12],
  ['The 60s & 70s', '📻', ['the-1960s', 'the-1970s'], 8],
  ['The 80s & 90s', '📼', ['the-1980s', 'the-1990s'], 10],
  ['The 2000s & 2010s', '📱', ['the-2000s', 'the-2010s'], 10],
  ['Games & Toys', '🎮', ['games-toys', 'video-games'], 8],
  ['Fantasy & Franchises', '🧙', ['harry-potter', 'lord-of-the-rings', 'game-of-thrones', 'star-wars', 'marvel', 'dc-batman'], 8],
  ['Royals & Stars', '👑', ['royal-family', 'oscars', 'famous-firsts'], 6],
  ['QI & Oddities', '🤔', ['no-such-thing-as-a-fish', 'ripleys-believe-it-or-not', 'record-breakers', 'words-language', 'mythology'], 8],
  ['Books & Arts', '📚', ['books', 'art', 'shakespeare', 'theatre'], 6],
  ['North East', '📍', ['north-east-england', 'newcastle-v-sunderland', 'alan-shearer'], 6],
];
const use = Object.fromEntries(CATS.map((c) => [c[0], 0])), cap = Object.fromEntries(CATS.map((c) => [c[0], Math.ceil(c[3] * 1.7)]));
const shuffle = (a) => { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
const pad = (n) => String(n).padStart(2, '0');
// already built games count towards each category's use
const indexFile = path.join(OUT, 'index.json'); let index = fs.existsSync(indexFile) ? JSON.parse(fs.readFileSync(indexFile, 'utf8')) : { games: [] };
index.games = index.games.filter((g) => +g.id.slice(1) < FROM || fs.existsSync(path.join(GAMES, g.id + '.json')));
for (const g of index.games) for (const c of g.cats) if (use[c.n] !== undefined) use[c.n]++;

let tries = 0;
for (let i = FROM; i < FROM + N; i++) {
  if (++tries > N * 6) { console.log('too many retries, stopping'); break; }
  const id = 'g' + pad(i);
  const left = (c) => cap[c[0]] - use[c[0]];
  // the five categories furthest from their cap (a little random so no two games match); never the same one twice in a game
  const pick = shuffle(CATS.filter((c) => left(c) > 0)).sort((a, b) => (use[a[0]] / cap[a[0]]) - (use[b[0]] / cap[b[0]]) + (Math.random() - 0.5) * 0.18).slice(0, 5);
  const cfg = { title: 'Box Clever ' + pad(i), code: 'TVBOX', cols: 6, start: 1000, typed: 2, siblingDecoys: true, replay: false, bots: [], cats: pick.map((c) => ({ name: c[0], emoji: c[1], slugs: c[2] })) };
  const cfgFile = path.join(here, 'tvbox-config.tmp.json'); fs.writeFileSync(cfgFile, JSON.stringify(cfg));
  const r = spawnSync(process.execPath, [path.join(here, 'build-boxes.mjs'), '--warmup', '--custom', cfgFile, '--no-media', '--code', 'TVBOX', '--title', cfg.title, '--avoid-extra', GAMES], { cwd: here, encoding: 'utf8', timeout: 180000 });
  const out = (r.stdout || '') + (r.stderr || '');
  if (r.status !== 0 || /problems: (?!none)/.test(out)) { console.log(id, 'FAILED', out.split('\n').slice(-6).join(' | ')); i--; use[pick[0][0]]++; continue; }
  const quiz = JSON.parse(fs.readFileSync(path.join(here, 'boxes-custom-last.json'), 'utf8'));
  const box = quiz.questions.find((q) => q.type === 'boxes'), short = box.cats.filter((c) => c.qs.length < cfg.cols + 3);
  if (short.length) { console.log(id, 'short category', short.map((c) => c.name + ':' + c.qs.length).join(', '), '- retrying'); use[short[0].name] = cap[short[0].name]; i--; continue; }
  quiz.settings.warmup = { code: 'TVBOX', open: true, fun: true, replay: false, bots: 0 };
  fs.writeFileSync(path.join(GAMES, id + '.json'), JSON.stringify(quiz));
  for (const c of pick) use[c[0]]++;
  index.games = index.games.filter((g) => g.id !== id);
  index.games.push({ id, title: cfg.title, cats: box.cats.map((c) => ({ n: c.name, e: c.emoji })), file: 'tvbox/games/' + id + '.json' });
  index.games.sort((a, b) => a.id.localeCompare(b.id));
  fs.writeFileSync(indexFile, JSON.stringify(index));
  console.log(id, box.cats.map((c) => c.emoji + c.name + '(' + c.qs.length + ')').join(' · '), '· reserve', (box.reserve || []).length);
}
fs.rmSync(path.join(here, 'tvbox-config.tmp.json'), { force: true });
console.log('games:', index.games.length, '· category uses:', Object.entries(use).map(([k, v]) => k + ' ' + v).join(', '));
