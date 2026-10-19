# Bank session 19 Oct 2026: 3 Categorise questions -> bank/sort-59.json. Two groups, four items each. Each pair of categories
# was probed against every Categorise question in the live bank first (none of these pairs were there).
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("Comedy", ["Dinnerladies", "Still Game", "sitcoms"], "easy", "A Dinnerladies character or a Still Game character?", "Dinnerladies", "Still Game",
  ["Bren", "Tony", "Dolly", "Twinkle"], ["Jack", "Victor", "Winston", "Isa"])
s("Nature", ["ponies", "dogs", "breeds"], "medium", "A breed of pony or a breed of dog?", "Pony", "Dog",
  ["Shetland", "Exmoor", "Dartmoor", "Connemara"], ["Dalmatian", "Pomeranian", "Labrador", "Weimaraner"])
s("Comedy", ["Detectorists", "The Thick of It", "sitcoms"], "medium", "From Detectorists or from The Thick of It?", "Detectorists", "The Thick of It",
  ["Andy", "Lance", "Danebury", "Simon and Garfunkel"], ["Malcolm Tucker", "Ollie Reeder", "Nicola Murray", "DoSAC"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-59.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
