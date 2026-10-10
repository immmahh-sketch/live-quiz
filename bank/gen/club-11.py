# Bank session 10 Oct 2026: more 1% Club puzzles -> bank/club-9.json. Logic, number and wordplay, each with a one-line
# "why". Tested against every club puzzle in the live bank with lqsql/neardup.py (a copy of the server's near-duplicate
# rule: word overlap of 80%, or 50% with the same answer) before importing.
import json, os
PCTS = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 1]
OUT = []
def c(pct, cat, tags, text, answers, why):
    assert pct in PCTS, (text, pct)
    diff = "easy" if pct >= 70 else "medium" if pct >= 40 else "hard"
    OUT.append({"type": "club", "text": text, "answers": answers, "pct": pct, "why": why, "difficulty": diff, "category": cat, "tags": tags})

c(90, "Numbers", ["sweets", "taking away"], "Lucy has 10 sweets and eats 4 of them. How many does she have left?", ["6", "Six"], "10 − 4 = 6.")
c(90, "Wordplay", ["backwards", "animals"], "Spell GOD backwards. Which animal do you get?", ["Dog", "A dog"], "G-O-D reversed is D-O-G.")
c(80, "Numbers", ["adding"], "Add 25 four times over. What's the total?", ["100", "One hundred"], "25 × 4 = 100.")
c(70, "Numbers", ["shapes", "sides"], "Two squares and a triangle: how many sides do they have between them?", ["11", "Eleven"], "4 + 4 + 3 = 11.")
c(70, "Logic", ["time", "clocks"], "It's 3pm now. What time will it be ten hours from now?", ["1am", "1 am", "1 o'clock in the morning", "01:00"], "3pm plus 9 hours is midnight, plus one more is 1am.")
c(60, "Wordplay", ["anagrams", "food"], "Unscramble OTOMAT to find something red you can eat.", ["Tomato"], "O-T-O-M-A-T rearranges to TOMATO.")
c(60, "Numbers", ["time"], "Add a quarter of an hour to half an hour. How many minutes is that?", ["45", "Forty-five"], "15 + 30 = 45.")
c(50, "Numbers", ["time", "comparing"], "Which lasts longer: a hundred minutes, or an hour and a half?", ["100 minutes"], "An hour and a half is only 90 minutes.")
c(50, "Numbers", ["money", "dividing"], "A box of 6 eggs costs £1.20. How much is that per egg?", ["20p", "20 pence", "£0.20"], "£1.20 ÷ 6 = 20p.")
c(40, "Wordplay", ["patterns", "alphabet"], "Going backwards two at a time: Z, X, V, T. Which letter follows?", ["R"], "Z (y) X (w) V (u) T (s) R.")
c(40, "Numbers", ["handshakes"], "Four friends meet, and every pair of them shakes hands once. How many shakes is that?", ["6", "Six"], "Each of 4 shakes 3 hands, but that counts every shake twice: 12 ÷ 2 = 6.")
c(30, "Numbers", ["percentages"], "Work out fifteen per cent of two hundred.", ["30", "Thirty"], "10% is 20 and 5% is 10, so 15% is 30.")
c(30, "Numbers", ["squares"], "What is the smallest three-digit number that's a perfect square?", ["100", "One hundred"], "10 × 10 = 100; 9 × 9 is only 81.")
c(20, "Numbers", ["calendar", "months"], "In a calendar year, count the thirty-day months.", ["4", "Four"], "April, June, September and November.")
c(20, "Logic", ["clocks"], "In a whole day, how many times does a clock's minute hand point straight up at the 12?", ["24", "Twenty-four"], "Once every hour, and there are 24 hours in a day.")
c(10, "Numbers", ["digits"], "Counting from 1 to 50, how many of the numbers have a 5 in them?", ["6", "Six"], "5, 15, 25, 35, 45, and don't forget 50.")
c(10, "Numbers", ["multiplying"], "What is 11 × 11 × 11?", ["1331", "1,331"], "11 × 11 = 121, and 121 × 11 = 1,331.")
c(5, "Numbers", ["patterns"], "Gaps of 1, then 2, then 3, then 4: 1, 2, 4, 7, 11. What's after 11?", ["16", "Sixteen"], "The gaps are 1, 2, 3, 4, so the next gap is 5: 11 + 5 = 16.")
c(5, "Logic", ["shapes", "triangles"], "Join the midpoints of a triangle's three sides. How many triangles can you now count?", ["5", "Five"], "Four small ones inside, plus the big one around them.")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'club-9.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'club puzzles written')
