# Bank session 18 Oct 2026: new Wipeout boards -> bank/wipeout-99.json (words that take an H in front; birds hidden in words).
# Same shapes as wipeout-92 to 94. Every decoy was checked letter by letter: no word made by putting H in front of Milk/Rope/
# Lamp/Desk/Coin, and no bird (asserted against a list) hidden in Pillow/Garden/Button/Ladder/Basket.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

# harm, hear, heat, hail, hire, hall, hate, hedge, hour, hash, hold, heel, hand, howl, hark
board("Words that make a new word when you put an H in front", "Anagrams and wordplay", "easy", ["wordplay", "letters"],
 ["Arm", "Ear", "Eat", "Ail", "Ire", "All", "Ate", "Edge", "Our", "Ash", "Old", "Eel", "And", "Owl", "Ark"],
 ["Milk", "Rope", "Lamp", "Desk", "Coin"])
# bOWLing, knOWLedge, wHEN, HENce, TITle, peTITion, appeTITe, dEMUre, CROWd, patTERN, eTERNal, wesTERN, cROOKed, bROOK, GULLible
BIRDS = ["owl", "hen", "tit", "emu", "crow", "wren", "jay", "kite", "tern", "rook", "lark", "gull", "swan", "dove", "raven", "duck", "crane",
         "rhea", "kiwi", "auk", "ern", "teal", "coot", "rail", "ruff", "smew", "shag", "tui", "moa", "ibis", "mynah", "pie", "cock", "lory"]
RIGHT = ["Bowling", "Knowledge", "When", "Hence", "Title", "Petition", "Appetite", "Demure", "Crowd", "Pattern", "Eternal", "Western", "Crooked", "Brook", "Gullible"]
WRONG = ["Pillow", "Garden", "Button", "Ladder", "Basket"]
assert all(any(v in w.lower() for v in BIRDS) for w in RIGHT)
assert not [w for w in WRONG if any(v in w.lower() for v in BIRDS)]
board("Words with a bird hidden inside them", "Anagrams and wordplay", "medium", ["wordplay", "hidden words", "birds"], RIGHT, WRONG)

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-99.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
