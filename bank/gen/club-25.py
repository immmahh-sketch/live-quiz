# Bank session 11 Oct 2026: more 1% Club puzzles -> bank/club-23.json. Logic, number and wordplay, each with a one-line
# "why". Tested against every club puzzle in the live bank with lqsql/neardup.py (a copy of the server's near-duplicate
# rule: word overlap of 80%, or 50% with the same answer) before importing.
import json, os
PCTS = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 1]
OUT = []
def c(pct, cat, tags, text, answers, why):
    assert pct in PCTS, (text, pct)
    diff = "easy" if pct >= 70 else "medium" if pct >= 40 else "hard"
    OUT.append({"type": "club", "text": text, "answers": answers, "pct": pct, "why": why, "difficulty": diff, "category": cat, "tags": tags})

c(90, "Numbers", ["money", "change"], "Pints are £5 each. You buy three and pay with a £20 note. How much change?", ["£5", "5", "Five pounds"], "3 × £5 = £15, and £20 − £15 = £5.")
c(80, "Numbers", ["comparing", "fractions"], "Which is more: half a dozen, or a quarter of twenty?", ["Half a dozen", "6"], "Half a dozen is 6; a quarter of twenty is 5.")
c(70, "Numbers", ["bus fares", "money"], "A bus fare is £2.50 each way. What do two people pay for a return trip?", ["£10", "10", "Ten pounds"], "£5 return each, and two of them make £10.")
c(50, "Numbers", ["rounds", "multiplying"], "Five friends each buy a round of five drinks at £4 a drink. What do they spend altogether?", ["£100", "100", "A hundred pounds"], "5 rounds × 5 drinks × £4 = £100.")
c(40, "Numbers", ["percentages", "tips"], "You leave a 15% tip on a £40 meal. How much is the tip?", ["£6", "6", "Six pounds"], "10% is £4, 5% is £2, so 15% is £6.")
c(20, "Numbers", ["wine", "dividing"], "A bottle of wine fills six glasses. Four people want three glasses each. How many bottles?", ["2", "Two"], "12 glasses ÷ 6 per bottle = 2.")
c(10, "Numbers", ["fuel", "multiplying"], "A car does 50 miles to the gallon and petrol costs £7 a gallon. What does a 200-mile trip cost in fuel?", ["£28", "28"], "200 ÷ 50 = 4 gallons, and 4 × £7 = £28.")
c(5, "Wordplay", ["months", "counting letters"], "Which month of the year has the longest name?", ["September"], "Nine letters; November, December and February have eight.")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'club-23.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'club puzzles written')
