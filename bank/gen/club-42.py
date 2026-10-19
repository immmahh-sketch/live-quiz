# Bank session 19 Oct 2026: more 1% Club puzzles -> bank/club-42.json. Logic, number and wordplay, each with a one-line
# "why" and short exact answers. Tested against every club puzzle in the live bank with lqsql/neardup.py (a copy of the
# server's near-duplicate rule) before importing; wording kept distinctive so a different puzzle isn't mistaken for an old one.
# Checked against the live club bank: no OWL, PARROT, beaver-dam, 1-to-30 or SWAN puzzles were there (1 to 50 with 3s was).
import json, os
PCTS = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 1]
OUT = []
def c(pct, cat, tags, text, answers, why):
    assert pct in PCTS, (text, pct)
    diff = "easy" if pct >= 70 else "medium" if pct >= 40 else "hard"
    OUT.append({"type": "club", "text": text, "answers": answers, "pct": pct, "why": why, "difficulty": diff, "category": cat, "tags": tags})

c(70, "Wordplay", ["anagrams", "birds"], "Rearrange the letters of OWL to make a word meaning 'not high'.", ["Low"], "O-W-L becomes L-O-W.")
c(30, "Wordplay", ["anagrams", "birds"], "Rearrange the letters of PARROT to make a word for a bird of prey, or a dinosaur.", ["Raptor"], "P-A-R-R-O-T becomes R-A-P-T-O-R.")
c(60, "Numbers", ["beavers", "dividing"], "A beaver dam grows 30 cm higher each week. How many weeks until it has grown 1.5 metres?", ["5", "Five", "5 weeks"], "1.5 m = 150 cm, and 150 ÷ 30 = 5.")
c(30, "Numbers", ["digits", "counting"], "Write out every number from 1 to 30. How many times do you write the digit 3?", ["4", "Four"], "3, 13, 23 and 30.")
c(50, "Wordplay", ["anagrams", "birds"], "Rearrange the letters of SWAN to make a word meaning 'cut with a saw'.", ["Sawn"], "S-W-A-N becomes S-A-W-N.")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'club-42.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'club puzzles written')
