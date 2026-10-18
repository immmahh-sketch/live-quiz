# Bank session 19 Oct 2026: more 1% Club puzzles -> bank/club-36.json. Logic, number and wordplay, each with a one-line
# "why" and short exact answers. Tested against every club puzzle in the live bank with lqsql/neardup.py (a copy of the
# server's near-duplicate rule) before importing; wording kept distinctive so a different puzzle isn't mistaken for an old one.
# Dropped as already in the bank: heads-and-legs farmyards, S's in MISSISSIPPI, subtracting 5 from 25, the bat and ball,
# taking away apples.
import json, os
PCTS = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 1]
OUT = []
def c(pct, cat, tags, text, answers, why):
    assert pct in PCTS, (text, pct)
    diff = "easy" if pct >= 70 else "medium" if pct >= 40 else "hard"
    OUT.append({"type": "club", "text": text, "answers": answers, "pct": pct, "why": why, "difficulty": diff, "category": cat, "tags": tags})

c(70, "Numbers", ["dogs", "multiplying"], "If one human year counts as seven 'dog years', how old in dog years is a 6-year-old dog?", ["42", "Forty-two"], "6 × 7 = 42.")
c(60, "Numbers", ["cats", "multiplying"], "A cat has 18 toes: five on each front paw and four on each back paw. How many toes do 3 cats have between them?", ["54", "Fifty-four"], "18 × 3 = 54.")
c(10, "Numbers", ["cats", "logic", "trick"], "A cat and her kitten weigh 5 kg together. The cat weighs 4 kg more than the kitten. How much does the kitten weigh?", ["500g", "0.5kg", "Half a kilo", "500 grams", "0.5"], "Not 1 kg: kitten ½ kg + cat 4½ kg = 5 kg, and the difference is 4 kg.")
c(60, "Numbers", ["goldfish", "time"], "The myth says a goldfish's memory lasts 3 seconds. How many fresh starts would that give it in one minute?", ["20", "Twenty"], "60 ÷ 3 = 20.")
c(30, "Time", ["dogs", "calendars"], "A dog is pregnant for 63 days. If her puppies arrive on 1 March 2027, in which month did she conceive?", ["December", "Dec"], "February 2027 has 28 days, January 31: that's 59 days, so 4 more takes you back to 28 December.")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'club-36.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'club puzzles written')
