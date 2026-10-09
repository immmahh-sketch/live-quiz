// Simulates quiz-api's nearDuplicate() for a bank file against a JSON dump of live rows, so clashes can be fixed
// before importing (the server skips them silently). The dump is the -o json output of a query returning t (text) and
// a (first answer) for the type, e.g. select q->>'text' t, q->>'answer' a from quiz_bank where type='nearest';
//   node tools/near-dup-sim.mjs bank/nearest-4.json C:/Users/GM/Documents/lqsql/near-all2.json
// Items are read with their text and first answer (answer, or answers[0]). Survey, twenty, unique, dingbat and the
// list types (order/sort/match/wipeout/race) use different rules on the server and aren't covered here.
import fs from 'node:fs';
const [file, dump] = process.argv.slice(2);
const norm = (s) => String(s || '').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/&/g, ' and ').replace(/[^a-z0-9]+/g, ' ').trim().replace(/^(the|a|an) /, '');
const STOP = new Set(['which', 'what', 'who', 'where', 'when', 'this', 'that', 'these', 'those', 'from', 'with', 'does', 'were', 'was', 'the', 'and', 'for', 'has', 'have', 'had', 'his', 'her', 'their', 'its', 'into', 'name', 'called', 'many', 'much', 'following']);
const tok = (s) => new Set(norm(s).split(' ').filter((w) => w.length >= 3 && !STOP.has(w)));
const live = JSON.parse(fs.readFileSync(dump, 'utf8').replace(/^[^{]*/, '')).rows.map((r) => ({ t: r.t, a: Array.isArray(r.a) ? r.a[0] : r.a }));
const mine = JSON.parse(fs.readFileSync(file, 'utf8'));
const ans = (x) => String(x.answer ?? (x.answers || [])[0] ?? '');
let n = 0;
for (const x of mine) {
  const tb = tok(x.text), hits = [];
  for (const r of live) {
    if (norm(r.t) === norm(x.text)) { hits.push(`same text`); continue; }
    const ta = tok(r.t); if (!ta.size || !tb.size) continue;
    let sh = 0; for (const w of ta) if (tb.has(w)) sh++;
    const ov = sh / Math.min(ta.size, tb.size), same = ta.size >= 3 && tb.size >= 3 && norm(r.a) === norm(ans(x)) && norm(ans(x)).length > 1;
    if (ov >= 0.8 || (same && ov >= 0.5)) hits.push(`${r.t} (${ov.toFixed(2)}${same ? ', same answer' : ''})`);
  }
  if (hits.length) { n++; console.log(x.text + '\n   ~ ' + hits.slice(0, 3).join('\n   ~ ')); }
}
console.log(`${mine.length} checked, ${n} would be skipped`);
