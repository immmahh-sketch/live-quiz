# Bank session 19 Oct 2026: 2 Match questions -> bank/match-48.json (British butterflies to their look, sitcom writing duos to a
# show they wrote). Each topic probed against every match question in the live bank first (none of these pairs were there).
# Import with: node tools/import-bank.mjs match
import json, os
OUT = []
def m(cat, tags, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff, "category": cat, "tags": tags})

m("Nature", ["butterflies", "British wildlife"], "medium", "Match each British butterfly to what it looks like",
  ("Red admiral", "Black wings with red bands"), ("Peacock", "Big eyespots on its wings"), ("Brimstone", "Sulphur-yellow wings"), ("Small tortoiseshell", "Orange with black and yellow patches"))
m("Comedy", ["sitcoms", "writers"], "medium", "Match each writing duo to a sitcom they wrote",
  ("Marks and Gran", "Birds of a Feather"), ("Galton and Simpson", "Steptoe and Son"), ("Clement and La Frenais", "Auf Wiedersehen, Pet"), ("Croft and Perry", "Dad's Army"))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'match-48.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'match questions written')
