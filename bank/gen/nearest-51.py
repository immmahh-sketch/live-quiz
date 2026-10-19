# Bank session 19 Oct 2026: more Nearest Wins questions -> bank/nearest-51.json (start years of 2000s and 2010s dramas, Sherlock).
# (text, answer, unit, spread, difficulty, category, wow). Tested with lqsql/neardup-n.py (the server's near-duplicate rule) before
# importing; the count of Conan Doyle's Holmes stories was already in, so it's not here.
import json, os
Q = [
 ("In what year did Downton Abbey first open its doors on ITV?", 2010, "", 2, "medium", "Television", False),
 ("In what year did Tommy Shelby and Peaky Blinders first reach BBC Two?", 2013, "", 2, "medium", "Television", False),
 ("In what year did Sarah Lancashire first play Sergeant Catherine Cawood in Happy Valley?", 2014, "", 2, "medium", "Television", False),
 ("In what year did Call the Midwife first cycle onto BBC One?", 2012, "", 2, "medium", "Television", False),
 ("In what year did Martin Clunes first play Doc Martin on ITV?", 2004, "", 2, "medium", "Television", False),
 ("In what year did Channel 5's remake of All Creatures Great and Small begin?", 2020, "", 2, "medium", "Television", False),
 ("Counting the Victorian special, how many episodes of Sherlock were made with Benedict Cumberbatch?", 13, "episodes", 3, "hard", "Television", True),
 ("In what year was the first Sherlock Holmes story, A Study in Scarlet, published?", 1887, "", 6, "hard", "Books", False),
]
here = os.path.dirname(os.path.abspath(__file__))
out = [{"type": "nearest", "text": t, "answer": a, "unit": u, "spread": s, "difficulty": d, "category": c, "tags": ["nearest wins"] + (["wow"] if w else [])} for t, a, u, s, d, c, w in Q]
json.dump(out, open(os.path.join(here, '..', 'nearest-51.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'nearest written')
