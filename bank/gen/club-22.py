# Bank session 11 Oct 2026: more 1% Club puzzles -> bank/club-20.json. Logic, number and wordplay, each with a one-line
# "why". Tested against every club puzzle in the live bank with lqsql/neardup.py (a copy of the server's near-duplicate
# rule: word overlap of 80%, or 50% with the same answer) before importing.
import json, os
PCTS = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 1]
OUT = []
def c(pct, cat, tags, text, answers, why):
    assert pct in PCTS, (text, pct)
    diff = "easy" if pct >= 70 else "medium" if pct >= 40 else "hard"
    OUT.append({"type": "club", "text": text, "answers": answers, "pct": pct, "why": why, "difficulty": diff, "category": cat, "tags": tags})

c(90, "Numbers", ["fractions", "stotties"], "You cut a stottie into 4 equal pieces and eat one. What fraction of it is left?", ["Three quarters", "3/4", "¾"], "Three of the four quarters remain.")
c(80, "Logic", ["rivers", "odd one out"], "Odd one out: Tyne, Wear, Tees, Thames.", ["Thames", "The Thames"], "The other three are North East rivers.")
c(70, "Time", ["football", "half-time"], "A match kicks off at 3pm: two 45-minute halves and a 15-minute break. With no added time, when does it finish?", ["4:45pm", "4.45pm", "Quarter to five", "16:45"], "45 + 15 + 45 = 105 minutes after 3pm.")
c(60, "Numbers", ["money", "pints"], "Three pints cost £13.50. What does one cost?", ["£4.50", "4.50", "£4.5"], "£13.50 ÷ 3 = £4.50.")
c(40, "Numbers", ["quiz scores"], "A quiz round has 10 questions worth 2 points each, plus a 5-point bonus. What's the most you can score?", ["25", "Twenty-five"], "20 + 5 = 25.")
c(30, "Numbers", ["ages"], "Sam is twice Jo's age. In 4 years Sam will be 20. How old is Jo now?", ["8", "Eight"], "Sam is 16 now, so Jo is 8.")
c(20, "Numbers", ["measuring", "ribbon"], "From a 3-metre ribbon, how many 25-centimetre pieces can you cut?", ["12", "Twelve"], "300 cm ÷ 25 cm = 12.")
c(10, "Time", ["24-hour clock", "digits"], "How many times a day does a 24-hour digital clock show the same digit four times, like 11:11?", ["3", "Three"], "00:00, 11:11 and 22:22; 33:33 isn't a time.")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'club-20.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'club puzzles written')
