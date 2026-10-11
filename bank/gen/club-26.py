# Bank session 11 Oct 2026: more 1% Club puzzles -> bank/club-24.json. Logic, number and wordplay, each with a one-line
# "why". Tested against every club puzzle in the live bank with lqsql/neardup.py (a copy of the server's near-duplicate
# rule: word overlap of 80%, or 50% with the same answer) before importing.
import json, os
PCTS = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 1]
OUT = []
def c(pct, cat, tags, text, answers, why):
    assert pct in PCTS, (text, pct)
    diff = "easy" if pct >= 70 else "medium" if pct >= 40 else "hard"
    OUT.append({"type": "club", "text": text, "answers": answers, "pct": pct, "why": why, "difficulty": diff, "category": cat, "tags": tags})

c(90, "Numbers", ["football", "adding"], "A football match finishes 3–2. How many goals were scored in total?", ["5", "Five"], "3 + 2 = 5.")
c(60, "Numbers", ["parking", "money"], "A car park charges £1.50 an hour. What do you pay for four hours?", ["£6", "6", "Six pounds"], "4 × £1.50 = £6.")
c(50, "Logic", ["outfits", "combinations"], "You pack 3 shirts and 2 pairs of trousers. How many different outfits can you make?", ["6", "Six"], "Each shirt goes with either pair: 3 × 2 = 6.")
c(40, "Numbers", ["darts", "even numbers"], "A dartboard has the numbers 1 to 20 round it. How many of them are even?", ["10", "Ten"], "Half of the twenty numbers are even.")
c(30, "Time", ["Metro", "dividing"], "A Metro comes every 6 minutes. How many arrive in an hour?", ["10", "Ten"], "60 ÷ 6 = 10.")
c(10, "Time", ["holidays", "calendar"], "You fly out on Friday 28 March and come home 10 nights later. What day of the week do you get back?", ["Monday"], "Seven nights takes you to Friday 4 April; three more make it Monday 7 April.")
c(1, "Logic", ["bouncing", "halving"], "A ball dropped from 16 m bounces back to half its height every time. How far has it travelled when it hits the ground for the third time?", ["40 m", "40", "Forty metres"], "16 down, 8 up and 8 down, 4 up and 4 down: 40 m.")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'club-24.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'club puzzles written')
