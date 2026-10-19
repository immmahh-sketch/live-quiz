# Bank session 19 Oct 2026: 1 Categorise question -> bank/sort-70.json. Two groups, four items each. Each pair of categories
# was probed against every Categorise question in the live bank first (Grange Hill v Byker Grove and Bond v the Doctor
# exist, so only the North East shows question was new).
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("Television", ["North East", "TV drama", "sitcoms"], "medium", "A TV show set in the North East or not?", "North East", "Somewhere else",
  ["Vera", "Byker Grove", "The Likely Lads", "Our Friends in the North"], ["Still Game", "Phoenix Nights", "Shameless", "The Royle Family"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-70.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
