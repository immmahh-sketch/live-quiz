# Bank session 18 Oct 2026: more 1% Club puzzles -> bank/club-32.json. Logic, number and wordplay, each with a one-line
# "why" and short exact answers. Tested against every club puzzle in the live bank with lqsql/neardup.py (a copy of the
# server's near-duplicate rule) before importing; wording kept distinctive so a different puzzle isn't mistaken for an old one.
# Dropped as already in the bank: the months with the shortest and longest names.
import json, os
PCTS = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 1]
OUT = []
def c(pct, cat, tags, text, answers, why):
    assert pct in PCTS, (text, pct)
    diff = "easy" if pct >= 70 else "medium" if pct >= 40 else "hard"
    OUT.append({"type": "club", "text": text, "answers": answers, "pct": pct, "why": why, "difficulty": diff, "category": cat, "tags": tags})

c(60, "Wordplay", ["palindromes"], "Spell the five-letter palindrome meaning flat and even.", ["Level"], "L-E-V-E-L is the same both ways.")
c(50, "Wordplay", ["days", "letters"], "Of Monday to Sunday, which day's name has the most letters?", ["Wednesday"], "Wednesday has nine letters; Thursday and Saturday have eight.")
c(50, "Numbers", ["sudoku", "adding"], "A Sudoku row holds each digit from 1 to 9 once. What does the row add up to?", ["45", "Forty-five"], "1 + 2 + … + 9 = 45.")
c(40, "Time", ["timetables", "ferries"], "A ferry leaves at 6:00am and then every 40 minutes. When does the fifth ferry leave?", ["8:40am", "8:40", "8.40", "08:40"], "6:00, 6:40, 7:20, 8:00, 8:40.")
c(30, "Numbers", ["digits", "multiplying", "trick"], "Multiply together the four digits of the year 2026. What do you get?", ["0", "Zero", "Nothing"], "One of the digits is 0, so the answer is 0.")
c(20, "Money", ["coins", "change"], "Pay exactly £1.99 using as few UK coins as possible. How many coins is that?", ["7", "Seven"], "£1 + 50p + 20p + 20p + 5p + 2p + 2p = £1.99.")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'club-32.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'club puzzles written')
