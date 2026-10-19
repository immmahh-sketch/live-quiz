# Bank session 19 Oct 2026: 2 Categorise questions -> bank/sort-72.json. Each pair of categories was probed against every
# Categorise question in the live bank first (no Taskmaster, Countdown-host or Fifteen to One sorts were there).
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

# Bill Bailey is the trap: a comedian who won Strictly (2020)
s("Television", ["Taskmaster", "Strictly Come Dancing", "champions"], "hard", "A Taskmaster champion or a Strictly champion?", "Taskmaster", "Strictly",
  ["Josh Widdicombe", "Rob Beckett", "Kerry Godliman", "Liza Tarbuck"], ["Bill Bailey", "Jill Halfpenny", "Chris Hollins", "Kelvin Fletcher"])
s("Television", ["Countdown", "Fifteen to One", "quiz hosts"], "medium", "Has hosted Countdown or has hosted Fifteen to One?", "Countdown", "Fifteen to One",
  ["Richard Whiteley", "Des Lynam", "Nick Hewer", "Colin Murray"], ["William G. Stewart", "Adam Hills", "Sandi Toksvig"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-72.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
