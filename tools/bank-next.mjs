// Prints what the next bank-writing session should do: the first topic (in bank/topics.json
// order) that has fewer than the target number of questions of some type in its bank/topics
// files, and how many of each type it still needs. Plain types (choice, text, tf) target 50 per
// topic; put-in-order and categorise 5; the heavy types (highlow, smash, tune 10 each; wipeout
// boards 5; races 3) are whole rounds, so fewer are needed.
// Difficulty: every item is rated on its own merits, never relabelled to hit a mix. A topic whose
// honest ratings stray from the 25/45/30 easy/medium/hard mix gets a balancing top-up of new
// questions at the levels it is short of, so the mix is fixed by writing harder (or easier)
// questions, not by relabelling.
// Usage: node tools/bank-next.mjs [--target 50] [--list] [--all]
import fs from "node:fs";
import path from "node:path";
const dir = path.dirname(new URL(import.meta.url).pathname.replace(/^\/([A-Z]:)/, "$1"));
const bank = path.join(dir, "..", "bank");
const args = process.argv.slice(2);
const TARGET = args.includes("--target") ? +args[args.indexOf("--target") + 1] : 50;
// Every topic gets every writable type, so a themed quiz can have any round. Catchphrase is left out: it only comes from video clips.
const GOAL = { choice: TARGET, text: TARGET, tf: TARGET, order: Math.round(TARGET / 10), sort: Math.round(TARGET / 10), highlow: 10, smash: 10, tune: 10, rhyme: 10, wipeout: 5, race: 3, pin: 5, match: 5, wheel: 5, club: 5, dingbat: 3 };
const MIX = { easy: 0.25, medium: 0.45, hard: 0.3 };
const topics = JSON.parse(fs.readFileSync(path.join(bank, "topics.json"), "utf8"));
const tdir = path.join(bank, "topics");
const files = fs.existsSync(tdir) ? fs.readdirSync(tdir).filter((f) => f.endsWith(".json")) : [];
const counts = {}, levels = {};
for (const f of files) {
  const slug = f.replace(/\.json$/, "").split("__")[0];
  for (const it of JSON.parse(fs.readFileSync(path.join(tdir, f), "utf8"))) {
    const c = counts[slug] = counts[slug] || {}; c[it.type] = (c[it.type] || 0) + 1;
    const l = levels[slug] = levels[slug] || { easy: 0, medium: 0, hard: 0 }; if (it.difficulty in l) l[it.difficulty]++;
  }
}
const SIGNATURE = new Set(topics.filter((t) => t.group === "Signature").map((t) => t.slug)); // answer-is-always-X topics only need plain questions
const GEO = new Set(topics.filter((t) => t.group === "Geography").map((t) => t.slug)); // place topics get twice the pins
const need = (slug) => { const c = counts[slug] || {}; const out = {}; for (const [t, g] of Object.entries(GOAL)) { const n = t === "pin" && GEO.has(slug) ? g * 2 : g; if (SIGNATURE.has(slug) && !["choice", "text"].includes(t)) continue; out[t] = Math.max(0, n - (c[t] || 0)); } return out; };
// How many new questions of each level bring the topic to the mix, when it is also gaining `add` items for missing types.
// Returns null when a finished topic is close enough (small drifts are fine).
const split = (slug, add) => {
  const l = levels[slug] || { easy: 0, medium: 0, hard: 0 }, n = l.easy + l.medium + l.hard;
  const total = Math.max(n + add, ...Object.entries(MIX).map(([k, p]) => Math.ceil(l[k] / p)));
  const out = {}; for (const [k, p] of Object.entries(MIX)) out[k] = Math.max(0, Math.round(p * total) - l[k]);
  return !add && out.easy + out.medium + out.hard < Math.max(8, Math.round(0.03 * n)) ? null : out;
};
const mixOf = (slug) => { const l = levels[slug] || {}; const n = (l.easy || 0) + (l.medium || 0) + (l.hard || 0); return n ? `easy ${Math.round(100 * l.easy / n)}% · medium ${Math.round(100 * l.medium / n)}% · hard ${Math.round(100 * l.hard / n)}%` : "unrated"; };
const words = (o) => ["easy", "medium", "hard"].filter((k) => o[k] > 0).map((k) => `${o[k]} ${k}`).join(", ");
const rows = topics.map((t) => ({ t, n: need(t.slug), have: counts[t.slug] || {} }));
const short = (r) => Object.entries(r.n).filter(([, v]) => v > 0);
const unbalanced = (r) => !short(r).length && !!counts[r.t.slug] && !!split(r.t.slug, 0);
const pending = (r) => short(r).length > 0 || unbalanced(r);
if (args.includes("--list")) { for (const r of rows) console.log(`${r.t.slug.padEnd(26)} ${Object.keys(GOAL).map((t) => `${t} ${String(r.have[t] || 0).padStart(2)}`).join("  ")}  | ${mixOf(r.t.slug)}`); process.exit(0); }
const done = rows.filter((r) => !pending(r)).length;
console.log(`${done}/${topics.length} topics complete (${rows.filter(unbalanced).length} more have every type but need difficulty balancing).`);
// Topics with fewer than 100 questions come first, so every topic can carry a themed quiz; balancing follows.
const total = (r) => Object.values(r.have).reduce((x, y) => x + y, 0);
const order = [...rows.filter((r) => pending(r) && total(r) < 100), ...rows.filter((r) => pending(r) && total(r) >= 100)];
const todo = args.includes("--all") ? order : order.slice(0, 1);
if (!todo.length) { console.log("All topics at target."); process.exit(0); }
for (const next of todo) {
  const n = files.filter((f) => f === next.t.slug + ".json" || f.startsWith(next.t.slug + "__")).length;
  const suffix = n ? `__${n + 1}` : "";
  const add = short(next).reduce((s, [, v]) => s + v, 0);
  if (add) {
    console.log(`NEXT: ${next.t.slug} (${next.t.name}) → write bank/topics/${next.t.slug}${suffix}.json with ${short(next).map(([k, v]) => `${v} ${k}`).join(", ")}`);
    if (counts[next.t.slug]) console.log(`Difficulty: the topic is ${mixOf(next.t.slug)} so far; make about ${words(split(next.t.slug, add))} of them (rated honestly).`);
  } else {
    const d = split(next.t.slug, 0), sum = d.easy + d.medium + d.hard; // at most 100 in one session; the next run asks for the rest
    if (sum > 100) for (const k of Object.keys(d)) d[k] = Math.round(d[k] * 100 / sum);
    console.log(`BALANCE: ${next.t.slug} (${next.t.name}) is ${mixOf(next.t.slug)} → write bank/topics/${next.t.slug}${suffix}.json with ${words(d)} questions, genuinely that hard (mostly choice, text and tf; any type is fine)`);
  }
  console.log(`Brief: ${next.t.brief}`);
}
