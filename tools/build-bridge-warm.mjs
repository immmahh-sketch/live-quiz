// Builds the three 6 x 6 boards of the Bridge of Lies warm-up: node tools/build-bridge-warm.mjs [--seed 2026]
//   in:  tools/bridge-warm-src.json  [{ cat, correct: [...], wrong: [...] } x 3]
//   out: tools/bridge-warm-boards.json  [{ cat, n, m, tiles: [{ t, ok } | { pad }] } x 3]   (tile index = i * m + j; saved into the quiz row by tools/save-bridge-warm.mjs)
// A 6 x 6 lattice turned 45 degrees is a symmetric diamond: columns of 2,3,4,5,6,5,4,3,2 answers between the two pads, which sit level with each other.
// The route between the pads is 9 correct answers; 4 more correct tiles sit around it; every other tile (21) is a lie.
import fs from 'node:fs'; import path from 'node:path';
const root = path.resolve(path.dirname(new URL(import.meta.url).pathname.replace(/^\/(\w:)/, '$1')), '..');
const N = 6, M = 6, EXTRA = 4, SEED = +(process.argv[process.argv.indexOf('--seed') + 1]) || 2026;
const mulberry = (a) => () => { a |= 0; a = (a + 0x6d2b79f5) | 0; let t = Math.imul(a ^ (a >>> 15), 1 | a); t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296; };
const around = (i, j) => [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]].filter(([x, y]) => x >= 0 && x < N && y >= 0 && y < M);
function shortest(ok) {
  const key = (i, j) => i + ',' + j, dist = new Map([[key(0, 0), 0]]), q = [[0, 0]];
  while (q.length) { const [i, j] = q.shift(), d = dist.get(key(i, j)); if (i === N - 1 && j === M - 1) return d - 1; for (const [x, y] of around(i, j)) { const k = key(x, y); if (!dist.has(k) && (ok.has(k) || (x === N - 1 && y === M - 1))) { dist.set(k, d + 1); q.push([x, y]); } } }
  return Infinity;
}
function board(seed, good, bad) {
  const rnd = mulberry(seed), shuf = (a) => { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(rnd() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
  const steps = shuf([...Array(N - 1).fill('i'), ...Array(M - 1).fill('j')]); let i = 0, j = 0; const route = [];
  for (const s of steps.slice(0, -1)) { if (s === 'i') i++; else j++; route.push([i, j]); }
  const ok = new Set(route.map(([a, b]) => a + ',' + b)), isPad = (a, b) => (a === 0 && b === 0) || (a === N - 1 && b === M - 1);
  const free = []; for (let a = 0; a < N; a++) for (let b = 0; b < M; b++) if (!isPad(a, b) && !ok.has(a + ',' + b)) free.push([a, b]);
  const near = shuf(free.filter(([a, b]) => route.some(([x, y]) => Math.abs(x - a) + Math.abs(y - b) === 1))), far = shuf(free.filter((t) => !near.includes(t)));
  for (const [a, b] of [...near.slice(0, Math.ceil(EXTRA / 2)), ...far.slice(0, Math.floor(EXTRA / 2))]) ok.add(a + ',' + b);
  if (shortest(ok) !== N + M - 3) throw new Error('shortest route is ' + shortest(ok));
  const g = shuf(good), w = shuf(bad), tiles = []; let gi = 0, wi = 0;
  for (let a = 0; a < N; a++) for (let b = 0; b < M; b++) tiles.push(a === 0 && b === 0 ? { pad: 'start' } : a === N - 1 && b === M - 1 ? { pad: 'end' } : ok.has(a + ',' + b) ? { t: g[gi++], ok: 1 } : { t: w[wi++], ok: 0 });
  if (gi > good.length || wi > bad.length) throw new Error('not enough answers');
  return tiles;
}
const src = JSON.parse(fs.readFileSync(path.join(root, 'tools/bridge-warm-src.json'), 'utf8'));
const norm = (s) => String(s).toLowerCase().replace(/[^a-z0-9]+/g, ' ').trim();
const out = src.map((g, k) => {
  const all = [...g.correct, ...g.wrong]; if (new Set(all.map(norm)).size !== all.length) throw new Error(g.cat + ': a tile appears twice');
  for (const t of all) if (t.length > 22 || t.split(/\s+/).length > 4 || t.split(/\s+/).some((w) => w.length > 12)) throw new Error(g.cat + ': "' + t + '" will not fit a tile');
  return { cat: g.cat, n: N, m: M, tiles: board(SEED + k * 7919, g.correct, g.wrong) };
});
fs.writeFileSync(path.join(root, 'tools/bridge-warm-boards.json'), JSON.stringify(out));
const col = (b) => { const c = {}; b.tiles.forEach((t, k) => { const s = Math.floor(k / M) + (k % M); c[s] = (c[s] || 0) + 1; }); return Object.values(c).join(','); };
console.log(out.map((b) => `${b.cat}: columns ${col(b)}, ${b.tiles.filter((t) => t.ok).length} correct, ${b.tiles.filter((t) => t.ok === 0).length} lies`).join('\n'));
