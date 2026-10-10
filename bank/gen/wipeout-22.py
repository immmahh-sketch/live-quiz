# Bank session 10 Oct 2026: new Wipeout boards -> bank/wipeout-22.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Words that make a new word when you add 'room' to the end", "Words and language", "easy", ["wordplay", "compound words"],
 ["Bed", "Bath", "Class", "Show", "Mush", "Ball", "Board", "Store", "Head", "Elbow", "Leg", "Wiggle", "Court", "Cloak", "Dark"],
 ["Door", "Wall", "Window", "Floor", "Roof"])
board("Words that make a new word when you add 'lock' to the end", "Words and language", "medium", ["wordplay", "compound words"],
 ["Pad", "Dead", "Grid", "Head", "Hem", "Wed", "War", "Air", "Arm", "Fore", "Inter", "Gun", "Flint", "Over", "Wrist"],
 ["Door", "Key", "Safe", "Bolt", "Chain"])
board("Words that make a new word when you put 'out' in front", "Words and language", "easy", ["wordplay", "compound words"],
 ["Side", "Line", "Look", "Come", "Break", "Burst", "Fit", "Law", "Let", "Put", "Rage", "Run", "Grow", "Post", "Cast"],
 ["Into", "Inside", "Under", "Above", "Behind"])
board("Words that make a new word when you put 'over' in front", "Words and language", "easy", ["wordplay", "compound words"],
 ["Coat", "Board", "Take", "Time", "Head", "Lap", "Load", "Look", "Night", "Rule", "Turn", "Weight", "Flow", "Come", "Haul"],
 ["Glove", "Sock", "Scarf", "Belt", "Tie"])
board("Words that make a new word when you put 'under' in front", "Words and language", "easy", ["wordplay", "compound words"],
 ["Ground", "Wear", "Line", "Dog", "Stand", "Take", "Cover", "Cut", "Pass", "Water", "World", "Arm", "Graduate", "Study", "Current"],
 ["Roof", "Ceiling", "Table", "Chair", "Window"])
board("Men who won the US Open tennis singles, 1990 to 2025", "Sport", "hard", ["tennis", "US Open"],
 ["Pete Sampras", "Stefan Edberg", "Andre Agassi", "Patrick Rafter", "Marat Safin", "Lleyton Hewitt", "Andy Roddick", "Roger Federer", "Juan Martín del Potro", "Rafael Nadal", "Novak Djokovic", "Andy Murray", "Marin Čilić", "Stan Wawrinka", "Carlos Alcaraz"],
 ["Tim Henman", "Greg Rusedski", "David Ferrer", "Casper Ruud", "Nick Kyrgios"])
board("Winners of golf's Open Championship, 1990 to 2025", "Sport", "hard", ["golf", "The Open"],
 ["Nick Faldo", "Ian Baker-Finch", "John Daly", "Greg Norman", "Nick Price", "Tiger Woods", "Ernie Els", "Pádraig Harrington", "Darren Clarke", "Rory McIlroy", "Phil Mickelson", "Jordan Spieth", "Shane Lowry", "Collin Morikawa", "Scottie Scheffler"],
 ["Colin Montgomerie", "Lee Westwood", "Sergio García", "Luke Donald", "Rickie Fowler"])
board("Tour de France winners, 1990 to 2025", "Cycling", "hard", ["Tour de France", "cycling"],
 ["Greg LeMond", "Miguel Indurain", "Bjarne Riis", "Jan Ullrich", "Marco Pantani", "Carlos Sastre", "Alberto Contador", "Cadel Evans", "Bradley Wiggins", "Chris Froome", "Vincenzo Nibali", "Geraint Thomas", "Egan Bernal", "Tadej Pogačar", "Jonas Vingegaard"],
 ["Mark Cavendish", "Peter Sagan", "Chris Boardman", "Mario Cipollini", "Wout van Aert"])
board("Shades of red", "Art and design", "medium", ["colours", "red"],
 ["Crimson", "Scarlet", "Vermilion", "Cherry", "Ruby", "Burgundy", "Maroon", "Cardinal", "Carmine", "Claret", "Wine", "Blood red", "Brick red", "Oxblood", "Cerise"],
 ["Teal", "Ochre", "Taupe", "Lilac", "Khaki"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-22.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'boards written')
