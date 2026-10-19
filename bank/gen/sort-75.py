# Bank session 19 Oct 2026: 2 Categorise questions -> bank/sort-75.json. Each pair of categories was probed against every
# Categorise question in the live bank first (no Minder sort; Taggart only as a detective in a Scotland/England sort; a
# butterfly-or-moth sort exists, so the butterflies here are different ones set against beetles).
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("Television", ["Minder", "Taggart", "ITV"], "medium", "A character from Minder or from Taggart?", "Minder", "Taggart",
  ["Arthur Daley", "Terry McCann", "Ray Daley", "DS Chisholm"], ["Mike Jardine", "Jackie Reid", "Matt Burke", "Robbie Ross"])
# the glow-worm, the cardinal and the devil's coach horse are all beetles
s("Nature", ["insects", "beetles", "butterflies", "British wildlife"], "hard", "A British beetle or a British butterfly?", "Beetle", "Butterfly",
  ["Ladybird", "Devil's coach horse", "Cardinal", "Glow-worm"], ["Red admiral", "Comma", "Brimstone", "Painted lady"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-75.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
