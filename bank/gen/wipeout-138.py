# Bank session 19 Oct 2026: new Wipeout boards -> bank/wipeout-138.json ('wall' in front; 'mother' in front).
# Neither prefix was used before. Every decoy was checked: no 'wall' word or phrase is made with Sock/Cup/Ladder/Spoon/Coin (Lamp and
# Clock kept off: wall lamp, wall clock), and no 'mother' one with Lamp/Sock/Cup/Ladder/Clock.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Letters or words that make a new word, phrase or name when you put 'wall' in front", "Anagrams and wordplay", "medium", ["wordplay", "compound words"],
 ["Paper", "Flower", "Et", "Chart", "Op", "Ow", "Aby", "Bars", "Socket", "Mounted", "Light", "Hanging", "Painting", "Eye", "Street"],
 ["Sock", "Cup", "Ladder", "Spoon", "Coin"])
board("Words that make a new word, phrase or name when you put 'mother' in front", "Anagrams and wordplay", "easy", ["wordplay", "compound words"],
 ["Board", "Land", "Tongue", "Hood", "Ship", "Nature", "Hen", "Superior", "Earth", "Goose", "Teresa", "Country", "Figure", "Church", "Love"],
 ["Lamp", "Sock", "Cup", "Ladder", "Clock"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-138.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
