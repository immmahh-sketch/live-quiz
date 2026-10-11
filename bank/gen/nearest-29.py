# Bank session 11 Oct 2026: more Nearest Wins questions -> bank/nearest-29.json: North East years, TV years and sporting numbers.
# (text, answer, unit, spread, difficulty, category, wow). Tested against the live bank with a copy of the server's near-duplicate rule first.
import json, os
Q = [
 ("Count every player on the field at Croke Park in an All-Ireland Gaelic football final. What's the total?", 30, "players", 4, "hard", "Sport", True),
 ("Over one lap in the 400 m hurdles, how many barriers does each athlete jump?", 10, "hurdles", 2, "medium", "Sport", False),
 ("How many maximum 147 breaks has Ronnie O'Sullivan made in professional competition?", 15, "maximums", 3, "hard", "Sport", False),
 ("Roughly how many people live on the Isle of Man?", 84000, "people", 12000, "hard", "UK geography", False),
]
here = os.path.dirname(os.path.abspath(__file__))
out = [{"type": "nearest", "text": t, "answer": a, "unit": u, "spread": s, "difficulty": d, "category": c, "tags": ["nearest wins"] + (["wow"] if w else [])} for t, a, u, s, d, c, w in Q]
json.dump(out, open(os.path.join(here, '..', 'nearest-29.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'nearest written')
