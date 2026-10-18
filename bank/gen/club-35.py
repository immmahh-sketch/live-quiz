# Bank session 18 Oct 2026: more 1% Club puzzles -> bank/club-35.json. Logic, number and wordplay, each with a one-line
# "why" and short exact answers. Tested against every club puzzle in the live bank with lqsql/neardup.py (a copy of the
# server's near-duplicate rule) before importing; wording kept distinctive so a different puzzle isn't mistaken for an old one.
# Dropped as already in the bank: 100 days from Wednesday, digit 1 from 1 to 20, three cats and mice, spelt wrong in every
# dictionary, games in a 20-team league, edges of a cube, clock hands meeting in 12 hours.
import json, os
PCTS = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 1]
OUT = []
def c(pct, cat, tags, text, answers, why):
    assert pct in PCTS, (text, pct)
    diff = "easy" if pct >= 70 else "medium" if pct >= 40 else "hard"
    OUT.append({"type": "club", "text": text, "answers": answers, "pct": pct, "why": why, "difficulty": diff, "category": cat, "tags": tags})

c(70, "Sport", ["tennis", "scoring"], "A tennis player wins a game without losing a single point. How many points did they win?", ["4", "Four"], "15, 30, 40, game: four points.")
c(30, "Games and puzzles", ["Rubik's Cube", "counting"], "In a standard Rubik's Cube, how many of the small cubes show three coloured faces?", ["8", "Eight"], "Only the corner pieces show three colours, and a cube has 8 corners.")
c(10, "Games and puzzles", ["cake", "cutting", "lateral thinking"], "What's the fewest straight cuts that will divide a round cake into 8 equal pieces?", ["3", "Three"], "Two cuts across make 4 quarters; one cut through the middle, sideways, makes 8.")
c(50, "Games and puzzles", ["cards", "counting"], "In a standard 52-card pack, how many red cards show a jack, queen or king?", ["6", "Six"], "Two red suits, each with a jack, queen and king.")
c(40, "Wordplay", ["months", "letters"], "How many of the twelve months have the letter R in their name?", ["8", "Eight"], "January, February, March, April, September, October, November, December.")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'club-35.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'club puzzles written')
