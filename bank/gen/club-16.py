# Bank session 11 Oct 2026: more 1% Club puzzles -> bank/club-14.json. Logic, number and wordplay, each with a one-line
# "why". Tested against every club puzzle in the live bank with lqsql/neardup.py (a copy of the server's near-duplicate
# rule: word overlap of 80%, or 50% with the same answer) before importing.
import json, os
PCTS = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 1]
OUT = []
def c(pct, cat, tags, text, answers, why):
    assert pct in PCTS, (text, pct)
    diff = "easy" if pct >= 70 else "medium" if pct >= 40 else "hard"
    OUT.append({"type": "club", "text": text, "answers": answers, "pct": pct, "why": why, "difficulty": diff, "category": cat, "tags": tags})

c(80, "Wordplay", ["backwards", "kitchen"], "Read TOP from right to left. Which kitchen item do you get?", ["Pot", "POT"], "T-O-P reversed is P-O-T.")
c(70, "Wordplay", ["letters", "counting"], "Count the letters in the word ELEPHANT.", ["8", "Eight"], "E-L-E-P-H-A-N-T.")
c(60, "Numbers", ["squares", "adding"], "Square 3, square 4, and add the results.", ["25", "Twenty-five"], "9 + 16 = 25.")
c(40, "Numbers", ["patterns", "squares"], "Fill the gap in this run of squares: 1, 4, ?, 16, 25.", ["9", "Nine"], "They're square numbers: 1, 4, 9, 16, 25.")
c(30, "Numbers", ["primes"], "Spot the prime among 21, 27, 29 and 33.", ["29", "Twenty-nine"], "21 = 3 × 7, 27 = 3 × 9, 33 = 3 × 11, but 29 has no factors.")
c(30, "Numbers", ["halving", "doubling"], "Half of a number is 18. What is that number doubled?", ["72", "Seventy-two"], "The number is 36, and double 36 is 72.")
c(20, "Logic", ["days"], "Monday is two days after which day?", ["Saturday"], "Saturday, Sunday, Monday.")
c(10, "Numbers", ["chess", "squares"], "On a chess board, how many light-coloured squares are there?", ["32", "Thirty-two"], "Half of the 64.")
c(5, "Logic", ["patterns", "trick"], "If 1 = 5, 2 = 25, 3 = 125 and 4 = 625, what does 5 equal?", ["1", "One"], "The very first line says 1 = 5, so 5 = 1.")
c(5, "Numbers", ["shapes", "angles"], "Add up all the inside angles of a hexagon. How many degrees is that?", ["720", "720 degrees", "Seven hundred and twenty"], "A hexagon splits into four triangles: 4 × 180 = 720.")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'club-14.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'club puzzles written')
