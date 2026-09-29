// Checks the play-at-home sets (home/sets): every set has the right shape, no question turns up twice anywhere in
// them (the same id, the same question, or the same answer to a question about the same thing), and none of them is
// in a hosted quiz.
//   node tools/home-check.mjs [dir]
// [dir] (optional) holds history.json (tools/home-history.sql) and any backup-*.json of hosted quizzes to check against.
import fs from "node:fs";
import path from "node:path";
import { clash, key, hostedKeys, giveaway, norm, readJson, rowsOf } from "./home-lib.mjs";

const setsDir = new URL("../home/sets/", import.meta.url).pathname.replace(/^\/([A-Z]:)/, "$1");
const dir = process.argv[2];
const SHAPE = { millionaire: { questions: 15 }, chase: { typed: 100, mc: 40 }, weakest: { typed: 140 }, club: { questions: 11 } };
const problems = [], items = [];
const say = (s) => problems.push(s);

const files = fs.readdirSync(setsDir).filter((f) => /^[a-z]+-\d+\.json$/.test(f)).sort();
const index = readJson(path.join(setsDir, "index.json"));
for (const f of files) {
  const s = readJson(path.join(setsDir, f)), label = f.replace(/\.json$/, "");
  const want = SHAPE[s.game]; if (!want) { say(`${label}: unknown game ${s.game}`); continue; }
  if (!(index[s.game]?.sets >= s.set)) say(`${label}: not counted in index.json`);
  for (const [list, min] of Object.entries(want)) {
    const qs = s.lists?.[list] || [];
    if (qs.length < min) say(`${label}: ${list} has ${qs.length}, needs at least ${min}`);
    qs.forEach((q, i) => {
      const where = `${label} ${list}[${i}] ${q.id}`;
      if (!q.id || !q.text) say(`${where}: missing id or text`);
      if (q.options) {
        if (!Number.isInteger(q.correct) || !q.options[q.correct]) say(`${where}: bad correct index`);
        if (new Set(q.options.map(norm)).size !== q.options.length) say(`${where}: repeated option`);
        if (s.game === "millionaire" && q.options.length !== 4) say(`${where}: needs 4 options`);
        if (s.game === "chase" && q.options.length !== 3) say(`${where}: needs 3 options`);
      } else if (!Array.isArray(q.answers) || !q.answers.length) say(`${where}: no accepted answers`);
      if (s.game === "club" && !(q.pct > 0)) say(`${where}: no percentage`);
      const ans = q.answers ? q.answers[0] : q.options?.[q.correct];
      if (s.game !== "club" && giveaway(q.text, ans)) say(`${where}: the answer is in the question`);
      items.push(key(q.text, String(ans || ""), { id: q.id, where }));
    });
  }
  if (s.game === "club") { const p = s.lists.questions.map((q) => q.pct); if (p.some((x, i) => i && x > p[i - 1])) say(`${label}: the ladder is not in order`); }
}

// the same id or the same question twice, anywhere in the home sets
const seen = new Map();
for (const it of items) { if (seen.has(it.id)) say(`${it.id} is in both ${seen.get(it.id)} and ${it.where}`); else seen.set(it.id, it.where); }
const byWord = new Map();
let dupes = 0, similar = 0, similarHosted = 0;
for (const it of items) {
  const cands = new Set();
  for (const w of [...it.words, "=" + it.ans]) for (const o of byWord.get(w) || []) cands.add(o);
  for (const o of cands) { const why = clash(it, o, false); if (clash(it, o)) similar++; if (why) { dupes++; say(`${why}: ${o.where} “${o.text}” / ${it.where} “${it.text}”`); } }
  for (const w of [...it.words, "=" + it.ans]) { if (!byWord.has(w)) byWord.set(w, []); byWord.get(w).push(it); }
}

// nothing shared with a hosted quiz
let hostedN = 0;
if (dir) {
  const hosted = [];
  if (fs.existsSync(path.join(dir, "history.json"))) hosted.push(...rowsOf(path.join(dir, "history.json")));
  for (const f of fs.readdirSync(dir).filter((f) => /^backup-.*\.json$/.test(f))) { const d = readJson(path.join(dir, f)); hosted.push(...(Array.isArray(d) ? d : d.quizzes || d.rows || [])); }
  const hk = hostedKeys(hosted); hostedN = hk.length;
  for (const h of hk) {
    const cands = new Set(); for (const w of [...h.words, "=" + h.ans]) for (const o of byWord.get(w) || []) cands.add(o);
    for (const o of cands) { const why = clash(h, o, false); if (clash(h, o)) similarHosted++; if (why) say(`${why} as hosted quiz “${h.from}”: ${o.where} “${o.text}” / “${h.text}”`); }
  }
}
console.log(`Alike but not the same (same kind of question, different answer): ${similar} within the sets, ${similarHosted} with hosted quizzes.`);
console.log(`${files.length} sets, ${items.length} questions${dir ? `, checked against ${hostedN} hosted items` : ""}.`);
if (problems.length) { console.log(`${problems.length} problem(s):`); for (const p of problems.slice(0, 200)) console.log(" - " + p); process.exit(1); }
console.log("All clear: every set is complete, nothing repeats, nothing is shared with a hosted quiz.");
