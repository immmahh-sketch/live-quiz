# Bank session 19 Oct 2026: new Wipeout boards -> bank/wipeout-140.json ('glass' in front; 'film' in front).
# Neither prefix was used before. Every decoy was checked: no 'glass' word or phrase is made with Sock/Ladder/Coin/Shoe/Tent, and
# no 'film' one with Sock/Ladder/Cup/Clock/Coin.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Words that make a new word or phrase when you put 'glass' in front", "Anagrams and wordplay", "easy", ["wordplay", "compound words"],
 ["House", "Ware", "Blower", "Eye", "Ceiling", "Jaw", "Slipper", "Paper", "Cutter", "Wool", "Work", "Wing", "Snake", "Frog", "Door"],
 ["Sock", "Ladder", "Coin", "Shoe", "Tent"])
board("Words that make a new word or phrase when you put 'film' in front", "Anagrams and wordplay", "easy", ["wordplay", "compound words"],
 ["Star", "Maker", "Set", "Noir", "Festival", "Crew", "Buff", "Script", "Studio", "Strip", "Score", "Critic", "Reel", "Rights", "Fan"],
 ["Sock", "Ladder", "Cup", "Clock", "Coin"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-140.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
