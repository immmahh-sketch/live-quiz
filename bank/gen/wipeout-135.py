# Bank session 19 Oct 2026: new Wipeout boards -> bank/wipeout-135.json ('shoe' in front; 'pig' in front).
# Neither prefix was used before. Every decoy was checked: no 'shoe' word or phrase is made with Lamp/Cup/Ladder/Clock/Spoon (Sock
# kept off as too close), and no 'pig' one with Lamp/Sock/Cup/Ladder/Clock.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Words that make a new word or phrase when you put 'shoe' in front", "Anagrams and wordplay", "easy", ["wordplay", "compound words"],
 ["Horn", "Lace", "Box", "Shine", "String", "Maker", "Tree", "Polish", "Shop", "Size", "Rack", "Brush", "Leather", "Repair", "Print"],
 ["Lamp", "Cup", "Ladder", "Clock", "Spoon"])
board("Words that make a new word or phrase when you put 'pig' in front", "Anagrams and wordplay", "medium", ["wordplay", "compound words"],
 ["Tail", "Sty", "Skin", "Let", "Pen", "Iron", "Swill", "Farm", "Ment", "Eon", "Headed", "Out", "Sticker", "Roast", "Latin"],
 ["Lamp", "Sock", "Cup", "Ladder", "Clock"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-135.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
