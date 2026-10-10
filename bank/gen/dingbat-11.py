# Bank session 10 Oct 2026: 33 more dingbats -> bank/dingbat-11.json. Checked against every answer already in the bank (live and files).
# Elements: t text, x/y 0–100 (centre), s size 1–6, optional rot, flip "h"/"v", style strike/underline/box/outline, color #hex.
import json, os, glob
B = []
def d(answers, cat, diff, *els, tags=()):
    B.append({"answers": answers, "elements": [dict(e) for e in els], "category": cat, "tags": list(tags), "difficulty": diff})
def e(t, x=50, y=50, s=5, **k): return {"t": t, "x": x, "y": y, "s": s, **k}
RED, GREEN, PURPLE, GOLD, SILVER, PINK, YELLOW, BROWN = "#d42020", "#1f9a3a", "#7b2fbe", "#c9a227", "#9aa0a6", "#e8579a", "#e0b400", "#7a4a1e"
RED, GREY, GOLD, SILVER, YELLOW = "#d42020", "#8a8f94", "#c9a227", "#9aa0a6", "#e0b400"
BLUE, BLACK, BROWN, PURPLE, GREEN, PINK = "#1f5fd4", "#111111", "#7a4a1e", "#7b2fbe", "#1f9a3a", "#e8579a"

ORANGE = "#e07a00"

# colours
d(["Red wine"], "Food and drink", "easy", e("WINE", s=6, color=RED))
d(["Pink gin"], "Food and drink", "easy", e("GIN", s=6, color=PINK))
d(["Green beans"], "Food and drink", "easy", e("BEANS", s=6, color=GREEN))
d(["Blue jeans"], "Fashion", "easy", e("JEANS", s=6, color=BLUE))
d(["Orange squash"], "Food and drink", "easy", e("SQUASH", s=5, color=ORANGE))
d(["Golden syrup"], "Food and drink", "easy", e("SYRUP", s=6, color=GOLD))
d(["Silver Jubilee", "Silver jubilee"], "History", "medium", e("JUBILEE", s=5, color=SILVER))
d(["Yellow jersey", "The yellow jersey"], "Sport", "medium", e("JERSEY", s=5, color=YELLOW), tags=["Tour de France"])
d(["Brown sugar"], "Food and drink", "easy", e("SUGAR", s=6, color=BROWN))
# sizes and positions
d(["Big Fish"], "Film", "medium", e("FISH", s=6), tags=["Tim Burton"])
d(["Big Dipper", "The Big Dipper"], "Everyday life", "medium", e("DIPPER", s=6))
d(["Small wonder", "Small wonders"], "Phrase", "medium", e("wonder", s=1))
d(["Top Trumps"], "Games and toys", "easy", e("TRUMPS", y=8, s=5))
d(["Topknot", "Top knot"], "Fashion", "medium", e("KNOT", y=8, s=5))
# underlined
d(["Underline"], "Words and language", "easy", e("LINE", s=6, style="underline"))
d(["Understudy"], "Theatre", "medium", e("STUDY", s=6, style="underline"))
d(["Underwater"], "Nature", "easy", e("WATER", s=6, style="underline"))
d(["Underarm"], "Sport", "medium", e("ARM", s=6, style="underline"))
# backwards
d(["Backpack"], "Everyday life", "easy", e("KCAP", s=6))
d(["Backdrop"], "Theatre", "medium", e("PORD", s=6))
d(["Backgammon"], "Games and toys", "medium", e("NOMMAG", s=6))
d(["Backwater"], "Phrase", "medium", e("RETAW", s=6))
# doubled
d(["Double cream"], "Food and drink", "easy", e("CREAM CREAM", s=4))
d(["Double bass"], "Music", "easy", e("BASS BASS", s=5))
d(["Double yellow lines", "Double yellows"], "Everyday life", "medium", e("LINES LINES", s=4, color=YELLOW))
# split and crossed
d(["Split hairs", "Splitting hairs"], "Phrase", "medium", e("HA", x=38, y=46, s=6, rot=-10), e("IRS", x=64, y=56, s=6, rot=10))
d(["Crossbar"], "Sport", "medium", e("BAR", s=6, style="strike"))
d(["Crossfire", "Caught in the crossfire"], "Phrase", "medium", e("FIRE", s=6, style="strike"))
# in and counted
d(["The Cat in the Hat", "Cat in the Hat"], "Children's books", "medium", e("HAcatT", s=6), tags=["Dr. Seuss"])
d(["Ship in a bottle"], "Everyday life", "medium", e("BOTshipTLE", s=5))
d(["The Four Tops", "Four Tops"], "Music", "medium", e("TOPS TOPS TOPS TOPS", s=3))
d(["The Three Musketeers", "Three Musketeers"], "Books", "medium", e("MUSKETEER\nMUSKETEER\nMUSKETEER", s=3))
d(["Five a day", "Five-a-day"], "Food and drink", "medium", e("DAY DAY DAY DAY DAY", s=3))
have = set()
here = os.path.dirname(os.path.abspath(__file__))
for f in glob.glob(os.path.join(here, '..', 'dingbat*.json')):
    if f.endswith('dingbat-11.json'): continue
    for r in json.load(open(f, encoding='utf-8')): have.update(a.lower() for a in r['answers'])
live = os.path.join(here, '..', '..', '..', 'lqsql', 'ding-a.json')
if os.path.exists(live): have.update(r['a'].lower() for r in json.load(open(live, encoding='utf-8'))['rows'] if r.get('a'))
clash = [b['answers'][0] for b in B if any(a.lower() in have for a in b['answers'])]
assert not clash, clash
json.dump(B, open(os.path.join(here, '..', 'dingbat-11.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'dingbats written')
