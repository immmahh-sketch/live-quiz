# Bank session 12 Oct 2026: 2 more Match questions -> bank/match-25.json (friars by robe colour, Cold War words).
# Each title checked against every match question in the live bank. Import with: node tools/import-bank.mjs match
import json, os
OUT = []
def m(cat, tags, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff, "category": cat, "tags": tags})

m("History", ["friars", "monks", "religion"], "hard", "Match each order of friars to the name their robes gave them",
  ("Franciscans", "Greyfriars"), ("Dominicans", "Blackfriars"), ("Carmelites", "Whitefriars"), ("Augustinians", "Austin Friars"))
m("History", ["Cold War", "words"], "medium", "Match each Cold War word to what it meant",
  ("Glasnost", "Openness"), ("Perestroika", "Restructuring"), ("Détente", "Easing of tension"), ("Brinkmanship", "Pushing right to the edge of war"))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'match-25.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'match questions written')
