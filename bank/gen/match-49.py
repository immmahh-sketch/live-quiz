# Bank session 19 Oct 2026: 2 Match questions -> bank/match-49.json (more sitcom families, northern comedians' home towns). Each
# topic probed against every match question in the live bank first (Trotters / Royles / Boswells / Goods was there, so these
# use other families). Import with: node tools/import-bank.mjs match
import json, os
OUT = []
def m(cat, tags, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff, "category": cat, "tags": tags})

m("Comedy", ["sitcoms", "families"], "medium", "Which comedy does each of these TV families live in?",
  ("The Goodmans", "Friday Night Dinner"), ("The Brockmans", "Outnumbered"), ("The Harpers", "My Family"), ("The Garveys", "Benidorm"))
m("Comedy", ["comedians", "the North"], "medium", "Match each comedian to their home town",
  ("Peter Kay", "Bolton"), ("Sarah Millican", "South Shields"), ("Johnny Vegas", "St Helens"), ("Jason Manford", "Salford"))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'match-49.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'match questions written')
