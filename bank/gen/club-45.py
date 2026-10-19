# Bank session 19 Oct 2026: more 1% Club puzzles -> bank/club-45.json. Logic, number and wordplay on a soap and TV-detective theme,
# each with a one-line "why" and short exact answers. Tested against every club puzzle in the live bank with lqsql/neardup.py
# (a copy of the server's near-duplicate rule) before importing.
import json, os
PCTS = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 1]
OUT = []
def c(pct, cat, tags, text, answers, why):
    assert pct in PCTS, (text, pct)
    diff = "easy" if pct >= 70 else "medium" if pct >= 40 else "hard"
    OUT.append({"type": "club", "text": text, "answers": answers, "pct": pct, "why": why, "difficulty": diff, "category": cat, "tags": tags})

c(70, "Numbers", ["Neighbours", "years"], "Kylie Minogue was born in 1968 and started playing Charlene at 18. In which year did she start?", ["1986"], "1968 + 18 = 1986.")
c(60, "Logic", ["detectives", "cars"], "Morse, Frost and Taggart each drive one of a Jaguar, a Ford and a Vauxhall. Morse drives the Jaguar, and Frost doesn't drive the Vauxhall. Who drives the Vauxhall?", ["Taggart"], "Morse has the Jaguar, so Frost has the Ford, leaving the Vauxhall for Taggart.")
c(40, "Time", ["soaps", "days"], "A soap is shown every Monday, Wednesday and Friday. Episode 1 goes out on a Monday. On which day is episode 10 shown?", ["Monday"], "Episodes 1, 4, 7 and 10 all fall on Mondays.")
c(30, "Wordplay", ["letters", "alphabet"], "F comes a certain number of letters before M in the alphabet. Which letter comes the same number of letters after M?", ["T"], "F is 7 before M, and 7 after M is T.")
c(30, "Wordplay", ["letters", "soaps"], "Count every letter E in EMMERDALE, EASTENDERS and NEIGHBOURS put together. How many is that?", ["7", "Seven"], "EMMERDALE has 3, EASTENDERS has 3 and NEIGHBOURS has 1.")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'club-45.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'club puzzles written')
