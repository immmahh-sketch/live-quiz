# Bank session 19 Oct 2026: new Wipeout boards -> bank/wipeout-113.json (words that take SC in front; creepy-crawlies hidden in words).
# Same shapes as wipeout-92 to 94. Every decoy was checked letter by letter: no word made by putting SC in front of Milk/Fish/
# Cup/Coin/Tree, and no creepy-crawly (asserted against a list) hidden in Pillow/Garden/Button/Ladder/Basket.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

# scale, scan, scant, scare, scold, scone, score, scout, scowl, scream, scrub, scramble, scamp, scion, scoops
board("Words that make a new word when you put SC in front", "Anagrams and wordplay", "medium", ["wordplay", "letters"],
 ["Ale", "An", "Ant", "Are", "Old", "One", "Ore", "Out", "Owl", "Ream", "Rub", "Ramble", "Amp", "Ion", "Oops"],
 ["Milk", "Fish", "Cup", "Coin", "Tree"])
# giANT, wANT, plANT, elephANT, BEEf, BEEn, MOTHer, sMOTHer, TICKet, sTICKy, bLOUSE, BUGle, uNIT, kNIT, pANTry
BUGS = ["ant", "bee", "fly", "gnat", "wasp", "moth", "flea", "tick", "louse", "mite", "bug", "nit", "worm", "slug", "snail", "spider", "aphid",
        "earwig", "cricket", "beetle", "midge", "weevil", "termite", "cicada", "locust", "emmet", "grub", "maggot"]
RIGHT = ["Giant", "Want", "Plant", "Elephant", "Beef", "Been", "Mother", "Smother", "Ticket", "Sticky", "Blouse", "Bugle", "Unit", "Knit", "Pantry"]
WRONG = ["Pillow", "Garden", "Button", "Ladder", "Basket"]
assert all(any(v in w.lower() for v in BUGS) for w in RIGHT)
assert not [w for w in WRONG if any(v in w.lower() for v in BUGS)], [w for w in WRONG if any(v in w.lower() for v in BUGS)]
board("Words with a creepy-crawly hidden inside them", "Anagrams and wordplay", "medium", ["wordplay", "hidden words", "insects"], RIGHT, WRONG)

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-113.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
