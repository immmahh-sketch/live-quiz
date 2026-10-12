# Bank session 12 Oct 2026: 2 more Put in order questions -> bank/order-30.json (Metro east to the coast, bridges up the Wear).
# Each theme was checked against every order question title and
# item list in the live bank (the server also skips any whose items match one already there).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

o("The North East of England", ["Metro", "Tyne and Wear", "transport"], "medium", "Put these Metro stations in order, heading east from Monument towards the coast",
  ["Manors", "Byker", "Wallsend", "Percy Main", "North Shields", "Tynemouth"], "first stop first")
o("The North East of England", ["River Wear", "bridges", "Sunderland"], "hard", "Put these bridges over the Wear in order, going upriver from the sea",
  ["Wearmouth Bridge", "Queen Alexandra Bridge", "Northern Spire", "The A19 bridge at Hylton", "Framwellgate Bridge in Durham"], "nearest the sea first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-30.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
