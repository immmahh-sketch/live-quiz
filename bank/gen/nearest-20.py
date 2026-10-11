# Bank session 11 Oct 2026: more Nearest Wins questions -> bank/nearest-20.json: sporting firsts, body and animal facts, units.
# (text, answer, unit, spread, difficulty, category, wow). Tested against the live bank with a copy of the server's near-duplicate rule first.
import json, os
Q = [
 ("Roughly how many tiny eyes line the edge of a scallop's shell?", 200, "eyes", 80, "hard", "Animals", True),
 ("In what year was the RNLI lifeboat charity founded?", 1824, "", 25, "hard", "History", False),
 ("In what year was the National Trust founded?", 1895, "", 20, "hard", "History", False),
 ("In what year was the Football Association founded?", 1863, "", 15, "hard", "Football", False),
 ("In what year was golf's first Open Championship played?", 1860, "", 20, "hard", "Sport", False),
 ("In what year did Oxford and Cambridge first row the Boat Race?", 1829, "", 20, "hard", "Sport", False),
 ("In what year was the Rugby Football Union founded?", 1871, "", 15, "hard", "Sport", False),
 ("In what year was the MCC, cricket's famous club at Lord's, founded?", 1787, "", 25, "hard", "Sport", False),
 ("In what year were the first Commonwealth Games, then the British Empire Games, held?", 1930, "", 12, "hard", "Sport", False),
 ("In what year was golf's first Ryder Cup played?", 1927, "", 12, "hard", "Sport", False),
]
here = os.path.dirname(os.path.abspath(__file__))
out = [{"type": "nearest", "text": t, "answer": a, "unit": u, "spread": s, "difficulty": d, "category": c, "tags": ["nearest wins"] + (["wow"] if w else [])} for t, a, u, s, d, c, w in Q]
json.dump(out, open(os.path.join(here, '..', 'nearest-20.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'nearest written')
