# Bank session 12 Oct 2026: 2 more Put in order questions -> bank/order-33.json (Anglo-Saxon kings, North East saints by death).
# Each theme was checked against every order question title and
# item list in the live bank (the server also skips any whose items match one already there).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

o("History", ["Anglo-Saxons", "kings"], "hard", "Put these Anglo-Saxon kings in order of their reigns, earliest first",
  ["Alfred the Great", "Athelstan", "Edgar the Peaceful", "Æthelred the Unready", "Edward the Confessor", "Harold Godwinson"], "earliest first")
o("History", ["saints", "Northumbria", "North East"], "hard", "Put these North East saints in order of when they died, earliest first",
  ["St Aidan", "St Hilda", "St Cuthbert", "St Wilfrid", "St Bede", "St Godric"], "earliest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-33.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
