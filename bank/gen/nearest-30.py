# Bank session 11 Oct 2026: more Nearest Wins questions -> bank/nearest-30.json: shop founding years, game kit and odd body counts.
# (text, answer, unit, spread, difficulty, category, wow). Tested against the live bank with a copy of the server's near-duplicate rule first.
import json, os
Q = [
 ("How many red stitches hold together a regulation baseball?", 108, "stitches", 15, "hard", "Sport", True),
 ("When did John James Sainsbury begin trading from Drury Lane?", 1869, "", 12, "hard", "Brands", False),
 ("IKEA was founded in Sweden in which year?", 1943, "", 8, "medium", "Brands", False),
]
here = os.path.dirname(os.path.abspath(__file__))
out = [{"type": "nearest", "text": t, "answer": a, "unit": u, "spread": s, "difficulty": d, "category": c, "tags": ["nearest wins"] + (["wow"] if w else [])} for t, a, u, s, d, c, w in Q]
json.dump(out, open(os.path.join(here, '..', 'nearest-30.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'nearest written')
