# Bank session 11 Oct 2026: more 1% Club puzzles -> bank/club-21.json. Logic, number and wordplay, each with a one-line
# "why". Tested against every club puzzle in the live bank with lqsql/neardup.py (a copy of the server's near-duplicate
# rule: word overlap of 80%, or 50% with the same answer) before importing.
import json, os
PCTS = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 1]
OUT = []
def c(pct, cat, tags, text, answers, why):
    assert pct in PCTS, (text, pct)
    diff = "easy" if pct >= 70 else "medium" if pct >= 40 else "hard"
    OUT.append({"type": "club", "text": text, "answers": answers, "pct": pct, "why": why, "difficulty": diff, "category": cat, "tags": tags})

c(90, "Numbers", ["adding", "taking away"], "Six bottles of Brown Ale sit on a shelf. You drink two, then buy three more. How many are on the shelf now?", ["7", "Seven"], "6 − 2 + 3 = 7.")
c(70, "Numbers", ["money", "sausage rolls"], "Sausage rolls are 90p each. How many can you buy with a £5 note?", ["5", "Five"], "5 × 90p = £4.50, and a sixth would cost £5.40.")
c(60, "Numbers", ["quiz scores", "multiplying"], "A quiz has 8 rounds of 10 questions, and you get 7 right in every round. What's your total?", ["56", "Fifty-six"], "8 × 7 = 56.")
c(50, "Time", ["days of the week", "counting back"], "Quiz night is a Saturday. What day of the week was it ten days before?", ["Wednesday"], "Seven days back is Saturday again; three more is Wednesday.")
c(40, "Time", ["timetables", "trains"], "A Metro leaves every 12 minutes, starting at 7:00. At what time does the fifth one leave?", ["7:48", "7.48", "Twelve minutes to eight"], "7:00, 7:12, 7:24, 7:36, 7:48.")
c(1, "Numbers", ["coins", "combinations"], "Using only 1p, 2p and 5p pieces, count the different combinations totalling exactly 10p.", ["10", "Ten"], "With no 5p: 6 ways; with one 5p: 3 ways; with two 5p: 1 way.")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'club-21.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'club puzzles written')
