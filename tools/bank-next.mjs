// Prints what the next bank-writing session should do: the first topic (in bank/topics.json
// order) that has fewer than the target number of questions of some type in its bank/topics
// files, and how many of each type it still needs. Plain types (choice, text, tf) target 50 per
// topic; put-in-order and categorise 5; the heavy types (highlow, smash, tune 10 each; wipeout
// boards 5; races 3) are whole rounds, so fewer are needed.
// Usage: node tools/bank-next.mjs [--target 50] [--list] [--all]
import fs from "node:fs";
import path from "node:path";
const dir = path.dirname(new URL(import.meta.url).pathname.replace(/^\/([A-Z]:)/, "$1"));
const bank = path.join(dir, "..", "bank");
const args = process.argv.slice(2);
const TARGET = +(args[args.indexOf("--target") + 1] || 50);
// Every topic gets every writable type, so a themed quiz can have any round. Catchphrase is left out: it only comes from video clips.
const GOAL = { choice: TARGET, text: TARGET, tf: TARGET, order: Math.round(TARGET / 10), sort: Math.round(TARGET / 10), highlow: 10, smash: 10, tune: 10, rhyme: 10, wipeout: 5, race: 3, pin: 5, match: 5, wheel: 5, club: 5, dingbat: 3 };
const topics = JSON.parse(fs.readFileSync(path.join(bank, "topics.json"), "utf8"));
const tdir = path.join(bank, "topics");
const files = fs.existsSync(tdir) ? fs.readdirSync(tdir).filter((f) => f.endsWith(".json")) : [];
const counts = {};
for (const f of files) {
  const slug = f.replace(/\.json$/, "").split("__")[0];
  for (const it of JSON.parse(fs.readFileSync(path.join(tdir, f), "utf8"))) { const c = counts[slug] = counts[slug] || {}; c[it.type] = (c[it.type] || 0) + 1; }
}
const SIGNATURE = new Set(topics.filter((t) => t.group === "Signature").map((t) => t.slug)); // answer-is-always-X topics only need plain questions
const GEO = new Set(topics.filter((t) => t.group === "Geography").map((t) => t.slug)); // place topics get twice the pins
const need = (slug) => { const c = counts[slug] || {}; const out = {}; for (const [t, g] of Object.entries(GOAL)) { const n = t === "pin" && GEO.has(slug) ? g * 2 : g; if (SIGNATURE.has(slug) && !["choice", "text"].includes(t)) continue; out[t] = Math.max(0, n - (c[t] || 0)); } return out; };
const rows = topics.map((t) => ({ t, n: need(t.slug), have: counts[t.slug] || {} }));
const short = (r) => Object.entries(r.n).filter(([, v]) => v > 0);
if (args.includes("--list")) { for (const r of rows) console.log(`${r.t.slug.padEnd(26)} ${Object.keys(GOAL).map((t) => `${t} ${String(r.have[t] || 0).padStart(2)}`).join("  ")}`); process.exit(0); }
const done = rows.filter((r) => !short(r).length).length;
console.log(`${done}/${topics.length} topics complete.`);
const todo = args.includes("--all") ? rows.filter((r) => short(r).length) : rows.filter((r) => short(r).length).slice(0, 1);
if (!todo.length) { console.log("All topics at target."); process.exit(0); }
for (const next of todo) {
  const n = files.filter((f) => f === next.t.slug + ".json" || f.startsWith(next.t.slug + "__")).length;
  const suffix = n ? `__${n + 1}` : "";
  console.log(`NEXT: ${next.t.slug} (${next.t.name}) → write bank/topics/${next.t.slug}${suffix}.json with ${short(next).map(([k, v]) => `${v} ${k}`).join(", ")}`);
  console.log(`Brief: ${next.t.brief}`);
}
