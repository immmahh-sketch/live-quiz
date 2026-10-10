# Bank session 10 Oct 2026: more Nearest Wins questions -> bank/nearest-17.json: British landmarks, TV years and famous numbers.
# (text, answer, unit, spread, difficulty, category, wow). Tested against the live bank with a copy of the server's near-duplicate rule first.
import json, os
Q = [
 ("Blackpool's famous seaside tower stands how many metres high?", 158, "m", 40, "hard", "Landmarks", False),
 ("Roughly how long is Brighton Palace Pier, to the nearest 25 metres?", 525, "m", 150, "hard", "Landmarks", False),
 ("The Severn flows from Wales to the Bristol Channel. Roughly how many miles long is it?", 220, "miles", 50, "medium", "UK geography", False),
 ("Roughly how many million people called Wales home at the 2021 census?", 3.1, "million", 0.8, "hard", "UK geography", False),
 ("In what year did Emmerdale Farm first air on ITV?", 1972, "", 6, "hard", "TV", False),
 ("In what year did the BBC start the world's first regular TV service?", 1936, "", 10, "hard", "TV", True),
 ("In what year did Sky TV launch in Britain?", 1989, "", 6, "medium", "TV", False),
 ("How many Oscars has Meryl Streep won?", 3, "Oscars", 2, "hard", "Film", False),
 ("Judi Dench first played M in GoldenEye. How old was she when it came out?", 60, "", 10, "hard", "James Bond", False),
 ("Counting the Great Bell and its quarter bells, how many bells hang in the Elizabeth Tower?", 5, "bells", 2, "hard", "Landmarks", True),
 ("Roughly how many miles of track does the Tyne and Wear Metro run on?", 48, "miles", 15, "hard", "North East England", False),
 ("In what year did Newcastle's Eldon Square shopping centre open?", 1976, "", 8, "hard", "North East England", False),
 ("In what year did Nissan start building cars in Sunderland?", 1986, "", 6, "medium", "North East England", False),
 ("In what year did I'm a Celebrity... Get Me Out of Here! first air?", 2002, "", 4, "medium", "TV", False),
 ("How many MPs sit in the House of Commons?", 650, "MPs", 100, "medium", "Politics", False),
 ("How many senators are there in the United States Senate?", 100, "senators", 30, "medium", "Politics", False),
 ("Roughly how many nations have a seat in the UN General Assembly?", 193, "countries", 30, "hard", "Politics", False),
]
here = os.path.dirname(os.path.abspath(__file__))
out = [{"type": "nearest", "text": t, "answer": a, "unit": u, "spread": s, "difficulty": d, "category": c, "tags": ["nearest wins"] + (["wow"] if w else [])} for t, a, u, s, d, c, w in Q]
json.dump(out, open(os.path.join(here, '..', 'nearest-17.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'nearest written')
