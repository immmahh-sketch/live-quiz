# Bank session 19 Oct 2026: 2 Put in order questions -> bank/order-76.json (James Corden's projects, Ruth Jones's projects).
# Probed against every order question in the live bank first (nothing on Corden or Jones's careers).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

# 2007, 2013, 2015, 2019
o("Television", ["James Corden", "actors"], "medium", "Put these James Corden projects in order of first release, earliest first",
  ["Gavin & Stacey", "The Wrong Mans", "The Late Late Show", "Cats (the film)"], "earliest first")
# 2007, 2012, 2015, 2024
o("Television", ["Ruth Jones", "writers"], "hard", "Put these Ruth Jones projects in order of first release, earliest first",
  ["Gavin & Stacey", "Stella", "Never Greener (her novel)", "Gavin & Stacey: The Finale"], "earliest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-76.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
