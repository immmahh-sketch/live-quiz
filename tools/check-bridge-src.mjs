// Checks the hand-written Bridge of Lies source files: node tools/check-bridge-src.mjs tools/bridge-src/part-1.json [more files]
// Each file is a JSON array of { cat, correct: [..], wrong: [..] }.
import fs from 'node:fs';
const files = process.argv.slice(2); if (!files.length) { console.error('give one or more files'); process.exit(2); }
const norm = (s) => String(s).toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/&/g, ' and ').replace(/[^a-z0-9]+/g, ' ').trim();
let bad = 0, games = 0; const cats = new Map(); const say = (m) => { console.log('✗ ' + m); bad++; };
for (const f of files) {
  let a; try { a = JSON.parse(fs.readFileSync(f, 'utf8')); } catch (e) { say(f + ': not valid JSON: ' + e.message); continue; }
  if (!Array.isArray(a)) { say(f + ': must be an array'); continue; }
  a.forEach((g, i) => {
    const at = `${f} #${i + 1} "${g?.cat}"`; games++;
    if (!g || typeof g.cat !== 'string' || g.cat.length < 8 || g.cat.length > 70) return say(at + ': cat missing or too short/long (8-70 chars)');
    const ck = norm(g.cat); if (cats.has(ck)) say(at + ': duplicate category (also ' + cats.get(ck) + ')'); cats.set(ck, at);
    if (!Array.isArray(g.correct) || g.correct.length < 16 || g.correct.length > 22) say(at + `: needs 16-22 correct answers, has ${g.correct?.length}`);
    if (!Array.isArray(g.wrong) || g.wrong.length < 34 || g.wrong.length > 50) say(at + `: needs 34-50 wrong answers, has ${g.wrong?.length}`);
    const all = new Map();
    for (const [kind, list] of [['correct', g.correct || []], ['wrong', g.wrong || []]]) for (const t of list) {
      if (typeof t !== 'string' || !t.trim()) { say(at + ': empty ' + kind); continue; }
      if (t.length > 22) say(at + `: "${t}" is longer than 22 characters`);
      if (t.trim().split(/\s+/).length > 4) say(at + `: "${t}" has more than 4 words`);
      if (t.split(/\s+/).some((w) => w.length > 12)) say(at + `: "${t}" has a word longer than 12 letters`);
      const k = norm(t); if (all.has(k)) say(at + `: "${t}" appears twice (${all.get(k)} and ${kind})`); all.set(k, kind);
    }
  });
}
console.log(bad ? `\n${bad} problem(s) in ${games} game(s)` : `OK: ${games} game(s), ${cats.size} categories`);
process.exit(bad ? 1 : 0);
