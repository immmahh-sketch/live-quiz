# Bank session 19 Oct 2026: 2 Categorise questions -> bank/sort-76.json. Each pair of categories was probed against every
# Categorise question in the live bank first (no David Jason v Ronnie Barker or fungus v flower sorts).
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

# Granville and Arkwright are the trap: both from Open All Hours
s("Television", ["David Jason", "Ronnie Barker", "sitcoms"], "medium", "A character played by David Jason or by Ronnie Barker?", "David Jason", "Ronnie Barker",
  ["Del Boy", "Granville", "Pop Larkin", "Jack Frost"], ["Fletcher", "Arkwright", "Clarence", "Lord Rustless"])
s("Nature", ["fungi", "wild flowers", "British wildlife"], "hard", "A British fungus or a British wild flower?", "Fungus", "Wild flower",
  ["Fly agaric", "Penny bun", "Jelly ear", "Dead man's fingers"], ["Lords-and-ladies", "Cuckooflower", "Lady's slipper", "Bird's-foot trefoil"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-76.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
