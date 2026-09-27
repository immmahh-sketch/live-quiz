// Stocks the bank with Only One games: 8 closed-list prompts each ({p, a: [every correct answer]}), drawn at random
// from bank/unique-prompts.json. Re-running adds fresh games (one that starts like an existing one is skipped). Needs LQ_PASSWORD.
import fs from "fs";
const API = "https://safcrtrfdzsnftghibot.supabase.co/functions/v1/quiz-api";
const KEY = "sb_publishable_RGaIB8W145BFCWzOxamQvA_7VIkTHMU";
const PASSWORD = process.env.LQ_PASSWORD;
if (!PASSWORD) { console.error("Set LQ_PASSWORD to the host password."); process.exit(1); }
async function call(body) {
  const r = await fetch(API, { method: "POST", headers: { "content-type": "application/json", apikey: KEY, Authorization: "Bearer " + KEY }, body: JSON.stringify({ password: PASSWORD, ...body }) });
  const d = await r.json().catch(() => ({})); if (!r.ok || d.error) throw new Error(d.error || "HTTP " + r.status); return d;
}
const all = JSON.parse(fs.readFileSync(new URL("../bank/unique-prompts.json", import.meta.url), "utf8"));
for (let i = all.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [all[i], all[j]] = [all[j], all[i]]; }
const games = [], N = +(process.env.GAMES || 8);
for (let g = 0; g < N; g++) { const pick = [...all].sort(() => Math.random() - 0.5).slice(0, 8); games.push({ type: "unique", text: "Only One", prompts: pick, perRound: 100, prize: 1000, time: 25, difficulty: "medium", media: { kind: "none" }, partial: false }); }
const r = await call({ action: "bank_add", type: "unique", category: "Only One", tags: ["unique"], questions: games });
console.log(`+${r.added} (${r.skipped} skipped) → ${r.total}`);
