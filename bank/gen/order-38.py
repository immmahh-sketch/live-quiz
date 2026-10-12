# Bank session 13 Oct 2026: 2 more Put in order questions -> bank/order-38.json (east coast lighthouses, Jungle Book films).
# Each theme was checked against every order question title and
# item list in the live bank (the server also skips any whose items match one already there).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

o("The North East of England", ["lighthouses", "coast", "North East"], "hard", "Put these east coast lighthouses in order from north to south",
  ["Longstone", "Coquet", "St Mary's", "Souter", "Flamborough Head", "Spurn"], "northernmost first")
o("Film", ["The Jungle Book", "Disney", "films"], "medium", "Put these Jungle Book films in order of release, earliest first",
  ["Disney's cartoon", "Disney's live-action film with Jason Scott Lee", "The Jungle Book 2", "Jon Favreau's remake", "Mowgli: Legend of the Jungle"], "earliest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-38.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
