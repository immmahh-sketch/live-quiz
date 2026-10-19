# Bank session 19 Oct 2026: 3 more Only One prompts (the Walmington-on-Sea Home Guard platoon, the Chipmunks and Chipettes,
# Charlie's Angels) appended to bank/unique-prompts.json. Each is a closed list with every correct answer
# (other accepted forms after a slash), so a fair answer is never knocked out. Probed against the 728 prompts already in the pool
# (nothing on Dad's Army, the Chipmunks or Charlie's Angels; the Brady Bunch, Famous Five and Scooby gang are already there).
# Games are built from the pool with: GAMES=8 node tools/unique-stock.mjs
import json, os
NEW = [
 ("Name a member of the Home Guard platoon in Dad's Army", ["Mainwaring/Captain Mainwaring/George Mainwaring", "Wilson/Sergeant Wilson/Arthur Wilson",
   "Jones/Lance Corporal Jones/Corporal Jones/Jack Jones", "Frazer/Private Frazer/James Frazer", "Godfrey/Private Godfrey/Charles Godfrey",
   "Pike/Private Pike/Frank Pike", "Walker/Private Walker/Joe Walker"]),
 ("Name one of the Chipmunks or Chipettes", ["Alvin", "Simon", "Theodore", "Brittany", "Jeanette", "Eleanor"]),
 ("Name one of Charlie's Angels in the original 1970s TV series, or Charlie's assistant", ["Sabrina/Sabrina Duncan", "Jill/Jill Munroe", "Kelly/Kelly Garrett",
   "Kris/Kris Munroe", "Tiffany/Tiffany Welles", "Bosley/John Bosley"]),
]
here = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(here, '..', 'unique-prompts.json')
cur = json.load(open(path, encoding='utf-8'))
have = {x['p'].lower() for x in cur}
added = [{"p": p, "a": a} for p, a in NEW if p.lower() not in have]
json.dump(cur + added, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(added), 'prompts added; now', len(cur) + len(added))
