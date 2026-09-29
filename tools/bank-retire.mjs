// Takes bank items of any type out of stock (stamped rejected, so they are never picked; bank_restore undoes it).
//   LQ_PASSWORD=… node tools/bank-retire.mjs <type> <id> [<id> …]
// e.g. node tools/bank-retire.mjs race q_b099e837 q_041a2991
// For Wipeout boards, tools/wipe-topup.mjs does the same with { "retire": true } and can also top up or widen.
const API = "https://safcrtrfdzsnftghibot.supabase.co/functions/v1/quiz-api";
const KEY = "sb_publishable_RGaIB8W145BFCWzOxamQvA_7VIkTHMU";
const PASSWORD = process.env.LQ_PASSWORD;
if (!PASSWORD) { console.error("Set LQ_PASSWORD to the host password."); process.exit(1); }
const [type, ...ids] = process.argv.slice(2);
if (!type || !ids.length) { console.error("Usage: node tools/bank-retire.mjs <type> <id> [<id> …]"); process.exit(1); }
async function call(body) {
  const r = await fetch(API, { method: "POST", headers: { "content-type": "application/json", apikey: KEY, Authorization: "Bearer " + KEY }, body: JSON.stringify({ password: PASSWORD, ...body }) });
  const d = await r.json().catch(() => ({})); if (!r.ok || d.error) throw new Error(d.error || "HTTP " + r.status); return d;
}
for (const id of ids) {
  const { question: q } = await call({ action: "bank_get", type, id });
  await call({ action: "bank_reject", question: { ...q, bankId: id } });
  console.log(`${id}  ${q.text}: retired`);
}
