# Bank session 19 Oct 2026: 2 Match questions -> bank/match-42.json (British animals' homes, sitcom spin-offs and sequels).
# Each topic probed against every match question in the live bank first (no animal homes or spin-off pairs were there).
# Import with: node tools/import-bank.mjs match
import json, os
OUT = []
def m(cat, tags, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff, "category": cat, "tags": tags})

m("Nature", ["British wildlife", "homes"], "medium", "Match each animal to the name of its home",
  ("Badger", "Sett"), ("Otter", "Holt"), ("Squirrel", "Drey"), ("Rabbit", "Warren"))
m("Comedy", ["sitcoms", "spin-offs"], "medium", "Match each spin-off or sequel to the show it came from",
  ("Grace & Favour", "Are You Being Served?"), ("Max and Paddy's Road to Nowhere", "Phoenix Nights"), ("In the Loop", "The Thick of It"), ("Still Open All Hours", "Open All Hours"))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'match-42.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'match questions written')
