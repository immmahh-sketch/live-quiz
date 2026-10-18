# Bank session 18 Oct 2026: new Wipeout boards -> bank/wipeout-104.json (words that take an R in front; weapons hidden in words).
# Same shapes as wipeout-92 to 94. Every decoy was checked letter by letter: no word made by putting R in front of Milk/Fish/
# Cup/Coin/Shoe, and no weapon (asserted against a list) hidden in Pillow/Garden/Button/Ladder/Basket.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

# race, rail, rash, rear, reel, rink, roar, rice, rally, rant, raid, ramp, reach, rode, rate
board("Words that make a new word when you put an R in front", "Anagrams and wordplay", "easy", ["wordplay", "letters"],
 ["Ace", "Ail", "Ash", "Ear", "Eel", "Ink", "Oar", "Ice", "Ally", "Ant", "Aid", "Amp", "Each", "Ode", "Ate"],
 ["Milk", "Fish", "Cup", "Coin", "Shoe"])
# beGUN, GUNk, elBOW, BOWl, nARROW, bARROW, gLANCE, freeLANCE, griMACE, sPIKE, relAXEd, BOMBastic, rieSLING, deterMINE, exaMINE
WEAPONS = ["gun", "bow", "arrow", "sword", "spear", "lance", "mace", "pike", "axe", "bomb", "sling", "mine", "club", "knife", "dagger",
           "sabre", "dirk", "rifle", "pistol", "cannon", "tank", "mortar", "dart", "musket", "cutlass", "rapier", "halberd", "javelin"]
RIGHT = ["Begun", "Gunk", "Elbow", "Bowl", "Narrow", "Barrow", "Glance", "Freelance", "Grimace", "Spike", "Relaxed", "Bombastic", "Riesling", "Determine", "Examine"]
WRONG = ["Pillow", "Garden", "Button", "Ladder", "Basket"]
assert all(any(v in w.lower() for v in WEAPONS) for w in RIGHT)
assert not [w for w in WRONG if any(v in w.lower() for v in WEAPONS)]
board("Words with a weapon hidden inside them", "Anagrams and wordplay", "medium", ["wordplay", "hidden words", "weapons"], RIGHT, WRONG)

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-104.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
