# Bank session 19 Oct 2026: 2 Match questions -> bank/match-73.json (Spooks cast, Killing Eve cast). Each topic probed against every
# match question in the live bank first (nothing on either show). Import with: node tools/import-bank.mjs match
import json, os
OUT = []
def m(cat, tags, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff, "category": cat, "tags": tags})

m("Television", ["Spooks", "actors", "BBC"], "medium", "Match each Spooks actor to their character",
  ("Peter Firth", "Harry Pearce"), ("Matthew Macfadyen", "Tom Quinn"), ("Nicola Walker", "Ruth Evershed"), ("Richard Armitage", "Lucas North"))
m("Television", ["Killing Eve", "actors", "BBC"], "medium", "Match each Killing Eve actor to their character",
  ("Sandra Oh", "Eve Polastri"), ("Jodie Comer", "Villanelle"), ("Fiona Shaw", "Carolyn Martens"), ("Kim Bodnia", "Konstantin"))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'match-73.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'match questions written')
