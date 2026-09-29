// Builds the play-at-home game sets (home/sets/<game>-NN.json) from reviewed candidates, and writes the SQL that takes
// every question used out of the bank's stock, so a hosted quiz can never pick it.
//   node tools/home-build.mjs <dir> [first set number, default 1] [how many, default 10]
// <dir> holds pool.json (a fresh export: tools/home-pool.sql), cands-mc4.json (read by hand), cands-typed.json and
// cands-mc3.json with their review verdicts in review/result-*.jsonl, club-pick.json (the 1% Club ladder, picked and
// rated by hand), and optionally mc4-drop.json (ids dropped from the Millionaire candidates).
// Writes home/sets/*.json, home/sets/index.json and <dir>/reserve.sql. Run tools/home-check.mjs afterwards.
import fs from "node:fs";
import path from "node:path";
import { norm, giveaway, readJson, rowsOf, key, hostedKeys, ClashIndex } from "./home-lib.mjs";

const dir = process.argv[2];
const first = +(process.argv[3] || 1), count = +(process.argv[4] || 10);
if (!dir) { console.error("Usage: node tools/home-build.mjs <dir> [first] [count]"); process.exit(1); }
const out = new URL("../home/sets/", import.meta.url).pathname.replace(/^\/([A-Z]:)/, "$1");
fs.mkdirSync(out, { recursive: true });

// Per set: how many of each, by difficulty
const PLAN = {
  millionaire: { easy: 5, medium: 5, hard: 5 },
  chase: { typed: { easy: 30, medium: 70, hard: 25 }, mc: { easy: 14, medium: 26, hard: 8 } },
  weakest: { typed: { easy: 68, medium: 76, hard: 16 } },
};
const CLUB_LADDER = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 1];

let seed = 1002 + first; const rnd = () => ((seed = (seed * 1103515245 + 12345) & 0x7fffffff) / 0x7fffffff);
const shuffle = (a) => a.map((x) => [rnd(), x]).sort((p, q) => p[0] - q[0]).map((x) => x[1]);

// ------------------------------------------------------------ reviewed candidates
const verdict = new Map();
for (const f of fs.readdirSync(path.join(dir, "review")).filter((f) => /^result-\d+\.jsonl$/.test(f)))
  for (const line of fs.readFileSync(path.join(dir, "review", f), "utf8").split("\n")) if (line.trim()) { const v = JSON.parse(line); verdict.set(v.id, v); }
function reviewed(list, kind) {
  const keep = [];
  for (const c of list) {
    const v = verdict.get(c.id); if (!v || v.v !== "keep") continue;
    const it = { ...c, difficulty: ["easy", "medium", "hard"].includes(v.d) ? v.d : c.difficulty };
    if (v.fix && String(v.fix).trim().length > 15) it.text = String(v.fix).trim();
    if (kind === "typed") {
      it.answers = [...new Set([...(c.answers || []), ...(v.add || [])].map((a) => String(a).trim()).filter(Boolean))];
      if (giveaway(it.text, it.answers[0])) continue; // a rewording that gives it away
    } else {
      const right = c.options[c.correct], wrong = (v.keepWrong || []).filter((w) => c.options.includes(w) && w !== right).slice(0, 2);
      if (wrong.length !== 2) continue;
      it.options = [right, ...wrong]; it.correct = 0;
      if (giveaway(it.text, right)) continue;
    }
    keep.push(it);
  }
  return keep;
}
const typed = reviewed(readJson(path.join(dir, "cands-typed.json")), "typed");
const mc3 = reviewed(readJson(path.join(dir, "cands-mc3.json")), "mc3");
const mc4Drop = new Set(fs.existsSync(path.join(dir, "mc4-drop.json")) ? readJson(path.join(dir, "mc4-drop.json")) : []);
const mc4 = readJson(path.join(dir, "cands-mc4.json")).filter((c) => !mc4Drop.has(c.id));
// One more pass over everything at once: nothing that repeats a hosted quiz, a question already in a home set, or
// another candidate (the same fact asked both ways round slips past the word test used when picking).
const hosted = [...(fs.existsSync(path.join(dir, "history.json")) ? rowsOf(path.join(dir, "history.json")) : [])];
for (const f of fs.readdirSync(dir).filter((f) => /^backup-.*.json$/.test(f))) { const d = readJson(path.join(dir, f)); hosted.push(...(Array.isArray(d) ? d : d.quizzes || d.rows || [])); }
const seenIdx = new ClashIndex(false);
hostedKeys(hosted).forEach((k) => seenIdx.add(k));
for (const f of fs.readdirSync(out).filter((f) => /^[a-z]+-d+.json$/.test(f))) {
  const s = readJson(path.join(out, f)); if (s.set >= first && s.set <= first + count - 1) continue; // sets being rebuilt don't count
  for (const list of Object.values(s.lists || {})) for (const q of list) seenIdx.add(key(q.text, q.answers ? q.answers[0] : q.options[q.correct]));
}
const clubIds = new Set(Object.entries(readJson(path.join(dir, "club-pick.json"))).filter(([k]) => /^d+$/.test(k)).flatMap(([, v]) => v));
const pool0 = new Map(rowsOf(path.join(dir, "pool.json")).map((r) => [r.id, r]));
for (const id of clubIds) { const r = pool0.get(id); if (!r) continue; const k = key(String(r.q.text), String((r.q.answers || [])[0] || "")); const h = seenIdx.hit(k); if (h) console.warn(`1% Club ${id} ${h.why}: “${r.q.text}” / “${h.o.text}”`); seenIdx.add(k); }
let dropped = 0;
const unique = (list) => list.filter((q) => { const k = key(q.text, q.answers ? q.answers[0] : q.options[q.correct]); if (seenIdx.hit(k)) { dropped++; return false; } seenIdx.add(k); return true; });
for (const [name, list] of [["mc4", mc4], ["mc3", mc3], ["typed", typed]]) { const u = unique(list); list.length = 0; list.push(...u); }
console.log(`repeats taken out: ${dropped}`);
console.log(`reviewed: typed ${typed.length}, three-option ${mc3.length}, Millionaire ${mc4.length}`);

