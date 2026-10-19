# Bank session 19 Oct 2026: 2 Categorise questions -> bank/sort-78.json. Each pair of categories was probed against every
# Categorise question in the live bank first (no real-v-fictional village sort; no 1970s-v-1990s police show sort). An Emmerdale v
# Neighbours sort was drafted and dropped: both casts are already used against Coronation Street, Hollyoaks and Home and Away.
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

# each real village played the fictional one on screen: Goathland/Aidensfield, Esholt/Beckindale, Port Isaac/Portwenn, Plockton/Lochdubh
s("Television", ["TV locations", "villages"], "hard", "A real village, or a made-up one from a TV show?", "Real", "Made up",
  ["Goathland", "Esholt", "Port Isaac", "Plockton"], ["Aidensfield", "Beckindale", "Portwenn", "Lochdubh"])
s("Television", ["police", "TV drama"], "medium", "A police or detective show that began in the 1970s, or in the 1990s?", "1970s", "1990s",
  ["The Sweeney", "The Professionals", "Shoestring"], ["A Touch of Frost", "Heartbeat", "Cracker", "Dalziel and Pascoe"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-78.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
