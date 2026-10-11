# Bank session 11 Oct 2026: new Wipeout boards -> bank/wipeout-53.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

W = "Words and language"
board("Words that make a new word or phrase when you add 'paper' to the end", W, "easy", ["wordplay", "compound words"],
 ["News", "Wall", "Sand", "Toilet", "Fly", "Wrapping", "Tissue", "Tracing", "Waste", "Note", "Sugar", "Rice", "Blotting", "Greaseproof", "Kitchen"],
 ["Book", "Pen", "Card", "Ink", "Glue"])
board("Letters that make a new word when you add 'port' to the end", W, "hard", ["wordplay", "hidden words"],
 ["Air", "Sea", "Pass", "Sup", "Re", "Im", "Ex", "Trans", "Space", "Heli", "Car", "Rap", "De", "S", "Pur"],
 ["Land", "Ship", "Bus", "Train", "Dock"])
board("Words that make a new word when you add 'wear' to the end", W, "medium", ["wordplay", "compound words"],
 ["Under", "Foot", "Sports", "Swim", "Night", "Rain", "Leisure", "Eye", "Neck", "Knit", "Beach", "Head", "Outer", "Active", "Work"],
 ["Hat", "Shoe", "Coat", "Sock", "Tie"])
board("Words that make a new word or phrase when you add 'cup' to the end", W, "medium", ["wordplay", "compound words"],
 ["Tea", "Egg", "Butter", "Hic", "World", "Suction", "Paper", "Coffee", "Sippy", "Loving", "Stirrup", "Davis", "FA", "King", "Ryder"],
 ["Mug", "Plate", "Saucer", "Spoon", "Glass"])
board("Words that make a new word when you put 'down' in front", W, "medium", ["wordplay", "compound words"],
 ["Pour", "Fall", "Load", "Stairs", "Hill", "Town", "Turn", "Grade", "Side", "Size", "Wind", "Right", "Beat", "Trodden", "Cast"],
 ["Up", "Ladder", "Lift", "Floor", "Low"])
board("Words that make a new word or phrase when you put 'time' in front", W, "medium", ["wordplay", "compound words"],
 ["Table", "Line", "Keeper", "Bomb", "Share", "Scale", "Less", "Piece", "Out", "Zone", "Lord", "Frame", "Travel", "Sheet", "Lapse"],
 ["Watch", "Hour", "Day", "Date", "Week"])
board("Words that make a new word or phrase when you put 'fish' in front", W, "easy", ["wordplay", "compound words"],
 ["Monger", "Cake", "Bowl", "Net", "Finger", "Wife", "Hook", "Tank", "Pond", "Bone", "Eye", "Shop", "Paste", "Knife", "Farm"],
 ["Chip", "Sea", "Water", "Rod", "Boat"])
board("Words that make a new word or phrase when you put 'bird' in front", W, "easy", ["wordplay", "compound words"],
 ["Cage", "Song", "Bath", "Seed", "Table", "Brain", "Box", "Watcher", "Life", "Call", "House", "Feeder", "Strike", "Dog", "Flu"],
 ["Tree", "Sky", "Cat", "Worm", "Feather"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-53.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
