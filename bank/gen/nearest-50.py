# Bank session 19 Oct 2026: more Nearest Wins questions -> bank/nearest-50.json (cop-show and soap start years, British islands,
# birds). (text, answer, unit, spread, difficulty, category, wow). Tested with lqsql/neardup-n.py (the server's near-duplicate rule)
# before importing; Emmerdale's start year and Neighbours' length were already in, so they're not here.
# Dropped: Brookside's start (same answer as an old Channel 4 launch question); four others reworded for the rule.
import json, os
Q = [
 ("Holby City Hospital's emergency department first appeared on screen, in Casualty, in which year?", 1986, "", 3, "medium", "Television", False),
 ("In what year did John Thaw and Dennis Waterman's The Sweeney begin?", 1975, "", 3, "medium", "Television", False),
 ("In what year did Bodie and Doyle's The Professionals begin on ITV?", 1977, "", 3, "hard", "Television", False),
 ("In what year did Home and Away begin in Australia?", 1988, "", 3, "medium", "Television", False),
 ("The one-off police drama Woodentop, which grew into The Bill, was shown in which year?", 1983, "", 3, "hard", "Television", False),
 ("The Isle of Skye covers roughly how many square kilometres?", 1656, "km²", 350, "hard", "Geography", False),
 ("Lundy island is roughly how many miles from end to end?", 3, "miles", 1, "hard", "Geography", True),
 ("A grey partridge lays roughly how many eggs in one go?", 15, "eggs", 4, "medium", "Nature", True),
 ("How many kinds of bat breed in Britain, roughly?", 18, "species", 4, "hard", "Nature", True),
]
here = os.path.dirname(os.path.abspath(__file__))
out = [{"type": "nearest", "text": t, "answer": a, "unit": u, "spread": s, "difficulty": d, "category": c, "tags": ["nearest wins"] + (["wow"] if w else [])} for t, a, u, s, d, c, w in Q]
json.dump(out, open(os.path.join(here, '..', 'nearest-50.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'nearest written')
