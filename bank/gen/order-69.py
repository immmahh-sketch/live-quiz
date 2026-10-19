# Bank session 19 Oct 2026: 2 Put in order questions -> bank/order-69.json (Phil Redmond's shows, British hospital dramas).
# Probed against every order question in the live bank first (Grange Hill only in a children's TV order; no hospital drama order).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

# 1978, 1982, 1995
o("Television", ["Phil Redmond", "soaps", "children's TV"], "medium", "Put these Phil Redmond creations in order of first broadcast, earliest first",
  ["Grange Hill", "Brookside", "Hollyoaks"], "earliest first")
# 1957, 1975, 1986, 1999, 2012
o("Television", ["hospital dramas", "TV drama"], "hard", "Put these British hospital dramas in order of first broadcast, earliest first",
  ["Emergency – Ward 10", "Angels", "Casualty", "Holby City", "Call the Midwife"], "earliest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-69.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
