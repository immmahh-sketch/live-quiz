# Bank session 19 Oct 2026: more 1% Club puzzles -> bank/club-38.json. Logic, number and wordplay, each with a one-line
# "why" and short exact answers. Tested against every club puzzle in the live bank with lqsql/neardup.py (a copy of the
# server's near-duplicate rule) before importing; wording kept distinctive so a different puzzle isn't mistaken for an old one.
# Checked against the live club bank: no eagle-speed, frogspawn, goat-vision, STEAM or spoonerism puzzles were there.
import json, os
PCTS = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 1]
OUT = []
def c(pct, cat, tags, text, answers, why):
    assert pct in PCTS, (text, pct)
    diff = "easy" if pct >= 70 else "medium" if pct >= 40 else "hard"
    OUT.append({"type": "club", "text": text, "answers": answers, "pct": pct, "why": why, "difficulty": diff, "category": cat, "tags": tags})

c(50, "Numbers", ["eagles", "speed"], "A golden eagle dives at 240 km an hour. How many kilometres would it cover in 15 minutes at that speed?", ["60", "60 km", "Sixty"], "15 minutes is a quarter of an hour: 240 ÷ 4 = 60.")
c(40, "Numbers", ["frogs", "halving"], "A clump of frogspawn holds 2,000 eggs. Half are eaten, and half of the rest never hatch. How many tadpoles are left?", ["500", "Five hundred"], "2,000 → 1,000 → 500.")
c(50, "Numbers", ["goats", "angles"], "A goat can see 320 degrees around itself. How many degrees of a full circle can't it see?", ["40", "40 degrees", "Forty"], "A full circle is 360 degrees: 360 − 320 = 40.")
c(40, "Wordplay", ["anagrams", "letters"], "Move the first letter of STEAM to the end. What new word do you get?", ["Teams"], "S-TEAM becomes TEAM-S.")
c(30, "Wordplay", ["spoonerisms"], "Swap the first letters of 'tons of soil'. What phrase do you get?", ["Sons of toil"], "T and S trade places: Sons of toil.")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'club-38.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'club puzzles written')
