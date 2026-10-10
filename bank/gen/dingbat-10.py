# Bank session 10 Oct 2026: 41 more dingbats (the classic phrases are all in already) -> bank/dingbat-10.json. Checked against every answer already in bank/dingbat*.json.
# Elements: t text, x/y 0–100 (centre), s size 1–6, optional rot, flip "h"/"v", style strike/underline/box/outline, color #hex.
import json, os, glob
B = []
def d(answers, cat, diff, *els, tags=()):
    B.append({"answers": answers, "elements": [dict(e) for e in els], "category": cat, "tags": list(tags), "difficulty": diff})
def e(t, x=50, y=50, s=5, **k): return {"t": t, "x": x, "y": y, "s": s, **k}
RED, GREEN, PURPLE, GOLD, SILVER, PINK, YELLOW, BROWN = "#d42020", "#1f9a3a", "#7b2fbe", "#c9a227", "#9aa0a6", "#e8579a", "#e0b400", "#7a4a1e"
RED, GREY, GOLD, SILVER, YELLOW = "#d42020", "#8a8f94", "#c9a227", "#9aa0a6", "#e0b400"
BLUE, BLACK, BROWN, PURPLE, GREEN, PINK = "#1f5fd4", "#111111", "#7a4a1e", "#7b2fbe", "#1f9a3a", "#e8579a"

# over, under and in
d(["Eye in the sky"], "Phrase", "medium", e("SKeyeY", s=6))
# top and bottom
d(["Bottom line", "The bottom line"], "Phrase", "easy", e("LINE", y=92, s=5))
# colours
d(["Black sheep", "Black sheep of the family"], "Phrase", "easy", e("SHEEP", s=6, color=BLACK))
d(["Brown bread"], "Food and drink", "easy", e("BREAD", s=6, color=BROWN))
# backwards, flipped and split
d(["Backstroke"], "Sport", "medium", e("EKORTS", s=6))
d(["Turn back time", "Turn back the clock"], "Phrase", "medium", e("EMIT", s=6))
d(["Upside-down cake", "Upside down cake", "Pineapple upside-down cake"], "Food and drink", "medium", e("CAKE", s=6, flip="v"))
# sizes, steps and counts
d(["Rising damp"], "Phrase", "medium", e("D", x=28, y=82, s=5), e("A", x=42, y=64, s=5), e("M", x=58, y=46, s=5), e("P", x=72, y=28, s=5), tags=["sitcoms"])
d(["Seven seas", "The seven seas"], "World geography", "medium", e("C C C C C C C", s=4))

# second batch: phrases not yet in the bank
d(["Upper class"], "Phrase", "easy", e("CLASS", y=8, s=5))
d(["Lower case", "Lowercase"], "Words and language", "medium", e("case", y=92, s=5))
d(["Highs and lows"], "Phrase", "medium", e("HIGHS", y=10, s=4), e("LOWS", y=90, s=4))
d(["Undercurrent"], "Nature", "hard", e("CURRENT", s=5, style="underline"))
d(["Back to back"], "Phrase", "medium", e("KCAB BACK", s=4))
d(["Backlash"], "Phrase", "medium", e("HSAL", s=6))
d(["Backlog"], "Phrase", "medium", e("GOL", s=6))
d(["Backbencher", "Backbenchers"], "Politics", "hard", e("REHCNEB", s=5))
d(["Spin doctor"], "Politics", "medium", e("DOCTOR", s=5, rot=160))
d(["Green tea"], "Food and drink", "easy", e("TEA", s=6, color=GREEN))
d(["Redwood"], "Nature", "easy", e("WOOD", s=6, color=RED))
d(["Blackbird"], "Nature", "easy", e("BIRD", s=6, color=BLACK))
d(["Blue Planet", "The Blue Planet"], "TV", "easy", e("PLANET", s=5, color=BLUE), tags=["David Attenborough"])
d(["Red Arrows", "The Red Arrows"], "Britain", "easy", e("ARROWS", s=5, color=RED))
d(["Golden Hind", "The Golden Hind"], "History", "medium", e("HIND", s=6, color=GOLD), tags=["Francis Drake"])
d(["Golden retriever"], "Nature", "easy", e("RETRIEVER", s=4, color=GOLD))
d(["Silver Surfer", "The Silver Surfer"], "Film", "medium", e("SURFER", s=5, color=SILVER), tags=["Marvel"])
d(["Purple Heart"], "History", "medium", e("HEART", s=6, color=PURPLE))
d(["Brown Owl"], "Everyday life", "medium", e("OWL", s=6, color=BROWN), tags=["Brownies"])
d(["Blue blood", "Blue-blooded"], "Phrase", "medium", e("BLOOD", s=6, color=BLUE))
d(["Black Widow"], "Film", "easy", e("WIDOW", s=6, color=BLACK), tags=["Marvel"])
d(["Green Goblin", "The Green Goblin"], "Film", "medium", e("GOBLIN", s=5, color=GREEN), tags=["Spider-Man"])
d(["Yellow Pages"], "Brands", "easy", e("PAGES", s=6, color=YELLOW))
d(["Blue Lagoon", "The Blue Lagoon"], "Film", "medium", e("LAGOON", s=5, color=BLUE))
d(["Little Chef"], "Brands", "easy", e("chef", s=1))
d(["Little Italy"], "World geography", "medium", e("italy", s=1))
d(["The Big Easy", "Big Easy"], "World geography", "medium", e("EASY", s=6), tags=["New Orleans"])
d(["Double take"], "Phrase", "easy", e("TAKE TAKE", s=5))
d(["Double trouble"], "Phrase", "easy", e("TROUBLE TROUBLE", s=3))
d(["Double agent"], "Phrase", "easy", e("AGENT AGENT", s=4))
d(["Split level", "Split-level"], "Everyday life", "medium", e("LEV", x=38, y=46, s=6, rot=-10), e("EL", x=64, y=56, s=6, rot=10))
d(["Broken Arrow"], "Film", "hard", e("ARR", x=38, y=46, s=6, rot=-15), e("OW", x=64, y=58, s=6, rot=15))

have = set()
here = os.path.dirname(os.path.abspath(__file__))
for f in glob.glob(os.path.join(here, '..', 'dingbat*.json')):
    if f.endswith('dingbat-10.json'): continue
    for r in json.load(open(f, encoding='utf-8')): have.update(a.lower() for a in r['answers'])
live = os.path.join(here, '..', '..', '..', 'lqsql', 'ding-a.json')
if os.path.exists(live): have.update(r['a'].lower() for r in json.load(open(live, encoding='utf-8'))['rows'] if r.get('a'))
clash = [b['answers'][0] for b in B if any(a.lower() in have for a in b['answers'])]
assert not clash, clash
json.dump(B, open(os.path.join(here, '..', 'dingbat-10.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'dingbats written')
