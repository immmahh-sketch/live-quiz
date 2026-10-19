# Bank session 19 Oct 2026: 2 Match questions -> bank/match-71.json (Gavin & Stacey cast, Cold Feet cast). Each topic probed against
# every match question in the live bank first (Gavin & Stacey has setting, surname and one-star matches, but no cast match; nothing on
# Cold Feet). Import with: node tools/import-bank.mjs match
import json, os
OUT = []
def m(cat, tags, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff, "category": cat, "tags": tags})

m("Television", ["Gavin & Stacey", "actors", "BBC"], "easy", "Match each Gavin & Stacey actor to their character",
  ("James Corden", "Smithy"), ("Ruth Jones", "Nessa"), ("Rob Brydon", "Uncle Bryn"), ("Alison Steadman", "Pam"))
m("Television", ["Cold Feet", "actors", "ITV"], "hard", "Match each Cold Feet actor to their character",
  ("James Nesbitt", "Adam"), ("Helen Baxendale", "Rachel"), ("John Thomson", "Pete"), ("Hermione Norris", "Karen"))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'match-71.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'match questions written')
