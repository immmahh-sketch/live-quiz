# Bank session 19 Oct 2026: new Wipeout boards -> bank/wipeout-116.json (words that take BL in front; metals hidden in words).
# Same shapes as wipeout-92 to 94. Every decoy was checked letter by letter: no word made by putting BL in front of Milk/Fish/
# Cup/Coin/Tree, and no metal (asserted against a list) hidden in Pillow/Garden/Button/Ladder/Basket.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

# blink, bland, blare, bleach, bleat, blend, blimp, bloat, blow, blown, blaster, blunder, blender, blab, blear
board("Words that make a new word when you put BL in front", "Anagrams and wordplay", "medium", ["wordplay", "letters"],
 ["Ink", "And", "Are", "Each", "Eat", "End", "Imp", "Oat", "Ow", "Own", "Aster", "Under", "Ender", "Ab", "Ear"],
 ["Milk", "Fish", "Cup", "Coin", "Tree"])
# sTINg, maTINee, desTINy, saTIN, laTIN, conTINent, reTINa, batTINg, TINsel, IRONic, envIRONment, mariGOLD, misLEAD, pLEAD, LEADer
METALS = ["tin", "iron", "gold", "lead", "zinc", "copper", "brass", "steel", "nickel", "silver", "bronze", "chrome", "platinum", "mercury",
          "cobalt", "titanium", "aluminium", "pewter", "solder", "alloy", "tungsten", "uranium", "lithium", "sodium"]
RIGHT = ["Sting", "Matinee", "Destiny", "Satin", "Latin", "Continent", "Retina", "Batting", "Tinsel", "Ironic", "Environment", "Marigold", "Mislead", "Plead", "Leader"]
WRONG = ["Pillow", "Garden", "Button", "Ladder", "Basket"]
assert all(any(v in w.lower() for v in METALS) for w in RIGHT)
assert not [w for w in WRONG if any(v in w.lower() for v in METALS)], [w for w in WRONG if any(v in w.lower() for v in METALS)]
board("Words with a metal hidden inside them", "Anagrams and wordplay", "medium", ["wordplay", "hidden words", "metals"], RIGHT, WRONG)

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-116.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
