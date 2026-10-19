# Bank session 19 Oct 2026: new Wipeout boards -> bank/wipeout-125.json ('silver' in front; 'sky' in front).
# Same shape as the 'green' and 'hot' in front boards; neither prefix was used before. Every decoy was checked: no 'silver' word or
# phrase is made with Desk/Lamp/Clock/Sock/Ladder (Coin and Shoe kept off: silver coin, silver shoes), and no 'sky' one with
# Desk/Shoe/Coin/Sock/Cup.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Words that make a new word or phrase when you put 'silver' in front", "Anagrams and wordplay", "easy", ["wordplay", "compound words"],
 ["Fish", "Ware", "Smith", "Back", "Screen", "Spoon", "Lining", "Birch", "Jubilee", "Medal", "Surfer", "Stone", "Side", "Fox", "Wedding"],
 ["Desk", "Lamp", "Clock", "Sock", "Ladder"])
board("Words that make a new word or phrase when you put 'sky' in front", "Anagrams and wordplay", "easy", ["wordplay", "compound words"],
 ["Lark", "Line", "Light", "Scraper", "Diving", "Rocket", "Blue", "High", "Fall", "Jack", "Ward", "Writing", "Walker", "Lab", "Sports"],
 ["Desk", "Shoe", "Coin", "Sock", "Cup"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-125.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
