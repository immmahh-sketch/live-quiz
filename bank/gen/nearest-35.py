# Bank session 11 Oct 2026: more Nearest Wins questions -> bank/nearest-35.json: North East industry, marches and institutions.
# (text, answer, unit, spread, difficulty, category, wow). Tested against the live bank with a copy of the server's near-duplicate rule first.
import json, os
Q = [
 ("Wearmouth Colliery, the last pit in the Durham coalfield, closed in which year?", 1993, "", 5, "hard", "North East", False),
 ("Britain's last deep coal mine, Kellingley Colliery, closed in which year?", 2015, "", 4, "medium", "History", False),
 ("The first Durham Miners' Gala was held in which year?", 1871, "", 10, "hard", "North East", False),
 ("Roughly how many miles did the Jarrow marchers walk to London?", 291, "miles", 40, "hard", "North East", False),
 ("The Hancock Museum in Newcastle first opened in which year?", 1884, "", 12, "hard", "North East", False),
]
here = os.path.dirname(os.path.abspath(__file__))
out = [{"type": "nearest", "text": t, "answer": a, "unit": u, "spread": s, "difficulty": d, "category": c, "tags": ["nearest wins"] + (["wow"] if w else [])} for t, a, u, s, d, c, w in Q]
json.dump(out, open(os.path.join(here, '..', 'nearest-35.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'nearest written')
