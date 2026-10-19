# Bank session 19 Oct 2026: new Wipeout boards -> bank/wipeout-131.json ('fly' in front; 'tail' in front).
# The bank has 'fly' and 'tail' added to the end, but neither in front. Every decoy was checked: no 'fly' word or phrase is made
# with Lamp/Sock/Cup/Ladder/Clock, and no 'tail' one with Sock/Cup/Ladder/Clock/Spoon (Lamp kept off: tail lamp).
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Words that make a new word or phrase when you put 'fly' in front", "Anagrams and wordplay", "easy", ["wordplay", "compound words"],
 ["Wheel", "Over", "Paper", "Past", "Weight", "Leaf", "By", "Half", "Fishing", "Sheet", "Tipping", "Swatter", "Away", "Blown", "Trap"],
 ["Lamp", "Sock", "Cup", "Ladder", "Clock"])
board("Words that make a new word or phrase when you put 'tail' in front", "Anagrams and wordplay", "easy", ["wordplay", "compound words"],
 ["Gate", "Back", "Spin", "Coat", "Wind", "Pipe", "Light", "Bone", "Plane", "End", "Fin", "Feather", "Gunner", "Board", "Lift"],
 ["Sock", "Cup", "Ladder", "Clock", "Spoon"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-131.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
