# Bank session 9 Oct 2026 (third pass): 29 new dingbats -> bank/dingbat-5.json. None of these answers is live yet.
# Elements: t text, x/y 0–100 (centre), s size 1–6, optional rot, flip "h"/"v", style strike/underline/box/outline, color #hex.
import json, os
B = []
def d(answers, cat, diff, *els, tags=()):
    B.append({"answers": answers, "elements": [dict(e) for e in els], "category": cat, "tags": list(tags), "difficulty": diff})
def e(t, x=50, y=50, s=5, **k): return {"t": t, "x": x, "y": y, "s": s, **k}
RED, GREEN, BLUE, PINK, SILVER, GOLD, ORANGE, YELLOW, PALE = "#d42020", "#1f9a3a", "#1f5fd4", "#ff5fa8", "#9aa0a6", "#c9a227", "#f28c18", "#e8c400", "#cfd3d6"

# colour
d(["Greenland"], "Geography", "easy", e("LAND", s=6, color=GREEN))
d(["Red Sea", "The Red Sea"], "Geography", "easy", e("SEA", s=6, color=RED))
d(["Yellowstone"], "Geography", "medium", e("STONE", s=6, color=YELLOW))
d(["Pink Lady"], "Food", "medium", e("LADY", s=6, color=PINK), tags=["apples", "cocktails"])
d(["Orange juice"], "Food", "easy", e("JUICE", s=6, color=ORANGE))
d(["Redcar"], "The North East of England", "medium", e("CAR", s=6, color=RED))
d(["Red card"], "Football", "easy", e("CARD", s=6, color=RED))
d(["Blue whale"], "Animals", "easy", e("WHALE", s=6, color=BLUE))
d(["Silver lining", "Every cloud has a silver lining"], "Phrase", "medium", e("LINING", s=5, color=SILVER))
d(["Golden Gate", "Golden Gate Bridge"], "Places", "medium", e("GATE", s=6, color=GOLD))
d(["Light sleeper"], "Phrase", "medium", e("SLEEPER", s=5, color=PALE))
d(["Bright idea"], "Phrase", "medium", e("IDEA", s=6, color=YELLOW))
d(["Blank cheque"], "Phrase", "medium", e("CHEQUE", s=6, style="outline"))
# position, size and spacing
d(["High five"], "Phrase", "easy", e("5", y=8, s=4))
d(["Top of the morning"], "Phrase", "medium", e("MORNING", y=8, s=4))
d(["Big wheel"], "Phrase", "easy", e("WHEEL", s=6))
d(["Small fry"], "Phrase", "medium", e("fry", s=1))
d(["Spaced out"], "Phrase", "easy", e("S   P   A   C   E   D", s=3))
d(["Square eyes"], "Phrase", "easy", e("EYES", s=6, style="box"))
d(["Falling apart"], "Phrase", "medium", e("A", x=30, y=18, s=5), e("P", x=40, y=34, s=5), e("A", x=50, y=50, s=5), e("R", x=60, y=66, s=5), e("T", x=70, y=82, s=5))
d(["Long overdue"], "Phrase", "medium", e("OVERDUUUUUUE", s=3))
# missing, broken, reversed or crossed out
d(["Broken home"], "Phrase", "easy", e("HO     ME", s=6))
d(["Paradise lost", "Paradise Lost"], "Books and literature", "medium", e("PARADI_E", s=5))
d(["Cross-section", "Cross section"], "Phrase", "medium", e("SECTION", s=5), e("X", s=6, color=RED))
d(["Backtrack"], "Word", "medium", e("KCART", s=6))
# something inside something
d(["Head in the sand"], "Phrase", "medium", e("SAheadND", s=5))
d(["Fly in the ointment"], "Phrase", "medium", e("OINTflyMENT", s=4))
d(["Once in a while"], "Phrase", "medium", e("WHonceILE", s=5))
d(["Little by little"], "Phrase", "medium", e("little", x=32, s=1), e("by", s=2), e("little", x=68, s=1))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'dingbat-5.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'dingbats written')
