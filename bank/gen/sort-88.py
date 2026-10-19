# Bank session 19 Oct 2026: 2 Categorise questions -> bank/sort-88.json. Each pair of categories was probed against every
# Categorise question in the live bank first (no Life on Mars or Fleabag sorts).
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("Television", ["Life on Mars", "Ashes to Ashes", "BBC"], "medium", "A character from Life on Mars or from its sequel, Ashes to Ashes?", "Life on Mars", "Ashes to Ashes",
  ["Sam Tyler", "Annie Cartwright", "Maya Roy", "Frank Morgan"], ["Alex Drake", "Shaz Granger", "Jim Keats", "Evan White"])
s("Television", ["Fleabag", "Phoebe Waller-Bridge"], "medium", "Fleabag or Killing Eve character?", "Fleabag", "Killing Eve",
  ["Claire", "The Godmother", "Boo", "Harry"], ["Eve Polastri", "Villanelle", "Konstantin", "Carolyn Martens"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-88.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
