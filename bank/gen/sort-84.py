# Bank session 19 Oct 2026: 2 Categorise questions -> bank/sort-84.json. Each pair of categories was probed against every
# Categorise question in the live bank first (Sherlock characters are already used in three sorts, so this one is about the actors
# who played Holmes and Watson; no Happy Valley character sort).
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("Film", ["Sherlock Holmes", "actors"], "hard", "Played Sherlock Holmes or played Dr Watson?", "Holmes", "Watson",
  ["Basil Rathbone", "Jeremy Brett", "Robert Downey Jr", "Benedict Cumberbatch"], ["Nigel Bruce", "Edward Hardwicke", "Jude Law", "Martin Freeman"])
s("Television", ["Happy Valley", "Line of Duty", "BBC"], "medium", "A character from Happy Valley or from Line of Duty?", "Happy Valley", "Line of Duty",
  ["Catherine Cawood", "Tommy Lee Royce", "Clare Cartwright", "Ryan Cawood"], ["Ted Hastings", "Steve Arnott", "Kate Fleming", "Lindsay Denton"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-84.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
