// Stamps a difficulty on every item of a topic file and pushes the ratings to the bank.
// Usage: LQ_PASSWORD=... node tools/rate-topic.mjs <file> [--easy "sub|sub"] [--hard "sub|sub"] [--default medium]
// An item is rated by the first substring (case-insensitive) that matches its text / track / phrase;
// everything else gets the default. Items that already carry a difficulty are left alone unless --force.
import fs from "node:fs";
const args = process.argv.slice(2);
const file = args[0];
const opt = (k, d = "") => { const i = args.indexOf(k); return i > 0 ? args[i + 1] : d; };
const easy = opt("--easy").split("|").filter(Boolean).map((s) => s.toLowerCase());
const hard = opt("--hard").split("|").filter(Boolean).map((s) => s.toLowerCase());
const dflt = opt("--default", "medium"), force = args.includes("--force");
const items = JSON.parse(fs.readFileSync(file, "utf8"));
const label = (it) => String(it.text || it.track || it.phrase || it.place || "").toLowerCase();
let n = { easy: 0, medium: 0, hard: 0 };
for (const it of items) {
  if (it.difficulty && !force) { n[it.difficulty]++; continue; }
  const l = label(it);
  it.difficulty = easy.some((s) => l.includes(s)) ? "easy" : hard.some((s) => l.includes(s)) ? "hard" : dflt;
  n[it.difficulty]++;
}
fs.writeFileSync(file, "[\n" + items.map((it) => JSON.stringify(it)).join(",\n") + "\n]\n");
console.log(`${file}: ${items.length} items → easy ${n.easy}, medium ${n.medium}, hard ${n.hard}`);
if (!process.env.LQ_PASSWORD) { console.log("(no LQ_PASSWORD: bank not updated)"); process.exit(0); }
const URL = "https://safcrtrfdzsnftghibot.supabase.co/functions/v1/quiz-api";
const call = async (body) => { const r = await fetch(URL, { method: "POST", headers: { "Content-Type": "application/json", apikey: "sb_publishable_RGaIB8W145BFCWzOxamQvA_7VIkTHMU" }, body: JSON.stringify({ password: process.env.LQ_PASSWORD, ...body }) }); const j = await r.json(); if (j.error) throw new Error(j.error); return j; };
const byType = {}; for (const it of items) (byType[it.type] = byType[it.type] || []).push(it);
for (const [type, list] of Object.entries(byType)) {
  const r = await call({ action: "bank_patch", type, patches: list.map((it) => ({ type, text: it.text, track: it.track, artist: it.artist, phrase: it.phrase, place: it.place, answers: it.answers, difficulty: it.difficulty })) });
  console.log(`  ${type}: ${r.changed} rated in the bank${r.missing ? `, ${r.missing} not found` : ""}`);
}
