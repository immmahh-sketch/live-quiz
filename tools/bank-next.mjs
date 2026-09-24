// Prints what the next bank-writing session should do: the first topic (in bank/topics.json
// order) that has fewer than TARGET questions of a plain type in its bank/topics files, and
// how many of each type it still needs. Types counted: choice, text, tf (plus order/sort at a
// lower target). Usage: node tools/bank-next.mjs [--target 50] [--list]
import fs from "node:fs";
import path from "node:path";
const dir = path.dirname(new URL(import.meta.url).pathname.replace(/^\/([A-Z]:)/, "$1"));
const bank = path.join(dir, "..", "bank");
const args = process.argv.slice(2);
const TARGET = +(args[args.indexOf("--target") + 1] || 50);
const SMALL = Math.round(TARGET / 10); // order and sort: a tenth as many
const topics = JSON.parse(fs.readFileSync(path.join(bank, "topics.json"), "utf8"));
const tdir = path.join(bank, "topics");
const files = fs.existsSync(tdir) ? fs.readdirSync(tdir).filter((f) => f.endsWith(".json")) : [];
const counts = {};
for (const f of files) {
  const slug = f.replace(/\.json$/, "").split("__")[0];
  for (const it of JSON.parse(fs.readFileSync(path.join(tdir, f), "utf8"))) { const c = counts[slug] = counts[slug] || {}; c[it.type] = (c[it.type] || 0) + 1; }
}
const need = (slug) => { const c = counts[slug] || {}; return { choice: Math.max(0, TARGET - (c.choice || 0)), text: Math.max(0, TARGET - (c.text || 0)), tf: Math.max(0, TARGET - (c.tf || 0)), order: Math.max(0, SMALL - (c.order || 0)), sort: Math.max(0, SMALL - (c.sort || 0)) }; };
const rows = topics.map((t) => ({ t, n: need(t.slug), have: counts[t.slug] || {} }));
if (args.includes("--list")) { for (const r of rows) console.log(`${r.t.slug.padEnd(26)} choice ${String(r.have.choice || 0).padStart(3)}  text ${String(r.have.text || 0).padStart(3)}  tf ${String(r.have.tf || 0).padStart(3)}  order ${r.have.order || 0}  sort ${r.have.sort || 0}`); process.exit(0); }
const next = rows.find((r) => Object.values(r.n).some((v) => v > 0));
const done = rows.filter((r) => !Object.values(r.n).some((v) => v > 0)).length;
console.log(`${done}/${topics.length} topics at target ${TARGET}.`);
if (!next) { console.log("All topics at target."); process.exit(0); }
const suffix = files.some((f) => f.startsWith(next.t.slug)) ? `__${files.filter((f) => f.startsWith(next.t.slug + "__") || f === next.t.slug + ".json").length + 1}` : "";
console.log(`NEXT: ${next.t.slug} (${next.t.name}) → write bank/topics/${next.t.slug}${suffix}.json with ${Object.entries(next.n).filter(([, v]) => v > 0).map(([k, v]) => `${v} ${k}`).join(", ")}`);
console.log(`Brief: ${next.t.brief}`);
