// Shared rules for the play-at-home games (home/sets/*.json): what a question must look like for each use,
// and when two questions count as "the same" (the same test the server uses for warm-up clashes).
import fs from "node:fs";

export const norm = (s) => String(s || "").toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "")
  .replace(/&/g, " and ").replace(/[^a-z0-9]+/g, " ").trim().replace(/^(the|a|an) /, "");
const CLASH_STOP = new Set("which what where when whose does were that this with from have into about their there these those they them than then name named first most many much only also over under after before your called known".split(" "));
export const clashWords = (s) => new Set(norm(s).split(" ").filter((w) => w.length > 3 && !CLASH_STOP.has(w)));

/** One-show, seasonal and signature categories: never in a general-knowledge home game. */
export const NICHE = /^(dexter|bridgerton|the handmaid's tale|breaking bad and better call saul|game of thrones|covid-19|halloween music|christmas songs|christmas films|christmas tv|christmas|easter and spring|valentine's day and love songs|bonfire night and autumn|new year|summer holidays|halloween|brighton|roger|alan shearer|song lyrics|connections and links|anagrams and wordplay|name the year)$/i;
export const LOCAL = /newcastle|sunderland|north east|geordie|mackem|tyne|wearside|gateshead|durham|northumberland|teesside|middlesbrough/i;
/** Needs its options on screen to make sense, so it cannot be a typed question. */
export const NEEDS_OPTIONS = /\b(of these|the following|odd one out|which one|not\b|none of|all of|true or false|which is there more of|which is (bigger|larger|longer|older|taller|heavier)|approximately|roughly|about how|how many times more)\b|, or [^?]*\?$/i;

/** The right answer of a bank question (or a home-set question) as text. */
export function answerOf(q) {
  if (q.type === "choice") return String((q.options || []).find((o) => o.id === q.correct)?.text ?? "");
  if (Array.isArray(q.answers)) return String(q.answers[0] ?? "");
  if (Array.isArray(q.options) && Number.isInteger(q.correct)) return String(q.options[q.correct] ?? "");
  return "";
}
export const wrongOf = (q) => (q.options || []).filter((o) => o.id !== q.correct).map((o) => String(o.text));

/** Same question, or the same answer to a question about the same thing. Strict (the server's warm-up test, used
 *  when picking): three shared words make it the same question. Otherwise (checking): near-identical wording, the
 *  same answer about the same thing, or one fact asked both ways round. */
export function clash(a, b, strict = true) {
  const wa = a.words || clashWords(a.text), wb = b.words || clashWords(b.text);
  let common = 0; for (const t of wa) if (wb.has(t)) common++;
  const ax = a.ans ?? norm(a.answer), ay = b.ans ?? norm(b.answer);
  const sameAns = ax.length > 3 && ax === ay && !/^(true|false|yes|no)$/.test(ax);
  if (strict) {
    const textSame = common >= 3 && common / Math.max(1, Math.min(wa.size, wb.size)) >= 0.5;
    return textSame ? "same question" : sameAns && common >= 1 ? "same answer" : "";
  }
  if (sameAns && common >= 1) return "same answer";
  if (common >= 3 && common / Math.max(1, Math.max(wa.size, wb.size)) >= 0.75) return "same question";
  const ta = " " + norm(a.text) + " ", tb = " " + norm(b.text) + " ";
  if (ax.length >= 4 && ay.length >= 4 && tb.includes(" " + ax + " ") && ta.includes(" " + ay + " ")) return "same fact both ways";
  return "";
}
/** Index items for fast clash checks: { text, answer, words, ans }. */
export const key = (text, answer, extra = {}) => ({ text, answer, words: clashWords(text), ans: norm(answer), ...extra });

