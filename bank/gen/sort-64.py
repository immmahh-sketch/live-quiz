# Bank session 19 Oct 2026: 2 Categorise questions -> bank/sort-64.json. Two groups, four items each. Each pair of categories
# was probed against every Categorise question in the live bank first (none of these pairs were there).
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("Comedy", ["Friday Night Dinner", "Bread", "sitcoms"], "easy", "From Friday Night Dinner or from Bread?", "Friday Night Dinner", "Bread",
  ["Martin", "Jackie", "Jim", "Wilson the dog"], ["Nellie", "Joey", "Aveline", "Lilo Lil"])
s("Food and drink", ["fruit", "gardening"], "medium", "Does this fruit grow on a tree or a bush?", "Tree", "Bush",
  ["Apple", "Pear", "Cherry", "Plum"], ["Blackcurrant", "Gooseberry", "Redcurrant", "Blueberry"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-64.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
