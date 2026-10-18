# Bank session 18 Oct 2026: more Nearest Wins questions -> bank/nearest-42.json (geography and everyday counts).
# (text, answer, unit, spread, difficulty, category, wow). Tested with lqsql/neardup-n.py (the server's near-duplicate rule)
# and lqsql/audit/tf-dupcheck.py before importing; anything already in the bank is dropped (the Scilly islands,
# Ireland's counties, Germany's neighbours, Russia's time zones and Land's End to John o' Groats were all there,
# and so were Gaelic football teams, limerick lines and haiku syllables).
import json, os
Q = [
 ("In the British winter, how many hours ahead of London is Tokyo?", 9, "hours", 2, "medium", "World geography", False),
 ("Roughly how many baked beans are in a standard 415g tin?", 465, "beans", 60, "hard", "Food and drink", True),
 ("On the shortest day, roughly how many hours of daylight does Newcastle get?", 7, "hours", 1, "medium", "The North East of England", True),
 ("How many raised dots make up a single Braille cell?", 6, "dots", 1, "medium", "Science and technology", False),
]
here = os.path.dirname(os.path.abspath(__file__))
out = [{"type": "nearest", "text": t, "answer": a, "unit": u, "spread": s, "difficulty": d, "category": c, "tags": ["nearest wins"] + (["wow"] if w else [])} for t, a, u, s, d, c, w in Q]
json.dump(out, open(os.path.join(here, '..', 'nearest-42.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'nearest written')
