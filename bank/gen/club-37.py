# Bank session 19 Oct 2026: more 1% Club puzzles -> bank/club-37.json. Logic, number and wordplay, each with a one-line
# "why" and short exact answers. Tested against every club puzzle in the live bank with lqsql/neardup.py (a copy of the
# server's near-duplicate rule) before importing; wording kept distinctive so a different puzzle isn't mistaken for an old one.
# Dropped as already in the bank: LISTEN/SILENT, unbeaten on 22 points, the Invincibles' draws, ASTRONOMER = MOON STARER.
import json, os
PCTS = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 1]
OUT = []
def c(pct, cat, tags, text, answers, why):
    assert pct in PCTS, (text, pct)
    diff = "easy" if pct >= 70 else "medium" if pct >= 40 else "hard"
    OUT.append({"type": "club", "text": text, "answers": answers, "pct": pct, "why": why, "difficulty": diff, "category": cat, "tags": tags})

c(60, "Numbers", ["tortoises", "speed"], "A tortoise plods along at 0.3 km an hour. How long does it take to cover 1.5 km?", ["5 hours", "5", "Five hours"], "1.5 ÷ 0.3 = 5.")
c(50, "Numbers", ["koalas", "time"], "A koala sleeps 20 hours a day. How many hours is it awake in a week?", ["28", "28 hours"], "4 hours a day × 7 days = 28.")
c(30, "Numbers", ["seesaw", "balance"], "On a seesaw, a 30 kg child sits 2 metres from the middle. How far from the middle must a 60 kg adult sit on the other side to balance?", ["1 metre", "1", "1m", "One metre"], "Twice the weight needs half the distance: 30 × 2 = 60 × 1.")
c(40, "Wordplay", ["anagrams"], "Rearrange the letters of THE EYES into two words that say what they do.", ["They see"], "T-H-E-E-Y-E-S makes THEY SEE.")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'club-37.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'club puzzles written')
