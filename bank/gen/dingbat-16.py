# Bank session 11 Oct 2026: more dingbats -> bank/dingbat-16.json. Checked against every answer already in the bank (live and files).
# Elements: t text, x/y 0–100 (centre), s size 1–6, optional rot, flip "h"/"v", style strike/underline/box/outline, color #hex.
import json, os, glob
B = []
def d(answers, cat, diff, *els, tags=()):
    B.append({"answers": answers, "elements": [dict(e) for e in els], "category": cat, "tags": list(tags), "difficulty": diff})
def e(t, x=50, y=50, s=5, **k): return {"t": t, "x": x, "y": y, "s": s, **k}
RED, GREY, GOLD, SILVER, YELLOW = "#d42020", "#8a8f94", "#c9a227", "#9aa0a6", "#e0b400"
BLUE, BROWN, PURPLE, GREEN, PINK, ORANGE = "#1f5fd4", "#7a4a1e", "#7b2fbe", "#1f9a3a", "#e8579a", "#e07a00"

# under (underlined)
d(["Underscore"], "Phrase", "medium", e("SCORE", s=6, style="underline"))
d(["Underwire", "Underwired"], "Everyday life", "medium", e("WIRE", s=6, style="underline"))
d(["Undersell"], "Phrase", "medium", e("SELL", s=6, style="underline"))
d(["Undercut"], "Phrase", "medium", e("CUT", s=6, style="underline"))
d(["Undertone", "Undertones"], "Phrase", "hard", e("TONE", s=6, style="underline"))
# backwards
d(["Backstab", "Backstabbing", "Stab in the back"], "Phrase", "medium", e("BATS", s=6))
d(["Backpedal", "Backpedalling"], "Phrase", "medium", e("LADEP", s=6))
# sizes and positions
d(["Bigmouth", "Big mouth"], "Phrase", "medium", e("MOUTH", s=6))
d(["Top banana"], "Phrase", "medium", e("BANANA", y=15, s=4))
d(["Low cost", "Low-cost"], "Phrase", "easy", e("COST", y=85, s=4))
d(["Left wing", "Left-wing"], "Politics", "medium", e("WING", x=15, s=4))
d(["Right wing", "Right-wing"], "Politics", "medium", e("WING", x=85, s=4))
d(["Leftover", "Leftovers"], "Food and drink", "medium", e("OVER", x=15, s=4))
d(["Left hand", "Left-hand"], "Phrase", "medium", e("HAND", x=19, s=4))
d(["Right hand", "Right-hand", "Right-hand man"], "Phrase", "medium", e("HAND", x=81, s=4))
d(["Far left", "The far left"], "Politics", "hard", e("LEFT", x=12, s=3))
d(["Far right", "The far right"], "Politics", "hard", e("RIGHT", x=85, s=3))
d(["Downturn"], "Phrase", "hard", e("TURN", s=5, rot=90))
# hollow letters: ghost and ice
d(["Ghostwriter", "Ghost writer"], "Books", "medium", e("WRITER", s=5, style="outline"))
d(["Ghost ship"], "Phrase", "medium", e("SHIP", s=6, style="outline"))
d(["Iceberg"], "Nature", "hard", e("BERG", s=6, style="outline"))
d(["Ice queen", "The Ice Queen"], "Phrase", "hard", e("QUEEN", s=6, style="outline"))
# colours
d(["Gold medal"], "Sport", "easy", e("MEDAL", s=6, color=GOLD))

here = os.path.dirname(os.path.abspath(__file__))
have = set()
for f in glob.glob(os.path.join(here, '..', 'dingbat*.json')):
    if f.endswith('dingbat-16.json'): continue
    for r in json.load(open(f, encoding='utf-8')): have.update(a.lower() for a in r['answers'])
live = os.path.join(here, '..', '..', '..', 'lqsql', 'ding-a.json')
if os.path.exists(live): have.update(r['a'].lower() for r in json.load(open(live, encoding='utf-8'))['rows'] if r.get('a'))
clash = [b['answers'][0] for b in B if any(a.lower() in have for a in b['answers'])]
print('clash:', clash)
B = [b for b in B if b['answers'][0] not in clash]
json.dump(B, open(os.path.join(here, '..', 'dingbat-16.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'dingbats written')
