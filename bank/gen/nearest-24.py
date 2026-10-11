# Bank session 11 Oct 2026: more Nearest Wins questions -> bank/nearest-24.json: chart runs, TV series and book counts.
# (text, answer, unit, spread, difficulty, category, wow). Tested against the live bank with a copy of the server's near-duplicate rule first.
import json, os
Q = [
 ("How many players started the very first series of The Traitors?", 22, "players", 5, "hard", "TV", False),
 ("How many series of Breaking Bad were made?", 5, "series", 2, "medium", "TV", False),
 ("How many Discworld novels did Terry Pratchett write?", 41, "novels", 8, "hard", "Books", False),
 ("Novels and short stories together: how many Sherlock Holmes stories did Conan Doyle write?", 60, "stories", 12, "hard", "Books", True),
 ("In how many novels does Hercule Poirot appear?", 33, "novels", 8, "hard", "Books", False),
 ("How many James Bond novels did Ian Fleming write, story collections left out?", 12, "novels", 3, "hard", "Books", False),
 ("How many series of the original Gavin & Stacey were there, specials left out?", 3, "series", 1, "medium", "TV", False),
 ("How many episodes of The Office (UK) were there, specials left out?", 12, "episodes", 3, "hard", "TV", False),
]
here = os.path.dirname(os.path.abspath(__file__))
out = [{"type": "nearest", "text": t, "answer": a, "unit": u, "spread": s, "difficulty": d, "category": c, "tags": ["nearest wins"] + (["wow"] if w else [])} for t, a, u, s, d, c, w in Q]
json.dump(out, open(os.path.join(here, '..', 'nearest-24.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'nearest written')
