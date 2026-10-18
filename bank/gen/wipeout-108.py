# Bank session 19 Oct 2026: new Wipeout boards -> bank/wipeout-108.json (words that take BR in front; currencies hidden in words).
# Same shapes as wipeout-92 to 94. Every decoy was checked letter by letter: no word made by putting BR in front of Milk/Fish/
# Cup/Coin/Tree, and no currency (asserted against a list) hidden in Pillow/Window/Button/Ladder/Basket.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

# brash, brace, brink, brought, brow, brown, brand, breach, braid, brawl, brother, broil, breast, brewer, bray
board("Words that make a new word when you put BR in front", "Anagrams and wordplay", "medium", ["wordplay", "letters"],
 ["Ash", "Ace", "Ink", "Ought", "Ow", "Own", "And", "Each", "Aid", "Awl", "Other", "Oil", "East", "Ewer", "Ay"],
 ["Milk", "Fish", "Cup", "Coin", "Tree"])
# doYEN, nEUROn, comPOUND, imPOUND, deCENT, reCENT, bRAND, erRAND, WONder, REALity, MARKet, FRANCe, DIMEnsion, tRIAL, FRANChise
MONEY = ["yen", "euro", "pound", "dollar", "cent", "rand", "won", "real", "peso", "rupee", "lira", "mark", "franc", "dime", "penny", "krona",
         "krone", "leu", "rial", "riyal", "dinar", "baht", "yuan", "lev", "lek", "kip", "sol", "zloty", "forint", "shekel", "pence", "quid",
         "shilling", "guinea", "florin", "groat", "ruble", "rouble", "kuna", "dong", "naira", "taka"]
RIGHT = ["Doyen", "Neuron", "Compound", "Impound", "Decent", "Recent", "Brand", "Errand", "Wonder", "Reality", "Market", "France", "Dimension", "Trial", "Franchise"]
WRONG = ["Pillow", "Window", "Button", "Ladder", "Basket"]
assert all(any(v in w.lower() for v in MONEY) for w in RIGHT)
assert not [w for w in WRONG if any(v in w.lower() for v in MONEY)]
board("Words with a currency hidden inside them", "Anagrams and wordplay", "hard", ["wordplay", "hidden words", "money"], RIGHT, WRONG)

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-108.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
