# Bank session 12 Oct 2026: 2 more Categorise questions -> bank/sort-40.json. Two groups, three or four items each. Each pair of
# categories was checked against every Categorise question already in the live bank.
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("History", ["Anglo-Saxons", "Normans", "kings"], "medium", "An Anglo-Saxon king or a Norman king?", "Anglo-Saxon", "Norman",
  ["Alfred the Great", "Athelstan", "Edgar the Peaceful", "Æthelred the Unready"], ["William the Conqueror", "William Rufus", "Henry I", "Stephen"])
s("Food and drink", ["bread", "Britain", "France"], "medium", "A British bread or a French bread?", "British", "French",
  ["Stottie", "Bloomer", "Farl", "Bannock"], ["Baguette", "Brioche", "Fougasse", "Pain de campagne"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-40.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
