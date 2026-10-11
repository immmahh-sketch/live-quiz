# Bank session 11 Oct 2026: more dingbats -> bank/dingbat-14.json. Checked against every answer already in the bank (live and files).
# Elements: t text, x/y 0–100 (centre), s size 1–6, optional rot, flip "h"/"v", style strike/underline/box/outline, color #hex.
import json, os, glob
B = []
def d(answers, cat, diff, *els, tags=()):
    B.append({"answers": answers, "elements": [dict(e) for e in els], "category": cat, "tags": list(tags), "difficulty": diff})
def e(t, x=50, y=50, s=5, **k): return {"t": t, "x": x, "y": y, "s": s, **k}
RED, GREY, GOLD, SILVER, YELLOW = "#d42020", "#8a8f94", "#c9a227", "#9aa0a6", "#e0b400"
BLUE, BROWN, PURPLE, GREEN, PINK, ORANGE = "#1f5fd4", "#7a4a1e", "#7b2fbe", "#1f9a3a", "#e8579a", "#e07a00"


# under (underlined)
d(["Underworld"], "Phrase", "medium", e("WORLD", s=5, style="underline"))
d(["Undergrowth"], "Nature", "medium", e("GROWTH", s=5, style="underline"))
d(["Undertaker"], "Phrase", "medium", e("TAKER", s=5, style="underline"))
d(["Underage", "Under age"], "Phrase", "medium", e("AGE", s=6, style="underline"))
d(["Underpass"], "Phrase", "medium", e("PASS", s=6, style="underline"))
d(["Underwear"], "Fashion", "easy", e("WEAR", s=6, style="underline"))
# crossed out
d(["Crossover"], "Phrase", "medium", e("OVER", s=6, style="strike"))
d(["Crossbreed"], "Nature", "medium", e("BREED", s=5, style="strike"))
d(["Cross-examine", "Cross examine"], "Law", "medium", e("EXAMINE", s=5, style="strike"))
d(["Crosswalk"], "Phrase", "medium", e("WALK", s=6, style="strike"))
# backwards
d(["Backside"], "Phrase", "easy", e("EDIS", s=6))
d(["Backchat"], "Phrase", "medium", e("TAHC", s=6))
d(["Background"], "Phrase", "medium", e("DNUORG", s=5))
d(["Backdoor", "Back door"], "Phrase", "easy", e("ROOD", s=6))
d(["Back seat", "Backseat"], "Phrase", "medium", e("TAES", s=6))
# sizes and positions
d(["Big toe"], "Phrase", "easy", e("TOE", s=6))
d(["Big shot"], "Phrase", "medium", e("SHOT", s=6))
d(["Big bucks"], "Phrase", "medium", e("BUCKS", s=6))
d(["Big cheese"], "Phrase", "medium", e("CHEESE", s=5))
d(["Small fortune", "A small fortune"], "Phrase", "medium", e("fortune", s=1))
d(["High school"], "Phrase", "medium", e("SCHOOL", y=15, s=4))
# colours
d(["Golden hour", "The golden hour"], "Phrase", "hard", e("HOUR", s=6, color=GOLD))
d(["Red nose", "Red Nose Day"], "Phrase", "easy", e("NOSE", s=6, color=RED))
# counted
d(["Four-poster", "Four-poster bed", "Four poster"], "Everyday life", "medium", e("POSTER POSTER\nPOSTER POSTER", s=3))
d(["Tenpin bowling", "Ten pin bowling", "Tenpin", "Ten pin"], "Sport", "medium", e("PIN PIN PIN PIN\nPIN PIN PIN\nPIN PIN\nPIN", s=2))
d(["Twelve Angry Men", "12 Angry Men"], "Film", "hard", e("MEN MEN MEN MEN\nMEN MEN MEN MEN\nMEN MEN MEN MEN", s=2, color=RED))

have = set()
here = os.path.dirname(os.path.abspath(__file__))
for f in glob.glob(os.path.join(here, '..', 'dingbat*.json')):
    if f.endswith('dingbat-14.json'): continue
    for r in json.load(open(f, encoding='utf-8')): have.update(a.lower() for a in r['answers'])
live = os.path.join(here, '..', '..', '..', 'lqsql', 'ding-a.json')
if os.path.exists(live): have.update(r['a'].lower() for r in json.load(open(live, encoding='utf-8'))['rows'] if r.get('a'))
clash = [b['answers'][0] for b in B if any(a.lower() in have for a in b['answers'])]
print('clash:', clash)
B = [b for b in B if b['answers'][0] not in clash]
json.dump(B, open(os.path.join(here, '..', 'dingbat-14.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'dingbats written')
