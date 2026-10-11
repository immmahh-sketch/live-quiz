# Bank session 11 Oct 2026: more 1% Club puzzles -> bank/club-18.json. Logic, number and wordplay, each with a one-line
# "why". Tested against every club puzzle in the live bank with lqsql/neardup.py (a copy of the server's near-duplicate
# rule: word overlap of 80%, or 50% with the same answer) before importing.
import json, os
PCTS = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 1]
OUT = []
def c(pct, cat, tags, text, answers, why):
    assert pct in PCTS, (text, pct)
    diff = "easy" if pct >= 70 else "medium" if pct >= 40 else "hard"
    OUT.append({"type": "club", "text": text, "answers": answers, "pct": pct, "why": why, "difficulty": diff, "category": cat, "tags": tags})

c(90, "Numbers", ["buses", "adding and taking away"], "The 21 bus to Durham has 20 passengers. At Chester-le-Street 5 get off and 3 get on. How many are aboard now?", ["18", "Eighteen"], "20 − 5 + 3 = 18.")
c(80, "Wordplay", ["vowels"], "Which one of these letters is a vowel: B, K, O or T?", ["O"], "A, E, I, O and U are the vowels.")
c(70, "Numbers", ["legs", "animals"], "Count the feet: two farm cats plus three hens.", ["14", "Fourteen"], "2 × 4 + 3 × 2 = 8 + 6 = 14.")
c(50, "Time", ["percentages", "hours"], "What is twenty-five per cent of sixty?", ["15", "Fifteen"], "A quarter of 60 is 15.")
c(30, "Numbers", ["chocolate", "rows"], "A chocolate bar is 4 rows of 6 squares. You snap off and eat one whole row of 6. How many squares are left?", ["18", "Eighteen"], "24 squares in all, minus 6, leaves 18.")
c(20, "Logic", ["families", "trick questions"], "A mum has four daughters, and each daughter has one brother. How many children does she have?", ["5", "Five"], "The four girls all share the same one brother.")


here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'club-18.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'club puzzles written')
