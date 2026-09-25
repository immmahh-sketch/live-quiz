// Lists the items of a bank topic file that are not in the live bank (the importer skipped them as
// duplicates of questions already there), so they can be replaced with fresh ones and re-imported.
// Usage: LQ_PASSWORD=... node tools/bank-missing.mjs bank/topics/<slug>__N.json
import fs from "node:fs";
const URL = "https://safcrtrfdzsnftghibot.supabase.co/functions/v1/quiz-api";
const call = async (body) => { const r = await fetch(URL, { method: "POST", headers: { "Content-Type": "application/json", apikey: "sb_publishable_RGaIB8W145BFCWzOxamQvA_7VIkTHMU" }, body: JSON.stringify({ password: process.env.LQ_PASSWORD, ...body }) }); const j = await r.json(); if (j.error) throw new Error(j.error); return j; };
const norm = (s) => String(s || "").toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "").replace(/&/g, " and ").replace(/[^a-z0-9]+/g, " ").trim().replace(/^(the|a|an) /, "");
const key = (t, q) => norm(t === "pin" ? q.place : t === "dingbat" ? (q.answers || [])[0] : t === "tune" ? `${q.track} ${q.artist}` : q.phrase || q.text);
const items = JSON.parse(fs.readFileSync(process.argv[2], "utf8"));
const live = {};
let n = 0;
for (const [i, q] of items.entries()) {
  const t = q.type;
  live[t] = live[t] || new Set((await call({ action: "bank_list", type: t })).questions.map((x) => norm(t === "pin" || t === "dingbat" || t === "tune" ? x.answer : x.text)));
  // iTunes often stores a tune under a longer title ("Song (feat. X) [Remastered]"), so a tune only needs its title to lead a live one
  const k = key(t, q), trackKey = t === "tune" ? norm(q.track) : "";
  if (!live[t].has(k) && !(trackKey && [...live[t]].some((x) => x.startsWith(trackKey)))) { n++; console.log(`${i}\t${t}\t${q.difficulty || ""}\t${q.text || q.phrase || q.place || q.track}`); }
}
console.log(n ? `${n} of ${items.length} not in the bank (duplicates): replace them and import again.` : `All ${items.length} are in the bank.`);
