# Bank session 11 Oct 2026: new Wipeout boards -> bank/wipeout-52.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

W = "Words and language"
board("Letters that make a new word when you put 'sand' in front", W, "medium", ["wordplay", "compound words"],
 ["Castle", "Paper", "Stone", "Bag", "Pit", "Storm", "Bank", "Dune", "Piper", "Box", "Fly", "Bar", "Blast", "Wich", "Al"],
 ["Sea", "Shell", "Wave", "Sun", "Rock"])
board("Letters that make a new word or phrase when you put 'pass' in front", W, "hard", ["wordplay", "compound words"],
 ["Port", "Word", "Book", "Over", "Age", "Enger", "Ion", "Ive", "Able", "Key", "Code", "Mark", "Out", "Ed", "Ing"],
 ["Card", "Gate", "Ticket", "Road", "Hand"])
board("Words that make a new word or phrase when you put 'hair' in front", W, "easy", ["wordplay", "compound words"],
 ["Brush", "Cut", "Dryer", "Spray", "Band", "Pin", "Line", "Net", "Grip", "Dresser", "Style", "Piece", "Clip", "Dye", "Raising"],
 ["Shoe", "Nail", "Face", "Bath", "Lip"])
board("Letters that make a new word when you put 'car' in front", W, "hard", ["wordplay", "hidden words"],
 ["Pet", "Rot", "Toon", "Go", "Pool", "Park", "Wash", "Boot", "Ton", "Rier", "Nation", "Avan", "Bon", "Ousel", "Ol"],
 ["Bike", "Wheel", "Road", "Bus", "Lorry"])
board("Words that make a new word or phrase when you put 'bath' in front", W, "easy", ["wordplay", "compound words"],
 ["Robe", "Room", "Tub", "Mat", "Water", "Time", "Towel", "Salts", "Bomb", "Chair", "Plug", "Sheet", "Ing", "Os", "House"],
 ["Shower", "Sink", "Kitchen", "Bed", "Shelf"])
board("Words that make a new word or phrase when you put 'dog' in front", W, "medium", ["wordplay", "compound words"],
 ["House", "Fish", "Fight", "Collar", "Leg", "Ma", "Sled", "Ear", "Rose", "Days", "Gone", "Tag", "Wood", "Watch", "Basket"],
 ["Cat", "Pen", "Cup", "Shoe", "Tree"])
board("Letters that make a new word or phrase when you put 'wind' in front", W, "medium", ["wordplay", "compound words"],
 ["Mill", "Screen", "Sock", "Fall", "Swept", "Breaker", "Surfing", "Chill", "Pipe", "Bag", "Cheater", "Farm", "Turbine", "Ow", "Jammer"],
 ["Rain", "Storm", "Cloud", "Sun", "Snow"])
board("Letters that make a new word or phrase when you put 'pin' in front", W, "hard", ["wordplay", "hidden words"],
 ["Ball", "Cushion", "Point", "Stripe", "Hole", "Head", "Wheel", "Afore", "Ch", "E", "K", "Apple", "Ion", "Up", "Number"],
 ["Needle", "Thread", "Button", "Cloth", "Sock"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-52.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
