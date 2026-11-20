// Builds the three 6 x 6 boards of the Bridge of Lies warm-up: node tools/build-bridge-warm.mjs [--seed 2026]
//   in:  tools/bridge-warm-src.json  [{ cat, correct: [...], wrong: [...] } x 3]
//   out: tools/bridge-warm-boards.json  [{ cat, n, m, tiles: [{ t, ok } | { pad }] } x 3]   (tile index = i * m + j; saved into the quiz row by tools/save-bridge-warm.mjs)
// A 6 x 6 lattice turned 45 degrees is a symmetric diamond: columns of 2,3,4,5,6,5,4,3,2 answers between the two pads, which sit level with each other.
// The true route between the pads is a long winding path (no two of its tiles touch except in sequence, so there are no short cuts), found by a random search.
// Then dead ends are added: extra correct tiles hanging off the route (each touching only one other correct tile, and never the finish pad), whose neighbours are all lies.
// Every other tile is a lie. Dead ends score 100 like any correct answer but lead nowhere.
import fs from 'node:fs'; import path from 'node:path';
const root = path.resolve(path.dirname(new URL(import.meta.url).pathname.replace(/^\/(\w:)/, '$1')), '..');
const N = 6, M = 6, MIN_PATH = 13, MAX_PATH = 16, TARGET_CORRECT = 22, SEED = +(process.argv[process.argv.indexOf('--seed') + 1]) || 2026;
const mulberry = (a) => () => { a |= 0; a = (a + 0x6d2b79f5) | 0; let t = Math.imul(a ^ (a >>> 15), 1 | a); t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296; };
const nb = (i, j) => [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]].filter(([x, y]) => x >= 0 && x < N && y >= 0 && y < M);
const K = (i, j) => i * M + j;
/** fewest correct tiles between the pads (BFS over correct tiles and the two pads) */
function shortest(ok) {
  const dist = new Map([[0, 0]]), q = [[0, 0]];
  while (q.length) { const [i, j] = q.shift(), d = dist.get(K(i, j)); if (i === N - 1 && j === M - 1) return d - 1; for (const [x, y] of nb(i, j)) { const k = K(x, y); if (!dist.has(k) && (ok.has(k) || k === K(N - 1, M - 1))) { dist.set(k, d + 1); q.push([x, y]); } } }
  return Infinity;
}
/** a winding chordless path from the start pad to the finish pad: between MIN_PATH and MAX_PATH tiles between the pads, wandering at least 3 rows off the middle diagonal; found by random walks */
function winding(rnd) {
  for (let tries = 0; tries < 20000; tries++) {
    const path = [[0, 0]], on = new Set([0]); let steps = 0, found = false;
    const dfs = () => {
      if (++steps > 3000) return false;
      const [ci, cj] = path[path.length - 1];
      if (ci === N - 1 && cj === M - 1) { const between = path.length - 2, off = Math.max(...path.map(([a, b]) => Math.abs(a - b))); return between >= MIN_PATH && between <= MAX_PATH && off >= 3; }
      if (path.length - 1 > MAX_PATH + 1) return false;
      const opts = nb(ci, cj).filter(([x, y]) => !on.has(K(x, y)) && nb(x, y).filter(([a, b]) => on.has(K(a, b))).length === 1).sort(() => rnd() - 0.5); // touches only the tile it comes from
      for (const [x, y] of opts) { path.push([x, y]); on.add(K(x, y)); if (dfs()) return true; path.pop(); on.delete(K(x, y)); }
      return false;
    };
    if (dfs()) return path.slice();
  }
  throw new Error('no winding path found');
}
function board(seed, good, bad) {
  const rnd = mulberry(seed), shuf = (a) => { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(rnd() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
  const route = winding(rnd).slice(1, -1), ok = new Set(route.map(([a, b]) => K(a, b))), routeLen = route.length;
  // dead ends: grow correct tiles off the route (each touches exactly one correct tile or pad, and never the finish pad) until there are TARGET_CORRECT
  const fin = K(N - 1, M - 1), isCorrectish = (k) => ok.has(k) || k === 0 || k === fin;
  const spur = new Set();
  for (let guard = 0; guard < 400 && ok.size < TARGET_CORRECT; guard++) {
    const cand = [];
    for (let a = 0; a < N; a++) for (let b = 0; b < M; b++) { const k = K(a, b); if (k === 0 || k === fin || ok.has(k)) continue; const ns = nb(a, b).map(([x, y]) => K(x, y)); if (ns.includes(fin)) continue; if (ns.filter(isCorrectish).length === 1) cand.push(k); }
    if (!cand.length) break;
    const k = shuf(cand)[0]; ok.add(k); spur.add(k);
    if (shortest(ok) !== routeLen) { ok.delete(k); spur.delete(k); } // never a short cut
  }
  if (shortest(ok) !== routeLen) throw new Error('shortest route is ' + shortest(ok));
  const g = shuf(good), w = shuf(bad), tiles = []; let gi = 0, wi = 0;
  for (let a = 0; a < N; a++) for (let b = 0; b < M; b++) { const k = K(a, b); tiles.push(k === 0 ? { pad: 'start' } : k === fin ? { pad: 'end' } : ok.has(k) ? { t: g[gi++], ok: 1 } : { t: w[wi++], ok: 0 }); }
  if (gi > good.length || wi > bad.length) throw new Error('not enough answers: need ' + gi + ' correct and ' + wi + ' wrong');
  return { tiles, routeLen, spurs: spur.size };
}
const src = JSON.parse(fs.readFileSync(path.join(root, 'tools/bridge-warm-src.json'), 'utf8'));
const norm = (s) => String(s).toLowerCase().replace(/[^a-z0-9]+/g, ' ').trim();
const out = [], info = [];
src.forEach((g, k) => {
  const all = [...g.correct, ...g.wrong]; if (new Set(all.map(norm)).size !== all.length) throw new Error(g.cat + ': a tile appears twice');
  for (const t of all) if (t.length > 22 || t.split(/\s+/).length > 4 || t.split(/\s+/).some((w) => w.length > 12)) throw new Error(g.cat + ': "' + t + '" will not fit a tile');
  const b = board(SEED + k * 7919, g.correct, g.wrong);
  out.push({ cat: g.cat, ...(g.hint ? { hint: g.hint } : {}), n: N, m: M, tiles: b.tiles }); info.push(`${g.cat}: route ${b.routeLen} tiles, ${b.spurs} dead-end tiles, ${b.tiles.filter((t) => t.ok).length} correct, ${b.tiles.filter((t) => t.ok === 0).length} lies`);
});
fs.writeFileSync(path.join(root, 'tools/bridge-warm-boards.json'), JSON.stringify(out));
console.log(info.join('\n'));
// a picture of each board (O = route or dead-end tile that is correct, . = lie, S/F pads), one row per lattice row
out.forEach((b) => { console.log('\n' + b.cat); for (let i = 0; i < N; i++) console.log(Array.from({ length: M }, (_, j) => { const t = b.tiles[K(i, j)]; return t.pad ? (t.pad === 'start' ? 'S' : 'F') : t.ok ? 'O' : '.'; }).join(' ')); });
