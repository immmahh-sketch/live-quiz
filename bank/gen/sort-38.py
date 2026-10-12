# Bank session 12 Oct 2026: 2 more Categorise questions -> bank/sort-38.json. Two groups, three or four items each. Each pair of
# categories was checked against every Categorise question already in the live bank.
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("Games and toys", ["Monopoly", "board games"], "medium", "On the UK Monopoly board or the American one?", "UK", "American",
  ["Mayfair", "Old Kent Road", "Pall Mall", "Leicester Square"], ["Boardwalk", "Park Place", "Marvin Gardens", "Baltic Avenue"])
s("History", ["Romans", "Hadrian's Wall", "roads"], "medium", "A Roman fort or a Roman road?", "Fort", "Road",
  ["Housesteads", "Chesters", "Birdoswald", "Segedunum"], ["Dere Street", "Ermine Street", "Watling Street", "Fosse Way"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-38.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
