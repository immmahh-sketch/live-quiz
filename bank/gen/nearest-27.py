# Bank session 11 Oct 2026: more Nearest Wins questions -> bank/nearest-27.json: heights, reigns, sets and sporting tallies.
# (text, answer, unit, spread, difficulty, category, wow). Tested against the live bank with a copy of the server's near-duplicate rule first.
import json, os
Q = [
 ("In what year did Greggs open its first shop, on Gosforth High Street?", 1951, "", 10, "hard", "North East", True),
 ("In what year did Kevin Keegan first sign for Newcastle as a player?", 1982, "", 4, "medium", "Football", False),
 ("Scotland's Stephen Hendry lifted the trophy at the Crucible how many times?", 7, "titles", 2, "medium", "Sport", False),
 ("Europe's biggest shopping centre when it opened, Gateshead's MetroCentre first traded in which year?", 1986, "", 4, "medium", "North East", False),
 ("The Lindisfarne Gospels were made on Holy Island around which year?", 715, "", 60, "hard", "North East", True),
 ("How many arches does the Ribblehead Viaduct on the Settle-Carlisle line have?", 24, "arches", 5, "hard", "UK geography", False),
 ("Sunderland Empire Theatre first opened its doors in which year?", 1907, "", 15, "hard", "North East", False),
 ("Roughly how many people packed into Wembley Stadium for Live Aid in 1985?", 72000, "people", 10000, "hard", "Music", False),
]
here = os.path.dirname(os.path.abspath(__file__))
out = [{"type": "nearest", "text": t, "answer": a, "unit": u, "spread": s, "difficulty": d, "category": c, "tags": ["nearest wins"] + (["wow"] if w else [])} for t, a, u, s, d, c, w in Q]
json.dump(out, open(os.path.join(here, '..', 'nearest-27.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'nearest written')
