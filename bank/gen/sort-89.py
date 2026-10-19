# Bank session 19 Oct 2026: 2 Categorise questions -> bank/sort-89.json. Each pair of categories was probed against every
# Categorise question in the live bank first (no Spooks sort; a general BBC-or-ITV sort exists but not for spy series).
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("Television", ["Spooks", "Line of Duty", "BBC"], "medium", "A character from Spooks or from Line of Duty?", "Spooks", "Line of Duty",
  ["Harry Pearce", "Tom Quinn", "Ruth Evershed", "Ros Myers"], ["Ted Hastings", "Steve Arnott", "Kate Fleming", "Dot Cottan"])
s("Television", ["spies", "British TV", "BBC", "ITV"], "hard", "A British spy series made for the BBC or for ITV?", "BBC", "ITV",
  ["Spooks", "The Night Manager", "Tinker Tailor Soldier Spy"], ["Callan", "The Avengers", "Danger Man", "The Prisoner"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-89.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
