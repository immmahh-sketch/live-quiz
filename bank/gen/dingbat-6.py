# Bank session 9 Oct 2026 (fourth pass): more dingbats -> bank/dingbat-6.json, a few for Christmas. None of these answers is live.
# Elements: t text, x/y 0–100 (centre), s size 1–6, optional rot, flip "h"/"v", style strike/underline/box/outline, color #hex.
import json, os
B = []
def d(answers, cat, diff, *els, tags=()):
    B.append({"answers": answers, "elements": [dict(e) for e in els], "category": cat, "tags": list(tags), "difficulty": diff})
def e(t, x=50, y=50, s=5, **k): return {"t": t, "x": x, "y": y, "s": s, **k}
RED, GREEN, BLUE, ICE, GREY, PURPLE, GOLD, SILVER = "#d42020", "#1f9a3a", "#1f5fd4", "#7fc8f0", "#8a8f94", "#7b2fbe", "#c9a227", "#9aa0a6"

# Christmas
d(["Blue Christmas"], "Christmas", "medium", e("CHRISTMAS", s=4, color=BLUE), tags=["Elvis"])
d(["We Three Kings", "Three kings"], "Christmas", "easy", e("KING", y=24, s=4), e("KING", y=50, s=4), e("KING", y=76, s=4), tags=["carols"])
d(["Snowdrop"], "Nature", "medium", e("SNOW", y=90, s=4))
d(["Santa's little helper"], "Christmas", "medium", e("SANTA'S", y=40, s=5), e("helper", y=72, s=1))
d(["Ice Ice Baby"], "Music", "medium", e("ICE  ICE", y=40, s=5, color=ICE), e("baby", y=72, s=2), tags=["Vanilla Ice"])
# colour
d(["Ice cold"], "Phrase", "easy", e("COLD", s=6, color=ICE))
d(["Green fingers"], "Phrase", "easy", e("FINGERS", s=5, color=GREEN))
d(["Red alert"], "Phrase", "easy", e("ALERT", s=6, color=RED))
d(["Grey matter"], "Phrase", "medium", e("MATTER", s=5, color=GREY))
d(["Purple patch"], "Phrase", "medium", e("PATCH", s=6, color=PURPLE))
d(["Red-handed", "Caught red-handed"], "Phrase", "medium", e("HANDED", s=5, color=RED))
d(["Golden Boot"], "Football", "medium", e("BOOT", s=6, color=GOLD))
d(["Silver screen"], "Film", "medium", e("SCREEN", s=5, color=SILVER))
# repeats, reversals and layout
d(["Backwards and forwards"], "Phrase", "medium", e("SDRAWKCAB", y=36, s=4), e("FORWARDS", y=66, s=4))
d(["Two-timing", "Two timing"], "Phrase", "medium", e("TIMING", y=36, s=4), e("TIMING", y=66, s=4))
d(["Double-decker", "Double decker"], "Phrase", "easy", e("DECKER", y=36, s=4), e("DECKER", y=66, s=4))
d(["Cut short"], "Phrase", "medium", e("SHOR", s=6))
d(["Raining cats and dogs"], "Phrase", "easy", e("CATS", x=20, y=15, s=3), e("DOGS", x=48, y=34, s=3), e("CATS", x=76, y=18, s=3),
  e("DOGS", x=28, y=64, s=3), e("CATS", x=60, y=82, s=3), e("DOGS", x=82, y=56, s=3))
d(["On cloud nine", "Cloud nine"], "Phrase", "medium", e("9", y=28, s=4), e("CLOUD", y=62, s=5))
d(["A drop in the ocean", "Drop in the ocean"], "Phrase", "medium", e("OCEdropAN", s=5))
d(["Crack of dawn"], "Phrase", "medium", e("DA", x=34, y=44, s=6, rot=-10), e("WN", x=68, y=58, s=6, rot=10))
d(["Inside job"], "Phrase", "medium", e("JinsideOB", s=5))
d(["Back to square one", "Square one"], "Phrase", "easy", e("1", s=6, style="box"))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'dingbat-6.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'dingbats written')
