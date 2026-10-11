# Bank session 11 Oct 2026: more Nearest Wins questions -> bank/nearest-25.json: awards, chart and game counts.
# (text, answer, unit, spread, difficulty, category, wow). Tested against the live bank with a copy of the server's near-duplicate rule first.
import json, os
Q = [
 ("How many Grammy Awards has Beyoncé won, the most ever?", 35, "Grammys", 8, "hard", "Music", False),
 ("Madonna has topped the UK singles chart how many times?", 13, "number ones", 3, "hard", "Music", False),
 ("Westlife's tally of UK chart-toppers comes to how many?", 14, "number ones", 3, "hard", "Music", False),
 ("Stations and utilities included, how many properties can you buy on a Monopoly board?", 28, "properties", 5, "hard", "Games and toys", False),
 ("How many pieces does each player start with in draughts?", 12, "pieces", 3, "medium", "Games and toys", False),
 ("How many counters does each player have in backgammon?", 15, "counters", 3, "hard", "Games and toys", False),
 ("How many bonus points do you get for using all seven tiles in Scrabble?", 50, "points", 10, "hard", "Games and toys", True),
]
here = os.path.dirname(os.path.abspath(__file__))
out = [{"type": "nearest", "text": t, "answer": a, "unit": u, "spread": s, "difficulty": d, "category": c, "tags": ["nearest wins"] + (["wow"] if w else [])} for t, a, u, s, d, c, w in Q]
json.dump(out, open(os.path.join(here, '..', 'nearest-25.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'nearest written')
