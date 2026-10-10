# Bank session 10 Oct 2026: more Nearest Wins questions -> bank/nearest-6.json.
# (text, answer, unit, spread, difficulty, category, wow). Each was checked against the live bank's wording first.
import json, os
Q = [
 ("Wayne Rooney scored his first Premier League goal against Arsenal in 2002. How old was he?", 16, "years old", 5, "medium", "Football", False),
 ("How many goals did Wayne Rooney score for England?", 53, "goals", 20, "medium", "Football", False),
 ("Concorde made its last ever commercial flight in which year?", 2003, "", 10, "medium", "Science and technology", False),
 ("Papua New Guinea has more languages than any other country. Roughly how many, to the nearest 100?", 840, "languages", 400, "hard", "Words and language", True),
 ("How many species of penguin are there, by the most common count?", 18, "species", 8, "hard", "Animals", False),
 ("The world's first cash machine was opened by Barclays in Enfield in which year?", 1967, "", 20, "hard", "Science and technology", True),
 ("Tim Berners-Lee put the world's first website online in which year?", 1991, "", 10, "medium", "Science and technology", False),
 ("YouTube was launched in which year?", 2005, "", 6, "easy", "Science and technology", False),
 ("The Football League, the world's oldest, was founded in which year?", 1888, "", 30, "hard", "Football", False),
 ("Tickets for the very first Glastonbury Festival cost £1. Roughly how many people went, to the nearest 500?", 1500, "people", 2000, "hard", "Music", True),
 ("A Rubik's Cube can be scrambled into how many quintillion different positions?", 43, "quintillion", 40, "hard", "Games and toys", True),
 ("A blue whale's heart is the biggest of any animal. Roughly how much does it weigh, in kilograms?", 180, "kg", 150, "hard", "Animals", True),
 ("How many Ballon d'Or awards had Lionel Messi won, up to 2025?", 8, "awards", 5, "easy", "Football", False),
 ("How many men's World Cups had Brazil won, up to 2022?", 5, "World Cups", 3, "easy", "Football", False),
 ("Newcastle United last won the FA Cup in which year?", 1955, "", 30, "medium", "The North East of England", False),
 ("Newcastle United beat Liverpool at Wembley to win the League Cup in which year?", 2025, "", 15, "medium", "The North East of England", True),
 ("Newcastle United won the Inter-Cities Fairs Cup, beating Újpest, in which year?", 1969, "", 20, "hard", "The North East of England", False),
 ("Sunderland won the Championship play-off final at Wembley to return to the Premier League in which year?", 2025, "", 8, "medium", "The North East of England", False),
 ("How many locks are there on the Caledonian Canal, from Inverness to Fort William?", 29, "locks", 15, "hard", "Scotland", False),
 ("Neptune's Staircase near Fort William is Britain's longest flight of locks. How many locks does it have?", 8, "locks", 5, "hard", "Scotland", False),
 ("The Leeds and Liverpool Canal is the longest single canal in Britain. Roughly how many miles long is it?", 127, "miles", 60, "hard", "Britain", False),
 ("The Humber Bridge's main span was once the longest in the world. How long is it, to the nearest 10 metres?", 1410, "metres", 600, "hard", "Britain", False),
 ("Roughly how many people were on board the Titanic when she sank, to the nearest 100?", 2200, "people", 1000, "medium", "History", False),
 ("How many lifeboats did the Titanic carry?", 20, "lifeboats", 15, "medium", "History", True),
 ("How many children did Queen Victoria have?", 9, "children", 6, "medium", "The royal family", False),
]
here = os.path.dirname(os.path.abspath(__file__))
out = [{"type": "nearest", "text": t, "answer": a, "unit": u, "spread": s, "difficulty": d, "category": c, "tags": ["nearest wins"] + (["wow"] if w else [])} for t, a, u, s, d, c, w in Q]
json.dump(out, open(os.path.join(here, '..', 'nearest-6.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'nearest written')
