# Bank session 10 Oct 2026: more 1% Club puzzles -> bank/club-7.json. Logic, number and wordplay, each with a one-line
# "why". Tested against every club puzzle in the live bank with lqsql/neardup.py (a copy of the server's near-duplicate
# rule: word overlap of 80%, or 50% with the same answer) before importing.
import json, os
PCTS = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 1]
OUT = []
def c(pct, cat, tags, text, answers, why):
    assert pct in PCTS, (text, pct)
    diff = "easy" if pct >= 70 else "medium" if pct >= 40 else "hard"
    OUT.append({"type": "club", "text": text, "answers": answers, "pct": pct, "why": why, "difficulty": diff, "category": cat, "tags": tags})


c(90, "Numbers", ["multiplying"], "Multiply any number at all by zero. What do you get?", ["0", "Zero", "Nothing"], "Anything times zero is zero.")
c(90, "Numbers", ["apples", "adding"], "Ben has 3 apples and buys a dozen more. How many apples does he have now?", ["15", "Fifteen"], "A dozen is 12, and 3 + 12 = 15.")
c(80, "Numbers", ["legs", "insects"], "How many legs do two spiders and two ants have between them?", ["28", "Twenty-eight"], "Spiders have 8 legs and ants have 6: 16 + 12 = 28.")
c(80, "Wordplay", ["patterns", "letters"], "Skipping one letter each time: A, C, E, G. Which letter follows?", ["I"], "A (b) C (d) E (f) G (h) I.")
c(70, "Numbers", ["time"], "How many hours are there in three whole days?", ["72", "Seventy-two"], "24 × 3 = 72.")
c(60, "Numbers", ["clocks", "angles"], "At exactly three o'clock, what angle do a clock's two hands make?", ["90", "90 degrees", "A right angle"], "A quarter of the way round the face: 360 ÷ 4 = 90.")
c(50, "Numbers", ["patterns"], "Fill the gap in this run of numbers, each 4 apart: 3, 7, 11, __, 19", ["15", "Fifteen"], "11 + 4 = 15, and 15 + 4 = 19.")
c(40, "Numbers", ["time"], "From midnight to midnight, how many minutes tick by?", ["1440", "1,440"], "60 minutes × 24 hours = 1,440.")
c(40, "Wordplay", ["palindromes"], "Write RACECAR backwards. What word do you get?", ["Racecar", "RACECAR"], "It's a palindrome: it reads the same both ways.")
c(30, "Numbers", ["patterns"], "The gaps shrink by one each time: a hundred, 90, 81, 73. Which number follows?", ["66", "Sixty-six"], "The gaps are 10, 9, 8, so the next is 7: 73 − 7 = 66.")
c(30, "Logic", ["coins", "chance"], "Toss a coin three times in a row. How many different heads-and-tails sequences could you get?", ["8", "Eight"], "Two choices each time: 2 × 2 × 2 = 8.")
c(20, "Logic", ["ages", "sisters"], "Sally is 10 and her sister is half her age. When Sally is 70, how old will her sister be?", ["65", "Sixty-five"], "Her sister is 5 years younger, not half her age for ever: 70 − 5 = 65.")
c(20, "Numbers", ["prime numbers"], "What is the first prime number after 20?", ["23", "Twenty-three"], "21 = 3 × 7 and 22 = 2 × 11, but 23 has no factors.")
c(20, "Logic", ["trains", "tunnels"], "A train a mile long runs at a mile a minute into a tunnel a mile long. How many minutes from its front going in to its back coming out?", ["2", "Two", "2 minutes"], "The front must travel the tunnel's mile plus the train's own mile.")
c(10, "Logic", ["families"], "A man has three daughters, and each daughter has one brother. How many children does he have?", ["4", "Four"], "The daughters all share the same brother: 3 girls + 1 boy.")
c(5, "Numbers", ["powers"], "Which is bigger: 2 multiplied by itself ten times, or 10 cubed?", ["2 to the power 10", "2^10", "The first", "1024", "2 multiplied by itself ten times"], "2¹⁰ is 1,024, while 10³ is 1,000.")
c(1, "Wordplay", ["numbers", "letters"], "Spelt out in English, which number has as many letters as its own value?", ["Four", "4"], "F-O-U-R has four letters; no other number word matches itself.")

c(50, "Numbers", ["shapes", "corners"], "How many corners do a triangle and a hexagon have between them?", ["9", "Nine"], "3 + 6 = 9.")

c(70, "Wordplay", ["anagrams", "kitchen"], "Rearrange the letters of STOP to spell things you cook in.", ["Pots"], "S-T-O-P rearranges to POTS.")
c(30, "Wordplay", ["spelling", "letters"], "Spell out EXCELLENCE. Count its Es. What do you get?", ["4", "Four"], "E-x-c-E-l-l-E-n-c-E: four of them.")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'club-7.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'club puzzles written')
