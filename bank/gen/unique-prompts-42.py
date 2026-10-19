# Bank session 19 Oct 2026: 3 more Only One prompts (Taskmaster champions of series 11 to 16, Britain's native conifers, birds of
# prey that breed in Britain) appended to bank/unique-prompts.json. Each is a closed list with every correct answer (other accepted
# forms after a slash), so a fair answer is never knocked out. Probed against the 721 prompts already in the pool (Taskmaster series
# 1 to 10 was already there, so this is the next run; nothing on conifers or birds of prey).
# Games are built from the pool with: GAMES=8 node tools/unique-stock.mjs
import json, os
NEW = [
 ("Name a Taskmaster series champion from series 11 to 16", ["Sarah Kendall", "Morgana Robinson", "Sophie Duker", "Dara Ó Briain/Dara O Briain/Dara O'Briain",
   "Mae Martin", "Sam Campbell"]),
 ("Name one of Britain's three native conifer trees", ["Scots pine/Scot's pine", "Yew/English yew", "Juniper/Common juniper"]),
 ("Name a bird of prey that breeds in Britain, not counting owls", ["Golden eagle", "White-tailed eagle/Sea eagle/White-tailed sea eagle", "Osprey",
   "Red kite/Kite", "Buzzard/Common buzzard", "Honey buzzard", "Marsh harrier", "Hen harrier", "Montagu's harrier", "Goshawk", "Sparrowhawk",
   "Kestrel", "Merlin", "Hobby", "Peregrine/Peregrine falcon"]),
]
here = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(here, '..', 'unique-prompts.json')
cur = json.load(open(path, encoding='utf-8'))
have = {x['p'].lower() for x in cur}
added = [{"p": p, "a": a} for p, a in NEW if p.lower() not in have]
json.dump(cur + added, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(added), 'prompts added; now', len(cur) + len(added))
