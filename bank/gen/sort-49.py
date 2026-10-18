# Bank session 18 Oct 2026: 3 Categorise questions -> bank/sort-49.json. Two groups, three or four items each. Each pair of
# categories was probed against every Categorise question in the live bank first ('Auf Wiedersehen, Pet' or 'Only Fools and
# Horses' exists, but not against The Likely Lads).
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("British sitcoms", ["The Likely Lads", "Auf Wiedersehen Pet", "North East"], "medium", "A character from The Likely Lads or from Auf Wiedersehen, Pet?", "The Likely Lads", "Auf Wiedersehen, Pet",
  ["Bob", "Terry", "Thelma"], ["Oz", "Neville", "Barry", "Bomber"])
s("Crime dramas", ["Vera", "Line of Duty", "detectives"], "medium", "A character from Vera or from Line of Duty?", "Vera", "Line of Duty",
  ["Joe Ashworth", "Aiden Healy", "Kenny Lockhart", "Malcolm Donahue"], ["Ted Hastings", "Steve Arnott", "Kate Fleming", "Dot Cottan"])
s("Everyday life", ["batteries", "paper sizes"], "easy", "A battery size or a paper size?", "Battery", "Paper",
  ["AAA", "AA", "C", "D"], ["A4", "A3", "A5", "A2"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-49.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
