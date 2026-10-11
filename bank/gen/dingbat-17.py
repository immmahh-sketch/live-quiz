# Bank session 11 Oct 2026: more dingbats -> bank/dingbat-17.json. Checked against every answer already in the bank (live and files).
# Elements: t text, x/y 0–100 (centre), s size 1–6, optional rot, flip "h"/"v", style strike/underline/box/outline, color #hex.
import json, os, glob
B = []
def d(answers, cat, diff, *els, tags=()):
    B.append({"answers": answers, "elements": [dict(e) for e in els], "category": cat, "tags": list(tags), "difficulty": diff})
def e(t, x=50, y=50, s=5, **k): return {"t": t, "x": x, "y": y, "s": s, **k}
RED, GREY, GOLD, SILVER, YELLOW = "#d42020", "#8a8f94", "#c9a227", "#9aa0a6", "#e0b400"
BLUE, BROWN, PURPLE, GREEN, PINK, ORANGE = "#1f5fd4", "#7a4a1e", "#7b2fbe", "#1f9a3a", "#e8579a", "#e07a00"

# under (underlined)
d(["Undershirt", "Under shirt"], "Fashion", "medium", e("SHIRT", s=6, style="underline"))
d(["Understate", "Understatement"], "Phrase", "medium", e("STATE", s=6, style="underline"))
d(["Underfed"], "Phrase", "medium", e("FED", s=6, style="underline"))
d(["Underdressed"], "Fashion", "medium", e("DRESSED", s=5, style="underline"))
d(["Undergraduate"], "Phrase", "hard", e("GRADUATE", s=4, style="underline"))
# backwards
d(["Backtalk", "Back talk"], "Phrase", "medium", e("KLAT", s=6))
d(["Backhander"], "Phrase", "hard", e("REDNAH", s=6))
# sizes and positions
d(["Big business"], "Phrase", "medium", e("BUSINESS", s=6))
d(["Smallholding"], "Nature", "hard", e("holding", s=1))
d(["Top dollar"], "Phrase", "medium", e("DOLLAR", y=15, s=4))
d(["Top heavy", "Top-heavy"], "Phrase", "medium", e("HEAVY", y=15, s=4))
d(["High horse", "On your high horse"], "Phrase", "medium", e("HORSE", y=15, s=4))
d(["High road", "The high road"], "Phrase", "medium", e("ROAD", y=15, s=4))
d(["Low battery"], "Everyday life", "easy", e("BATTERY", y=85, s=4))
d(["Low-lying", "Low lying"], "Phrase", "hard", e("LYING", y=85, s=4))
d(["Left out"], "Phrase", "medium", e("OUT", x=15, s=4))
d(["Right away"], "Phrase", "medium", e("AWAY", x=82, s=4))
d(["Downfall"], "Phrase", "hard", e("FALL", s=5, rot=90))
d(["Upload"], "Everyday life", "hard", e("LOAD", s=5, rot=-90))
d(["Slow motion", "In slow motion"], "Film", "medium", e("M  O  T  I  O  N", s=4))
# colours
d(["Red-handed", "Red handed", "Caught red-handed"], "Phrase", "medium", e("HANDED", s=6, color=RED))
d(["Silver medal"], "Sport", "easy", e("MEDAL", s=6, color=SILVER))
d(["Gold standard", "The gold standard"], "Phrase", "medium", e("STANDARD", s=5, color=GOLD))
d(["Purple prose"], "Books", "hard", e("PROSE", s=6, color=PURPLE))
# hollow letters: ghost
d(["Ghost story", "Ghost stories"], "Books", "medium", e("STORY", s=6, style="outline"))
d(["Ghost train"], "Phrase", "medium", e("TRAIN", s=6, style="outline"))

here = os.path.dirname(os.path.abspath(__file__))
have = set()
for f in glob.glob(os.path.join(here, '..', 'dingbat*.json')):
    if f.endswith('dingbat-17.json'): continue
    for r in json.load(open(f, encoding='utf-8')): have.update(a.lower() for a in r['answers'])
live = os.path.join(here, '..', '..', '..', 'lqsql', 'ding-a.json')
if os.path.exists(live): have.update(r['a'].lower() for r in json.load(open(live, encoding='utf-8'))['rows'] if r.get('a'))
clash = [b['answers'][0] for b in B if any(a.lower() in have for a in b['answers'])]
print('clash:', clash)
B = [b for b in B if b['answers'][0] not in clash]
json.dump(B, open(os.path.join(here, '..', 'dingbat-17.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'dingbats written')
