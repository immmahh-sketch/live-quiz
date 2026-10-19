# Bank session 19 Oct 2026: new Wipeout boards -> bank/wipeout-136.json ('land' in front; 'in' in front).
# The bank has 'land' added to the end but not in front, and no 'in' board. Every decoy was checked: no 'land' or 'in' word or phrase
# is made with Lamp/Sock/Cup/Ladder/Clock.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Words that make a new word or phrase when you put 'land' in front", "Anagrams and wordplay", "easy", ["wordplay", "compound words"],
 ["Lord", "Mark", "Slide", "Fill", "Lady", "Line", "Mine", "Scape", "Locked", "Owner", "Fall", "Mass", "Lubber", "Rover", "Grab"],
 ["Lamp", "Sock", "Cup", "Ladder", "Clock"])
board("Words that make a new word when you put 'in' in front", "Anagrams and wordplay", "medium", ["wordplay", "compound words"],
 ["Side", "Put", "Come", "Box", "Let", "Sight", "Mate", "Form", "Field", "Lay", "Land", "Sect", "Vest", "Tent", "Deed"],
 ["Lamp", "Sock", "Cup", "Ladder", "Clock"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-136.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
