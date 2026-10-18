# Bank session 18 Oct 2026: more Nearest Wins questions -> bank/nearest-40.json (TV, games and nature numbers).
# North East dates were tried first and were all in the bank already; the earthworm's hearts, a lobster's legs, the
# Rubik's Cube, dots on two dice and Summer Wine's run were there too. (text, answer, unit, spread, difficulty, category, wow).
# Tested with lqsql/neardup-n.py (the server's near-duplicate rule) and lqsql/audit/tf-dupcheck.py before importing.
import json, os
Q = [
 ("How many numbered Thunderbird craft were there in the original 'Thunderbirds'?", 5, "craft", 1, "medium", "Television", False),
 ("Ronnie Barker's 'Porridge' ran to how many series?", 3, "series", 1, "hard", "British sitcoms", False),
 ("Roughly how many episodes of ''Allo 'Allo!' were made?", 85, "episodes", 15, "hard", "British sitcoms", False),
 ("How many contestants take part in each series of 'Taskmaster'?", 5, "contestants", 1, "medium", "Television", False),
 ("Connect 4: how many counters fill the whole grid?", 42, "counters", 6, "medium", "Games and toys", False),
 ("In Harry Potter, a Quidditch side fields how many players?", 7, "players", 1, "medium", "Harry Potter", False),
]
here = os.path.dirname(os.path.abspath(__file__))
out = [{"type": "nearest", "text": t, "answer": a, "unit": u, "spread": s, "difficulty": d, "category": c, "tags": ["nearest wins"] + (["wow"] if w else [])} for t, a, u, s, d, c, w in Q]
json.dump(out, open(os.path.join(here, '..', 'nearest-40.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'nearest written')
