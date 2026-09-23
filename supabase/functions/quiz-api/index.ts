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
//   save_game   — record a finished game's scoreboard
//   games       — recent finished games
//
// Deploy with "Verify JWT" OFF — the browser only holds the publishable key.

import Anthropic from "npm:@anthropic-ai/sdk";

const SUPA_URL = Deno.env.get("SUPABASE_URL")!;
const SERVICE_KEY = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!;
const HOST_PW = Deno.env.get("QUIZ_HOST_PASSWORD") || "";
const ANTHROPIC_KEY = Deno.env.get("ANTHROPIC_API_KEY") || "";
const BUCKET = "quiz-media";
const UA = "LiveQuiz/1.0 (https://github.com/immmahh-sketch/live-quiz)";
const MODEL = "claude-opus-5";
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

/** Finds a photo of the subject that the quiz is not already using, copies it into our bucket, and returns {url, source}. */
async function wikiPicture(title: string, used: Set<string>): Promise<{ url: string; source: string } | null> {
  const fresh = (cs: Candidate[]) => cs.filter((c) => !used.has(c.url) && !used.has(c.key));
  const words = keyWords(title);
  const [article, category, search, lead] = await Promise.all([articlePhotos(title, words), categoryPhotos(title, words), searchPhotos(title, words), leadPhoto(title)]);
  const seen = new Set<string>();
  let pool = fresh([...article, ...category, ...search]).filter((c) => !seen.has(c.url) && seen.add(c.url));
  // The lead image is the one Wikipedia's editors chose, so it always stays in the running
  // when the pool is thin; it just stops being the only choice.
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
        model: MODEL,
        max_tokens: 4000,
        system: JUDGE_SYSTEM,
        output_config: { effort: "low" },
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
- Never put the answer, or a giveaway, in the question text.
- Keep question text under 140 characters. Answers under 40 characters.

Question types and their JSON shapes (use only the types you are asked for, and mix them):
- "choice": {"type":"choice","text":"...","options":["A","B","C","D"],"answer":"<exactly one of the options>","time":20}
  Wrong options must be plausible and of the same kind as the answer.
- "text": {"type":"text","text":"...","answers":["canonical answer","other accepted form",...],"time":25}
  Put the answer as it should be shown first; then alternatives that are also fully correct (nicknames, a surname on its own if that would be accepted).
- "order": {"type":"order","text":"Put these in order, earliest first","items":["first","second","third","fourth"],"hint":"earliest to latest","time":30}
  Items listed in the CORRECT order. 3 to 5 items. The question text must say what order.
- "match": {"type":"match","text":"Match the breed to the picture","pairs":[{"left":"Labrador Retriever","rightPicture":"Labrador Retriever"},...],"time":40}
  3 or 4 pairs. "rightPicture" is the exact English Wikipedia article title whose lead picture shows the thing (only when a pictures round is wanted); otherwise use "right":"text" for a word-to-word match.
- "pin": {"type":"pin","text":"Drop the pin on Namibia","place":"Namibia","lat":-22.0,"lon":17.0,"sizeKm":1200,"time":20}
  Only countries, cities, seas and famous landmarks. lat/lon of its centre in decimal degrees; sizeKm is roughly how wide the place is (a city ~30, a small country ~300, a large country ~2000).
- "tf": {"type":"tf","text":"<a statement>","answer":true}
  A crisp statement that is definitely true or definitely false. Mix true and false across the set.
- "sort": {"type":"sort","text":"Which of these actors have been in Coronation Street?","categories":["Been in Coronation Street","Never been in Coronation Street"],"items":[{"text":"...","category":"<exactly one of the categories>"}]}
  2 to 4 categories, 4 to 8 items, at least one item per category. Every placement must be certain.
- "wipeout": {"type":"wipeout","text":"Footballers who have played for Newcastle United","right":["...x15"],"wrong":["...x5"]}
  A list question. "right" are 15 answers that definitely fit; "wrong" are 5 that are plausible (same kind of thing, same era or league) but definitely do not fit. Verify every one — a wrong answer that actually fits ruins the round.

Pictures: add "picture":"<exact English Wikipedia article title>" to any question where a picture makes it better or is the question itself ("Which city is this?", "Name this bird"). Use only titles you are confident exist, whose lead image shows the thing and does not contain its name as a caption in the image. Do not add a picture that gives the answer away when the question is not about identifying the picture.

Times are in seconds: 15–45. Harder or longer questions get longer.

Reply with JSON only: {"questions":[ ... ]}`;

interface GenOpts { topic: string; brief: string; count: number; difficulty: string; types: string[]; pictures: boolean; web: boolean; avoid: string[]; usedPictures: string[]; }

async function generate(o: GenOpts) {
  const client = anthropic();
  const wantPictures = o.pictures;
  const typeList = o.types.length ? o.types : ["choice", "text"];
  // The portal asks for a big round in batches; this is what earlier batches already wrote.
  const avoid = o.avoid.length ? `\nAlready written for this round — do not repeat these facts or ask them another way:\n${o.avoid.map((t) => "- " + t).join("\n")}` : "";
  // The host's own brief for the round outranks the topic line: "a sports round, but every
  // question about Harry Kane" means every question about Harry Kane.
  const brief = o.brief ? `\nThe host's brief for this round — follow it closely, it decides what every question is about:\n${o.brief}` : "";
  const prompt = `Write ${o.count} pub quiz questions.
Round: ${o.topic || "general knowledge"}${brief}
Difficulty: ${o.difficulty}
Question types to use (mix them across the set): ${typeList.join(", ")}
Pictures round: ${wantPictures ? "yes — give roughly half the questions a picture, and use rightPicture for match questions" : "no pictures"}${avoid}`;

  const params: Anthropic.MessageCreateParamsNonStreaming = {
    model: MODEL,
    max_tokens: 16000,
    system: WRITER_SYSTEM,
    output_config: { effort: "medium" },
    messages: [{ role: "user", content: prompt }],
  };
  if (o.web) params.tools = [{ type: "web_search_20260209", name: "web_search", max_uses: 8 }];

  const msg = await ask(client, params);
  const out = extractJson(textOf(msg));
  const raw: any[] = Array.isArray(out?.questions) ? out.questions : [];
  if (!raw.length) throw new Error("The AI did not write any questions. Try a broader topic.");

  const uid = (p: string) => p + "_" + crypto.randomUUID().replace(/-/g, "").slice(0, 8);
  const warnings: string[] = [];
  const used = new Set<string>(o.usedPictures);
  let map: string | null = null;
  if (raw.some((q) => q?.type === "pin")) {
    map = await worldMap();
    if (!map) warnings.push("Could not fetch a world map, so the drop-the-pin questions were left out.");
  }

  const questions = await Promise.all(raw.slice(0, o.count).map(async (r) => {
    const time = Math.min(90, Math.max(10, Math.round(+r.time || 25)));
    const base: any = { id: uid("q"), type: r.type, text: String(r.text || "").trim(), time, media: { kind: "none" }, partial: false };
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
    if (r.type === "pin") {
      if (!map) return null;
      const lat = +r.lat, lon = +r.lon;
      if (!isFinite(lat) || !isFinite(lon) || Math.abs(lat) > 90 || Math.abs(lon) > 180) return null;
      const sizeKm = Math.max(20, Math.min(5000, +r.sizeKm || 300));
      const full = Math.max(0.012, Math.min(0.08, (sizeKm / 2) / 40075));
      base.media = { kind: "image", url: map, credit: "Wikimedia Commons: Equirectangular projection SW" };
      base.pin = { x: (lon + 180) / 360, y: (90 - lat) / 180 };
      base.radiusFull = +full.toFixed(4);
      base.radiusZero = +Math.min(0.3, full * 4).toFixed(4);
      base.place = String(r.place || "").trim();
      return base;
    }
    return null;
  }));

  const kept = questions.filter(Boolean);
  if (!kept.length) throw new Error("None of the AI's questions were usable. Try again.");
  return { questions: kept, warnings, searched: !!o.web };
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

async function verifyQuestions(items: { id: string; summary: string }[]) {
  const msg = await ask(anthropic(), {
    model: MODEL,
    max_tokens: 8000,
    system: CHECK_SYSTEM,
    output_config: { effort: "medium" },
    tools: [{ type: "web_search_20260209", name: "web_search", max_uses: 10 }],
    messages: [{ role: "user", content: "Check these questions:\n\n" + items.map((i) => `[id ${i.id}]\n${i.summary}`).join("\n\n") }],
  });
  const out = extractJson(textOf(msg));
  const checks: Record<string, { verdict: string; note: string; fix?: string }> = {};
  for (const c of out?.checks || []) {
    if (typeof c?.id !== "string" || !items.some((i) => i.id === c.id)) continue;
    const verdict = ["ok", "doubt", "wrong"].includes(c.verdict) ? c.verdict : "doubt";
    checks[c.id] = { verdict, note: String(c.note || "").slice(0, 600), ...(c.fix ? { fix: String(c.fix).slice(0, 200) } : {}) };
  }
  return { checks };
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
        count: Array.isArray(r.questions) ? r.questions.length : 0,
        types: Array.isArray(r.questions) ? Array.from(new Set(r.questions.map((q: any) => q.type))) : [],
      })) });
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
      const types = (Array.isArray(body.types) ? body.types : []).filter((t: unknown) => ["choice", "text", "order", "match", "pin", "tf", "sort", "wipeout"].includes(String(t)));
      const out = await generate({
        topic: String(body.brief ? (body.title || body.topic || "") : (body.topic || "")).slice(0, 200),
        brief: String(body.brief || "").slice(0, 1500),
        count: Math.min(8, Math.max(1, Math.round(+body.count || 5))),
        avoid: (Array.isArray(body.avoid) ? body.avoid : []).map((s: unknown) => String(s ?? "").slice(0, 160)).filter(Boolean).slice(-60),
        usedPictures: (Array.isArray(body.usedPictures) ? body.usedPictures : []).map((s: unknown) => String(s ?? "").slice(0, 300)).filter(Boolean).slice(-300),
        difficulty: ["easy", "medium", "hard", "mixed"].includes(String(body.difficulty)) ? String(body.difficulty) : "mixed",
        types,
        pictures: body.pictures !== false,
        web: body.web !== false,
      });
      return json(out);
    }

    if (action === "verify") {
      if (!ANTHROPIC_KEY) return json({ error: "AI is not set up on the server yet — add ANTHROPIC_API_KEY as a Supabase secret." }, 503);
      const items = (Array.isArray(body.questions) ? body.questions : [])
        .filter((q: any) => q && typeof q.id === "string" && typeof q.summary === "string")
        .slice(0, 6)
        .map((q: any) => ({ id: q.id.slice(0, 40), summary: q.summary.slice(0, 1500) }));
      if (!items.length) return json({ error: "Nothing to check." }, 400);
      return json(await verifyQuestions(items));
    }

    if (action === "save_game") {
      const g = body.game || {};
      await rest(`quiz_games`, { method: "POST", body: JSON.stringify({
        code: String(g.code || "").slice(0, 12),
        quiz_id: UUID_RE.test(String(g.quiz_id)) ? g.quiz_id : null,
        title: String(g.title || "").slice(0, 120),
        players: Array.isArray(g.players) ? g.players.slice(0, 500) : [],
        questions: Math.max(0, Math.round(+g.questions || 0)),
        started_at: g.started_at || null,
      }) });
      return json({ ok: true });
    }

    if (action === "games") {
      const rows = await rest(`quiz_games?select=*&order=ended_at.desc&limit=50`);
      return json({ games: rows || [] });
    }

    return json({ error: "Unknown action." }, 400);
  } catch (e) {
    console.error(e);
    return json({ error: String((e as Error)?.message || e) }, 500);
  }
});
