// Where the natural-voice speech bank stands, what it has cost, and how many games of each kind are left to play:  node tools/voice-status.mjs
// Exit code 2 when the spend has reached 80% of the budget, or a kind of game is down to 5 or fewer (the text says which: NEED ...).
const URL = 'https://safcrtrfdzsnftghibot.supabase.co/functions/v1/quiz-api', KEY = 'sb_publishable_RGaIB8W145BFCWzOxamQvA_7VIkTHMU';
const call = async (body) => (await fetch(URL, { method: 'POST', headers: { 'content-type': 'application/json', apikey: KEY, Authorization: 'Bearer ' + KEY }, body: JSON.stringify(body) })).json();
const site = async (u) => (await fetch('https://letsquiz.uk/' + u + '?x=' + Date.now())).json();
const st = await call({ action: 'tts_status' });
const [bi, ri, bp, rp] = await Promise.all([site('tvbox/index.json'), site('bridge/index.json'), call({ action: 'pool_state', pool: 'BOX2P' }), call({ action: 'pool_state', pool: 'BRIDGE' })]);
const left = (idx, pool) => idx.games.filter((g) => !(pool.played || []).includes(g.id)).length;
const box = left(bi, bp), bridge = left(ri, rp);
const pct = Math.round((100 * st.total) / st.totalCap);
console.log(`Speech bank: ${st.stagesDone} of ${st.stagesTotal} steps done, ${st.kept} lines kept (${(st.bytes / 1e6).toFixed(1)} MB)`);
console.log(`Spend: ${st.total.toLocaleString()} characters of the ${st.totalCap.toLocaleString()} budget (${pct}%), about $${st.estCostUSD} so far. Today ${st.today.toLocaleString()} of ${st.dayCap.toLocaleString()}. Stopped: ${st.stopped || 'no'}`);
console.log(`Next: ${(st.nextStages || []).join('; ') || 'nothing, the plan is complete'}`);
console.log(`Games left to play: Box Clever ${box} of ${bi.games.length}, Bridge of Lies ${bridge} of ${ri.games.length}`);
let code = 0;
if (pct >= 80) { console.log(`WARNING: ${pct}% of the speech budget is used.`); code = 2; }
if (box <= 5) { console.log(`NEED 50 more Box Clever games (only ${box} left): node tools/build-tvbox.mjs --games 50 --from ${bi.games.length + 1}, then commit and push`); code = 2; }
if (bridge <= 5) { console.log(`NEED 50 more Bridge of Lies games (only ${bridge} left): write tools/bridge-src/part-NN.json, then node tools/build-bridge.mjs`); code = 2; }
process.exit(code);
