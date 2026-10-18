# Bank session 19 Oct 2026: new Wipeout boards -> bank/wipeout-107.json (words that take SH in front; fish hidden in words).
# Same shapes as wipeout-92 to 94. Every decoy was checked letter by letter: no word made by putting SH in front of Milk/Fish/
# Cup/Coin/Tree, and no fish (asserted against a list) hidden in Pillow/Window/Button/Ladder/Basket (Garden hides a gar).
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

# shall, share, shin, shore, shout, shown, shrub, shape, shark, shelf, shone, shrug, shaft, shale, shrink
board("Words that make a new word when you put SH in front", "Anagrams and wordplay", "medium", ["wordplay", "letters"],
 ["All", "Are", "In", "Ore", "Out", "Own", "Rub", "Ape", "Ark", "Elf", "One", "Rug", "Aft", "Ale", "Rink"],
 ["Milk", "Fish", "Cup", "Coin", "Tree"])
# fEELing, whEEL, pEEL, CODe, CARPet, pRAY, arRAY, sPIKE, DABble, emBASSy, CHARm, forTUNAte, conSOLE, SOLEmn, sHAKE
FISH = ["eel", "cod", "carp", "ray", "pike", "dab", "bass", "char", "tuna", "sole", "hake", "ling", "rudd", "chub", "dace", "perch", "trout",
        "bream", "plaice", "shad", "ide", "gar", "koi", "orfe", "tench", "roach", "goby", "smelt", "sprat", "skate", "shark", "pollock",
        "haddock", "herring", "mackerel", "salmon", "sardine", "anchovy", "bib", "pout", "wrasse", "mullet", "brill", "turbot"]
RIGHT = ["Feeling", "Wheel", "Peel", "Code", "Carpet", "Pray", "Array", "Spike", "Dabble", "Embassy", "Charm", "Fortunate", "Console", "Solemn", "Shake"]
WRONG = ["Pillow", "Window", "Button", "Ladder", "Basket"]
assert all(any(v in w.lower() for v in FISH) for w in RIGHT)
assert not [w for w in WRONG if any(v in w.lower() for v in FISH)]
board("Words with a fish hidden inside them", "Anagrams and wordplay", "medium", ["wordplay", "hidden words", "fish"], RIGHT, WRONG)

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-107.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
