# Bank session 11 Oct 2026: more 1% Club puzzles -> bank/club-10.json. Logic, number and wordplay, each with a one-line
# "why". Tested against every club puzzle in the live bank with lqsql/neardup.py (a copy of the server's near-duplicate
# rule: word overlap of 80%, or 50% with the same answer) before importing.
import json, os
PCTS = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 1]
OUT = []
def c(pct, cat, tags, text, answers, why):
    assert pct in PCTS, (text, pct)
    diff = "easy" if pct >= 70 else "medium" if pct >= 40 else "hard"
    OUT.append({"type": "club", "text": text, "answers": answers, "pct": pct, "why": why, "difficulty": diff, "category": cat, "tags": tags})

c(90, "Numbers", ["eggs", "taking away"], "A farmer carries 12 eggs and drops 3, which smash. How many are still whole?", ["9", "Nine"], "12 − 3 = 9.")
c(90, "Logic", ["legs", "animals"], "Three hens and one dog are in a yard. How many legs between them?", ["10", "Ten"], "Three hens have 6 legs and the dog has 4.")
c(80, "Numbers", ["halving"], "Halve 40, then halve it again. What's left?", ["10", "Ten"], "40 → 20 → 10.")
c(70, "Numbers", ["time", "trains"], "Your bus sets off at 10:45 and the ride lasts 50 minutes. When do you get off?", ["11:35", "11.35", "11:35am", "Twenty-five to twelve"], "10:45 plus 15 minutes is 11:00, plus 35 more is 11:35.")
c(70, "Numbers", ["fractions", "comparing"], "Which is bigger: three quarters, or two thirds?", ["Three quarters", "3/4"], "Three quarters is 9/12; two thirds is only 8/12.")
c(60, "Numbers", ["time", "days"], "Six hours is a quarter of a day. How many minutes is that?", ["360", "Three hundred and sixty"], "A quarter of a day is 6 hours, and 6 × 60 = 360.")
c(60, "Wordplay", ["anagrams", "stationery"], "Unscramble LIPNCE to find something you write with.", ["Pencil"], "L-I-P-N-C-E rearranges to PENCIL.")
c(30, "Numbers", ["think of a number"], "Pick any starting figure. Double it, add 6, halve the result, then subtract your starting figure. What remains, whatever you picked?", ["3", "Three"], "Doubling then halving cancels out, leaving just half of the 6.")
c(20, "Numbers", ["primes", "odd one out"], "Spot the one that is not prime: 2, 3, 5, 9, 11, 13.", ["9", "Nine"], "All the others are prime numbers; 9 is 3 × 3.")
c(10, "Numbers", ["speed", "averages"], "You drive 60 miles at 30 mph, then 60 miles back at 60 mph. What's your average speed for the whole trip, in mph?", ["40", "40 mph", "Forty"], "120 miles in 3 hours (2 there, 1 back) is 40 mph, not 45.")
c(5, "Logic", ["handshakes", "parties"], "At a party, everyone shakes hands with everyone else once, and there are 28 handshakes. How many people are there?", ["8", "Eight"], "8 people each shake 7 hands: 8 × 7 ÷ 2 = 28.")

c(80, "Numbers", ["coins", "money"], "How many 2p coins make up £3?", ["150", "One hundred and fifty"], "£3 is 300p, and 300 ÷ 2 = 150.")
c(50, "Logic", ["buses", "working backwards"], "15 people get off a bus and 10 get on, leaving 25 aboard. How many were on to start with?", ["30", "Thirty"], "Work backwards: 25 − 10 + 15 = 30.")
c(20, "Numbers", ["percentages", "sales"], "A £20 shirt is cut by 10%, then cut by 10% again. What does it cost now?", ["£16.20", "16.20", "£16.20p"], "£20 → £18 → £16.20; the second cut is 10% of £18, not of £20.")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'club-10.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'club puzzles written')
