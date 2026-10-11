# Bank session 11 Oct 2026: more 1% Club puzzles -> bank/club-16.json. Logic, number and wordplay, each with a one-line
# "why". Tested against every club puzzle in the live bank with lqsql/neardup.py (a copy of the server's near-duplicate
# rule: word overlap of 80%, or 50% with the same answer) before importing.
import json, os
PCTS = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 1]
OUT = []
def c(pct, cat, tags, text, answers, why):
    assert pct in PCTS, (text, pct)
    diff = "easy" if pct >= 70 else "medium" if pct >= 40 else "hard"
    OUT.append({"type": "club", "text": text, "answers": answers, "pct": pct, "why": why, "difficulty": diff, "category": cat, "tags": tags})

c(90, "Numbers", ["clothes", "pairs"], "You put on a pair of socks and a pair of shoes. How many items is that on your feet?", ["4", "Four"], "Two socks plus two shoes.")
c(80, "Numbers", ["counting in fives"], "Fill the gap in the five times table: 5, 10, 15, ?, 25.", ["20", "Twenty"], "Each step adds 5, so 15 + 5 = 20.")
c(50, "Time", ["February", "calendar"], "In a February that isn't a leap year, what's the most Fridays it can have?", ["4", "Four"], "28 days is exactly four weeks, so every weekday appears four times.")
c(40, "Logic", ["weight", "trick questions"], "Which weighs more: a kilogram of feathers or 900 grams of bricks?", ["A kilogram of feathers", "Feathers", "The feathers"], "1,000 grams beats 900 grams, whatever it's made of.")
c(1, "Numbers", ["digits", "multiplying"], "Use the digits 1, 2, 3 and 4 once each to make two two-digit numbers with the biggest possible product. What is that product?", ["1312", "1,312"], "41 × 32 = 1,312 beats 42 × 31 = 1,302 and every other split.")
c(70, "Logic", ["ages", "family"], "Gran is older than Aunt Jo, and Aunt Jo is older than Uncle Pete. Who's the youngest of the three?", ["Uncle Pete", "Pete"], "Gran > Jo > Pete, so Pete is youngest.")
c(60, "Numbers", ["ages"], "Mum is 34 and her son is 8. How old will Mum be when her son turns 20?", ["46", "Forty-six"], "That's 12 years away, and 34 + 12 = 46.")
c(50, "Numbers", ["money", "dividing"], "A pack of six bread rolls costs £1.50. What's the price of one roll?", ["25p", "25 pence", "£0.25"], "150p ÷ 6 = 25p.")
c(60, "Time", ["trains", "Whitby"], "Grandad's Whitby train departs at 10:50 and the trip lasts 25 minutes. When does he get there?", ["11:15", "Quarter past eleven", "11.15"], "10 minutes takes it to 11:00, then 15 more.")
c(5, "Numbers", ["money", "fish and chips"], "At the chippy, a fish and a portion of chips come to £4 in total. The fish is £3 dearer than the chips. How much are the chips?", ["50p", "50 pence", "£0.50"], "Chips 50p, fish £3.50: £4 altogether, £3 apart.")
c(30, "Numbers", ["phone battery", "percentages"], "Your phone battery is at 40% and drops 5% every hour. How many hours until it's dead?", ["8", "Eight", "8 hours"], "40 ÷ 5 = 8.")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'club-16.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'club puzzles written')

