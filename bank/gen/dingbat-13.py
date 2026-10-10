# Bank session 11 Oct 2026: more dingbats -> bank/dingbat-13.json. Checked against every answer already in the bank (live and files).
# Elements: t text, x/y 0–100 (centre), s size 1–6, optional rot, flip "h"/"v", style strike/underline/box/outline, color #hex.
import json, os, glob
B = []
def d(answers, cat, diff, *els, tags=()):
    B.append({"answers": answers, "elements": [dict(e) for e in els], "category": cat, "tags": list(tags), "difficulty": diff})
def e(t, x=50, y=50, s=5, **k): return {"t": t, "x": x, "y": y, "s": s, **k}
RED, GREY, GOLD, SILVER, YELLOW = "#d42020", "#8a8f94", "#c9a227", "#9aa0a6", "#e0b400"
BLUE, BROWN, PURPLE, GREEN, PINK, ORANGE = "#1f5fd4", "#7a4a1e", "#7b2fbe", "#1f9a3a", "#e8579a", "#e07a00"


# colours
d(["Green belt"], "Phrase", "medium", e("BELT", s=6, color=GREEN))
d(["Golden goose", "The golden goose"], "Phrase", "medium", e("GOOSE", s=6, color=GOLD))
d(["Bluebell"], "Nature", "easy", e("BELL", s=6, color=BLUE))
d(["Bluebottle", "Blue bottle"], "Nature", "medium", e("BOTTLE", s=6, color=BLUE))
d(["Bluebird"], "Nature", "easy", e("BIRD", s=6, color=BLUE))
d(["Blue tit"], "Nature", "easy", e("TIT", s=6, color=BLUE))
d(["Green Goddess", "The Green Goddess"], "TV", "medium", e("GODDESS", s=5, color=GREEN))
d(["Green Lantern"], "Film", "medium", e("LANTERN", s=5, color=GREEN))
d(["Greyhound"], "Nature", "easy", e("HOUND", s=6, color=GREY))
d(["Goldfish"], "Nature", "easy", e("FISH", s=6, color=GOLD))
d(["Golden oldie", "Golden oldies"], "Phrase", "medium", e("OLDIE", s=6, color=GOLD))
d(["Silverware"], "Sport", "medium", e("WARE", s=6, color=SILVER))
d(["Red squirrel"], "Nature", "easy", e("SQUIRREL", s=4, color=RED))
d(["Red light"], "Phrase", "easy", e("LIGHT", s=6, color=RED))
d(["Red rose"], "Nature", "easy", e("ROSE", s=6, color=RED))
d(["Red Admiral"], "Nature", "medium", e("ADMIRAL", s=5, color=RED))
# sizes and positions
d(["Little finger"], "Phrase", "easy", e("finger", s=1))
d(["High tea"], "Food and drink", "medium", e("TEA", y=15, s=4))
d(["High street", "The high street"], "Phrase", "easy", e("STREET", y=15, s=4))
d(["High heels"], "Fashion", "easy", e("HEELS", y=15, s=4))
d(["Upstairs"], "Phrase", "easy", e("STAIRS", y=15, s=4))
d(["Uptown"], "Places", "medium", e("TOWN", y=15, s=4))
d(["Downstairs"], "Phrase", "easy", e("STAIRS", y=85, s=4))
d(["Low key", "Low-key"], "Phrase", "medium", e("KEY", y=85, s=4))
d(["Lowlands", "The Lowlands"], "Places", "medium", e("LANDS", y=85, s=4))
d(["Lie low"], "Phrase", "medium", e("LIE", y=85, s=4))
d(["Stand up", "Stand-up"], "Phrase", "medium", e("STAND", s=5, rot=-90))
d(["Rising star"], "Phrase", "medium", e("STAR", x=20, y=78, s=3), e("STAR", x=50, y=50, s=3), e("STAR", x=80, y=22, s=3))
d(["Sinking feeling", "That sinking feeling"], "Phrase", "medium", e("FEELING", x=25, y=22, s=3), e("FEELING", x=50, y=50, s=3), e("FEELING", x=75, y=78, s=3))
d(["Face to face"], "Phrase", "medium", e("FACE", x=27, s=5), e("FACE", x=73, s=5, flip="h"))
# crossed out
d(["Cross Channel", "Cross-Channel"], "Travel", "medium", e("CHANNEL", s=5, style="strike"))
d(["Crosswind"], "Nature", "medium", e("WIND", s=6, style="strike"))
d(["Crossbones", "Skull and crossbones"], "History", "medium", e("BONES", s=6, style="strike"))
# in
d(["Pig in a poke", "A pig in a poke"], "Phrase", "hard", e("POpigKE", s=5))
d(["Frog in your throat", "A frog in your throat", "Frog in the throat"], "Phrase", "medium", e("THRfrogOAT", s=4))
d(["Bull in a china shop", "A bull in a china shop"], "Phrase", "medium", e("CHINA SHbullOP", s=3))
d(["Needle in a haystack", "A needle in a haystack"], "Phrase", "medium", e("HAYneedleSTACK", s=3))
d(["Lost in space"], "TV", "medium", e("SPAlostCE", s=4))
d(["Hand in hand"], "Phrase", "easy", e("HAhandND", s=5))
d(["Arm in arm"], "Phrase", "easy", e("ARarmM", s=5))

have = set()
here = os.path.dirname(os.path.abspath(__file__))
for f in glob.glob(os.path.join(here, '..', 'dingbat*.json')):
    if f.endswith('dingbat-13.json'): continue
    for r in json.load(open(f, encoding='utf-8')): have.update(a.lower() for a in r['answers'])
live = os.path.join(here, '..', '..', '..', 'lqsql', 'ding-a.json')
if os.path.exists(live): have.update(r['a'].lower() for r in json.load(open(live, encoding='utf-8'))['rows'] if r.get('a'))
clash = [b['answers'][0] for b in B if any(a.lower() in have for a in b['answers'])]
print('clash:', clash)
B = [b for b in B if b['answers'][0] not in clash]
json.dump(B, open(os.path.join(here, '..', 'dingbat-13.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'dingbats written')
