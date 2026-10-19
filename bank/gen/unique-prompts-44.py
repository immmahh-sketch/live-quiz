# Bank session 19 Oct 2026: 2 more Only One prompts (the Shelby siblings, the Crawley sisters) appended to bank/unique-prompts.json.
# Each is a closed list with every correct answer (other accepted forms after a slash), so a fair answer is never knocked out.
# Probed against the 727 prompts already in the pool (a Shelby siblings prompt was already there, so only the Crawley sisters went in).
# Games are built from the pool with: GAMES=8 node tools/unique-stock.mjs
import json, os
NEW = [
 ("Name one of the three Crawley sisters in Downton Abbey", ["Mary/Lady Mary", "Edith/Lady Edith", "Sybil/Lady Sybil"]),
]
here = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(here, '..', 'unique-prompts.json')
cur = json.load(open(path, encoding='utf-8'))
have = {x['p'].lower() for x in cur}
added = [{"p": p, "a": a} for p, a in NEW if p.lower() not in have]
json.dump(cur + added, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(added), 'prompts added; now', len(cur) + len(added))
