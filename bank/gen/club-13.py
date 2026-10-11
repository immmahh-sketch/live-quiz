# Bank session 11 Oct 2026: more 1% Club puzzles -> bank/club-11.json. Logic, number and wordplay, each with a one-line
# "why". Tested against every club puzzle in the live bank with lqsql/neardup.py (a copy of the server's near-duplicate
# rule: word overlap of 80%, or 50% with the same answer) before importing.
import json, os
PCTS = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 1]
OUT = []
def c(pct, cat, tags, text, answers, why):
    assert pct in PCTS, (text, pct)
    diff = "easy" if pct >= 70 else "medium" if pct >= 40 else "hard"
    OUT.append({"type": "club", "text": text, "answers": answers, "pct": pct, "why": why, "difficulty": diff, "category": cat, "tags": tags})

c(90, "Numbers", ["wheels", "adding"], "Two bicycles and a tricycle are parked outside. How many wheels in all?", ["7", "Seven"], "2 + 2 + 3 = 7.")
c(70, "Numbers", ["measuring", "comparing"], "Which is longer: 2 metres, or 150 centimetres?", ["2 metres", "2m", "Two metres"], "2 metres is 200 centimetres.")
c(60, "Logic", ["days", "calendar"], "If today is Wednesday, what day was it ten days ago?", ["Sunday"], "Seven days ago was Wednesday; three more back is Sunday.")
c(60, "Numbers", ["fractions", "pizza"], "Three whole pizzas are each cut into quarters. How many slices?", ["12", "Twelve"], "3 × 4 = 12.")
c(50, "Numbers", ["doubling", "halving"], "Double 35, halve 50, then add the two answers together.", ["95", "Ninety-five"], "70 + 25 = 95.")
c(50, "Logic", ["odd one out", "animals"], "Which is the odd one out: CAT, DOG, COW, OWL?", ["Owl", "OWL"], "The owl is a bird; the others are mammals.")
c(40, "Numbers", ["money", "logic"], "A pencil costs 30p more than a rubber, and together they cost 50p. What does the rubber cost?", ["10p", "10 pence", "Ten pence"], "Rubber 10p, pencil 40p: 40 is 30 more than 10, and they add to 50.")
c(20, "Numbers", ["adding", "multiplying"], "Which number do you get both by adding 1, 2 and 3 together and by multiplying them?", ["6", "Six"], "1 + 2 + 3 = 6 and 1 × 2 × 3 = 6.")

c(60, "Numbers", ["time", "films"], "A film starts at 7:40pm and runs for 1 hour 50 minutes. When does it finish?", ["9:30pm", "9.30pm", "9:30", "Half past nine"], "7:40 plus 2 hours is 9:40; take off 10 minutes: 9:30.")
c(40, "Numbers", ["shapes", "corners"], "Count the corners on three squares and two triangles together.", ["18", "Eighteen"], "3 × 4 = 12 and 2 × 3 = 6: 18 in all.")
c(10, "Numbers", ["doubling"], "Which whole number is exactly double the whole number just before it?", ["2", "Two"], "2 is double 1; for any bigger number, double the one before is too big.")
c(1, "Numbers", ["adding", "patterns"], "Add up every whole number from 1 to 20.", ["210", "Two hundred and ten"], "Pair them up: 1 + 20, 2 + 19 and so on gives ten pairs of 21.")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'club-11.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'club puzzles written')
