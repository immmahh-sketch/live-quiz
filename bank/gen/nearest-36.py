# Bank session 11 Oct 2026: more Nearest Wins questions -> bank/nearest-36.json: TV show numbers.
# (text, answer, unit, spread, difficulty, category, wow). Tested against the live bank with a copy of the server's near-duplicate rule first.
import json, os
Q = [
 ("Only Fools and Horses ran from 1981 to 2003. How many years is that?", 22, "years", 3, "easy", "TV", False),
 ("How many series of The Crystal Maze did Richard O'Brien host?", 4, "series", 1, "hard", "TV", False),
 ("How many numbers are picked in a Countdown numbers round?", 6, "numbers", 1, "medium", "TV", False),
 ("How many hexagons were on the Blockbusters board?", 20, "hexagons", 4, "hard", "TV", True),
 ("How many series of the UK Office did Ricky Gervais make, before the Christmas specials?", 2, "series", 1, "medium", "TV", False),
 ("How many contestants take part in a normal episode of Pointless?", 8, "contestants", 2, "medium", "TV", False),
]
here = os.path.dirname(os.path.abspath(__file__))
out = [{"type": "nearest", "text": t, "answer": a, "unit": u, "spread": s, "difficulty": d, "category": c, "tags": ["nearest wins"] + (["wow"] if w else [])} for t, a, u, s, d, c, w in Q]
json.dump(out, open(os.path.join(here, '..', 'nearest-36.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'nearest written')
