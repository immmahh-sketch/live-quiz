// Supabase Edge Function: quiz-api
//
// Everything the Live Quiz host portal needs from the server, behind one
// password (QUIZ_HOST_PASSWORD). The live game itself does not come
// through here — it runs over Realtime between the host screen and the
// phones — so this is the quiet part: storing quizzes, keeping pictures,
// judging typed answers with AI at the end of a question, and writing
// whole quizzes with AI when asked.
//
// Actions (all POST, JSON body {action, password, ...}):
//   login       — checks the password
//   list        — the host's quizzes
//   get         — one quiz, with its questions
//   save        — create or update a quiz
//   delete      — remove a quiz
//   upload      — store a picture (base64 in, public URL out)
//   check_text  — judge players' typed answers against the accepted ones
//   generate    — write questions on a topic, with pictures, using web search
//   verify      — fact-check questions with web search; verdict and note per question
//   more_wipeout — extra right answers for a Wipeout board, so it outnumbers the players
//   map         — a blank, label-free map of a country, region or continent
//   picture     — a photo of a named subject from Wikipedia / Commons, copied into our bucket
//   save_game   — record a finished game: scoreboard plus the full answer-by-answer report
//   games       — recent finished games (summaries)
//   game        — one finished game with its report
//
// Deploy with "Verify JWT" OFF — the browser only holds the publishable key.

import Anthropic from "npm:@anthropic-ai/sdk";

const SUPA_URL = Deno.env.get("SUPABASE_URL")!;
const SERVICE_KEY = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!;
const HOST_PW = Deno.env.get("QUIZ_HOST_PASSWORD") || "";
const ANTHROPIC_KEY = Deno.env.get("ANTHROPIC_API_KEY") || "";
const BUCKET = "quiz-media";
const UA = "LiveQuiz/1.0 (https://github.com/immmahh-sketch/live-quiz)";
// Models by job. Opus writes the craft types (wordplay and logic) where quality shows and
// no lookup is needed; Sonnet writes plain factual questions with web search and does the
// fact-checking; Haiku judges typed answers during games. "premium" puts everything on Opus.
const OPUS = "claude-opus-5", SONNET = "claude-sonnet-5", HAIKU = "claude-haiku-4-5-20251001";
const MODEL = OPUS;
const CRAFT_TYPES = ["club", "dingbat", "rhyme", "highlow", "smash", "wheel"];
function writerPlan(types: string[], premium: boolean) {
  const craft = types.length > 0 && types.every((t) => CRAFT_TYPES.includes(t));
  const tune = types.length > 0 && types.every((t) => t === "tune");
  return { model: premium || craft ? OPUS : SONNET, web: !craft && !tune, searches: premium ? 6 : 3 };
}
/** What a call cost, for the portal to add up. */
function usageOf(msg: Anthropic.Message, model: string) {
  const u: any = msg.usage || {};
  return { model, input: u.input_tokens || 0, output: u.output_tokens || 0, cacheRead: u.cache_read_input_tokens || 0, cacheWrite: u.cache_creation_input_tokens || 0, searches: u.server_tool_use?.web_search_requests || 0 };
}
const UUID_RE = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i;

const CORS = {
  "access-control-allow-origin": "*",
  "access-control-allow-headers": "authorization, apikey, content-type",
  "access-control-allow-methods": "POST, OPTIONS",
};
function json(body: unknown, status = 200) {
  return new Response(JSON.stringify(body), { status, headers: { ...CORS, "content-type": "application/json" } });
}

/** PostgREST with the service role. Bypasses RLS — never expose directly. */
async function rest(path: string, init: RequestInit = {}) {
  const r = await fetch(`${SUPA_URL}/rest/v1/${path}`, {
    ...init,
    headers: { apikey: SERVICE_KEY, Authorization: `Bearer ${SERVICE_KEY}`, "Content-Type": "application/json", ...(init.headers || {}) },
  });
  if (!r.ok) throw new Error(`REST ${path} -> ${r.status} ${await r.text()}`);
  const t = await r.text();
  return t ? JSON.parse(t) : null;
}

// ---------------------------------------------------------------- storage
function extFor(ct: string) {
  return ct.includes("png") ? "png" : ct.includes("webp") ? "webp" : ct.includes("gif") ? "gif" : "jpg";
}
async function storagePut(path: string, bytes: Uint8Array, contentType: string): Promise<string> {
  const r = await fetch(`${SUPA_URL}/storage/v1/object/${BUCKET}/${path}`, {
    method: "POST",
    headers: { apikey: SERVICE_KEY, Authorization: `Bearer ${SERVICE_KEY}`, "Content-Type": contentType, "x-upsert": "true" },
    body: bytes,
  });
  if (!r.ok) throw new Error(`storage put ${path} -> ${r.status} ${await r.text()}`);
  return `${SUPA_URL}/storage/v1/object/public/${BUCKET}/${path}`;
}
async function storageExists(path: string): Promise<string | null> {
  const url = `${SUPA_URL}/storage/v1/object/public/${BUCKET}/${path}`;
  const r = await fetch(url, { method: "HEAD" });
  return r.ok ? url : null;
}
/** Copies a picture from the web into our bucket, so a game never depends on someone else's hosting. */
async function copyImage(src: string, key: string): Promise<string | null> {
  try {
    const r = await fetch(src, { headers: { "user-agent": UA } });
    if (!r.ok) return null;
    const ct = (r.headers.get("content-type") || "").split(";")[0].trim();
    if (!ct.startsWith("image/") || ct.includes("svg")) return null;
    const bytes = new Uint8Array(await r.arrayBuffer());
    if (bytes.length < 1000 || bytes.length > 8_000_000) return null;
    return await storagePut(`${key}.${extFor(ct)}`, bytes, ct);
  } catch (e) {
    console.warn("copyImage failed", src, String(e));
    return null;
  }
}

// ---------------------------------------------------------------- Wikipedia / Commons pictures
//
// Three sources, tried in order, so the same subject does not always get the same photo:
//   1. every photograph in the English Wikipedia article (chosen at random)
//   2. a Wikimedia Commons search for the subject (chosen at random from the best matches)
//   3. the article's lead image (the old behaviour) as a last resort
// Pictures the quiz already uses are skipped, and each one is copied into our bucket.

interface Candidate { url: string; key: string; }
const BAD_NAME = /logo|icon|flag|map|coat|seal|emblem|crest|diagram|chart|graph|plot|scheme|signature|symbol|banner|badge|stamp|coin|wiki|ambox|edit|question|star|arrow|button|pictogram|silhouette|locator|orthographic|portrait|painting|drawing|engraving|illustration|lithograph|sketch|poster|cover|screenshot|page|skull|skeleton|anatomy|disease|x-ray|xray/i;
const STOP = new Set(["the", "and", "of", "a", "an", "in", "on", "at", "to", "for", "de", "la", "le", "dog", "cat", "bird", "city", "river", "mount", "lake", "island", "islands", "national", "park", "castle", "cathedral", "church", "bridge", "tower", "palace", "stadium", "football", "club", "united", "city"]);
/** Words of the subject that a file name should contain to count as being about it. */
function keyWords(title: string): string[] {
  const ws = title.toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/\(.*?\)/g, "").split(/[^a-z0-9]+/).filter((w) => w.length >= 3 && !STOP.has(w));
  return ws.length ? ws : title.toLowerCase().split(/[^a-z0-9]+/).filter((w) => w.length >= 3);
}
async function mw(api: string, params: Record<string, string>): Promise<any> {
  const u = `${api}?${new URLSearchParams({ ...params, format: "json" })}`;
  const r = await fetch(u, { headers: { "user-agent": UA } });
  if (!r.ok) return null;
  return r.json();
}
function candidatesFrom(data: any, words: string[] | null): Candidate[] {
  const out: Candidate[] = [];
  for (const p of Object.values(data?.query?.pages || {}) as any[]) {
    const ii = p?.imageinfo?.[0]; const name = String(p?.title || "");
    if (!ii || !/^image\/(jpeg|png)$/.test(ii.mime || "")) continue;
    const norm = name.toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "");
    // Article galleries and searches drift off the subject (a portrait that happens to
    // include a pug, a labrador in the pug article); the file name has to name the thing.
    if (words && (BAD_NAME.test(name) || !words.some((w) => norm.includes(w)))) continue;
    const w = +ii.width || 0, h = +ii.height || 0;
    if (w < 640 || h < 400 || w / h > 2.4 || h / w > 1.8) continue;
    const src = String(ii.thumburl || ii.url || "").split("?")[0];
    if (src) out.push({ url: src, key: name.toLowerCase() });
  }
  return out;
}
const IIPROPS = { prop: "imageinfo", iiprop: "url|mime|size", iiurlwidth: "1400" };
async function articlePhotos(title: string, words: string[]): Promise<Candidate[]> {
  const data = await mw("https://en.wikipedia.org/w/api.php", { action: "query", titles: title, redirects: "1", generator: "images", gimlimit: "50", ...IIPROPS }).catch(() => null);
  return candidatesFrom(data, words);
}
async function categoryPhotos(title: string, words: string[]): Promise<Candidate[]> {
  // Commons categories are usually the article title, sometimes its plural.
  for (const cat of [title, title + "s"]) {
    const data = await mw("https://commons.wikimedia.org/w/api.php", { action: "query", generator: "categorymembers", gcmtitle: "Category:" + cat, gcmtype: "file", gcmlimit: "50", ...IIPROPS }).catch(() => null);
    const cs = candidatesFrom(data, words);
    if (cs.length) return cs;
  }
  return [];
}
async function searchPhotos(title: string, words: string[]): Promise<Candidate[]> {
  const data = await mw("https://commons.wikimedia.org/w/api.php", { action: "query", generator: "search", gsrsearch: `${title} filetype:bitmap`, gsrnamespace: "6", gsrlimit: "30", ...IIPROPS }).catch(() => null);
  return candidatesFrom(data, words);
}
async function leadPhoto(title: string): Promise<Candidate[]> {
  const data = await mw("https://en.wikipedia.org/w/api.php", { action: "query", titles: title, redirects: "1", prop: "pageimages", piprop: "thumbnail|name", pithumbsize: "1400" }).catch(() => null);
  const p = (Object.values(data?.query?.pages || {}) as any[])[0];
  const src = String(p?.thumbnail?.source || "").split("?")[0];
  return src ? [{ url: src, key: String(p?.pageimage || src).toLowerCase() }] : [];
}
const pick = <T>(arr: T[]): T | undefined => arr.length ? arr[Math.floor(Math.random() * arr.length)] : undefined;

/** Is this Wikipedia subject a person? (Wikidata: instance of human.) People get their portrait, not a random photo that mentions them. */
async function isHuman(title: string): Promise<boolean> {
  try {
    const data = await mw("https://en.wikipedia.org/w/api.php", { action: "query", titles: title, redirects: "1", prop: "pageprops", ppprop: "wikibase_item" });
    const qid = (Object.values(data?.query?.pages || {}) as any[])[0]?.pageprops?.wikibase_item;
    if (!qid) return false;
    const claims = await mw("https://www.wikidata.org/w/api.php", { action: "wbgetclaims", entity: qid, property: "P31" });
    return (claims?.claims?.P31 || []).some((c: any) => c?.mainsnak?.datavalue?.value?.id === "Q5");
  } catch { return false; }
}

/** Finds a photo of the subject that the quiz is not already using, copies it into our bucket, and returns {url, source}. `portrait` forces the article's lead image (the right choice for a person). */
async function wikiPicture(title: string, used: Set<string>, portrait = false): Promise<{ url: string; source: string } | null> {
  const fresh = (cs: Candidate[]) => cs.filter((c) => !used.has(c.url) && !used.has(c.key));
  const words = keyWords(title);
  // Flags, emblems, logos, maps and the like have one canonical image: the article's own. The varied pool would hand back photos that merely mention them.
  const canonical = /^(flag|flags|coat of arms|emblem|seal|logo|map|national anthem|crest|badge|insignia)s? of /i.test(title) || /\b(flag|logo|coat of arms|emblem)\b/i.test(title);
  const person = portrait || canonical || await isHuman(title);
  const [article, category, search, lead] = person
    ? [[], [], [], await leadPhoto(title)]
    : await Promise.all([articlePhotos(title, words), categoryPhotos(title, words), searchPhotos(title, words), leadPhoto(title)]);
  const seen = new Set<string>();
  let pool = fresh([...article, ...category, ...search]).filter((c) => !seen.has(c.url) && seen.add(c.url));
  // The lead image is the one Wikipedia's editors chose, so it always stays in the running
  // when the pool is thin; it just stops being the only choice. For a person it is the only choice.
  if (pool.length < 3) pool = pool.concat(fresh(lead).filter((c) => !seen.has(c.url)));
  if (!pool.length) pool = lead; // better a repeat than no picture at all
  // Try up to three candidates in case one fails to download.
  for (let i = 0; i < 3 && pool.length; i++) {
    const c = pick(pool)!; pool = pool.filter((x) => x !== c);
    const url = await copyImage(c.url, `wiki/${slug(title)}-${crypto.randomUUID().slice(0, 8)}`);
    if (url) { used.add(c.url); used.add(c.key); return { url, source: c.url }; }
  }
  return null;
}
function slug(s: string) { return s.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "").slice(0, 50) || "pic"; }

/** A plain equirectangular world map for AI-written "drop the pin" questions, copied once. */
async function worldMap(): Promise<string | null> {
  const existing = await storageExists("maps/world.jpg");
  if (existing) return existing;
  const candidates = ["Equirectangular_projection_SW.jpg", "Equirectangular-projection.jpg"];
  for (const file of candidates) {
    const api = `https://commons.wikimedia.org/w/api.php?action=query&titles=File:${encodeURIComponent(file)}&prop=imageinfo&iiprop=url&iiurlwidth=2000&format=json`;
    const r = await fetch(api, { headers: { "user-agent": UA } }).catch(() => null);
    if (!r?.ok) continue;
    const pages = Object.values((await r.json())?.query?.pages || {}) as any[];
    const src = pages[0]?.imageinfo?.[0]?.thumburl?.split("?")[0];
    if (!src) continue;
    try {
      const img = await fetch(src, { headers: { "user-agent": UA } });
      if (!img.ok) continue;
      const bytes = new Uint8Array(await img.arrayBuffer());
      return await storagePut("maps/world.jpg", bytes, "image/jpeg");
    } catch { /* try the next */ }
  }
  return null;
}

// ---------------------------------------------------------------- location maps
//
// Wikipedia's "location maps" are blank, label-free maps of every country, region and
// continent, each with the maths to put a latitude/longitude on it (Module:Location
// map/data/<name>). Simple ones give a bounding box; others give x/y formulas in a
// tiny arithmetic language, which is evaluated here after a strict character check.

