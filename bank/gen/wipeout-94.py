# Bank session 18 Oct 2026: new Wipeout boards -> bank/wipeout-94.json (colours hidden in words; words that take a B in front).
# Same shapes as wipeout-92/93. Every decoy was checked letter by letter: no colour hidden in Basket/Biscuit/Chimney/Doormat/
# Kitten, and no word made by putting B in front of Cat/Moon/Tree/Milk/Sock.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

# sTANd, TiTANic, TANgle, cREDit, hundRED, sh-RED, sTEALth, sCREAM, PLUMber, sLIME, pROSE, BUFFet, mariGOLD, JADEd, FAWNed
board("Words with a colour hidden inside them", "Anagrams and wordplay", "medium", ["wordplay", "hidden words", "colours"],
 ["Stand", "Titanic", "Tangle", "Credit", "Hundred", "Shred", "Stealth", "Scream", "Plumber", "Slime", "Prose", "Buffet", "Marigold", "Jaded", "Fawned"],
 ["Basket", "Biscuit", "Chimney", "Doormat", "Kitten"])
# brush, blame, boat, bring, ball, bear, band, bend, brain, bread, brag, blush, bride, bright, beat
board("Words that make a new word when you put a B in front", "Anagrams and wordplay", "easy", ["wordplay", "letters"],
 ["Rush", "Lame", "Oat", "Ring", "All", "Ear", "And", "End", "Rain", "Read", "Rag", "Lush", "Ride", "Right", "Eat"],
 ["Cat", "Moon", "Tree", "Milk", "Sock"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-94.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
