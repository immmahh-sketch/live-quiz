# Bank session 9 Oct 2026 (second pass): 30 new dingbats -> bank/dingbat-4.json. None of these answers is live yet.
# Leans on the colour option (e.g. "DAY" in green = Green Day), which the bank has barely used.
# Elements: t text, x/y 0–100 (centre), s size 1–6, optional rot, flip "h"/"v", style strike/underline/box/outline, color #hex.
import json, os
B = []
def d(answers, cat, diff, *els, tags=()):
    B.append({"answers": answers, "elements": [dict(e) for e in els], "category": cat, "tags": list(tags), "difficulty": diff})
def e(t, x=50, y=50, s=5, **k): return {"t": t, "x": x, "y": y, "s": s, **k}
RED, GREEN, BLUE, PINK, SILVER = "#d42020", "#1f9a3a", "#1f5fd4", "#ff5fa8", "#9aa0a6"

d(["Mixed messages"], "Phrase", "easy", e("SGEMSESA", s=5))
d(["Split personality"], "Phrase", "easy", e("PERSON     ALITY", s=4))
d(["Backward step", "A step backwards", "Step backwards"], "Phrase", "medium", e("PETS", s=6))
d(["Partly cloudy"], "Phrase", "medium", e("CLOU", s=6))
d(["Over the moon"], "Phrase", "medium", e("COW", y=26, s=4), e("MOON", y=72, s=5))
d(["Undercover agent", "Undercover"], "Phrase", "medium", e("COVER", y=30, s=5), e("AGENT", y=68, s=5))
d(["All over the place"], "Phrase", "medium", e("PLACE", s=5), e("ALL", x=16, y=16, s=2), e("ALL", x=84, y=16, s=2), e("ALL", x=16, y=84, s=2), e("ALL", x=84, y=84, s=2), e("ALL", x=50, y=12, s=2), e("ALL", x=50, y=88, s=2))
d(["Middle of the road"], "Phrase", "easy", e("ROmiddleAD", s=4))
d(["Turnover", "Turn over"], "Word", "medium", e("OVER", s=6, rot=180))
d(["Shortbread"], "Food", "easy", e("bread", s=1))
d(["Big top"], "Phrase", "easy", e("TOP", s=6))
d(["Downhill"], "Word", "easy", e("HILL", y=90, s=3))
d(["Lowlife"], "Word", "medium", e("life", y=92, s=2))
d(["Uptown Girl"], "Music", "medium", e("TOWN", y=10, s=4), e("GIRL", y=60, s=5), tags=["Billy Joel"])
d(["Highway to Hell"], "Music", "medium", e("WAY", y=10, s=4), e("TO HELL", y=78, s=4), tags=["AC/DC"])
d(["Three Little Pigs", "The Three Little Pigs"], "Phrase", "easy", e("pigs   pigs   pigs", s=1))
d(["Split ends"], "Phrase", "easy", e("EN      DS", s=6))
d(["Box office"], "Phrase", "medium", e("OFFICE", s=5, style="box"))
d(["Inbox"], "Word", "medium", e("IN", s=6, style="box"))
d(["Outline"], "Word", "medium", e("LINE", s=6, style="outline"))
d(["Red Red Wine"], "Music", "medium", e("RED", y=34, s=5, color=RED), e("WINE", y=66, s=5, color=RED), tags=["UB40"])
d(["Green Day"], "Music", "easy", e("DAY", s=6, color=GREEN), tags=["bands"])
d(["Blue Moon"], "Music", "easy", e("MOON", s=6, color=BLUE))
d(["Pink Floyd"], "Music", "easy", e("FLOYD", s=6, color=PINK), tags=["bands"])
d(["Pink Panther", "The Pink Panther"], "Film", "easy", e("PANTHER", s=5, color=PINK))
d(["Bluetooth"], "Word", "easy", e("TOOTH", s=6, color=BLUE))
d(["Greenhouse"], "Word", "easy", e("HOUSE", s=6, color=GREEN))
d(["Redhead"], "Word", "easy", e("HEAD", s=6, color=RED))
d(["Silverstone"], "Sport", "medium", e("STONE", s=6, color=SILVER), tags=["Formula One"])
d(["Mixed doubles"], "Sport", "medium", e("BOLDUSE", s=5), tags=["tennis"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'dingbat-4.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'dingbats written')
