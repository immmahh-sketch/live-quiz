# Bank session 19 Oct 2026: 2 Categorise questions -> bank/sort-63.json. Two groups, four items each. Each pair of categories
# was probed against every Categorise question in the live bank first (none of these pairs were there).
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("Comedy", ["Birds of a Feather", "Goodnight Sweetheart", "Marks and Gran"], "easy", "From Birds of a Feather or from Goodnight Sweetheart?", "Birds of a Feather", "Goodnight Sweetheart",
  ["Sharon", "Tracey", "Dorien", "Chigwell"], ["Gary Sparrow", "Phoebe", "Ducketts Passage", "Yvonne"])
# none of the moths has 'moth' in its everyday name
s("Nature", ["butterflies", "moths", "British wildlife"], "hard", "A British butterfly or a British moth?", "Butterfly", "Moth",
  ["Red admiral", "Peacock", "Painted lady", "Small tortoiseshell"], ["Cinnabar", "Six-spot burnet", "Garden tiger", "Puss"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-63.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
