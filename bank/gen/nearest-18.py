# Bank session 11 Oct 2026: more Nearest Wins questions -> bank/nearest-18.json: North East years, famous numbers, history and sport.
# (text, answer, unit, spread, difficulty, category, wow). Tested against the live bank with a copy of the server's near-duplicate rule first.
import json, os
Q = [
 ("In what year did Newcastle United last win the top-flight league title?", 1927, "", 10, "hard", "Football", True),
 ("In what year did the Sage Gateshead concert hall open?", 2004, "", 4, "hard", "North East England", False),
 ("How many cards are in a full tarot deck?", 78, "cards", 15, "hard", "Games and toys", True),
 ("In what year did the first iPhone go on sale?", 2007, "", 3, "medium", "Science and tech", False),
 ("How many stripes are on the flag of the United States?", 13, "stripes", 4, "medium", "World geography", False),
 ("How tall is Grey's Monument in Newcastle, in metres?", 41, "m", 10, "hard", "North East England", False),
 ("In what year did the Vikings raid the monastery on Lindisfarne?", 793, "", 40, "hard", "History", True),
 ("How many dots are there on a pair of standard dice, added together?", 42, "dots", 8, "medium", "Games and toys", True),
 ("How many grams does a 12-sided pound coin weigh?", 8.75, "g", 2, "hard", "Everyday life", True),
 ("Lewis Hamilton has been Formula One champion how many times?", 7, "titles", 2, "easy", "Sport", False),
 ("Wainwright's Coast to Coast walk, from St Bees to Robin Hood's Bay, is roughly how many miles?", 192, "miles", 40, "hard", "UK geography", False),
 ("How many Lake District fells did Alfred Wainwright describe in his famous guidebooks?", 214, "fells", 50, "hard", "UK geography", True),
 ("How many Scottish mountains over 3,000 feet are listed as Munros?", 282, "Munros", 60, "hard", "UK geography", True),
 ("How many players are on a Gaelic football team?", 15, "players", 3, "medium", "Sport", False),
 ("Emperor, king, Adélie, chinstrap and the rest: how many penguin species exist in all?", 18, "species", 5, "hard", "Animals", False),
]
here = os.path.dirname(os.path.abspath(__file__))
out = [{"type": "nearest", "text": t, "answer": a, "unit": u, "spread": s, "difficulty": d, "category": c, "tags": ["nearest wins"] + (["wow"] if w else [])} for t, a, u, s, d, c, w in Q]
json.dump(out, open(os.path.join(here, '..', 'nearest-18.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'nearest written')
