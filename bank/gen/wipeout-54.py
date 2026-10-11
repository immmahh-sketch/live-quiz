# Bank session 11 Oct 2026: new Wipeout boards -> bank/wipeout-54.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

W = "Words and language"
board("Words that make a new word or phrase when you add 'shop' to the end", W, "easy", ["wordplay", "compound words"],
 ["Work", "Book", "Pawn", "Barber", "Sweet", "Chip", "Coffee", "Gift", "Charity", "Toy", "Corner", "Tea", "Wood", "Closed", "Photo"],
 ["Till", "Bag", "Price", "Basket", "Queue"])
board("Letters that make a new word when you put 'ear' in front", W, "medium", ["wordplay", "compound words"],
 ["Ring", "Plug", "Lobe", "Wig", "Drum", "Mark", "Phones", "Muffs", "Shot", "Ache", "Wax", "Piece", "Bud", "Ly", "N"],
 ["Nose", "Eye", "Mouth", "Chin", "Lip"])
board("Words that make a new word or phrase when you add 'bell' to the end", W, "medium", ["wordplay", "compound words"],
 ["Blue", "Door", "Cow", "Dumb", "Bar", "Hand", "Church", "Sleigh", "Kettle", "Jingle", "Camp", "Tinker", "Diving", "School", "Wedding"],
 ["Gong", "Whistle", "Horn", "Buzzer", "Chime"])
board("Words that make a new word or phrase when you add 'ring' to the end", W, "easy", ["wordplay", "compound words"],
 ["Ear", "Key", "Wedding", "Boxing", "Nose", "Bull", "Fairy", "Engagement", "Signet", "Smoke", "Onion", "Teething", "Toe", "Belly", "Napkin"],
 ["Watch", "Chain", "Bracelet", "Necklace", "Brooch"])
board("Letters that make a new word or phrase when you add 'nut' to the end", W, "medium", ["wordplay", "compound words"],
 ["Pea", "Wal", "Hazel", "Chest", "Coco", "Dough", "Brazil", "Pine", "Cashew", "Beech", "Ginger", "Wing", "Butter", "Monkey", "Do"],
 ["Bolt", "Screw", "Shell", "Seed", "Kernel"])
board("Words that make a new word or phrase when you add 'point' to the end", W, "medium", ["wordplay", "compound words"],
 ["Pin", "Gun", "Knife", "View", "Stand", "Check", "Ball", "Match", "Set", "Break", "Flash", "Turning", "Vantage", "Focal", "Boiling"],
 ["Edge", "Tip", "Line", "Dot", "Spot"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-54.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
