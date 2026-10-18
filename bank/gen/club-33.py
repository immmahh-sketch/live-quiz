# Bank session 18 Oct 2026: more 1% Club puzzles -> bank/club-33.json. Logic, number and wordplay, each with a one-line
# "why" and short exact answers. Tested against every club puzzle in the live bank with lqsql/neardup.py (a copy of the
# server's near-duplicate rule) before importing; wording kept distinctive so a different puzzle isn't mistaken for an old one.
# Dropped as already in the bank: E's in SEVENTEEN, numbers containing a 3, the dartboard total, minutes in a fortnight,
# O T T F F S S E, the number with as many letters as its value, and the alphabetical-order numbers.
import json, os
PCTS = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 1]
OUT = []
def c(pct, cat, tags, text, answers, why):
    assert pct in PCTS, (text, pct)
    diff = "easy" if pct >= 70 else "medium" if pct >= 40 else "hard"
    OUT.append({"type": "club", "text": text, "answers": answers, "pct": pct, "why": why, "difficulty": diff, "category": cat, "tags": tags})

c(40, "Time", ["calendars", "days"], "1 January 2027 is a Friday. On what day of the week does 1 January 2028 fall?", ["Saturday", "Sat"], "2027 isn't a leap year, so 365 days = 52 weeks + 1 day: one day on from Friday.")
c(30, "Numbers", ["Roman numerals", "years"], "Of all the years from 2000 onwards, which one needs the fewest Roman numerals to write?", ["2000", "MM"], "2000 is just MM: two letters. Every later year adds at least one more.")
c(50, "Numbers", ["camels", "adding"], "A dromedary has one hump and a Bactrian camel has two. A herd of 5 camels has 7 humps. How many are Bactrian?", ["2", "Two"], "If all 5 had one hump there'd be 5; the 2 extra humps mean 2 Bactrians.")
c(20, "Numbers", ["dominoes", "counting"], "In a double-six set of dominoes, how many dominoes have at least one six on them?", ["7", "Seven"], "6-0, 6-1, 6-2, 6-3, 6-4, 6-5 and the double six: 7.")
c(10, "Numbers", ["dice", "logic"], "On a dice, opposite faces add up to 7. Looking at a corner you can see 1, 2 and 3. What do the three hidden faces add up to?", ["15", "Fifteen"], "The hidden faces are 6, 5 and 4: 15.")
c(50, "Numbers", ["snooker", "adding"], "In snooker, what's the most points you can score by potting one red and then one colour?", ["8", "Eight"], "A red is worth 1 and the black, the most valuable colour, 7.")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'club-33.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'club puzzles written')
