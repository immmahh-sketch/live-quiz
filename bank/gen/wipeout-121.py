# Bank session 19 Oct 2026: new Wipeout boards -> bank/wipeout-121.json ('egg' in front; 'bull' in front).
# Same shape as the 'tea' and 'fish' in front boards already in the bank. Every decoy was checked: no 'egg' or 'bull' word
# or phrase is made with Desk/Lamp/Shoe/Tree/Coin.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Words that make a new word or phrase when you put 'egg' in front", "Anagrams and wordplay", "easy", ["wordplay", "compound words"],
 ["Shell", "Cup", "Head", "Plant", "Timer", "Box", "White", "Yolk", "Roll", "Custard", "Nog", "Whisk", "Sandwich", "Spoon", "Hunt"],
 ["Desk", "Lamp", "Shoe", "Tree", "Coin"])
board("Words that make a new word or phrase when you put 'bull' in front", "Anagrams and wordplay", "easy", ["wordplay", "compound words"],
 ["Dog", "Frog", "Fight", "Ring", "Dozer", "Finch", "Horn", "Pen", "Terrier", "Bar", "Market", "Whip", "Head", "Shark", "Elephant"],
 ["Desk", "Lamp", "Shoe", "Tree", "Coin"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-121.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
