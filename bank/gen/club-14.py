# Bank session 11 Oct 2026: more 1% Club puzzles -> bank/club-12.json. Logic, number and wordplay, each with a one-line
# "why". Tested against every club puzzle in the live bank with lqsql/neardup.py (a copy of the server's near-duplicate
# rule: word overlap of 80%, or 50% with the same answer) before importing.
import json, os
PCTS = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 1]
OUT = []
def c(pct, cat, tags, text, answers, why):
    assert pct in PCTS, (text, pct)
    diff = "easy" if pct >= 70 else "medium" if pct >= 40 else "hard"
    OUT.append({"type": "club", "text": text, "answers": answers, "pct": pct, "why": why, "difficulty": diff, "category": cat, "tags": tags})

c(90, "Numbers", ["legs", "spiders"], "A pair of spiders: how many legs in total?", ["16", "Sixteen"], "8 + 8 = 16.")
c(90, "Logic", ["weight", "comparing"], "Which is heavier: a kilo of sugar, or two kilos of feathers?", ["Two kilos of feathers", "2 kilos of feathers", "The feathers"], "Two kilos is more than one, whatever it's made of.")
c(70, "Wordplay", ["anagrams", "school"], "Unscramble HOCSOL to find somewhere children go on weekdays.", ["School"], "H-O-C-S-O-L rearranges to SCHOOL.")
c(70, "Numbers", ["times tables"], "What is nine nines, take away one?", ["80", "Eighty"], "9 × 9 = 81, minus 1 is 80.")
c(60, "Numbers", ["shapes", "perimeter"], "A rectangle measures 6 cm by 4 cm. How far is it all the way round?", ["20 cm", "20", "Twenty centimetres"], "6 + 4 + 6 + 4 = 20.")
c(60, "Wordplay", ["vowels", "counting"], "Count the vowels in ALPHABET.", ["3", "Three"], "A, A and E.")
c(50, "Logic", ["months", "calendar"], "Which month comes six months after March?", ["September"], "April, May, June, July, August, September.")
c(50, "Numbers", ["coins", "money"], "£1.50 in 5p pieces: how many coins is that?", ["30", "Thirty"], "150 ÷ 5 = 30.")
c(40, "Numbers", ["ages"], "Mia is twice as old as Leo. In four years Leo will be 10. How old is Mia now?", ["12", "Twelve"], "Leo is 6 now, so Mia is 12.")
c(40, "Numbers", ["fractions"], "Take half of sixty, then a third of that.", ["10", "Ten"], "Half of 60 is 30; a third of 30 is 10.")
c(20, "Logic", ["days", "calendar"], "Starting on a Monday, which weekday is it a hundred days later?", ["Wednesday"], "100 days is 14 weeks and 2 days, so two days on from Monday.")
c(10, "Numbers", ["shapes", "diagonals"], "How many diagonals can you draw inside a hexagon?", ["9", "Nine"], "Each of the 6 corners joins 3 others not next to it: 6 × 3 ÷ 2 = 9.")
c(5, "Numbers", ["pairs", "logic"], "Two whole numbers multiply to make 36 and add up to 13. What's the bigger one?", ["9", "Nine"], "9 × 4 = 36 and 9 + 4 = 13.")
c(1, "Numbers", ["multiplying", "zeros"], "Multiply together every whole number from 1 to 20. How many zeros are on the end of the answer?", ["4", "Four"], "Each zero needs a 5 paired with a 2, and 5, 10, 15 and 20 give four 5s.")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'club-12.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'club puzzles written')
