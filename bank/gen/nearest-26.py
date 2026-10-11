# Bank session 11 Oct 2026: more Nearest Wins questions -> bank/nearest-26.json: long-running TV careers.
# (text, answer, unit, spread, difficulty, category, wow). Tested against the live bank with a copy of the server's near-duplicate rule first.
import json, os
Q = [
 ("Ken Barlow first appeared in Coronation Street in 1960. How many years had he been on it by 2025?", 65, "years", 8, "medium", "TV", True),
 ("For how many years did Bruce Forsyth host Strictly Come Dancing?", 10, "years", 3, "medium", "TV", False),
 ("For how many years did David Dimbleby chair Question Time?", 25, "years", 5, "hard", "TV", False),
 ("For how many years did Gary Lineker present Match of the Day?", 26, "years", 5, "medium", "TV", False),
 ("For how many years did Jeremy Paxman host University Challenge?", 29, "years", 5, "hard", "TV", False),
 ("Molly and Arthur Weasley have how many children in all?", 7, "children", 2, "medium", "Books", False),
 ("For how many years was Terry Wogan the BBC's TV voice of Eurovision?", 28, "years", 6, "hard", "TV", False),
 ("For how many years did Richard and Judy present This Morning?", 13, "years", 4, "hard", "TV", False),
]
here = os.path.dirname(os.path.abspath(__file__))
out = [{"type": "nearest", "text": t, "answer": a, "unit": u, "spread": s, "difficulty": d, "category": c, "tags": ["nearest wins"] + (["wow"] if w else [])} for t, a, u, s, d, c, w in Q]
json.dump(out, open(os.path.join(here, '..', 'nearest-26.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'nearest written')
