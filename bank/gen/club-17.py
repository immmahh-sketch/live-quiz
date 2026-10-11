# Bank session 11 Oct 2026: more 1% Club puzzles -> bank/club-15.json. Logic, number and wordplay, each with a one-line
# "why". Tested against every club puzzle in the live bank with lqsql/neardup.py (a copy of the server's near-duplicate
# rule: word overlap of 80%, or 50% with the same answer) before importing.
import json, os
PCTS = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 1]
OUT = []
def c(pct, cat, tags, text, answers, why):
    assert pct in PCTS, (text, pct)
    diff = "easy" if pct >= 70 else "medium" if pct >= 40 else "hard"
    OUT.append({"type": "club", "text": text, "answers": answers, "pct": pct, "why": why, "difficulty": diff, "category": cat, "tags": tags})

c(90, "Wordplay", ["alphabet"], "Which comes first in the alphabet: K or H?", ["H"], "H is the 8th letter, K the 11th.")
c(80, "Wordplay", ["anagrams"], "Rearrange the letters of EVIL to make a word meaning 'not dead'.", ["Live", "LIVE"], "E-V-I-L rearranges to L-I-V-E.")
c(70, "Numbers", ["money", "change"], "Three apples cost 20p each. What change do you get from £1?", ["40p", "40 pence", "£0.40"], "3 × 20p = 60p, and £1 − 60p = 40p.")
c(70, "Numbers", ["even numbers"], "Count on in twos from 98. What comes after it?", ["100", "One hundred"], "98 + 2 = 100.")
c(60, "Numbers", ["triangles", "corners"], "Five triangles: what's the total of their corners?", ["15", "Fifteen"], "5 × 3 = 15.")
c(50, "Numbers", ["multiplying", "comparing"], "Pick the larger product: three nines, or four sevens.", ["Four sevens", "4 × 7", "28"], "3 × 9 = 27, but 4 × 7 = 28.")
c(40, "Numbers", ["digits", "adding"], "Write seventy-seven in figures, then add its two digits together.", ["14", "Fourteen"], "7 + 7 = 14.")
c(20, "Numbers", ["primes"], "What's the biggest two-digit prime number?", ["97", "Ninety-seven"], "98 and 99 both have factors; 97 doesn't.")
c(10, "Numbers", ["time", "minutes"], "It's 22:45 on a 24-hour clock. How many minutes until midnight?", ["75", "Seventy-five"], "15 minutes to 23:00, then 60 more to midnight.")
c(90, "Numbers", ["legs", "furniture"], "A three-legged stool stands next to a four-legged chair. How many legs is that?", ["7", "Seven"], "3 + 4 = 7.")
c(20, "Numbers", ["area", "rectangles"], "A rectangle has an area of 24 square metres, and one side is 4 metres. How long is the other side?", ["6", "6 metres", "Six"], "24 ÷ 4 = 6.")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'club-15.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'club puzzles written')
