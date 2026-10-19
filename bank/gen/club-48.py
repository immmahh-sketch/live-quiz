# Bank session 19 Oct 2026: more 1% Club puzzles -> bank/club-48.json. Wordplay and number puzzles on actors' and dramas' names,
# each with a one-line "why" and short exact answers. Tested against every club puzzle in the live bank with lqsql/neardup.py
# (a copy of the server's near-duplicate rule) before importing.
import json, os
PCTS = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 1]
OUT = []
def c(pct, cat, tags, text, answers, why):
    assert pct in PCTS, (text, pct)
    diff = "easy" if pct >= 70 else "medium" if pct >= 40 else "hard"
    OUT.append({"type": "club", "text": text, "answers": answers, "pct": pct, "why": why, "difficulty": diff, "category": cat, "tags": tags})

c(70, "Wordplay", ["anagrams", "actors"], "Rearrange the letters of ELBA, as in Idris, to make a bundle of hay.", ["Bale"], "E-L-B-A becomes B-A-L-E.")
c(60, "Wordplay", ["anagrams", "James Bond"], "Rearrange the letters of CRAIG, as in Daniel, to make something you might smoke.", ["Cigar"], "C-R-A-I-G becomes C-I-G-A-R.")
c(40, "Wordplay", ["anagrams", "actors"], "Rearrange the letters of MADDEN, as in Richard, to make a word meaning 'condemned'.", ["Damned"], "M-A-D-D-E-N becomes D-A-M-N-E-D.")
c(40, "Numbers", ["Sherlock", "digits"], "Add up the digits of Sherlock's house number, 221, then multiply by the number of letters in SHERLOCK. What do you get?", ["40", "Forty"], "2 + 2 + 1 = 5, and SHERLOCK has 8 letters: 5 × 8 = 40.")
c(20, "Wordplay", ["letters", "Happy Valley"], "In the words HAPPY VALLEY, how many different letters appear exactly twice?", ["4", "Four"], "A, P, L and Y each appear twice; H, V and E once.")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'club-48.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'club puzzles written')
