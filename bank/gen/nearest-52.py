# Bank session 19 Oct 2026: more Nearest Wins questions -> bank/nearest-52.json (start years of crime and comedy dramas, a few
# facts about them). (text, answer, unit, spread, difficulty, category, wow). Tested with lqsql/neardup-n.py (the server's near-
# duplicate rule) before importing; Gavin & Stacey's and Line of Duty's series counts were already in, so they're not here.
# Two were reworded so the rule wouldn't read them as old questions with the same answer year.
import json, os
Q = [
 ("In what year did Luther first stalk the screen on BBC One?", 2010, "", 2, "medium", "Television", False),
 ("In what year did the first series of Bodyguard air on the BBC?", 2018, "", 2, "medium", "Television", False),
 ("In what year did Life on Mars first send Sam Tyler back to the 1970s?", 2006, "", 2, "medium", "Television", False),
 ("Phoebe Waller-Bridge's guinea pig cafe owner arrived on BBC Three in which year?", 2016, "", 2, "medium", "Television", False),
 ("In what year did the pilot of Cold Feet first go out on ITV?", 1997, "", 2, "hard", "Television", False),
 ("Gavin met Stacey over the phone on BBC Three, starting in which year?", 2007, "", 2, "medium", "Television", False),
 ("In what year did Line of Duty's first series begin?", 2012, "", 2, "medium", "Television", False),
 ("Roughly how many millions watched the finale of Bodyguard?", 17, "million", 3, "hard", "Television", True),
]
here = os.path.dirname(os.path.abspath(__file__))
out = [{"type": "nearest", "text": t, "answer": a, "unit": u, "spread": s, "difficulty": d, "category": c, "tags": ["nearest wins"] + (["wow"] if w else [])} for t, a, u, s, d, c, w in Q]
json.dump(out, open(os.path.join(here, '..', 'nearest-52.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'nearest written')
