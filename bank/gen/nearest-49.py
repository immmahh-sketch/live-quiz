# Bank session 19 Oct 2026: more Nearest Wins questions -> bank/nearest-49.json (TV detective-drama years and British wildlife
# and landmarks). (text, answer, unit, spread, difficulty, category, wow). Tested with lqsql/neardup-n.py (the server's
# near-duplicate rule) before importing. Dropped: an owl's head-turn (already in); the Taggart one reworded.
import json, os
Q = [
 ("In what year did John Nettles's Bergerac begin on BBC One?", 1981, "", 3, "medium", "Television", False),
 ("In what year did George Cole and Dennis Waterman's Minder begin on ITV?", 1979, "", 3, "medium", "Television", False),
 ("In what year did Ian McShane's Lovejoy first appear on BBC One?", 1986, "", 3, "hard", "Television", False),
 ("Mark McManus first played Glasgow detective Jim Taggart in which year?", 1983, "", 3, "hard", "Television", False),
 ("How many episodes of Inspector Morse were made with John Thaw, from 1987 to 2000?", 33, "episodes", 6, "hard", "Television", True),
 ("Roughly how many northern gannets crowd onto the Bass Rock in summer?", 150000, "gannets", 40000, "hard", "Nature", True),
 ("In what year were red kites first released back into England and Scotland?", 1989, "", 4, "hard", "Nature", False),
 ("The Sycamore Gap tree on Hadrian's Wall was said to be roughly how many years old when it was cut down in 2023?", 150, "years", 40, "medium", "North East", True),
 ("A brown hare can sprint at roughly how many miles an hour?", 45, "mph", 8, "medium", "Nature", False),
 ("In what year did the Spanish City dome open at Whitley Bay?", 1910, "", 8, "hard", "North East", False),
]
here = os.path.dirname(os.path.abspath(__file__))
out = [{"type": "nearest", "text": t, "answer": a, "unit": u, "spread": s, "difficulty": d, "category": c, "tags": ["nearest wins"] + (["wow"] if w else [])} for t, a, u, s, d, c, w in Q]
json.dump(out, open(os.path.join(here, '..', 'nearest-49.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'nearest written')
