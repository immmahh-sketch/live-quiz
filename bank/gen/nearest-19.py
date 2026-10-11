# Bank session 11 Oct 2026: more Nearest Wins questions -> bank/nearest-19.json: North East history, famous firsts, British brands.
# (text, answer, unit, spread, difficulty, category, wow). Tested against the live bank with a copy of the server's near-duplicate rule first.
import json, os
Q = [
 ("In what year did Newcastle upon Tyne become a city?", 1882, "", 20, "hard", "North East England", False),
 ("In what year did Kevin Keegan first become Newcastle United manager?", 1992, "", 4, "medium", "Football", False),
 ("In what year did Grace Darling row out to rescue the Forfarshire's survivors?", 1838, "", 20, "hard", "North East England", True),
 ("In what year did the Jarrow March to London take place?", 1936, "", 8, "medium", "History", False),
 ("Roughly how many men set off on the Jarrow March?", 200, "marchers", 60, "hard", "History", True),
 ("The 'blinking eye' that tilts across the Tyne opened in what year?", 2001, "", 3, "medium", "North East England", False),
 ("In what year was Penshaw Monument built?", 1844, "", 25, "hard", "North East England", False),
 ("Newcastle's Swing Bridge first swung open in what year?", 1876, "", 20, "hard", "North East England", False),
 ("Robert Stephenson's High Level Bridge across the Tyne opened in what year?", 1849, "", 20, "hard", "North East England", False),
 ("In what year did the Theatre Royal on Grey Street open?", 1837, "", 25, "hard", "North East England", False),
 ("In what year did Northumberland become a National Park?", 1956, "", 10, "hard", "North East England", False),
 ("Cars first drove under the river between Jarrow and Howdon in what year?", 1967, "", 8, "medium", "North East England", False),
]
here = os.path.dirname(os.path.abspath(__file__))
out = [{"type": "nearest", "text": t, "answer": a, "unit": u, "spread": s, "difficulty": d, "category": c, "tags": ["nearest wins"] + (["wow"] if w else [])} for t, a, u, s, d, c, w in Q]
json.dump(out, open(os.path.join(here, '..', 'nearest-19.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'nearest written')
