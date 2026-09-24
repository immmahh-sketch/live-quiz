// Fills the question bank by topic using the server's AI writer (Sonnet for plain types).
//   LQ_PASSWORD=... node tools/generate-bank.mjs --topics christmas-movies,friends --per 100 --types choice,text,tf
//   LQ_PASSWORD=... node tools/generate-bank.mjs --all --per 100
// Topics come from bank/topics.json. For each topic and type it asks the writer for questions
// in batches, then adds them to the bank tagged with the topic (category = topic name), so a
// round on that topic pulls them first. Progress is saved in bank/gen/<slug>.json so a run can
// be resumed; --dry prints the plan and the estimated cost without calling anything.
import fs from "node:fs";
import path from "node:path";

const API = "https://safcrtrfdzsnftghibot.supabase.co/functions/v1/quiz-api";
const KEY = "sb_publishable_RGaIB8W145BFCWzOxamQvA_7VIkTHMU";
const PASSWORD = process.env.LQ_PASSWORD;
const args = Object.fromEntries(process.argv.slice(2).map((a, i, all) => a.startsWith("--") ? [a.slice(2), all[i + 1] && !all[i + 1].startsWith("--") ? all[i + 1] : true] : []).filter((x) => x.length));
const dir = path.dirname(new URL(import.meta.url).pathname.replace(/^\/([A-Z]:)/, "$1"));
const topics = JSON.parse(fs.readFileSync(path.join(dir, "..", "bank", "topics.json"), "utf8"));
const chosen = args.all ? topics : topics.filter((t) => String(args.topics || "").split(",").includes(t.slug));
const per = +args.per || 100;
const types = String(args.types || "choice,text,tf,order,sort").split(",");
const SPLIT = { choice: 0.4, text: 0.3, tf: 0.15, order: 0.08, sort: 0.07 };
const BATCH = { choice: 6, text: 6, tf: 6, order: 4, sort: 4, club: 4, dingbat: 4, tune: 4 };
if (!chosen.length) { console.error("No topics matched. Use --topics slug,slug or --all."); process.exit(1); }
if (!PASSWORD && !args.dry) { console.error("Set LQ_PASSWORD."); process.exit(1); }

const plan = chosen.map((t) => ({ t, want: Object.fromEntries(types.map((ty) => [ty, Math.max(0, Math.round(per * (SPLIT[ty] ?? 1 / types.length)))])) }));
const calls = plan.reduce((a, p) => a + Object.entries(p.want).reduce((b, [ty, n]) => b + Math.ceil(n / (BATCH[ty] || 4)), 0), 0);
const questions = plan.reduce((a, p) => a + Object.values(p.want).reduce((b, n) => b + n, 0), 0);
// Sonnet at list price, with the cached prompt: roughly 3k cached input + 700 fresh input + 1.2k output per call, plus up to 3 searches.
const usd = calls * ((3000 * 0.3 + 700 * 3 + 1200 * 15) / 1e6 + 3 * 0.01);
console.log(`${chosen.length} topic(s), ${questions} questions, ~${calls} writer calls, roughly $${usd.toFixed(0)} at list prices (mostly web search).`);
if (args.dry) process.exit(0);

async function call(body) {
  const r = await fetch(API, { method: "POST", headers: { "content-type": "application/json", apikey: KEY, Authorization: "Bearer " + KEY }, body: JSON.stringify({ password: PASSWORD, ...body }) });
  const d = await r.json();
  if (!r.ok || d.error) throw new Error(d.error || ("HTTP " + r.status));
  return d;
}
const genDir = path.join(dir, "..", "bank", "gen"); fs.mkdirSync(genDir, { recursive: true });

for (const { t, want } of plan) {
  const file = path.join(genDir, t.slug + ".json");
  const done = fs.existsSync(file) ? JSON.parse(fs.readFileSync(file, "utf8")) : { added: {}, avoid: [] };
  console.log(`\n== ${t.name}`);
  for (const [type, n] of Object.entries(want)) {
    let have = done.added[type] || 0;
    while (have < n) {
      const count = Math.min(BATCH[type] || 4, n - have);
      try {
        const r = await call({ action: "generate", useBank: false, premium: false, pictures: false, web: true, types: [type], count, topic: t.name, title: t.name, brief: t.brief, avoid: done.avoid.slice(-400) });
        const qs = (r.questions || []).filter((q) => q.type === type);
        if (!qs.length) { console.warn(`  ${type}: writer returned nothing, moving on`); break; }
        const add = await call({ action: "bank_add", type, category: t.name, tags: t.tags, questions: qs });
        have += add.added; done.added[type] = have;
        for (const q of qs) done.avoid.push(q.text || q.phrase || "");
        fs.writeFileSync(file, JSON.stringify(done));
        const u = r.usage || {};
        console.log(`  ${type}: ${have}/${n}  (+${add.added}, ${add.skipped} dupes; ${u.model || ""} ${u.searches || 0} searches)`);
      } catch (e) { console.error(`  ${type}: ${e.message}`); await new Promise((res) => setTimeout(res, 5000)); if (/credit|rate/i.test(e.message)) process.exit(1); }
    }
  }
}
const status = await call({ action: "bank_status" });
console.log("\nBank now:", Object.entries(status.bank).map(([t, s]) => `${t} ${s.unused}/${s.total}`).join(" · "));
