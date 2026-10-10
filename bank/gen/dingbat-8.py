# Bank session 10 Oct 2026: more dingbats -> bank/dingbat-8.json. Checked against every answer already in bank/dingbat*.json.
# Elements: t text, x/y 0–100 (centre), s size 1–6, optional rot, flip "h"/"v", style strike/underline/box/outline, color #hex.
import json, os, glob
B = []
def d(answers, cat, diff, *els, tags=()):
    B.append({"answers": answers, "elements": [dict(e) for e in els], "category": cat, "tags": list(tags), "difficulty": diff})
def e(t, x=50, y=50, s=5, **k): return {"t": t, "x": x, "y": y, "s": s, **k}
RED, GREEN, PURPLE, GOLD, SILVER, PINK, YELLOW, BROWN = "#d42020", "#1f9a3a", "#7b2fbe", "#c9a227", "#9aa0a6", "#e8579a", "#e0b400", "#7a4a1e"
RED, GREEN, BLUE, GREY, GOLD, YELLOW, ORANGE, BLUECHEESE = "#d42020", "#1f9a3a", "#1f5fd4", "#8a8f94", "#c9a227", "#e0b400", "#f07c1a", "#4a7bd0"

# reversals and halves
d(["Backhand"], "Sport", "medium", e("DNAH", s=6))
d(["Reverse gear", "Reverse gears"], "Phrase", "medium", e("RAEG", s=6))
d(["Back to front"], "Phrase", "medium", e("TNORF", s=6))
d(["Half time", "Half-time"], "Football", "medium", e("TI", s=6))
d(["Half moon", "Half-moon"], "Phrase", "medium", e("MO", s=6))
# size and shape
d(["The Little Mermaid", "Little Mermaid"], "Film", "medium", e("mermaid", s=1), tags=["Disney"])
d(["Big Bird"], "TV", "medium", e("BIRD", s=6), tags=["Sesame Street"])
d(["Small screen"], "TV", "medium", e("screen", s=1))
d(["Tall story", "Tall tale"], "Phrase", "medium", e("S", y=14, s=4), e("T", y=32, s=4), e("O", y=50, s=4), e("R", y=68, s=4), e("Y", y=86, s=4))
# colour
d(["Red tape"], "Phrase", "easy", e("TAPE", s=6, color=RED))
d(["Blue cheese"], "Food and drink", "easy", e("CHEESE", s=5, color=BLUECHEESE))
d(["The Green Mile", "Green Mile"], "Film", "medium", e("MILE", s=6, color=GREEN), tags=["Tom Hanks"])
d(["Orange County"], "Places", "medium", e("COUNTY", s=5, color=ORANGE))
d(["Yellow fever"], "Phrase", "medium", e("FEVER", s=6, color=YELLOW))
d(["Grey area"], "Phrase", "easy", e("AREA", s=6, color=GREY))
d(["Golden Globe", "Golden Globes"], "Film", "medium", e("GLOBE", s=6, color=GOLD))
# styles, flips and turns
d(["Cross-eyed", "Cross eyed"], "Phrase", "medium", e("EYED", s=6, style="strike"))
d(["Cancelled flight", "Flight cancelled"], "Phrase", "medium", e("FLIGHT", s=5, style="strike"))
d(["Box set", "Boxset", "Box-set"], "TV", "easy", e("SET", s=6, style="box"))
d(["Flipping heck"], "Phrase", "medium", e("HECK", s=6, flip="v"))
d(["Turning point"], "Phrase", "medium", e("POINT", s=5, rot=90))
d(["Leaning Tower of Pisa", "The Leaning Tower of Pisa"], "Places", "medium", e("PISA", s=6, rot=12))
d(["Double Dutch"], "Phrase", "medium", e("DUTCH  DUTCH", s=5))
# things in, among and out of things
d(["Pie in the sky"], "Phrase", "medium", e("SKpieY", s=6))
d(["Frog in the throat", "A frog in your throat", "A frog in the throat"], "Phrase", "medium", e("THRfrogOAT", s=5))
d(["Ants in your pants", "Ants in his pants", "Ants in the pants"], "Phrase", "medium", e("PAantsNTS", s=5))
d(["Cat among the pigeons", "Put the cat among the pigeons"], "Phrase", "medium", e("PIGEONS", x=26, y=20, s=3), e("PIGEONS", x=74, y=24, s=3), e("CAT", s=5),
  e("PIGEONS", x=24, y=78, s=3), e("PIGEONS", x=76, y=80, s=3))
d(["Fish out of water", "Like a fish out of water"], "Phrase", "medium", e("fish", y=22, s=2), e("WATER", y=66, s=5))

have = set()
here = os.path.dirname(os.path.abspath(__file__))
for f in glob.glob(os.path.join(here, '..', 'dingbat*.json')):
    if f.endswith('dingbat-8.json'): continue
    for r in json.load(open(f, encoding='utf-8')): have.update(a.lower() for a in r['answers'])
clash = [b['answers'][0] for b in B if any(a.lower() in have for a in b['answers'])]
assert not clash, clash
json.dump(B, open(os.path.join(here, '..', 'dingbat-8.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'dingbats written')
