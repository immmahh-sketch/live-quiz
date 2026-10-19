# Bank session 19 Oct 2026: 2 Categorise questions -> bank/sort-81.json. Each pair of categories was probed against every
# Categorise question in the live bank first (no Call the Midwife or Doc Martin sorts; no lizard-or-snake sort). An Inner v Outer
# Hebrides sort was drafted and dropped: the same one is already in.
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("Television", ["Call the Midwife", "Doc Martin", "TV drama"], "medium", "A character from Call the Midwife or from Doc Martin?", "Call the Midwife", "Doc Martin",
  ["Sister Julienne", "Sister Evangelina", "Chummy", "Dr Turner"], ["Louisa", "Aunt Joan", "Bert Large", "PC Penhale"])
# the slow worm is the trap: a legless lizard, not a snake
s("Nature", ["reptiles", "British wildlife"], "medium", "A British lizard or a British snake?", "Lizard", "Snake",
  ["Slow worm", "Sand lizard", "Common lizard"], ["Adder", "Grass snake", "Smooth snake"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-81.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
