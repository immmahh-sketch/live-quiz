# Bank session 18 Oct 2026: new Wipeout boards -> bank/wipeout-101.json (words that take a G in front; trees hidden in words).
# Same shapes as wipeout-92 to 94. Every decoy was checked letter by letter: no word made by putting G in front of Shoe/Milk/
# Tree/Desk/Cup, and no tree (asserted against a list) hidden in Pillow/Garden/Button/Ladder/Basket.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

# grate, glove, glad, ghost, grid, grip, ground, gaunt, glean, grain, glance, grow, globe, glass, grave
board("Words that make a new word when you put a G in front", "Anagrams and wordplay", "medium", ["wordplay", "letters"],
 ["Rate", "Love", "Lad", "Host", "Rid", "Rip", "Round", "Aunt", "Lean", "Rain", "Lance", "Row", "Lobe", "Lass", "Rave"],
 ["Shoe", "Milk", "Tree", "Desk", "Cup"])
# sOAK, clOAK, crOAK, fASHion, hELMet, FIRst, FIRm, sPINE, bALDERdash, ELDERly, PLANEt, sTEAK, HOLLYwood, BOXer, PALMistry
TREES = ["oak", "ash", "elm", "fir", "yew", "pine", "bay", "box", "palm", "lime", "alder", "elder", "plane", "teak", "holly", "fig", "beech",
         "hazel", "maple", "larch", "cedar", "rowan", "willow", "birch", "gum", "cork", "olive", "apple", "pear", "plum", "cherry", "date", "spruce", "aspen", "poplar"]
RIGHT = ["Soak", "Cloak", "Croak", "Fashion", "Helmet", "First", "Firm", "Spine", "Balderdash", "Elderly", "Planet", "Steak", "Hollywood", "Boxer", "Palmistry"]
WRONG = ["Pillow", "Garden", "Button", "Ladder", "Basket"]
assert all(any(v in w.lower() for v in TREES) for w in RIGHT)
assert not [w for w in WRONG if any(v in w.lower() for v in TREES)]
board("Words with a tree hidden inside them", "Anagrams and wordplay", "medium", ["wordplay", "hidden words", "trees"], RIGHT, WRONG)

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-101.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
