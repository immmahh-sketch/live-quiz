# Bank session 10 Oct 2026: more dingbats -> bank/dingbat-9.json. Checked against every answer already in bank/dingbat*.json.
# Elements: t text, x/y 0–100 (centre), s size 1–6, optional rot, flip "h"/"v", style strike/underline/box/outline, color #hex.
import json, os, glob
B = []
def d(answers, cat, diff, *els, tags=()):
    B.append({"answers": answers, "elements": [dict(e) for e in els], "category": cat, "tags": list(tags), "difficulty": diff})
def e(t, x=50, y=50, s=5, **k): return {"t": t, "x": x, "y": y, "s": s, **k}
RED, GREEN, PURPLE, GOLD, SILVER, PINK, YELLOW, BROWN = "#d42020", "#1f9a3a", "#7b2fbe", "#c9a227", "#9aa0a6", "#e8579a", "#e0b400", "#7a4a1e"
RED, GREY, GOLD, SILVER, YELLOW = "#d42020", "#8a8f94", "#c9a227", "#9aa0a6", "#e0b400"

# up, down, high and low
d(["Upset"], "Phrase", "medium", e("SET", y=10, s=5))
d(["Downpour"], "Weather", "medium", e("POUR", y=90, s=5))
d(["Highly strung"], "Phrase", "medium", e("STRUNG", y=8, s=4))
d(["High hopes"], "Phrase", "medium", e("HOPES", y=8, s=4))
d(["Low tide"], "Nature", "medium", e("TIDE", y=92, s=4))
d(["Bottoms up", "Bottoms up!"], "Phrase", "medium", e("BOTTOMS", y=10, s=4))
# backwards
d(["Back pay"], "Phrase", "medium", e("YAP", s=6))
d(["Feedback"], "Phrase", "medium", e("DEEF", s=6))
# splits and sizes
d(["Split pea", "Split peas"], "Food and drink", "medium", e("P", x=40, y=46, s=6, rot=-10), e("EA", x=62, y=56, s=6, rot=10))
d(["Big Mac"], "Food and drink", "easy", e("MAC", s=6), tags=["McDonald's"])
d(["Small change"], "Phrase", "medium", e("change", s=1))
d(["Tall order"], "Phrase", "medium", e("O", y=14, s=4), e("R", y=32, s=4), e("D", y=50, s=4), e("E", y=68, s=4), e("R", y=86, s=4))
# colour
d(["Grey squirrel"], "Nature", "easy", e("SQUIRREL", s=5, color=GREY))
d(["Red herring"], "Phrase", "easy", e("HERRING", s=5, color=RED))
d(["Golden handshake"], "Phrase", "medium", e("HANDSHAKE", s=4, color=GOLD))
d(["Silver birch"], "Nature", "medium", e("BIRCH", s=6, color=SILVER))
d(["Yellow Brick Road", "The Yellow Brick Road", "Goodbye Yellow Brick Road"], "Film", "medium", e("BRICK ROAD", s=4, color=YELLOW), tags=["The Wizard of Oz"])
d(["Red Rum"], "Sport", "medium", e("RUM", s=6, color=RED), tags=["Grand National"])
# things in, over and up
d(["Hand over fist"], "Phrase", "medium", e("HAND", y=35, s=5), e("FIST", y=67, s=5))
d(["A bird in the hand", "Bird in the hand", "A bird in the hand is worth two in the bush"], "Phrase", "medium", e("HAbirdND", s=6))
d(["Spanner in the works", "A spanner in the works"], "Phrase", "medium", e("WORspannerKS", s=4))
d(["Feather in your cap", "A feather in your cap", "Feather in his cap"], "Phrase", "medium", e("CfeatherAP", s=5))
d(["Bee in your bonnet", "A bee in your bonnet", "Bee in her bonnet"], "Phrase", "medium", e("BONbeeNET", s=5))
d(["Elephant in the room", "The elephant in the room"], "Phrase", "medium", e("ROelephantOM", s=4))
d(["Ace up your sleeve", "An ace up your sleeve", "Ace up the sleeve"], "Phrase", "medium", e("ACE", y=30, s=4), e("SLEEVE", y=66, s=5))
# styles and repeats
d(["Crossed wires", "Crossed lines"], "Phrase", "medium", e("WIRES", s=6, style="strike"))
d(["Boxing clever"], "Phrase", "medium", e("CLEVER", s=5, style="box"))
d(["Flipping burgers", "Burger flipping"], "Food and drink", "medium", e("BURGERS", s=5, flip="v"))
d(["Two-tone", "Two tone"], "Music", "medium", e("TONE  TONE", s=5))

have = set()
here = os.path.dirname(os.path.abspath(__file__))
for f in glob.glob(os.path.join(here, '..', 'dingbat*.json')):
    if f.endswith('dingbat-9.json'): continue
    for r in json.load(open(f, encoding='utf-8')): have.update(a.lower() for a in r['answers'])
live = os.path.join(here, '..', '..', '..', 'lqsql', 'ding-a.json')
if os.path.exists(live): have.update(r['a'].lower() for r in json.load(open(live, encoding='utf-8'))['rows'] if r.get('a'))
clash = [b['answers'][0] for b in B if any(a.lower() in have for a in b['answers'])]
assert not clash, clash
json.dump(B, open(os.path.join(here, '..', 'dingbat-9.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'dingbats written')
