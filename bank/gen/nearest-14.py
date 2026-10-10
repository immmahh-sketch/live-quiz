# Bank session 10 Oct 2026: more Nearest Wins questions -> bank/nearest-14.json: sport and games in numbers.
# (text, answer, unit, spread, difficulty, category, wow). Each was checked against the live bank's wording first.
import json, os
Q = [
 ("Roughly how many tennis balls are used at Wimbledon each year, to the nearest thousand?", 55000, "balls", 20000, "medium", "Sport", True),
 ("How many players make up a rugby union match-day squad, counting the replacements?", 23, "players", 6, "hard", "Sport", False),
 ("Roughly how many people can Lord's cricket ground hold, to the nearest thousand?", 31000, "people", 8000, "hard", "Sport", False),
 ("A cricket bat can be no longer than how many inches?", 38, "inches", 8, "hard", "Sport", False),
 ("Roughly how far do the riders cover in a whole Tour de France, to the nearest 100 kilometres?", 3400, "km", 1000, "hard", "Sport", False),
 ("The fastest serve ever hit at Wimbledon was in 2010. How fast was it, to the nearest mile per hour?", 148, "mph", 15, "hard", "Sport", False),
 ("Javier Sotomayor's high jump world record has stood since 1993. How high is it, in metres, to two decimal places?", 2.45, "m", 0.2, "hard", "Sport", True),
 ("Roughly how tall is each letter of the Hollywood sign, in metres?", 14, "m", 6, "medium", "Film", False),
 ("Roughly how many stars are there on the Hollywood Walk of Fame, to the nearest hundred?", 2800, "stars", 900, "hard", "Film", False),
 ("How many little green houses come in a standard Monopoly set?", 32, "houses", 10, "hard", "Games and toys", False),
 ("How many red hotels come in a standard Monopoly set?", 12, "hotels", 5, "hard", "Games and toys", False),
 ("How many pieces are there in a full chess set, both colours together?", 32, "pieces", 8, "easy", "Games and toys", False),
 ("UK pool is played with reds and yellows. Counting the black and the white too, how many balls is that?", 16, "balls", 4, "medium", "Games and toys", False),
 ("Roughly how much does a full-size football weigh, in grams?", 430, "g", 120, "hard", "Football", False),
 ("At a free kick, how many yards away must the wall stand?", 10, "yards", 4, "medium", "Football", False),
 ("How high is a full-size football goal, in feet?", 8, "feet", 3, "medium", "Football", False),
 ("Measure a full-size football goal from post to post. How many feet is it?", 24, "feet", 8, "medium", "Football", False),
 ("Roughly how much did a Paris 2024 Olympic gold medal weigh, in grams?", 529, "g", 200, "hard", "Olympics", True),
 ("Since 2024, what is the most horses allowed to start the Grand National?", 34, "horses", 8, "hard", "Sport", False),
 ("The 2025 London Marathon set a world record for finishers. Roughly how many crossed the line, to the nearest thousand?", 56000, "runners", 15000, "hard", "Sport", True),
 ("How many laps is the Monaco Grand Prix?", 78, "laps", 20, "hard", "Sport", False),
 ("The fastest speed ever recorded by a Formula One car in a race weekend is about how many miles per hour?", 231, "mph", 40, "hard", "Sport", False),
 ("How high is the bullseye from the floor on a standard dartboard, in centimetres?", 173, "cm", 40, "hard", "Sport", False),
 ("A golf ball can weigh no more than roughly how many grams?", 46, "g", 15, "hard", "Sport", False),
]
here = os.path.dirname(os.path.abspath(__file__))
out = [{"type": "nearest", "text": t, "answer": a, "unit": u, "spread": s, "difficulty": d, "category": c, "tags": ["nearest wins"] + (["wow"] if w else [])} for t, a, u, s, d, c, w in Q]
json.dump(out, open(os.path.join(here, '..', 'nearest-14.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'nearest written')
