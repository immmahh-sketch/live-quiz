# Bank session 19 Oct 2026: 2 Categorise questions -> bank/sort-85.json. Each pair of categories was probed against every
# Categorise question in the live bank first (no Broadchurch v Poldark character sort; no Cornwall v Dorset filming sort).
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("Television", ["Broadchurch", "Poldark"], "medium", "A character from Broadchurch or from Poldark?", "Broadchurch", "Poldark",
  ["Alec Hardy", "Ellie Miller", "Beth Latimer", "Joe Miller"], ["Demelza", "George Warleggan", "Francis", "Elizabeth"])
s("Television", ["TV locations", "film locations", "Cornwall", "Dorset"], "hard", "Filmed mainly in Cornwall or in Dorset?", "Cornwall", "Dorset",
  ["Poldark", "Doc Martin", "Fisherman's Friends", "Jamaica Inn"], ["Broadchurch", "The French Lieutenant's Woman", "Far from the Madding Crowd"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-85.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
