# Bank session 19 Oct 2026: 2 Put in order questions -> bank/order-70.json (Martin Clunes's shows, English islands by size).
# Probed against every order question in the live bank first (nothing on Clunes; the British islands order uses Lewis and Harris,
# Skye, Mull, Anglesey and the Isle of Wight, so only the Isle of Wight is shared).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

# 1983, 1992, 2004, 2019
o("Television", ["Martin Clunes", "sitcoms", "TV drama"], "medium", "Put these Martin Clunes shows in order of first broadcast, earliest first",
  ["No Place Like Home", "Men Behaving Badly", "Doc Martin", "Manhunt"], "earliest first")
# about 380, 94, 30, 18 and 2 square km
o("Geography", ["islands", "England", "size"], "hard", "Put these English islands in order of size, largest first",
  ["Isle of Wight", "Isle of Sheppey", "Hayling Island", "Canvey Island", "Brownsea Island"], "largest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-70.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
