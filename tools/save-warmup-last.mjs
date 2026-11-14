// Saves tools/boxes-warmup-last.json (the reviewed warm-up) over an existing quiz, then shows what the player page will serve.
//   LQ_PASSWORD=<host password> node tools/save-warmup-last.mjs <quiz id>
import fs from 'node:fs'; import path from 'node:path'; import url from 'node:url';
const { api } = await import('./lq.mjs');
const here = path.dirname(url.fileURLToPath(import.meta.url)), id = process.argv[2];
if (!id) { console.log('give the quiz id to save over'); process.exit(1); }
const quiz = JSON.parse(fs.readFileSync(path.join(here, 'boxes-warmup-last.json'), 'utf8')); quiz.id = id;
const r = await api('save', { quiz }); console.log('saved', r.id || JSON.stringify(r).slice(0, 200));
const code = quiz.settings.warmup.code, o = await api('warmup_open', { code });
console.log(code, '->', o.closed ? 'closed' : 'open', o.nextOpens || '', o.title || (o.quiz && o.quiz.title) || '');
