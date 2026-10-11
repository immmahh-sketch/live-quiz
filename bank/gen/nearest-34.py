# Bank session 11 Oct 2026: more Nearest Wins questions -> bank/nearest-34.json: North East football grounds, clubs and crowds.
# (text, answer, unit, spread, difficulty, category, wow). Tested against the live bank with a copy of the server's near-duplicate rule first.
import json, os
Q = [
 ("Sunderland played their last game at Roker Park in which year?", 1997, "", 4, "medium", "North East", False),
 ("Durham County Cricket Club became a first-class county in which year?", 1992, "", 5, "hard", "North East", False),
 ("Middlesbrough's Riverside Stadium opened in which year?", 1995, "", 4, "medium", "North East", False),
 ("St James' Park's record crowd, set in 1930, was roughly how many?", 68386, "people", 5000, "hard", "North East", True),
 ("Roker Park's record crowd, against Derby in 1933, was roughly how many?", 75118, "people", 6000, "hard", "North East", True),
 ("Sunderland's tally of top-flight English titles stands at what?", 6, "titles", 2, "medium", "North East", False),
 ("The Magpies' tally of top-flight English titles stands at what? (Newcastle United)", 4, "titles", 1, "medium", "North East", False),
]
here = os.path.dirname(os.path.abspath(__file__))
out = [{"type": "nearest", "text": t, "answer": a, "unit": u, "spread": s, "difficulty": d, "category": c, "tags": ["nearest wins"] + (["wow"] if w else [])} for t, a, u, s, d, c, w in Q]
json.dump(out, open(os.path.join(here, '..', 'nearest-34.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'nearest written')
