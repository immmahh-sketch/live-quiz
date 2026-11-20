// Saves the Bridge of Lies warm-up quiz: node tools/save-bridge-warm.mjs [--week-test] [--save]   (host password in LQ_PASSWORD)
//   reads tools/bridge-warm-boards.json (from tools/build-bridge-warm.mjs); without --save it only prints what it would write.
//   --week-test puts settings.warmup.week = 5, so letsquiz.uk/warmup?c=TESTWARMUP&wk=5 can try it before it opens (remove it afterwards: run again without the flag).
//   The settings (bonus, forQuiz, next) are copied from the Box Clever warm-up 2f690664 so the weekly bonus keeps adding up towards the same hosted game.
import fs from 'node:fs'; import path from 'node:path';
const root = path.resolve(path.dirname(new URL(import.meta.url).pathname.replace(/^\/(\w:)/, '$1')), '..');
const API = 'https://safcrtrfdzsnftghibot.supabase.co/functions/v1/quiz-api', KEY = 'sb_publishable_RGaIB8W145BFCWzOxamQvA_7VIkTHMU', PW = process.env.LQ_PASSWORD;
if (!PW) { console.error('Set LQ_PASSWORD'); process.exit(1); }
const call = async (body) => { const r = await fetch(API, { method: 'POST', headers: { 'content-type': 'application/json', apikey: KEY, Authorization: 'Bearer ' + KEY }, body: JSON.stringify({ password: PW, ...body }) }); const j = await r.json(); if (!r.ok) throw new Error(j.error || r.status); return j; };
const FROM = '2026-11-21T05:00:00Z', UNTIL = '2026-11-27T17:00:00Z', TEMPLATE = '2f690664-7f95-4a34-8abc-6d4261363298', LAST = path.join(root, 'tools/bridge-warm-last.json');
const boards = JSON.parse(fs.readFileSync(path.join(root, 'tools/bridge-warm-boards.json'), 'utf8'));
const tpl = (await call({ action: 'get', id: TEMPLATE })).quiz.settings.warmup;
const warmup = { code: 'WARMUP', open: true, fun: true, replay: false, season: 's-bridge-2026-11-21', from: FROM, until: UNTIL, bonus: tpl.bonus, forQuiz: tpl.forQuiz, next: tpl.next, bots: 0, bridge: { rounds: boards }, ...(process.argv.includes('--week-test') ? { week: 5 } : {}) };
const settings = { warmup, share: false };
const questions = [{ id: 'q_bridge_info', type: 'slide', text: 'Bridge of Lies warm-up', body: 'Three bridges, played on the phone at letsquiz.uk/warmup. Boards are in settings.warmup.bridge.rounds.', time: 20, media: { kind: 'none' } }];
const last = fs.existsSync(LAST) ? JSON.parse(fs.readFileSync(LAST, 'utf8')) : {};
const quiz = { ...(last.id ? { id: last.id } : {}), title: 'Bridge of Lies Warm-up: three bridges, one score', settings, questions };
console.log(JSON.stringify({ ...quiz, settings: { warmup: { ...warmup, bridge: '[3 boards]' } }, questions: '[1 slide]' }, null, 1));
if (!process.argv.includes('--save')) { console.log('(not saved: add --save)'); process.exit(0); }
const r = await call({ action: 'save', quiz });
const id = r.quiz?.id || r.id; fs.writeFileSync(LAST, JSON.stringify({ id })); console.log('saved', id);
