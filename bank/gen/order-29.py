# Bank session 12 Oct 2026: 3 more Put in order questions -> bank/order-29.json (Sunderland's grounds, Cheryl singles, the A1 heading
# north). Each theme was checked against every order question title and
# item list in the live bank (the server also skips any whose items match one already there).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

o("Football", ["Sunderland", "football grounds", "North East"], "hard", "Put Sunderland's home grounds in the order they used them, earliest first",
  ["Blue House Field", "Abbs Field", "Newcastle Road", "Roker Park", "Stadium of Light"], "earliest first")
o("Music", ["Cheryl", "Girls Aloud", "North East"], "medium", "Put these Cheryl solo singles in order of release, earliest first",
  ["Fight for This Love", "Parachute", "Promise This", "Call My Name", "Crazy Stupid Love"], "earliest first")
o("UK geography", ["A1", "roads", "North East"], "medium", "Put these towns in the order you pass them heading north up the A1",
  ["Stevenage", "Stamford", "Newark-on-Trent", "Wetherby", "Morpeth", "Alnwick", "Berwick-upon-Tweed"], "southernmost first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-29.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
