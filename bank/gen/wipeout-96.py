# Bank session 18 Oct 2026: new Wipeout boards -> bank/wipeout-96.json (words that take a C in front; numbers hidden in words).
# Same shapes as wipeout-92 to 94. Every decoy was checked letter by letter: no word made by putting C in front of Fish/Desk/
# Gold/Tree/Bird, and no number (one to ten) hidden in Pillow/Garden/Bucket/Saddle/Mirror.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

# chill, clock, crest, cold, cart, clone, cash, clap, crow, chip, crib, crate, clean, clever, cheap
board("Words that make a new word when you put a C in front", "Anagrams and wordplay", "easy", ["wordplay", "letters"],
 ["Hill", "Lock", "Rest", "Old", "Art", "Lone", "Ash", "Lap", "Row", "Hip", "Rib", "Rate", "Lean", "Lever", "Heap"],
 ["Fish", "Desk", "Gold", "Tree", "Bird"])
# lONEly, mONEy, phONE, stONE, hONEst, TENnis, atTENd, kitTEN, ofTEN, lisTEN, neTWOrk, caNINE, wEIGHT, hEIGHT, frEIGHT
board("Words with a number hidden inside them", "Anagrams and wordplay", "medium", ["wordplay", "hidden words", "numbers"],
 ["Lonely", "Money", "Phone", "Stone", "Honest", "Tennis", "Attend", "Kitten", "Often", "Listen", "Network", "Canine", "Weight", "Height", "Freight"],
 ["Pillow", "Garden", "Bucket", "Saddle", "Mirror"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-96.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
