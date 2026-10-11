# Bank session 11 Oct 2026: new Wipeout boards -> bank/wipeout-51.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

W = "Words and language"
board("Words that make a new word or phrase when you put 'rain' in front", W, "easy", ["wordplay", "compound words"],
 ["Bow", "Coat", "Drop", "Fall", "Forest", "Water", "Storm", "Cloud", "Maker", "Proof", "Check", "Gauge", "Dance", "Shadow", "Wear"],
 ["Sun", "Wet", "Cup", "Sock", "Tree"])
board("Words that make a new word or phrase when you put 'door' in front", W, "easy", ["wordplay", "compound words"],
 ["Bell", "Step", "Mat", "Way", "Knob", "Stop", "Man", "Frame", "Keeper", "Nail", "Post", "Handle", "Knocker", "Jamb", "Hinge"],
 ["Roof", "Floor", "Wall", "Chair", "Lamp"])
board("Words that make a new word or phrase when you put 'horse' in front", W, "medium", ["wordplay", "compound words"],
 ["Shoe", "Power", "Play", "Radish", "Fly", "Hair", "Box", "Man", "Back", "Race", "Whip", "Chestnut", "Sense", "Rider", "Tail"],
 ["Cow", "Tree", "Book", "Cup", "Sock"])
board("Words that make a new word when you put 'news' in front", W, "medium", ["wordplay", "compound words"],
 ["Paper", "Agent", "Reader", "Flash", "Letter", "Room", "Caster", "Feed", "Group", "Hound", "Worthy", "Print", "Stand", "Reel", "Desk"],
 ["Book", "Card", "Page", "Pen", "Ink"])
board("Words that make a new word or phrase when you put 'tea' in front", W, "easy", ["wordplay", "compound words"],
 ["Pot", "Cup", "Spoon", "Bag", "Towel", "Time", "Shop", "Room", "Cake", "Leaf", "Party", "Set", "Light", "Break", "Trolley"],
 ["Glass", "Plate", "Fork", "Chair", "Wine"])
board("Words that make a new word when you put 'play' in front", W, "medium", ["wordplay", "compound words"],
 ["Ground", "Mate", "Time", "Group", "House", "Pen", "Thing", "Wright", "List", "Off", "Station", "Boy", "Room", "School", "Ful"],
 ["Game", "Ball", "Run", "Song", "Seat"])
board("Words that make a new word or phrase when you put 'key' in front", W, "medium", ["wordplay", "compound words"],
 ["Board", "Hole", "Note", "Ring", "Stone", "Pad", "Word", "Stroke", "Worker", "Card", "Chain", "Fob", "Holder", "Signature", "Lime"],
 ["Lock", "Door", "Cup", "Shoe", "Tree"])
board("Letters that make a new word when you put 'cat' in front", W, "hard", ["wordplay", "hidden words"],
 ["Walk", "Fish", "Nap", "Call", "Gut", "Flap", "Kin", "Apult", "Erpillar", "Alogue", "Astrophe", "Egory", "Hedral", "Tle", "Ch"],
 ["Dog", "Mouse", "Paw", "Bowl", "Tree"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-51.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
