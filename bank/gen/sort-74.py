# Bank session 19 Oct 2026: 2 Categorise questions -> bank/sort-74.json. Each pair of categories was probed against every
# Categorise question in the live bank first (no Bergerac, Lovejoy or wader sorts; the seabird sorts use Puffin, Gannet,
# Kittiwake and Guillemot, so the seabirds here are different ones).
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("Television", ["Bergerac", "Lovejoy", "BBC"], "hard", "A character from Bergerac or from Lovejoy?", "Bergerac", "Lovejoy",
  ["Charlie Hungerford", "Philippa Vale", "Barney Crozier", "Diamante Lil"], ["Tinker", "Eric Catchpole", "Lady Jane Felsham", "Charlotte Cavendish"])
s("Nature", ["birds", "seabirds", "waders", "British wildlife"], "hard", "Seabird or wader?", "Seabird", "Wader",
  ["Fulmar", "Shag", "Razorbill", "Manx shearwater"], ["Curlew", "Oystercatcher", "Avocet", "Lapwing"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-74.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
