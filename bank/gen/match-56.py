# Bank session 19 Oct 2026: 2 Match questions -> bank/match-56.json (panel shows to team captains, birds to their nests).
# Each topic probed against every match question in the live bank first (the comedians-to-panel-shows match uses Lee Mack,
# Hugh Dennis, Ian Hislop and Alan Davies, so none of those are here; nothing on nests). Import with: node tools/import-bank.mjs match
import json, os
OUT = []
def m(cat, tags, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff, "category": cat, "tags": tags})

m("Television", ["panel shows", "team captains"], "medium", "Match each panel show to one of its long-serving team captains",
  ("Never Mind the Buzzcocks", "Phill Jupitus"), ("8 Out of 10 Cats", "Sean Lock"), ("A Question of Sport", "Matt Dawson"), ("They Think It's All Over", "David Gower"))
m("Nature", ["birds", "nests", "British wildlife"], "medium", "Match each British bird to where it nests",
  ("Puffin", "A burrow in a clifftop"), ("House martin", "A mud cup under the eaves"), ("Great spotted woodpecker", "A hole it drills in a tree"), ("Reed warbler", "Woven between reed stems"))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'match-56.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'match questions written')
