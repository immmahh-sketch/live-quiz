# Bank session 19 Oct 2026: new Wipeout boards -> bank/wipeout-142.json ('ground' in front; 'flash' in front).
# Neither prefix was used before. Every decoy was checked: no 'ground' or 'flash' word or phrase is made with Sock/Ladder/Cup/Spoon/Coin.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Words that make a new word, phrase or name when you put 'ground' in front", "Anagrams and wordplay", "easy", ["wordplay", "compound words"],
 ["Floor", "Work", "Hog", "Breaking", "Rules", "Nut", "Sheet", "Water", "Crew", "Swell", "Zero", "Control", "Staff", "Beef", "Frost"],
 ["Sock", "Ladder", "Cup", "Spoon", "Coin"])
board("Words that make a new word, phrase or name when you put 'flash' in front", "Anagrams and wordplay", "easy", ["wordplay", "compound words"],
 ["Light", "Back", "Card", "Flood", "Point", "Drive", "Bulb", "Mob", "Gun", "Dance", "Forward", "Fiction", "Sale", "Harry", "Gordon"],
 ["Sock", "Ladder", "Cup", "Spoon", "Coin"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-142.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
