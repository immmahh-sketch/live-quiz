# Bank session 18 Oct 2026: 2 Put in order questions -> bank/order-45.json (big numbers, loudness). Probed against every order
# question in the live bank first (animal speeds and weights, sizes, sporting distances and pitch were already there).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

# 10^3, 10^6, 10^9, 10^12, 10^15, 10^100
o("Maths and numbers", ["big numbers", "powers of ten"], "medium", "Put these numbers in order of size, smallest first",
  ["Thousand", "Million", "Billion", "Trillion", "Quadrillion", "Googol"], "smallest first")
# roughly 20, 30, 60, 75, 110 and 140 decibels
o("Science", ["sound", "decibels"], "medium", "Put these sounds in order of loudness, quietest first",
  ["Rustling leaves", "A whisper", "Normal conversation", "A vacuum cleaner", "A rock concert", "A jet engine taking off"], "quietest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-45.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
