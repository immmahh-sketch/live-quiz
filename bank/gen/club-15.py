# Bank session 11 Oct 2026: more 1% Club puzzles -> bank/club-13.json. Logic, number and wordplay, each with a one-line
# "why". Tested against every club puzzle in the live bank with lqsql/neardup.py (a copy of the server's near-duplicate
# rule: word overlap of 80%, or 50% with the same answer) before importing.
import json, os
PCTS = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 1]
OUT = []
def c(pct, cat, tags, text, answers, why):
    assert pct in PCTS, (text, pct)
    diff = "easy" if pct >= 70 else "medium" if pct >= 40 else "hard"
    OUT.append({"type": "club", "text": text, "answers": answers, "pct": pct, "why": why, "difficulty": diff, "category": cat, "tags": tags})

c(90, "Numbers", ["wheels", "cars"], "Three cars are parked in a row. How many wheels touch the ground?", ["12", "Twelve"], "3 × 4 = 12.")
c(80, "Numbers", ["taking away"], "Take one away from a thousand.", ["999", "Nine hundred and ninety-nine"], "1,000 − 1 = 999.")
c(80, "Numbers", ["dozens"], "How many eggs make two dozen?", ["24", "Twenty-four"], "A dozen is 12, so two dozen is 24.")
c(70, "Wordplay", ["anagrams"], "Rearrange the letters of NIGHT to make a word meaning 'an object'.", ["Thing"], "N-I-G-H-T rearranges to THING.")
c(70, "Numbers", ["doubling"], "Add 45 to itself.", ["90", "Ninety"], "45 + 45 = 90.")
c(60, "Numbers", ["time", "football"], "A match kicks off at 3pm and finishes 105 minutes later, half-time included. When does it end?", ["4:45pm", "4.45pm", "4:45", "Quarter to five"], "3pm plus 1 hour 45 minutes is 4:45pm.")
c(50, "Numbers", ["halfway"], "Which number sits exactly halfway between 30 and 70?", ["50", "Fifty"], "30 + 70 = 100, and half of 100 is 50.")
c(50, "Wordplay", ["spelling", "numbers"], "Write the number 8 as a word. How many letters is that?", ["5", "Five"], "E-I-G-H-T.")
c(40, "Numbers", ["trains", "multiplying"], "A train has 8 carriages with 60 seats in each. How many seats altogether?", ["480", "Four hundred and eighty"], "8 × 60 = 480.")
c(30, "Wordplay", ["alphabet"], "Which letter is the 13th in the alphabet?", ["M"], "A to M is the first half of the alphabet: M is 13th.")
c(30, "Numbers", ["percentages"], "What's fifteen per cent of sixty?", ["9", "Nine"], "10% is 6 and 5% is 3: 9.")
c(10, "Numbers", ["doubling", "squaring"], "Which whole number above zero gives the same answer whether you add it to itself or multiply it by itself?", ["2", "Two"], "2 + 2 = 4 and 2 × 2 = 4.")
c(20, "Numbers", ["powers", "digits"], "Double 1 ten times over to reach 1,024. Now add up the digits of 1,024.", ["7", "Seven"], "1 + 0 + 2 + 4 = 7.")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'club-13.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'club puzzles written')
