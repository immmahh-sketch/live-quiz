# Bank session 19 Oct 2026: 2 Categorise questions -> bank/sort-67.json. Two groups, four items each. Each pair of categories
# was probed against every Categorise question in the live bank first (none of these pairs were there).
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

# Penelope Keith is in both
s("Comedy", ["To the Manor Born", "The Good Life", "Penelope Keith"], "medium", "From To the Manor Born or from The Good Life?", "To the Manor Born", "The Good Life",
  ["Audrey", "Brabinger", "Grantleigh", "Richard DeVere"], ["Tom", "Barbara", "Margo", "Jerry"])
# both written by Carla Lane
s("Comedy", ["Butterflies", "Bread", "Carla Lane"], "medium", "From Butterflies or from Bread?", "Butterflies", "Bread",
  ["Ria", "Ben the dentist", "Leonard", "Russell"], ["Nellie", "Joey", "Aveline", "Freddie"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-67.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
