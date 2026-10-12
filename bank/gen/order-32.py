# Bank session 12 Oct 2026: 2 more Put in order questions -> bank/order-32.json (fictional dogs by debut, great liners by launch).
# Each theme was checked against every order question title and
# item list in the live bank (the server also skips any whose items match one already there).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

o("TV", ["dogs", "fictional animals"], "medium", "Put these fictional dogs in order of their first appearance, earliest first",
  ["Toto", "Pluto", "Lassie", "Snoopy", "Scooby-Doo", "Gromit", "Brian Griffin"], "earliest first")
o("History", ["ships", "ocean liners", "shipbuilding"], "hard", "Put these great liners in order of launch, earliest first",
  ["Great Eastern", "Mauretania", "Queen Mary", "Canberra", "Queen Elizabeth 2"], "earliest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-32.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
