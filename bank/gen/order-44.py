# Bank session 18 Oct 2026: 1 Put in order question -> bank/order-44.json (planets by temperature; the trap is that Venus,
# not Mercury, is hottest). Probed against every order question in the live bank first: rivers by length, shapes by sides and
# newspapers by founding date were all there already.
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

# average surface (or cloud-top) temperature: Venus ~464°C, Mercury ~167°C, Earth ~15°C, Mars ~-63°C, Jupiter ~-110°C
o("Space and astronomy", ["planets", "temperature", "Venus"], "hard", "Put these planets in order of average temperature, hottest first",
  ["Venus", "Mercury", "Earth", "Mars", "Jupiter"], "hottest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-44.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
