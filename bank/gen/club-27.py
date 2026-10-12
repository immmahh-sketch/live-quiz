# Bank session 12 Oct 2026: more 1% Club puzzles -> bank/club-27.json. Logic, number and wordplay, each with a one-line
# "why". Tested against every club puzzle in the live bank with lqsql/neardup.py (a copy of the server's near-duplicate
# rule: word overlap of 80%, or 50% with the same answer) before importing.
import json, os
PCTS = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 1]
OUT = []
def c(pct, cat, tags, text, answers, why):
    assert pct in PCTS, (text, pct)
    diff = "easy" if pct >= 70 else "medium" if pct >= 40 else "hard"
    OUT.append({"type": "club", "text": text, "answers": answers, "pct": pct, "why": why, "difficulty": diff, "category": cat, "tags": tags})

c(60, "Logic", ["darts"], "On a dartboard, which number sits at the very top, between the 5 and the 1?", ["20", "Twenty"], "The board runs 20, 1, 18, 4… from the top, with the 5 on the other side of the 20.")
c(50, "Logic", ["Great North Run", "order"], "Ellie finished the Great North Run before Jo, but after Kim. Who finished first?", ["Kim"], "Kim, then Ellie, then Jo.")
c(50, "Numbers", ["fractions", "comparing"], "Which is bigger: a third of ninety, or a quarter of a hundred?", ["A third of 90", "Third of 90", "30", "The third"], "A third of 90 is 30; a quarter of 100 is 25.")
c(50, "Time", ["trains", "adding time"], "A train leaves Newcastle at 10:47 and takes 2 hours 55 minutes to reach London. What time does it arrive?", ["13:42", "1:42", "1:42pm", "1.42pm", "1.42"], "10:47 + 3 hours is 13:47; take off 5 minutes: 13:42.")
c(40, "Words", ["letters", "counting"], "How many times does the letter E appear in NEWCASTLE UPON TYNE?", ["3", "Three"], "NEWCASTLE has two, UPON has none, TYNE has one.")

c(70, "Numbers", ["Greggs", "money"], "Sausage rolls cost £1.20 each. How much do five of them cost?", ["£6", "6", "Six pounds", "£6.00"], "5 × £1.20 = £6.")
c(60, "Logic", ["compass", "sequences"], "Going clockwise round a compass from North, the points are N, E, S… then?", ["W", "West"], "The points of the compass, going clockwise from North.")
c(30, "Numbers", ["shapes", "spiders", "football"], "Multiply a hexagon's sides by a spider's legs, then subtract the players in one football team. What's the result?", ["37", "Thirty-seven"], "6 × 8 = 48, and 48 − 11 = 37.")
c(40, "Time", ["cycling", "speed"], "Sunderland is 12 miles from Newcastle. A cyclist rides there and back at 12 mph. How many minutes does the round trip take?", ["120", "120 minutes", "Two hours"], "24 miles at 12 miles an hour is 2 hours: 120 minutes.")
c(10, "Numbers", ["percentages", "shopping"], "A £40 coat goes up by 10%, then the new price is cut by 10%. What does it cost now?", ["£39.60", "39.60", "39.6"], "Up 10% is £44; 10% off £44 is £4.40, leaving £39.60.")
c(10, "Time", ["calendar", "Saturdays"], "A year that isn't a leap year starts on a Saturday. How many Saturdays does it have?", ["53", "Fifty-three"], "365 days is 52 weeks and 1 day, and that extra day is a Saturday.")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'club-27.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'club puzzles written')
