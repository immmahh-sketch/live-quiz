# Bank session 12 Oct 2026: 3 more Match questions -> bank/match-22.json (Roman forts today, shipyards to rivers, Vera cast).
# Each title checked against every match question in the live bank. Import with: node tools/import-bank.mjs match
import json, os
OUT = []
def m(cat, tags, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff, "category": cat, "tags": tags})

m("History", ["Romans", "Hadrian's Wall", "North East"], "hard", "Match each Roman fort to the place where it stands today",
  ("Segedunum", "Wallsend"), ("Arbeia", "South Shields"), ("Pons Aelius", "Newcastle"), ("Coria", "Corbridge"))
m("History", ["shipbuilding", "rivers"], "medium", "Match each shipyard to the river it stood on",
  ("Swan Hunter", "Tyne"), ("Doxford", "Wear"), ("Cammell Laird", "Mersey"), ("John Brown & Company", "Clyde"))
m("TV", ["Vera", "actors", "North East"], "medium", "Match each actor to their role in 'Vera'",
  ("Brenda Blethyn", "Vera Stanhope"), ("David Leon", "Joe Ashworth"), ("Kenny Doughty", "Aiden Healy"), ("Jon Morrison", "Kenny Lockhart"))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'match-22.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'match questions written')
