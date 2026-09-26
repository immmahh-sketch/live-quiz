// Moves drop-the-pin bank items off maps players might not recognise. The map has no labels, so a
// close-up of Ukraine or Hertfordshire leaves people not even knowing which country or county they are
// looking at. A pin keeps its close-up only when the question names the country or county (or it is
// London, the UK nations, the USA, Australia or the North East, which this crowd knows by shape);
// otherwise it goes up one level: a foreign country to its continent, a US state to the USA, an
// English county to the UK. Also rewrites the region in the bank/topics source files.
// Usage: LQ_PASSWORD=... node tools/widen-pins.mjs [--apply]   (without --apply it only lists the moves)
import fs from "node:fs";
import path from "node:path";
const dir = path.dirname(new URL(import.meta.url).pathname.replace(/^\/([A-Z]:)/, "$1"));
const bankDir = path.join(dir, "..", "bank");
const API = "https://safcrtrfdzsnftghibot.supabase.co/functions/v1/quiz-api";
const call = async (body) => { const r = await fetch(API, { method: "POST", headers: { "Content-Type": "application/json", apikey: "sb_publishable_RGaIB8W145BFCWzOxamQvA_7VIkTHMU" }, body: JSON.stringify({ password: process.env.LQ_PASSWORD, ...body }) }); const j = await r.json(); if (j.error) throw new Error(j.error); return j; };
const apply = process.argv.includes("--apply");

// region shown on the map → [the wider map, words in the question that mean players know where they are]
const KEEP = new Set(["the United Kingdom", "World", "the United States", "Europe", "Greater London", "Scotland", "Asia", "Wales", "Ireland", "Africa", "South America", "Australia", "Northern Ireland", "Middle East", "North Atlantic", "Tyne and Wear", "Northumberland", "County Durham", "North America", "Oceania"]);
const WIDER = {
  France: ["Europe", "france french"], Italy: ["Europe", "italy italian"], Germany: ["Europe", "germany german"], Spain: ["Europe", "spain spanish costa balearic canary"],
  Greece: ["Europe", "greece greek"], Turkey: ["Europe", "turkey turkish"], Sweden: ["Europe", "sweden swedish"], Switzerland: ["Europe", "switzerland swiss"],
  Netherlands: ["Europe", "netherlands dutch holland"], Belgium: ["Europe", "belgium belgian"], Poland: ["Europe", "poland polish"], Denmark: ["Europe", "denmark danish jutland"],
  Austria: ["Europe", "austria austrian"], Romania: ["Europe", "romania romanian transylvania transylvanian"], Ukraine: ["Europe", "ukraine ukrainian"], "Bosnia and Herzegovina": ["Europe", "bosnia bosnian"],
  India: ["Asia", "india indian"], China: ["Asia", "china chinese"], Japan: ["Asia", "japan japanese"], Pakistan: ["Asia", "pakistan pakistani"],
  Egypt: ["Africa", "egypt egyptian"], Tunisia: ["Africa", "tunisia tunisian"], Sudan: ["Africa", "sudan sudanese"],
  Mexico: ["North America", "mexico mexican"], Canada: ["North America", "canada canadian"], Brazil: ["South America", "brazil brazilian"], "New Zealand": ["Oceania", "zealand kiwi"],
  Paris: ["Europe", "paris parisian"], Florida: ["USA", "florida"], California: ["USA", "california californian"], Massachusetts: ["USA", "massachusetts"],
  Merseyside: ["United Kingdom", "merseyside liverpool mersey"], "Greater Manchester": ["United Kingdom", "manchester salford"], "West Yorkshire": ["United Kingdom", "yorkshire leeds bradford calderdale halifax wakefield huddersfield"],
  "South Yorkshire": ["United Kingdom", "yorkshire sheffield barnsley rotherham doncaster"], "West Midlands county": ["United Kingdom", "birmingham coventry wolverhampton midlands"],
  Brighton: ["United Kingdom", "brighton"], "Brighton & Hove": ["United Kingdom", "brighton hove"], "East Sussex": ["United Kingdom", "sussex brighton"], "West Sussex": ["United Kingdom", "sussex"],
  Buckinghamshire: ["United Kingdom", "buckinghamshire bucks"], Hertfordshire: ["United Kingdom", "hertfordshire herts"], Essex: ["United Kingdom", "essex"], Kent: ["United Kingdom", "kent"],
  Dorset: ["United Kingdom", "dorset"], Cornwall: ["United Kingdom", "cornwall cornish"], Surrey: ["United Kingdom", "surrey"], Somerset: ["United Kingdom", "somerset"],
  Leicestershire: ["United Kingdom", "leicestershire leicester"], Oxfordshire: ["United Kingdom", "oxfordshire oxford"], Cheshire: ["United Kingdom", "cheshire chester"], Berkshire: ["United Kingdom", "berkshire"],
  Nottinghamshire: ["United Kingdom", "nottinghamshire nottingham sherwood"], Hampshire: ["United Kingdom", "hampshire"], Lancashire: ["United Kingdom", "lancashire"], Cumbria: ["United Kingdom", "cumbria lake district"],
  Cambridgeshire: ["United Kingdom", "cambridgeshire cambridge"], Lincolnshire: ["United Kingdom", "lincolnshire lincoln"], Devon: ["United Kingdom", "devon"], Staffordshire: ["United Kingdom", "staffordshire"],
  Northamptonshire: ["United Kingdom", "northamptonshire northampton"], Norfolk: ["United Kingdom", "norfolk"], "Isle of Wight": ["United Kingdom", "isle of wight"], Bedfordshire: ["United Kingdom", "bedfordshire bedford"],
  Warwickshire: ["United Kingdom", "warwickshire"],
};
const norm = (s) => ` ${String(s || "").toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/[^a-z0-9]+/g, " ")} `;
const names = (words) => { const w = words.split(" "); const out = []; for (let i = 0; i < w.length; i++) { out.push(w[i]); if (w[i] === "lake" || w[i] === "isle") { out.push(w.slice(i, i + (w[i] === "isle" ? 3 : 2)).join(" ")); } } return out; };

