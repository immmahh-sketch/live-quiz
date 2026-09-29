// Builds the Millionaire sets as a proper ladder: like the show, the first questions are nursery-easy and each rung
// is a little harder, up to a genuinely hard £1,000,000 question.
//   node tools/home-mil-ladder.mjs <dir> [first=1] [count=10]
// <dir>/mil-scores.json: [{ id, score }] with every candidate rated by hand 1–10 (1 = "What kind of animal is Peppa?",
// 9 = "Which Delibes opera has the Flower Duet?"). Question content comes from <dir>/pool.json, cands-mc4.json and
// mil-easy.json (the bank's "too easy" and easy multiple choice, which the hosted builder never uses for the first).
// Writes home/sets/millionaire-NN.json and <dir>/mil-reserve.sql: it reserves what the sets now use and puts back into
// stock anything a Millionaire set used before and no longer does. Run tools/home-check.mjs afterwards.
import fs from "node:fs";
import path from "node:path";
import { norm, giveaway, readJson, rowsOf, key, hostedKeys, ClashIndex } from "./home-lib.mjs";

const dir = process.argv[2], first = +(process.argv[3] || 1), count = +(process.argv[4] || 10);
if (!dir) { console.error("Usage: node tools/home-mil-ladder.mjs <dir> [first] [count]"); process.exit(1); }
const out = new URL("../home/sets/", import.meta.url).pathname.replace(/^\/([A-Z]:)/, "$1");
// the rating wanted on each rung, £100 up to £1,000,000
const LADDER = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 7, 8, 9];
const level = (s) => (s <= 3 ? "easy" : s <= 6 ? "medium" : "hard");

let seed = 1515 + first; const rnd = () => ((seed = (seed * 1103515245 + 12345) & 0x7fffffff) / 0x7fffffff);
const shuffle = (a) => a.map((x) => [rnd(), x]).sort((p, q) => p[0] - q[0]).map((x) => x[1]);

// question content, by id, as { text, options, correct, category }
const content = new Map();
const fromBank = (r) => { const o = r.q.options || []; return { text: String(r.q.text).trim(), options: o.map((x) => String(x.text)), correct: o.findIndex((x) => x.id === r.q.correct), category: r.q.category || r.category || "" }; };
for (const f of ["pool.json", "mil-easy.json"]) if (fs.existsSync(path.join(dir, f))) for (const r of rowsOf(path.join(dir, f))) if (r.q?.options) content.set(r.id, fromBank(r));
for (const c of readJson(path.join(dir, "cands-mc4.json"))) content.set(c.id, { text: c.text, options: c.options, correct: c.correct, category: c.category });

// nothing that repeats a hosted quiz or another home game (the other Millionaire sets are being rebuilt, so they don't count)
const seen = new ClashIndex(false);
const hosted = fs.existsSync(path.join(dir, "history.json")) ? rowsOf(path.join(dir, "history.json")) : [];
for (const f of fs.readdirSync(dir).filter((f) => /^backup-.*\.json$/.test(f))) { const d = readJson(path.join(dir, f)); hosted.push(...(Array.isArray(d) ? d : d.quizzes || d.rows || [])); }
hostedKeys(hosted).forEach((k) => seen.add(k));
for (const f of fs.readdirSync(out).filter((f) => /^[a-z]+-\d+\.json$/.test(f) && !f.startsWith("millionaire-"))) for (const l of Object.values(readJson(path.join(out, f)).lists)) for (const q of l) seen.add(key(q.text, q.answers ? q.answers[0] : q.options[q.correct]));
let clashing = 0;
const scores = readJson(path.join(dir, "mil-scores.json")).filter((s) => { if (!content.has(s.id)) return false; const c = content.get(s.id); const k = key(c.text, c.options[c.correct]); if (seen.hit(k)) { clashing++; return false; } seen.add(k); return true; });
console.log(`left out ${clashing} that repeat a hosted quiz, another home game or each other`);
const pool = shuffle(scores.map((s) => ({ ...s, ...content.get(s.id) })));
const byScore = (t) => pool.filter((q) => q.score === t && !q.taken);

