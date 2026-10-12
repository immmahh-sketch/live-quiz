# Bank session 12 Oct 2026: 3 more Match questions -> bank/match-21.json (North East dishes, spices by plant part, dances by country).
# Each title checked against every match question in the live bank. Import with: node tools/import-bank.mjs match
import json, os
OUT = []
def m(cat, tags, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff, "category": cat, "tags": tags})

m("Food and drink", ["North East", "food"], "medium", "Match each North East dish to what it is",
  ("Parmo", "Breaded chicken under white sauce and cheese"), ("Stottie", "A flat, round loaf of bread"),
  ("Pease pudding", "A spread made from split peas"), ("Panackelty", "A meat and potato bake"))
m("Food and drink", ["spices", "plants"], "hard", "Match each spice to the part of the plant it comes from",
  ("Cinnamon", "Bark"), ("Cloves", "Flower buds"), ("Ginger", "Root"), ("Nutmeg", "Seed"))
m("Music", ["dance", "countries"], "medium", "Match each dance to the country it comes from",
  ("Tango", "Argentina"), ("Flamenco", "Spain"), ("Samba", "Brazil"), ("Polka", "Czech Republic"))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'match-21.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'match questions written')
