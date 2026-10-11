# Bank session 11 Oct 2026: more Nearest Wins questions -> bank/nearest-32.json: North East monuments, towers and saints.
# (text, answer, unit, spread, difficulty, category, wow). Tested against the live bank with a copy of the server's near-duplicate rule first.
import json, os
Q = [
 ("How many steps lead to the top of St Mary's Lighthouse at Whitley Bay?", 137, "steps", 15, "hard", "North East", False),
 ("How many steps climb Durham Cathedral's central tower?", 325, "steps", 30, "hard", "North East", False),
 ("How tall is Durham Cathedral's central tower, in metres?", 66, "metres", 8, "hard", "North East", False),
 ("St Wilfrid founded Hexham Abbey in which year?", 674, "", 40, "hard", "North East", True),
 ("The Venerable Bede died at Jarrow in which year?", 735, "", 30, "hard", "North East", False),
 ("The Tyne Bridge's great steel arch spans roughly how many metres?", 161, "metres", 20, "hard", "North East", False),
]
here = os.path.dirname(os.path.abspath(__file__))
out = [{"type": "nearest", "text": t, "answer": a, "unit": u, "spread": s, "difficulty": d, "category": c, "tags": ["nearest wins"] + (["wow"] if w else [])} for t, a, u, s, d, c, w in Q]
json.dump(out, open(os.path.join(here, '..', 'nearest-32.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'nearest written')
