# Bank session 19 Oct 2026: new Wipeout boards -> bank/wipeout-124.json ('green' in front; 'hot' in front).
# Same shape as the 'sweet' and 'road' in front boards already in the bank; neither prefix was used before. Every decoy was
# checked: no 'green' word or phrase is made with Desk/Lamp/Shoe/Coin/Clock, and no 'hot' one with Lamp/Coin/Clock/Sock/Ladder
# (Desk and Shoe were kept off the 'hot' board: hot-desk, hot shoe).
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Words that make a new word or phrase when you put 'green' in front", "Anagrams and wordplay", "easy", ["wordplay", "compound words"],
 ["House", "Grocer", "Belt", "Fly", "Finch", "Light", "Room", "Card", "Keeper", "Field", "Horn", "Gage", "Land", "Tea", "Fingers"],
 ["Desk", "Lamp", "Shoe", "Coin", "Clock"])
board("Words that make a new word or phrase when you put 'hot' in front", "Anagrams and wordplay", "easy", ["wordplay", "compound words"],
 ["Dog", "Pot", "Line", "Spot", "Shot", "Water", "Bed", "Head", "Cake", "Air", "Rod", "Tub", "Plate", "Seat", "Potato"],
 ["Lamp", "Coin", "Clock", "Sock", "Ladder"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-124.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
