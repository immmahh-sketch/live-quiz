# Bank session 19 Oct 2026: new Wipeout boards -> bank/wipeout-137.json ('pen' in front; 'bus' in front).
# Neither prefix was used before. Both mix whole-word compounds with sneaky hidden ones (pen+guin, bus+iness), so they're rated
# medium. Every decoy was checked: no 'pen' or 'bus' word or phrase is made with Lamp/Sock/Cup/Ladder/Clock.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Letters or words that make a new word or phrase when you put 'pen' in front", "Anagrams and wordplay", "medium", ["wordplay", "compound words"],
 ["Knife", "Friend", "House", "Pal", "Name", "Holder", "Pusher", "Ding", "Chant", "Cil", "Ny", "Sion", "Tagon", "Dulum", "Guin"],
 ["Lamp", "Sock", "Cup", "Ladder", "Clock"])
board("Letters or words that make a new word or phrase when you put 'bus' in front", "Anagrams and wordplay", "medium", ["wordplay", "compound words"],
 ["Stop", "Station", "Lane", "Pass", "Shelter", "Driver", "Fare", "Ker", "Tle", "Iness", "Boy", "Load", "Ride", "Route", "Tour"],
 ["Lamp", "Sock", "Cup", "Ladder", "Clock"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-137.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
