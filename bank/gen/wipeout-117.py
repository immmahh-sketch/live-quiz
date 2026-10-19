# Bank session 19 Oct 2026: new Wipeout boards -> bank/wipeout-117.json (words that take SW in front; words that take an E on the end).
# Same shapes as wipeout-92 to 94. Every decoy was checked letter by letter: no word made by putting SW in front of Milk/Fish/
# Cup/Coin/Tree, and no word made by adding E to Fish/Cup/Book/Milk/Desk (Dog was avoided: a doge is a word).
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

# swear, sweat, swell, swill, switch, swore, swallow, swamp, swan, swarm, sway, sweater, swab, swash, swears
board("Words that make a new word when you put SW in front", "Anagrams and wordplay", "medium", ["wordplay", "letters"],
 ["Ear", "Eat", "Ell", "Ill", "Itch", "Ore", "Allow", "Amp", "An", "Arm", "Ay", "Eater", "Ab", "Ash", "Ears"],
 ["Milk", "Fish", "Cup", "Coin", "Tree"])
# hate, note, cape, pine, kite, hope, bite, cane, care, cute, fate, huge, mane, made, robe
RIGHT = ["Hat", "Not", "Cap", "Pin", "Kit", "Hop", "Bit", "Can", "Car", "Cut", "Fat", "Hug", "Man", "Mad", "Rob"]
WRONG = ["Fish", "Cup", "Book", "Milk", "Desk"]
board("Words that make a new word when you add an E to the end", "Anagrams and wordplay", "easy", ["wordplay", "letters"], RIGHT, WRONG)

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-117.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
