# Bank session 10 Oct 2026: 19 more Nearest Wins questions -> bank/nearest-15.json: the North East, games and sport in numbers. Tested against the live bank with a copy of the server's near-duplicate rule first.
# (text, answer, unit, spread, difficulty, category, wow). Each was checked against the live bank's wording first.
import json, os
Q = [
 ("How many players are on the pitch altogether during a rugby union match, both sides counted?", 30, "players", 8, "easy", "Sport", False),
 ("How many times have Newcastle United been champions of England's top flight?", 4, "titles", 2, "hard", "North East England", False),
 ("The Great North Run goes from Newcastle to South Shields. How many miles is it, to one decimal place?", 13.1, "miles", 3, "easy", "North East England", False),
 ("Brendan Foster set up a half marathon from Newcastle to South Shields. When was the first one held?", 1981, "", 10, "medium", "North East England", False),
 ("The CBBC drama Byker Grove, filmed in Newcastle, began in which year?", 1989, "", 8, "hard", "North East England", False),
 ("Tower Bridge, London's famous lifting bridge, first opened to traffic in which year?", 1894, "", 25, "medium", "Landmarks", False),
 ("Roughly how fast did Concorde cruise, to the nearest 50 miles per hour?", 1350, "mph", 350, "hard", "Transport", True),
 ("Add up all the dots on an ordinary six-sided dice. What do you get?", 21, "dots", 6, "medium", "Games and toys", False),
 ("Add together every number on a roulette wheel, from 0 to 36. What's the total?", 666, "", 150, "hard", "Games and toys", True),
 ("How many numbered pockets are there on a European roulette wheel, counting the zero?", 37, "pockets", 8, "medium", "Games and toys", False),
 ("How many hurdles do the runners clear in a men's 110 metres hurdles race?", 10, "hurdles", 3, "medium", "Sport", False),
 ("How many arches carry Robert Stephenson's Royal Border Bridge over the Tweed at Berwick?", 28, "arches", 10, "hard", "North East England", True),
 ("How many points is a touchdown worth in American football, before the extra point?", 6, "points", 2, "medium", "Sport", False),
 ("Netball goals sit on top of posts. How tall are the posts, in feet?", 10, "feet", 3, "hard", "Sport", False),
 ("What is the heaviest a ten-pin bowling ball is allowed to be, in pounds?", 16, "lb", 5, "hard", "Sport", False),
 ("How many points is the Z tile worth in English Scrabble?", 10, "points", 3, "medium", "Games and toys", False),
 ("How much money does each player start with in UK Monopoly, in pounds?", 1500, "£", 400, "medium", "Games and toys", False),
 ("How many squares does a standard Snakes and Ladders board have?", 100, "squares", 25, "easy", "Games and toys", False),
 ("How many cards does each player get at the start of a game of Uno?", 7, "cards", 3, "medium", "Games and toys", False),
]
here = os.path.dirname(os.path.abspath(__file__))
out = [{"type": "nearest", "text": t, "answer": a, "unit": u, "spread": s, "difficulty": d, "category": c, "tags": ["nearest wins"] + (["wow"] if w else [])} for t, a, u, s, d, c, w in Q]
json.dump(out, open(os.path.join(here, '..', 'nearest-15.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'nearest written')
