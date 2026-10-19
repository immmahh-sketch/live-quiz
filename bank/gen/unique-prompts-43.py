# Bank session 19 Oct 2026: 3 more Only One prompts (the Small Isles, the Grant family of Brookside, the main characters of The
# Professionals) appended to bank/unique-prompts.json. Each is a closed list with every correct answer (other accepted forms after
# a slash), so a fair answer is never knocked out. Probed against the 724 prompts already in the pool (Channel Islands, Scilly and
# the Royle family were already there; nothing on these).
# Games are built from the pool with: GAMES=8 node tools/unique-stock.mjs
import json, os
NEW = [
 ("Name one of Scotland's Small Isles", ["Rum/Rhum", "Eigg", "Muck", "Canna", "Sanday"]),
 ("Name a member of the Grant family in Brookside", ["Bobby/Bobby Grant", "Sheila/Sheila Grant", "Barry/Barry Grant", "Damon/Damon Grant",
   "Karen/Karen Grant", "Claire/Claire Grant"]),
 ("Name one of the three main characters in The Professionals", ["Bodie/William Bodie", "Doyle/Ray Doyle", "Cowley/George Cowley"]),
]
here = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(here, '..', 'unique-prompts.json')
cur = json.load(open(path, encoding='utf-8'))
have = {x['p'].lower() for x in cur}
added = [{"p": p, "a": a} for p, a in NEW if p.lower() not in have]
json.dump(cur + added, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(added), 'prompts added; now', len(cur) + len(added))
