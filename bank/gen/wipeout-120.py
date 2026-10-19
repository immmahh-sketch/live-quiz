# Bank session 19 Oct 2026: new Wipeout boards -> bank/wipeout-120.json ('gold' in front; 'milk' in front).
# Same shape as the 'tea' and 'fish' in front boards already in the bank. Every decoy was checked: no 'gold' word or phrase
# with Milk/Desk/Lamp/Shoe/Tree (Cup was left out: the Gold Cup), and no 'milk' one with Desk/Lamp/Shoe/Tree/Coin.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Words that make a new word or phrase when you put 'gold' in front", "Anagrams and wordplay", "easy", ["wordplay", "compound words"],
 ["Fish", "Finch", "Mine", "Smith", "Crest", "Field", "Rush", "Medal", "Dust", "Leaf", "Standard", "Card", "Coast", "Bar", "Digger"],
 ["Milk", "Desk", "Lamp", "Shoe", "Tree"])
board("Words that make a new word or phrase when you put 'milk' in front", "Anagrams and wordplay", "easy", ["wordplay", "compound words"],
 ["Shake", "Man", "Maid", "Float", "Tooth", "Chocolate", "Bottle", "Churn", "Round", "Carton", "Weed", "Jug", "Powder", "Pudding", "Bar"],
 ["Desk", "Lamp", "Shoe", "Tree", "Coin"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-120.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
