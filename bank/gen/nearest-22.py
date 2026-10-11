# Bank session 11 Oct 2026: more Nearest Wins questions -> bank/nearest-22.json: TV, film and sporting tallies.
# (text, answer, unit, spread, difficulty, category, wow). Tested against the live bank with a copy of the server's near-duplicate rule first.
import json, os
Q = [
 ("How many episodes of Friends were made?", 236, "episodes", 40, "hard", "TV", True),
 ("How many top-flight titles have Liverpool won, up to 2025?", 20, "titles", 3, "medium", "Football", False),
 ("Counting old First Division wins too, how many English league titles have Manchester United won?", 20, "titles", 3, "medium", "Football", False),
 ("How many FA Cups have Arsenal won, a record?", 14, "cups", 3, "medium", "Football", False),
 ("West Germany included, how many times have Germany lifted the men's World Cup?", 4, "World Cups", 1, "medium", "Football", False),
 ("How many Wimbledon singles titles did Martina Navratilova win?", 9, "titles", 2, "medium", "Sport", False),
 ("How many times did Chris Froome win the Tour de France?", 4, "wins", 1, "medium", "Sport", False),
 ("How many UK number ones did Elvis Presley have?", 21, "number ones", 5, "hard", "Music", False),
 ("How many Olympic gold medals did Sir Chris Hoy win?", 6, "golds", 2, "medium", "Sport", False),
]
here = os.path.dirname(os.path.abspath(__file__))
out = [{"type": "nearest", "text": t, "answer": a, "unit": u, "spread": s, "difficulty": d, "category": c, "tags": ["nearest wins"] + (["wow"] if w else [])} for t, a, u, s, d, c, w in Q]
json.dump(out, open(os.path.join(here, '..', 'nearest-22.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'nearest written')
