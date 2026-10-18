# Bank session 18 Oct 2026: 2 Put in order questions -> bank/order-46.json (battery sizes, pencil grades). Probed against every
# order question in the live bank first (Starbucks cup sizes, bed sizes, snooker values and chilli heat were already there).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

o("Everyday life", ["batteries", "sizes"], "easy", "Put these batteries in order of size, smallest first",
  ["AAA", "AA", "C", "D"], "smallest first")
# H = hard, B = black (soft); the higher the number, the harder (H) or softer (B) it is
o("Everyday life", ["pencils", "art", "drawing"], "medium", "Put these pencil grades in order, hardest first",
  ["4H", "2H", "H", "HB", "B", "2B", "4B"], "hardest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-46.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
