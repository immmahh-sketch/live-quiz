# Bank session 19 Oct 2026: new Wipeout boards -> bank/wipeout-110.json (words that take CL in front; car parts hidden in words).
# Same shapes as wipeout-92 to 94. Every decoy was checked letter by letter: no word made by putting CL in front of Milk/Fish/
# Cup/Coin/Tree, and no car part (asserted against a list) hidden in Pillow/Garden/Button/Ladder/Basket (Window is one).
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

# claim, clash, clamp, clear, clever, clink, cloak, clone, clout, clown, clamber, clasp, clamour, clay, claw
board("Words that make a new word when you put CL in front", "Anagrams and wordplay", "medium", ["wordplay", "letters"],
 ["Aim", "Ash", "Amp", "Ear", "Ever", "Ink", "Oak", "One", "Out", "Own", "Amber", "Asp", "Amour", "Ay", "Aw"],
 ["Milk", "Fish", "Cup", "Coin", "Tree"])
# tHORNy, HORNet, BOOTh, BOOTleg, SEATed, pROOF, sWING, fLIGHT, pLIGHT, inFANt, FANcy, childHOOD, neighbourHOOD, DIALogue
CAR = ["horn", "boot", "seat", "roof", "wing", "light", "fan", "hood", "dial", "door", "window", "gear", "tyre", "wheel", "brake", "pedal", "axle",
       "clutch", "bumper", "bonnet", "mirror", "belt", "exhaust", "engine", "piston", "valve", "plug", "spoiler", "grille", "choke", "lock", "mat",
       "key", "tank", "fuse", "cam", "rim", "hub", "sump", "aerial", "wiper"]
RIGHT = ["Thorny", "Hornet", "Booth", "Bootleg", "Seated", "Proof", "Swing", "Flight", "Plight", "Infant", "Fancy", "Childhood", "Neighbourhood", "Dialogue", "Unseat"]
WRONG = ["Pillow", "Garden", "Button", "Ladder", "Basket"]
assert all(any(v in w.lower() for v in CAR) for w in RIGHT)
assert not [w for w in WRONG if any(v in w.lower() for v in CAR)], [w for w in WRONG if any(v in w.lower() for v in CAR)]
board("Words with a part of a car hidden inside them", "Anagrams and wordplay", "medium", ["wordplay", "hidden words", "cars"], RIGHT, WRONG)

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-110.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
