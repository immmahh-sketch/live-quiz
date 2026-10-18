# Bank session 18 Oct 2026: 4 more Only One prompts (University Challenge or Blockbusters hosts, Generation Game hosts, great
# apes, Deal or No Deal / Weakest Link / Millionaire hosts) appended to bank/unique-prompts.json. Each is a closed list with
# every correct answer (other accepted forms after a slash), so a fair answer is never knocked out. Probed against the 700
# prompts already in the pool (the Chasers, Bake Off presenters and Mastermind presenters were already there).
# Games are built from the pool with: GAMES=8 node tools/unique-stock.mjs
import json, os
NEW = [
 ("Name a host of University Challenge or of Blockbusters, up to 2025", ["Bamber Gascoigne/Gascoigne", "Jeremy Paxman/Paxman", "Amol Rajan/Rajan",
   "Bob Holness/Holness", "Michael Aspel/Aspel", "Liza Tarbuck/Tarbuck", "Simon Mayo/Mayo", "Dara Ó Briain/Dara O Briain/Dara O'Briain/O Briain"]),
 ("Name a host of The Generation Game, up to 2025", ["Bruce Forsyth/Forsyth/Brucie", "Larry Grayson/Grayson", "Jim Davidson/Davidson",
   "Mel Giedroyc/Giedroyc/Mel", "Sue Perkins/Perkins/Sue"]),
 ("Name a species of great ape, apart from humans", ["Gorilla", "Chimpanzee/Chimp", "Bonobo/Pygmy chimpanzee", "Orangutan/Orang-utan/Orangutang"]),
 ("Name a UK host of Deal or No Deal, The Weakest Link or Who Wants to Be a Millionaire?, up to 2025", ["Noel Edmonds/Edmonds", "Stephen Mulhern/Mulhern",
   "Anne Robinson/Robinson", "Romesh Ranganathan/Ranganathan/Romesh", "Chris Tarrant/Tarrant", "Jeremy Clarkson/Clarkson"]),
]
here = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(here, '..', 'unique-prompts.json')
cur = json.load(open(path, encoding='utf-8'))
have = {x['p'].lower() for x in cur}
added = [{"p": p, "a": a} for p, a in NEW if p.lower() not in have]
json.dump(cur + added, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(added), 'prompts added; now', len(cur) + len(added))