// ------------------------------------------------------------ dealing a set
/** Deals `plan` ({level: n}) from `pool` (removing what it takes): mixed categories, no repeated answer, and no
 *  question that names another's answer. */
function deal(pool, plan, taken) {
  const got = [];
  const ansOf = (q) => norm(q.answers ? q.answers[0] : q.options[q.correct]);
  const ok = (q) => {
    const a = ansOf(q), t = " " + norm(q.text) + " ";
    if (taken.answers.has(a)) return false;
    if (a.length >= 4 && [...taken.texts].some((x) => x.includes(" " + a + " "))) return false;
    if ([...taken.answers].some((x) => x.length >= 4 && t.includes(" " + x + " "))) return false;
    return true;
  };
  for (const [level, n] of Object.entries(plan)) {
    let need = n;
    for (let pass = 0; pass < 2 && need > 0; pass++) {
      const cap = pass === 0 ? 2 : 99; // at most two from one category per level, unless it runs short
      const perCat = new Map();
      for (const q of shuffle(pool.filter((x) => x.difficulty === level))) {
        if (need <= 0) break;
        if ((perCat.get(q.category) || 0) >= cap || !ok(q)) continue;
        perCat.set(q.category, (perCat.get(q.category) || 0) + 1);
        pool.splice(pool.indexOf(q), 1); got.push(q); need--;
        taken.answers.add(ansOf(q)); taken.texts.add(" " + norm(q.text) + " ");
      }
    }
    if (need > 0) {
      // short of this level: the nearest level makes up the rest (and says so)
      const alt = { easy: "medium", hard: "medium", medium: "easy" }[level];
      console.warn(`  short of ${level} questions: ${need} ${alt} instead`);
      for (const q of shuffle(pool.filter((x) => x.difficulty === alt))) { if (need <= 0) break; if (!ok(q)) continue; pool.splice(pool.indexOf(q), 1); got.push(q); need--; taken.answers.add(ansOf(q)); taken.texts.add(" " + norm(q.text) + " "); }
      if (need > 0) throw new Error(`Ran out of ${level} questions (${need} short)`);
    }
  }
  return got;
}
/** Spreads a list so the same category and difficulty do not bunch together. */
function spread(list) {
  const left = shuffle(list), outL = [];
  while (left.length) {
    const prev = outL[outL.length - 1], prev2 = outL[outL.length - 2];
    let i = left.findIndex((q) => !prev || (q.category !== prev.category && !(prev2 && q.difficulty === prev.difficulty && q.difficulty === prev2.difficulty)));
    if (i < 0) i = 0;
    outL.push(left.splice(i, 1)[0]);
  }
  return outL;
}
const clean = (q, extra = {}) => { const o = { id: q.id, text: q.text, category: q.category, difficulty: q.difficulty, ...extra }; if (q.answers) o.answers = q.answers; if (q.options) { const idx = shuffle(q.options.map((_, i) => i)); o.options = idx.map((i) => q.options[i]); o.correct = idx.indexOf(q.correct); } if (q.wow) o.wow = true; return o; };

