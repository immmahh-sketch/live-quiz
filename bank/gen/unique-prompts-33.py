# Bank session 18 Oct 2026: 4 more Only One prompts (Gerry Anderson's 1960s puppet series, Taskmaster champions of series
# 1 to 10, the first six Mr Men books, David Croft's sitcoms) appended to bank/unique-prompts.json. Each is a closed list with
# every correct answer (other accepted forms after a slash), so a fair answer is never knocked out. Probed against the 691
# prompts already in the pool (Red Dwarf, Men Behaving Badly, Keeping Up Appearances, ringed planets were already there).
# Games are built from the pool with: GAMES=8 node tools/unique-stock.mjs
import json, os
NEW = [
 ("Name one of Gerry Anderson's 1960s puppet series", ["Torchy the Battery Boy/Torchy", "Four Feather Falls", "Supercar", "Fireball XL5", "Stingray",
   "Thunderbirds", "Captain Scarlet and the Mysterons/Captain Scarlet", "Joe 90", "The Secret Service"]),
 ("Name a Taskmaster series champion from series 1 to 10", ["Josh Widdicombe/Widdicombe", "Katherine Ryan/Ryan", "Rob Beckett/Beckett", "Noel Fielding/Fielding",
   "Bob Mortimer/Mortimer", "Liza Tarbuck/Tarbuck", "Kerry Godliman/Godliman", "Lou Sanders/Sanders", "Ed Gamble/Gamble", "Richard Herring/Herring"]),
 ("Name one of the first six Mr Men books, from 1971", ["Mr Tickle/Mr. Tickle", "Mr Greedy/Mr. Greedy", "Mr Happy/Mr. Happy", "Mr Nosey/Mr. Nosey", "Mr Sneeze/Mr. Sneeze", "Mr Bump/Mr. Bump"]),
 ("Name a sitcom written by David Croft", ["Dad's Army", "Are You Being Served?/Are You Being Served", "Grace & Favour/Grace and Favour", "It Ain't Half Hot Mum",
   "Hi-de-Hi!/Hi-de-Hi/Hi De Hi", "'Allo 'Allo!/Allo Allo", "You Rang, M'Lord?/You Rang My Lord", "Oh, Doctor Beeching!/Oh Doctor Beeching"]),
]
here = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(here, '..', 'unique-prompts.json')
cur = json.load(open(path, encoding='utf-8'))
have = {x['p'].lower() for x in cur}
added = [{"p": p, "a": a} for p, a in NEW if p.lower() not in have]
json.dump(cur + added, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(added), 'prompts added; now', len(cur) + len(added))
