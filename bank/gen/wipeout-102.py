# Bank session 18 Oct 2026: new Wipeout boards -> bank/wipeout-102.json (words that take a D in front; car makes hidden in words).
# Same shapes as wipeout-92 to 94. Every decoy was checked letter by letter: no word made by putting D in front of Milk/Fish/
# Cup/Tree/Coin, and no car make (asserted against a list) hidden in Pillow/Garden/Button/Ladder/Basket.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

# drink, done, drag, dice, drum, down, dream, drift, dwell, danger, draw, drove, dread, drip, dash
board("Words that make a new word when you put a D in front", "Anagrams and wordplay", "medium", ["wordplay", "letters"],
 ["Rink", "One", "Rag", "Ice", "Rum", "Own", "Ream", "Rift", "Well", "Anger", "Raw", "Rove", "Read", "Rip", "Ash"],
 ["Milk", "Fish", "Cup", "Tree", "Coin"])
# afFORD, oxFORD, hereFORD, MINIstry, MINImum, adMINIster, SEATed, unSEAT, AUDIence, AUDItion, AUDIble, pROVERb, DAFfodil, DODGEm, ALFAlfa
CARS = ["kia", "ford", "mini", "seat", "audi", "rover", "daf", "dodge", "alfa", "lotus", "fiat", "opel", "skoda", "bmw", "honda", "mazda", "tesla",
        "saab", "lada", "volvo", "jeep", "smart", "ram", "gmc", "jaguar", "porsche", "ferrari", "nissan", "toyota", "lexus", "mg", "datsun", "morris", "austin"]
RIGHT = ["Afford", "Oxford", "Hereford", "Ministry", "Minimum", "Administer", "Seated", "Unseat", "Audience", "Audition", "Audible", "Proverb", "Daffodil", "Dodgem", "Alfalfa"]
WRONG = ["Pillow", "Garden", "Button", "Ladder", "Basket"]
assert all(any(v in w.lower() for v in CARS) for w in RIGHT)
assert not [w for w in WRONG if any(v in w.lower() for v in CARS)]
board("Words with a car make hidden inside them", "Anagrams and wordplay", "hard", ["wordplay", "hidden words", "cars"], RIGHT, WRONG)

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-102.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
