# Bank session 19 Oct 2026: new Wipeout boards -> bank/wipeout-133.json ('stone' in front; 'day' in front).
# The bank has 'stone' and 'day' added to the end but not in front. Every decoy was checked: no 'stone' or 'day' word or phrase is
# made with Lamp/Sock/Cup/Ladder/Clock.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Words that make a new word or phrase when you put 'stone' in front", "Anagrams and wordplay", "easy", ["wordplay", "compound words"],
 ["Wall", "Mason", "Ware", "Work", "Fish", "Chat", "Age", "Cold", "Circle", "Washed", "Fruit", "Fly", "Throw", "Crop", "Cutter"],
 ["Lamp", "Sock", "Cup", "Ladder", "Clock"])
board("Words that make a new word or phrase when you put 'day' in front", "Anagrams and wordplay", "easy", ["wordplay", "compound words"],
 ["Break", "Dream", "Light", "Time", "Bed", "Trip", "Off", "Return", "Job", "Care", "Pass", "Out", "Shift", "Room", "Lily"],
 ["Lamp", "Sock", "Cup", "Ladder", "Clock"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-133.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
