// Local test relay for Let's Quiz (testing only, never deployed): serves this repo with common.js pointed at /api here,
// and /api forwards to the real quiz-api adding the host password, so the password never goes into a browser.
// The password is read from the file named by LQ_RELAY_PW (default: relay.pw beside this file; never commit one).
//   node tools/test-relay.mjs   → http://localhost:8790/host.html?quiz=<id>&bots=4&auto=0
// In the browser, put any dummy value in localStorage lq_host_pw so host.html doesn't bounce to the builder.
import http from 'node:http'; import fs from 'node:fs'; import path from 'node:path'; import url from 'node:url';
const HERE = path.dirname(url.fileURLToPath(import.meta.url)), ROOT = path.join(HERE, '..');
const PW = fs.readFileSync(process.env.LQ_RELAY_PW || path.join(HERE, 'relay.pw'), 'utf8').trim();
const UP = 'https://safcrtrfdzsnftghibot.supabase.co/functions/v1/quiz-api';
const TYPES = { '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.png': 'image/png', '.jpg': 'image/jpeg', '.svg': 'image/svg+xml', '.json': 'application/json', '.webmanifest': 'application/manifest+json', '.mp3': 'audio/mpeg' };
http.createServer(async (req, res) => {
  const u = new URL(req.url, 'http://x');
  if (u.pathname === '/api') {
    let b = ''; for await (const c of req) b += c;
    let j = {}; try { j = JSON.parse(b); } catch {}
    j.password = PW;
    for (let i = 0; i < 3; i++) {
      try {
        const r = await fetch(UP, { method: 'POST', headers: { 'content-type': 'application/json', apikey: req.headers.apikey || '', authorization: req.headers.authorization || '' }, body: JSON.stringify(j) });
        res.writeHead(r.status, { 'content-type': 'application/json' }); return res.end(await r.text());
      } catch (e) { if (i === 2) { res.writeHead(502, { 'content-type': 'application/json' }); return res.end(JSON.stringify({ error: 'relay: ' + e.message })); } await new Promise((r) => setTimeout(r, 800)); }
    }
  }
  let p = decodeURIComponent(u.pathname); if (p === '/') p = '/index.html';
  let f = path.join(ROOT, p); if (!fs.existsSync(f) && fs.existsSync(f + '.html')) f += '.html';
  if (!f.startsWith(path.normalize(ROOT)) || !fs.existsSync(f) || fs.statSync(f).isDirectory()) { res.writeHead(404); return res.end('not found'); }
  let body = fs.readFileSync(f);
  if (p.endsWith('/assets/common.js')) body = Buffer.from(String(body).replace("const API = SUPABASE_URL + '/functions/v1/quiz-api';", "const API = location.origin + '/api';"));
  res.writeHead(200, { 'content-type': TYPES[path.extname(f)] || 'application/octet-stream', 'cache-control': 'no-store' }); res.end(body);
}).listen(8790, () => console.log('relay on 8790'));
