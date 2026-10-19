# Bank session 19 Oct 2026: 2 more Only One prompts (UK Wheel of Fortune or Big Break presenters, the four UK capitals)
# appended to bank/unique-prompts.json. Each is a closed list with every correct answer (other accepted forms after a slash),
# so a fair answer is never knocked out. Probed against the 713 prompts already in the pool (Bread, Friday Night Dinner and
# Birds of a Feather characters were already there).
# Games are built from the pool with: GAMES=8 node tools/unique-stock.mjs
import json, os
NEW = [
 ("Name a presenter of the UK Wheel of Fortune or of Big Break, up to 2025", ["Nicky Campbell/Campbell", "Bradley Walsh/Walsh", "John Leslie/Leslie",
   "Graham Norton/Norton", "Jim Davidson/Davidson", "John Virgo/Virgo"]),
 ("Name one of the four capital cities of the UK's nations", ["London", "Edinburgh", "Cardiff", "Belfast"]),
]
here = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(here, '..', 'unique-prompts.json')
cur = json.load(open(path, encoding='utf-8'))
have = {x['p'].lower() for x in cur}
added = [{"p": p, "a": a} for p, a in NEW if p.lower() not in have]
json.dump(cur + added, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(added), 'prompts added; now', len(cur) + len(added))