interface LocMap { region: string; name: string; url: string; project: (lat: number, lon: number) => { x: number; y: number } | null; kmPerWidth: (lat: number) => number; bounds?: { top: number; bottom: number; left: number; right: number }; }
const MAP_ALIASES: Record<string, string> = { uk: "United Kingdom", "great britain": "United Kingdom", britain: "United Kingdom", england: "United Kingdom", scotland: "Scotland", wales: "Wales", us: "USA", usa: "USA", "united states": "USA", "united states of america": "USA", america: "USA", world: "World", earth: "World", globe: "World", "the world": "World", holland: "Netherlands", "czech republic": "Czech Republic", "south korea": "South Korea", "north korea": "North Korea", ireland: "Ireland", "republic of ireland": "Ireland", "northern ireland": "Northern Ireland", uae: "United Arab Emirates", london: "United Kingdom Greater London", "greater london": "United Kingdom Greater London" };
const SAFE_EXPR = /^[\s\d.+\-*/^()<>=,$]*$/;
function compileExpr(src: string): ((lat: number, lon: number) => number) | null {
  let s = src.replace(/\s+/g, " ").trim();
  // Strip the maths words, check nothing else is left, then put them back as Math calls.
  const words = ["cos", "sin", "tan", "acos", "asin", "atan", "sqrt", "abs", "exp", "log", "pi"];
  const stripped = s.replace(new RegExp(`\\b(${words.join("|")})\\b`, "g"), "");
  if (!SAFE_EXPR.test(stripped) || s.length > 2000) return null;
  s = s.replace(/\$1/g, "lat").replace(/\$2/g, "lon").replace(/\bpi\b/g, "Math.PI").replace(/\^/g, "**");
  for (const w of words) if (w !== "pi") s = s.replace(new RegExp(`\\b${w}\\(`, "g"), `Math.${w}(`);
  s = s.replace(/([^<>=!])=([^=])/g, "$1==$2"); // Lua's single '=' comparisons, if any
  try {
    const f = new Function("lat", "lon", `"use strict"; return (${s});`) as (lat: number, lon: number) => number;
    const test = f(45, 10); if (!isFinite(+test)) return null;
    return f;
  } catch { return null; }
}
const mapCache = new Map<string, LocMap | null>();
async function locationMap(regionIn: string): Promise<LocMap | null> {
  const key = String(regionIn || "").trim().replace(/\s+/g, " ");
  const region = MAP_ALIASES[key.toLowerCase()] || key;
  if (!region) return null;
  if (mapCache.has(region)) return mapCache.get(region)!;
  const build = async (): Promise<LocMap | null> => {
    if (region === "World") {
      const url = await worldMap(); if (!url) return null;
      return { region, name: "World", url, project: (lat, lon) => ({ x: (lon + 180) / 360, y: (90 - lat) / 180 }), kmPerWidth: () => 40075, bounds: { top: 90, bottom: -90, left: -180, right: 180 } };
    }
    // Some modules are just a pointer to another ("return require [[Module:Location map/data/UK Scotland]]"): follow up to two.
    let title = "Module:Location map/data/" + region, src = "";
    for (let hop = 0; hop < 3; hop++) {
      const data = await mw("https://en.wikipedia.org/w/api.php", { action: "query", prop: "revisions", rvprop: "content", rvslots: "main", formatversion: "2", redirects: "1", titles: title }).catch(() => null);
      src = data?.query?.pages?.[0]?.revisions?.[0]?.slots?.main?.content || "";
      const next = src.length < 300 ? src.match(/require\s*\(?\s*(?:\[\[|["'])(Module:Location map\/data\/[^\]"']+)/) : null;
      if (!next) break; title = next[1];
    }
    if (!src) return null;
    const num = (k: string) => { const m = src.match(new RegExp(`\\b${k}\\s*=\\s*(-?[\\d.]+)`)); return m ? +m[1] : NaN; };
    const str = (k: string) => { const m = src.match(new RegExp(`\\b${k}\\s*=\\s*'([^']+)'`)) || src.match(new RegExp(`\\b${k}\\s*=\\s*"([^"]+)"`)); return m ? m[1] : ""; };
    const image = str("image"); if (!image) return null;
    let project: LocMap["project"]; let bounds: LocMap["bounds"];
    const top = num("top"), bottom = num("bottom"), left = num("left"), right = num("right");
    if ([top, bottom, left, right].every(isFinite)) {
      bounds = { top, bottom, left, right };
      project = (lat, lon) => ({ x: (lon - left) / (right - left), y: (top - lat) / (top - bottom) });
    } else {
      const fx = compileExpr(str("x")), fy = compileExpr(str("y"));
      if (!fx || !fy) return null;
      project = (lat, lon) => { const x = fx(lat, lon) / 100, y = fy(lat, lon) / 100; return isFinite(x) && isFinite(y) ? { x, y } : null; };
    }
    const kmPerWidth = (lat: number) => { const a = project(lat, 0), b = project(lat, 1); const dx = a && b ? Math.abs(b.x - a.x) : 0; return dx > 0 ? (111.32 * Math.cos(lat * Math.PI / 180)) / dx : 40075; };
    // The map itself: Commons renders the SVG to a PNG at the width asked for.
    const slugName = slug(region);
    let url = await storageExists(`maps/${slugName}.png`);
    if (!url) {
      const info = await mw("https://commons.wikimedia.org/w/api.php", { action: "query", titles: "File:" + image, prop: "imageinfo", iiprop: "url|mime", iiurlwidth: "1600" }).catch(() => null);
      const ii = (Object.values(info?.query?.pages || {}) as any[])[0]?.imageinfo?.[0];
      const thumb = String(ii?.thumburl || "").split("?")[0]; if (!thumb) return null;
      try {
        const r = await fetch(thumb, { headers: { "user-agent": UA } }); if (!r.ok) return null;
        const bytes = new Uint8Array(await r.arrayBuffer()); if (bytes.length < 1000) return null;
        url = await storagePut(`maps/${slugName}.png`, bytes, "image/png");
      } catch { return null; }
    }
    return { region, name: str("name") || region, url, project, kmPerWidth, bounds };
  };
  let m = await build().catch(() => null);
  // Wikipedia files UK counties and cities as "United Kingdom <name>" (Tyne and Wear, Cornwall, Greater London…).
  if (!m && region !== "World" && !/^United Kingdom /.test(region)) m = await locationMap("United Kingdom " + region);
  mapCache.set(region, m);
  return m;
}

// ---------------------------------------------------------------- Claude
function anthropic() {
  if (!ANTHROPIC_KEY) throw new Error("ANTHROPIC_API_KEY is not set on the server.");
  return new Anthropic({ apiKey: ANTHROPIC_KEY });
}
function textOf(msg: Anthropic.Message): string {
  return msg.content.filter((b): b is Anthropic.TextBlock => b.type === "text").map((b) => b.text).join("\n");
}
function extractJson(text: string): any {
  const fenced = text.match(/```(?:json)?\s*([\s\S]*?)```/);
  const body = fenced ? fenced[1] : text;
  const start = body.indexOf("{"), end = body.lastIndexOf("}");
  if (start < 0 || end < start) throw new Error("The AI did not return JSON.");
  return JSON.parse(body.slice(start, end + 1));
}
/** Runs a request to completion, resuming if a server tool pauses the turn. */
async function ask(client: Anthropic, params: Anthropic.MessageCreateParamsNonStreaming): Promise<Anthropic.Message> {
  const messages = [...params.messages];
  for (let i = 0; i < 8; i++) {
    const msg = await client.messages.stream({ ...params, messages }).finalMessage();
    if (msg.stop_reason === "pause_turn") { messages.push({ role: "assistant", content: msg.content }); continue; }
    if (msg.stop_reason === "refusal") throw new Error("The AI declined that request.");
    return msg;
  }
  throw new Error("The AI kept pausing. Try again.");
}

// ---------------------------------------------------------------- typed-answer judging
function norm(s: string) {
  return String(s || "").toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "")
    .replace(/&/g, " and ").replace(/[^a-z0-9]+/g, " ").trim().replace(/^(the|a|an) /, "");
}
function lev(a: string, b: string) {
  if (a === b) return 0; if (!a.length) return b.length; if (!b.length) return a.length;
  let prev = Array.from({ length: b.length + 1 }, (_, i) => i);
  for (let i = 1; i <= a.length; i++) {
    const cur = [i];
    for (let j = 1; j <= b.length; j++) cur[j] = Math.min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1));
    prev = cur;
  }
  return prev[b.length];
}
function sim(a: string, b: string) { return 1 - lev(a, b) / Math.max(a.length, b.length, 1); }
function localVerdict(answer: string, accepted: string[]): "right" | "wrong" | "unsure" {
  const n = norm(answer);
  if (!n) return "wrong";
  for (const acc of accepted) {
    const m = norm(acc);
    if (!m) continue;
    if (n === m) return "right";
    if (m.length >= 4 && sim(n, m) >= 0.85) return "right";
  }
  return "unsure";
}
function fuzzyVerdict(answer: string, accepted: string[]): boolean {
  const n = norm(answer);
  return accepted.some((acc) => { const m = norm(acc); return m && (sim(n, m) >= 0.72 || (m.length >= 5 && n.includes(m))); });
}

/** Answer Smash: the longest run of letters that ends the first answer and starts the second. Mirrors the portal's copy. */
function smashOf(a: string, b: string): { smash: string; overlap: number } {
  const letters = (s: string) => s.toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/[^a-z0-9]/g, "");
  const la = letters(a), lb = letters(b);
  let n = 0;
  for (let k = Math.min(la.length - 1, lb.length - 1); k >= 1; k--) if (la.slice(-k) === lb.slice(0, k)) { n = k; break; }
  if (!n) return { smash: "", overlap: 0 };
  let seen = 0, i = 0;
  while (i < b.length && seen < n) { if (/[a-z0-9]/i.test(b[i].normalize("NFD")[0])) seen++; i++; }
  return { smash: a.trimEnd() + b.slice(i), overlap: n };
}

const JUDGE_SYSTEM = `You are the adjudicator for a live pub quiz. Players typed their answers on a phone in a hurry. Decide whether each typed answer should be accepted as correct against the accepted answers for the question.

Accept: misspellings and typos, any capitalisation, missing or extra "the"/"a", abbreviations and common short forms, initials with a surname, alternative names that clearly refer to the same thing (NYC for New York City, Bobby Charlton for Sir Bobby Charlton, "1st" for "first"), the answer plus extra correct detail, and numbers written as words or digits. Where the question asks for a surname or a single word, a fuller correct answer is still right.

Reject: a different thing, an answer that hedges between two or more candidates, an answer too vague to identify the thing asked for, or one that only shares a word with the accepted answer.

Reply with JSON only, no commentary: {"verdicts":[{"id":"<id>","correct":true|false}]}`;

async function checkText(question: string, accepted: string[], answers: { id: string; text: string }[]) {
  const results: Record<string, { correct: boolean; how: string }> = {};
  const pending: { id: string; text: string }[] = [];
  for (const a of answers) {
    const v = localVerdict(a.text, accepted);
    if (v === "unsure") pending.push(a);
    else results[a.id] = { correct: v === "right", how: "match" };
  }
  let mode = "match";
  if (pending.length && ANTHROPIC_KEY) {
    try {
      const msg = await ask(anthropic(), {
        model: HAIKU,
        max_tokens: 4000,
        system: JUDGE_SYSTEM,
        messages: [{ role: "user", content: JSON.stringify({ question, accepted_answers: accepted, player_answers: pending }) }],
      });
      const out = extractJson(textOf(msg));
      for (const v of out?.verdicts || []) {
        if (typeof v?.id === "string" && typeof v?.correct === "boolean" && pending.some((p) => p.id === v.id)) {
          results[v.id] = { correct: v.correct, how: "ai" };
        }
      }
      mode = "ai";
    } catch (e) {
      console.error("AI judge failed, falling back to fuzzy match:", String(e));
      mode = "fuzzy";
    }
  } else if (pending.length) {
    mode = "fuzzy";
  }
  for (const p of pending) if (!results[p.id]) results[p.id] = { correct: fuzzyVerdict(p.text, accepted), how: "fuzzy" };
  return { results, mode };
}

// ---------------------------------------------------------------- AI quiz writing
// 20 Questions: the same yes/no tree as assets/common.js (TWENTY_KINDS / TWENTY_QS). Keep the two in step.
const TWENTY_KINDS: [string, string][] = [["person","Is it a person?"],["character","Is it a fictional character?"],["animal","Is it an animal?"],["place","Is it a place?"],["food","Is it a food or drink?"],["object","Is it an object?"],["title","Is it a film, TV show, book or song?"],["brand","Is it a brand or company?"]];
const TWENTY_TREE: Record<string, [string, string][]> = {"person":[["p_man","Is it a man?"],["p_woman","Is it a woman?"],["p_alive","Are they alive?"],["p_over50","Are they over 50? (Or were they, when they died?)"],["p_over70","Are they over 70?"],["p_under30","Are they under 30?"],["p_history","Did they live before 1900?"],["p_british","Are they British?"],["p_american","Are they American?"],["p_irish","Are they Irish?"],["p_knighted","Have they been knighted or made a dame?"],["p_english","Are they English?"],["p_scottish","Are they Scottish?"],["p_welsh","Are they Welsh?"],["p_northeast","Are they from the North East?"],["p_north","Are they from the north of England?"],["p_london","Are they from London?"],["p_music","Are they a singer or musician?"],["p_actor","Are they an actor?"],["p_sport","Are they a sports star?"],["p_tv","Are they a TV presenter or personality?"],["p_comedy","Are they a comedian?"],["p_politics","Are they a politician or leader?"],["p_royal","Are they royal?"],["p_writer","Are they a writer?"],["p_science","Are they a scientist or inventor?"],["p_business","Are they a business person?"],["p_hero","Are they famous for bravery or a daring feat?"],["p_b1970","Were they famous before 1970?"],["p_b1980","Were they famous before 1980?"],["p_b1990","Were they famous before 1990?"],["p_b2000","Were they famous before 2000?"],["p_b2010","Were they famous before 2010?"],["p_band","Have they been in a band or group?"],["p_boyband","Were they in a boy band or girl group?"],["p_frontman","Were they the main singer of their band?"],["p_solo","Have they had hits as a solo artist?"],["p_number1","Have they had a UK number one?"],["p_christmas1","Have they had a Christmas number one?"],["p_songwriter","Do they write their own songs?"],["p_instrument","Do they play guitar or piano on stage?"],["p_pop","Are they mainly a pop act?"],["p_rock","Are they mainly rock or indie?"],["p_rap","Are they a rapper or grime artist?"],["p_soul","Are they mainly soul, R&B or Motown?"],["p_dance","Are they mainly dance or electronic?"],["p_talent","Did they find fame on a TV talent show?"],["p_judge","Have they been a judge on a TV talent show?"],["p_acted","Have they also acted in films or TV dramas?"],["p_brit","Have they won a Brit Award?"],["p_grammy","Have they won a Grammy?"],["p_glasto","Have they headlined Glastonbury?"],["p_active","Are they still performing?"],["p_bondtheme","Have they sung a James Bond theme?"],["p_eurovision","Have they sung at Eurovision?"],["p_xfactorwin","Did they win The X Factor?"],["p_takethat","Were they in Take That?"],["p_westlife","Were they in Westlife?"],["p_boyzone","Were they in Boyzone?"],["p_1d","Were they in One Direction?"],["p_busted","Were they in Busted or McFly?"],["p_spice","Were they in the Spice Girls?"],["p_girlsaloud","Were they in Girls Aloud?"],["p_littlemix","Were they in Little Mix?"],["p_sugababes","Were they in the Sugababes?"],["p_steps","Were they in Steps?"],["p_beatles","Were they in the Beatles?"],["p_stones","Were they in the Rolling Stones?"],["p_queenband","Were they in Queen?"],["p_oasis","Were they in Oasis?"],["p_police","Were they in the Police?"],["p_coldplay","Were they in Coldplay?"],["p_u2","Were they in U2?"],["p_abba","Were they in ABBA?"],["p_arctic","Were they in Arctic Monkeys?"],["p_direstraits","Were they in Dire Straits?"],["p_hollywood","Have they starred in Hollywood films?"],["p_oscar","Have they won an Oscar?"],["p_soap","Have they been in a soap?"],["p_sitcom","Have they starred in a sitcom?"],["p_funny","Are they best known for comedy roles?"],["p_action","Are they known for action films?"],["p_bond","Have they been in a James Bond film?"],["p_superhero","Have they played a superhero?"],["p_potter","Have they been in a Harry Potter film?"],["p_whoactor","Have they been in Doctor Who?"],["p_voice","Have they voiced an animated character?"],["p_sang","Have they sung in a musical film or show?"],["p_period","Are they known for costume or period dramas?"],["p_stage","Are they known for theatre and Shakespeare?"],["p_corrie","Have they been in Coronation Street?"],["p_eastenders","Have they been in EastEnders?"],["p_emmerdale","Have they been in Emmerdale?"],["p_hollyoaks","Have they been in Hollyoaks?"],["p_marvel","Have they been in a Marvel film?"],["p_starwars","Have they been in a Star Wars film?"],["p_football","Are they a footballer?"],["p_cricket","Are they a cricketer?"],["p_tennis","Do they play tennis?"],["p_rugby","Do they play rugby?"],["p_athletics","Are they an athlete (running, jumping or throwing)?"],["p_boxing","Are they a boxer or fighter?"],["p_motor","Are they a racing driver?"],["p_golf","Are they a golfer?"],["p_cycling","Are they a cyclist?"],["p_swim","Are they a swimmer or diver?"],["p_cue","Do they play darts or snooker?"],["p_country","Have they represented their country?"],["p_captain","Have they captained their country?"],["p_olympic","Have they won an Olympic medal?"],["p_world","Have they been world champion or won a World Cup?"],["p_spoty","Have they won BBC Sports Personality of the Year?"],["p_retired","Have they retired from playing?"],["p_pundit","Are they a TV pundit or commentator?"],["p_manager","Have they been a manager or coach?"],["p_toon","Have they played for Newcastle?"],["p_mackem","Have they played for Sunderland?"],["p_prem","Have they played in the Premier League?"],["p_manutd","Have they played for Manchester United?"],["p_liverpool","Have they played for Liverpool?"],["p_striker","Are they a striker?"],["p_keeper","Are they a goalkeeper?"],["p_arsenal","Have they played for Arsenal?"],["p_chelsea","Have they played for Chelsea?"],["p_mancity","Have they played for Manchester City?"],["p_spurs","Have they played for Spurs?"],["p_everton","Have they played for Everton?"],["p_boro","Have they played for Middlesbrough?"],["p_leeds","Have they played for Leeds?"],["p_abroad","Have they played for a club abroad?"],["p_ballon","Have they won the Ballon d'Or?"],["p_reality","Did they find fame on reality TV?"],["p_gameshow","Have they hosted a quiz or game show?"],["p_chat","Have they hosted a chat show?"],["p_saturday","Have they fronted Saturday-night TV?"],["p_cook","Are they a TV cook or chef?"],["p_nature","Do they present nature or travel shows?"],["p_news","Are they a newsreader or journalist?"],["p_duo","Are they half of a presenting double act?"],["p_strictly","Have they been a contestant on Strictly?"],["p_jungle","Have they been a contestant on I'm a Celebrity?"],["p_daytime","Have they presented breakfast or daytime TV?"],["p_kidstv","Did they start on children's TV?"],["p_takeaway","Have they presented Saturday Night Takeaway?"],["p_imceleb","Have they presented I'm a Celebrity?"],["p_bgt","Have they hosted or judged Britain's Got Talent?"],["p_bakeoff","Have they presented or judged Bake Off?"],["p_topgear","Have they presented Top Gear?"],["p_bluepeter","Have they presented Blue Peter?"],["p_thismorning","Have they presented This Morning?"],["p_standup","Are they a stand-up comic?"],["p_panel","Are they a regular on TV panel shows?"],["p_csitcom","Have they starred in a sitcom?"],["p_double","Are they part of a double act?"],["p_characters","Are they known for playing comic characters?"],["p_silent","Are they known for visual or silent comedy?"],["p_cfilm","Have they starred in films?"],["p_blackadder","Were they in Blackadder?"],["p_python","Were they in Monty Python?"],["p_pm","Have they been Prime Minister?"],["p_president","Have they been a president?"],["p_mp","Have they been a UK MP?"],["p_labour","Are they Labour?"],["p_tory","Are they Conservative?"],["p_inoffice","Are they in office now?"],["p_wartime","Did they lead a country in a war?"],["p_resigned","Did they resign or get forced out?"],["p_monarch","Have they been king or queen?"],["p_heir","Are they in line to the throne?"],["p_marriedin","Did they marry into the royal family?"],["p_tudor","Were they a Tudor?"],["p_divorced","Have they been divorced?"],["p_kidsbooks","Do they write children's books?"],["p_crime","Do they write crime or thrillers?"],["p_poet","Are they a poet?"],["p_plays","Did they write plays?"],["p_fantasy","Do they write fantasy or science fiction?"],["p_filmed","Have their books been made into films?"],["p_bookseries","Did they write a famous series of books?"],["p_school","Are their books studied at school?"],["p_invented","Did they invent something we still use?"],["p_theory","Are they famous for a theory or law?"],["p_space","Are they linked to space or the stars?"],["p_medicine","Are they linked to medicine?"],["p_nobel","Did they win a Nobel Prize?"],["p_tvsci","Do they present science on TV?"],["p_billion","Are they a billionaire?"],["p_techco","Did they found a tech company?"],["p_shopco","Did they found a shop or high-street brand?"],["p_den","Have they been on Dragons' Den or The Apprentice?"],["p_rocket","Have they run a space company?"],["p_sea","Did their feat happen at sea?"],["p_war","Are they linked to a war?"],["p_rescue","Did they save lives?"],["p_explore","Were they an explorer or adventurer?"],["p_astro","Have they been into space?"],["p_nurse","Were they a nurse or doctor?"]],"character":[["c_human","Are they human?"],["c_animal","Are they an animal?"],["c_male","Are they male?"],["c_female","Are they female?"],["c_hero","Are they a goodie?"],["c_villain","Are they a baddie?"],["c_kids","Are they mainly for children?"],["c_animated","Are they animated, a cartoon or a puppet?"],["c_powers","Do they have special powers or magic?"],["c_british","Are they British?"],["c_american","Are they American?"],["c_old","Did they first appear before 1980?"],["c_hat","Do they usually wear a hat?"],["c_royal","Are they a king, queen, prince or princess?"],["c_christmas","Are they linked to Christmas?"],["c_school","Do they go to school?"],["c_detective","Are they a detective or spy?"],["c_film","Are they best known from films?"],["c_tv","Are they best known from TV?"],["c_book","Did they start in a book?"],["c_game","Are they from a video game?"],["c_comic","Did they start in comics?"],["c_franchise","Have they been in more than three films?"],["c_starwars","Are they from Star Wars?"],["c_potter","Are they from Harry Potter?"],["c_soapc","Are they from a soap?"],["c_sitcomc","Are they from a sitcom?"],["c_classic","Are they from a book over 100 years old?"],["c_bookseries","Are they in a series of books?"],["c_bear","Are they a bear?"],["c_dog","Are they a dog?"],["c_cat","Are they a cat?"],["c_mouse","Are they a mouse or rat?"],["c_pig","Are they a pig?"],["c_bird","Are they a bird?"],["c_rabbit","Are they a rabbit?"],["c_lion","Are they a lion?"],["c_talks","Can they talk?"],["c_clothes","Do they wear clothes?"],["c_disney","Are they a Disney character?"],["c_pixar","Are they from Pixar?"],["c_simpsons","Are they from The Simpsons?"],["c_stopmotion","Are they stop-motion or a puppet?"],["c_super","Are they a superhero?"],["c_marvel","Are they from Marvel?"],["c_mask","Do they wear a mask?"],["c_fly","Can they fly?"],["c_wizard","Do they cast spells?"],["c_alien","Are they from another planet?"],["c_toystory","Are they from Toy Story?"],["c_lionking","Are they from The Lion King?"],["c_frozen","Are they from Frozen?"],["c_muppet","Are they a Muppet?"],["c_wallace","Are they from Wallace and Gromit?"],["c_dc","Are they from DC Comics?"]],"animal":[["a_mammal","Is it a mammal?"],["a_bird","Is it a bird?"],["a_reptile","Is it a reptile?"],["a_fish","Is it a fish?"],["a_insect","Is it an insect, spider or bug?"],["a_amphibian","Is it a frog, toad or newt?"],["a_pet","Is it a common pet?"],["a_farm","Is it a farm animal?"],["a_wildbritain","Is it found wild in Britain?"],["a_zoo","Would you see it at a zoo?"],["a_bigger","Is it bigger than a person?"],["a_small","Is it smaller than a cat?"],["a_fourlegs","Does it have four legs?"],["a_fly","Can it fly?"],["a_water","Does it live in or around water?"],["a_sea","Does it live in the sea?"],["a_meat","Does it eat meat?"],["a_plants","Does it eat plants?"],["a_danger","Can it be dangerous to people?"],["a_venom","Is it venomous or poisonous?"],["a_stripes","Does it have stripes or spots?"],["a_blackwhite","Is it black and white?"],["a_horns","Does it have horns, antlers or tusks?"],["a_tail","Does it have a long tail?"],["a_herd","Does it live in a herd, pack or colony?"],["a_eggs","Does it lay eggs?"],["a_nocturnal","Is it mostly active at night?"],["a_hibernate","Does it hibernate?"],["a_fast","Is it famous for being fast?"],["a_endangered","Is it endangered?"],["a_eat","Do people in Britain eat it?"],["a_africa","Is it found in Africa?"],["a_asia","Is it found in Asia?"],["a_australia","Is it found in Australia?"],["a_americas","Is it found in the Americas?"],["a_catfam","Is it in the cat family?"],["a_dogfam","Is it in the dog family?"],["a_hooves","Does it have hooves?"],["a_ape","Is it a monkey or ape?"],["a_rodent","Is it a rodent?"],["a_marsupial","Is it a marsupial?"],["a_whale","Is it a whale, dolphin or seal?"],["a_bear","Is it a bear?"],["a_flightless","Is it a bird that can't fly?"],["a_prey","Is it a bird of prey?"],["a_garden","Would you see it in a British garden?"],["a_swims","Does it swim?"],["a_talkbird","Can it copy speech?"],["a_colourful","Is it brightly coloured?"],["a_sting","Can it sting?"],["a_eightlegs","Does it have eight legs?"],["a_snake","Is it a snake?"],["a_shell","Does it have a shell?"]],"place":[["pl_uk","Is it in the UK?"],["pl_europe","Is it in Europe?"],["pl_americas","Is it in the Americas?"],["pl_asia","Is it in Asia?"],["pl_africa","Is it in Africa?"],["pl_oceania","Is it in Australia or the Pacific?"],["pl_england","Is it in England?"],["pl_scotland","Is it in Scotland?"],["pl_wales","Is it in Wales?"],["pl_ni","Is it in Northern Ireland?"],["pl_northeast","Is it in the North East?"],["pl_north","Is it in the north of England?"],["pl_london","Is it in London?"],["pl_france","Is it in France?"],["pl_italy","Is it in Italy?"],["pl_spain","Is it in Spain?"],["pl_germany","Is it in Germany?"],["pl_usa","Is it in the USA?"],["pl_canada","Is it in Canada?"],["pl_nyc","Is it in New York?"],["pl_tyneside","Is it on Tyneside?"],["pl_sunderland","Is it in Sunderland?"],["pl_northumberland","Is it in Northumberland?"],["pl_durham","Is it in County Durham?"],["pl_country","Is it a country?"],["pl_city","Is it a city or town?"],["pl_region","Is it a region, county or state?"],["pl_building","Is it a building or landmark?"],["pl_natural","Is it a natural feature?"],["pl_island","Is it an island?"],["pl_capital","Is it a capital city?"],["pl_bigpop","Do more than a million people live there?"],["pl_english","Do they speak English there?"],["pl_olympics","Has it hosted the Olympics?"],["pl_club","Is it home to a famous football club?"],["pl_religious","Is it a church, cathedral or temple?"],["pl_castle","Is it a castle or palace?"],["pl_stadium","Is it a stadium?"],["pl_bridge","Is it a bridge?"],["pl_statue","Is it a statue or sculpture?"],["pl_tall","Is it taller than 100 metres?"],["pl_old","Is it over 500 years old?"],["pl_mountain","Is it a mountain or hill?"],["pl_waterfeat","Is it a river, lake, waterfall or sea?"],["pl_beach","Is it a beach or stretch of coast?"],["pl_forest","Is it a forest, park or moor?"],["pl_sea","Is it by the sea?"],["pl_river","Is it on a river?"],["pl_hot","Is it usually hot there?"],["pl_snow","Does it often get snow?"],["pl_tourist","Is it a big tourist attraction?"],["pl_heritage","Is it (or is it home to) a World Heritage Site?"]],"food":[["f_drink","Is it a drink?"],["f_alcohol","Does it contain alcohol?"],["f_beer","Is it a beer, lager or cider?"],["f_spirit","Is it a spirit?"],["f_wine","Is it wine or champagne?"],["f_cocktail","Is it a cocktail?"],["f_fizzy","Is it fizzy?"],["f_hotdrink","Is it drunk hot?"],["f_milk","Is it made with milk?"],["f_juice","Is it a fruit juice?"],["f_caffeine","Does it contain caffeine?"],["f_sweet","Is it sweet?"],["f_hot","Is it usually served hot?"],["f_fruitveg","Is it a fruit or vegetable?"],["f_fruit","Is it a fruit?"],["f_tropical","Does it grow in hot countries?"],["f_raw","Is it usually eaten raw?"],["f_meat","Does it contain meat or fish?"],["f_fish","Does it contain fish or seafood?"],["f_pork","Does it contain pork?"],["f_beef","Does it contain beef?"],["f_chicken","Does it contain chicken?"],["f_egg","Does it contain egg?"],["f_dairy","Does it contain dairy?"],["f_cheese","Does it contain cheese?"],["f_chocolate","Does it contain chocolate?"],["f_cake","Is it a cake, biscuit or pudding?"],["f_pastry","Is it made with pastry?"],["f_bread","Is it bread or served in bread?"],["f_potato","Is it made from potato?"],["f_rice","Does it contain rice or pasta?"],["f_fried","Is it fried?"],["f_hands","Do you eat it with your hands?"],["f_takeaway","Is it a takeaway favourite?"],["f_breakfast","Is it eaten at breakfast?"],["f_snack","Is it a snack?"],["f_round","Is it round?"],["f_brand","Is it a brand name?"],["f_christmas","Is it linked to Christmas?"],["f_orange","Is it orange?"],["f_british","Is it a British classic?"],["f_scot","Is it Scottish?"],["f_northeast","Is it from the North East?"],["f_italian","Is it Italian?"],["f_indian","Is it Indian?"],["f_chinese","Is it Chinese?"],["f_japanese","Is it Japanese?"],["f_american","Is it American?"],["f_mexican","Is it Mexican?"],["f_french","Is it French?"]],"object":[["o_vehicle","Is it a vehicle?"],["o_wear","Do you wear it?"],["o_toy","Is it a toy or game?"],["o_tool","Is it a tool?"],["o_sport","Is it used in sport?"],["o_music","Is it a musical instrument?"],["o_eat","Is it used for eating or drinking?"],["o_cook","Is it used for cooking?"],["o_clean","Is it used for cleaning?"],["o_write","Is it used for writing or drawing?"],["o_furniture","Is it furniture?"],["o_comm","Is it used to communicate?"],["o_money","Is it to do with money?"],["o_time","Does it tell the time?"],["o_home","Would you find it in most homes?"],["o_kitchen","Is it kept in the kitchen?"],["o_bathroom","Is it kept in the bathroom?"],["o_bedroom","Is it kept in the bedroom?"],["o_living","Is it kept in the living room?"],["o_garden","Is it used in the garden?"],["o_office","Is it used at school or work?"],["o_electric","Does it use electricity or batteries?"],["o_screen","Does it have a screen?"],["o_plug","Does it plug into the wall?"],["o_internet","Does it connect to the internet?"],["o_pocket","Can it fit in your pocket?"],["o_heavy","Is it heavier than a person?"],["o_hold","Do you hold it in your hand to use it?"],["o_metal","Is it mostly metal?"],["o_wood","Is it mostly wood?"],["o_plastic","Is it mostly plastic?"],["o_glass","Is it mostly glass?"],["o_paper","Is it mostly paper or card?"],["o_fabric","Is it mostly fabric?"],["o_old","Was it around before 1900?"],["o_new","Was it invented after 1990?"],["o_sharp","Is it sharp?"],["o_wheels","Does it have wheels?"],["o_moving","Does it have moving parts?"],["o_light","Does it give off light?"],["o_sound","Does it make a sound or music?"],["o_round","Is it round?"],["o_engine","Does it have an engine?"],["o_flies","Does it fly?"],["o_boat","Does it go on water?"],["o_public","Is it public transport?"],["o_rails","Does it run on rails?"],["o_feet","Do you wear it on your feet?"],["o_head","Do you wear it on your head?"],["o_jewel","Is it jewellery?"],["o_warm","Is it worn to keep warm?"],["o_ball","Is it a ball?"],["o_hit","Do you hit something with it?"],["o_strings","Does it have strings?"],["o_blow","Do you blow into it?"],["o_keys","Does it have keys?"]],"title":[["t_film","Is it a film?"],["t_tv","Is it a TV show?"],["t_book","Is it a book?"],["t_song","Is it a song?"],["t_game","Is it a video game?"],["t_e_old","Did it come out before 1970?"],["t_e_70","Did it come out in the 1970s?"],["t_e_80","Did it come out in the 1980s?"],["t_e_90","Did it come out in the 1990s?"],["t_e_00","Did it come out in the 2000s?"],["t_e_10","Did it come out in 2010 or later?"],["t_british","Is it British?"],["t_american","Is it American?"],["t_kids","Is it mainly for children?"],["t_comedy","Is it a comedy?"],["t_animated","Is it animated?"],["t_series","Is it part of a series or franchise?"],["t_scary","Is it scary?"],["t_love","Is it a love story?"],["t_christmas","Is it linked to Christmas?"],["t_real","Is it based on a true story?"],["t_scifi","Is it science fiction or fantasy?"],["t_crime","Is it about crime or detectives?"],["t_war","Is it about a war?"],["t_sport","Is it about sport?"],["t_animal","Is an animal a main character?"],["t_northeast","Is it set in the North East?"],["t_london","Is it set in London?"],["t_named","Is its title a character's name?"],["t_bookfirst","Was it a book first?"],["t_disney","Is it a Disney film?"],["t_pixar","Is it a Pixar film?"],["t_bestpic","Did it win the Best Picture Oscar?"],["t_bond","Is it a James Bond film?"],["t_superhero","Is it a superhero film?"],["t_sequel","Is it a sequel?"],["t_musical","Is it a musical?"],["t_sitcom","Is it a sitcom?"],["t_soap","Is it a soap?"],["t_quiz","Is it a quiz or game show?"],["t_reality","Is it reality TV?"],["t_drama","Is it a drama?"],["t_bbc","Is it on the BBC?"],["t_itv","Is it on ITV?"],["t_netflix","Is it on Netflix?"],["t_running","Is it still being made?"],["t_long","Has it run for over 20 years?"],["t_number1","Was it a UK number one?"],["t_xmas1","Was it a Christmas number one?"],["t_band","Is it by a band or group?"],["t_male","Is it sung by a man?"],["t_slow","Is it a slow song?"],["t_dance","Is it a party or dance song?"],["t_filmsong","Is it from a film?"],["t_cover","Is it a cover version?"],["t_novel","Is it a novel?"],["t_picture","Is it a picture book?"],["t_classic","Is it over 100 years old?"],["t_oasis","Is it by Oasis?"],["t_queen","Is it by Queen?"],["t_beatles","Is it by the Beatles?"],["t_wham","Is it by Wham! or George Michael?"],["t_abba","Is it by ABBA?"],["t_starwars","Is it a Star Wars film?"],["t_hpfilm","Is it a Harry Potter film?"]],"brand":[["b_food","Does it sell food or drink?"],["b_shop","Is it a shop or supermarket?"],["b_tech","Is it a tech company?"],["b_cars","Does it make cars?"],["b_clothes","Does it sell clothes or shoes?"],["b_sport","Is it a sports brand?"],["b_bank","Is it a bank?"],["b_airline","Is it an airline?"],["b_online","Is it mainly online?"],["b_uk","Is it British?"],["b_american","Is it American?"],["b_german","Is it German?"],["b_japanese","Is it Japanese?"],["b_french","Is it French?"],["b_northeast","Was it founded in the North East?"],["b_old","Was it founded before 1950?"],["b_logo","Is its logo an animal or a person?"],["b_red","Is its logo mainly red?"],["b_letters","Is its name letters or initials?"],["b_person","Is it named after a person?"],["b_highstreet","Is it on most high streets?"],["b_luxury","Is it a luxury brand?"],["b_supermarket","Is it a supermarket?"],["b_fastfood","Is it a fast-food chain?"],["b_coffee","Does it sell coffee?"],["b_drinks","Does it mainly make drinks?"],["b_sweets","Does it make sweets, chocolate or crisps?"],["b_phone","Does it make phones or computers?"],["b_social","Is it a social media app?"],["b_search","Is it a search engine?"],["b_stream","Is it a streaming service?"],["b_games","Does it make games or consoles?"],["b_sportscar","Does it make luxury or sports cars?"],["b_ukfactory","Does it build cars in Britain?"]]};
/** What the writer is told when a round wants 20 Questions: the item shape and every question id it must answer. */
function twentyGuide(): string {
  return `20 Questions ("twenty"): everyone hunts the same well-known answer by asking yes/no questions from a FIXED list, then guessing.
Shape: {"type":"twenty","answers":["Gary Barlow","Barlow"],"what":"person","yes":["p_man","p_alive","p_over50","p_british","p_music",...]}
- "answers": the answer first, then other ways people would type it. Pick answers a British room knows well.
- "what": exactly one of ${TWENTY_KINDS.map(([id, t]) => `${id} (${t})`).join(", ")}.
- "yes": EVERY question id from that kind's list below whose true answer is Yes (anything not listed counts as No). Go through the whole list. Every Yes must be certainly true today; if one is arguable, choose a different answer.
${Object.entries(TWENTY_TREE).map(([k, qs]) => `${k}: ${qs.map(([id, t]) => `${id} = ${t}`).join(" | ")}`).join("\n")}`;
}
const WRITER_SYSTEM = `You write questions for a live pub quiz played over a video call. Players answer on their phones and score more the faster they answer, so questions must be crisp, unambiguous and have one clearly correct answer. Write for a British audience: British spelling, and references a British room would know, unless the topic says otherwise.

Rules:
- Every fact must be correct. If you are not certain, verify with web search before using it — and always search for anything that could have changed recently (current record holders, "most recent", this year's events, who currently holds a job).
- Vary the sub-topics and difficulty within the set; never two questions on the same fact.
- Give every question a "difficulty" field: "easy", "medium" or "hard". For a mixed set aim for roughly a quarter easy, nearly half medium and the rest hard.
- Never put the answer, or a giveaway, in the question text.
- Keep question text under 140 characters. Answers under 40 characters.

What makes a good pub-quiz question (this matters as much as accuracy):
- It should make the room think or argue: a specific, interesting fact with a hook, not something everybody knows instantly. "What is given on the fifth day of the Twelve Days of Christmas", "the capital of France", "how many legs has a spider", "the largest planet" — nursery-level staples like these are never acceptable, even at easy. Easy means a fact most adults know but have to reach for, not one a child chants.
- Do not ask for something the audience can recite as a list or a lyric; do not ask the most famous thing about a famous subject unless you are asking for a detail of it.
- Wrong options must be genuinely tempting: the same kind of thing, the same era, things a player could believe. Never fillers from a well-known list where the odd one out is obvious, never options that rule themselves out.
- Prefer the surprising angle: the record nobody expects, the connection between two things, the detail behind the famous fact, the number people misjudge.
- Before you reply, reread every question and delete any that a bored ten-year-old would answer without pausing, then write a better one in its place.

Question types and their JSON shapes (use only the types you are asked for, and mix them):
- "choice": {"type":"choice","text":"...","options":["A","B","C","D"],"answer":"<exactly one of the options>","time":20}
  Wrong options must be plausible and of the same kind as the answer.
- "text": {"type":"text","text":"...","answers":["canonical answer","other accepted form",...],"time":25}
  Put the answer as it should be shown first; then alternatives that are also fully correct (nicknames, a surname on its own if that would be accepted).
- "order": {"type":"order","text":"Put these in order, earliest first","items":["first","second","third","fourth"],"hint":"earliest to latest","time":30}
  Items listed in the CORRECT order. 3 to 5 items. The question text must say what order.
- "match": {"type":"match","text":"Match the breed to the picture","pairs":[{"left":"Labrador Retriever","rightPicture":"Labrador Retriever"},...],"time":40}
  3 or 4 pairs. "rightPicture" is the exact English Wikipedia article title whose lead picture shows the RIGHT-HAND answer itself (only when a pictures round is wanted); otherwise use "right":"text" for a word-to-word match. Use pictures only when the right-hand things are recognisable from a photo: people (their article title), animals and breeds, foods, logos, artworks, landmarks, or countries as "Flag of <country>". Never picture the left-hand item on the right (a "landmark to its country" match shows each country's flag on the right, not the landmark), and never use a picture for an abstract answer such as a year, a name or a job.
- "pin": {"type":"pin","text":"Which city hosts a famous film festival every May?","place":"Cannes","region":"France","lat":43.55,"lon":7.02,"sizeKm":30,"time":20}
  A pin question is two tests in one: the text asks a fact the player must know, and the place is the answer they then have to find on the map. Never name the place, or a giveaway of it, in the text ("Which city hosted the 2016 Olympics?" → Rio de Janeiro; "In which state was the Declaration of Independence signed?" → Pennsylvania). "Drop the pin on X" is never acceptable.
  Only countries, cities, seas and famous landmarks. lat/lon of its centre in decimal degrees; sizeKm is roughly how wide the place is (a city ~30, a small country ~300, a large country ~2000). "region" is the blank map to show: the country the place is in for a city or landmark, the continent for a country, "World" only when the place spans continents or the question is about the world. Use the English Wikipedia name for the country or continent (France, United Kingdom, USA, Europe, Africa, South America, Australia). Never put the region's name in the question text when it gives the answer away.
- "tf": {"type":"tf","text":"<a statement>","answer":true}
- "nearest": {"type":"nearest","text":"How many steps are there to the top of Grey's Monument?","answer":164,"unit":"steps","spread":80}
  Nearest Wins, like House of Games' Distinctly Average: a question whose answer is ONE certain number, and players guess how close they can get (closest wins). Pick numbers people misjudge, never ones everybody knows: heights, lengths, years, counts, distances, records, ages, populations, prices at the time. "answer" is a plain number (no commas or units); "unit" is a short word for what it counts, or "" for a year; "spread" is how far off a guess can be and still score a little: about 25 for a year, about half the answer for most other numbers. The number must be stable and verifiable: say "at the 2021 census", "when it opened" and so on where it could change.
- "draw": {"type":"draw","text":"Draw It: at the seaside","words":["Sandcastle","Deckchair","Seagull","Ice cream","Lighthouse","Crab","Bucket and spade","Pier","Donkey","Beach hut","Surfboard","Sunglasses"]}
  Draw It (Pictionary on phones): players take turns to draw a word for the others to guess. Give 12 to 20 words on the round's theme that can be DRAWN without writing letters: concrete, picturable things and places, one to three words each, known to everyone in the room. No abstract ideas, no brand names that only work as a logo.
  A crisp statement that is definitely true or definitely false. Mix true and false across the set.
- "sort": {"type":"sort","text":"Which of these actors have been in Coronation Street?","categories":["Been in Coronation Street","Never been in Coronation Street"],"items":[{"text":"...","category":"<exactly one of the categories>"}]}
  2 to 4 categories, 4 to 8 items, at least one item per category. Every placement must be certain.
- "wipeout": {"type":"wipeout","text":"Footballers who have played for Newcastle United","right":["...x15"],"wrong":["...x5"]}
  A list question. "right" are 15 answers that definitely fit; "wrong" are 5 that are plausible (same kind of thing, same era or league) but definitely do not fit. Verify every one — a wrong answer that actually fits ruins the round.
- "race": {"type":"race","text":"The Race: capital cities","target":10,"bank":[{"q":"Capital of Peru?","right":"Lima","wrong":["Quito","Bogotá","Santiago"]} x20]}
  A quick-fire bank of 20 short multiple-choice questions on one topic, answered in a hurry on a phone: one short line each, four short answers. Easy to medium.
- "pin" (spot-the-thing): {"type":"pin","mode":"area","text":"Which of these instruments carries the filling to the tooth?","tiles":["Amalgam carrier","Dental mirror","Periodontal probe","Dental explorer","Dental elevator"],"answer":"Amalgam carrier"}
  The same rule: the tiles are a line-up, and the text asks a fact about one of them without naming it ("Which Simpson shot Mr Burns?" over a line-up of Simpsons characters → Maggie).
  A collage of 4 to 6 pictures; the player taps the right one. "tiles" are exact English Wikipedia article titles whose lead image clearly shows the object (tools, animals, cars, flags, foods, buildings, faces); "answer" is one of them. Only when a pictures round is wanted.
- "wheel": {"type":"wheel","category":"Phrase","phrase":"A PIECE OF CAKE"}
  A Wheel of Fortune puzzle: a well-known phrase, title, name or place in capitals, letters and spaces only (no punctuation), 8 to 40 letters, no word longer than 12 letters, whole phrase at most 4 words per row across 4 rows of 12/14/14/12 tiles. Category as on the show: Phrase, Person, Place, Thing, Event, Food & Drink, Song Title, Movie Title, TV Show, Before & After, Landmark, Occupation.
- "highlow": {"type":"highlow","text":"<highbrow clue>","lowText":"<lowbrow clue>","answers":["Gold","Au"]}
  Highbrow Lowbrow, as on House of Games: two clues with exactly the same answer. The highbrow clue is hard and scholarly (science, history, literature, the arts); the lowbrow clue is easy and from pop culture, telly, sport or everyday life. Neither clue may work for any other answer.
- "club": {"type":"club","pct":50,"text":"If planet EARTH has a HEART, which body part does MARS have?","answers":["Arms"],"why":"EARTH is an anagram of HEART, so MARS is an anagram of ARMS."}
  The 1% Club, in the style of The 1% Club: a logic, maths, pattern, wordplay or lateral-thinking puzzle that needs NO general knowledge, only working out, solvable in 30 seconds by reading the question (anagrams, letter/number patterns, "which is the odd one out", what-comes-next, counting, riddles that reward reading carefully). "pct" is how many people would get it: 90 is easy, 50 medium, 10 hard, 1 fiendish; spread the percentages across a batch and label honestly. The answer must be a single unambiguous word, number or short phrase; write the question so nothing else fits. "why" is one short sentence of working that shows why the answer is right (it is shown with the answer). No pictures.
- "tune": {"type":"tune","ask":"song","track":"Last Christmas","artist":"Wham!","year":1984,"answers":["Last Christmas"]}
  Name That Tune: a 30-second official preview of the track plays on the screen. "ask" is what players must give: "song" (the title), "artist", "year" (the year it was first released, as a number), "film" (the film the track is best known from — add "film":"Home Alone" — only for genuine film songs and themes), or "lyric" (add "cueLine": a very famous line from the song, shown on screen, and "lyricLine": the line that follows it; only for lyrics most people know). Use the exact official track title and the artist credit as on streaming services, well-known recordings only, and mix the asks across a set. "answers" holds the accepted answers for the ask (title, artist, year, film or line first). No pictures.
- "dingbat": {"type":"dingbat","answers":["Man overboard"],"elements":[{"t":"MAN","x":50,"y":30,"s":5},{"t":"BOARD","x":50,"y":70,"s":5}]}
  Dingbats (say what you see): a well-known phrase, saying, title or word hidden in how words sit on a 16:9 white board. Each element is a word or letters with its centre at x,y (0–100, per cent of the board), size s (1 tiny … 6 huge, 4 normal), optional "rot" (degrees, e.g. 90 or -90 for a word on its side, 180 upside down), optional "flip" ("h" mirrored/backwards, "v" upside down) and optional "style" ("strike" crossed out, "underline", "box" for a word in a box, "outline" for hollow letters). Use classic devices: one word over another (over/under/on), inside a box (in/inside), repeated (e.g. "aid aid aid" = first aid), split or missing letters, tiny and huge (little/big), backwards, a word at the far left or right edge (left/right/end), high or low on the board. 1 to 6 elements; keep it fair, solvable and British. The answer is the phrase. No pictures.
- "rhyme": {"type":"rhyme","text":"Sherlock Holmes's companion","answer1":"Watson","text2":"A large, loud gathering after dark","answer2":"Party"}
  Rhyme Time: two clues whose answers rhyme (the endings sound the same when said aloud). Players type both answers. Keep each answer to one or two words.
- "smash": {"type":"smash","picture":"Emma Watson","pictureAnswer":"Emma Watson","text":"Sega's blue hedgehog","clueAnswer":"Sonic the Hedgehog"}
  Answer Smash, as on House of Games: the picture shows a well-known person, place or thing ("picture" is its English Wikipedia title, "pictureAnswer" the name players would say); "text" is a clue whose answer starts with the same letters that end the picture's answer — Emma WatSON + SONic the Hedgehog → "Emma Watsonic the Hedgehog"; Judi DenCH + CHina → "Judi Denchina". The overlap must be at least two letters and genuine. Keep the clue short and the answers well known.

Pictures: add "picture":"<exact English Wikipedia article title>" to any question where a picture makes it better or is the question itself ("Which city is this?", "Name this bird"). The title must be the article whose LEAD IMAGE IS THE THING ASKED ABOUT: for a flag question that is "Flag of Bhutan", never "Bhutan"; for a logo "Logo of …" or the company; for a coat of arms "Coat of arms of …"; for a landmark the landmark's own article, not the city's; for a person, their article. Use only titles you are confident exist, whose lead image shows the thing and does not contain its name as a caption in the image. Do not add a picture that gives the answer away when the question is not about identifying the picture.

Times are in seconds: 15–45. Harder or longer questions get longer.

Reply with JSON only: {"questions":[ ... ]}`;

interface GenOpts { topic: string; brief: string; count: number; difficulty: string; types: string[]; pictures: boolean; web: boolean; avoid: string[]; usedPictures: string[]; premium: boolean; }

/** Turns the writer's raw JSON (or a bank file in the same shape) into finished questions: pictures, maps, clips, ids. */
async function finishRaw(raw: any[], count: number, usedPictures: string[], wantPictures: boolean): Promise<{ questions: any[]; warnings: string[] }> {
  const uid = (p: string) => p + "_" + crypto.randomUUID().replace(/-/g, "").slice(0, 8);
  const warnings: string[] = [];
  const used = new Set<string>(usedPictures);
  const world = raw.some((q) => q?.type === "pin") ? await locationMap("World") : null;

  const questions = await Promise.all(raw.slice(0, count).map(async (r) => {
    const time = Math.min(90, Math.max(10, Math.round(+r.time || 25)));
    const base: any = { id: uid("q"), type: r.type, text: String(r.text || r.phrase || (r.type === "tune" ? r.track : r.type === "dingbat" ? "Say what you see" : r.type === "draw" ? "Draw It" : r.type === "twenty" ? "20 Questions: who or what am I?" : "") || "").trim(), time, media: { kind: "none" }, partial: false };
    if (["easy", "medium", "hard"].includes(r.difficulty)) base.difficulty = r.difficulty; // easy / medium / hard, from the writer or the bank file
    if (!base.text) return null;

    if (wantPictures && typeof r.picture === "string" && r.picture.trim() && r.type !== "pin") {
      const pic = await wikiPicture(r.picture.trim(), used);
      if (pic) base.media = { kind: "image", url: pic.url, source: pic.source, credit: `Wikipedia / Wikimedia Commons: ${r.picture.trim()}` };
      else warnings.push(`No picture found for “${r.picture}” (question kept without one).`);
    }

    if (r.type === "choice") {
      const opts = (Array.isArray(r.options) ? r.options : []).map((s: unknown) => String(s ?? "").trim()).filter(Boolean).slice(0, 4);
      if (opts.length < 2) return null;
      base.options = opts.map((text: string) => ({ id: uid("o"), text }));
      const ans = norm(String(r.answer || ""));
      const hit = base.options.find((op: any) => norm(op.text) === ans) || base.options[0];
      base.correct = hit.id;
      return base;
    }
    if (r.type === "text") {
      const answers = (Array.isArray(r.answers) ? r.answers : [r.answer]).map((s: unknown) => String(s ?? "").trim()).filter(Boolean);
      if (!answers.length) return null;
      base.answers = answers; base.ai = true;
      return base;
    }
    if (r.type === "order") {
      const items = (Array.isArray(r.items) ? r.items : []).map((s: unknown) => String(s ?? "").trim()).filter(Boolean).slice(0, 6);
      if (items.length < 3) return null;
      base.items = items.map((text: string) => ({ id: uid("i"), text }));
      base.hint = String(r.hint || "").trim();
      return base;
    }
    if (r.type === "match") {
      const pairs = await Promise.all((Array.isArray(r.pairs) ? r.pairs : []).slice(0, 4).map(async (p: any) => {
        const left = String(p?.left ?? "").trim();
        if (!left) return null;
        if (wantPictures && typeof p?.rightPicture === "string" && p.rightPicture.trim()) {
          const pic = await wikiPicture(p.rightPicture.trim(), used);
          if (pic) return { id: uid("p"), left, right: { kind: "image", value: pic.url, source: pic.source } };
          warnings.push(`No picture for “${p.rightPicture}” in a match question.`);
        }
        const right = String(p?.right ?? "").trim();
        return right ? { id: uid("p"), left, right: { kind: "text", value: right } } : null;
      }));
      base.pairs = pairs.filter(Boolean);
      if (base.pairs.length < 2) return null;
      return base;
    }
    if (r.type === "tf") {
      if (typeof r.answer !== "boolean") return null;
      base.answer = r.answer;
      return base;
    }
    if (r.type === "nearest") {
      const n = typeof r.answer === "number" ? r.answer : parseFloat(String(r.answer ?? "").replace(/[,£$€\s]/g, ""));
      if (!Number.isFinite(n)) return null;
      base.answer = String(n); base.unit = String(r.unit ?? "").trim().slice(0, 20);
      const sp = +r.spread; base.spread = Number.isFinite(sp) && sp > 0 ? sp : null; base.time = 25; base.media = { kind: "none" };
      return base;
    }
    if (r.type === "twenty") {
      const what = String(r.what || r.kind || ""), ids = TWENTY_TREE[what];
      const answers = [...new Set((Array.isArray(r.answers) ? r.answers : [r.answer]).map((a: unknown) => String(a ?? "").trim()).filter(Boolean))].slice(0, 8);
      if (!ids || !answers.length) return null;
      const f = r.facts && typeof r.facts === "object" ? r.facts : {}; for (const id of Array.isArray(r.yes) ? r.yes : []) f[String(id)] = true;
      Object.assign(base, { what, answers, facts: Object.fromEntries(ids.map(([id]) => [id, f[id] === true])), maxQ: 20, prize: 1000, prize2: 500, prize3: 100, penalty: 200, time: 180, ai: true, media: { kind: "none" } });
      return base;
    }
    if (r.type === "draw") {
      const words = [...new Set((Array.isArray(r.words) ? r.words : []).map((w: unknown) => String(w ?? "").trim()).filter((w: string) => w && w.length <= 30))].slice(0, 30);
      if (words.length < 6) return null;
      base.text = String(r.text || "Draw It").trim() || "Draw It"; base.words = words; base.turns = 3; base.guessPoints = 500; base.drawerPoints = 100; base.time = 60; base.media = { kind: "none" };
      return base;
    }
    if (r.type === "sort") {
      const cats = (Array.isArray(r.categories) ? r.categories : []).map((s: unknown) => String(s ?? "").trim()).filter(Boolean).slice(0, 4);
      if (cats.length < 2) return null;
      base.categories = cats.map((name: string) => ({ id: uid("c"), name }));
      base.items = (Array.isArray(r.items) ? r.items : []).slice(0, 12).map((it: any) => {
        const text = String(it?.text ?? "").trim(); const cat = base.categories.find((c: any) => norm(c.name) === norm(String(it?.category ?? "")));
        return text && cat ? { id: uid("i"), text, category: cat.id } : null;
      }).filter(Boolean);
      if (base.items.length < 2) return null;
      return base;
    }
    if (r.type === "wipeout") {
      const list = (a: unknown) => (Array.isArray(a) ? a : []).map((s: unknown) => String(s ?? "").trim()).filter(Boolean);
      const right = list(r.right).slice(0, 15), wrong = list(r.wrong).slice(0, Math.max(1, 20 - Math.min(15, list(r.right).length)));
      if (right.length < 3 || !wrong.length) return null;
      base.right = right.map((text: string) => ({ id: uid("w"), text }));
      base.wrong = wrong.map((text: string) => ({ id: uid("w"), text }));
      base.pickPoints = 200; base.penalty = 500; base.time = 5;
      return base;
    }
    if (r.type === "race") {
      const bank = (Array.isArray(r.bank) ? r.bank : []).map((b: any) => {
        const text = String(b?.q ?? b?.text ?? "").trim(), right = String(b?.right ?? "").trim();
        const wrong = (Array.isArray(b?.wrong) ? b.wrong : []).map((s: unknown) => String(s ?? "").trim()).filter(Boolean).slice(0, 3);
        return text && right && wrong.length ? { id: uid("b"), text, options: [right, wrong[0] || "", wrong[1] || "", wrong[2] || ""] } : null;
      }).filter(Boolean);
      // Always 20 questions and a target of 10, so a player can get ten wrong and still finish.
      if (bank.length < 20) return null;
      base.bank = bank.slice(0, 20); base.target = 10; base.perCorrect = 100; base.prize = 500; base.prize2 = 200; base.prize3 = 100; base.forfeit = 200; base.time = 120;
      return base;
    }
    if (r.type === "highlow") {
      const lowText = String(r.lowText || "").trim();
      const answers = (Array.isArray(r.answers) ? r.answers : [r.answer]).map((s: unknown) => String(s ?? "").trim()).filter(Boolean);
      if (!lowText || !answers.length) return null;
      base.lowText = lowText; base.answers = answers; base.highPoints = 1000; base.lowPoints = 500; base.ai = true; base.time = Math.max(base.time, 40);
      return base;
    }
    if (r.type === "tune") {
      const ask = ["song", "artist", "year", "film", "lyric"].includes(r.ask) ? r.ask : "song";
      const track = String(r.track || "").trim(), artist = String(r.artist || "").trim();
      if (!track || !artist) return null;
      const hit = await tuneLookup(`${track} ${artist}`, track, artist);
      if (!hit) { warnings.push(`No preview found for “${track}” by ${artist} (question dropped).`); return null; }
      let answers = (Array.isArray(r.answers) ? r.answers : [r.answer]).map((s: unknown) => String(s ?? "").trim()).filter(Boolean);
      const film = String(r.film || "").trim(), lyric = String(r.lyricLine || "").trim(), cue = String(r.cueLine || "").trim();
      if (ask === "song") { const clean = cleanTitle(hit.track); answers = [clean, ...answers.filter((a) => norm(a) !== norm(clean)), ...(norm(hit.track) !== norm(clean) ? [hit.track] : [])]; }
      if (ask === "artist") answers = [hit.artist, ...answers.filter((a) => norm(a) !== norm(hit.artist))];
      if (ask === "year") answers = [String(hit.year || r.year || "")].filter(Boolean);
      if (ask === "film") { if (!film) return null; answers = [film, ...answers.filter((a) => norm(a) !== norm(film))]; }
      if (ask === "lyric") { if (!lyric || !cue) return null; answers = [lyric, ...answers.filter((a) => norm(a) !== norm(lyric))]; base.cue = cue; }
      if (!answers.length) return null;
      base.text = ""; base.ask = ask; base.track = hit.track; base.artist = hit.artist; base.year = hit.year; base.film = film; base.answers = answers; base.tolerance = 1; base.ai = true; base.time = 30;
      base.media = { kind: "audio", url: hit.previewUrl, artwork: hit.artwork, start: 0, length: 15, credit: "Preview via Apple Music" };
      return base;
    }
    if (r.type === "club") {
      const answers = (Array.isArray(r.answers) ? r.answers : [r.answer]).map((s: unknown) => String(s ?? "").trim()).filter(Boolean);
      if (!answers.length) return null;
      base.answers = answers; base.pct = Math.min(99, Math.max(1, Math.round(+r.pct || 50))); base.ai = true; base.time = 30; base.media = { kind: "none" };
      const why = String(r.why ?? "").trim(); if (why) base.why = why.slice(0, 300); // one line of working, shown with the answer
      return base;
    }
    if (r.type === "dingbat") {
      const answers = (Array.isArray(r.answers) ? r.answers : [r.answer]).map((s: unknown) => String(s ?? "").trim()).filter(Boolean);
      const elements = (Array.isArray(r.elements) ? r.elements : []).slice(0, 8).map((e: any) => {
        const t = String(e?.t ?? e?.text ?? "").trim(); if (!t) return null;
        const num = (v: any, d: number, lo: number, hi: number) => Math.min(hi, Math.max(lo, Number.isFinite(+v) ? +v : d));
        const out: any = { t: t.slice(0, 40), x: num(e?.x, 50, 0, 100), y: num(e?.y, 50, 0, 100), s: num(e?.s, 4, 1, 6) };
        if (e?.rot) out.rot = num(e.rot, 0, -180, 180);
        if (e?.flip === "h" || e?.flip === "v") out.flip = e.flip;
        if (["strike", "underline", "box", "outline"].includes(e?.style)) out.style = e.style;
        return out;
      }).filter(Boolean);
      if (!answers.length || !elements.length) return null;
      base.text = String(r.text || "Say what you see").trim(); base.answers = answers; base.elements = elements; base.ai = true; base.time = 45; base.media = { kind: "none" };
      return base;
    }
    if (r.type === "rhyme") {
      const text2 = String(r.text2 || "").trim(), answer1 = String(r.answer1 || "").trim(), answer2 = String(r.answer2 || "").trim();
      if (!text2 || !answer1 || !answer2) return null;
      base.text2 = text2; base.answer1 = answer1; base.answer2 = answer2; base.ai = true;
      return base;
    }
    if (r.type === "wheel") {
      const phrase = String(r.phrase || "").toUpperCase().replace(/[^A-Z0-9' &-]/g, "").replace(/\s+/g, " ").trim();
      const words = phrase.split(" ").filter(Boolean);
      if (!phrase || phrase.replace(/[^A-Z]/g, "").length < 4 || words.some((w) => w.length > 14) || phrase.length > 52) { warnings.push(`Dropped a Wheel of Fortune phrase that would not fit the board (${r.phrase}).`); return null; }
      base.text = phrase; base.phrase = phrase; base.category = String(r.category || "Phrase").trim().slice(0, 40); base.revealEvery = 4; base.startLetters = ""; base.ai = true; base.media = { kind: "none" };
      return base;
    }
    if (r.type === "smash") {
      const pictureAnswer = String(r.pictureAnswer || r.picture || "").trim(), clueAnswer = String(r.clueAnswer || "").trim();
      const sm = smashOf(pictureAnswer, clueAnswer);
      if (!pictureAnswer || !clueAnswer || sm.overlap < 2) { warnings.push(`Dropped an Answer Smash whose answers did not overlap (${pictureAnswer} + ${clueAnswer}).`); return null; }
      const pic = await wikiPicture(String(r.picture || pictureAnswer).trim(), used, true);
      if (!pic) { warnings.push(`No picture found for “${r.picture || pictureAnswer}”, so that Answer Smash was left out.`); return null; }
      base.media = { kind: "image", url: pic.url, source: pic.source, credit: `Wikipedia / Wikimedia Commons: ${r.picture || pictureAnswer}` };
      base.pictureAnswer = pictureAnswer; base.clueAnswer = clueAnswer; base.smash = sm.smash; base.ai = true;
      return base;
    }
    if (r.type === "pin" && r.mode === "area") {
      const tiles = (Array.isArray(r.tiles) ? r.tiles : []).map((s: unknown) => String(s ?? "").trim()).filter(Boolean).slice(0, 6);
      const answer = String(r.answer || "").trim();
      const ai = tiles.findIndex((t) => norm(t) === norm(answer));
      if (tiles.length < 3 || ai < 0) return null;
      const pics = await Promise.all(tiles.map((t) => wikiPicture(t, used)));
      const collage = tiles.map((title, i) => pics[i] ? { title, url: pics[i]!.url, credit: `Wikipedia / Wikimedia Commons: ${title}` } : null);
      if (!collage[ai]) { warnings.push(`No picture found for “${answer}”, so that spot-the-thing question was left out.`); return null; }
      const kept = collage.filter(Boolean) as any[];
      if (kept.length < 3) { warnings.push(`Too few pictures found for “${base.text}”, so it was left out.`); return null; }
      base.mode = "area"; base.collage = kept; base.answerIndex = kept.findIndex((t: any) => t.title === tiles[ai]); base.place = tiles[ai];
      base.media = { kind: "none" }; // the portal tiles the pictures into one and uploads it
      return base;
    }
    if (r.type === "pin") {
      const lat = +r.lat, lon = +r.lon;
      if (!isFinite(lat) || !isFinite(lon) || Math.abs(lat) > 90 || Math.abs(lon) > 180) return null;
      // The map the question asked for, falling back to the world when it has none or the place is off its edge.
      let map = typeof r.region === "string" && r.region.trim() ? await locationMap(r.region.trim()) : null;
      let pt = map ? map.project(lat, lon) : null;
      if (!map || !pt || pt.x < 0.02 || pt.x > 0.98 || pt.y < 0.02 || pt.y > 0.98) {
        if (map) warnings.push(`“${r.place}” is off the edge of the ${map.name} map, so it is on the world map instead.`);
        else if (r.region) warnings.push(`No blank map of “${r.region}” could be found, so “${r.place}” is on the world map.`);
        map = world; pt = map ? map.project(lat, lon) : null;
      }
      if (!map || !pt) { warnings.push(`Could not fetch a map for “${r.place}”, so that question was left out.`); return null; }
      const sizeKm = Math.max(5, Math.min(5000, +r.sizeKm || 300));
      const full = Math.max(0.012, Math.min(0.12, (sizeKm / 2) / map.kmPerWidth(lat)));
      base.media = { kind: "image", url: map.url, credit: `Wikimedia Commons: ${map.name} location map` };
      base.mapRegion = map.name;
      if (map.bounds) base.mapBounds = map.bounds;
      base.pin = { x: +pt.x.toFixed(4), y: +pt.y.toFixed(4) };
      base.radiusFull = +full.toFixed(4);
      base.radiusZero = +Math.min(0.35, full * 4).toFixed(4);
      base.place = String(r.place || "").trim();
      return base;
    }
    return null;
  }));

  const kept = questions.filter(Boolean);
  return { questions: kept, warnings };
}

async function generate(o: GenOpts) {
  const client = anthropic();
  const wantPictures = o.pictures;
  const typeList = o.types.length ? o.types : ["choice", "text"];
  // The portal asks for a big round in batches; this is what earlier batches already wrote.
  const avoid = o.avoid.length ? `Already used, in this quiz or in earlier quizzes the same host has run — do not repeat these facts, ask them another way, or reuse their answers as the answer to something else:\n${o.avoid.map((t) => "- " + t).join("\n")}` : "";
  // The host's own brief for the round outranks the topic line: "a sports round, but every
  // question about Harry Kane" means every question about Harry Kane.
  const brief = o.brief ? `\nThe host's brief for this round — follow it closely, it decides what every question is about:\n${o.brief}` : "";
  const prompt = `Write ${o.count} pub quiz questions.
Round: ${o.topic || "general knowledge"}${brief}
Difficulty: ${o.difficulty}${o.difficulty === "mixed" ? " (about 25% easy, 45% medium, 30% hard)" : ""}
Question types to use (mix them across the set): ${typeList.join(", ")}${typeList.includes("twenty") ? "\n\n" + twentyGuide() : ""}
Pictures round: ${wantPictures ? "yes — give roughly half the questions a picture, and use rightPicture for match questions" : "no pictures"}`;

  const plan = writerPlan(typeList, o.premium);
  // The long system prompt and the do-not-repeat list are the same for every batch of a
  // round, so they are marked cacheable: later batches read them at a fraction of the price.
  const params: Anthropic.MessageCreateParamsNonStreaming = {
    model: plan.model,
    max_tokens: 16000,
    system: [{ type: "text", text: WRITER_SYSTEM, cache_control: { type: "ephemeral" } }],
    output_config: { effort: "medium" },
    messages: [{ role: "user", content: avoid ? [{ type: "text", text: avoid, cache_control: { type: "ephemeral" } }, { type: "text", text: prompt }] : prompt }],
  };
  if (o.web && plan.web) params.tools = [{ type: "web_search_20260209", name: "web_search", max_uses: plan.searches }];

  const msg = await ask(client, params);
  const usage = usageOf(msg, plan.model);
  const out = extractJson(textOf(msg));
  const raw: any[] = Array.isArray(out?.questions) ? out.questions : [];
  if (!raw.length) throw new Error("The AI did not write any questions. Try a broader topic.");

  const { questions: kept, warnings } = await finishRaw(raw, o.count, o.usedPictures, wantPictures);
  if (!kept.length) throw new Error("None of the AI's questions were usable. Try again.");
  return { questions: kept, warnings, searched: !!(o.web && plan.web), usage };
}

// ---------------------------------------------------------------- fact-checking
const CHECK_SYSTEM = `You are the independent fact-checker for a pub quiz. The questions were written by someone else, possibly by an AI. For each question, decide whether the marked answer is correct and the question is fair to ask a room of players who answer quickly on their phones.

Use web search to confirm anything you are not completely certain of — especially numbers, dates, records, "first", "most", "current" and anything that may have changed recently. Do not take the quiz's answer on trust; check it.

Verdicts:
- "ok": the marked answer is correct and it is the one clear answer.
- "doubt": probably fine, but something is worth the host's look — a second defensible answer, a wrong option that is arguably right, a fact that sources disagree on or that may be out of date, wording that could be read two ways, or an item in an order/match set you could not confirm.
- "wrong": the marked answer is incorrect, the order or a pairing is wrong, an item is in the wrong category, a Wipeout "right" answer does not fit or a "wrong" one does, or the question cannot be answered as written.

Be exacting but not pedantic: a pub quiz accepts common knowledge and ordinary rounding. For each question write a note of one or two plain sentences saying what you checked and, if there is a problem, what is wrong and what it should be. When you know the correct answer, give it in "fix".

Reply with JSON only: {"checks":[{"id":"...","verdict":"ok|doubt|wrong","note":"...","fix":"optional corrected answer"}]}`;

async function verifyQuestions(items: { id: string; summary: string }[], premium = false) {
  const model = premium ? OPUS : SONNET;
  const msg = await ask(anthropic(), {
    model,
    max_tokens: 8000,
    system: [{ type: "text", text: CHECK_SYSTEM, cache_control: { type: "ephemeral" } }],
    output_config: { effort: "medium" },
    tools: [{ type: "web_search_20260209", name: "web_search", max_uses: premium ? 10 : 6 }],
    messages: [{ role: "user", content: "Check these questions:\n\n" + items.map((i) => `[id ${i.id}]\n${i.summary}`).join("\n\n") }],
  });
  const out = extractJson(textOf(msg));
  const checks: Record<string, { verdict: string; note: string; fix?: string }> = {};
  for (const c of out?.checks || []) {
    if (typeof c?.id !== "string" || !items.some((i) => i.id === c.id)) continue;
    const verdict = ["ok", "doubt", "wrong"].includes(c.verdict) ? c.verdict : "doubt";
    checks[c.id] = { verdict, note: String(c.note || "").slice(0, 600), ...(c.fix ? { fix: String(c.fix).slice(0, 200) } : {}) };
  }
  return { usage: usageOf(msg, model), checks };
}

// ---------------------------------------------------------------- handler
Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response(null, { headers: CORS });
  try {
    const body = await req.json().catch(() => ({}));
    const { action, password } = body;

    if (!HOST_PW) return json({ error: "The server has no QUIZ_HOST_PASSWORD set." }, 500);
    if (typeof password !== "string" || password !== HOST_PW) return json({ error: "Wrong password." }, 401);

    if (action === "login") return json({ ok: true, ai: !!ANTHROPIC_KEY });

    if (action === "list") {
      const rows = await rest(`quiz_quizzes?select=id,title,settings,questions,created_at,updated_at&order=updated_at.desc`);
      return json({ quizzes: (rows || []).map((r: any) => ({
        id: r.id, title: r.title, updated_at: r.updated_at, created_at: r.created_at,
        template: !!(r.settings && r.settings.template),
        bank: !!(r.settings && r.settings.bank),
        rounds: Array.isArray(r.settings?.rounds) ? r.settings.rounds.map((x: any) => ({ title: x?.title || "", count: Object.values(x?.mix || {}).reduce((a: number, b: any) => a + (+b || 0), 0) || +x?.count || 0, types: Object.keys(x?.mix || {}) })) : [],
        count: Array.isArray(r.questions) ? r.questions.filter((q: any) => q?.type !== "slide").length : 0,
        types: Array.isArray(r.questions) ? Array.from(new Set(r.questions.filter((q: any) => q?.type !== "slide").map((q: any) => q.type))) : [],
      })) });
    }

    if (action === "history") {
      // Every question ever saved, newest quiz first, so the writer can avoid repeating any of them.
      const rows = await rest(`quiz_quizzes?select=id,title,questions,updated_at&order=updated_at.desc&limit=200`);
      const out: { quiz: string; text: string }[] = [];
      for (const r of rows || []) {
        if (body.exclude && r.id === body.exclude) continue;
        for (const q of (Array.isArray(r.questions) ? r.questions : [])) {
          const text = q?.type === "smash" ? `${q.pictureAnswer} + ${q.clueAnswer}` : q?.type === "wheel" ? q.phrase : q?.type === "race" ? `Race: ${q.text}` : q?.text;
          if (typeof text === "string" && text.trim()) out.push({ quiz: r.title, text: text.trim().slice(0, 160) });
          if (q?.type === "race" && Array.isArray(q.bank)) for (const b of q.bank) if (b?.text) out.push({ quiz: r.title, text: String(b.text).trim().slice(0, 160) });
        }
        if (out.length > 1500) break;
      }
      return json({ questions: out.slice(0, 1500), quizzes: (rows || []).length });
    }

    if (action === "get") {
      if (!UUID_RE.test(String(body.id))) return json({ error: "Bad quiz id." }, 400);
      const rows = await rest(`quiz_quizzes?id=eq.${body.id}&select=*`);
      if (!rows?.[0]) return json({ error: "That quiz no longer exists." }, 404);
      return json({ quiz: rows[0] });
    }

    if (action === "save") {
      const q = body.quiz || {};
      const title = String(q.title || "").trim().slice(0, 120) || "Untitled quiz";
      const settings = typeof q.settings === "object" && q.settings ? q.settings : {};
      const questions = Array.isArray(q.questions) ? q.questions : [];
      if (JSON.stringify(questions).length > 2_000_000) return json({ error: "That quiz is too large to save." }, 413);
      const payload = { title, settings, questions, updated_at: new Date().toISOString() };
      let rows;
      if (q.id && UUID_RE.test(String(q.id))) {
        rows = await rest(`quiz_quizzes?id=eq.${q.id}`, { method: "PATCH", headers: { Prefer: "return=representation" }, body: JSON.stringify(payload) });
        if (!rows?.[0]) rows = await rest(`quiz_quizzes`, { method: "POST", headers: { Prefer: "return=representation" }, body: JSON.stringify({ id: q.id, ...payload }) });
      } else {
        rows = await rest(`quiz_quizzes`, { method: "POST", headers: { Prefer: "return=representation" }, body: JSON.stringify(payload) });
      }
      return json({ quiz: rows[0] });
    }

    if (action === "delete") {
      if (!UUID_RE.test(String(body.id))) return json({ error: "Bad quiz id." }, 400);
      await rest(`quiz_quizzes?id=eq.${body.id}`, { method: "DELETE" });
      return json({ ok: true });
    }

    if (action === "upload") {
      const ct = String(body.contentType || "image/jpeg");
      if (!/^image\/(jpeg|png|webp|gif)$/.test(ct)) return json({ error: "Only JPEG, PNG, WebP or GIF pictures." }, 400);
      let bytes: Uint8Array;
      try { bytes = Uint8Array.from(atob(String(body.data || "")), (c) => c.charCodeAt(0)); }
      catch { return json({ error: "The picture data was not readable." }, 400); }
      if (bytes.length < 100) return json({ error: "That picture is empty." }, 400);
      if (bytes.length > 6_000_000) return json({ error: "That picture is too big (6 MB max after resizing)." }, 413);
      const url = await storagePut(`uploads/${crypto.randomUUID()}.${extFor(ct)}`, bytes, ct);
      return json({ url });
    }

    if (action === "check_text") {
      const question = String(body.question || "");
      const accepted = (Array.isArray(body.accepted) ? body.accepted : []).map((s: unknown) => String(s ?? "")).filter(Boolean);
      const answers = (Array.isArray(body.answers) ? body.answers : [])
        .filter((a: any) => a && typeof a.id === "string" && typeof a.text === "string")
        .slice(0, 200)
        .map((a: any) => ({ id: a.id, text: a.text.slice(0, 200) }));
      if (!accepted.length) return json({ error: "No accepted answers to check against." }, 400);
      return json(await checkText(question, accepted, answers));
    }

    if (action === "generate") {
      if (!ANTHROPIC_KEY) return json({ error: "AI is not set up on the server yet — add ANTHROPIC_API_KEY as a Supabase secret." }, 503);
      const KNOWN = ["choice", "text", "order", "match", "pin", "tf", "sort", "wipeout", "race", "smash", "wheel", "highlow", "rhyme", "club", "dingbat", "tune", "catchphrase", "nearest", "draw", "twenty", ...Object.keys(RACE_GAMES)];
      const asked = (Array.isArray(body.types) ? body.types : []).map(String);
      let types = asked.filter((t) => KNOWN.includes(t));
      // Hot Potato, King of the Hill and Blockbusters play on a race's bank of quick questions: take or write a race, then reshape it.
      const game = types.length === 1 && RACE_GAMES[types[0]] ? types[0] : "";
      if (game) {
        types = ["race"];
        if (game === "blockbusters") body.brief = `${String(body.brief || "")}\nThis bank is for Blockbusters: every right answer is a single word or short name, and the 20 right answers each start with a DIFFERENT letter of the alphabet (never Q, X or Z).`.trim();
      }
      const reshape = (list: any[]) => game ? list.map((q: any) => q?.type === "race" ? raceToGame(q, game) : q) : list;
      const unknownTypes = asked.filter((t) => !KNOWN.includes(t));
      if (asked.length && !types.length) return json({ error: `This server does not know the question type${unknownTypes.length > 1 ? 's' : ''} ${unknownTypes.join(", ")} yet — redeploy the quiz-api function.` }, 400);
      // The bank first: anything pre-written that fits this round comes free, and only the shortfall is written by the AI.
      const wantCount = Math.min(8, Math.max(1, Math.round(+body.count || 5)));
      const quizId = UUID_RE.test(String(body.quizId || "")) ? String(body.quizId) : "";
      let fromBank: any[] = []; const bankInfo: any = {};
      if (body.useBank !== false && quizId && types.length === 1) {
        try { fromBank = await bankTake(types[0], wantCount, String(body.topic || body.title || ""), String(body.brief || ""), quizId, ["easy", "medium", "hard"].includes(String(body.difficulty)) ? String(body.difficulty) : "mixed", bankInfo); } catch (e) { console.warn("bank take failed", String(e)); }
      }
      if (fromBank.length >= wantCount) return json({ questions: reshape(fromBank), warnings: [], searched: false, usage: null, unknownTypes, fromBank: fromBank.length, bankInfo });
      // Catchphrase clips only come from the bank: the AI cannot make a video.
      if (types[0] === "catchphrase") return json({ questions: fromBank, warnings: fromBank.length < wantCount ? ["The Catchphrase clips in the bank have run out. Add more, or pick another type for the rest."] : [], searched: false, usage: null, unknownTypes, fromBank: fromBank.length, bankInfo });
      const out = await generate({
        topic: String(body.brief ? (body.title || body.topic || "") : (body.topic || "")).slice(0, 200),
        brief: String(body.brief || "").slice(0, 1500),
        count: wantCount - fromBank.length,
        avoid: [...fromBank.map((q: any) => String(q.text || "")), ...(Array.isArray(body.avoid) ? body.avoid : []).map((s: unknown) => String(s ?? "").slice(0, 160))].filter(Boolean).slice(0, 400),
        usedPictures: (Array.isArray(body.usedPictures) ? body.usedPictures : []).map((s: unknown) => String(s ?? "").slice(0, 300)).filter(Boolean).slice(-300),
        difficulty: ["easy", "medium", "hard", "mixed"].includes(String(body.difficulty)) ? String(body.difficulty) : "mixed",
        types,
        pictures: body.pictures !== false,
        web: body.web !== false,
        premium: body.premium === true,
      });
      return json({ ...out, questions: reshape([...fromBank, ...out.questions]), unknownTypes, fromBank: fromBank.length, bankInfo });
    }

    if (action === "kahoot_import") {
      // A Kahoot, from its link (Kahoot's own public data: exact wording, answers, timers and pictures) or from a printout
      // of its page. A printout is read by Claude; the link printed in its footer is then tried first, so a public
      // Kahoot still comes through exactly, and only a private one falls back to what was read off the page.
      let uuid = kahootId(String(body.url || ""));
      let read: any = null;
      if (!uuid && Array.isArray(body.pages) && body.pages.length) {
        if (!ANTHROPIC_KEY) return json({ error: "Reading a PDF needs the AI, and ANTHROPIC_API_KEY is not set on the server." }, 503);
        read = await kahootRead(body.pages.slice(0, 15).map(String));
        read.offset = Math.max(0, Math.round(+body.offset || 0));
        uuid = kahootId(String(read.url || ""));
      }
      if (uuid) {
        const k = await kahootFetch(uuid);
        if (k && (!read || Math.abs(k.questions.length + k.skipped - (read.questions || []).length) <= 2)) return json({ source: "kahoot", uuid, usage: read?.usage || null, ...k });
        if (!read) return json({ error: "Kahoot would not share that quiz. Set its visibility to Public in Kahoot, or upload a PDF of it instead." }, 404);
      }
      if (!read) return json({ error: "Upload a PDF of the Kahoot, or paste its link." }, 400);
      return json({ source: "pdf", ...(await kahootFromRead(read)), usage: read.usage || null });
    }
    if (action === "bank_status") {
      const rows = await bankRows();
      return json({ bank: bankStatus(rows), categories: bankCategories(rows), low: BANK_LOW });
    }
    if (action === "bank_list") {
      const type = String(body.type || "");
      const row = (await bankRows(type)).find((r) => r.settings?.type === type);
      const qs: any[] = row ? row.questions : [];
      return json({ questions: qs.map((q) => ({ id: q.id, text: q.text || q.phrase || q.place || "", answer: q.type === "choice" ? (q.options || []).find((o: any) => o.id === q.correct)?.text : q.type === "tf" ? String(q.answer) : q.type === "wheel" ? q.phrase : q.type === "pin" ? q.place : q.type === "order" ? (q.items || []).map((i: any) => i.text).join(" → ") : q.type === "rhyme" ? [q.answer1, q.answer2].filter(Boolean).join(" / ") : q.type === "smash" ? q.smash || "" : q.type === "tune" ? `${q.track || ""} — ${q.artist || ""}` : (q.answers || [])[0] || "", category: q.category || "", tags: q.tags || [], used: q.used || null, pct: q.pct, rejected: !!q.used?.rejected, difficulty: q.difficulty || "", media: q.media?.kind && q.media.kind !== "none" ? q.media.kind : "" })) });
    }
    if (action === "bank_patch") {
      // Sets difficulty (and optionally category / tags) on bank items, matched by id or, failing that, by what
      // makes them the same question (bankKey), so a topic file with ratings can rate what it already imported.
      const type = String(body.type || "");
      const patches = (Array.isArray(body.patches) ? body.patches : []).slice(0, 500);
      if (!patches.length) return json({ error: "Nothing to change." }, 400);
      const row = await bankRow(type);
      const byKey = new Map<string, any>(); for (const q of row.questions) byKey.set(bankKey(q), q);
      let changed = 0, missing = 0;
      for (const p of patches) {
        const q = (p.id && row.questions.find((x: any) => x.id === p.id)) || byKey.get(bankKey({ ...p, type }));
        if (!q) { missing++; continue; }
        if (["easy", "medium", "hard"].includes(p.difficulty)) q.difficulty = p.difficulty;
        if (typeof p.newText === "string" && p.newText.trim()) q.text = p.newText.trim().slice(0, 200);
        if (typeof p.category === "string") q.category = p.category.slice(0, 60);
        if (typeof p.why === "string" && p.why.trim()) q.why = p.why.trim().slice(0, 300);
        if (Array.isArray(p.tags)) q.tags = p.tags.map((t: unknown) => String(t).slice(0, 40)).slice(0, 12);
        if (p.set && typeof p.set === "object") for (const k of ["perCorrect", "prize", "prize2", "prize3", "forfeit", "study", "time", "target"]) if (typeof p.set[k] === "number" && isFinite(p.set[k])) q[k] = Math.max(0, Math.min(50000, p.set[k]));
        changed++;
      }
      if (changed) await bankSave(row);
      return json({ ok: true, changed, missing });
    }
    if (action === "bank_move") {
      // Moves a category of items from one bank row to another (e.g. Catchphrase clips out of Type the answer).
      const from = await bankRow(String(body.from || "")), to = await bankRow(String(body.to || "")), cat = String(body.category || "");
      if (!cat || from.id === to.id) return json({ error: "Nothing to move." }, 400);
      const moving = from.questions.filter((q: any) => q.category === cat);
      if (!moving.length) return json({ moved: 0 });
      from.questions = from.questions.filter((q: any) => q.category !== cat);
      for (const q of moving) { if (body.kind) q.kind = String(body.kind).slice(0, 30); to.questions.push(q); }
      await bankSave(to); await bankSave(from);
      return json({ moved: moving.length });
    }
    if (action === "bank_get") {
      const type = String(body.type || ""), id = String(body.id || "");
      const row = (await bankRows(type)).find((r) => r.settings?.type === type);
      const q = row?.questions?.find((x: any) => x.id === id);
      if (!q) return json({ error: "That bank item no longer exists." }, 404);
      return json({ question: q });
    }
    if (action === "bank_restore") {
      // Back to fresh: clears the used stamp (rejected or not) so the item can go into a quiz again.
      const type = String(body.type || ""), id = String(body.id || "");
      const row = await bankRow(type);
      const q = row.questions.find((x: any) => x.id === id);
      if (!q) return json({ error: "That bank item no longer exists." }, 404);
      delete q.used; await bankSave(row);
      return json({ ok: true });
    }
    if (action === "bank_edit") {
      // Replaces a bank item's wording and answers (same id and category), for fixing rejected ones. An Answer Smash
      // gets a fresh picture when its picture answer changes; a tune gets a fresh clip when its song or artist changes.
      // "fresh" puts the item back into stock.
      const type = String(body.type || ""), id = String(body.id || "");
      const row = await bankRow(type);
      const i = row.questions.findIndex((x: any) => x.id === id);
      if (i < 0) return json({ error: "That bank item no longer exists." }, 404);
      const nq = body.question && typeof body.question === "object" ? body.question : null;
      if (!nq || (nq.type !== type && nq.kind !== type)) return json({ error: "Nothing to save." }, 400);
      const keep = row.questions[i];
      if (!String(nq.text || nq.phrase || nq.track || "").trim()) return json({ error: "The question needs some words." }, 400);
      if (nq.type === "race") {
        if (!Array.isArray(nq.bank) || nq.bank.length !== 20) return json({ error: "A race needs exactly 20 questions, so a player can get ten wrong and still finish." }, 400);
        nq.target = 10;
      }
      if (nq.type === "smash") {
        const pa = String(nq.pictureAnswer || "").trim(), ca = String(nq.clueAnswer || "").trim(), sm = smashOf(pa, ca);
        if (!pa || !ca || sm.overlap < 2) return json({ error: `“${pa}” and “${ca}” need to share at least two letters where they join.` }, 400);
        nq.pictureAnswer = pa; nq.clueAnswer = ca; nq.smash = sm.smash;
        if (norm(pa) !== norm(keep.pictureAnswer || "") || !nq.media?.url) {
          const pic = await wikiPicture(pa, new Set(), true);
          if (!pic) return json({ error: `No picture of “${pa}” on Wikipedia. Try the article's exact name.` }, 404);
          nq.media = { kind: "image", url: pic.url, source: pic.source, credit: `Wikipedia / Wikimedia Commons: ${pa}` };
        }
      }
      if (nq.type === "tune" && (norm(nq.track || "") !== norm(keep.track || "") || norm(nq.artist || "") !== norm(keep.artist || ""))) {
        const track = String(nq.track || "").trim(), artist = String(nq.artist || "").trim();
        const hit = track && artist ? await tuneLookup(`${track} ${artist}`, track, artist) : null;
        if (!hit) return json({ error: `No preview of “${track}” by ${artist} could be found. Check the spelling.` }, 404);
        nq.media = { ...(keep.media || {}), kind: "audio", url: hit.previewUrl, artwork: hit.artwork, start: 0, credit: "Preview via Apple Music" };
        if (hit.year) nq.year = hit.year;
        const lead = nq.ask === "artist" ? hit.artist : nq.ask === "song" ? cleanTitle(hit.track) : nq.ask === "year" && hit.year ? String(hit.year) : "";
        if (lead) nq.answers = [lead, ...(Array.isArray(nq.answers) ? nq.answers : []).filter((a: any) => norm(String(a)) !== norm(lead) && nq.ask !== "year")];
      }
      row.questions[i] = { ...nq, id, category: keep.category, tags: keep.tags, used: keep.used };
      if (body.fresh) delete row.questions[i].used;
      await bankSave(row);
      return json({ ok: true, question: row.questions[i] });
    }
    if (action === "bank_reject") {
      // "I don't like this question": the bank item it came from (or the question itself, added to the bank)
      // is stamped used + rejected, so it never comes round again but can be reviewed and improved later.
      const q = body.question && typeof body.question === "object" ? body.question : null;
      if (!q || !q.type) return json({ error: "Nothing to reject." }, 400);
      if (RACE_GAMES[String(q.type)] || q.type === "draw") return json({ ok: true, skipped: true }); // these games keep no bank rows of their own
      const quizId = UUID_RE.test(String(body.quizId || "")) ? String(body.quizId) : "";
      const row = await bankRow(String(q.kind || q.type));
      const at = new Date().toISOString();
      let item = row.questions.find((x: any) => x.id === q.bankId) || row.questions.find((x: any) => nearDuplicate(x, q));
      let added = false;
      if (!item) {
        item = { ...q, id: "q_" + crypto.randomUUID().replace(/-/g, "").slice(0, 8), category: String(body.category || q.category || "").slice(0, 60), tags: (q.tags || []).slice(0, 12) };
        delete item.fromBank; delete item.round; delete item.bankId; delete item.check;
        row.questions.push(item); added = true;
      }
      item.used = { quiz: quizId, at, rejected: true, note: String(body.note || "").slice(0, 200) };
      await bankSave(row);
      return json({ ok: true, id: item.id, added });
    }
    if (action === "bank_pass") {
      // "Not the one I want" (as opposed to "bad question"): the question goes back into stock unused, or is added
      // as new stock if the AI wrote it, and is marked passed-over for this quiz so the swap brings a different one.
      const q = body.question && typeof body.question === "object" ? body.question : null;
      if (!q || !q.type) return json({ error: "Nothing to pass on." }, 400);
      if (RACE_GAMES[String(q.type)] || q.type === "draw") return json({ ok: true, skipped: true }); // these games keep no bank rows of their own
      const quizId = UUID_RE.test(String(body.quizId || "")) ? String(body.quizId) : "";
      const row = await bankRow(String(q.kind || q.type));
      let item = row.questions.find((x: any) => x.id === q.bankId) || row.questions.find((x: any) => nearDuplicate(x, q));
      let added = false;
      if (!item) {
        const cat0 = String(body.category || q.category || "").trim();
        item = { ...q, id: "q_" + crypto.randomUUID().replace(/-/g, "").slice(0, 8), category: (junkCategory(cat0) ? "" : cat0).slice(0, 60), tags: (q.tags || []).slice(0, 12) };
        delete item.fromBank; delete item.round; delete item.bankId; delete item.check;
        if (item.type === "race") Object.assign(item, { perCorrect: 100, prize: 500, prize2: 200, prize3: 100, forfeit: 200 });
        row.questions.push(item); added = true;
      }
      if (!item.used?.rejected) delete item.used;
      if (quizId) item.passed = [...new Set([...(Array.isArray(item.passed) ? item.passed : []), quizId])].slice(-20);
      await bankSave(row);
      return json({ ok: true, id: item.id, added });
    }
    if (action === "bank_restock") {
      // Puts a finished quiz's questions back into stock and deletes the quiz: bank-sourced ones go back to
      // unused, AI-written ones are added (skipping anything that is already in the bank or near enough).
      const id = String(body.id || "");
      if (!UUID_RE.test(id)) return json({ error: "Bad quiz id." }, 400);
      const rows = await rest(`quiz_quizzes?id=eq.${id}&select=*`);
      const quiz = rows?.[0];
      if (!quiz) return json({ error: "That quiz no longer exists." }, 404);
      if (quiz.settings?.bank) return json({ error: "That is a bank row, not a quiz." }, 400);
      const roundTitle = (rid: string) => String((Array.isArray(quiz.settings?.rounds) ? quiz.settings.rounds : []).find((r: any) => r?.id === rid)?.title || "");
      const banks = await bankRows();
      const out: Record<string, { restored: number; added: number; skipped: number }> = {};
      const touched = new Set<any>();
      // 1. anything this quiz took from the bank goes back to fresh (rejected stays rejected)
      for (const row of banks) for (const q of row.questions || []) if (q.used && q.used.quiz === id && !q.used.rejected) { delete q.used; touched.add(row); const t = row.settings.type; out[t] = out[t] || { restored: 0, added: 0, skipped: 0 }; out[t].restored++; }
      // 2. everything the writer made goes in as new stock, with a duplicate check against the whole bank of its type
      for (const q of (Array.isArray(quiz.questions) ? quiz.questions : [])) {
        if (!q || !q.type || q.type === "slide" || q.type === "draw" || RACE_GAMES[q.type]) continue; // slides are not questions, and the race-bank games have no bank rows of their own
        const t = String(q.kind || q.type); out[t] = out[t] || { restored: 0, added: 0, skipped: 0 };
        if (q.fromBank || q.bankId) continue; // already counted under restored
        let row = banks.find((r) => r.settings?.type === t);
        if (!row) { row = await bankRow(t); banks.push(row); }
        const key = bankKey(q);
        if (!key || row.questions.some((x: any) => nearDuplicate(x, q))) { out[t].skipped++; continue; }
        const cat0 = String(q.category || roundTitle(q.round) || "").trim();
        const c = { ...q, id: "q_" + crypto.randomUUID().replace(/-/g, "").slice(0, 8), category: (junkCategory(cat0) ? "" : cat0).slice(0, 60), tags: (q.tags || []).slice(0, 12) };
        if (c.type === "race") Object.assign(c, { perCorrect: 100, prize: 500, prize2: 200, prize3: 100, forfeit: 200 });
        delete c.used; delete c.fromBank; delete c.round; delete c.bankId; delete c.check;
        row.questions.push(c); touched.add(row); out[t].added++;
      }
      for (const row of touched) await bankSave(row); // a full part spills into a new one
      if (body.keep !== true) await rest(`quiz_quizzes?id=eq.${id}`, { method: "DELETE" });
      return json({ ok: true, title: quiz.title, deleted: body.keep !== true, result: out });
    }
    if (action === "bank_delete") {
      const type = String(body.type || ""), id = String(body.id || "");
      const row = await bankRow(type);
      const before = row.questions.length;
      row.questions = row.questions.filter((q: any) => q.id !== id);
      if (row.questions.length !== before) await bankSave(row);
      return json({ ok: true, removed: before - row.questions.length });
    }
    if (action === "bank_import") {
      // Raw items in the writer's JSON shape (plus category/tags); finished here so pictures, maps and clips are resolved once.
      const type = String(body.type || "");
      const items = (Array.isArray(body.items) ? body.items : []).slice(0, 60).map((r: any) => ({ ...r, type }));
      if (!items.length) return json({ error: "Nothing to import." }, 400);
      const { questions, warnings } = await finishRaw(items, items.length, [], true);
      const row = await bankRow(type);
      const keyOf = bankKey, rawKey = bankKey;
      const have = new Set(row.questions.map(keyOf));
      let added = 0;
      questions.forEach((q: any, n: number) => {
        const key = keyOf(q);
        if (!key || have.has(key) || row.questions.some((x: any) => nearDuplicate(x, q))) return;
        have.add(key);
        const src = items.find((r: any) => rawKey(r) === key) || items[n] || {};
        q.category = String(src.category || "").slice(0, 60); q.tags = (Array.isArray(src.tags) ? src.tags : []).map((t: unknown) => String(t).slice(0, 40)).slice(0, 12);
        row.questions.push(q); added++;
      });
      await bankSave(row);
      return json({ added, skipped: items.length - added, warnings, total: row.questions.length });
    }
    if (action === "bank_add") {
      // Already-finished questions (from the writer) go straight into the bank under a topic.
      const type = String(body.type || "");
      const category = String(body.category || "").slice(0, 60);
      const tags = (Array.isArray(body.tags) ? body.tags : []).map((t: unknown) => String(t).slice(0, 40)).slice(0, 12);
      const qs = (Array.isArray(body.questions) ? body.questions : []).filter((q: any) => q && (q.type === type || q.kind === type)).slice(0, 40);
      if (!qs.length) return json({ error: "Nothing to add." }, 400);
      const row = await bankRow(type);
      const keyOf = bankKey;
      const have = new Set(row.questions.map(keyOf));
      let added = 0;
      for (const q of qs) {
        const key = keyOf(q); if (!key || have.has(key) || row.questions.some((x: any) => nearDuplicate(x, q))) continue;
        have.add(key);
        const c = { ...q, id: "q_" + crypto.randomUUID().replace(/-/g, "").slice(0, 8), category, tags: [...new Set([...(q.tags || []), ...tags])] };
        delete c.used; delete c.fromBank; delete c.round;
        row.questions.push(c); added++;
      }
      if (added) await bankSave(row);
      return json({ added, skipped: qs.length - added, total: row.questions.length });
    }
    if (action === "tune_search") {
      const term = String(body.term || "").trim().slice(0, 120);
      if (!term) return json({ error: "What song?" }, 400);
      return json({ results: await tuneSearch(term, 8) });
    }

    if (action === "picture") {
      const title = String(body.title || "").trim().slice(0, 120);
      if (!title) return json({ error: "What should the picture be of?" }, 400);
      const used = new Set<string>((Array.isArray(body.usedPictures) ? body.usedPictures : []).map((s: unknown) => String(s ?? "")));
      const pic = await wikiPicture(title, used);
      if (!pic) return json({ error: `No usable picture of “${title}” on Wikipedia. Try the article's exact title, or upload one.` }, 404);
      return json({ url: pic.url, source: pic.source });
    }

    if (action === "map") {
      const region = String(body.region || "").slice(0, 80);
      if (!region.trim()) return json({ error: "Which place?" }, 400);
      const map = await locationMap(region);
      if (!map) return json({ error: `No blank map of “${region}” could be found. Try the country or continent's usual English name, or “World”.` }, 404);
      return json({ url: map.url, region: map.name, bounds: map.bounds || null });
    }

    if (action === "more_wipeout") {
      // A Wipeout board needs more right answers than there are players. Asked for at game time once the host knows how many joined.
      if (!ANTHROPIC_KEY) return json({ error: "AI is not set up on the server." }, 503);
      const text = String(body.text || "").slice(0, 300);
      const right = (Array.isArray(body.right) ? body.right : []).map((s: unknown) => String(s ?? "").trim()).filter(Boolean).slice(0, 60);
      const wrong = (Array.isArray(body.wrong) ? body.wrong : []).map((s: unknown) => String(s ?? "").trim()).filter(Boolean).slice(0, 30);
      const need = Math.min(25, Math.max(1, Math.round(+body.need || 5)));
      if (!text) return json({ error: "No question." }, 400);
      const msg = await ask(anthropic(), {
        model: SONNET, max_tokens: 4000, output_config: { effort: "medium" },
        system: `You add answers to a Wipeout quiz board. The board is a list question; every answer on it must be short (a name or a few words) and either definitely fit the question or definitely not. You are asked for MORE answers that definitely fit. Verify with web search when unsure — one that does not truly fit ruins the round. Never repeat anything already on the board, in any spelling. Reply with JSON only: {"right":["..."]}`,
        messages: [{ role: "user", content: `Question: ${text}\nAlready on the board as RIGHT: ${right.join(" | ")}\nAlready on the board as WRONG: ${wrong.join(" | ")}\nGive ${need} more answers that definitely fit, most famous first.` }],
      });
      const out = extractJson(textOf(msg));
      const have = new Set([...right, ...wrong].map(norm));
      const extra = (Array.isArray(out?.right) ? out.right : []).map((s: unknown) => String(s ?? "").trim().slice(0, 60)).filter((s: string) => s && !have.has(norm(s)) && have.add(norm(s))).slice(0, need);
      return json({ right: extra });
    }

    if (action === "verify") {
      if (!ANTHROPIC_KEY) return json({ error: "AI is not set up on the server yet — add ANTHROPIC_API_KEY as a Supabase secret." }, 503);
      const items = (Array.isArray(body.questions) ? body.questions : [])
        .filter((q: any) => q && typeof q.id === "string" && typeof q.summary === "string")
        .slice(0, 6)
        .map((q: any) => ({ id: q.id.slice(0, 40), summary: q.summary.slice(0, 6000) }));
      if (!items.length) return json({ error: "Nothing to check." }, 400);
      return json(await verifyQuestions(items, body.premium === true));
    }

    if (action === "save_game") {
      const g = body.game || {};
      const report = g.report && typeof g.report === "object" ? g.report : null;
      if (report && JSON.stringify(report).length > 4_000_000) return json({ error: "That game's report is too large to save." }, 413);
      const rows = await rest(`quiz_games`, { method: "POST", headers: { Prefer: "return=representation" }, body: JSON.stringify({
        code: String(g.code || "").slice(0, 12),
        quiz_id: UUID_RE.test(String(g.quiz_id)) ? g.quiz_id : null,
        title: String(g.title || "").slice(0, 120),
        players: Array.isArray(g.players) ? g.players.slice(0, 500) : [],
        questions: Math.max(0, Math.round(+g.questions || 0)),
        started_at: g.started_at || null,
        report,
      }) });
      return json({ ok: true, id: rows?.[0]?.id || null });
    }

    if (action === "games") {
      const rows = await rest(`quiz_games?select=id,code,quiz_id,title,players,questions,started_at,ended_at&order=ended_at.desc&limit=100`);
      return json({ games: rows || [] });
    }

    if (action === "game") {
      if (!UUID_RE.test(String(body.id))) return json({ error: "Bad game id." }, 400);
      const rows = await rest(`quiz_games?id=eq.${body.id}&select=*`);
      if (!rows?.[0]) return json({ error: "That game record no longer exists." }, 404);
      return json({ game: rows[0] });
    }

    return json({ error: "Unknown action." }, 400);
  } catch (e) {
    console.error(e);
    return json({ error: friendly(String((e as Error)?.message || e)) }, 500);
  }
});

// ---------------------------------------------------------------- Kahoot import
function kahootId(s: string): string { const m = String(s || "").match(/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/i); return m ? m[0].toLowerCase() : ""; }
const unhtml = (s: unknown) => String(s ?? "").replace(/<br\s*\/?>/gi, " ").replace(/<[^>]+>/g, "").replace(/&nbsp;/g, " ").replace(/&amp;/g, "&").replace(/&quot;/g, '"').replace(/&#0?39;|&apos;/g, "'").replace(/&lt;/g, "<").replace(/&gt;/g, ">").replace(/\s+/g, " ").trim();
/** One Kahoot slide in the writer's raw shape, or null for slides with no quiz equivalent (polls, word clouds, content). */
function kahootRaw(k: any): any | null {
  const text = unhtml(k.question || k.title), time = Math.max(5, Math.min(120, Math.round((+k.time || 20000) / 1000)));
  const ch = (Array.isArray(k.choices) ? k.choices : []).map((c: any) => ({ t: unhtml(c.answer), ok: !!c.correct })).filter((c: any) => c.t);
  if (!text) return null;
  if (k.type === "quiz" || k.type === "multiple_select_quiz") {
    if (ch.length < 2 || !ch.some((c: any) => c.ok)) return null;
    const right = ch.find((c: any) => c.ok).t, rest = ch.filter((c: any) => c.t !== right).map((c: any) => c.t);
    if (ch.length === 2 && ch.every((c: any) => /^(true|false)$/i.test(c.t))) return { type: "tf", text, answer: /^true$/i.test(right), time };
    return { type: "choice", text, options: [right, ...rest].slice(0, 4), answer: right, time };
  }
  if (k.type === "true_false") { const right = ch.find((c: any) => c.ok)?.t || ""; return /^(true|false)$/i.test(right) ? { type: "tf", text, answer: /^true$/i.test(right), time } : null; }
  if (k.type === "open_ended") return ch.length ? { type: "text", text, answers: ch.map((c: any) => c.t), time } : null;
  if (k.type === "jumble") return ch.length >= 2 ? { type: "order", text, items: ch.map((c: any) => c.t), hint: "", time } : null;
  return null;
}
async function kahootFinish(raws: { raw: any; image?: string }[]): Promise<any[]> {
  const out: any[] = [];
  for (const { raw, image } of raws) {
    const { questions } = await finishRaw([raw], 1, [], false);
    const q = questions[0]; if (!q) continue;
    q.time = raw.time; if (raw.kn) q.kn = raw.kn; if (raw.kpic) q.kpic = raw.kpic; if (raw.kvideo) q.kvideo = true;
    if (image) q.media = { kind: "image", url: image, credit: "Kahoot" };
    out.push(q);
  }
  return out;
}
async function kahootFetch(uuid: string): Promise<{ title: string; description: string; questions: any[]; skipped: number } | null> {
  try {
    const r = await fetch(`https://create.kahoot.it/rest/kahoots/${uuid}`, { headers: { accept: "application/json" } });
    if (!r.ok) return null;
    const d = await r.json();
    const slides = Array.isArray(d.questions) ? d.questions : [];
    const raws = slides.map((k: any) => ({ raw: kahootRaw(k), image: typeof k.image === "string" && /^https:\/\//.test(k.image) ? k.image : undefined })).filter((x: any) => x.raw);
    return { title: unhtml(d.title) || "Kahoot quiz", description: unhtml(d.description), questions: await kahootFinish(raws), skipped: slides.length - raws.length };
  } catch { return null; }
}
/** Claude reads printed Kahoot pages: every question, its answers in screen order, which are ticked, and the page link. */
async function kahootRead(pages: string[]): Promise<any> {
  const content: any[] = pages.map((p) => { const m = p.match(/^data:(image\/(?:jpeg|png|webp));base64,(.+)$/); return m ? { type: "image", source: { type: "base64", media_type: m[1], data: m[2] } } : null; }).filter(Boolean);
  if (!content.length) throw new Error("The PDF pages could not be read.");
  content.push({ type: "text", text: `These are the pages of a Kahoot quiz, printed from Kahoot's website. Read every question slide in order across all pages and reply with JSON only, no prose:
{"title":"the quiz title","url":"the create.kahoot.it link printed in the page header or footer, copied exactly character by character, or null","questions":[{"n":1,"type":"quiz | true_false | type_answer | puzzle | poll | other","question":"the question wording, exactly","answers":["answers in screen order: top-left, top-right, bottom-left, bottom-right"],"correct":[0-based indexes of the answers marked with a tick],"page":1,"picture":[0.1,0.2,0.3,0.4],"video":false}]}
"page" is which image the slide is on (1 = the first image). "picture" is the box around the photo or drawing inside that slide, as [left, top, right, bottom] fractions (0 to 1) of that whole image's width and height, drawn tightly round the picture itself and not the purple background, or null when the slide has no picture. "video" is true when the slide shows "Video no longer supported" in place of its media.
"n" is the slide number printed above each slide (as in "7 - Quiz"). Copy wording exactly as printed, including capitals. Skip nothing, except a slide cut off at the top or bottom edge of a page whose answers you cannot fully see.` });
  const msg = await anthropic().messages.create({ model: SONNET, max_tokens: 16000, messages: [{ role: "user", content }] });
  const t = textOf(msg); const j = t.slice(t.indexOf("{"), t.lastIndexOf("}") + 1);
  let read: any; try { read = JSON.parse(j); } catch { throw new Error("The PDF could not be read as a Kahoot. Try a clearer printout, or paste the Kahoot's link."); }
  read.usage = usageOf(msg, SONNET);
  return read;
}
async function kahootFromRead(read: any): Promise<{ title: string; description: string; questions: any[]; skipped: number }> {
  const slides = Array.isArray(read.questions) ? read.questions : [];
  const raws = slides.map((q: any) => {
    const answers = (Array.isArray(q.answers) ? q.answers : []).map((a: unknown) => String(a ?? "").trim()).filter(Boolean);
    const correct = (Array.isArray(q.correct) ? q.correct : []).map((n: any) => +n).filter((n: number) => n >= 0 && n < answers.length);
    const type = q.type === "true_false" ? "true_false" : q.type === "type_answer" ? "open_ended" : q.type === "puzzle" ? "jumble" : q.type === "quiz" ? "quiz" : "other";
    const raw = kahootRaw({ type, question: q.question, time: 20000, choices: answers.map((a: string, i: number) => ({ answer: a, correct: type === "jumble" || type === "open_ended" || correct.includes(i) })) });
    if (raw && +q.n > 0) raw.kn = Math.round(+q.n); // the slide number, so pages read in batches can be stitched back together
    const box = Array.isArray(q.picture) && q.picture.length === 4 && q.picture.every((v: any) => isFinite(+v) && +v >= 0 && +v <= 1) ? q.picture.map(Number) : null;
    if (raw && box && box[2] - box[0] > 0.02 && box[3] - box[1] > 0.02 && +q.page >= 1) raw.kpic = { page: (read.offset || 0) + Math.round(+q.page) - 1, box };
    if (raw && q.video === true) raw.kvideo = true;
    return { raw };
  }).filter((x: any) => x.raw);
  return { title: String(read.title || "Kahoot quiz").trim(), description: "", questions: await kahootFinish(raws), skipped: slides.length - raws.length };
}

// ---------------------------------------------------------------- the question bank
//
// Pre-written questions, one quiz_quizzes row per type flagged settings.bank = true, so no new
// table is needed. Each item carries category/tags for matching a themed round and a "used"
// stamp once it has gone into a quiz, so it never comes round again.
const BANK_LOW = 25;
const EVERGREEN = ["club", "dingbat", "wheel", "pin", "tune", "catchphrase", "twenty"]; // theme-free types: any unused item will do when the round has no matching one
/** What makes two items "the same": the phrase for dingbats and wheels, the place for pins, the track for tunes, the wording otherwise. */
function bankKey(q: any): string { if (q?.media?.kind === "youtube" && q.media.videoId) return "yt:" + q.media.videoId; if (q?.media?.kind === "image" && q.media.source && /which .*(flag|picture|this)/i.test(q.text || "")) return "img:" + q.media.source; return norm(q?.type === "dingbat" || q?.type === "twenty" ? (q.answers || [])[0] || "" : q?.type === "tune" ? `${q.track} ${q.artist}` : q?.type === "pin" ? q.place || q.text : q?.phrase || q?.text || ""); }
/** The right answer of a finished question, as plain text, for near-duplicate checks. */
function bankAnswer(q: any): string {
  if (!q) return "";
  if (q.type === "choice") return String((q.options || []).find((o: any) => o.id === q.correct)?.text || "");
  if (q.type === "tf") return String(q.answer);
  if (q.type === "wheel") return String(q.phrase || "");
  if (q.type === "pin") return String(q.place || "");
  if (q.type === "tune") return `${q.track} ${q.artist}`;
  if (q.type === "smash") return `${q.pictureAnswer} ${q.clueAnswer}`;
  if (q.type === "order" || q.type === "sort" || q.type === "match") return (q.items || q.pairs || []).map((i: any) => i.text || i.left || "").join(" ");
  if (q.type === "wipeout") return (q.right || []).map((i: any) => i.text || "").join(" ");
  if (q.type === "race") return (q.bank || []).map((b: any) => b.text || "").join(" ");
  return String((q.answers || [])[0] || "");
}
const DUP_STOP = new Set(["which", "what", "who", "where", "when", "this", "that", "these", "those", "from", "with", "does", "were", "was", "the", "and", "for", "has", "have", "had", "his", "her", "their", "its", "into", "name", "called", "many", "much", "following"]);
const tokens = (s: string) => new Set(norm(s).split(" ").filter((w) => w.length >= 3 && !DUP_STOP.has(w)));
/** True when two items ask the same thing another way: same answer and most of the same words, or nearly identical wording. */
function nearDuplicate(a: any, b: any): boolean {
  if (a.type !== b.type) return false;
  const ka = bankKey(a), kb = bankKey(b);
  if (ka && ka === kb) return true;
  // Rounds made of lists all read alike ("Put these in order, earliest first"): what makes them the same is their items.
  if (a.type === "twenty") return false; // one answer each: the same answer already has the same key
  if (["order", "sort", "match", "wipeout", "race"].includes(a.type)) { const x = norm(bankAnswer(a)), y = norm(bankAnswer(b)); return !!x && x === y; }
  if (a.type === "pin") return false; // a pin is its place: Brighton Palace Pier is not Brighton, Washington Old Hall is not Washington, D.C.
  if (ka.startsWith("img:") || kb.startsWith("img:") || ka.startsWith("yt:") || kb.startsWith("yt:")) return false; // different picture or clip = different question
  const ta = tokens(ka), tb = tokens(kb);
  if (!ta.size || !tb.size) return false;
  let shared = 0; for (const w of ta) if (tb.has(w)) shared++;
  const overlap = shared / Math.min(ta.size, tb.size);
  const sameAnswer = a.type !== "tf" && ta.size >= 3 && tb.size >= 3 && norm(bankAnswer(a)) === norm(bankAnswer(b)) && norm(bankAnswer(a)).length > 1;
  return overlap >= 0.8 || (sameAnswer && overlap >= 0.5);
}
// A type's bank can outgrow one row (multiple choice passed 4,000 items), so it lives in parts: rows with the same
// settings.type and a settings.part number. bankRows() hands back ONE merged row per type, holding every part's
// questions in order; bankSave() puts each question back in the part it came from and adds new ones to the last
// part, opening another part when that one is full. Everything else works on the merged row as before.
const BANK_PART_MAX = 1_800_000; // characters of JSON per part
const BANK_LABEL: Record<string, string> = { choice: "Multiple choice", text: "Type the answer", order: "Put in order", pin: "Drop the pin", match: "Match up", tf: "True or false", sort: "Categorise", wipeout: "Wipeout", race: "The Race", smash: "Answer Smash", wheel: "Wheel of Fortune", highlow: "Highbrow Lowbrow", rhyme: "Rhyme Time", club: "The 1% Club", catchphrase: "Catchphrase", dingbat: "Dingbats", tune: "Name That Tune", nearest: "Nearest Wins", draw: "Draw It", twenty: "20 Questions" };
// Pass a type to fetch just that type's parts: the whole bank is tens of MB and reading it all can hit the statement timeout.
async function bankRows(type?: string): Promise<any[]> {
  const one = async (t: string) => (await rest(`quiz_quizzes?settings->>bank=eq.true&settings->>type=eq.${encodeURIComponent(t)}&select=id,title,settings,questions`)) || [];
  let raw: any[];
  if (type) raw = await one(type);
  else { const types = [...new Set(((await rest(`quiz_quizzes?settings->>bank=eq.true&select=settings`)) || []).map((r: any) => String(r.settings?.type || "")))]; raw = []; for (const t of types) raw.push(...await one(t)); }
  const byType = new Map<string, any[]>();
  for (const r of raw) { const t = String(r.settings?.type || ""); if (!byType.has(t)) byType.set(t, []); byType.get(t)!.push(r); }
  return [...byType.entries()].map(([type, parts]) => {
    parts.sort((a, b) => (+a.settings?.part || 0) - (+b.settings?.part || 0));
    for (const p of parts) { p.questions = Array.isArray(p.questions) ? p.questions : []; p._orig = JSON.stringify(p.questions); }
    return { id: parts[0].id, title: parts[0].title, settings: { ...parts[0].settings, type }, questions: parts.flatMap((p) => p.questions), _parts: parts };
  });
}
async function bankNewPart(type: string, part: number): Promise<any> {
  const made = await rest(`quiz_quizzes`, { method: "POST", headers: { Prefer: "return=representation" }, body: JSON.stringify({ title: `Question bank: ${BANK_LABEL[type] || type}${part ? ` (part ${part + 1})` : ""}`, settings: { bank: true, type, ...(part ? { part } : {}) }, questions: [] }) });
  const row = Array.isArray(made) ? made[0] : made;
  row.questions = []; row._orig = "[]";
  return row;
}
async function bankRow(type: string): Promise<any> {
  const row = (await bankRows(type)).find((r) => r.settings?.type === type);
  if (row) return row;
  const first = await bankNewPart(type, 0);
  return { id: first.id, title: first.title, settings: { ...first.settings, type }, questions: [], _parts: [first] };
}
async function bankSave(row: any) {
  const parts: any[] = row._parts || [{ ...row, _orig: "" }];
  const home = new Map<string, number>();
  parts.forEach((p, i) => { for (const q of JSON.parse(p._orig || "[]")) if (q?.id) home.set(q.id, i); });
  const lists: any[][] = parts.map(() => []), fresh: any[] = [];
  for (const q of row.questions) { const i = q?.id ? home.get(q.id) : undefined; if (i === undefined) fresh.push(q); else lists[i].push(q); }
  for (const q of fresh) {
    let last = lists.length - 1;
    if (JSON.stringify(lists[last]).length + JSON.stringify(q).length > BANK_PART_MAX) {
      parts.push(await bankNewPart(String(row.settings?.type || ""), (+parts[last].settings?.part || 0) + 1)); lists.push([]); last++;
    }
    lists[last].push(q);
  }
  for (let i = 0; i < parts.length; i++) {
    const json = JSON.stringify(lists[i]);
    if (json === parts[i]._orig) continue;
    await rest(`quiz_quizzes?id=eq.${parts[i].id}`, { method: "PATCH", body: JSON.stringify({ questions: lists[i], updated_at: new Date().toISOString() }) });
    parts[i].questions = lists[i]; parts[i]._orig = json;
  }
  row._parts = parts;
}
function bankStatus(rows: any[]) {
  const out: Record<string, { total: number; unused: number; low: boolean; mix: Record<string, number> }> = {};
  for (const r of rows) {
    const qs = Array.isArray(r.questions) ? r.questions : []; const fresh = qs.filter((q: any) => !q.used);
    const mix = { easy: 0, medium: 0, hard: 0, unrated: 0 }; for (const q of fresh) mix[(["easy", "medium", "hard"].includes(q.difficulty) ? q.difficulty : "unrated") as keyof typeof mix]++;
    out[r.settings.type] = { total: qs.length, unused: fresh.length, low: fresh.length < BANK_LOW, mix };
  }
  return out;
}
/** The same counts cut by category (the topic an item was written for), with how many of each type it holds. */
function bankCategories(rows: any[]) {
  const out: Record<string, { total: number; unused: number; mix: Record<string, number>; types: Record<string, { total: number; unused: number }> }> = {};
  for (const r of rows) {
    const type = r.settings.type;
    for (const q of Array.isArray(r.questions) ? r.questions : []) {
      const c = out[q.category || ""] ||= { total: 0, unused: 0, mix: { easy: 0, medium: 0, hard: 0, unrated: 0 }, types: {} };
      const t = c.types[type] ||= { total: 0, unused: 0 };
      c.total++; t.total++;
      if (q.used) continue;
      c.unused++; t.unused++;
      c.mix[["easy", "medium", "hard"].includes(q.difficulty) ? q.difficulty : "unrated"]++;
    }
  }
  return out;
}
const WORD = (s: string) => new Set(norm(s).split(" ").filter((w) => w.length >= 4));
/** Words in a round's title or brief that say nothing about its theme ("Round 1", "questions about the show"). */
const THEME_STOP = new Set(["round", "rounds", "quiz", "quizzes", "question", "questions", "about", "based", "show", "shows", "series", "programme", "program", "from", "with", "that", "this", "these", "those", "their", "there", "what", "which", "some", "more", "most", "only", "mixed", "general", "knowledge", "trivia", "easy", "hard", "medium", "difficult", "tricky", "family", "friendly", "answer", "answers", "each", "every", "make", "made", "write", "include", "including", "like", "also", "just", "plus", "other", "things", "stuff", "anything", "everything", "famous", "popular", "classic", "best", "good", "great", "topic", "theme", "themed", "fun", "please", "want", "should", "would", "could", "about", "into", "over", "under", "your", "them", "they", "have", "been", "will", "than", "then", "when", "where", "while", "people", "players", "player", "team", "teams", "night", "tonight", "week", "weekly", "new", "untitled", "incorrect", "correct", "wrong", "right", "often", "think", "thinks", "thought", "actually", "really", "commonly", "usually", "mistake", "mistaken", "mistakes", "confuse", "confused", "trick", "tricks", "trap", "traps", "option", "options", "similar", "include", "includes", "adding", "fake", "real", "list", "lists", "ones", "called", "sound", "sounds", "instead", "rather", "though", "wipeout", "race", "smash", "catchphrase", "dingbat", "dingbats"]);
const JUNK_CATEGORY = /^(round\s*\d*|new quiz|untitled.*|ai quiz|quiz|general|test.*)$/i;
/** The games' own names. A round called "Wipeout" says which game it is, not what it is about, so these never count as a theme. */
const GAME_NAME = /^(the\s+)?(wipeout|race|hot potato|king of the hill|blockbusters|the chase|chase|answer smash|smash|wheel of fortune|wheel|dingbats?|catchphrase|rhyme time|highbrow,? lowbrow|1% club|one per ?cent club|name that tune|multiple choice|true or false|true\/false|type the answer|put in order|drop the pin|match up|categorise|categorize|nearest wins|draw it)( round)?$/i;
const junkCategory = (c: string) => JUNK_CATEGORY.test(c) || GAME_NAME.test(c.trim());
/** Games built on a race's bank of quick questions, with the settings each starts with. They never get bank rows of their own. */
const RACE_GAMES: Record<string, { label: string; set: () => Record<string, unknown> }> = {
  potato: { label: "Hot Potato", set: () => ({ fuseMin: 40, fuseMax: 90, perCorrect: 50, penalty: 300, time: 90 }) },
  koth: { label: "King of the Hill", set: () => ({ target: 3, prize: 1000, answerSecs: 3, perPoint: 100, maxRounds: 12, time: 15 }) },
  chase: { label: "The Chase", set: () => ({ headStart: 2, target: 5, teamPrize: 1000, chaserPrize: 200, time: 15 }) },
  blockbusters: { label: "Blockbusters", set: () => ({ teams: [{ name: "Newcastle", color: "#f2f2f2" }, { name: "Sunderland", color: "#e21b3c" }], hexPoints: 50, prize: 500, time: 20 }) },
};
/** A race (from the bank or freshly written) reshaped into one of those games: same questions, the game's own title and settings. */
function raceToGame(q: any, game: string) {
  const set = RACE_GAMES[game].set();
  const c = { ...q, type: game, ...set };
  for (const k of ["target", "maxWrong", "perCorrect", "prize", "prize2", "prize3", "forfeit"]) if (!(k in set)) delete c[k];
  c.text = `${RACE_GAMES[game].label}: ${String(q.text || "").replace(/^the race\s*[:\-–—]\s*/i, "").trim() || "quick-fire questions"}`;
  return c;
}
const GENERIC = /general knowledge|anything|mixed bag|pot ?luck|pub quiz|warm.?up|quick.?fire|random/i;
/** Takes up to `need` unused bank questions of a type for a quiz, preferring ones that match the round's topic and brief. */
async function bankTake(type: string, need: number, topic: string, brief: string, quizId: string, difficulty = "mixed", info: any = {}): Promise<any[]> {
  if (need <= 0) return [];
  // The builder sends "Round title. Brief": drop a title that is only a game's name, so the brief decides.
  const lead = topic.split(/[.:]/)[0].trim();
  if (GAME_NAME.test(lead)) topic = topic.slice(topic.indexOf(lead) + lead.length).replace(/^[\s.:–-]+/, "");
  const row = await bankRow(type);
  const qs: any[] = Array.isArray(row.questions) ? row.questions : [];
  const themed = !!(topic || brief).trim() && !GENERIC.test(topic + " " + brief) && (topic + " " + brief).trim().length > 3;
  const fresh = qs.filter((q) => !q.used && !(quizId && Array.isArray(q.passed) && q.passed.includes(quizId)));
  const haveOf = (q: any) => WORD([q.category, ...(q.tags || []), q.text, q.place, q.phrase, ...(q.answers || [])].filter(Boolean).join(" "));
  const haves = new Map(fresh.map((q) => [q, haveOf(q)]));
  // A word counts only when it is specific: not a filler word, and not one that turns up across a big slice of the
  // bank (so "Dexter" pulls Dexter questions, while "round" or "show" pull nothing).
  const common = Math.max(8, Math.round(fresh.length * 0.03));
  const want = new Set([...WORD(topic + " " + brief)].filter((w) => !THEME_STOP.has(w) && [...haves.values()].filter((h) => h.has(w)).length <= common));
  const text = " " + norm(topic + " " + brief) + " ";
  const score = (q: any) => {
    let sc = 0; const cat = norm(q.category || "");
    if (cat.length >= 4 && !junkCategory(cat) && !THEME_STOP.has(cat) && text.includes(" " + cat + " ")) sc += 3;
    // The item's own wording inside the brief ("US states" in "US states, with some cities as traps") is the strongest sign.
    const own = norm(q.text || ""); if (own.length >= 6 && text.includes(" " + own + " ")) sc += 3;
    const have = haves.get(q) || haveOf(q); for (const w of want) if (have.has(w)) sc += 1; return sc;
  };
  let pool = fresh.map((q) => ({ q, sc: score(q) }));
  info.themed = themed; info.keywords = [...want]; info.matching = pool.filter((x) => x.sc > 0).length;
  // Themed rounds take only close matches: at least half as good as the best, so one stray shared word
  // ("places", "cities") does not pull in a question from another subject.
  const best = Math.max(0, ...pool.map((x) => x.sc)), floor = best >= 2 ? Math.max(2, Math.ceil(best / 2)) : 1;
  if (themed) { const matching = pool.filter((x) => x.sc >= floor); pool = matching.length || !EVERGREEN.includes(type) ? matching : pool; }
  // best matches first, then a shuffle among equals so the same items do not always lead
  // A true shuffle first (a random sort comparator barely moves anything, so the same early items kept winning),
  // then best matches first; the sort is stable, so equals stay in their shuffled order.
  for (let i = pool.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [pool[i], pool[j]] = [pool[j], pool[i]]; }
  pool.sort((a, b) => b.sc - a.sc);
  // Difficulty: a set round takes that level first; a mixed round is built about a quarter easy, nearly half medium
  // and the rest hard (unrated items count as medium), falling back to whatever is left once a level runs dry.
  const level = (q: any) => (["easy", "medium", "hard"].includes(q.difficulty) ? q.difficulty : "medium");
  const quota: Record<string, number> = difficulty === "mixed"
    ? { easy: Math.round(need * 0.25), hard: Math.round(need * 0.3), medium: 0 }
    : { easy: 0, medium: 0, hard: 0, [difficulty]: need };
  if (difficulty === "mixed") quota.medium = need - quota.easy - quota.hard;
  const picked: any[] = [], left: typeof pool = [];
  for (const x of pool) { const l = level(x.q); if (quota[l] > 0) { quota[l]--; picked.push(x.q); } else left.push(x); }
  for (const x of left) { if (picked.length >= need) break; picked.push(x.q); }
  picked.length = Math.min(picked.length, need);
  if (!picked.length) return [];
  const at = new Date().toISOString();
  for (const q of picked) q.used = { quiz: quizId, at };
  await bankSave(row);
  return picked.map((q) => {
    const c = JSON.parse(JSON.stringify(q)); delete c.used; delete c.passed; c.bankId = q.id; c.id = "q_" + crypto.randomUUID().replace(/-/g, "").slice(0, 8); c.fromBank = true;
    if (c.type === "race") Object.assign(c, { perCorrect: 100, prize: 500, prize2: 200, prize3: 100, forfeit: 200 }); // today's scoring, whatever an old item carried
    return c;
  });
}

// ---------------------------------------------------------------- Name That Tune: Apple's public search for 30-second previews
function cleanTitle(t: string): string { return String(t || "").replace(/\s*[\(\[][^)\]]*(feat\.|featuring|remaster|remastered|version|edit|mix|mono|stereo|live|radio)[^)\]]*[\)\]]/gi, "").replace(/\s+-\s+(remaster(ed)?|single version|radio edit|\d{4} remaster).*$/i, "").trim(); }
interface TuneHit { track: string; artist: string; album: string; year: number | null; previewUrl: string; artwork: string }
async function tuneSearch(term: string, limit = 8): Promise<TuneHit[]> {
  const r = await fetch(`https://itunes.apple.com/search?term=${encodeURIComponent(term)}&entity=song&country=GB&limit=${limit}`);
  if (!r.ok) throw new Error("The music search is not answering right now.");
  const d = await r.json();
  return (d.results || []).filter((x: any) => x.previewUrl).map((x: any) => ({
    track: String(x.trackName || ""), artist: String(x.artistName || ""), album: String(x.collectionName || ""),
    year: x.releaseDate ? +String(x.releaseDate).slice(0, 4) : null, previewUrl: String(x.previewUrl), artwork: String(x.artworkUrl100 || ""),
  }));
}
/** The best match for a track the writer named: exact title first, then title-and-artist overlap; skips karaoke and tribute versions. */
async function tuneLookup(term: string, track: string, artist: string): Promise<TuneHit | null> {
  let hits: TuneHit[] = [];
  try { hits = await tuneSearch(term, 10); } catch { return null; }
  const bad = /karaoke|tribute|in the style of|cover|instrumental|made famous|originally performed|piano dreamers/i;
  const score = (h: TuneHit) => {
    if (bad.test(h.track + " " + h.artist + " " + h.album)) return -1;
    let sc = 0;
    if (norm(h.track) === norm(track)) sc += 4; else if (norm(h.track).startsWith(norm(track))) sc += 2; else if (norm(h.track).includes(norm(track))) sc += 1;
    if (norm(h.artist) === norm(artist)) sc += 3; else if (norm(h.artist).includes(norm(artist)) || norm(artist).includes(norm(h.artist))) sc += 2;
    return sc;
  };
  const best = hits.map((h) => ({ h, sc: score(h) })).filter((x) => x.sc >= 3).sort((a, b) => b.sc - a.sc)[0];
  return best ? best.h : null;
}

/** Turns the AI provider's raw errors into something a host can act on. */
function friendly(msg: string): string {
  if (/credit balance is too low/i.test(msg)) return "The AI account is out of credit, so nothing can be written or judged right now. Top it up at console.anthropic.com (Plans & Billing), then try again.";
  if (/invalid x-api-key|authentication_error/i.test(msg)) return "The AI key on the server is not valid. Check the ANTHROPIC_API_KEY secret.";
  if (/rate_limit|429/i.test(msg)) return "The AI is being rate-limited. Wait a minute and try again.";
  if (/overloaded|529/i.test(msg)) return "The AI is overloaded right now. Try again in a moment.";
  return msg;
}
