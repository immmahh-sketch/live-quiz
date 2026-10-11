# Bank session 11 Oct 2026: more Nearest Wins questions -> bank/nearest-31.json: long-distance paths, hills and Kielder.
# (text, answer, unit, spread, difficulty, category, wow). Tested against the live bank with a copy of the server's near-duplicate rule first.
import json, os
Q = [
 ("End to end, Edale to Kirk Yetholm, what is the Pennine Way's length in miles?", 268, "miles", 30, "hard", "UK geography", False),
 ("The Hadrian's Wall Path national trail, Wallsend to Bowness-on-Solway, is how many miles?", 84, "miles", 10, "hard", "North East", False),
 ("Roughly how many miles is the C2C cycle route across the north of England?", 137, "miles", 15, "hard", "North East", False),
 ("How many miles is the Cleveland Way, Helmsley to Filey?", 109, "miles", 12, "hard", "UK geography", False),
 ("How high is Cross Fell, the top of the Pennines, in metres?", 893, "metres", 60, "hard", "UK geography", False),
 ("How high is The Cheviot, Northumberland's highest hill, in metres?", 815, "metres", 60, "hard", "North East", False),
 ("Roughly how many million trees grow in Kielder Forest?", 150, "million trees", 30, "hard", "North East", True),
]
here = os.path.dirname(os.path.abspath(__file__))
out = [{"type": "nearest", "text": t, "answer": a, "unit": u, "spread": s, "difficulty": d, "category": c, "tags": ["nearest wins"] + (["wow"] if w else [])} for t, a, u, s, d, c, w in Q]
json.dump(out, open(os.path.join(here, '..', 'nearest-31.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'nearest written')
