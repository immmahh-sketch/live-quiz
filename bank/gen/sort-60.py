# Bank session 19 Oct 2026: 2 Categorise questions -> bank/sort-60.json. Two groups, four items each. Each pair of categories
# was probed against every Categorise question in the live bank first (Young Ones v Dad's Army exists, but not these pairs).
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

# Rik Mayall plays Rick in one and Richie in the other
s("Comedy", ["Bottom", "The Young Ones", "Rik Mayall"], "medium", "A Bottom character or a Young Ones character?", "Bottom", "The Young Ones",
  ["Richie", "Eddie", "Spudgun", "Dave Hedgehog"], ["Rick", "Vyvyan", "Neil", "Mike"])
# the slow worm is a legless lizard
s("Nature", ["amphibians", "reptiles", "British wildlife"], "medium", "An amphibian or a reptile?", "Amphibian", "Reptile",
  ["Frog", "Toad", "Newt", "Salamander"], ["Slow worm", "Adder", "Gecko", "Tortoise"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-60.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
