# Bank session 12 Oct 2026: 2 more Categorise questions -> bank/sort-39.json. Two groups, three or four items each. Each pair of
# categories was checked against every Categorise question already in the live bank.
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("Books", ["Brontë sisters", "Jane Austen", "characters"], "medium", "A Brontë character or a Jane Austen character?", "Brontë", "Jane Austen",
  ["Heathcliff", "Mr Rochester", "Cathy Earnshaw", "Bertha Mason"], ["Mr Knightley", "Fanny Price", "Marianne Dashwood", "Mr Wickham"])
s("The North East of England", ["Newcastle", "Sunderland", "streets"], "medium", "A street in Newcastle or in Sunderland?", "Newcastle", "Sunderland",
  ["Grey Street", "Grainger Street", "Northumberland Street", "Collingwood Street"], ["Fawcett Street", "Holmeside", "Vine Place", "Hylton Road"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-39.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