const reserve = []; // [label, id]
const write = (game, n, lists) => {
  const f = `${game}-${String(n).padStart(2, "0")}.json`;
  fs.writeFileSync(path.join(out, f), JSON.stringify({ game, set: n, made: new Date().toISOString().slice(0, 10), lists }, null, 1) + "\n");
  for (const list of Object.values(lists)) for (const q of list) reserve.push([`${game}-${String(n).padStart(2, "0")}`, q.id, q.pct]);
};

const last = first + count - 1;
for (let n = first; n <= last; n++) {
  // Millionaire: five of each level, easiest first
  const t1 = { answers: new Set(), texts: new Set() };
  const m = deal(mc4, PLAN.millionaire, t1);
  const byLevel = (lv) => spread(m.filter((q) => q.difficulty === lv));
  write("millionaire", n, { questions: [...byLevel("easy"), ...byLevel("medium"), ...byLevel("hard")].map((q) => clean(q)) });
  // The Chase: a stream of typed quick-fire questions and a stream of three-option head-to-head ones
  const t2 = { answers: new Set(), texts: new Set() };
  write("chase", n, { typed: spread(deal(typed, PLAN.chase.typed, t2)).map((q) => clean(q)), mc: spread(deal(mc3, PLAN.chase.mc, t2)).map((q) => clean(q)) });
  // The Weakest Link: one long typed stream, easier on the whole
  const t3 = { answers: new Set(), texts: new Set() };
  write("weakest", n, { typed: spread(deal(typed, PLAN.weakest.typed, t3)).map((q) => clean(q)) });
}

// The 1% Club: the ladder picked and rated by hand, one question per rung in each set
const pick = readJson(path.join(dir, "club-pick.json"));
const poolRows = new Map(rowsOf(path.join(dir, "pool.json")).map((r) => [r.id, r]));
const rungs = CLUB_LADDER.map((pct) => pick[String(pct)] || []); // in set order, as picked
for (let n = first; n <= last; n++) {
  const qs = CLUB_LADDER.map((pct, i) => {
    const id = rungs[i][n - first]; if (!id) throw new Error(`No ${pct}% question for set ${n}`);
    const r = poolRows.get(id); if (!r) throw new Error(`${id} is not in the pool (used, flagged or missing)`);
    const answers = [...new Set([...(r.q.answers || []), ...((pick.addAnswers || {})[id] || [])])];
    return { id, pct, text: String(r.q.text).trim(), answers, why: (pick.fixWhy || {})[id] || r.q.why || "", category: r.q.category || "" };
  });
  write("club", n, { questions: qs });
}

// index of what exists
const idx = {};
for (const f of fs.readdirSync(out).filter((f) => /^[a-z]+-\d+\.json$/.test(f))) { const g = f.replace(/-\d+\.json$/, ""); idx[g] = { sets: Math.max((idx[g] || {}).sets || 0, +f.match(/-(\d+)\.json$/)[1]) }; }
idx.updated = new Date().toISOString().slice(0, 10);
fs.writeFileSync(path.join(out, "index.json"), JSON.stringify(idx, null, 1) + "\n");

// the SQL that takes them out of stock: used = true, and q.used says which home game has it
const byLabel = new Map();
for (const [label, id, pct] of reserve) { if (!byLabel.has(label)) byLabel.set(label, []); byLabel.get(label).push([id, pct]); }
let sql = "-- Takes the play-at-home questions out of the bank's stock (tools/home-build.mjs).\n";
for (const [label, rows] of byLabel) {
  sql += `update quiz_bank set used = true, updated_at = now(), q = jsonb_set(q, '{used}', jsonb_build_object('home', '${label}', 'at', now()::text)) where id = any(array[${rows.map(([id]) => `'${id}'`).join(",")}]);\n`;
  for (const [id, pct] of rows) if (pct) sql += `update quiz_bank set q = jsonb_set(q, '{pct}', '${pct}'::jsonb) where id = '${id}';\n`;
}
for (const id of pick.retire || []) sql += `update quiz_bank set used = true, updated_at = now(), q = jsonb_set(q, '{used}', jsonb_build_object('rejected', true, 'note', 'duplicate of a play-at-home question', 'at', now()::text)) where id = '${id}';\n`;
fs.writeFileSync(path.join(dir, "reserve.sql"), sql);
console.log(`wrote sets ${first}-${last}: ${reserve.length} questions; left over: typed ${typed.length}, three-option ${mc3.length}, Millionaire ${mc4.length}`);
console.log(`reserve SQL: ${path.join(dir, "reserve.sql")}`);
