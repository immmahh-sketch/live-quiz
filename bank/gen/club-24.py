# Bank session 11 Oct 2026: more 1% Club puzzles -> bank/club-22.json. Logic, number and wordplay, each with a one-line
# "why". Tested against every club puzzle in the live bank with lqsql/neardup.py (a copy of the server's near-duplicate
# rule: word overlap of 80%, or 50% with the same answer) before importing.
import json, os
PCTS = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 1]
OUT = []
def c(pct, cat, tags, text, answers, why):
    assert pct in PCTS, (text, pct)
    diff = "easy" if pct >= 70 else "medium" if pct >= 40 else "hard"
    OUT.append({"type": "club", "text": text, "answers": answers, "pct": pct, "why": why, "difficulty": diff, "category": cat, "tags": tags})

c(90, "Numbers", ["sharing", "stotties"], "Twelve stotties are shared equally between four families. How many does each family get?", ["3", "Three"], "12 ÷ 4 = 3.")
c(80, "Logic", ["sport", "odd one out"], "Odd one out: Beckham, Rooney, Kane, Federer.", ["Federer", "Roger Federer"], "The others are England footballers; Federer plays tennis.")
c(60, "Sport", ["darts", "doubles"], "A darts player needs exactly 40 to finish. Which double is the classic one to aim for?", ["Double 20", "D20", "Double top"], "Double 20 scores 40 — 'double top'.")
c(50, "Sport", ["snooker", "adding"], "In snooker, what do the six colours add up to, potting each once (yellow to black)?", ["27", "Twenty-seven"], "2 + 3 + 4 + 5 + 6 + 7 = 27.")
c(40, "Sport", ["cricket", "multiplying"], "A cricket over has 6 balls. How many balls in a 20-over innings?", ["120", "One hundred and twenty"], "20 × 6 = 120.")
c(5, "Sport", ["darts", "odd numbers"], "What's the highest ODD total you can score with three darts?", ["177", "One hundred and seventy-seven"], "Two treble 20s and a treble 19: 60 + 60 + 57 = 177.")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'club-22.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'club puzzles written')
