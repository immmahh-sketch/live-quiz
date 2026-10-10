# Bank session 10 Oct 2026: 23 more 1% Club puzzles -> bank/club-5.json. Logic, number and wordplay, each with a
# one-line "why". Checked against every club puzzle already in the live bank, wording included (short questions that
# share most of their words with a live one are skipped by the server as near-duplicates).
import json, os
PCTS = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 1]
OUT = []
def c(pct, cat, tags, text, answers, why):
    assert pct in PCTS, (text, pct)
    diff = "easy" if pct >= 70 else "medium" if pct >= 40 else "hard"
    OUT.append({"type": "club", "text": text, "answers": answers, "pct": pct, "why": why, "difficulty": diff, "category": cat, "tags": tags})

c(90, "Numbers", ["shapes"], "How many sides do four hexagons have altogether?", ["24", "Twenty-four"], "A hexagon has 6 sides: 4 × 6 = 24.")
c(80, "Numbers", ["football"], "A team scores 2 goals before half-time and 3 after it, and lets in 4. By how many goals do they win?", ["1", "One"], "They score 5 and let in 4.")
c(80, "Numbers", ["money"], "A florist sells a dozen roses for £24. How much is that for each rose?", ["£2", "2", "2 pounds"], "£24 ÷ 12 = £2.")
c(80, "Numbers", ["time"], "How many minutes are there in two and a half hours?", ["150"], "60 + 60 + 30 = 150.")
c(70, "Numbers", ["fractions"], "Share 99 sweets equally between three children. How many does each child get?", ["33", "Thirty-three"], "99 ÷ 3 = 33.")
c(70, "Wordplay", ["anagrams", "months"], "Unscramble RAMCH to find a month of the year.", ["March"], "R-A-M-C-H makes MARCH.")
c(70, "Numbers", ["shapes"], "How many corners does a cube have?", ["8", "Eight"], "Four on the top face and four on the bottom.")
c(60, "Logic", ["riddles"], "What gets wetter the more it dries?", ["A towel", "Towel"], "A towel soaks up the water as it dries you.")
c(60, "Logic", ["riddles"], "What has a head and a tail but no body?", ["A coin", "Coin"], "Heads or tails!")
c(60, "Numbers", ["angles", "shapes"], "Add up the four angles inside a square. What do you get, in degrees?", ["360"], "Four right angles: 4 × 90 = 360.")
c(60, "Numbers", ["time"], "How long is a quarter of an hour, counted in seconds?", ["900"], "15 minutes × 60 seconds = 900.")
c(50, "Wordplay", ["months", "letters"], "Which month has the longest name, and how many letters is that?", ["9", "Nine", "September, 9"], "SEPTEMBER has nine letters; no month has more.")
c(50, "Logic", ["money", "percentages"], "A shop doubles all its prices, then holds a half-price sale. What does a £30 jumper cost in the sale?", ["£30", "30"], "Doubled to £60, then halved back to £30.")
c(40, "Numbers", ["percentages"], "What is 25% of 25% of 160?", ["10", "Ten"], "25% of 160 is 40, and 25% of 40 is 10.")
c(40, "Logic", ["shapes", "triangles"], "A triangle is cut by one straight line from a corner to the opposite side. How many triangles can you count now?", ["3", "Three"], "The two small ones, plus the big one they make together.")
c(30, "Numbers", ["fractions"], "Cut a cake in half, halve one piece, then halve that piece again. What fraction of the whole cake is your piece?", ["An eighth", "1/8", "One eighth", "0.125"], "½ × ½ × ½ = ⅛.")
c(30, "Wordplay", ["tricks"], "Say 'silk' out loud three times. Now: what do cows drink?", ["Water"], "Cows drink water; the silk makes you want to say milk.")
c(30, "Logic", ["tricks"], "How many birthdays does the average person have?", ["One", "1"], "You're only born once: the rest are anniversaries of it.")
c(20, "Logic", ["riddles", "mountains"], "Before Mount Everest was discovered, what was the highest mountain in the world?", ["Mount Everest", "Everest"], "It was still Everest, even before anyone measured it.")
c(20, "Numbers", ["algebra"], "Half of a number is 4 more than a third of it. What is the number?", ["24", "Twenty-four"], "12 is 4 more than 8: half of 24 and a third of 24.")
c(10, "Numbers", ["digits"], "Write out every number from 1 to 30. How many times do you write the digit 2?", ["13", "Thirteen"], "2, 12, 22 for the units, plus 20 to 29 for the tens: 3 + 10 = 13.")
c(5, "Numbers", ["squares", "cubes"], "Apart from 1, what is the smallest whole number that is both a square number and a cube number?", ["64", "Sixty-four"], "64 = 8 × 8 and 4 × 4 × 4.")
c(1, "Logic", ["clocks", "angles"], "Over twelve hours, how often do a clock's two hands form a perfect right angle?", ["22", "Twenty-two"], "Twice every hour, except around 3 and 9 where two of those moments fall together: 24 − 2 = 22.")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'club-5.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'club puzzles written')
