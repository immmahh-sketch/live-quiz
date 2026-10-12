# Bank session 12 Oct 2026 (second pass): more 1% Club puzzles -> bank/club-28.json. Logic, number and wordplay, each with a one-line
# "why". Tested against every club puzzle in the live bank with lqsql/neardup.py (a copy of the server's near-duplicate
# rule: word overlap of 80%, or 50% with the same answer) before importing.
import json, os
PCTS = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 1]
OUT = []
def c(pct, cat, tags, text, answers, why):
    assert pct in PCTS, (text, pct)
    diff = "easy" if pct >= 70 else "medium" if pct >= 40 else "hard"
    OUT.append({"type": "club", "text": text, "answers": answers, "pct": pct, "why": why, "difficulty": diff, "category": cat, "tags": tags})

c(90, "Numbers", ["Metro", "money"], "A Metro ticket costs £2. How much do three tickets cost?", ["£6", "6", "Six pounds"], "3 × £2 = £6.")
c(70, "Logic", ["compass", "directions"], "You face north and turn right. Which way are you facing now?", ["East"], "A right turn from north points you east.")
c(60, "Words", ["backwards", "wordplay"], "Write STOP backwards, then put an S on the front. What word have you made?", ["Spots", "SPOTS"], "STOP backwards is POTS, and S in front makes SPOTS.")
c(50, "Numbers", ["square numbers"], "Which square number lies between 20 and 30?", ["25", "Twenty-five"], "4 × 4 = 16 and 6 × 6 = 36, so it's 5 × 5 = 25.")
c(40, "Numbers", ["football", "league points"], "A team wins 5, draws 3 and loses 2. With 3 points for a win and 1 for a draw, how many points have they got?", ["18", "Eighteen"], "5 × 3 = 15, plus 3 for the draws = 18.")
c(30, "Time", ["clocks", "subtracting"], "A clock is 10 minutes fast. It shows five to three. What's the real time?", ["2:45", "Quarter to three", "2.45", "14:45"], "Five to three, take away 10 minutes, is quarter to three.")
c(10, "Logic", ["chess", "squares"], "How many squares on a chessboard are not on its outside edge?", ["36", "Thirty-six"], "Take the outer ring away and a 6 × 6 square of 36 is left.")
c(5, "Numbers", ["digits", "reasoning"], "Which two-digit number is exactly three times the sum of its own digits?", ["27", "Twenty-seven"], "2 + 7 = 9, and 3 × 9 = 27. No other two-digit number works.")
c(1, "Numbers", ["square numbers", "reasoning"], "I'm a whole number over 10. Half of me is a square number, and so is twice me. What's the smallest I can be?", ["18", "Eighteen"], "Half of 18 is 9 (3 × 3) and double 18 is 36 (6 × 6). 8 also works, but it's under 10.")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'club-28.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'club puzzles written')
