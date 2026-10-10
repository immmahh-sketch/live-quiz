# Bank session 10 Oct 2026: more Nearest Wins questions -> bank/nearest-13.json: islands, lakes, landmarks and sport in numbers.
# (text, answer, unit, spread, difficulty, category, wow). Each was checked against the live bank's wording first.
import json, os
Q = [
 ("The Lake District is full of meres, waters and tarns. How many of its lakes actually have 'Lake' in their name?", 1, "", 2, "hard", "UK geography", True),
 ("Indonesia is the world's biggest island country. Roughly how many islands does it have, to the nearest thousand?", 17000, "islands", 6000, "hard", "World geography", True),
 ("Finland is called 'the land of a thousand lakes', but roughly how many does it really have, to the nearest thousand?", 188000, "lakes", 80000, "hard", "World geography", True),
 ("Wales is said to have more castles for its size than anywhere in Europe. Roughly how many, to the nearest 100?", 600, "castles", 250, "medium", "Wales", True),
 ("Roughly how many pubs are there in the UK, to the nearest thousand?", 45000, "pubs", 15000, "medium", "Food and drink", False),
 ("Roughly how many million strawberries are eaten at Wimbledon each year?", 2, "million", 1.5, "medium", "Sport", False),
 ("Roughly how many million real Christmas trees are bought in the UK each year?", 7, "million", 3, "medium", "Christmas", False),
 ("Scotland has far more islands than most people guess. Roughly how many, to the nearest 10?", 790, "islands", 300, "hard", "Scotland", True),
 ("Sweden has more islands than any other country. Roughly how many, to the nearest thousand?", 267000, "islands", 100000, "hard", "World geography", True),
 ("Roughly how many countries are there in Europe?", 44, "countries", 8, "medium", "Europe", False),
 ("Bulgaria joined in January 2026. How many EU countries use the euro now?", 21, "countries", 5, "medium", "Europe", False),
 ("Counting every club ever promoted to it or that started in it, how many teams have now had a Premier League season (up to 2025-26)?", 51, "clubs", 12, "hard", "Football", False),
 ("How many clubs are there in the four divisions of the Premier League and Football League together?", 92, "clubs", 15, "easy", "Football", False),
 ("How many clubs make up the Scottish Professional Football League?", 42, "clubs", 10, "medium", "Football", False),
 ("Roughly how many athletes competed at the Paris 2024 Olympics, to the nearest 100?", 10500, "athletes", 3000, "medium", "Olympics", False),
 ("Louis XIV's Palace of Versailles is enormous. About how many rooms does it contain?", 2300, "rooms", 900, "hard", "Landmarks", False),
 ("How many mirrors line the Hall of Mirrors at Versailles?", 357, "mirrors", 150, "hard", "Landmarks", True),
 ("How many steps make up the Spanish Steps in Rome?", 135, "steps", 50, "medium", "Landmarks", False),
 ("Roughly how many soldiers are there in China's Terracotta Army, to the nearest 1,000?", 8000, "soldiers", 3000, "medium", "History", False),
 ("Roughly how many of the giant stone heads called moai stand on Easter Island, to the nearest 100?", 900, "moai", 350, "medium", "History", False),
 ("How many cards are there in a standard Uno deck?", 108, "cards", 30, "hard", "Games and toys", False),
 ("Roughly how many different species of bird have ever been recorded in Britain, to the nearest 10?", 630, "species", 200, "hard", "Nature", True),
 ("Roughly how many words are there in the King James Bible, to the nearest 10,000?", 783000, "words", 300000, "hard", "Religion", False),
 ("How many rooms are there in the White House?", 132, "rooms", 50, "medium", "Landmarks", False),
 ("The Maldives is a nation of coral atolls in the Indian Ocean. About how many islands is it made of?", 1190, "islands", 400, "hard", "World geography", True),
]
here = os.path.dirname(os.path.abspath(__file__))
out = [{"type": "nearest", "text": t, "answer": a, "unit": u, "spread": s, "difficulty": d, "category": c, "tags": ["nearest wins"] + (["wow"] if w else [])} for t, a, u, s, d, c, w in Q]
json.dump(out, open(os.path.join(here, '..', 'nearest-13.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'nearest written')
