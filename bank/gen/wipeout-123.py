# Bank session 19 Oct 2026: new Wipeout boards -> bank/wipeout-123.json ('sweet' in front; 'road' in front).
# Same shape as the 'tea' and 'fish' in front boards already in the bank. Every decoy was checked: no 'sweet' word or
# phrase is made with Desk/Lamp/Shoe/Coin/Tree, and no 'road' one with Desk/Lamp/Shoe/Coin/Cup.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Words that make a new word or phrase when you put 'sweet' in front", "Anagrams and wordplay", "easy", ["wordplay", "compound words"],
 ["Corn", "Heart", "Shop", "Pea", "Bread", "Tooth", "Potato", "Chilli", "Talk", "Dreams", "Pepper", "William", "Spot", "Sixteen", "Meat"],
 ["Desk", "Lamp", "Shoe", "Coin", "Tree"])
board("Words that make a new word or phrase when you put 'road' in front", "Anagrams and wordplay", "easy", ["wordplay", "compound words"],
 ["Works", "Side", "Block", "House", "Kill", "Map", "Rage", "Sign", "Runner", "Show", "Trip", "Tax", "Hog", "Safety", "Test"],
 ["Desk", "Lamp", "Shoe", "Coin", "Cup"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-123.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
