# Bank session 19 Oct 2026: 4 Put in order questions -> bank/order-56.json (Marks and Gran's sitcoms, Nicholas Lyndhurst's
# career, Carla Lane's sitcoms, four sitcoms' start dates). Probed against every order question in the live bank first
# (none of these were there).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

# 1982, 1989, 1993
o("Comedy", ["Marks and Gran", "sitcoms"], "hard", "Put these Marks and Gran sitcoms in order of first series, earliest first",
  ["Shine On Harvey Moon", "Birds of a Feather", "Goodnight Sweetheart"], "earliest first")
# 1978, 1981, 1993, 2013
o("Television", ["Nicholas Lyndhurst", "career"], "medium", "Put these Nicholas Lyndhurst shows in the order he joined them, earliest first",
  ["Butterflies", "Only Fools and Horses", "Goodnight Sweetheart", "New Tricks"], "earliest first")
# 1969, 1978, 1986
o("Comedy", ["Carla Lane", "sitcoms"], "medium", "Put these Carla Lane sitcoms in order of first series, earliest first",
  ["The Liver Birds", "Butterflies", "Bread"], "earliest first")
# 1986, 1989, 1993, 2011
o("Comedy", ["sitcoms"], "medium", "Put these family sitcoms in the order they began, earliest first",
  ["Bread", "Birds of a Feather", "Goodnight Sweetheart", "Friday Night Dinner"], "earliest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-56.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
