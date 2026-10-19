# Bank session 19 Oct 2026: 3 more Only One prompts (the Garvey family in Benidorm, Dinnerladies' main characters, the six
# Horrible Histories stars who wrote Ghosts) appended to bank/unique-prompts.json. Each is a closed list with every correct
# answer (other accepted forms after a slash), so a fair answer is never knocked out. Probed against the 710 prompts already
# in the pool (Bottom, Ghosts, Rab C. Nesbitt and Still Game characters were already there).
# Games are built from the pool with: GAMES=8 node tools/unique-stock.mjs
import json, os
NEW = [
 ("Name a member of the Garvey family in Benidorm", ["Mick/Mick Garvey", "Janice/Janice Garvey", "Chantelle/Chantelle Garvey", "Michael/Michael Garvey",
   "Madge/Madge Harvey"]),
 ("Name a main character from Dinnerladies", ["Bren", "Tony", "Dolly", "Jean", "Twinkle", "Anita", "Philippa", "Stan", "Petula"]),
 ("Name one of the six Horrible Histories stars who write and star in Ghosts", ["Mathew Baynton/Matthew Baynton/Baynton", "Simon Farnaby/Farnaby",
   "Martha Howe-Douglas/Howe-Douglas", "Jim Howick/Howick", "Laurence Rickard/Rickard", "Ben Willbond/Willbond"]),
]
here = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(here, '..', 'unique-prompts.json')
cur = json.load(open(path, encoding='utf-8'))
have = {x['p'].lower() for x in cur}
added = [{"p": p, "a": a} for p, a in NEW if p.lower() not in have]
json.dump(cur + added, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(added), 'prompts added; now', len(cur) + len(added))
