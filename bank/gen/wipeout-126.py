# Bank session 19 Oct 2026: new Wipeout boards -> bank/wipeout-126.json ('dead' in front; 'free' in front).
# Same shape as the 'silver' and 'sky' in front boards; neither prefix was used before. Every decoy was checked: no 'dead' word or
# phrase is made with Lamp/Coin/Clock/Sock/Cup, and no 'free' one with Lamp/Clock/Sock/Cup/Ladder.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Words that make a new word or phrase when you put 'dead' in front", "Anagrams and wordplay", "easy", ["wordplay", "compound words"],
 ["Line", "Lock", "Pan", "End", "Heat", "Wood", "Beat", "Weight", "Ringer", "Pool", "Sea", "Eye", "Bolt", "Duck", "Loss"],
 ["Lamp", "Coin", "Clock", "Sock", "Cup"])
board("Words that make a new word or phrase when you put 'free' in front", "Anagrams and wordplay", "easy", ["wordplay", "compound words"],
 ["Hold", "Lance", "Mason", "Way", "Kick", "Style", "Range", "Fall", "Wheeling", "Hand", "Loader", "View", "Trade", "Lunch", "Spirit"],
 ["Lamp", "Clock", "Sock", "Cup", "Ladder"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-126.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
