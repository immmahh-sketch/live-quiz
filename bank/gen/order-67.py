# Bank session 19 Oct 2026: 2 Put in order questions -> bank/order-67.json (Emmerdale milestones, Neighbours milestones).
# Probed against every order question in the live bank first (soaps appear only in when-they-began orders and Kylie only in
# chart and album orders).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

# 1972, 1989, 1993, 1994, 2022
o("Television", ["Emmerdale", "soaps"], "hard", "Put these Emmerdale milestones in order, earliest first",
  ["Emmerdale Farm begins", "'Farm' is dropped from the title", "A plane crashes on the village", "The Dingles arrive", "The 50th anniversary"], "earliest first")
# 1985, 1987, 1988, 2008, 2022
o("Television", ["Neighbours", "soaps"], "medium", "Put these Neighbours milestones in order, earliest first",
  ["The first episode", "Scott and Charlene's wedding", "Kylie's first number one, 'I Should Be So Lucky'", "The UK move to Channel 5", "The 'final' episode before the revival"], "earliest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-67.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
