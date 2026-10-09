// Checks a 20 Questions bank file before import: every Yes is a real question in that kind's branch, its gates
// (needs / any) are met, the answer isn't already in bank/twenty.json, and no two answers (old or new) share the
// exact same set of Yes answers, which would make them impossible to tell apart.
//   node tools/twenty-check.mjs bank/twenty-2.json
import fs from 'node:fs';
import { LQ } from './lq.mjs';
const file = process.argv[2];
if (!file) { console.error('usage: node tools/twenty-check.mjs <file>'); process.exit(1); }
const read = (f) => JSON.parse(fs.readFileSync(f, 'utf8'));
const yesOf = (x) => (x.yes || Object.entries(x.facts || {}).filter(([, v]) => v).map(([k]) => k)).slice().sort();
const norm = (s) => String(s).toLowerCase().replace(/[^a-z0-9]/g, '');
const mine = read(file), others = fs.readdirSync('bank').filter((f) => /^twenty.*\.json$/.test(f) && 'bank/' + f !== file.replace(/\\/g, '/')).flatMap((f) => read('bank/' + f));
const seen = new Map(others.map((x) => [x.what + ':' + yesOf(x).join(','), x.answers[0]]));
const names = new Set(others.flatMap((x) => x.answers.map(norm)));
let bad = 0;
for (const x of mine) {
  const ids = new Set(LQ.twentyBranch(x.what).map((q) => q.id)), yes = new Set(yesOf(x)), probs = [];
  if (!ids.size) probs.push('unknown kind ' + x.what);
  for (const id of yes) {
    const q = LQ.TWENTY_QS.find((q) => q.id === id && q.cat === x.what);
    if (!q) { probs.push('not a ' + x.what + ' question: ' + id); continue; }
    const miss = q.needs.filter((n) => !yes.has(n)); if (miss.length) probs.push(id + ' needs ' + miss.join('+'));
    if (q.any.length && !q.any.some((n) => yes.has(n))) probs.push(id + ' needs one of ' + q.any.join('/'));
  }
  if (x.answers.some((a) => names.has(norm(a)))) probs.push('already in the bank');
  const key = x.what + ':' + [...yes].sort().join(',');
  if (seen.has(key)) probs.push('same answers as ' + seen.get(key));
  seen.set(key, x.answers[0]);
  if (probs.length) { bad++; console.log(x.answers[0] + ': ' + probs.join('; ')); }
}
console.log(mine.length + ' checked, ' + bad + ' with problems');
