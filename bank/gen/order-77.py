# Bank session 19 Oct 2026: 2 Put in order questions -> bank/order-77.json (John Simm's roles, Phoebe Waller-Bridge's projects).
# Probed against every order question in the live bank first (only Simm as the Master and Waller-Bridge nowhere).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

# 2003, 2006, 2007, 2011
o("Television", ["John Simm", "actors"], "hard", "Put these John Simm roles in the order he first played them, earliest first",
  ["State of Play", "Life on Mars", "The Master in Doctor Who", "Mad Dogs"], "earliest first")
# 2016, 2018, 2021, 2023
o("Film", ["Phoebe Waller-Bridge", "writers"], "medium", "Put these Phoebe Waller-Bridge projects in order of first release, earliest first",
  ["Fleabag", "Solo: A Star Wars Story", "No Time to Die", "Indiana Jones and the Dial of Destiny"], "earliest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-77.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
