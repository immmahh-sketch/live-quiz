# Bank session 19 Oct 2026: more 1% Club puzzles -> bank/club-41.json. Logic, number and wordplay, each with a one-line
# "why" and short exact answers. Tested against every club puzzle in the live bank with lqsql/neardup.py (a copy of the
# server's near-duplicate rule) before importing; wording kept distinctive so a different puzzle isn't mistaken for an old one.
# Checked against the live club bank: NIGHT/THING, EARTH/HEART, RACE/CARE and LEMON/MELON were already there.
import json, os
PCTS = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 1]
OUT = []
def c(pct, cat, tags, text, answers, why):
    assert pct in PCTS, (text, pct)
    diff = "easy" if pct >= 70 else "medium" if pct >= 40 else "hard"
    OUT.append({"type": "club", "text": text, "answers": answers, "pct": pct, "why": why, "difficulty": diff, "category": cat, "tags": tags})

c(60, "Wordplay", ["magpies", "rhymes"], "In the magpie rhyme that starts 'One for sorrow, two for joy', how many magpies are 'for a boy'?", ["4", "Four"], "One for sorrow, two for joy, three for a girl, four for a boy.")
c(50, "Wordplay", ["anagrams"], "Rearrange the letters of DUSTY to make a word for what you do before an exam.", ["Study"], "D-U-S-T-Y becomes S-T-U-D-Y.")
c(50, "Wordplay", ["anagrams"], "Rearrange the letters of PEACH to make a word meaning 'not expensive'.", ["Cheap"], "P-E-A-C-H becomes C-H-E-A-P.")
c(60, "Wordplay", ["anagrams"], "Rearrange the letters of SWORD to make a word for what a sentence is made of.", ["Words"], "S-W-O-R-D becomes W-O-R-D-S.")
c(60, "Numbers", ["kingfishers", "multiplying"], "A 40-gram kingfisher eats its own weight in fish every day. How many grams of fish is that in a week?", ["280", "280 grams", "280g"], "40 × 7 = 280.")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'club-41.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'club puzzles written')
