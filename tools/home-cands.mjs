// Picks candidate questions for the play-at-home games from an export of the bank, for review before any set is built.
//   node tools/home-cands.mjs <dir>
// <dir> holds pool.json (unused, unflagged choice/text/club rows: tools/home-pool.sql) and history.json (every hosted
// quiz: tools/home-history.sql), plus any extra hosted quizzes as backup-*.json. Writes <dir>/cands-<kind>.json.
// Kinds: mc4 (Millionaire), mc3 (Chase head-to-head), typed (Chase and Weakest Link quick-fire), club (The 1% Club).
// Nothing already in a home set (home/sets) or any hosted quiz is picked, and no two candidates are the same question.
import fs from "node:fs";
import path from "node:path";
import { NICHE, LOCAL, answerOf, wrongOf, clash, key, hostedKeys, typeable, giveaway, aliases, readJson, rowsOf } from "./home-lib.mjs";

const dir = process.argv[2];
if (!dir) { console.error("Usage: node tools/home-cands.mjs <dir>"); process.exit(1); }
const want = JSON.parse(process.env.WANT || '{"mc4":{"easy":65,"medium":65,"hard":65},"typed":{"easy":1030,"medium":1900,"hard":700},"mc3":{"easy":60,"medium":360,"hard":180}}');

const pool = rowsOf(path.join(dir, "pool.json"));
const hosted = [...rowsOf(path.join(dir, "history.json"))];
for (const f of fs.readdirSync(dir).filter((f) => /^backup-.*\.json$/.test(f))) { const d = readJson(path.join(dir, f)); hosted.push(...(Array.isArray(d) ? d : d.quizzes || d.rows || [])); }
const setsDir = new URL("../home/sets/", import.meta.url);
const setsPath = setsDir.pathname.replace(/^\/([A-Z]:)/, "$1");
const inSets = [];
if (fs.existsSync(setsPath)) for (const f of fs.readdirSync(setsPath).filter((f) => f.endsWith(".json") && f !== "index.json")) {
  const s = readJson(path.join(setsPath, f));
  for (const list of Object.values(s.lists || {})) for (const q of list) inSets.push(key(q.text, q.answers ? q.answers[0] : q.options[q.correct], { id: q.id }));
}
const taken = hostedKeys(hosted).concat(inSets);
const takenIds = new Set(inSets.map((k) => k.id));
console.log(`pool ${pool.length}, hosted items ${taken.length - inSets.length}, already in home sets ${inSets.length}`);

// An index by word and by answer, so each clash check only looks at items that could clash.
class Index {
  constructor() { this.by = new Map(); }
  add(k) { for (const w of [...k.words, "=" + k.ans]) { if (!this.by.has(w)) this.by.set(w, []); this.by.get(w).push(k); } }
  hit(k) { const seen = new Set(); for (const w of [...k.words, "=" + k.ans]) for (const o of this.by.get(w) || []) { if (seen.has(o)) continue; seen.add(o); const why = clash(k, o); if (why) return { o, why }; } return null; }
}
const idx = new Index(); taken.forEach((k) => idx.add(k));

const cat = (r) => String(r.q.category || "");
const usable = pool.filter((r) => !NICHE.test(cat(r)) && !LOCAL.test(cat(r)) && !LOCAL.test(r.q.text || "") && !takenIds.has(r.id));
// deterministic shuffle, so a re-run picks the same candidates
let seed = 20261002; const rnd = () => ((seed = (seed * 1103515245 + 12345) & 0x7fffffff) / 0x7fffffff);
const shuffled = usable.map((r) => [rnd(), r]).sort((a, b) => a[0] - b[0]).map((x) => x[1]);

