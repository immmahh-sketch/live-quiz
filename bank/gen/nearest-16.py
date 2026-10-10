# Bank session 10 Oct 2026: more Nearest Wins questions -> bank/nearest-16.json: measures, animals and sport in numbers.
# (text, answer, unit, spread, difficulty, category, wow). Tested against the live bank with a copy of the server's near-duplicate rule first.
import json, os
Q = [
 ("A UK gallon holds roughly how many litres, to one decimal place?", 4.5, "litres", 1.5, "medium", "Everyday life", False),
 ("A mile is how many feet long?", 5280, "feet", 1500, "hard", "Everyday life", False),
 ("Roughly how much blood do you give at one blood donation session, in millilitres?", 470, "ml", 150, "hard", "Science", False),
 ("How many days does a hen's egg take to hatch?", 21, "days", 7, "medium", "Animals", False),
 ("How many teeth does an adult cat have?", 30, "teeth", 8, "hard", "Animals", False),
 ("Counting front and back paws, how many toes does a typical cat have?", 18, "toes", 5, "hard", "Animals", True),
 ("Roughly how fast can a racehorse gallop, in miles per hour?", 40, "mph", 12, "medium", "Animals", False),
 ("How many panels made up the classic black-and-white football?", 32, "panels", 10, "hard", "Football", False),
 ("How many feathers go into a top-quality badminton shuttlecock?", 16, "feathers", 5, "hard", "Sport", False),
 ("How long is a ten-pin bowling lane from the foul line to the head pin, in feet?", 60, "feet", 15, "hard", "Sport", False),
 ("How heavy is the shot thrown by men at the Olympics, to the nearest kilogram?", 7, "kg", 3, "hard", "Olympics", False),
 ("How many scoring rings are there on an Olympic archery target?", 10, "rings", 3, "medium", "Olympics", False),
 ("In water polo, how many swimmers per side are in the pool, goalkeeper included?", 7, "players", 2, "medium", "Sport", False),
 ("How many minutes long is each quarter of an NBA basketball game?", 12, "minutes", 4, "hard", "Sport", False),
 ("How many points is a try worth in rugby league?", 4, "points", 1, "medium", "Sport", False),
 ("In what year did women first compete at the modern Olympic Games?", 1900, "", 20, "hard", "Olympics", True),
 ("A full game of croquet is played through how many hoops on the lawn?", 6, "hoops", 2, "hard", "Sport", False),
 ("How many riders make up a polo team on horseback?", 4, "riders", 2, "hard", "Sport", False),
 ("How many points is a field goal worth in American football?", 3, "points", 1, "medium", "Sport", False),
 ("How tall is a table tennis net, to the nearest centimetre?", 15, "cm", 5, "hard", "Sport", False),
 ("Add up every spot on every tile in a double-six domino set. What's the total?", 168, "spots", 50, "hard", "Games and toys", True),
]
here = os.path.dirname(os.path.abspath(__file__))
out = [{"type": "nearest", "text": t, "answer": a, "unit": u, "spread": s, "difficulty": d, "category": c, "tags": ["nearest wins"] + (["wow"] if w else [])} for t, a, u, s, d, c, w in Q]
json.dump(out, open(os.path.join(here, '..', 'nearest-16.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'nearest written')
