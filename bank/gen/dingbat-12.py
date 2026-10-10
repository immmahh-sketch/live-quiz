# Bank session 10 Oct 2026: 30 more dingbats -> bank/dingbat-12.json. Checked against every answer already in the bank (live and files).
# Elements: t text, x/y 0–100 (centre), s size 1–6, optional rot, flip "h"/"v", style strike/underline/box/outline, color #hex.
import json, os, glob
B = []
def d(answers, cat, diff, *els, tags=()):
    B.append({"answers": answers, "elements": [dict(e) for e in els], "category": cat, "tags": list(tags), "difficulty": diff})
def e(t, x=50, y=50, s=5, **k): return {"t": t, "x": x, "y": y, "s": s, **k}
RED, GREY, GOLD, SILVER, YELLOW = "#d42020", "#8a8f94", "#c9a227", "#9aa0a6", "#e0b400"
BLUE, BROWN, PURPLE, GREEN, PINK, ORANGE = "#1f5fd4", "#7a4a1e", "#7b2fbe", "#1f9a3a", "#e8579a", "#e07a00"

# colours
d(["Grey's Anatomy", "Greys Anatomy"], "TV", "medium", e("ANATOMY", s=5, color=GREY))
d(["Silver fox"], "Phrase", "medium", e("FOX", s=6, color=SILVER))
d(["Golden eagle"], "Nature", "easy", e("EAGLE", s=6, color=GOLD))
d(["Golden ticket", "The golden ticket"], "Children's books", "easy", e("TICKET", s=5, color=GOLD), tags=["Willy Wonka"])
d(["Redcurrant", "Redcurrants"], "Food and drink", "medium", e("CURRANT", s=5, color=RED))
d(["Pink lemonade"], "Food and drink", "easy", e("LEMONADE", s=4, color=PINK))
d(["Green card"], "Phrase", "medium", e("CARD", s=6, color=GREEN))
d(["Red kite"], "Nature", "medium", e("KITE", s=6, color=RED))
d(["Brown bear"], "Nature", "easy", e("BEAR", s=6, color=BROWN))
d(["Orange peel"], "Food and drink", "easy", e("PEEL", s=6, color=ORANGE))
# sizes and positions
d(["Big cat", "Big cats"], "Nature", "easy", e("CAT", s=6))
d(["Bigfoot", "Big Foot"], "Phrase", "easy", e("FOOT", s=6))
d(["Little toe"], "Phrase", "easy", e("toe", s=1))
d(["Upper hand", "The upper hand"], "Phrase", "medium", e("HAND", y=8, s=5))
d(["Top floor"], "Phrase", "easy", e("FLOOR", y=8, s=5))
d(["Underpants"], "Phrase", "easy", e("PANTS", s=6, style="underline"))
# backwards
d(["Backyard", "Back yard"], "Phrase", "easy", e("DRAY", s=6))
d(["Backstreet", "Back street"], "Phrase", "medium", e("TEERTS", s=6))
d(["Backpacker"], "Travel", "medium", e("REKCAP", s=6))
# doubled
d(["Double glazing"], "Everyday life", "easy", e("GLAZING GLAZING", s=3))
d(["Double chin"], "Phrase", "easy", e("CHIN CHIN", s=5))
d(["Double espresso"], "Food and drink", "medium", e("ESPRESSO ESPRESSO", s=3))
# crossed out
d(["Crossbow"], "History", "easy", e("BOW", s=6, style="strike"))
d(["Cross-country", "Cross country"], "Sport", "medium", e("COUNTRY", s=5, style="strike"))
d(["Cross stitch", "Cross-stitch"], "Everyday life", "medium", e("STITCH", s=5, style="strike"))
# in and counted
d(["Fish in a barrel", "Shooting fish in a barrel"], "Phrase", "medium", e("BARfishREL", s=5))
d(["Snake in the grass", "A snake in the grass"], "Phrase", "medium", e("GRAsnakeSS", s=5))
d(["Seven Dwarfs", "The Seven Dwarfs"], "Children's books", "medium", e("DWARF DWARF DWARF\nDWARF DWARF\nDWARF DWARF", s=2))
d(["Six Nations", "The Six Nations"], "Sport", "medium", e("NATIONS NATIONS\nNATIONS NATIONS\nNATIONS NATIONS", s=2), tags=["rugby"])
d(["Nine lives"], "Phrase", "medium", e("LIVES LIVES LIVES\nLIVES LIVES LIVES\nLIVES LIVES LIVES", s=2))

have = set()
here = os.path.dirname(os.path.abspath(__file__))
for f in glob.glob(os.path.join(here, '..', 'dingbat*.json')):
    if f.endswith('dingbat-12.json'): continue
    for r in json.load(open(f, encoding='utf-8')): have.update(a.lower() for a in r['answers'])
live = os.path.join(here, '..', '..', '..', 'lqsql', 'ding-a.json')
if os.path.exists(live): have.update(r['a'].lower() for r in json.load(open(live, encoding='utf-8'))['rows'] if r.get('a'))
clash = [b['answers'][0] for b in B if any(a.lower() in have for a in b['answers'])]
assert not clash, clash
json.dump(B, open(os.path.join(here, '..', 'dingbat-12.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'dingbats written')
