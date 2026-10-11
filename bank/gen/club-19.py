# Bank session 11 Oct 2026: more 1% Club puzzles -> bank/club-17.json. Logic, number and wordplay, each with a one-line
# "why". Tested against every club puzzle in the live bank with lqsql/neardup.py (a copy of the server's near-duplicate
# rule: word overlap of 80%, or 50% with the same answer) before importing.
import json, os
PCTS = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 1]
OUT = []
def c(pct, cat, tags, text, answers, why):
    assert pct in PCTS, (text, pct)
    diff = "easy" if pct >= 70 else "medium" if pct >= 40 else "hard"
    OUT.append({"type": "club", "text": text, "answers": answers, "pct": pct, "why": why, "difficulty": diff, "category": cat, "tags": tags})

c(90, "Numbers", ["tricycles", "wheels"], "Three tricycles are parked outside a nursery. How many wheels altogether?", ["9", "Nine"], "3 wheels each, 3 × 3 = 9.")
c(80, "Logic", ["odd one out", "days and months"], "Odd one out: Tuesday, Thursday, March, Saturday.", ["March"], "March is a month; the rest are days.")
c(70, "Numbers", ["knitting", "multiplying"], "Grandma knits 3 scarves a week. How many has she made after 4 weeks?", ["12", "Twelve"], "3 × 4 = 12.")
c(60, "Sport", ["cricket", "wickets"], "A cricket side of 11 has lost 4 wickets. How many of its batters are not yet out?", ["7", "Seven"], "11 − 4 = 7, counting the two at the crease.")
c(50, "Logic", ["queues", "position"], "In a bakery queue, Ellie is 5th from the front and 5th from the back. How many people are queuing?", ["9", "Nine"], "4 ahead of her, 4 behind her, plus Ellie.")
c(40, "Numbers", ["primes", "odd one out"], "Spot the number that isn't prime: 2, 3, 5, 9, 11.", ["9", "Nine"], "The others are prime; 9 is 3 × 3.")
c(20, "Logic", ["lifts", "dividing"], "A lift takes at most 8 people. What's the fewest trips needed to carry 30 people up?", ["4", "Four"], "Three trips carry 24; the last 6 need a fourth.")

c(20, "Numbers", ["shapes", "sides"], "How many sides do a hexagon and an octagon have between them?", ["14", "Fourteen"], "6 + 8 = 14.")
c(10, "Logic", ["sheep", "trick questions"], "A farmer has 17 sheep. All but 9 run off. How many does he still have?", ["9", "Nine"], "'All but 9' means 9 stay behind.")
c(1, "Logic", ["tides", "ships"], "A rope ladder hangs over a moored ship's side, with 4 rungs above the water. The tide rises a metre. How many rungs are above water now?", ["4", "Four"], "The ship floats up with the tide, and the ladder with it.")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'club-17.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'club puzzles written')
