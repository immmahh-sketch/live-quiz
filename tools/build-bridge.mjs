// Builds the 50 Bridge of Lies games (and the short test bridge) from the hand-written sources: node tools/build-bridge.mjs
//   in:  tools/bridge-src/part-*.json   (each an array of { cat, correct: [...], wrong: [...] })
//   out: bridge/games/gNN.json  { id, cat, n, m, tiles: [{ t, ok } | { pad: 'start' | 'end' }] }   tile index = i * m + j
//        bridge/index.json      { games: [{ id, cat }] }       tests/bridge.json (the test run: a short bridge, replayable)
// The board is a square lattice of n x m tiles turned 45 degrees, like the TV show's: it is a diamond, crossed from the left corner (the red START
// pad, tile 0,0) to the right corner (the green FINISH pad, tile n-1,m-1). A tile touches the four tiles next to it in the lattice. A hidden route of
// correct answers joins the two pads (n+m-3 tiles between them: 10 for the 6 x 7 board), so the shortest way across is exactly that many correct
// answers. A few more correct tiles sit around it; every other tile is a lie.
import fs from 'node:fs'; import path from 'node:path';
const root = path.resolve(path.dirname(new URL(import.meta.url).pathname.replace(/^\/(\w:)/, '$1')), '..');
const N = 6, M = 7, EXTRA = 4, GAMES = process.argv.includes('--partial') ? 40 : 50;
const mulberry = (a) => () => { a |= 0; a = (a + 0x6d2b79f5) | 0; let t = Math.imul(a ^ (a >>> 15), 1 | a); t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296; };
const around = (i, j, n, m) => [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]].filter(([x, y]) => x >= 0 && x < n && y >= 0 && y < m);
/** fewest correct tiles between the pads (BFS over correct tiles and the two pads) */
function shortest(ok, n, m) {
  const key = (i, j) => i + ',' + j, dist = new Map([[key(0, 0), 0]]), q = [[0, 0]];
  while (q.length) { const [i, j] = q.shift(), d = dist.get(key(i, j)); if (i === n - 1 && j === m - 1) return d - 1; for (const [x, y] of around(i, j, n, m)) { const k = key(x, y); if (!dist.has(k) && (ok.has(k) || (x === n - 1 && y === m - 1))) { dist.set(k, d + 1); q.push([x, y]); } } }
  return Infinity;
}
function board(seed, good, bad, n, m, extra) {
  const rnd = mulberry(seed), shuf = (a) => { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(rnd() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
  // the route: n-1 steps one way and m-1 the other, in a random order
  const steps = shuf([...Array(n - 1).fill('i'), ...Array(m - 1).fill('j')]); let i = 0, j = 0; const route = [];
  for (const s of steps.slice(0, -1)) { if (s === 'i') i++; else j++; route.push([i, j]); }
  const ok = new Set(route.map(([a, b]) => a + ',' + b)), isPad = (a, b) => (a === 0 && b === 0) || (a === n - 1 && b === m - 1);
  const free = []; for (let a = 0; a < n; a++) for (let b = 0; b < m; b++) if (!isPad(a, b) && !ok.has(a + ',' + b)) free.push([a, b]);
  const near = shuf(free.filter(([a, b]) => route.some(([x, y]) => Math.abs(x - a) + Math.abs(y - b) === 1))), far = shuf(free.filter((t) => !near.includes(t)));
  for (const [a, b] of [...near.slice(0, Math.ceil(extra / 2)), ...far.slice(0, Math.floor(extra / 2))]) ok.add(a + ',' + b);
  if (shortest(ok, n, m) !== n + m - 3) throw new Error('shortest route is ' + shortest(ok, n, m));
  const g = shuf(good), w = shuf(bad), tiles = []; let gi = 0, wi = 0;
  for (let a = 0; a < n; a++) for (let b = 0; b < m; b++) tiles.push(a === 0 && b === 0 ? { pad: 'start' } : a === n - 1 && b === m - 1 ? { pad: 'end' } : ok.has(a + ',' + b) ? { t: g[gi++], ok: 1 } : { t: w[wi++], ok: 0 });
  if (gi > good.length || wi > bad.length) throw new Error('not enough answers');
  return tiles;
}
const src = fs.readdirSync(path.join(root, 'tools/bridge-src')).filter((f) => /^part-\d+\.json$/.test(f)).sort().flatMap((f) => JSON.parse(fs.readFileSync(path.join(root, 'tools/bridge-src', f), 'utf8')));
if (src.length < GAMES) { console.error(`only ${src.length} source games, need ${GAMES}`); process.exit(1); }
fs.mkdirSync(path.join(root, 'bridge/games'), { recursive: true }); const index = [];
src.slice(0, GAMES).forEach((g, k) => {
  const id = 'g' + String(k + 1).padStart(2, '0');
  fs.writeFileSync(path.join(root, 'bridge/games', id + '.json'), JSON.stringify({ id, cat: g.cat, n: N, m: M, tiles: board(1000 + k * 7919, g.correct, g.wrong, N, M, EXTRA) })); index.push({ id, cat: g.cat });
});
fs.writeFileSync(path.join(root, 'bridge/index.json'), JSON.stringify({ games: index }));
// the test bridge: 3 x 5 (five correct answers across), a simple category, the same board every time
const fruit = { cat: 'Test bridge: fruit', correct: ['Apple', 'Banana', 'Orange', 'Pear', 'Grape', 'Mango', 'Plum'], wrong: ['Carrot', 'Potato', 'Onion', 'Leek', 'Cabbage', 'Turnip'] };
fs.mkdirSync(path.join(root, 'tests'), { recursive: true });
fs.writeFileSync(path.join(root, 'tests/bridge.json'), JSON.stringify({ id: 'test', cat: fruit.cat, n: 3, m: 5, tiles: board(7, fruit.correct, fruit.wrong, 3, 5, 2) }));
console.log(`built ${index.length} bridges and the test bridge`);
