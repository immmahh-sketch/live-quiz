# Bank session 18 Oct 2026: more Nearest Wins questions -> bank/nearest-39.json. A first draft (Orkney islands, heartbeats,
# Statue of Liberty, Scrabble squares, Tube stations, Channel Tunnel, Highway Code, Sunderland city status, Grey's Monument,
# Caledonian Canal locks, speed of sound) was all in the bank already, so only less familiar numbers are here; a second
# batch lost dominoes, a firkin, Ribblehead, the Royal Border Bridge, the Monument's steps, Munros, the Pennine Way and the Wall path the same way.
# (text, answer, unit, spread, difficulty, category, wow). Tested against the live bank with lqsql/neardup-n.py (a copy of the
# server's near-duplicate rule) and against every true/false, choice and text question (lqsql/audit/tf-dupcheck.py) first.
import json, os
Q = [
 ("A typical golf ball has about how many dimples?", 336, "dimples", 60, "hard", "Sport", True),
 ("How many countries are members of the Commonwealth?", 56, "countries", 6, "medium", "World geography", False),
 ("How many white hexagons are there on a classic black-and-white football?", 20, "hexagons", 4, "medium", "Sport", True),
 ("How many sheets of paper are in a ream?", 500, "sheets", 100, "medium", "Everyday life", False),
 ("How many points does the Commonwealth Star on Australia's flag have?", 7, "points", 1, "hard", "World geography", False),
 ("How tall is Blackpool Tower, in metres?", 158, "metres", 20, "medium", "UK geography", False),
]
here = os.path.dirname(os.path.abspath(__file__))
out = [{"type": "nearest", "text": t, "answer": a, "unit": u, "spread": s, "difficulty": d, "category": c, "tags": ["nearest wins"] + (["wow"] if w else [])} for t, a, u, s, d, c, w in Q]
json.dump(out, open(os.path.join(here, '..', 'nearest-39.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'nearest written')