const out = { mc4: [], typed: [], mc3: [], club: [] };
let clashes = 0;
function tryAdd(kind, r, item) {
  const k = key(item.text, item.answers ? item.answers[0] : item.options[item.correct]);
  if (idx.hit(k)) { clashes++; return false; }
  idx.add(k); out[kind].push(item); r.picked = kind; return true;
}
/** Round-robin by category within each difficulty, so every list is as mixed as the pool allows. */
function pick(kind, quota, rows, make) {
  for (const [level, n] of Object.entries(quota)) {
    const byCat = new Map();
    for (const r of rows) if (!r.picked && (r.difficulty || r.q.difficulty || "medium") === level) { const c = cat(r); if (!byCat.has(c)) byCat.set(c, []); byCat.get(c).push(r); }
    let got = 0, moved = true;
    while (got < n && moved) {
      moved = false;
      for (const list of byCat.values()) {
        while (list.length) { const r = list.shift(); const it = make(r); if (it && tryAdd(kind, r, it)) { got++; moved = true; break; } }
        if (got >= n) break;
      }
    }
    console.log(`${kind} ${level}: ${got}/${n}`);
  }
}
const base = (r) => ({ id: r.id, category: cat(r), difficulty: r.difficulty || r.q.difficulty || "medium", ...(r.q.wow ? { wow: true } : {}) });
const mcOk = (r, n) => r.type === "choice" && (r.q.options || []).length === 4 && /\?$/.test(String(r.q.text).trim()) && String(r.q.text).length <= 150 && r.q.options.every((o) => String(o.text).length <= 40) && !giveaway(r.q.text, answerOf(r.q));
function mc(r, n) {
  if (!mcOk(r, n)) return null;
  const right = answerOf(r.q), wrong = wrongOf(r.q);
  if (n === 3 && /\b(all of|none of|both)\b/i.test(wrong.join(" "))) return null;
  return { ...base(r), text: String(r.q.text).trim(), right, wrong };
}
function typed(r) {
  const ans = r.type === "text" ? (r.q.answers || []) : [answerOf(r.q)];
  if (!ans.length || !typeable(r.q.text, ans[0])) return null;
  // without its options a multiple-choice question is harder to recall: one level up, until the review rates it
  const up = { easy: "medium", medium: "hard", hard: "hard" };
  const b = base(r); if (r.type === "choice") b.difficulty = up[b.difficulty] || "hard";
  return { ...b, text: String(r.q.text).trim(), answers: aliases(r.q.text, ans), src: r.type };
}
const toSet = (it) => ("right" in it ? (({ right, wrong, ...rest }) => ({ ...rest, options: [right, ...wrong], correct: 0 }))(it) : it);

pick("mc4", want.mc4, shuffled, (r) => { const m = mc(r, 4); return m && toSet(m); });
// typed: the ones written to be typed first, then multiple-choice questions that stand up without their options
pick("typed", want.typed, shuffled.filter((r) => r.type === "text"), typed);
const short = Object.fromEntries(Object.entries(want.typed).map(([l, n]) => [l, Math.max(0, n - out.typed.filter((x) => x.difficulty === l).length)]));
// a choice question counts one level harder once typed: fill medium from easy ones, hard from medium ones
pick("typed", { easy: short.medium + short.easy, medium: short.hard }, shuffled.filter((r) => r.type === "choice"), typed);
pick("mc3", want.mc3, shuffled, (r) => { const m = mc(r, 3); return m && toSet(m); });
// The 1% Club: every question with its percentage, checked for clashes like the rest
for (const r of shuffled.filter((r) => r.type === "club").sort((a, b) => (+b.q.pct) - (+a.q.pct))) {
  const it = { ...base(r), pct: +r.q.pct, text: String(r.q.text).trim(), answers: r.q.answers || [], why: r.q.why || "" };
  tryAdd("club", r, it);
}
console.log(`clashes skipped: ${clashes}`);
for (const [k, list] of Object.entries(out)) {
  fs.writeFileSync(path.join(dir, `cands-${k}.json`), "[\n" + list.map((x) => JSON.stringify(x)).join(",\n") + "\n]\n");
  console.log(k, list.length);
}
