# Bank session 18 Oct 2026: 3 more Only One prompts (Blankety Blank hosts, UK Price Is Right hosts, Crystal Maze or Robot Wars
# hosts and co-hosts) appended to bank/unique-prompts.json. Each is a closed list with every correct answer (other accepted
# forms after a slash), so a fair answer is never knocked out. Probed against the 704 prompts already in the pool.
# Games are built from the pool with: GAMES=8 node tools/unique-stock.mjs
import json, os
NEW = [
 ("Name a host of Blankety Blank, up to 2025", ["Terry Wogan/Wogan", "Les Dawson/Dawson", "Lily Savage/Paul O'Grady/O'Grady/Savage",
   "David Walliams/Walliams", "Bradley Walsh/Walsh"]),
 ("Name a host of the UK version of The Price Is Right, up to 2025", ["Leslie Crowther/Crowther", "Bob Warman/Warman", "Bruce Forsyth/Forsyth/Brucie",
   "Joe Pasquale/Pasquale", "Alan Carr/Carr"]),
 ("Name a host or co-host of The Crystal Maze or of Robot Wars, up to 2025", ["Richard O'Brien/O'Brien", "Ed Tudor-Pole/Ed Tudor Pole/Tudor-Pole",
   "Stephen Merchant/Merchant", "Richard Ayoade/Ayoade", "Jeremy Clarkson/Clarkson", "Craig Charles/Charles", "Philippa Forrester/Forrester",
   "Dara Ó Briain/Dara O Briain/Dara O'Briain/O Briain", "Angela Scanlon/Scanlon"]),
]
here = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(here, '..', 'unique-prompts.json')
cur = json.load(open(path, encoding='utf-8'))
have = {x['p'].lower() for x in cur}
added = [{"p": p, "a": a} for p, a in NEW if p.lower() not in have]
json.dump(cur + added, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(added), 'prompts added; now', len(cur) + len(added))
