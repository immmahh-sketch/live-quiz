# Bank session 19 Oct 2026: 2 Match questions -> bank/match-43.json (sitcoms to their home towns, Scottish comedians to their
# shows). Each topic probed against every match question in the live bank first (Black Books / Phoenix Nights stars and
# local pubs were there, so these ask about the towns instead). Import with: node tools/import-bank.mjs match
import json, os
OUT = []
def m(cat, tags, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff, "category": cat, "tags": tags})

m("Comedy", ["sitcoms", "places"], "medium", "Match each sitcom to the city or town it's set in",
  ("Still Game", "Glasgow"), ("Dinnerladies", "Manchester"), ("Phoenix Nights", "Bolton"), ("Black Books", "London"))
m("Comedy", ["Scotland", "comedians"], "medium", "Match each Scottish comedian to the show they're best known for",
  ("Gregor Fisher", "Rab C. Nesbitt"), ("Limmy", "Limmy's Show"), ("Ford Kiernan", "Still Game"), ("Frankie Boyle", "Mock the Week"))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'match-43.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'match questions written')
