# Bank session 19 Oct 2026: more Nearest Wins questions -> bank/nearest-45.json (classic sitcoms and pets).
# (text, answer, unit, spread, difficulty, category, wow). Tested with lqsql/neardup-n.py (the server's near-duplicate rule)
# and lqsql/audit/tf-dupcheck.py before importing; anything already in the bank is dropped (a dog's teeth, Only Fools',
# episode count, hens' eggs a year and cats' sleep were already there).
import json, os
Q = [
 ("How many episodes of Are You Being Served? were made?", 69, "episodes", 10, "hard", "Comedy", False),
 ("Counting both shows and the specials, how many episodes of Yes Minister and Yes, Prime Minister were made?", 38, "episodes", 6, "hard", "Comedy", False),
 ("In what year was Steptoe and Son first shown?", 1962, "", 3, "medium", "Comedy", False),
 ("In what year did The Inbetweeners Movie come out?", 2011, "", 2, "easy", "Film", False),
 ("Roughly how many pet dogs are there in the UK, in millions?", 13, "million", 2, "medium", "Nature", False),
 ("Tish, the oldest goldfish on record, lived to what age?", 43, "years", 6, "hard", "Nature", True),
 ("How many bones are there in a horse's skeleton?", 205, "bones", 15, "hard", "Nature", False),
 ("Roughly how many whiskers does a cat have on its muzzle?", 24, "whiskers", 4, "medium", "Nature", False),
]
here = os.path.dirname(os.path.abspath(__file__))
out = [{"type": "nearest", "text": t, "answer": a, "unit": u, "spread": s, "difficulty": d, "category": c, "tags": ["nearest wins"] + (["wow"] if w else [])} for t, a, u, s, d, c, w in Q]
json.dump(out, open(os.path.join(here, '..', 'nearest-45.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'nearest written')
