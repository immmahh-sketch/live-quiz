# Bank session 18 Oct 2026: more Nearest Wins questions -> bank/nearest-43.json (games, animals, TV and landmarks).
# (text, answer, unit, spread, difficulty, category, wow). Tested with lqsql/neardup-n.py (the server's near-duplicate rule)
# and lqsql/audit/tf-dupcheck.py before importing; anything already in the bank is dropped (harp strings, ostrich eggs,
# hedgehog spines, Scrabble, dominoes, Rubik's Cube the Elizabeth Tower's height and Monopoly's 32 houses were all there).
import json, os
Q = [
 ("In what year was Mastermind, with Magnus Magnusson in the black chair, first shown?", 1972, "", 3, "medium", "Television", False),
 ("What's the fewest starting numbers a standard Sudoku can have and still have only one solution?", 17, "clues", 3, "hard", "Maths and numbers", True),
 ("In a single bound, roughly how many metres can a red kangaroo cover?", 8, "metres", 2, "medium", "Nature", False),
 ("A newborn kangaroo crawls into its mother's pouch. Roughly how many grams does it weigh?", 1, "grams", 1, "hard", "Nature", True),
 ("In what year was the first Paddington book, 'A Bear Called Paddington', published?", 1958, "", 4, "medium", "Books", False),
 ("In what year was A. A. Milne's first 'Winnie-the-Pooh' book published?", 1926, "", 4, "medium", "Books", False),
 ("A kiwi lays a huge egg for its size. Roughly what percentage of the mother's body weight is it?", 20, "%", 4, "hard", "Nature", True),
 ("In what year did the Girl Guides begin in Britain?", 1910, "", 3, "hard", "History", False),
 ("How many steps climb to the top of the Elizabeth Tower, home of Big Ben?", 334, "steps", 30, "hard", "London", False),
 ("How many episodes of the original 1960s 'Thunderbirds' were made?", 32, "episodes", 6, "hard", "Television", False),
 ("How many people are asked each question in the Pointless survey?", 100, "people", 20, "medium", "Television", False),
 ("In chess, how many different first moves can White make?", 20, "moves", 4, "medium", "Games and puzzles", True),
]
here = os.path.dirname(os.path.abspath(__file__))
out = [{"type": "nearest", "text": t, "answer": a, "unit": u, "spread": s, "difficulty": d, "category": c, "tags": ["nearest wins"] + (["wow"] if w else [])} for t, a, u, s, d, c, w in Q]
json.dump(out, open(os.path.join(here, '..', 'nearest-43.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'nearest written')
