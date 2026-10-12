# Bank session 12 Oct 2026: 2 more Put in order questions -> bank/order-35.json (Top Gear presenters, Nissan Sunderland models).
# Each theme was checked against every order question title and
# item list in the live bank (the server also skips any whose items match one already there).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

o("TV", ["Top Gear", "presenters"], "hard", "Put these Top Gear presenters in order of their first series, earliest first",
  ["Angela Rippon", "Noel Edmonds", "Jeremy Clarkson", "Richard Hammond", "Chris Evans", "Freddie Flintoff"], "earliest first")
o("The North East of England", ["Nissan", "Sunderland", "cars"], "hard", "Put these Nissan models in the order Sunderland started building them, earliest first",
  ["Bluebird", "Primera", "Micra", "Qashqai", "Juke", "Leaf"], "earliest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-35.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
