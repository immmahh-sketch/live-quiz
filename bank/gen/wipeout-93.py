# Bank session 18 Oct 2026: new Wipeout boards -> bank/wipeout-93.json (body parts hidden in words; words that take an L in front).
# Same shapes as wipeout-92 (animals hidden, S in front). Every decoy was checked letter by letter: no body part hidden in
# Garden/Window/Bucket/Lantern/Pencil, and no word made by putting L in front of Oven/Apple/Arm/Egg/Ant.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

# SHINe, CHINa, bEARd, sHIP, LEGend, bARMy, ecLIPse, sHANDy, BROWse, orCHESTra, arGUMent, tomaTOEs, tRIBe, LUNGe, wHEEL
board("Words with a body part hidden inside them", "Anagrams and wordplay", "medium", ["wordplay", "hidden words", "the body"],
 ["Shine", "China", "Beard", "Ship", "Legend", "Barmy", "Eclipse", "Shandy", "Browse", "Orchestra", "Argument", "Tomatoes", "Tribe", "Lunge", "Wheel"],
 ["Garden", "Window", "Bucket", "Lantern", "Pencil"])
# lace, lamp, late, lice, lion, link, loaf, lash, laid, lend, ledge, lever, lark, learn, lover
board("Words that make a new word when you put an L in front", "Anagrams and wordplay", "easy", ["wordplay", "letters"],
 ["Ace", "Amp", "Ate", "Ice", "Ion", "Ink", "Oaf", "Ash", "Aid", "End", "Edge", "Ever", "Ark", "Earn", "Over"],
 ["Oven", "Apple", "Arm", "Egg", "Ant"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-93.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
