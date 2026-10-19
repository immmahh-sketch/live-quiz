# Bank session 19 Oct 2026: 2 Categorise questions -> bank/sort-79.json. Each pair of categories was probed against every
# Categorise question in the live bank first (no Professionals v Sweeney character sort; no English v Scottish island sort).
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("Television", ["The Professionals", "The Sweeney", "ITV"], "medium", "A character from The Professionals or from The Sweeney?", "The Professionals", "The Sweeney",
  ["Bodie", "Doyle", "Cowley"], ["Regan", "Carter", "Haskins"])
s("Geography", ["islands", "England", "Scotland"], "medium", "An English island or a Scottish island?", "English", "Scottish",
  ["Lindisfarne", "Lundy", "St Michael's Mount", "Hayling Island"], ["Iona", "Islay", "Bute", "Eigg"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-79.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
