# Bank session 19 Oct 2026: 3 Put in order questions -> bank/order-59.json (Judi Dench's career, breakfast TV launches, Penelope
# Keith's career). Probed against every order question in the live bank first (only an 'actors who played M' order was close).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

# 1981, 1992, 1995, 1999
o("Television", ["Judi Dench", "career"], "medium", "Put these moments in Judi Dench's career in order, earliest first",
  ["A Fine Romance begins", "As Time Goes By begins", "First plays M in GoldenEye", "Wins an Oscar for Shakespeare in Love"], "earliest first")
# 1983, 1992, 1993, 2010, 2014
o("Television", ["breakfast TV"], "hard", "Put these breakfast TV shows in order of launch, earliest first",
  ["TV-am", "The Big Breakfast", "GMTV", "Daybreak", "Good Morning Britain"], "earliest first")
# 1975, 1979, 2014
o("Television", ["Penelope Keith", "career"], "medium", "Put these moments in Penelope Keith's career in order, earliest first",
  ["The Good Life begins", "To the Manor Born begins", "She becomes a dame"], "earliest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-59.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
