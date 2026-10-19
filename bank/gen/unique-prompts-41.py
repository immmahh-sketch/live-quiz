# Bank session 19 Oct 2026: 4 more Only One prompts (British wildlife: native reptiles, native amphibians, breeding owls,
# wild deer) appended to bank/unique-prompts.json. Each is a closed list with every correct answer (other accepted forms after
# a slash), so a fair answer is never knocked out. Probed against the 717 prompts already in the pool (the crow family was
# already there; nothing on reptiles, amphibians, owls or deer).
# Games are built from the pool with: GAMES=8 node tools/unique-stock.mjs
import json, os
NEW = [
 ("Name one of Britain's native land reptiles", ["Adder/Viper", "Grass snake/Barred grass snake", "Smooth snake", "Slow worm/Slow-worm",
   "Common lizard/Viviparous lizard", "Sand lizard"]),
 ("Name one of Britain's native frogs, toads or newts", ["Common frog", "Pool frog", "Common toad", "Natterjack toad/Natterjack",
   "Smooth newt/Common newt", "Palmate newt", "Great crested newt/Crested newt"]),
 ("Name one of the five owls that regularly breed in Britain", ["Barn owl", "Tawny owl", "Little owl", "Long-eared owl", "Short-eared owl"]),
 ("Name a species of deer that lives wild in Britain", ["Red deer/Red", "Roe deer/Roe", "Fallow deer/Fallow", "Sika deer/Sika",
   "Muntjac/Muntjac deer/Reeves's muntjac", "Chinese water deer/Water deer"]),
]
here = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(here, '..', 'unique-prompts.json')
cur = json.load(open(path, encoding='utf-8'))
have = {x['p'].lower() for x in cur}
added = [{"p": p, "a": a} for p, a in NEW if p.lower() not in have]
json.dump(cur + added, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(added), 'prompts added; now', len(cur) + len(added))
