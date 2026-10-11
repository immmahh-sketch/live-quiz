# Bank session 11 Oct 2026: more 1% Club puzzles -> bank/club-19.json. Logic, number and wordplay, each with a one-line
# "why". Tested against every club puzzle in the live bank with lqsql/neardup.py (a copy of the server's near-duplicate
# rule: word overlap of 80%, or 50% with the same answer) before importing.
import json, os
PCTS = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 1]
OUT = []
def c(pct, cat, tags, text, answers, why):
    assert pct in PCTS, (text, pct)
    diff = "easy" if pct >= 70 else "medium" if pct >= 40 else "hard"
    OUT.append({"type": "club", "text": text, "answers": answers, "pct": pct, "why": why, "difficulty": diff, "category": cat, "tags": tags})

c(90, "Numbers", ["Metro", "money"], "A Metro day ticket costs £2. What do you pay for you and two friends?", ["£6", "6", "Six pounds"], "3 × £2 = £6.")
c(80, "Logic", ["days of the week", "odd one out"], "Which of these isn't a real day of the week: Wednesday, Funday, Friday, Monday?", ["Funday"], "The other three are real days.")
c(70, "Numbers", ["Greggs", "dividing"], "Sausage rolls come in packs of 4. You need 22 for a party. How many packs must you buy?", ["6", "Six"], "5 packs give only 20, so you need a sixth.")
c(60, "Numbers", ["halving", "doubling"], "Take eighteen, cut it in half, multiply by two and finally add one. Result?", ["19", "Nineteen"], "Halving then doubling gets you back to 18; add 1 for 19.")
c(50, "Numbers", ["doubling", "gossip"], "Gossip spreads: 3 people know at 9am, 6 by 10am and 12 by 11am. If it keeps doubling, how many know by noon?", ["24", "Twenty-four"], "12 doubled is 24.")
c(40, "Numbers", ["walking", "speed"], "Sunderland to Newcastle is about 12 miles. Walking at 3 miles an hour, how many hours will it take?", ["4", "Four", "4 hours"], "12 ÷ 3 = 4.")
c(40, "Numbers", ["money", "sharing"], "A pub quiz team of 6 shares a £45 prize equally. How much does each person get?", ["£7.50", "7.50", "£7.5"], "£45 ÷ 6 = £7.50.")
c(30, "Time", ["calendar", "Sundays"], "What's the most Sundays a 31-day month can have?", ["5", "Five"], "31 days is 4 weeks and 3 days, so three weekdays appear five times.")
c(5, "Wordplay", ["months", "counting letters"], "Which month of the year has the shortest name?", ["May"], "Three letters, one fewer than June or July.")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'club-19.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'club puzzles written')
