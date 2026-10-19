# Bank session 19 Oct 2026: 2 Categorise questions -> bank/sort-86.json. Each pair of categories was probed against every
# Categorise question in the live bank first (Bond sorts cover characters, cars, films and songs, not the actors; no Luther or
# Bodyguard character sort).
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("Film", ["James Bond", "actors"], "medium", "Played James Bond, or played a Bond villain?", "Bond", "Villain",
  ["Sean Connery", "Roger Moore", "Timothy Dalton", "Pierce Brosnan"], ["Christopher Lee", "Javier Bardem", "Christoph Waltz", "Rami Malek"])
s("Television", ["Luther", "Bodyguard", "BBC"], "medium", "A character from Luther or from Bodyguard?", "Luther", "Bodyguard",
  ["John Luther", "Alice Morgan", "Justin Ripley", "Zoe Luther"], ["David Budd", "Julia Montague", "Vicky Budd", "Anne Sampson"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-86.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
