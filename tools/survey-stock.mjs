// Stocks the bank with Family Fortunes prompts from bank/survey-prompts.json: [prompt, [likely answers]].
// The room is the survey, so the likely answers are only for the host's notes and the practice bots. Needs LQ_PASSWORD.
import fs from "fs";
const API = "https://safcrtrfdzsnftghibot.supabase.co/functions/v1/quiz-api";
const KEY = "sb_publishable_RGaIB8W145BFCWzOxamQvA_7VIkTHMU";
const PASSWORD = process.env.LQ_PASSWORD;
if (!PASSWORD) { console.error("Set LQ_PASSWORD to the host password."); process.exit(1); }
async function call(body) {
  const r = await fetch(API, { method: "POST", headers: { "content-type": "application/json", apikey: KEY, Authorization: "Bearer " + KEY }, body: JSON.stringify({ password: PASSWORD, ...body }) });
  const d = await r.json().catch(() => ({})); if (!r.ok || d.error) throw new Error(d.error || "HTTP " + r.status); return d;
}
const list = JSON.parse(fs.readFileSync(new URL("../bank/survey-prompts.json", import.meta.url), "utf8"));
const qs = list.map(([text, answers]) => ({ type: "text", kind: "survey", text: `We asked the room: ${text.charAt(0).toLowerCase()}${text.slice(1)}`, answers, ai: false, time: 30, difficulty: "easy", media: { kind: "none" }, partial: false }));
for (let i = 0; i < qs.length; i += 40) { const r = await call({ action: "bank_add", type: "survey", category: "Family Fortunes", tags: ["survey"], questions: qs.slice(i, i + 40) }); console.log(`+${r.added} (${r.skipped} skipped) → ${r.total}`); }
