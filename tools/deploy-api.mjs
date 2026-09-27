// Deploys the quiz-api edge function safely: node tools/deploy-api.mjs   (needs LQ_PASSWORD for the smoke test)
// 1. bundles it with esbuild and parses the result with Node, which rejects what esbuild lets through (an invalid
//    regular expression once stopped the function from starting at all: every page showed "Could not reach the server");
// 2. deploys with the Supabase CLI;
// 3. calls the live function and fails loudly unless it answers.
import { execFileSync } from "node:child_process";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";

const root = path.resolve(path.dirname(new URL(import.meta.url).pathname.replace(/^\/(\w:)/, "$1")), "..");
const out = path.join(os.tmpdir(), "quiz-api-check.mjs");
const run = (cmd, args) => execFileSync(cmd, args, { cwd: root, stdio: "inherit", shell: process.platform === "win32" });

console.log("1/3 checking the code parses…");
run("npx", ["--yes", "esbuild", "supabase/functions/quiz-api/index.ts", "--loader:.ts=ts", "--format=esm", `--outfile=${out}`, "--log-level=warning"]);
run("node", ["--check", out]);
fs.rmSync(out, { force: true });

console.log("2/3 deploying…");
run("npx", ["supabase", "functions", "deploy", "quiz-api", "--project-ref", "safcrtrfdzsnftghibot", "--no-verify-jwt"]);

console.log("3/3 checking it starts…");
const KEY = "sb_publishable_RGaIB8W145BFCWzOxamQvA_7VIkTHMU";
let last = "";
for (let i = 0; i < 6; i++) {
  await new Promise((r) => setTimeout(r, 3000));
  try {
    const r = await fetch("https://safcrtrfdzsnftghibot.supabase.co/functions/v1/quiz-api", { method: "POST", headers: { "content-type": "application/json", apikey: KEY, Authorization: "Bearer " + KEY }, body: JSON.stringify({ action: "login", password: process.env.LQ_PASSWORD || "" }) });
    last = `${r.status} ${(await r.text()).slice(0, 200)}`;
    if (r.status === 200 || r.status === 401) { console.log("✓ live and answering:", last); process.exit(0); }
  } catch (e) { last = e.message; }
}
console.error("✗ THE FUNCTION IS NOT ANSWERING. The app is down until this is fixed. Last reply:", last);
process.exit(1);
