# Bank session 18 Oct 2026: 2 Put in order questions -> bank/order-42.json (imperial lengths, eggs by size). Probed against
# every order question title and item list in the live bank first (old coins by value, a frog's life cycle and the Beaufort
# scale were already there).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

# 1 inch, 12 inches, 3 feet, 22 yards, 220 yards, 1,760 yards
o("Maths and numbers", ["imperial units", "length", "measurement"], "medium", "Put these old imperial lengths in order, shortest first",
  ["Inch", "Foot", "Yard", "Chain", "Furlong", "Mile"], "shortest first")
o("Nature", ["eggs", "birds"], "easy", "Put these eggs in order of size, smallest first",
  ["Quail's egg", "Hen's egg", "Duck egg", "Goose egg", "Emu egg", "Ostrich egg"], "smallest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-42.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
