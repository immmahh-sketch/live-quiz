# Bank session 13 Oct 2026: 2 more Categorise questions -> bank/sort-44.json. Two groups, three or four items each. Each pair of
# categories was checked against every Categorise question already in the live bank.
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("Books", ["The Jungle Book", "Watership Down", "animal stories"], "easy", "A character from 'The Jungle Book' or from 'Watership Down'?", "The Jungle Book", "Watership Down",
  ["Baloo", "Bagheera", "Shere Khan", "Kaa"], ["Hazel", "Fiver", "Bigwig", "General Woundwort"])
s("UK geography", ["lighthouses", "England", "Scotland"], "hard", "A lighthouse in England or in Scotland?", "England", "Scotland",
  ["Eddystone", "Souter", "Longstone", "Beachy Head"], ["Bell Rock", "Skerryvore", "Muckle Flugga", "Ardnamurchan"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-44.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
