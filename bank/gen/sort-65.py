# Bank session 19 Oct 2026: 2 Categorise questions -> bank/sort-65.json. Two groups, four items each. Each pair of categories
# was probed against every Categorise question in the live bank first (sheep v cattle breeds exists; goats weren't there).
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("Comedy", ["My Family", "Outnumbered", "sitcoms"], "easy", "A My Family character or an Outnumbered character?", "My Family", "Outnumbered",
  ["Ben", "Susan", "Nick", "Janey"], ["Pete", "Sue", "Jake", "Karen"])
s("Nature", ["farming", "breeds", "goats", "sheep"], "hard", "A breed of goat or a breed of sheep?", "Goat", "Sheep",
  ["Nubian", "Saanen", "Toggenburg", "Boer"], ["Suffolk", "Texel", "Herdwick", "Merino"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-65.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
