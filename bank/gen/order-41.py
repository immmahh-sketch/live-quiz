# Bank session 18 Oct 2026: 2 Put in order questions -> bank/order-41.json (steam locomotives, aircraft by first flight).
# Probed against every order question title and item list in the live bank first (TV channels by launch was already there).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

# 1829, 1923, 1938, 1960 (the last steam engine British Railways built), 2008 (a brand-new A1)
o("History", ["steam", "railways", "locomotives"], "medium", "Put these steam locomotives in the order they were built, earliest first",
  ["Stephenson's Rocket", "Flying Scotsman", "Mallard", "Evening Star", "Tornado"], "earliest first")
# 1903, 1936, 1949, 1969, 2005
o("Science and technology", ["aircraft", "aviation", "first flights"], "medium", "Put these aircraft in order of their first flight, earliest first",
  ["Wright Flyer", "Spitfire", "de Havilland Comet", "Concorde", "Airbus A380"], "earliest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-41.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
