# Bank session 19 Oct 2026: 2 Put in order questions -> bank/order-68.json (British islands by size, birds by clutch size).
# Probed against every order question in the live bank first (Scottish islands only north to south; Canary Islands by size; no
# clutch-size order). Police ranks and pregnancy lengths were drafted and dropped: both already in.
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

# about 2,180, 1,660, 875, 715 and 380 square km
o("Geography", ["islands", "UK", "size"], "medium", "Put these British islands in order of size, largest first",
  ["Lewis and Harris", "Skye", "Mull", "Anglesey", "Isle of Wight"], "largest first")
# usual clutch: 1, 2, 5, 9, 15
o("Nature", ["birds", "eggs", "British wildlife"], "medium", "Put these British birds in order of how many eggs they usually lay at a time, fewest first",
  ["Gannet", "Swift", "Robin", "Blue tit", "Grey partridge"], "fewest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-68.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
