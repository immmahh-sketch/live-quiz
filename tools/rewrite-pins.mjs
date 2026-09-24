// Turns "Drop the pin on X" bank questions into two-step questions ("Which city hosted the 2016
// Olympics?" → the player must know it is Rio, then find it) using bank/pin-clues.json (place → clue).
// Updates the bank in place and the bank/pin*.json source files. Usage: LQ_PASSWORD=... node tools/rewrite-pins.mjs
import fs from "node:fs";
import path from "node:path";
const dir = path.dirname(new URL(import.meta.url).pathname.replace(/^\/([A-Z]:)/, "$1"));
const bank = path.join(dir, "..", "bank");
const clues = JSON.parse(fs.readFileSync(path.join(bank, "pin-clues.json"), "utf8"));
const norm = (s) => String(s || "").toLowerCase().replace(/^the /, "").replace(/[^a-z0-9]+/g, " ").trim();
const byPlace = new Map(Object.entries(clues).map(([k, v]) => [norm(k), v]));
const API = "https://safcrtrfdzsnftghibot.supabase.co/functions/v1/quiz-api";
const call = async (body) => { const r = await fetch(API, { method: "POST", headers: { "Content-Type": "application/json", apikey: "sb_publishable_RGaIB8W145BFCWzOxamQvA_7VIkTHMU" }, body: JSON.stringify({ password: process.env.LQ_PASSWORD, ...body }) }); const j = await r.json(); if (j.error) throw new Error(j.error); return j; };
// source files first, so a re-import never brings the old wording back
for (const f of fs.readdirSync(bank).filter((f) => /^pin(-\d+)?\.json$/.test(f))) {
  const p = path.join(bank, f); const items = JSON.parse(fs.readFileSync(p, "utf8")); let n = 0;
  for (const it of items) { const c = byPlace.get(norm(it.place)); if (c && /^drop the pin/i.test(it.text || "")) { it.text = c; n++; } }
  fs.writeFileSync(p, JSON.stringify(items, null, 1) + "\n"); console.log(`${f}: ${n} rewritten`);
}
if (!process.env.LQ_PASSWORD) { console.log("(no LQ_PASSWORD: bank not updated)"); process.exit(0); }
const { questions } = await call({ action: "bank_list", type: "pin" });
const patches = [], missing = [];
for (const q of questions) {
  if (!/^drop the pin/i.test(q.text)) continue;
  const c = byPlace.get(norm(q.answer));
  if (c) patches.push({ id: q.id, newText: c }); else missing.push(q.answer);
}
for (let i = 0; i < patches.length; i += 100) { const r = await call({ action: "bank_patch", type: "pin", patches: patches.slice(i, i + 100) }); console.log(`bank: ${r.changed} rewritten`); }
if (missing.length) console.log("no clue for:", missing.join(", "));