// where each place is: from the source files first (they carry lat/lon and sizeKm), plus a few written by hand
const src = new Map([[" gibraltar ", { lat: 36.14, lon: -5.35, sizeKm: 5 }], [" lhasa ", { lat: 29.65, lon: 91.11, sizeKm: 20 }]]);
const topicFiles = fs.readdirSync(path.join(bankDir, "topics")).filter((f) => f.endsWith(".json")).map((f) => path.join(bankDir, "topics", f));
const pinFiles = fs.readdirSync(bankDir).filter((f) => /^pin.*\.json$/.test(f)).map((f) => path.join(bankDir, f));
for (const f of [...topicFiles, ...pinFiles]) { let items; try { items = JSON.parse(fs.readFileSync(f, "utf8")); } catch { continue; } if (!Array.isArray(items)) continue; for (const it of items) if (it?.type === "pin" && it.place && isFinite(+it.lat)) src.set(norm(it.place), it); }

// every pin in the bank with its map, read straight from the database export (tools cannot see mapBounds via bank_list)
const rows = JSON.parse(fs.readFileSync(process.env.PINS || path.join(dir, "..", "..", "lqsql", "pins-rows.json"), "utf8"));
const patches = [], kept = [], lost = [];
for (const r of rows) {
  if (KEEP.has(r.region) || !r.region) continue;
  const rule = WIDER[r.region]; if (!rule) { lost.push(`${r.place} (${r.region}: no rule)`); continue; }
  const text = norm(r.text);
  if (names(rule[1]).some((w) => text.includes(` ${w} `))) { kept.push(`${r.region}: ${r.text}`); continue; }
  let lat, lon, sizeKm;
  const s = src.get(norm(r.place));
  if (r.bounds && r.pin) {
    const b = typeof r.bounds === "string" ? JSON.parse(r.bounds) : r.bounds, p = typeof r.pin === "string" ? JSON.parse(r.pin) : r.pin;
    lon = b.left + p.x * (b.right - b.left); lat = b.top - p.y * (b.top - b.bottom);
    sizeKm = 2 * (+r.rf) * 111.32 * Math.cos(lat * Math.PI / 180) * (b.right - b.left);
  } else if (s) { lat = +s.lat; lon = +s.lon; sizeKm = +s.sizeKm || 60; }
  else { lost.push(`${r.place} (${r.region}: no coordinates)`); continue; }
  if (s && isFinite(+s.sizeKm)) sizeKm = +s.sizeKm; // the writer's own size beats one worked back from the old map
  patches.push({ id: r.id, region: rule[0], lat: +lat.toFixed(4), lon: +lon.toFixed(4), sizeKm: Math.max(1, Math.round(sizeKm)), place: r.place, from: r.region });
}
console.log(`${patches.length} to widen, ${kept.length} kept (the question names where), ${lost.length} not handled`);
for (const p of patches) console.log(`  ${p.from} → ${p.region}: ${p.place} (${p.lat}, ${p.lon}, ${p.sizeKm} km)`);
if (lost.length) console.log("not handled:", lost.join("; "));
if (process.env.SHOWKEPT) console.log(kept.join("\n"));
if (!apply) process.exit(0);

// the source files, so a re-import never brings the close-up back
const moved = new Map(patches.map((p) => [norm(p.place), p]));
for (const f of [...topicFiles, ...pinFiles]) {
  const raw = fs.readFileSync(f, "utf8"); let items; try { items = JSON.parse(raw); } catch { continue; } if (!Array.isArray(items)) continue;
  let n = 0;
  for (const it of items) { const p = it?.type === "pin" && moved.get(norm(it.place)); if (p && it.region !== p.region) { it.region = p.region; n++; } }
  if (!n) continue;
  const oneLine = raw.startsWith("[\n{");
  fs.writeFileSync(f, oneLine ? "[\n" + items.map((q) => JSON.stringify(q)).join(",\n") + "\n]\n" : JSON.stringify(items, null, 1) + "\n");
  console.log(`${path.basename(f)}: ${n} regions widened`);
}
let changed = 0; const skipped = [];
for (let i = 0; i < patches.length; i += 50) { const r = await call({ action: "bank_repin", patches: patches.slice(i, i + 50) }); changed += r.changed; skipped.push(...r.skipped); }
console.log(`bank: ${changed} moved`); if (skipped.length) console.log("skipped:", skipped.join("; "));
