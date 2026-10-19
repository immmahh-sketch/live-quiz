# Bank session 19 Oct 2026: 2 Categorise questions -> bank/sort-87.json. Each pair of categories was probed against every
# Categorise question in the live bank first (Gavin & Stacey only as a show against others and in an Only Fools sort; nothing on Cold
# Feet; no Barry-or-Billericay sort).
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("Television", ["Gavin & Stacey", "Wales", "Essex"], "medium", "A Gavin & Stacey character from Barry or from Billericay?", "Barry", "Billericay",
  ["Nessa", "Bryn", "Gwen", "Dave Coaches"], ["Smithy", "Gavin", "Pam", "Mick"])
s("Television", ["Cold Feet", "Gavin & Stacey"], "medium", "A character from Cold Feet or from Gavin & Stacey?", "Cold Feet", "Gavin & Stacey",
  ["Adam", "Rachel", "David", "Karen"], ["Gavin", "Stacey", "Nessa", "Smithy"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-87.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
