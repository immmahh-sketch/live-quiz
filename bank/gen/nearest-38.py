# Bank session 12 Oct 2026: more Nearest Wins questions -> bank/nearest-38.json: Anglo-Saxon dates, whisky, jazz, bread, chippies.
# (text, answer, unit, spread, difficulty, category, wow). Tested against the live bank with a copy of the server's near-duplicate rule first.
import json, os
Q = [
 ("The Synod of Whitby, which settled how to date Easter, met in which year?", 664, "", 10, "hard", "History", False),
 ("St Cuthbert, Northumbria's favourite saint, died in which year?", 687, "", 15, "hard", "History", False),
 ("Athelstan became the first king of all England in which year?", 927, "", 15, "hard", "History", False),
 ("Alfred the Great died in which year?", 899, "", 15, "hard", "History", False),
 ("By law, Scotch whisky must be aged in oak casks for at least how many years?", 3, "years", 1, "medium", "Beer, wine and spirits", False),
 ("Louis Armstrong's 'What a Wonderful World' came out in which year?", 1967, "", 4, "medium", "Music", False),
 ("Ronnie Scott's, London's famous jazz club, threw open its doors in what year?", 1959, "", 5, "hard", "Music", False),
 ("Chicago first dyed its river green for St Patrick's Day in which year?", 1962, "", 6, "hard", "World geography", True),
 ("The Chorleywood process, behind most of Britain's sliced bread, was invented in which year?", 1961, "", 6, "hard", "Food and drink", True),
 ("Roughly how many fish and chip shops are there in the UK?", 10500, "shops", 1500, "medium", "Food and drink", False),
]
here = os.path.dirname(os.path.abspath(__file__))
out = [{"type": "nearest", "text": t, "answer": a, "unit": u, "spread": s, "difficulty": d, "category": c, "tags": ["nearest wins"] + (["wow"] if w else [])} for t, a, u, s, d, c, w in Q]
json.dump(out, open(os.path.join(here, '..', 'nearest-38.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'nearest written')
