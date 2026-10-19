# Bank session 19 Oct 2026: 2 Put in order questions -> bank/order-60.json (British birds of prey by wingspan, Channel 4
# sitcoms by first series). Probed against every order question in the live bank first (Ant and Dec's shows and Edgar Wright's
# films were already there).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

# golden eagle about 2.1 m, osprey 1.6, buzzard 1.2, peregrine 1.0, kestrel 0.75
o("Nature", ["birds of prey", "wingspan"], "medium", "Put these birds of prey in order of wingspan, widest first",
  ["Golden eagle", "Osprey", "Buzzard", "Peregrine falcon", "Kestrel"], "widest first")
# 1995, 1999, 2000, 2003, 2006
o("Comedy", ["Channel 4", "sitcoms"], "medium", "Put these Channel 4 sitcoms in order of first series, earliest first",
  ["Father Ted", "Spaced", "Black Books", "Peep Show", "The IT Crowd"], "earliest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-60.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
