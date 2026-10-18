# Bank session 18 Oct 2026: new Wipeout boards -> bank/wipeout-100.json (words that take a W in front; vegetables hidden in words).
# Same shapes as wipeout-92 to 94. Every decoy was checked letter by letter: no word made by putting W in front of Fish/Gold/
# Book/Cake/Lamp, and no vegetable (asserted against a list) hidden in Pillow/Garden/Button/Ladder/Basket.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

# wheat, where, wink, whip, wrap, wore, waver, wheel, what, wage, weight, wrest, wail, whole, wrung
board("Words that make a new word when you put a W in front", "Anagrams and wordplay", "medium", ["wordplay", "letters"],
 ["Heat", "Here", "Ink", "Hip", "Rap", "Ore", "Aver", "Heel", "Hat", "Age", "Eight", "Rest", "Ail", "Hole", "Rung"],
 ["Fish", "Gold", "Book", "Cake", "Lamp"])
# rePEAt, PEAce, sPEAk, apPEAr, sLEEK, BEANie, sCORN, CORNer, aCORN, uniCORN, orCHARD, RiCHARD, arCHIVE, BEETle, YAMmer
VEG = ["pea", "leek", "bean", "yam", "kale", "okra", "corn", "cress", "chard", "chive", "beet", "swede", "neep", "onion", "pepper", "carrot",
       "turnip", "potato", "sprout", "marrow", "squash", "celery", "endive", "rocket", "pak", "choi", "leek", "parsnip", "radish", "spud"]
RIGHT = ["Repeat", "Peace", "Speak", "Appear", "Sleek", "Beanie", "Scorn", "Corner", "Acorn", "Unicorn", "Orchard", "Richard", "Archive", "Beetle", "Yammer"]
WRONG = ["Pillow", "Garden", "Button", "Ladder", "Basket"]
assert all(any(v in w.lower() for v in VEG) for w in RIGHT)
assert not [w for w in WRONG if any(v in w.lower() for v in VEG)]
board("Words with a vegetable hidden inside them", "Anagrams and wordplay", "medium", ["wordplay", "hidden words", "vegetables"], RIGHT, WRONG)

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-100.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
