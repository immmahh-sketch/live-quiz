# Bank session 19 Oct 2026: more Nearest Wins questions -> bank/nearest-47.json (sitcom years and British wildlife).
# (text, answer, unit, spread, difficulty, category, wow). Tested with lqsql/neardup-n.py (the server's near-duplicate rule)
# and lqsql/audit/tf-dupcheck.py before importing; none of these topics were in the nearest bank.
import json, os
Q = [
 ("At its peak, roughly how many million viewers watched the Liverpool sitcom Bread?", 21, "million", 4, "hard", "Comedy", True),
 ("In what year did Friday Night Dinner begin on Channel 4?", 2011, "", 2, "medium", "Comedy", False),
 ("In what year did Birds of a Feather begin on BBC One?", 1989, "", 3, "medium", "Comedy", False),
 ("In what year did Goodnight Sweetheart, with Nicholas Lyndhurst, begin?", 1993, "", 3, "medium", "Comedy", False),
 ("Gordon Brittas first took charge of Whitbury Leisure Centre on BBC One in which year?", 1991, "", 3, "medium", "Comedy", False),
 ("Roughly how many kilometres does a British swallow fly to reach South Africa for the winter?", 10000, "km", 2000, "medium", "Nature", True),
 ("Roughly how many metres of tunnel can a mole dig in a day?", 20, "metres", 5, "hard", "Nature", True),
 ("Roughly what percentage of the world's grey seals live around Britain?", 40, "%", 8, "hard", "Nature", True),
 ("What's the record number of fish a puffin has been seen carrying in its beak at once?", 62, "fish", 10, "hard", "Nature", True),
 ("Roughly how many wild red deer live in Scotland?", 400000, "deer", 80000, "hard", "Nature", False),
]
here = os.path.dirname(os.path.abspath(__file__))
out = [{"type": "nearest", "text": t, "answer": a, "unit": u, "spread": s, "difficulty": d, "category": c, "tags": ["nearest wins"] + (["wow"] if w else [])} for t, a, u, s, d, c, w in Q]
json.dump(out, open(os.path.join(here, '..', 'nearest-47.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'nearest written')
