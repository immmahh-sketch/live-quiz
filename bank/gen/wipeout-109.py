# Bank session 19 Oct 2026: new Wipeout boards -> bank/wipeout-109.json (words that take GR in front; tools hidden in words).
# Same shapes as wipeout-92 to 94. Every decoy was checked letter by letter: no word made by putting GR in front of Milk/Fish/
# Cup/Coin/Tree, and no tool (asserted against a list) hidden in Pillow/Window/Button/Ladder/Basket.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

# grace, graft, grail, grand, grant, grape, great, grill, grin, grit, grout, growl, grown, grasp, grid
board("Words that make a new word when you put GR in front", "Anagrams and wordplay", "medium", ["wordplay", "letters"],
 ["Ace", "Aft", "Ail", "And", "Ant", "Ape", "Eat", "Ill", "In", "It", "Out", "Owl", "Own", "Asp", "Id"],
 ["Milk", "Fish", "Cup", "Coin", "Tree"])
# brAWL, shAWL, crAWL, sHOE, bRAKE, proFILE, PLANEt, adVICE, serVICE, PICKle, PICKet, sNAIL, sPINach, tAXEs, seeSAW
TOOLS = ["axe", "saw", "awl", "hoe", "rake", "file", "drill", "plane", "level", "vice", "rule", "pick", "spade", "fork", "nail", "pin", "wrench",
         "mallet", "hammer", "screw", "chisel", "trowel", "spanner", "pliers", "shears", "adze", "auger", "hod", "jack", "lathe", "sander"]
RIGHT = ["Brawl", "Shawl", "Crawl", "Shoe", "Brake", "Profile", "Planet", "Advice", "Service", "Pickle", "Picket", "Snail", "Spinach", "Taxes", "Seesaw"]
WRONG = ["Pillow", "Window", "Button", "Ladder", "Basket"]
assert all(any(v in w.lower() for v in TOOLS) for w in RIGHT)
assert not [w for w in WRONG if any(v in w.lower() for v in TOOLS)]
board("Words with a tool hidden inside them", "Anagrams and wordplay", "medium", ["wordplay", "hidden words", "tools"], RIGHT, WRONG)

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-109.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
