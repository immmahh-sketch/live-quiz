# Bank session 9 Oct 2026: 32 new dingbats -> bank/dingbat-3.json. None of these answers is in the live bank yet.
# Elements: t text, x/y 0–100 (centre), s size 1–6, optional rot, flip "h"/"v", style strike/underline/box/outline.
import json, os
B = []
def d(answers, cat, diff, *els, tags=()):
    B.append({"answers": answers, "elements": [dict(e) for e in els], "category": cat, "tags": list(tags), "difficulty": diff})
def e(t, x=50, y=50, s=5, **k): return {"t": t, "x": x, "y": y, "s": s, **k}

d(["Mind the gap"], "Phrase", "easy", e("MI      ND"), tags=["London"])
d(["Banana split"], "Food", "easy", e("BANA      NA"))
d(["Broken promise"], "Phrase", "easy", e("PROM  ISE"))
d(["Cross my heart"], "Phrase", "medium", e("MY", x=24, s=4), e("HEART", x=60, s=4), e("X", x=60, s=6, color="#d22"))
d(["Once in a lifetime"], "Phrase", "medium", e("LIFEonceTIME", s=4))
d(["Forgive and forget"], "Phrase", "easy", e("4GIVE & 4GET"))
d(["Tuna sandwich"], "Food", "easy", e("BREAD", y=26, s=4), e("TUNA", y=50, s=4), e("BREAD", y=74, s=4))
d(["Sitting on the fence"], "Phrase", "easy", e("SITTING", y=34, s=4), e("|‾|‾|‾|‾|‾|‾|", y=64, s=4))
d(["Square dance"], "Phrase", "medium", e("DANCE", style="box"))
d(["Square root"], "Maths", "medium", e("ROOT", style="box"))
d(["Thinking outside the box"], "Phrase", "easy", e("THINKING", y=24, s=4), e("BOX", y=64, s=4, style="box"))
d(["Strike a pose"], "Music", "medium", e("POSE", s=6, style="strike"), tags=["Madonna"])
d(["Hollow victory"], "Phrase", "hard", e("VICTORY", s=5, style="outline"))
d(["Mirror image"], "Phrase", "easy", e("IMAGE", x=30, s=4), e("IMAGE", x=72, s=4, flip="h"))
d(["Turn the tables"], "Phrase", "medium", e("TABLES", s=5, rot=180))
d(["Backfire"], "Word", "easy", e("FIRE", s=6, flip="h"))
d(["Little Mix"], "Music", "medium", e("ltteil", s=2), tags=["girl groups"])
d(["Three Lions"], "Football", "easy", e("LIONS", y=24, s=4), e("LIONS", y=50, s=4), e("LIONS", y=76, s=4), tags=["England"])
d(["Two left feet"], "Phrase", "medium", e("FEET", x=16, y=38, s=4), e("FEET", x=16, y=64, s=4))
d(["Blood is thicker than water"], "Phrase", "medium", e("BLOOD", y=40, s=6), e("water", y=78, s=1))
d(["It's a small world", "Small world"], "Phrase", "easy", e("world", s=1))
d(["Big Bang", "The Big Bang Theory"], "Science", "easy", e("BANG", s=6))
d(["Low budget"], "Phrase", "easy", e("budget", y=90, s=3))
d(["High tide"], "Phrase", "easy", e("TIDE", y=10, s=4))
d(["Unfinished business"], "Phrase", "easy", e("BUSINE", s=5))
d(["Shrinking violet"], "Phrase", "medium", e("VIOLET", y=22, s=5), e("VIOLET", y=56, s=3), e("VIOLET", y=80, s=1))
d(["Growing up"], "Phrase", "easy", e("up", y=80, s=1), e("UP", y=60, s=3), e("UP", y=28, s=5))
d(["Tongue in cheek"], "Phrase", "easy", e("CHEtongueEK", s=4))
d(["Pain in the neck"], "Phrase", "easy", e("NEpainCK", s=5))
d(["Search high and low"], "Phrase", "medium", e("SEARCH", y=10, s=4), e("SEARCH", y=90, s=4))
d(["Fallen angel"], "Phrase", "medium", e("ANGEL", y=82, s=5, rot=180))
d(["Seven Up", "7 Up"], "Food", "medium", e("UP UP UP UP UP UP UP", s=3))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'dingbat-3.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'dingbats written')
