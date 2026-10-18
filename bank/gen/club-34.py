# Bank session 18 Oct 2026: more 1% Club puzzles -> bank/club-34.json. Logic, number and wordplay, each with a one-line
# "why" and short exact answers. Tested against every club puzzle in the live bank with lqsql/neardup.py (a copy of the
# server's near-duplicate rule) before importing; wording kept distinctive so a different puzzle isn't mistaken for an old one.
# Dropped as already in the bank: NEW DOOR, knockout-match counts, wine glasses per bottle, E's in one to ten.
import json, os
PCTS = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 1]
OUT = []
def c(pct, cat, tags, text, answers, why):
    assert pct in PCTS, (text, pct)
    diff = "easy" if pct >= 70 else "medium" if pct >= 40 else "hard"
    OUT.append({"type": "club", "text": text, "answers": answers, "pct": pct, "why": why, "difficulty": diff, "category": cat, "tags": tags})

c(10, "Wordplay", ["months", "alphabet"], "How many letters of the alphabet appear in none of the twelve months' names?", ["5", "Five"], "Only K, Q, W, X and Z are missing from January to December.")
c(50, "Numbers", ["cards", "dividing"], "Deal a full 52-card pack out equally to 5 players. How many cards are left over?", ["2", "Two"], "5 × 10 = 50, leaving 2.")
c(60, "Time", ["clocks", "minutes"], "How many minutes after midnight is 2:15am?", ["135", "135 minutes"], "Two hours is 120 minutes, plus 15.")
c(40, "Time", ["calendars", "Sundays"], "What's the most Sundays there can be in one calendar year?", ["53", "Fifty-three"], "52 weeks plus one or two spare days: if one of those is a Sunday, there are 53.")
c(50, "Games and puzzles", ["noughts and crosses", "counting"], "In noughts and crosses, how many different straight lines of three can win the game?", ["8", "Eight"], "3 rows, 3 columns and 2 diagonals.")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'club-34.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'club puzzles written')
