# Bank session 19 Oct 2026: new Wipeout boards -> bank/wipeout-111.json (words that take FL in front; boys' names hidden in words).
# Same shapes as wipeout-92 to 94. Every decoy was checked letter by letter: no word made by putting FL in front of Milk/Fish/
# Cup/Coin/Tree, and no boy's name (asserted against a list) hidden in Pillow/Garden/Button/Ladder/Basket.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

# flash, flat, flaw, flit, float, flour, flown, flail, flair, flask, flinch, flutter, flounce, flout, flay
board("Words that make a new word when you put FL in front", "Anagrams and wordplay", "medium", ["wordplay", "letters"],
 ["Ash", "At", "Aw", "It", "Oat", "Our", "Own", "Ail", "Air", "Ask", "Inch", "Utter", "Ounce", "Out", "Ay"],
 ["Milk", "Fish", "Cup", "Coin", "Tree"])
# TOMato, BENch, DANger, gIANt, DONkey, parDON, LEOpard, chameLEOn, ROBot, wardROBe, amERICa, genERIC, bALANce, broKEN, destROY
NAMES = ["tom", "ben", "dan", "ian", "ray", "don", "max", "leo", "rob", "sam", "ted", "eric", "alan", "des", "ken", "pat", "les", "bill", "roy",
         "guy", "jim", "joe", "tim", "bob", "rod", "ron", "ali", "len", "lee", "neil", "phil", "carl", "paul", "mark", "john", "jack", "sean",
         "dave", "matt", "adam", "luke", "owen", "alex", "ivan", "otto", "rory", "ross", "jake", "noel", "nick", "stan", "dean", "seth", "glen"]
RIGHT = ["Tomato", "Bench", "Danger", "Giant", "Donkey", "Pardon", "Leopard", "Chameleon", "Robot", "Wardrobe", "America", "Generic", "Balance", "Broken", "Destroy"]
WRONG = ["Pillow", "Garden", "Button", "Ladder", "Basket"]
assert all(any(v in w.lower() for v in NAMES) for w in RIGHT)
assert not [w for w in WRONG if any(v in w.lower() for v in NAMES)], [w for w in WRONG if any(v in w.lower() for v in NAMES)]
board("Words with a boy's name hidden inside them", "Anagrams and wordplay", "medium", ["wordplay", "hidden words", "names"], RIGHT, WRONG)

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-111.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
