# Bank session 19 Oct 2026: 2 Categorise questions -> bank/sort-68.json. Two groups, three or four items each. Each pair of
# categories was probed against every Categorise question in the live bank first (none of these pairs were there).
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

# Geoffrey Palmer is in both
s("Comedy", ["As Time Goes By", "Butterflies", "Geoffrey Palmer"], "medium", "From As Time Goes By or from Butterflies?", "As Time Goes By", "Butterflies",
  ["Jean", "Lionel", "Judy", "Rocky"], ["Ria", "Ben the dentist", "Leonard", "Russell"])
s("Television", ["breakfast TV", "BBC", "ITV"], "medium", "A BBC breakfast show or an ITV one?", "BBC", "ITV",
  ["Breakfast Time", "BBC Breakfast", "Breakfast News"], ["TV-am", "GMTV", "Daybreak", "Good Morning Britain"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-68.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
