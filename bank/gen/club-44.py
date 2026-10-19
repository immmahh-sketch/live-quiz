# Bank session 19 Oct 2026: more 1% Club puzzles -> bank/club-44.json. Logic, number and wordplay on a British wildlife theme,
# each with a one-line "why" and short exact answers. Tested against every club puzzle in the live bank with lqsql/neardup.py
# (a copy of the server's near-duplicate rule) before importing. Dropped: the DEER/REED anagram (already in); the hare
# race says 'a hundred' because the rule matches any text containing 100 to a short old puzzle.
import json, os
PCTS = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 1]
OUT = []
def c(pct, cat, tags, text, answers, why):
    assert pct in PCTS, (text, pct)
    diff = "easy" if pct >= 70 else "medium" if pct >= 40 else "hard"
    OUT.append({"type": "club", "text": text, "answers": answers, "pct": pct, "why": why, "difficulty": diff, "category": cat, "tags": tags})

c(60, "Wordplay", ["anagrams", "hares"], "Rearrange the letters of HARE to make a word meaning 'listen to'.", ["Hear"], "H-A-R-E becomes H-E-A-R.")
c(60, "Wordplay", ["letters", "birds"], "Take one letter out of STARLING to make a word meaning 'looking hard'.", ["Staring"], "Drop the L: STARLING becomes STARING.")
c(50, "Numbers", ["speed", "gannets"], "A diving gannet hits 60 miles an hour. At that speed, how many miles would it cover in 5 minutes?", ["5", "Five", "5 miles"], "60 mph is a mile a minute, so 5 minutes is 5 miles.")
c(40, "Time", ["days", "owls"], "A barn owl lays an egg every other day. The first comes on a Monday. On which day does the fifth arrive?", ["Tuesday"], "Monday, Wednesday, Friday, Sunday, Tuesday.")
c(30, "Numbers", ["speed", "fables"], "A hare runs a hundred metres at 10 metres a second but naps for a minute halfway. A tortoise plods it at 1 metre a second. By how many seconds does the hare win?", ["30", "Thirty", "30 seconds"], "Hare: 5 + 60 + 5 = 70 seconds; tortoise: 100 seconds.")
c(20, "Numbers", ["legs", "logic"], "A field holds deer and pheasants: 20 heads and 56 legs in all. How many deer are there?", ["8", "Eight"], "If all 20 were pheasants that's 40 legs; the 16 extra legs are 2 per deer, so 8 deer.")
c(10, "Wordplay", ["letters", "alphabet", "birds"], "How many letters of the alphabet never appear in the word OYSTERCATCHER?", ["17", "Seventeen"], "It uses only nine different letters (O, Y, S, T, E, R, C, A, H); 26 − 9 = 17.")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'club-44.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'club puzzles written')
