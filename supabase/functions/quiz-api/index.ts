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
const MAP_ALIASES: Record<string, string> = { uk: "United Kingdom", "great britain": "United Kingdom", britain: "United Kingdom", england: "United Kingdom", scotland: "Scotland", wales: "Wales", us: "USA", usa: "USA", "united states": "USA", "united states of america": "USA", america: "USA", world: "World", earth: "World", globe: "World", "the world": "World", holland: "Netherlands", "czech republic": "Czech Republic", "south korea": "South Korea", "north korea": "North Korea", ireland: "Ireland", "republic of ireland": "Ireland", "northern ireland": "Northern Ireland", uae: "United Arab Emirates" };
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
    const data = await mw("https://en.wikipedia.org/w/api.php", { action: "query", prop: "revisions", rvprop: "content", rvslots: "main", formatversion: "2", titles: "Module:Location map/data/" + region }).catch(() => null);
    const page = data?.query?.pages?.[0]; const src: string = page?.revisions?.[0]?.slots?.main?.content || "";
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
  const m = await build().catch(() => null);
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
- "club": {"type":"club","pct":50,"text":"If planet EARTH has a HEART, which body part does MARS have?","answers":["Arms"]}
  The 1% Club, in the style of The 1% Club: a logic, maths, pattern, wordplay or lateral-thinking puzzle that needs NO general knowledge, only working out, solvable in 30 seconds by reading the question (anagrams, letter/number patterns, "which is the odd one out", what-comes-next, counting, riddles that reward reading carefully). "pct" is how many people would get it: 90 is easy, 50 medium, 10 hard, 1 fiendish; spread the percentages across a batch and label honestly. The answer must be a single unambiguous word, number or short phrase; write the question so nothing else fits. No pictures.
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
    const base: any = { id: uid("q"), type: r.type, text: String(r.text || r.phrase || (r.type === "tune" ? r.track : r.type === "dingbat" ? "Say what you see" : "") || "").trim(), time, media: { kind: "none" }, partial: false };
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
      if (bank.length < 8) return null;
      base.bank = bank; base.target = Math.min(bank.length - 2, Math.max(3, Math.round(+r.target || 10))); base.perCorrect = 100; base.prize = 500; base.prize2 = 200; base.prize3 = 100; base.forfeit = 200; base.time = 120;
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
Question types to use (mix them across the set): ${typeList.join(", ")}
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
        count: Array.isArray(r.questions) ? r.questions.length : 0,
        types: Array.isArray(r.questions) ? Array.from(new Set(r.questions.map((q: any) => q.type))) : [],
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
      const KNOWN = ["choice", "text", "order", "match", "pin", "tf", "sort", "wipeout", "race", "smash", "wheel", "highlow", "rhyme", "club", "dingbat", "tune", "catchphrase"];
      const asked = (Array.isArray(body.types) ? body.types : []).map(String);
      const types = asked.filter((t) => KNOWN.includes(t));
      const unknownTypes = asked.filter((t) => !KNOWN.includes(t));
      if (asked.length && !types.length) return json({ error: `This server does not know the question type${unknownTypes.length > 1 ? 's' : ''} ${unknownTypes.join(", ")} yet — redeploy the quiz-api function.` }, 400);
      // The bank first: anything pre-written that fits this round comes free, and only the shortfall is written by the AI.
      const wantCount = Math.min(8, Math.max(1, Math.round(+body.count || 5)));
      const quizId = UUID_RE.test(String(body.quizId || "")) ? String(body.quizId) : "";
      let fromBank: any[] = []; const bankInfo: any = {};
      if (body.useBank !== false && quizId && types.length === 1) {
        try { fromBank = await bankTake(types[0], wantCount, String(body.topic || body.title || ""), String(body.brief || ""), quizId, ["easy", "medium", "hard"].includes(String(body.difficulty)) ? String(body.difficulty) : "mixed", bankInfo); } catch (e) { console.warn("bank take failed", String(e)); }
      }
      if (fromBank.length >= wantCount) return json({ questions: fromBank, warnings: [], searched: false, usage: null, unknownTypes, fromBank: fromBank.length, bankInfo });
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
      return json({ ...out, questions: [...fromBank, ...out.questions], unknownTypes, fromBank: fromBank.length, bankInfo });
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
      return json({ bank: bankStatus(await bankRows()), low: BANK_LOW });
    }
    if (action === "bank_list") {
      const type = String(body.type || "");
      const row = (await bankRows()).find((r) => r.settings?.type === type);
      const qs: any[] = row ? row.questions : [];
      return json({ questions: qs.map((q) => ({ id: q.id, text: q.text || q.phrase || q.place || "", answer: q.type === "choice" ? (q.options || []).find((o: any) => o.id === q.correct)?.text : q.type === "tf" ? String(q.answer) : q.type === "wheel" ? q.phrase : q.type === "pin" ? q.place : q.type === "order" ? (q.items || []).map((i: any) => i.text).join(" → ") : (q.answers || [])[0] || "", category: q.category || "", tags: q.tags || [], used: q.used || null, pct: q.pct, rejected: !!q.used?.rejected, difficulty: q.difficulty || "" })) });
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
      const row = (await bankRows()).find((r) => r.settings?.type === type);
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
      // Replaces a bank item's content (same id and stock status), for tidying up rejected ones.
      const type = String(body.type || ""), id = String(body.id || "");
      const row = await bankRow(type);
      const i = row.questions.findIndex((x: any) => x.id === id);
      if (i < 0) return json({ error: "That bank item no longer exists." }, 404);
      const nq = body.question && typeof body.question === "object" ? body.question : null;
      if (!nq || nq.type !== type) return json({ error: "Nothing to save." }, 400);
      const keep = row.questions[i];
      row.questions[i] = { ...nq, id, category: keep.category, tags: keep.tags, used: body.fresh ? undefined : keep.used };
      if (body.fresh) delete row.questions[i].used;
      await bankSave(row);
      return json({ ok: true });
    }
    if (action === "bank_reject") {
      // "I don't like this question": the bank item it came from (or the question itself, added to the bank)
      // is stamped used + rejected, so it never comes round again but can be reviewed and improved later.
      const q = body.question && typeof body.question === "object" ? body.question : null;
      if (!q || !q.type) return json({ error: "Nothing to reject." }, 400);
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
        if (!q || !q.type) continue;
        const t = String(q.kind || q.type); out[t] = out[t] || { restored: 0, added: 0, skipped: 0 };
        if (q.fromBank || q.bankId) continue; // already counted under restored
        let row = banks.find((r) => r.settings?.type === t);
        if (!row) { row = await bankRow(t); banks.push(row); }
        const key = bankKey(q);
        if (!key || row.questions.some((x: any) => nearDuplicate(x, q))) { out[t].skipped++; continue; }
        const cat0 = String(q.category || roundTitle(q.round) || "").trim();
        const c = { ...q, id: "q_" + crypto.randomUUID().replace(/-/g, "").slice(0, 8), category: (JUNK_CATEGORY.test(cat0) ? "" : cat0).slice(0, 60), tags: (q.tags || []).slice(0, 12) };
        if (c.type === "race") Object.assign(c, { perCorrect: 100, prize: 500, prize2: 200, prize3: 100, forfeit: 200 });
        delete c.used; delete c.fromBank; delete c.round; delete c.bankId; delete c.check;
        row.questions.push(c); touched.add(row); out[t].added++;
      }
      for (const row of touched) { if (JSON.stringify(row.questions).length > 1_900_000) return json({ error: `The ${row.settings.type} bank row is full.` }, 413); await bankSave(row); }
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
      if (JSON.stringify(row.questions).length > 1_900_000) return json({ error: "That bank row is full; start a second one for this type." }, 413);
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
      if (JSON.stringify(row.questions).length > 1_900_000) return json({ error: "That bank row is full; start a second one for this type." }, 413);
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
const EVERGREEN = ["club", "dingbat", "wheel", "pin", "tune", "catchphrase"]; // theme-free types: any unused item will do when the round has no matching one
/** What makes two items "the same": the phrase for dingbats and wheels, the place for pins, the track for tunes, the wording otherwise. */
function bankKey(q: any): string { if (q?.media?.kind === "youtube" && q.media.videoId) return "yt:" + q.media.videoId; if (q?.media?.kind === "image" && q.media.source && /which .*(flag|picture|this)/i.test(q.text || "")) return "img:" + q.media.source; return norm(q?.type === "dingbat" ? (q.answers || [])[0] || "" : q?.type === "tune" ? `${q.track} ${q.artist}` : q?.type === "pin" ? q.place || q.text : q?.phrase || q?.text || ""); }
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
  if (["order", "sort", "match", "wipeout", "race"].includes(a.type)) { const x = norm(bankAnswer(a)), y = norm(bankAnswer(b)); return !!x && x === y; }
  if (ka.startsWith("img:") || kb.startsWith("img:") || ka.startsWith("yt:") || kb.startsWith("yt:")) return false; // different picture or clip = different question
  const ta = tokens(ka), tb = tokens(kb);
  if (!ta.size || !tb.size) return false;
  let shared = 0; for (const w of ta) if (tb.has(w)) shared++;
  const overlap = shared / Math.min(ta.size, tb.size);
  const sameAnswer = a.type !== "tf" && ta.size >= 3 && tb.size >= 3 && norm(bankAnswer(a)) === norm(bankAnswer(b)) && norm(bankAnswer(a)).length > 1;
  return overlap >= 0.8 || (sameAnswer && overlap >= 0.5);
}
async function bankRows(): Promise<any[]> {
  return (await rest(`quiz_quizzes?settings->>bank=eq.true&select=id,title,settings,questions`)) || [];
}
async function bankRow(type: string): Promise<any> {
  const rows = await bankRows();
  const row = rows.find((r) => r.settings?.type === type);
  if (row) return row;
  const label: Record<string, string> = { choice: "Multiple choice", text: "Type the answer", order: "Put in order", pin: "Drop the pin", match: "Match up", tf: "True or false", sort: "Categorise", wipeout: "Wipeout", race: "The Race", smash: "Answer Smash", wheel: "Wheel of Fortune", highlow: "Highbrow Lowbrow", rhyme: "Rhyme Time", club: "The 1% Club", catchphrase: "Catchphrase", dingbat: "Dingbats", tune: "Name That Tune" };
  const made = await rest(`quiz_quizzes`, { method: "POST", headers: { Prefer: "return=representation" }, body: JSON.stringify({ title: `Question bank: ${label[type] || type}`, settings: { bank: true, type }, questions: [] }) });
  return Array.isArray(made) ? made[0] : made;
}
async function bankSave(row: any) {
  await rest(`quiz_quizzes?id=eq.${row.id}`, { method: "PATCH", body: JSON.stringify({ questions: row.questions, updated_at: new Date().toISOString() }) });
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
const WORD = (s: string) => new Set(norm(s).split(" ").filter((w) => w.length >= 4));
/** Words in a round's title or brief that say nothing about its theme ("Round 1", "questions about the show"). */
const THEME_STOP = new Set(["round", "rounds", "quiz", "quizzes", "question", "questions", "about", "based", "show", "shows", "series", "programme", "program", "from", "with", "that", "this", "these", "those", "their", "there", "what", "which", "some", "more", "most", "only", "mixed", "general", "knowledge", "trivia", "easy", "hard", "medium", "difficult", "tricky", "family", "friendly", "answer", "answers", "each", "every", "make", "made", "write", "include", "including", "like", "also", "just", "plus", "other", "things", "stuff", "anything", "everything", "famous", "popular", "classic", "best", "good", "great", "topic", "theme", "themed", "fun", "please", "want", "should", "would", "could", "about", "into", "over", "under", "your", "them", "they", "have", "been", "will", "than", "then", "when", "where", "while", "people", "players", "player", "team", "teams", "night", "tonight", "week", "weekly", "new", "untitled"]);
const JUNK_CATEGORY = /^(round\s*\d*|new quiz|untitled.*|ai quiz|quiz|general|test.*)$/i;
const GENERIC = /general knowledge|anything|mixed bag|pot ?luck|pub quiz|warm.?up|quick.?fire|random/i;
/** Takes up to `need` unused bank questions of a type for a quiz, preferring ones that match the round's topic and brief. */
async function bankTake(type: string, need: number, topic: string, brief: string, quizId: string, difficulty = "mixed", info: any = {}): Promise<any[]> {
  if (need <= 0) return [];
  const row = await bankRow(type);
  const qs: any[] = Array.isArray(row.questions) ? row.questions : [];
  const themed = !!(topic || brief).trim() && !GENERIC.test(topic + " " + brief) && (topic + " " + brief).trim().length > 3;
  const fresh = qs.filter((q) => !q.used);
  const haveOf = (q: any) => WORD([q.category, ...(q.tags || []), q.text, q.place, q.phrase, ...(q.answers || [])].filter(Boolean).join(" "));
  const haves = new Map(fresh.map((q) => [q, haveOf(q)]));
  // A word counts only when it is specific: not a filler word, and not one that turns up across a big slice of the
  // bank (so "Dexter" pulls Dexter questions, while "round" or "show" pull nothing).
  const common = Math.max(8, Math.round(fresh.length * 0.03));
  const want = new Set([...WORD(topic + " " + brief)].filter((w) => !THEME_STOP.has(w) && [...haves.values()].filter((h) => h.has(w)).length <= common));
  const text = " " + norm(topic + " " + brief) + " ";
  const score = (q: any) => {
    let sc = 0; const cat = norm(q.category || "");
    if (cat.length >= 4 && !JUNK_CATEGORY.test(cat) && !THEME_STOP.has(cat) && text.includes(" " + cat + " ")) sc += 3;
    const have = haves.get(q) || haveOf(q); for (const w of want) if (have.has(w)) sc += 1; return sc;
  };
  let pool = fresh.map((q) => ({ q, sc: score(q) }));
  info.themed = themed; info.keywords = [...want]; info.matching = pool.filter((x) => x.sc > 0).length;
  if (themed) { const matching = pool.filter((x) => x.sc > 0); pool = matching.length || !EVERGREEN.includes(type) ? matching : pool; }
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
    const c = JSON.parse(JSON.stringify(q)); delete c.used; c.bankId = q.id; c.id = "q_" + crypto.randomUUID().replace(/-/g, "").slice(0, 8); c.fromBank = true;
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
