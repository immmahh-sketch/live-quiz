# Bank session 19 Oct 2026: 2 Categorise questions -> bank/sort-71.json. Two groups, four items each. Each pair of categories
# was probed against every Categorise question in the live bank first (none of these pairs were there).
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("Television", ["music TV", "presenters"], "medium", "A presenter of The Tube or of Top of the Pops?", "The Tube", "Top of the Pops",
  ["Jools Holland", "Paula Yates", "Muriel Gray", "Leslie Ash"], ["Tony Blackburn", "Noel Edmonds", "Mike Read", "Bruno Brookes"])
# the wren, robin and blue tit stay all year; the swift, swallow, cuckoo and house martin fly to Africa
s("Nature", ["birds", "migration", "British wildlife"], "medium", "A British bird that stays all year, or one that leaves for Africa in autumn?", "Stays all year", "Leaves for Africa",
  ["Wren", "Robin", "Blue tit", "Blackbird"], ["Swift", "Swallow", "Cuckoo", "House martin"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-71.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
