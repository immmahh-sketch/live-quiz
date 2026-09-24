// Imports bank/<type>.json files into the question bank on the server.
//   node tools/import-bank.mjs club dingbat wheel        (or no args for every file in bank/)
// Needs the host password in LQ_PASSWORD. Items are in the writer's JSON shape plus
// "category" and "tags"; the server finishes them (pictures, maps, clips) and skips
// duplicates, so re-running is safe.
import fs from "node:fs";
import path from "node:path";
import vm from "node:vm";

const API = "https://safcrtrfdzsnftghibot.supabase.co/functions/v1/quiz-api";
const KEY = "sb_publishable_RGaIB8W145BFCWzOxamQvA_7VIkTHMU";
const PASSWORD = process.env.LQ_PASSWORD;
if (!PASSWORD) { console.error("Set LQ_PASSWORD to the host password."); process.exit(1); }

// common.js gives us the Wheel of Fortune board check without a browser
const ctx = { window: {}, localStorage: { getItem: () => null, setItem() {}, removeItem() {} }, location: { href: "https://letsquiz.uk/" }, URL, document: undefined, Image: class {}, fetch };
vm.createContext(ctx);
vm.runInContext(fs.readFileSync(new URL("../assets/common.js", import.meta.url), "utf8"), ctx);
const LQ = ctx.window.LQ;

async function call(body) {
  const r = await fetch(API, { method: "POST", headers: { "content-type": "application/json", apikey: KEY, Authorization: "Bearer " + KEY }, body: JSON.stringify({ password: PASSWORD, ...body }) });
  const d = await r.json();
  if (!r.ok || d.error) throw new Error(d.error || ("HTTP " + r.status));
  return d;
}

const dir = new URL("../bank/", import.meta.url);
// bank/<type>.json plus any bank/<type>-2.json, bank/<type>-extra.json… all count for that type
const dirPath = dir.pathname.replace(/^\/([A-Z]:)/, "$1");
const files = fs.readdirSync(dirPath).filter((f) => f.endsWith(".json") && f !== "topics.json");
const typeOf = (f) => f.replace(/\.json$/, "").replace(/-.*$/, "");
const types = process.argv.slice(2).length ? process.argv.slice(2).filter((a) => a !== "topics") : [...new Set(files.map(typeOf))];
for (const type of types) {
  const mine = files.filter((f) => typeOf(f) === type).sort();
  if (!mine.length) { console.warn(`${type}: no bank files`); continue; }
  let items = mine.flatMap((f) => JSON.parse(fs.readFileSync(path.join(dirPath, f), "utf8")));
  if (type === "wheel") {
    const before = items.length;
    items = items.filter((it) => { const ok = !!LQ.wheelLayout(String(it.phrase || "").toUpperCase()); if (!ok) console.warn(`  wheel: "${it.phrase}" does not fit the board, skipped`); return ok; });
    if (items.length !== before) console.log(`  ${before - items.length} phrase(s) skipped`);
  }
  if (type === "choice") {
    // bank files list the right answer first; the game keeps builder order, so shuffle here
    for (const it of items) { it.answer = it.answer || it.options[0]; it.options = it.options.map((o) => [Math.random(), o]).sort((a, b) => a[0] - b[0]).map((x) => x[1]); }
  }
  console.log(`${type}: ${items.length} items`);
  let added = 0, skipped = 0;
  const CHUNK = +process.env.CHUNK || 40;
  for (let i = 0; i < items.length; i += CHUNK) {
    const chunk = items.slice(i, i + CHUNK);
    try {
      const r = await call({ action: "bank_import", type, items: chunk });
      added += r.added; skipped += r.skipped;
      for (const w of r.warnings || []) console.warn("  !", w);
      process.stdout.write(`  ${Math.min(i + CHUNK, items.length)}/${items.length} → bank now ${r.total}\n`);
    } catch (e) { console.error(`  chunk ${i}: ${e.message}`); }
  }
  console.log(`  added ${added}, skipped ${skipped} (duplicates or unusable)`);
}
// bank/topics/<slug>.json: one file per topic, items of mixed types, each with "type"; the topic's
// name and tags from bank/topics.json are stamped on every item as category/tags.
const topicsDir = path.join(dirPath, "topics");
if (fs.existsSync(topicsDir) && (!process.argv.slice(2).length || process.argv.includes("topics"))) {
  const topics = JSON.parse(fs.readFileSync(path.join(dirPath, "topics.json"), "utf8"));
  const only = (process.env.TOPICS || "").split(",").filter(Boolean);
  for (const f of fs.readdirSync(topicsDir).filter((f) => f.endsWith(".json")).sort()) {
    const slug = f.replace(/\.json$/, "").split("__")[0]; // christmas-movies__2.json tops up christmas-movies
    if (only.length && !only.includes(slug)) continue;
    const t = topics.find((x) => x.slug === slug);
    if (!t) { console.warn(`topics/${f}: no such topic in topics.json, skipped`); continue; }
    const items = JSON.parse(fs.readFileSync(path.join(topicsDir, f), "utf8"));
    const byType = {};
    for (const it of items) {
      if (!it.type) continue;
      const item = { ...it, category: t.name, tags: [...new Set([...(t.tags || []), ...(it.tags || [])])] };
      if (item.type === "choice") { item.answer = item.answer || item.options[0]; item.options = item.options.map((o) => [Math.random(), o]).sort((a, b) => a[0] - b[0]).map((x) => x[1]); }
      if (item.type === "wheel" && !LQ.wheelLayout(String(item.phrase || "").toUpperCase())) { console.warn(`  ${slug}: wheel "${item.phrase}" does not fit, skipped`); continue; }
      (byType[item.type] = byType[item.type] || []).push(item);
    }
    console.log(`${t.name}: ${items.length} items (${Object.entries(byType).map(([k, v]) => `${k} ${v.length}`).join(", ")})`);
    for (const [type, list] of Object.entries(byType)) {
      for (let i = 0; i < list.length; i += 40) {
        try { const r = await call({ action: "bank_import", type, items: list.slice(i, i + 40) }); for (const w of r.warnings || []) console.warn("  !", w); process.stdout.write(`  ${type}: +${r.added} (${r.skipped} dupes) → ${r.total}
`); }
        catch (e) { console.error(`  ${type}: ${e.message}`); }
      }
    }
  }
}
const status = await call({ action: "bank_status" });
console.log("\nBank now:", Object.entries(status.bank).map(([t, s]) => `${t} ${s.unused}/${s.total}${s.low ? " LOW" : ""}`).join(" · "));
