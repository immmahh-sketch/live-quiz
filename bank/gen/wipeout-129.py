# Bank session 19 Oct 2026: new Wipeout boards -> bank/wipeout-129.json ('jack' in front; 'brain' in front).
# Same shape as the 'blue' and 'gun' in front boards; neither prefix was used before. Every decoy was checked: no 'jack' or 'brain'
# word or phrase is made with Lamp/Sock/Cup/Ladder/Clock.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Words that make a new word, phrase or name when you put 'jack' in front", "Anagrams and wordplay", "easy", ["wordplay", "compound words"],
 ["Pot", "Knife", "Daw", "Sparrow", "Fruit", "Rabbit", "Hammer", "Frost", "Russell", "Boot", "Sprat", "Straw", "Plug", "Black", "Dee"],
 ["Lamp", "Sock", "Cup", "Ladder", "Clock"])
board("Words that make a new word or phrase when you put 'brain' in front", "Anagrams and wordplay", "easy", ["wordplay", "compound words"],
 ["Wave", "Storm", "Wash", "Child", "Power", "Teaser", "Box", "Drain", "Dead", "Freeze", "Cell", "Surgeon", "Fog", "Food", "Scan"],
 ["Lamp", "Sock", "Cup", "Ladder", "Clock"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-129.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
