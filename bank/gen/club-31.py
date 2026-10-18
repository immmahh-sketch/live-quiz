# Bank session 18 Oct 2026: more 1% Club puzzles -> bank/club-31.json. Logic, number and wordplay, each with a one-line
# "why" and short exact answers. Tested against every club puzzle in the live bank with lqsql/neardup.py (a copy of the
# server's near-duplicate rule) before importing; wording kept distinctive so a different puzzle isn't mistaken for an old one.
# Dropped as already in the bank: a clock gaining 2 minutes an hour, the first prime after 89, FORTY's letters in order.
import json, os
PCTS = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 1]
OUT = []
def c(pct, cat, tags, text, answers, why):
    assert pct in PCTS, (text, pct)
    diff = "easy" if pct >= 70 else "medium" if pct >= 40 else "hard"
    OUT.append({"type": "club", "text": text, "answers": answers, "pct": pct, "why": why, "difficulty": diff, "category": cat, "tags": tags})

c(60, "Wordplay", ["alphabet", "letters"], "Which letter of the alphabet is the 18th?", ["R"], "A-I is 9, J-R takes you to 18: R.")
c(60, "Wordplay", ["spelling", "counting"], "Count the Es in the word EXCELLENCE.", ["4", "Four"], "E-X-C-E-L-L-E-N-C-E: four Es.")
c(50, "Numbers", ["paper", "doubling"], "Fold a sheet of paper in half, then in half again, four folds in all. How many layers thick is it?", ["16", "Sixteen"], "Each fold doubles it: 2, 4, 8, 16.")
c(40, "Logic", ["queues", "counting"], "Kim is fourth from the front of a queue and fourth from the back. How many people are queuing?", ["7", "Seven"], "Three in front of Kim, three behind, and Kim: seven.")
c(30, "Time", ["fortnight", "minutes"], "A fortnight lasts how many minutes?", ["20,160", "20160"], "14 days × 24 hours × 60 minutes = 20,160.")
c(20, "Numbers", ["ages", "algebra"], "Gran is 80 and her grandson is 8. In how many years will Gran be exactly five times his age?", ["10", "Ten"], "In 10 years she'll be 90 and he'll be 18, and 18 × 5 = 90.")
c(10, "Logic", ["pizza", "cutting"], "With three straight cuts across a round pizza, what is the most pieces you can make?", ["7", "Seven"], "Make every cut cross both of the others, and not all at one point: 7 pieces.")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'club-31.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'club puzzles written')
