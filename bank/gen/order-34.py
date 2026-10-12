# Bank session 12 Oct 2026: 2 more Put in order questions -> bank/order-34.json (pre-decimal coins by value, medieval kings).
# Each theme was checked against every order question title and
# item list in the live bank (the server also skips any whose items match one already there).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

o("History", ["coins", "money", "pre-decimal"], "medium", "Put these old British coins in order of value, lowest first",
  ["Farthing", "Halfpenny", "Threepenny bit", "Sixpence", "Shilling", "Florin", "Half crown"], "lowest first")
o("History", ["kings", "Normans", "Plantagenets"], "hard", "Put these medieval kings of England in order of their reigns, earliest first",
  ["William the Conqueror", "Henry I", "Stephen", "Henry II", "Richard the Lionheart", "Edward I", "Edward III"], "earliest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-34.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
