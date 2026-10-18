# Bank session 19 Oct 2026: new Wipeout boards -> bank/wipeout-105.json (words that take an N in front; girls' names hidden in words).
# Same shapes as wipeout-92 to 94. Every decoy was checked letter by letter: no word made by putting N in front of Milk/Fish/
# Cup/Coin/Shoe, and no girl's name (asserted against a list) hidden in Pillow/Garden/Button/Ladder/Basket.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

# nail, near, neat, nice, never, none, nought, naught, nape, node, narrow, neither, nether, nark, newer
board("Words that make a new word when you put an N in front", "Anagrams and wordplay", "medium", ["wordplay", "letters"],
 ["Ail", "Ear", "Eat", "Ice", "Ever", "One", "Ought", "Aught", "Ape", "Ode", "Arrow", "Either", "Ether", "Ark", "Ewer"],
 ["Milk", "Fish", "Cup", "Coin", "Shoe"])
# bANNer, ANNoy, EVEning, sEVEn, purSUE, isSUE, sKATEboard, PAMphlet, LIZard, oMEGa, tRUTH, dilEMMA, umbrELLA, caraMEL, anecDOTe
NAMES = ["ann", "eve", "may", "sue", "kate", "pam", "jan", "liz", "meg", "rose", "ruth", "emma", "ella", "mel", "val", "dot", "peg", "tina",
         "nan", "amy", "joy", "kim", "bea", "ada", "ida", "ivy", "fay", "gail", "jen", "lou", "lyn", "mia", "pat", "tia", "zoe", "eva", "ava",
         "una", "jill", "jane", "june", "beth", "lily", "rita", "edna", "vera", "nell", "kay", "dee"]
RIGHT = ["Banner", "Annoy", "Evening", "Seven", "Pursue", "Issue", "Skateboard", "Pamphlet", "Lizard", "Omega", "Truth", "Dilemma", "Umbrella", "Caramel", "Anecdote"]
WRONG = ["Pillow", "Garden", "Button", "Ladder", "Basket"]
assert all(any(v in w.lower() for v in NAMES) for w in RIGHT)
assert not [w for w in WRONG if any(v in w.lower() for v in NAMES)]
board("Words with a girl's name hidden inside them", "Anagrams and wordplay", "medium", ["wordplay", "hidden words", "names"], RIGHT, WRONG)

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-105.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
