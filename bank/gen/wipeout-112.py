# Bank session 19 Oct 2026: new Wipeout boards -> bank/wipeout-112.json (words that take SP in front; drinks hidden in words).
# Same shapes as wipeout-92 to 94. Every decoy was checked letter by letter: no word made by putting SP in front of Milk/Fish/
# Cup/Coin/Tree, and no drink (asserted against a list) hidden in Pillow/Garden/Button/Ladder/Basket.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

# spark, spear, spin, spit, spill, spout, space, spice, spoil, spray, spring, sprig, splash, sparrow, spinner
board("Words that make a new word when you put SP in front", "Anagrams and wordplay", "medium", ["wordplay", "letters"],
 ["Ark", "Ear", "In", "It", "Ill", "Out", "Ace", "Ice", "Oil", "Ray", "Ring", "Rig", "Lash", "Arrow", "Inner"],
 ["Milk", "Fish", "Cup", "Coin", "Tree"])
# sTEAm, TEAch, insTEAd, tALE, scALE, beGIN, enGINe, oriGIN, dRUM, cRUMb, PORTion, sWINE, choCOLAte, MEADow, forSAKE
DRINKS = ["tea", "ale", "gin", "rum", "port", "wine", "cola", "mead", "sake", "pop", "beer", "cider", "milk", "cava", "lager", "stout", "sherry",
          "brandy", "vodka", "whisky", "punch", "cocoa", "juice", "latte", "mocha", "perry", "soda", "grog", "sack", "chai"]
RIGHT = ["Steam", "Teach", "Instead", "Tale", "Scale", "Begin", "Engine", "Origin", "Drum", "Crumb", "Portion", "Swine", "Chocolate", "Meadow", "Forsake"]
WRONG = ["Pillow", "Garden", "Button", "Ladder", "Basket"]
assert all(any(v in w.lower() for v in DRINKS) for w in RIGHT)
assert not [w for w in WRONG if any(v in w.lower() for v in DRINKS)], [w for w in WRONG if any(v in w.lower() for v in DRINKS)]
board("Words with a drink hidden inside them", "Anagrams and wordplay", "medium", ["wordplay", "hidden words", "drinks"], RIGHT, WRONG)

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-112.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
