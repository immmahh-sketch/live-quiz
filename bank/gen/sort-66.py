# Bank session 19 Oct 2026: 2 Categorise questions -> bank/sort-66.json. Two groups, four items each. Each pair of categories
# was probed against every Categorise question in the live bank first (none of these pairs were there).
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("Comedy", ["Car Share", "Mrs Brown's Boys", "sitcoms"], "easy", "From Car Share or from Mrs Brown's Boys?", "Car Share", "Mrs Brown's Boys",
  ["Kayleigh", "John Redmond", "ForeverFresh", "Forever FM"], ["Agnes", "Winnie", "Buster", "Grandad"])
s("Nature", ["birds", "British wildlife", "food"], "medium", "A British bird that mostly eats fish, or one that mostly eats seeds?", "Fish", "Seeds",
  ["Kingfisher", "Grey heron", "Cormorant", "Osprey"], ["Goldfinch", "Chaffinch", "Bullfinch", "Greenfinch"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-66.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
