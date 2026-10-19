# Bank session 19 Oct 2026: 2 Categorise questions -> bank/sort-80.json. Each pair of categories was probed against every
# Categorise question in the live bank first (no Brookside or Casualty sorts; a hospital-or-police-station sort exists with American
# shows, so this one is British).
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("Television", ["Brookside", "Casualty", "TV drama"], "medium", "A character from Brookside or from Casualty?", "Brookside", "Casualty",
  ["Trevor Jordache", "Jimmy Corkhill", "Barry Grant", "Sheila Grant"], ["Charlie Fairhead", "Duffy", "Connie Beauchamp", "Josh Griffiths"])
s("Television", ["medical dramas", "police", "TV drama"], "easy", "A British medical drama or a British police drama?", "Medical", "Police",
  ["Casualty", "Holby City", "Angels", "Peak Practice"], ["The Bill", "Z-Cars", "Juliet Bravo", "Heartbeat"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-80.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
