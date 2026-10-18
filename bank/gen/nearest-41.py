# Bank session 18 Oct 2026: more Nearest Wins questions -> bank/nearest-41.json (games and TV counts).
# (text, answer, unit, spread, difficulty, category, wow). Tested with lqsql/neardup-n.py (the server's near-duplicate rule)
# and lqsql/audit/tf-dupcheck.py before importing; anything already in the bank is dropped
# (Jenga blocks, pool balls, Monopoly houses and snakes-and-ladders squares were all there).
import json, os
Q = [
 ("How many series of 'Men Behaving Badly' were made?", 6, "series", 1, "hard", "British sitcoms", False),
 ("How many episodes of 'Red Dwarf' did the BBC make in its first run, from 1988 to 1999?", 52, "episodes", 8, "hard", "British sitcoms", False),
 ("Rummikub: how many tiles come in the box?", 106, "tiles", 15, "hard", "Games and toys", True),
 ("The rope, the dagger, the candlestick... how many murder weapons does classic Cluedo have?", 6, "weapons", 1, "medium", "Games and toys", False),
]
here = os.path.dirname(os.path.abspath(__file__))
out = [{"type": "nearest", "text": t, "answer": a, "unit": u, "spread": s, "difficulty": d, "category": c, "tags": ["nearest wins"] + (["wow"] if w else [])} for t, a, u, s, d, c, w in Q]
json.dump(out, open(os.path.join(here, '..', 'nearest-41.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'nearest written')
