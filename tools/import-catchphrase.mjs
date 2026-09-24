// Turns bank/catchphrase/review.json (the clip review) into Catchphrase questions in the bank:
// typed-answer questions whose media is the unlisted YouTube clip. High/medium confidence go in
// as fresh stock; low confidence go in marked rejected with a note, so they show in the bank
// browser's Rejected view for a human check and can be restored with one click.
// Usage: LQ_PASSWORD=... node tools/import-catchphrase.mjs [--end 50]
import fs from "node:fs";
import path from "node:path";
const dir = path.dirname(new URL(import.meta.url).pathname.replace(/^\/([A-Z]:)/, "$1"));
const review = JSON.parse(fs.readFileSync(path.join(dir, "..", "bank", "catchphrase", "review.json"), "utf8"));
const args = process.argv.slice(2); const END = +(args[args.indexOf("--end") + 1] || 50);
const API = "https://safcrtrfdzsnftghibot.supabase.co/functions/v1/quiz-api";
const call = async (body) => { const r = await fetch(API, { method: "POST", headers: { "Content-Type": "application/json", apikey: "sb_publishable_RGaIB8W145BFCWzOxamQvA_7VIkTHMU" }, body: JSON.stringify({ password: process.env.LQ_PASSWORD, ...body }) }); const j = await r.json(); if (j.error) throw new Error(j.error); return j; };
const tidy = (s) => String(s || "").replace(/\s+/g, " ").trim().replace(/^./, (c) => c.toUpperCase());
const seen = new Set(); const fresh = [], unsure = [];
for (const r of review) {
  if (r.kind !== "catchphrase" || !r.answer) continue;
  const key = tidy(r.answer).toLowerCase(); if (seen.has(key)) continue; seen.add(key); // duplicate uploads of the same clip
  const q = { type: "text", kind: "catchphrase", text: "Catchphrase: say what you see", answers: [tidy(r.answer)], media: { kind: "youtube", url: `https://www.youtube.com/watch?v=${r.id}`, videoId: r.id, start: 0, end: END }, time: END, ai: true, difficulty: r.confidence === "high" ? "medium" : "hard", tags: ["catchphrase", "say what you see", "video"] };
  (r.confidence === "low" ? unsure : fresh).push({ q, r });
}
console.log(`catchphrases: ${fresh.length} to add as fresh, ${unsure.length} as 'check me'`);
if (!process.env.LQ_PASSWORD) { console.log("(no LQ_PASSWORD: bank not updated)"); process.exit(0); }
let added = 0;
for (let i = 0; i < fresh.length; i += 40) { const r = await call({ action: "bank_add", type: "catchphrase", category: "Catchphrase", tags: ["catchphrase"], questions: fresh.slice(i, i + 40).map((x) => x.q) }); added += r.added; }
console.log(`fresh: ${added} added`);
let parked = 0;
for (const { q, r } of unsure) { await call({ action: "bank_reject", question: { ...q, category: "Catchphrase" }, category: "Catchphrase", note: `Unverified guess from the clip's frames: ${r.note || ""}`.slice(0, 200) }); parked++; }
console.log(`parked for checking: ${parked}`);
const { bank } = await call({ action: "bank_status" });
console.log("text bank now", bank.text.unused, "/", bank.text.total);
