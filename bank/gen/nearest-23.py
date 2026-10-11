# Bank session 11 Oct 2026: more Nearest Wins questions -> bank/nearest-23.json: sporting tallies.
# (text, answer, unit, spread, difficulty, category, wow). Tested against the live bank with a copy of the server's near-duplicate rule first.
import json, os
Q = [
 ("How many Grand Slam singles titles did Steffi Graf win?", 22, "titles", 4, "medium", "Sport", False),
 ("How many golf majors did Jack Nicklaus win?", 18, "majors", 4, "medium", "Sport", False),
 ("How many Olympic gold medals did Jason Kenny win?", 7, "golds", 2, "medium", "Sport", False),
 ("How many Olympic gold medals did Laura Kenny win?", 5, "golds", 2, "medium", "Sport", False),
 ("How many Ballon d'Or awards has Cristiano Ronaldo won?", 5, "awards", 2, "medium", "Football", False),
 ("Newcastle's FA Cup wins: what's the total?", 6, "times", 2, "medium", "Football", False),
 ("How many Formula One world titles did Michael Schumacher win?", 7, "titles", 2, "easy", "Sport", False),
 ("How many golf majors has Tiger Woods won?", 15, "majors", 3, "medium", "Sport", False),
 ("How many times have England won the men's Rugby World Cup?", 1, "times", 1, "easy", "Sport", False),
]
here = os.path.dirname(os.path.abspath(__file__))
out = [{"type": "nearest", "text": t, "answer": a, "unit": u, "spread": s, "difficulty": d, "category": c, "tags": ["nearest wins"] + (["wow"] if w else [])} for t, a, u, s, d, c, w in Q]
json.dump(out, open(os.path.join(here, '..', 'nearest-23.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'nearest written')
