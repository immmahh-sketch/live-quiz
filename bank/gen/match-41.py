# Bank session 19 Oct 2026: 2 Match questions -> bank/match-41.json (sitcom pubs and clubs, sitcom characters' vehicles).
# Each topic probed against every match question in the live bank first (soap pubs and famous TV cars like KITT were
# already there, so these use British sitcoms). Import with: node tools/import-bank.mjs match
import json, os
OUT = []
def m(cat, tags, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff, "category": cat, "tags": tags})

m("Comedy", ["sitcoms", "pubs"], "medium", "Match each sitcom to its local pub or club",
  ("Only Fools and Horses", "The Nag's Head"), ("Phoenix Nights", "The Phoenix Club"), ("Early Doors", "The Grapes"), ("Still Game", "The Clansman"))
m("Comedy", ["sitcoms", "cars"], "easy", "Match each sitcom character to how they get about",
  ("Del Boy", "Yellow Reliant three-wheeler"), ("Mr Bean", "Mini"), ("Simon Cooper", "Yellow Fiat Cinquecento"), ("Albert Steptoe", "Horse and cart"))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'match-41.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'match questions written')
