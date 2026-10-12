# Bank session 12 Oct 2026: 2 more Put in order questions -> bank/order-31.json (jazz styles by era, North East acts by first hit).
# Each theme was checked against every order question title and
# item list in the live bank (the server also skips any whose items match one already there).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

o("Music", ["jazz", "music history"], "hard", "Put these styles of jazz in the order they emerged, earliest first",
  ["Ragtime", "Dixieland", "Swing", "Bebop", "Cool jazz", "Jazz fusion"], "earliest first")
o("Music", ["North East", "bands"], "medium", "Put these North East acts in order of their first hit, earliest first",
  ["The Animals", "Lindisfarne", "Dire Straits", "Prefab Sprout", "Maxïmo Park", "Sam Fender"], "earliest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-31.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
