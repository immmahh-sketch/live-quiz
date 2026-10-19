# Bank session 19 Oct 2026: more Nearest Wins questions -> bank/nearest-46.json (sitcom years and British wildlife).
# (text, answer, unit, spread, difficulty, category, wow). Tested with lqsql/neardup-n.py (the server's near-duplicate rule)
# and lqsql/audit/tf-dupcheck.py before importing; anything already in the bank is dropped (Ghosts' ghost count, the
# peregrine's dive speed and a badger's worms were already there).
import json, os
Q = [
 ("In what year did Bottom, with Rik Mayall and Ade Edmondson, begin on BBC Two?", 1991, "", 3, "medium", "Comedy", False),
 ("In what year did Still Game begin on BBC Scotland?", 2002, "", 3, "medium", "Comedy", False),
 ("In what year did Victoria Wood's Dinnerladies begin?", 1998, "", 3, "medium", "Comedy", False),
 ("How old was Victoria Wood when she died in 2016?", 62, "", 4, "hard", "Comedy", False),
 ("Roughly how many pairs of golden eagles breed in Scotland?", 500, "pairs", 100, "hard", "Nature", True),
 ("Roughly how many eggs are in one clump of common frogspawn?", 2000, "eggs", 500, "medium", "Nature", True),
 ("In what year was the Donkey Sanctuary founded in Devon?", 1969, "", 5, "hard", "Nature", False),
 ("In what year were grey squirrels first let loose in Britain, at Henbury Park in Cheshire?", 1876, "", 15, "hard", "Nature", True),
 ("Roughly how many badgers live in England and Wales?", 485000, "badgers", 100000, "hard", "Nature", True),
]
here = os.path.dirname(os.path.abspath(__file__))
out = [{"type": "nearest", "text": t, "answer": a, "unit": u, "spread": s, "difficulty": d, "category": c, "tags": ["nearest wins"] + (["wow"] if w else [])} for t, a, u, s, d, c, w in Q]
json.dump(out, open(os.path.join(here, '..', 'nearest-46.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'nearest written')
