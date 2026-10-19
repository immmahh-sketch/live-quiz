# Bank session 19 Oct 2026: 2 Put in order questions -> bank/order-71.json (James Herriot milestones, TV vet shows).
# Probed against every order question in the live bank first (nothing on Herriot or vet programmes).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

# 1916, 1970, 1975, 1978, 2020
o("Television", ["James Herriot", "All Creatures Great and Small", "books"], "hard", "Put these James Herriot milestones in order, earliest first",
  ["Alf Wight is born", "His first book, If Only They Could Talk", "The first film, All Creatures Great and Small", "The BBC series begins", "The Channel 5 remake begins"], "earliest first")
# 1978, 1994, 1997, 2014, 2015
o("Television", ["vets", "animals", "factual TV"], "hard", "Put these TV vet shows in order of first broadcast, earliest first",
  ["All Creatures Great and Small", "Animal Hospital", "Vets in Practice", "The Supervet", "The Yorkshire Vet"], "earliest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-71.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
