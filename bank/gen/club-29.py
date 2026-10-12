# Bank session 12 Oct 2026 (third pass): more 1% Club puzzles -> bank/club-29.json. Logic, number and wordplay, each with a one-line
# "why". Tested against every club puzzle in the live bank with lqsql/neardup.py (a copy of the server's near-duplicate
# rule: word overlap of 80%, or 50% with the same answer) before importing.
import json, os
PCTS = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 1]
OUT = []
def c(pct, cat, tags, text, answers, why):
    assert pct in PCTS, (text, pct)
    diff = "easy" if pct >= 70 else "medium" if pct >= 40 else "hard"
    OUT.append({"type": "club", "text": text, "answers": answers, "pct": pct, "why": why, "difficulty": diff, "category": cat, "tags": tags})

c(80, "Numbers", ["counting", "fives"], "Count up in fives starting from 5. What is the eighth number you say?", ["40", "Forty"], "5, 10, 15, 20, 25, 30, 35, 40.")
c(70, "Numbers", ["eggs", "dozens"], "You buy a dozen eggs and then half a dozen more. How many eggs have you got?", ["18", "Eighteen"], "12 + 6 = 18.")
c(60, "Numbers", ["curling", "teams"], "A curling team has four players. How many players take part in a game between two teams?", ["8", "Eight"], "4 × 2 = 8.")
c(40, "Time", ["dates", "America"], "Americans write the month first. What date do they mean by 10/12?", ["12 October", "October 12", "12th October"], "Month 10 is October, and the day is the 12th.")
c(30, "Time", ["films", "adding time"], "A film starts at 7:45pm and lasts 1 hour 50 minutes. What time does it finish?", ["9:35pm", "9:35", "9.35", "21:35"], "7:45 + 1 hour = 8:45, + 50 minutes = 9:35.")
c(30, "Numbers", ["fractions", "school"], "Two thirds of a class of 30 are girls. How many boys are there?", ["10", "Ten"], "Two thirds of 30 is 20 girls, leaving 10 boys.")
c(20, "Numbers", ["coins", "money"], "What is the fewest UK coins you need to make exactly 99p?", ["6", "Six"], "50p + 20p + 20p + 5p + 2p + 2p.")
c(10, "Time", ["midnight", "minutes"], "How many minutes are there from 11:45pm to 1:15am?", ["90", "Ninety"], "15 minutes to midnight, then 75 more to 1:15: 90 minutes.")
c(5, "Time", ["calendar", "days"], "Today is Sunday. What day of the week was it 1,000 days ago?", ["Monday"], "1,000 days is 142 weeks and 6 days, and six days before a Sunday is a Monday.")
c(1, "Numbers", ["digits", "reasoning"], "Which whole number is exactly twice the sum of its own digits?", ["18", "Eighteen"], "1 + 8 = 9, and 2 × 9 = 18. No other whole number (above zero) works.")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'club-29.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'club puzzles written')
