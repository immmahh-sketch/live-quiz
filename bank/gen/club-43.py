# Bank session 19 Oct 2026: more 1% Club puzzles -> bank/club-43.json. Logic, number and wordplay, each with a one-line
# "why" and short exact answers. Tested against every club puzzle in the live bank with lqsql/neardup.py (a copy of the
# server's near-duplicate rule) before importing. Dropped as already in: the smallest number 2-6 divide into, and the
# two-digit number three times its digit sum; three others reworded so the rule doesn't mistake them for different old puzzles.
import json, os
PCTS = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 1]
OUT = []
def c(pct, cat, tags, text, answers, why):
    assert pct in PCTS, (text, pct)
    diff = "easy" if pct >= 70 else "medium" if pct >= 40 else "hard"
    OUT.append({"type": "club", "text": text, "answers": answers, "pct": pct, "why": why, "difficulty": diff, "category": cat, "tags": tags})

c(70, "Numbers", ["squares", "odd one out"], "Spot the number here that isn't a perfect square: 9, 16, 25, 36, 48, 64.", ["48"], "The others are square numbers (3×3 up to 8×8); 48 isn't.")
c(70, "Numbers", ["shapes", "adding"], "Count every edge you'd draw for three triangles and two squares, none touching.", ["17", "Seventeen"], "3 × 3 = 9 and 2 × 4 = 8, so 17.")
c(50, "Numbers", ["animals", "legs"], "Multiply a spider's legs by an ant's legs, then take away a horse's legs. What's left?", ["44", "Forty-four"], "8 × 6 = 48, and 48 − 4 = 44.")
c(40, "Time", ["timetables", "Metro", "North East"], "A Metro train leaves at 7:00 and then every 12 minutes. Counting the 7:00, how many leave before 8:00?", ["5", "Five"], "7:00, 7:12, 7:24, 7:36 and 7:48; the next is 8:00.")
c(30, "Wordplay", ["letters", "North East"], "Spell out NEWCASTLE, then SUNDERLAND. Which letters turn up in the first word only? Give how many.", ["3", "Three"], "W, C and T; N, E, A, S and L are in both.")
c(20, "Numbers", ["digits", "logic"], "I'm a three-digit number. My digits add up to 2, and I'm odd. What am I?", ["101"], "Only 101, 110 and 200 have digits adding to 2, and only 101 is odd.")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'club-43.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'club puzzles written')
