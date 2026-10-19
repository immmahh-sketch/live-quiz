# Bank session 19 Oct 2026: more 1% Club puzzles -> bank/club-49.json. Wordplay, logic and number puzzles on a spy and sitcom theme,
# each with a one-line "why" and short exact answers. Tested against every club puzzle in the live bank with lqsql/neardup.py
# (a copy of the server's near-duplicate rule) before importing. Dropped: LISTEN to SILENT (already in).
import json, os
PCTS = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 1]
OUT = []
def c(pct, cat, tags, text, answers, why):
    assert pct in PCTS, (text, pct)
    diff = "easy" if pct >= 70 else "medium" if pct >= 40 else "hard"
    OUT.append({"type": "club", "text": text, "answers": answers, "pct": pct, "why": why, "difficulty": diff, "category": cat, "tags": tags})

c(60, "Numbers", ["Killing Eve", "multiplying"], "Killing Eve ran for 4 series of 8 episodes each. How many episodes is that altogether?", ["32", "Thirty-two"], "4 × 8 = 32.")
c(50, "Time", ["Spooks", "clocks"], "A 60-minute episode of Spooks starts at 9:00pm, and the news follows it 5 minutes later. What time does the news start?", ["10:05", "10:05pm", "10.05", "Five past ten"], "9:00 + 60 minutes = 10:00, plus 5 minutes = 10:05.")
c(40, "Wordplay", ["letters", "Killing Eve"], "The assassin in Killing Eve is called VILLANELLE. Count its distinct letters: how many is that?", ["6", "Six"], "V, I, L, A, N and E.")
c(30, "Logic", ["detectives", "swaps"], "Sherlock, Luther and Morse each own one of a violin, a coat and a Jaguar. Sherlock owns neither the coat nor the Jaguar, and Luther doesn't own the coat. Who owns the coat?", ["Morse"], "Sherlock has the violin; Luther isn't the coat, so he has the Jaguar; that leaves the coat for Morse.")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'club-49.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'club puzzles written')
