# Bank session 19 Oct 2026: new Wipeout boards -> bank/wipeout-127.json ('red' in front; 'cold' in front).
# Same shape as the 'dead' and 'free' in front boards; neither prefix was used before. Every decoy was checked: no 'red' word or
# phrase is made with Lamp/Sock/Cup/Ladder/Clock, and no 'cold' one with Lamp/Sock/Cup/Ladder/Coin.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Words that make a new word or phrase when you put 'red' in front", "Anagrams and wordplay", "easy", ["wordplay", "compound words"],
 ["Head", "Wood", "Neck", "Coat", "Card", "Carpet", "Light", "Wine", "Deer", "Kite", "Squirrel", "Nose", "Cross", "Tape", "Brick"],
 ["Lamp", "Sock", "Cup", "Ladder", "Clock"])
board("Words that make a new word or phrase when you put 'cold' in front", "Anagrams and wordplay", "easy", ["wordplay", "compound words"],
 ["Shoulder", "Feet", "Snap", "War", "Front", "Call", "Case", "Sore", "Turkey", "Comfort", "Storage", "Sweat", "Water", "Cream", "Blooded"],
 ["Lamp", "Sock", "Cup", "Ladder", "Coin"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-127.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
