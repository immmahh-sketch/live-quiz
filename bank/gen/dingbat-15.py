# Bank session 11 Oct 2026: more dingbats -> bank/dingbat-15.json. Checked against every answer already in the bank (live and files).
# Elements: t text, x/y 0–100 (centre), s size 1–6, optional rot, flip "h"/"v", style strike/underline/box/outline, color #hex.
import json, os, glob
B = []
def d(answers, cat, diff, *els, tags=()):
    B.append({"answers": answers, "elements": [dict(e) for e in els], "category": cat, "tags": list(tags), "difficulty": diff})
def e(t, x=50, y=50, s=5, **k): return {"t": t, "x": x, "y": y, "s": s, **k}
RED, GREY, GOLD, SILVER, YELLOW = "#d42020", "#8a8f94", "#c9a227", "#9aa0a6", "#e0b400"
BLUE, BROWN, PURPLE, GREEN, PINK, ORANGE = "#1f5fd4", "#7a4a1e", "#7b2fbe", "#1f9a3a", "#e8579a", "#e07a00"


# under (underlined)
d(["Underfoot"], "Phrase", "medium", e("FOOT", s=6, style="underline"))
d(["Underhand"], "Phrase", "medium", e("HAND", s=6, style="underline"))
d(["Underpaid"], "Phrase", "medium", e("PAID", s=6, style="underline"))
d(["Underrated"], "Phrase", "medium", e("RATED", s=5, style="underline"))
d(["Undersea"], "Nature", "medium", e("SEA", s=6, style="underline"))
d(["Undercoat"], "Everyday life", "medium", e("COAT", s=6, style="underline"))
d(["Underestimate"], "Phrase", "hard", e("ESTIMATE", s=4, style="underline"))
# crossed out
d(["Crosshair", "Crosshairs"], "Phrase", "medium", e("HAIR", s=6, style="strike"))
d(["Cross purposes", "At cross purposes"], "Phrase", "hard", e("PURPOSES", s=4, style="strike"))
# backwards
d(["Backflip"], "Sport", "easy", e("PILF", s=6))
d(["Backlit"], "Phrase", "medium", e("TIL", s=6))
d(["Backslash"], "Phrase", "medium", e("HSALS", s=6))
d(["Backwash"], "Phrase", "medium", e("HSAW", s=6))
d(["Backpacking"], "Travel", "medium", e("GNIKCAP", s=4))
d(["Backbite", "Backbiting"], "Phrase", "hard", e("ETIB", s=6))
# sizes and positions
d(["Big game"], "Sport", "medium", e("GAME", s=6))
d(["Big time", "The big time"], "Phrase", "medium", e("TIME", s=6))
d(["Bigwig"], "Phrase", "medium", e("WIG", s=6))
d(["Big screen", "The big screen"], "Film", "medium", e("SCREEN", s=5))
d(["Small hours", "The small hours"], "Phrase", "medium", e("hours", s=1))
d(["Small town"], "Phrase", "easy", e("town", s=1))
d(["Top brass"], "Phrase", "medium", e("BRASS", y=15, s=4))
d(["Top drawer"], "Phrase", "medium", e("DRAWER", y=15, s=4))
d(["Top shelf"], "Phrase", "easy", e("SHELF", y=15, s=4))
d(["Top notch"], "Phrase", "medium", e("NOTCH", y=15, s=4))
d(["High noon"], "Film", "medium", e("NOON", y=15, s=4))
d(["High rise", "High-rise"], "Phrase", "easy", e("RISE", y=15, s=4))
d(["High stakes"], "Phrase", "medium", e("STAKES", y=15, s=4))
d(["Low fat", "Low-fat"], "Food and drink", "easy", e("FAT", y=85, s=4))
d(["Low profile", "Keep a low profile"], "Phrase", "medium", e("PROFILE", y=85, s=4))
d(["Low season"], "Travel", "medium", e("SEASON", y=85, s=4))
d(["Low blow"], "Phrase", "medium", e("BLOW", y=85, s=4))
# colours
d(["Red mist", "The red mist"], "Phrase", "medium", e("MIST", s=6, color=RED))
d(["Redneck"], "Phrase", "medium", e("NECK", s=6, color=RED))
d(["Red-handed", "Caught red-handed", "Red handed"], "Phrase", "medium", e("HANDED", s=5, color=RED))
d(["Greenback"], "Phrase", "hard", e("BACK", s=6, color=GREEN))
d(["Blue chip", "Blue-chip"], "Phrase", "medium", e("CHIP", s=6, color=BLUE))
d(["Bluegrass"], "Music", "medium", e("GRASS", s=6, color=BLUE))
d(["Blueprint"], "Phrase", "easy", e("PRINT", s=6, color=BLUE))
d(["Golden rule", "The golden rule"], "Phrase", "medium", e("RULE", s=6, color=GOLD))
d(["Goldmine", "Gold mine"], "Phrase", "easy", e("MINE", s=6, color=GOLD))
d(["Goldsmith"], "Phrase", "medium", e("SMITH", s=6, color=GOLD))
d(["Silverback"], "Nature", "medium", e("BACK", s=6, color=SILVER))
d(["Yellow belly", "Yellow-bellied"], "Phrase", "medium", e("BELLY", s=6, color=YELLOW))

have = set()
here = os.path.dirname(os.path.abspath(__file__))
for f in glob.glob(os.path.join(here, '..', 'dingbat*.json')):
    if f.endswith('dingbat-15.json'): continue
    for r in json.load(open(f, encoding='utf-8')): have.update(a.lower() for a in r['answers'])
live = os.path.join(here, '..', '..', '..', 'lqsql', 'ding-a.json')
if os.path.exists(live): have.update(r['a'].lower() for r in json.load(open(live, encoding='utf-8'))['rows'] if r.get('a'))
clash = [b['answers'][0] for b in B if any(a.lower() in have for a in b['answers'])]
print('clash:', clash)
B = [b for b in B if b['answers'][0] not in clash]
json.dump(B, open(os.path.join(here, '..', 'dingbat-15.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'dingbats written')
