# Bank session 12 Oct 2026: 2 more Categorise questions -> bank/sort-41.json. Two groups, three or four items each. Each pair of
# categories was checked against every Categorise question already in the live bank.
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("TV", ["TV chefs", "gardening", "presenters"], "easy", "A TV chef or a TV gardener?", "Chef", "Gardener",
  ["Jamie Oliver", "Gordon Ramsay", "Nigella Lawson", "Rick Stein"], ["Monty Don", "Alan Titchmarsh", "Charlie Dimmock", "Carol Klein"])
s("TV", ["Top Gear", "Countryfile", "presenters"], "medium", "Presented 'Top Gear' or presented 'Countryfile'?", "Top Gear", "Countryfile",
  ["Jeremy Clarkson", "Richard Hammond", "James May", "Freddie Flintoff"], ["Matt Baker", "Ellie Harrison", "John Craven", "Adam Henson"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-41.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