/** Everything a hosted quiz has used (questions, game rows, list prompts) as clash keys. */
export function hostedKeys(quizzes) {
  const out = [];
  for (const quiz of quizzes) for (const q of quiz.questions || []) {
    if (!q || q.type === "slide") continue;
    const right = q.type === "choice" ? answerOf(q) : q.type === "smash" ? q.smash : q.type === "wheel" ? q.phrase : q.type === "pin" ? q.place : Array.isArray(q.answers) ? q.answers[0] : "";
    const text = q.type === "wheel" ? q.phrase : q.text;
    if (text) out.push(key(String(text), String(right || ""), { from: quiz.title }));
    for (const b of Array.isArray(q.bank) ? q.bank : []) out.push(key(String(b?.text || ""), String(b?.options?.[0] ?? ""), { from: quiz.title }));
  }
  return out;
}

/** A typed answer: short enough to type against the clock. */
export function typeable(text, ans) {
  const a = String(ans).trim();
  if (!a || a.length > 22 || a.split(/\s+/).length > 3) return false;
  if (/\b(about|approx|around|over|under|more than|less than|between)\b|%|\//i.test(a)) return false;
  if (/^\d{5,}$/.test(a.replace(/,/g, ""))) return false; // long numbers are guesses, not knowledge
  const t = String(text).trim();
  if (t.length < 20 || t.length > 130 || !/\?$/.test(t) || NEEDS_OPTIONS.test(t)) return false;
  return !giveaway(t, a);
}
/** The answer, or a telling part of it, is in the question. */
export function giveaway(text, ans) {
  const t = " " + norm(text) + " ";
  return norm(ans).split(" ").filter((w) => w.length >= 4).some((w) => t.includes(" " + w + " ")) || (norm(ans).length >= 3 && t.includes(" " + norm(ans) + " "));
}

/** Extra accepted spellings for a typed answer: a person's surname, digits for number words and back. */
const NUM = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"];
/** A question whose answer is a person, so the surname alone will do. */
const PERSON_Q = /^(who|whose)\b|\b(which|what) (\w+ ){0,3}(singer|actor|actress|man|woman|person|king|queen|player|driver|scientist|astronomer|physicist|chemist|author|writer|novelist|poet|playwright|composer|artist|painter|sculptor|drummer|guitarist|bassist|rapper|comedian|presenter|host|politician|prime minister|president|chancellor|footballer|cricketer|golfer|boxer|athlete|tennis player|chef|designer|inventor|explorer|star|emperor|empress|director|architect|engineer|pilot|astronaut|philosopher|monarch|pope|saint|general|admiral|dj|broadcaster|journalist|model|dancer)s?\b/i;
export function aliases(text, answers) {
  const out = [...answers];
  const a = String(answers[0]).trim();
  if (PERSON_Q.test(text) && /^[A-Z][a-z'-]+( [A-Z][a-z'-]+){1,2}$/.test(a) && !/^(The|St|Sir|Lord|Lady|King|Queen|Prince|Princess)\b/.test(a)) {
    const last = a.split(" ").pop(); if (last.length >= 4) out.push(last);
  }
  const n = NUM.indexOf(a.toLowerCase()); if (n >= 0) out.push(String(n));
  if (/^\d+$/.test(a) && +a <= 20) out.push(NUM[+a]);
  return [...new Set(out.map((x) => String(x).trim()).filter(Boolean))];
}

/** An index by word and by answer, so each clash check only looks at items that could clash. */
export class ClashIndex {
  constructor(strict = true) { this.by = new Map(); this.strict = strict; }
  add(k) { for (const w of [...k.words, "=" + k.ans]) { if (!this.by.has(w)) this.by.set(w, []); this.by.get(w).push(k); } }
  hit(k) {
    const seen = new Set();
    for (const w of [...k.words, "=" + k.ans]) for (const o of this.by.get(w) || []) { if (seen.has(o)) continue; seen.add(o); const why = clash(k, o, this.strict); if (why) return { o, why }; }
    // "same fact both ways" can share no word at all ("What is the capital of Kenya?" / "Nairobi is the capital of which country?")
    if (!this.strict && k.ans.length >= 4) for (const o of this.by.get("=" + k.ans) || []) if (!seen.has(o)) { const why = clash(k, o, false); if (why) return { o, why }; }
    return null;
  }
}
export const readJson = (p) => JSON.parse(fs.readFileSync(p, "utf8"));
export const rowsOf = (p) => { const d = readJson(p); return Array.isArray(d) ? d : d.rows; };
