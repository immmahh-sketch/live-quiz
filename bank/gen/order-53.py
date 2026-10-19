# Bank session 19 Oct 2026: 4 Put in order questions -> bank/order-53.json (Armando Iannucci's work, Peter Kay's career,
# horses by height, British mammals by size). Probed against every order question in the live bank first (none of these
# were there).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

# 1994, 1997, 2005, 2012, 2017
o("Comedy", ["Armando Iannucci", "career"], "hard", "Put these Armando Iannucci shows and films in order, earliest first",
  ["The Day Today", "I'm Alan Partridge", "The Thick of It", "Veep", "The Death of Stalin"], "earliest first")
# 2000, 2001, 2005, 2015
o("Comedy", ["Peter Kay", "career"], "medium", "Put these Peter Kay moments in order, earliest first",
  ["That Peter Kay Thing", "Phoenix Nights begins", "Amarillo goes to number one", "Car Share begins"], "earliest first")
o("Nature", ["horses", "donkeys", "height"], "easy", "Put these horses and donkeys in order of height at the shoulder, shortest first",
  ["Shetland pony", "Donkey", "Thoroughbred racehorse", "Shire horse"], "shortest first")
o("Nature", ["British wildlife", "mammals", "size"], "easy", "Put these British mammals in order of size, smallest first",
  ["Harvest mouse", "Grey squirrel", "Badger", "Red deer"], "smallest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-53.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
