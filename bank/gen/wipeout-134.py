# Bank session 19 Oct 2026: new Wipeout boards -> bank/wipeout-134.json ('rose' in front; 'ice' in front).
# Neither prefix was used before. Every decoy was checked: no 'rose' or 'ice' word or phrase is made with Lamp/Sock/Cup/Ladder/Clock.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Words that make a new word or phrase when you put 'rose' in front", "Anagrams and wordplay", "easy", ["wordplay", "compound words"],
 ["Bud", "Wood", "Mary", "Hip", "Garden", "Bush", "Water", "Petal", "Gold", "Window", "Tinted", "Bowl", "Bed", "Quartz", "Bay"],
 ["Lamp", "Sock", "Cup", "Ladder", "Clock"])
board("Words that make a new word or phrase when you put 'ice' in front", "Anagrams and wordplay", "easy", ["wordplay", "compound words"],
 ["Berg", "Cap", "Box", "Cream", "Cube", "Rink", "Skate", "Pick", "Age", "Hockey", "Lolly", "Breaker", "Pack", "Bucket", "Sheet"],
 ["Lamp", "Sock", "Cup", "Ladder", "Clock"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-134.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
