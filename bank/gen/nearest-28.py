# Bank session 11 Oct 2026: more Nearest Wins questions -> bank/nearest-28.json: viaducts, venues and sporting tallies.
# (text, answer, unit, spread, difficulty, category, wow). Tested against the live bank with a copy of the server's near-duplicate rule first.
import json, os
Q = [
 ("How many times did Ruby Walsh ride the Grand National winner?", 2, "wins", 1, "hard", "Sport", False),
 ("How many Wimbledon titles, singles and doubles together, did Billie Jean King win?", 20, "titles", 4, "hard", "Sport", True),
 ("How many locks make up the whole Caen Hill flight on the Kennet and Avon Canal?", 29, "locks", 5, "hard", "UK geography", True),
 ("How many steps lead to the top of the Scott Monument in Edinburgh?", 287, "steps", 40, "hard", "Scotland", False),
 ("Durham's Lumiere light festival was first held in which year?", 2009, "", 3, "hard", "North East", False),
 ("How many England caps did Wayne Rooney win?", 120, "caps", 12, "medium", "Football", False),
 ("How many arches does the Glenfinnan Viaduct, the Harry Potter railway bridge, have?", 21, "arches", 4, "hard", "Scotland", True),
 ("How many Test wickets did Shane Warne take?", 708, "wickets", 60, "hard", "Sport", False),
 ("Roughly how many words long is Lincoln's Gettysburg Address?", 272, "words", 50, "hard", "History", True),
 ("How old was Pelé when he won his first World Cup?", 17, "years old", 2, "medium", "Football", True),
]
here = os.path.dirname(os.path.abspath(__file__))
out = [{"type": "nearest", "text": t, "answer": a, "unit": u, "spread": s, "difficulty": d, "category": c, "tags": ["nearest wins"] + (["wow"] if w else [])} for t, a, u, s, d, c, w in Q]
json.dump(out, open(os.path.join(here, '..', 'nearest-28.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'nearest written')
