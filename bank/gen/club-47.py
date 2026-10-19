# Bank session 19 Oct 2026: more 1% Club puzzles -> bank/club-47.json. Logic, number and wordplay on a TV detective and period drama
# theme, each with a one-line "why" and short exact answers. Tested against every club puzzle in the live bank with lqsql/neardup.py
# (a copy of the server's near-duplicate rule) before importing. Dropped: VERA to RAVE (already in).
import json, os
PCTS = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 1]
OUT = []
def c(pct, cat, tags, text, answers, why):
    assert pct in PCTS, (text, pct)
    diff = "easy" if pct >= 70 else "medium" if pct >= 40 else "hard"
    OUT.append({"type": "club", "text": text, "answers": answers, "pct": pct, "why": why, "difficulty": diff, "category": cat, "tags": tags})

c(70, "Logic", ["Downton Abbey", "ages"], "Lady Mary is older than Lady Edith, and Lady Sybil is younger than Edith. Which of the three sisters is in the middle?", ["Edith", "Lady Edith"], "Mary, then Edith, then Sybil.")
c(40, "Wordplay", ["anagrams", "detectives"], "Rearrange the letters of LUTHER to make a word meaning 'to rush along dangerously fast'.", ["Hurtle"], "L-U-T-H-E-R becomes H-U-R-T-L-E.")
c(40, "Numbers", ["Sherlock", "counting"], "Counting both ends, how many whole numbers are there from 200 to 221?", ["22", "Twenty-two"], "221 − 200 = 21, plus one because both ends count.")
c(20, "Wordplay", ["letters", "Downton Abbey"], "In the words DOWNTON ABBEY, how many different letters appear exactly twice?", ["3", "Three"], "O, N and B each appear twice; D, W, T, A, E and Y once.")
c(10, "Numbers", ["Morse code", "combinations"], "Morse code uses dots and dashes. How many different signals can be made from exactly two symbols?", ["4", "Four"], "Dot-dot, dot-dash, dash-dot and dash-dash.")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'club-47.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'club puzzles written')
