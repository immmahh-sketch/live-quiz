# Bank session 18 Oct 2026: more 1% Club puzzles -> bank/club-30.json. Logic, number and wordplay, each with a one-line
# "why" and short exact answers (the warm-up marks typed answers by fuzzy match). Tested against every club puzzle in the
# live bank with lqsql/neardup.py (a copy of the server's near-duplicate rule) before importing. A first draft (tea- and butter-
# words, months with 28 days, day after tomorrow, the digit 1 from 1 to 20, the 3:15 clock angle) was already there, so it was replaced;
# a second round lost 2p coins in £3, the 30p two-coin riddle and the self-describing answer the same way,
# and a third lost ten per cent of ten per cent and minutes in a quarter of a day.
import json, os
PCTS = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 1]
OUT = []
def c(pct, cat, tags, text, answers, why):
    assert pct in PCTS, (text, pct)
    diff = "easy" if pct >= 70 else "medium" if pct >= 40 else "hard"
    OUT.append({"type": "club", "text": text, "answers": answers, "pct": pct, "why": why, "difficulty": diff, "category": cat, "tags": tags})

c(70, "Wordplay", ["vowels", "North East"], "How many of the letters in NEWCASTLE are vowels?", ["3", "Three"], "E, A and E: three vowels in nine letters.")
c(40, "Money", ["coins", "change"], "What is the smallest number of UK coins that add up to exactly 87p?", ["5", "Five"], "50p + 20p + 10p + 5p + 2p = 87p.")
c(60, "Numbers", ["square numbers", "odd one out"], "Four of these numbers are square numbers and one is not: 9, 16, 25, 27, 36. Which one is not?", ["27", "Twenty-seven"], "The others are square numbers (3², 4², 5², 6²); 27 is not.")
c(30, "Numbers", ["quiz scores", "fractions"], "Halfway through a 20-question quiz you have 7 right. How many of the last 10 must you get right to finish with three-quarters right?", ["8", "Eight"], "Three-quarters of 20 is 15, and 15 − 7 = 8.")
c(50, "Numbers", ["baking", "ratios"], "A recipe needs 3 eggs to make 12 cupcakes. How many eggs do you need for 20 cupcakes?", ["5", "Five"], "That's one egg for every 4 cupcakes, and 20 ÷ 4 = 5.")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'club-30.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'club puzzles written')
