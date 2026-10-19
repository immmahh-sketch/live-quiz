# Bank session 19 Oct 2026: 2 Categorise questions -> bank/sort-69.json. Two groups, four items each. Each pair of categories
# was probed against every Categorise question in the live bank first (none of these pairs were there).
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("Comedy", ["Spaced", "Black Books", "Channel 4"], "easy", "From Spaced or from Black Books?", "Spaced", "Black Books",
  ["Tim", "Daisy", "Marsha", "Colin the dog"], ["Bernard", "Manny", "Fran", "Nifty Gifty"])
# Richard Briers stars in both, and both were written by Esmonde and Larbey
s("Comedy", ["Ever Decreasing Circles", "The Good Life", "Richard Briers"], "medium", "From Ever Decreasing Circles or from The Good Life?", "Ever Decreasing Circles", "The Good Life",
  ["Martin", "Ann", "Paul Ryman", "Howard and Hilda"], ["Tom", "Barbara", "Margo", "Jerry"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-69.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
