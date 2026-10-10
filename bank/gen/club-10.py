# Bank session 10 Oct 2026: more 1% Club puzzles -> bank/club-8.json. Logic, number and wordplay, each with a one-line
# "why". Tested against every club puzzle in the live bank with lqsql/neardup.py (a copy of the server's near-duplicate
# rule: word overlap of 80%, or 50% with the same answer) before importing.
import json, os
PCTS = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 1]
OUT = []
def c(pct, cat, tags, text, answers, why):
    assert pct in PCTS, (text, pct)
    diff = "easy" if pct >= 70 else "medium" if pct >= 40 else "hard"
    OUT.append({"type": "club", "text": text, "answers": answers, "pct": pct, "why": why, "difficulty": diff, "category": cat, "tags": tags})

c(80, "Numbers", ["money", "change"], "Sam pays for a £3.20 sandwich with a £5 note. How much change does he get?", ["£1.80", "1.80", "£1.80p"], "£5.00 − £3.20 = £1.80.")
c(80, "Logic", ["months", "calendar"], "Count on two months from November. Which month do you land on?", ["January"], "November, December, January.")
c(80, "Numbers", ["measures"], "Which is longer: a metre or a yard?", ["A metre", "Metre"], "A metre is about 39 inches; a yard is 36.")
c(70, "Numbers", ["doubling"], "What do you get if you double 45?", ["90", "Ninety"], "45 + 45 = 90.")
c(70, "Numbers", ["time"], "A sand timer runs for five minutes. How many seconds is that?", ["300", "Three hundred"], "60 × 5 = 300.")
c(60, "Numbers", ["patterns", "dividing"], "Each number is a third of the one before: 81, 27, 9, 3. Which follows?", ["1", "One"], "3 ÷ 3 = 1.")
c(60, "Numbers", ["cooking", "ratios"], "A recipe for 4 people needs 200g of flour. How much flour for 8 people?", ["400g", "400", "400 grams"], "Twice the people, twice the flour.")
c(40, "Logic", ["painters", "rates"], "Three painters paint three fences in three hours. How long would six painters take to paint six fences?", ["3 hours", "Three hours", "3"], "Each painter does one fence in three hours, so twice the painters do twice the fences in the same time.")
c(30, "Logic", ["clocks", "time"], "A clock gains 2 minutes every hour. It's set right at noon. What does it show at 6pm real time?", ["6:12", "12 minutes past 6", "6.12", "18:12"], "Six hours × 2 minutes = 12 minutes fast.")
c(30, "Numbers", ["order of operations"], "Work out: half of 2, plus 2.", ["3", "Three"], "Half of 2 is 1, and 1 + 2 = 3.")
c(20, "Logic", ["leap years", "birthdays"], "Someone born on 29 February 2000 has had how many real birthdays, on the 29th, from 2001 to 2024?", ["6", "Six"], "2004, 2008, 2012, 2016, 2020 and 2024.")
c(20, "Wordplay", ["spelling", "letters"], "Count the S's in MISSISSIPPI.", ["4", "Four"], "M-I-S-S-I-S-S-I-P-P-I: two pairs of S.")
c(10, "Numbers", ["order of operations"], "What is 0.1 + 0.2 × 10?", ["2.1", "2 point 1"], "Multiply first: 0.2 × 10 = 2, then add 0.1.")
c(10, "Logic", ["riddles", "North Pole"], "A hunter walks a mile south, a mile east and a mile north, and ends up exactly where he started. He sees a bear. What colour is it?", ["White"], "Only at the North Pole does that walk bring you back: it's a polar bear.")
c(5, "Numbers", ["prime numbers"], "These are all primes: 2, 3, 5, 7, 11, 13. Which prime comes after 13?", ["17", "Seventeen"], "14, 15 and 16 all divide by something; 17 doesn't.")

c(40, "Numbers", ["powers"], "Which is bigger: 3 squared or 2 cubed?", ["3 squared", "3²", "9", "Three squared"], "3 × 3 = 9, while 2 × 2 × 2 = 8.")
c(1, "Logic", ["puzzles", "Tower of Hanoi"], "In the Tower of Hanoi puzzle with three discs, what is the fewest number of moves to shift the whole tower?", ["7", "Seven"], "With n discs it takes 2ⁿ − 1 moves: 2³ − 1 = 7.")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'club-8.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'club puzzles written')
