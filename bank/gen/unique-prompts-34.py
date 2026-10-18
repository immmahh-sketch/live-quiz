# Bank session 18 Oct 2026: 5 more Only One prompts (Mastermind presenters, Bullseye hosts, the Village People characters,
# Thunderbirds craft, Blackadder series and specials) appended to bank/unique-prompts.json. Each is a closed list with every
# correct answer (other accepted forms after a slash), so a fair answer is never knocked out. Probed against the 695 prompts
# already in the pool (Countdown presenters, International Rescue's members and Blackadder characters were already there).
# Games are built from the pool with: GAMES=8 node tools/unique-stock.mjs
import json, os
NEW = [
 ("Name a presenter of Mastermind on TV or radio, up to 2025", ["Magnus Magnusson/Magnusson", "Peter Snow", "Clive Anderson", "John Humphrys/Humphrys", "Clive Myrie/Myrie"]),
 ("Name a host of Bullseye, up to 2025", ["Jim Bowen/Bowen", "Dave Spikey/Spikey", "Freddie Flintoff/Andrew Flintoff/Flintoff"]),
 ("Name one of the Village People's characters", ["Cop/Policeman/Police officer", "Cowboy", "Construction worker/Builder/Hard hat", "Biker/Leatherman/Leather man",
   "Native American/Indian/Indian chief/Chief", "Soldier/GI/G.I./Sailor/Military man"]),
 ("Name one of the Thunderbirds craft, or Lady Penelope's car", ["Thunderbird 1/Thunderbird One", "Thunderbird 2/Thunderbird Two", "Thunderbird 3/Thunderbird Three",
   "Thunderbird 4/Thunderbird Four", "Thunderbird 5/Thunderbird Five", "FAB 1/FAB1/FAB One"]),
 ("Name a Blackadder series or special", ["The Black Adder/Black Adder/Blackadder I/Blackadder 1", "Blackadder II/Blackadder 2", "Blackadder the Third/Blackadder III/Blackadder 3",
   "Blackadder Goes Forth/Blackadder IV/Blackadder 4", "Blackadder's Christmas Carol/Blackadder Christmas Carol", "Blackadder: The Cavalier Years/The Cavalier Years/Cavalier Years",
   "Blackadder: Back & Forth/Blackadder Back and Forth/Back & Forth/Back and Forth"]),
]
here = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(here, '..', 'unique-prompts.json')
cur = json.load(open(path, encoding='utf-8'))
have = {x['p'].lower() for x in cur}
added = [{"p": p, "a": a} for p, a in NEW if p.lower() not in have]
json.dump(cur + added, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(added), 'prompts added; now', len(cur) + len(added))
