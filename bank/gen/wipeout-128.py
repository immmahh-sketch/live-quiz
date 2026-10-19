# Bank session 19 Oct 2026: new Wipeout boards -> bank/wipeout-128.json ('blue' in front; 'gun' in front).
# Same shape as the 'red' and 'cold' in front boards; neither prefix was used before. Every decoy was checked: no 'blue' word or
# phrase is made with Sock/Cup/Ladder/Clock/Spoon (Lamp kept off: the blue lamp), and no 'gun' one with Lamp/Sock/Cup/Ladder/Clock.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Words that make a new word or phrase when you put 'blue' in front", "Anagrams and wordplay", "easy", ["wordplay", "compound words"],
 ["Bell", "Berry", "Bird", "Bottle", "Print", "Tit", "Whale", "Cheese", "Grass", "Moon", "Tooth", "Jeans", "Collar", "Peter", "Chip"],
 ["Sock", "Cup", "Ladder", "Clock", "Spoon"])
board("Words that make a new word or phrase when you put 'gun' in front", "Anagrams and wordplay", "easy", ["wordplay", "compound words"],
 ["Powder", "Fire", "Man", "Shot", "Boat", "Point", "Smith", "Metal", "Dog", "Slinger", "Ship", "Runner", "Barrel", "Play", "Fight"],
 ["Lamp", "Sock", "Cup", "Ladder", "Clock"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-128.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
