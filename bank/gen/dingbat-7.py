# Bank session 10 Oct 2026: more dingbats -> bank/dingbat-7.json. Checked against every answer already in bank/dingbat*.json.
# Elements: t text, x/y 0–100 (centre), s size 1–6, optional rot, flip "h"/"v", style strike/underline/box/outline, color #hex.
import json, os, glob
B = []
def d(answers, cat, diff, *els, tags=()):
    B.append({"answers": answers, "elements": [dict(e) for e in els], "category": cat, "tags": list(tags), "difficulty": diff})
def e(t, x=50, y=50, s=5, **k): return {"t": t, "x": x, "y": y, "s": s, **k}
RED, GREEN, PURPLE, GOLD, SILVER, PINK, YELLOW, BROWN = "#d42020", "#1f9a3a", "#7b2fbe", "#c9a227", "#9aa0a6", "#e8579a", "#e0b400", "#7a4a1e"

# words inside words
d(["Man in the middle", "Piggy in the middle"], "Phrase", "medium", e("MIDmanDLE", s=5))
d(["Hole in the wall"], "Phrase", "medium", e("WAholeLL", s=5))
d(["Foot in the door"], "Phrase", "medium", e("DOfootOR", s=5))
d(["Man in the moon"], "Phrase", "easy", e("MOmanON", s=5))
d(["Bun in the oven"], "Phrase", "medium", e("OVbunEN", s=5))
# position
d(["Sign on the dotted line"], "Phrase", "medium", e("SIGN", y=38, s=5), e(". . . . . . . . . .", y=64, s=4))
d(["Hot under the collar"], "Phrase", "medium", e("COLLAR", y=36, s=4), e("HOT", y=66, s=4, color=RED))
d(["Feeling under the weather", "Under the weather"], "Phrase", "easy", e("WEATHER", y=36, s=4), e("FEELING", y=66, s=4))
d(["Life after death"], "Phrase", "medium", e("DEATH", x=30, s=4), e("LIFE", x=74, s=4))
d(["Man about town"], "Phrase", "medium", e("TOWN", y=16, s=3), e("TOWN", x=16, s=3), e("MAN", s=4), e("TOWN", x=84, s=3), e("TOWN", y=84, s=3))
d(["Top Cat"], "TV", "easy", e("CAT", y=12, s=4), tags=["cartoons"])
d(["Highland", "Highlands"], "Places", "medium", e("LAND", y=10, s=4), tags=["Scotland"])
d(["Once bitten, twice shy", "Once bitten twice shy"], "Phrase", "medium", e("BITTEN", y=34, s=4), e("SHY  SHY", y=66, s=4))
d(["Neck and neck"], "Phrase", "easy", e("NECK  NECK", s=5))
# breaks, falls and turns
d(["Split decision"], "Phrase", "medium", e("DECI", x=32, y=46, s=5, rot=-10), e("SION", x=70, y=56, s=5, rot=10))
d(["Falling star", "Shooting star"], "Phrase", "medium", e("S", x=28, y=14, s=4), e("T", x=42, y=38, s=4), e("A", x=56, y=62, s=4), e("R", x=70, y=86, s=4))
d(["Stand-up comedy", "Stand up comedy"], "Phrase", "medium", e("COMEDY", s=4, rot=-90))
# colour
d(["Tickled pink"], "Phrase", "easy", e("TICKLED", s=5, color=PINK))
d(["Green light"], "Phrase", "easy", e("LIGHT", s=6, color=GREEN))
d(["Yellow card"], "Football", "easy", e("CARD", s=6, color=YELLOW))
d(["Purple Haze"], "Music", "medium", e("HAZE", s=6, color=PURPLE), tags=["Jimi Hendrix"])
d(["Brown sauce"], "Food and drink", "easy", e("SAUCE", s=6, color=BROWN))
d(["Silver spoon", "Born with a silver spoon"], "Phrase", "medium", e("SPOON", s=6, color=SILVER))
d(["Gold rush"], "History", "medium", e("RUSH", s=6, color=GOLD))
# size
d(["Little Women"], "Books", "medium", e("women", s=1), tags=["Louisa May Alcott"])
d(["Tiny Tim"], "Christmas", "medium", e("tim", s=1), tags=["Dickens"])

have = set()
here = os.path.dirname(os.path.abspath(__file__))
for f in glob.glob(os.path.join(here, '..', 'dingbat*.json')):
    if f.endswith('dingbat-7.json'): continue
    for r in json.load(open(f, encoding='utf-8')): have.update(a.lower() for a in r['answers'])
clash = [b['answers'][0] for b in B if any(a.lower() in have for a in b['answers'])]
assert not clash, clash
json.dump(B, open(os.path.join(here, '..', 'dingbat-7.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'dingbats written')