const sets = Array.from({ length: count }, () => ({ qs: new Array(15), answers: new Set(), texts: [], cats: new Map() }));
const fits = (set, q) => {
  const a = norm(q.options[q.correct]), t = " " + norm(q.text) + " ";
  if (set.answers.has(a) || giveaway(q.text, q.options[q.correct])) return false;
  if (a.length >= 4 && set.texts.some((x) => x.includes(" " + a + " "))) return false;
  if ([...set.answers].some((x) => x.length >= 4 && t.includes(" " + x + " "))) return false;
  return (set.cats.get(q.category) || 0) < 1;
};
// hardest rungs first, so the scarce hard questions spread one per set; each rung goes round every set in turn
const rungs = LADDER.map((t, i) => ({ t, i })).sort((a, b) => b.t - a.t || b.i - a.i);
for (const { t, i } of rungs) for (const set of sets) {
  let q = null;
  for (const want of [t, t - 1, t + 1, t - 2]) { q = byScore(want).find((x) => fits(set, x)) || null; if (q) break; }
  if (!q) q = pool.find((x) => !x.taken && Math.abs(x.score - t) <= 2);
  if (!q) throw new Error(`Nothing for rung ${i + 1} (rating ${t})`);
  q.taken = true; set.qs[i] = q; set.answers.add(norm(q.options[q.correct])); set.texts.push(" " + norm(q.text) + " "); set.cats.set(q.category, (set.cats.get(q.category) || 0) + 1);
}

const before = new Set(), now = new Set();
for (const f of fs.readdirSync(out).filter((f) => /^millionaire-\d+\.json$/.test(f))) for (const q of readJson(path.join(out, f)).lists.questions) before.add(q.id);
let sql = "-- Millionaire ladders (tools/home-mil-ladder.mjs): reserve what the sets use now, release what they no longer use.\n";
sets.forEach((set, k) => {
  const n = first + k, label = `millionaire-${String(n).padStart(2, "0")}`;
  // the rungs must climb: sort each set by rating, keeping the order the dealing chose within a rating
  const qs = set.qs.slice().sort((a, b) => a.score - b.score).map((q) => {
    const idx = shuffle(q.options.map((_, i) => i));
    return { id: q.id, text: q.text, options: idx.map((i) => q.options[i]), correct: idx.indexOf(q.correct), category: q.category, difficulty: level(q.score), rating: q.score };
  });
  fs.writeFileSync(path.join(out, `${label}.json`), JSON.stringify({ game: "millionaire", set: n, made: new Date().toISOString().slice(0, 10), lists: { questions: qs } }, null, 1) + "\n");
  qs.forEach((q) => now.add(q.id));
  sql += `update quiz_bank set used = true, q = jsonb_set(q, '{used}', jsonb_build_object('home', '${label}', 'at', now()::text)) where id = any(array[${qs.map((q) => `'${q.id}'`).join(",")}]);\n`;
  console.log(`${label}: ${qs.map((q) => q.rating).join(" ")}`);
});
// Back into stock: whatever the database has reserved for these sets that they no longer use (worked out from the
// database, not the old files, so a re-run can't miss anything)
const labels = sets.map((_, k) => `'millionaire-${String(first + k).padStart(2, "0")}'`).join(",");
sql += `update quiz_bank set used = false, q = q - 'used' where q->'used'->>'home' in (${labels}) and not (id = any(array[${[...now].map((id) => `'${id}'`).join(",")}]));\n`;
fs.writeFileSync(path.join(dir, "mil-reserve.sql"), sql);
console.log(`${now.size} questions in the ladders (${[...now].filter((id) => !before.has(id)).length} new to them). SQL: ${path.join(dir, "mil-reserve.sql")}`);
