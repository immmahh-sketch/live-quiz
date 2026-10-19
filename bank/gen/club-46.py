# Bank session 19 Oct 2026: more 1% Club puzzles -> bank/club-46.json. Logic, number and wordplay on an islands and seaside theme,
# each with a one-line "why" and short exact answers. Tested against every club puzzle in the live bank with lqsql/neardup.py
# (a copy of the server's near-duplicate rule) before importing.
import json, os
PCTS = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 1]
OUT = []
def c(pct, cat, tags, text, answers, why):
    assert pct in PCTS, (text, pct)
    diff = "easy" if pct >= 70 else "medium" if pct >= 40 else "hard"
    OUT.append({"type": "club", "text": text, "answers": answers, "pct": pct, "why": why, "difficulty": diff, "category": cat, "tags": tags})

c(70, "Wordplay", ["anagrams", "islands"], "Rearrange the letters of SKYE to make the things you open a lock with.", ["Keys"], "S-K-Y-E becomes K-E-Y-S.")
c(60, "Wordplay", ["anagrams", "islands"], "Rearrange the letters of BUTE, a Scottish island, to make a nickname for the London Underground.", ["Tube"], "B-U-T-E becomes T-U-B-E.")
c(50, "Time", ["ferries", "islands"], "A ferry to Lundy leaves at 9:15am and takes 2 hours 50 minutes. What time does it arrive?", ["12:05", "12:05pm", "12.05", "Five past twelve"], "9:15 + 2 hours = 11:15, then 50 minutes more = 12:05.")
c(40, "Numbers", ["seaside", "multiplying"], "A cliff lift carries 12 people a trip, and each round trip takes 4 minutes. How many people can it take up in an hour?", ["180"], "60 ÷ 4 = 15 trips, and 15 × 12 = 180.")
c(30, "Numbers", ["birds", "logic"], "On a cliff there are 31 seabirds: puffins and gulls. There are 7 more gulls than puffins. How many puffins?", ["12", "Twelve"], "Take away the 7 extra gulls: 24 left, split evenly, so 12 puffins and 19 gulls.")
c(20, "Wordplay", ["letters", "islands"], "Which single letter can go in front of SLAY to make the name of a Scottish island?", ["I", "Islay"], "I + SLAY = ISLAY.")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'club-46.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'club puzzles written')
