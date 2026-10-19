# Bank session 19 Oct 2026: more 1% Club puzzles -> bank/club-39.json. Logic, number and wordplay, each with a one-line
# "why" and short exact answers. Tested against every club puzzle in the live bank with lqsql/neardup.py (a copy of the
# server's near-duplicate rule) before importing; wording kept distinctive so a different puzzle isn't mistaken for an old one.
# Checked against the live club bank: double letters (BOOKKEEPER) and the longest month name were already there.
import json, os
PCTS = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 1]
OUT = []
def c(pct, cat, tags, text, answers, why):
    assert pct in PCTS, (text, pct)
    diff = "easy" if pct >= 70 else "medium" if pct >= 40 else "hard"
    OUT.append({"type": "club", "text": text, "answers": answers, "pct": pct, "why": why, "difficulty": diff, "category": cat, "tags": tags})

c(50, "Numbers", ["bees", "multiplying"], "A bumblebee's wings beat 200 times a second. How many times do they beat in one minute?", ["12,000", "12000", "Twelve thousand"], "200 × 60 = 12,000.")
c(60, "Numbers", ["bats", "multiplying"], "A pipistrelle bat can eat 3,000 insects in one night. How many could it eat in a week?", ["21,000", "21000", "Twenty-one thousand"], "3,000 × 7 = 21,000.")
c(30, "Wordplay", ["days", "letters", "adding"], "Spell out all seven days of the week. How many letters is that altogether?", ["50", "Fifty"], "Monday 6, Tuesday 7, Wednesday 9, Thursday 8, Friday 6, Saturday 8, Sunday 6: 50.")
c(40, "Wordplay", ["days", "letters"], "Which day of the week has a letter D in its name that isn't part of the DAY at the end?", ["Wednesday"], "WeDnesday: the only D outside the final DAY.")
c(20, "Numbers", ["cats", "dogs", "legs"], "In a room there are some cats and some people. Altogether there are 13 heads and 38 legs. How many cats are there?", ["6", "Six"], "If all 13 were people that's 26 legs; the 12 extra legs come from cats with two more each: 6 cats.")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'club-39.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'club puzzles written')
