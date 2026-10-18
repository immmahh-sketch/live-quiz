# Bank session 18 Oct 2026: new Wipeout boards -> bank/wipeout-92.json (animals hidden in words; words that take an S in front).
# New wordplay shapes: no board in the bank is about hidden words, and the 'put X in front' boards use whole words, not one letter.
# Every decoy was checked letter by letter: no hidden animal in Candle/Silver/Garden/Pencil/Window, and no word made by
# putting S in front of Bread/Lamp/Fish/Door/Cake.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

# sCATter, piRATe, plANT, DOGma, COWardly, PIGment, bOWLing, BATtery, HENna, escAPE, RAMble, BEARing, jEWEl, GOATee, MOLEcule
board("Words with an animal hidden inside them", "Anagrams and wordplay", "medium", ["wordplay", "hidden words", "animals"],
 ["Scatter", "Pirate", "Planet", "Dogma", "Cowardly", "Pigment", "Bowling", "Battery", "Henna", "Escape", "Ramble", "Bearing", "Jewel", "Goatee", "Molecule"],
 ["Candle", "Silver", "Garden", "Pencil", "Window"])
# stool, share, swing, slip, snail, spear, smile, star, swear, slow, skill, spot, slice, snap, scream
board("Words that make a new word when you put an S in front", "Anagrams and wordplay", "easy", ["wordplay", "letters"],
 ["Tool", "Hare", "Wing", "Lip", "Nail", "Pear", "Mile", "Tar", "Wear", "Low", "Kill", "Pot", "Lice", "Nap", "Cream"],
 ["Bread", "Lamp", "Fish", "Door", "Cake"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-92.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
