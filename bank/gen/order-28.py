# Bank session 12 Oct 2026: 4 more Put in order questions -> bank/order-28.json (Metro green line, deserts by size,
# clubs by their last FA Cup win, Ant and Dec shows). Each theme was checked against every order question title and
# item list in the live bank (the server also skips any whose items match one already there).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

o("The North East of England", ["Metro", "Tyne and Wear", "transport"], "medium", "Put these Metro stations in order along the green line, heading south from the Airport",
  ["Regent Centre", "Haymarket", "Gateshead", "Stadium of Light", "Sunderland", "South Hylton"], "first stop first")
o("World geography", ["deserts", "geography"], "medium", "Put these deserts in order of size, largest first",
  ["Sahara", "Arabian", "Kalahari", "Thar", "Mojave"], "largest first")
o("Football", ["FA Cup", "football"], "hard", "Put these clubs in order of their most recent FA Cup win, earliest first",
  ["Newcastle United", "Sunderland", "Wimbledon", "Portsmouth", "Wigan Athletic", "Crystal Palace"], "earliest first")
o("TV", ["Ant and Dec", "TV presenters"], "medium", "Put these Ant and Dec shows in order of first broadcast, earliest first",
  ["Byker Grove", "SMTV Live", "Pop Idol", "I'm a Celebrity... Get Me Out of Here!", "Britain's Got Talent"], "earliest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-28.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
