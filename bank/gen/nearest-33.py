# Bank session 11 Oct 2026: more Nearest Wins questions -> bank/nearest-33.json: bridges, towers and halls by opening year.
# (text, answer, unit, spread, difficulty, category, wow). Tested against the live bank with a copy of the server's near-duplicate rule first.
import json, os
Q = [
 ("Lord Armstrong bought Bamburgh Castle in which year?", 1894, "", 12, "hard", "North East", False),
 ("Cragside became the first house lit by hydroelectricity in which year?", 1878, "", 10, "hard", "North East", True),
 ("Telford's Menai Suspension Bridge opened in which year?", 1826, "", 15, "hard", "UK geography", False),
 ("Bristol's Clifton Suspension Bridge opened in which year?", 1864, "", 15, "hard", "UK geography", False),
 ("Middlesbrough's Transporter Bridge opened in which year?", 1911, "", 10, "hard", "North East", False),
 ("Blackpool's seaside landmark on the Golden Mile welcomed its first visitors in which year?", 1894, "", 10, "medium", "UK geography", False),
 ("The Royal Albert Hall opened in which year?", 1871, "", 10, "hard", "Music", False),
]
here = os.path.dirname(os.path.abspath(__file__))
out = [{"type": "nearest", "text": t, "answer": a, "unit": u, "spread": s, "difficulty": d, "category": c, "tags": ["nearest wins"] + (["wow"] if w else [])} for t, a, u, s, d, c, w in Q]
json.dump(out, open(os.path.join(here, '..', 'nearest-33.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'nearest written')
