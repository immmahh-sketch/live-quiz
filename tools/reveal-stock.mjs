// Stocks the bank with Picture Reveal questions: a Wikipedia photo of each person in bank/reveal-people.json,
// copied into our bucket by the server's picture action, added under type "reveal". Re-running is safe: people
// already in the bank are skipped as duplicates. Needs the host password in LQ_PASSWORD.
import fs from "fs";
const API = "https://safcrtrfdzsnftghibot.supabase.co/functions/v1/quiz-api";
const KEY = "sb_publishable_RGaIB8W145BFCWzOxamQvA_7VIkTHMU";
const PASSWORD = process.env.LQ_PASSWORD;
if (!PASSWORD) { console.error("Set LQ_PASSWORD to the host password."); process.exit(1); }
async function call(body) {
  const r = await fetch(API, { method: "POST", headers: { "content-type": "application/json", apikey: KEY, Authorization: "Bearer " + KEY }, body: JSON.stringify({ password: PASSWORD, ...body }) });
  const d = await r.json().catch(() => ({})); if (!r.ok || d.error) throw new Error(d.error || "HTTP " + r.status); return d;
}
// PEOPLE=<file> stocks just the people in that file (the same shape), not the whole list again.
const people = JSON.parse(fs.readFileSync(process.env.PEOPLE || new URL("../bank/reveal-people.json", import.meta.url), "utf8"));
const out = [];
for (const p of people) {
  try {
    const pic = await call({ action: "picture", title: p.title });
    out.push({ type: "text", kind: "reveal", text: "Picture Reveal: who is this?", answers: p.answers, ai: true, tiles: 16, time: 40, difficulty: p.difficulty,
      media: { kind: "image", url: pic.url, credit: `Wikipedia / Wikimedia Commons: ${p.title}`, source: pic.source }, partial: false });
    process.stdout.write(".");
  } catch (e) { console.log(`\n  ! ${p.title}: ${e.message}`); }
}
console.log(`\n${out.length} pictures`);
for (let i = 0; i < out.length; i += 40) { const r = await call({ action: "bank_add", type: "reveal", category: "Famous faces", tags: ["people", "picture"], questions: out.slice(i, i + 40) }); console.log(`+${r.added} (${r.skipped} skipped) → ${r.total}`); }
