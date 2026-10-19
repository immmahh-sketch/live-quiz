# Bank session 19 Oct 2026: more Nearest Wins questions -> bank/nearest-48.json (sitcom years and British wildlife).
# (text, answer, unit, spread, difficulty, category, wow). Tested with lqsql/neardup-n.py (the server's near-duplicate rule)
# and lqsql/audit/tf-dupcheck.py before importing; none of these topics were in the nearest bank.
import json, os
Q = [
 ("Roughly how many million viewers watched the last episode of To the Manor Born's first series in 1979?", 24, "million", 4, "hard", "Comedy", True),
 ("In what year did Judi Dench and Geoffrey Palmer's As Time Goes By begin?", 1992, "", 3, "medium", "Comedy", False),
 ("In what year did Richard Briers's Ever Decreasing Circles begin?", 1984, "", 3, "hard", "Comedy", False),
 ("In what year did Simon Pegg and Jessica Hynes's Spaced begin on Channel 4?", 1999, "", 2, "medium", "Comedy", False),
 ("In what year did Man About the House begin on ITV?", 1973, "", 3, "medium", "Comedy", False),
 ("For roughly how many years were beavers missing from Britain before they came back?", 400, "years", 80, "hard", "Nature", True),
 ("By roughly what percentage have hazel dormouse numbers fallen in Britain since 2000?", 70, "%", 15, "hard", "Nature", True),
 ("Roughly how many breeding pairs of magpies are there in the UK?", 600000, "pairs", 150000, "hard", "Nature", False),
 ("Roughly how many grams does a kingfisher weigh?", 40, "grams", 10, "medium", "Nature", False),
 ("Roughly how many kinds of ladybird live in the UK?", 46, "kinds", 8, "hard", "Nature", True),
]
here = os.path.dirname(os.path.abspath(__file__))
out = [{"type": "nearest", "text": t, "answer": a, "unit": u, "spread": s, "difficulty": d, "category": c, "tags": ["nearest wins"] + (["wow"] if w else [])} for t, a, u, s, d, c, w in Q]
json.dump(out, open(os.path.join(here, '..', 'nearest-48.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'nearest written')
