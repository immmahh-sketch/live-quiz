# Bank session 18 Oct 2026: more Nearest Wins questions -> bank/nearest-44.json (wild animals and game shows).
# (text, answer, unit, spread, difficulty, category, wow). Tested with lqsql/neardup-n.py (the server's near-duplicate rule)
# and lqsql/audit/tf-dupcheck.py before importing; anything already in the bank is dropped (owl head turns, panda eating hours,
# koala sleep, camel drinking, Blockbusters hexagons and Crystal Maze series were all there).
import json, os
Q = [
 ("Roughly how many tigers are left in the wild, worldwide?", 5500, "tigers", 1000, "hard", "Nature", True),
 ("Roughly how many giant pandas live in the wild?", 1860, "pandas", 300, "hard", "Nature", True),
 ("A big male hippo weighs roughly how many tonnes?", 3, "tonnes", 1, "medium", "Nature", False),
 ("Roughly how many earthworms can a badger eat in a single night?", 200, "worms", 50, "hard", "Nature", True),
 ("Roughly how many teeth does a bottlenose dolphin have?", 90, "teeth", 15, "hard", "Nature", False),
 ("A big silverback gorilla weighs roughly how many kilograms?", 180, "kg", 30, "medium", "Nature", False),
 ("In what year did Bullseye, with Jim Bowen, first air?", 1981, "", 3, "medium", "Television", False),
 ("In what year did Anne Robinson first tell someone they were the weakest link?", 2000, "", 3, "medium", "Television", False),
 ("In what year did Ben Shephard's Tipping Point first air?", 2012, "", 3, "medium", "Television", False),
 ("How many clues make up an Only Connect wall?", 16, "clues", 3, "medium", "Television", False),
]
here = os.path.dirname(os.path.abspath(__file__))
out = [{"type": "nearest", "text": t, "answer": a, "unit": u, "spread": s, "difficulty": d, "category": c, "tags": ["nearest wins"] + (["wow"] if w else [])} for t, a, u, s, d, c, w in Q]
json.dump(out, open(os.path.join(here, '..', 'nearest-44.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'nearest written')
