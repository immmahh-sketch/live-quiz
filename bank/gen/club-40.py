# Bank session 19 Oct 2026: more 1% Club puzzles -> bank/club-40.json. Logic, number and wordplay, each with a one-line
# "why" and short exact answers. Tested against every club puzzle in the live bank with lqsql/neardup.py (a copy of the
# server's near-duplicate rule) before importing; wording kept distinctive so a different puzzle isn't mistaken for an old one.
# Checked against the live club bank: HORSE/SHORE was already there.
import json, os
PCTS = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 1]
OUT = []
def c(pct, cat, tags, text, answers, why):
    assert pct in PCTS, (text, pct)
    diff = "easy" if pct >= 70 else "medium" if pct >= 40 else "hard"
    OUT.append({"type": "club", "text": text, "answers": answers, "pct": pct, "why": why, "difficulty": diff, "category": cat, "tags": tags})

c(50, "Numbers", ["swallows", "dividing"], "A swallow flies 10,000 km to South Africa in 50 days. On average, how far does it fly each day?", ["200 km", "200"], "10,000 ÷ 50 = 200.")
c(50, "Numbers", ["moles", "dividing"], "A mole digs 20 metres of tunnel a day. How many days would it take to dig a kilometre?", ["50", "50 days", "Fifty"], "1,000 ÷ 20 = 50.")
c(60, "Wordplay", ["anagrams"], "Rearrange the letters of BREAD to make something that grows on a man's chin.", ["Beard"], "B-R-E-A-D becomes B-E-A-R-D.")
c(70, "Wordplay", ["anagrams"], "Rearrange the letters of SEAL to make a word for a time when shops cut their prices.", ["Sale"], "S-E-A-L becomes S-A-L-E.")
c(60, "Wordplay", ["anagrams"], "Rearrange the letters of DEER to make a tall plant that grows by water.", ["Reed"], "D-E-E-R becomes R-E-E-D.")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'club-40.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'club puzzles written')
