# Bank session 19 Oct 2026: new Wipeout boards -> bank/wipeout-132.json ('side' in front; 'pop' in front).
# The bank has 'side' added to the end but not in front, and no 'pop' board. Every decoy was checked: no 'side' word or phrase is
# made with Sock/Cup/Ladder/Clock/Spoon (Lamp kept off: side lamp), and no 'pop' one with Lamp/Cup/Ladder/Clock/Spoon (Sock kept
# off: pop sock).
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Words that make a new word or phrase when you put 'side' in front", "Anagrams and wordplay", "easy", ["wordplay", "compound words"],
 ["Board", "Burns", "Car", "Kick", "Line", "Show", "Step", "Track", "Walk", "Ways", "Effect", "Salad", "Order", "Street", "Saddle"],
 ["Sock", "Cup", "Ladder", "Clock", "Spoon"])
board("Words that make a new word, phrase or name when you put 'pop' in front", "Anagrams and wordplay", "easy", ["wordplay", "compound words"],
 ["Corn", "Star", "Gun", "Art", "Up", "Music", "Quiz", "Idol", "Eye", "Tart", "Group", "Song", "Video", "Culture", "Chart"],
 ["Lamp", "Cup", "Ladder", "Clock", "Spoon"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-132.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
