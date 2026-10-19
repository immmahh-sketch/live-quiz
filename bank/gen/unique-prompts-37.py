# Bank session 19 Oct 2026: 3 more Only One prompts (Yes Minister main characters, Robot Wars house robots, the four roaring
# big cats) appended to bank/unique-prompts.json. Each is a closed list with every correct answer (other accepted forms after
# a slash), so a fair answer is never knocked out. Probed against the 707 prompts already in the pool (IT Crowd, Black Books
# and Inbetweeners characters were already there).
# Games are built from the pool with: GAMES=8 node tools/unique-stock.mjs
import json, os
NEW = [
 ("Name a main character from Yes Minister or Yes, Prime Minister", ["Jim Hacker/Hacker/Jim", "Sir Humphrey Appleby/Sir Humphrey/Humphrey/Appleby",
   "Bernard Woolley/Bernard/Woolley", "Annie Hacker/Annie", "Sir Arnold Robinson/Sir Arnold/Arnold", "Dorothy Wainwright/Dorothy"]),
 ("Name one of the house robots from Robot Wars", ["Sir Killalot/Killalot", "Matilda", "Shunt", "Dead Metal", "Sgt Bash/Sergeant Bash", "Mr Psycho",
   "Growler", "Refbot", "Cassius Chrome"]),
 ("Name one of the four big cats that can roar", ["Lion", "Tiger", "Leopard", "Jaguar"]),
]
here = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(here, '..', 'unique-prompts.json')
cur = json.load(open(path, encoding='utf-8'))
have = {x['p'].lower() for x in cur}
added = [{"p": p, "a": a} for p, a in NEW if p.lower() not in have]
json.dump(cur + added, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(added), 'prompts added; now', len(cur) + len(added))
