// Repairs bank Wipeout boards by hand: top up, widen or retire.
//   LQ_PASSWORD=… node tools/wipe-topup.mjs bank/wipe-topups/<file>.json
// The file maps bank ids to what to do:
//   { "q_…": { "right": ["…"], "wrong": ["…"] } }                 add answers (duplicates of what is there are skipped)
//   { "q_…": { "text": "New wording", "setRight": [...], "setWrong": [...] } }   widen a closed set: new wording and lists
//   { "q_…": { "retire": true } }                                   take out of stock (stamped rejected; bank_restore undoes it)
// Aim for 15 right and 5 wrong. Safe to re-run: additions already on the board are skipped.
import fs from "fs";

const API = "https://safcrtrfdzsnftghibot.supabase.co/functions/v1/quiz-api";
const KEY = "sb_publishable_RGaIB8W145BFCWzOxamQvA_7VIkTHMU";
const PASSWORD = process.env.LQ_PASSWORD;
if (!PASSWORD) { console.error("Set LQ_PASSWORD."); process.exit(1); }
const file = process.argv[2];
if (!file) { console.error("Usage: node tools/wipe-topup.mjs <file.json>"); process.exit(1); }

async function call(body) {
  const r = await fetch(API, { method: "POST", headers: { "content-type": "application/json", apikey: KEY, Authorization: "Bearer " + KEY }, body: JSON.stringify({ password: PASSWORD, ...body }) });
  const j = await r.json();
  if (!r.ok || j.error) throw new Error(j.error || r.statusText);
  return j;
}
const norm = (s) => String(s || "").toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/[^a-z0-9]+/g, " ").trim();
const uid = () => "w_" + Math.random().toString(36).slice(2, 10);
const items = (list) => list.map((text) => ({ id: uid(), text }));

const plan = JSON.parse(fs.readFileSync(file, "utf8"));
for (const [id, add] of Object.entries(plan)) {
  const { question: q } = await call({ action: "bank_get", type: "wipeout", id });
  if (add.retire) {
    await call({ action: "bank_reject", question: { ...q, bankId: id } });
    console.log(`${id}  ${q.text}: retired`);
    continue;
  }
  let right = add.setRight ? items(add.setRight) : [...(q.right || [])];
  let wrong = add.setWrong ? items(add.setWrong) : [...(q.wrong || [])];
  const seen = new Set([...right, ...wrong].map((x) => norm(x.text)));
  const fresh = (list) => (list || []).filter((t) => { const k = norm(t); if (!k || seen.has(k)) return false; seen.add(k); return true; });
  right = [...right, ...items(fresh(add.right))].slice(0, 20);
  wrong = [...wrong, ...items(fresh(add.wrong))].slice(0, 10);
  const nq = { ...q, text: add.text || q.text, right, wrong };
  delete nq.used; // the server keeps the item's own used stamp
  await call({ action: "bank_edit", type: "wipeout", id, question: nq });
  console.log(`${id}  ${nq.text}: ${q.right.length}→${right.length} right, ${q.wrong.length}→${wrong.length} wrong`);
}
