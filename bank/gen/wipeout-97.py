# Bank session 18 Oct 2026: new Wipeout boards -> bank/wipeout-97.json (words that take a P in front; vehicles hidden in words).
# Same shapes as wipeout-92 to 94. Every decoy was checked letter by letter: no word made by putting P in front of Sock/Lamp/
# Book/Cake/Door, and no vehicle (asserted against a list) hidden in Pillow/Lemon/Garden/Sister/Mirror.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

# plane, pray, price, peach, pear, plump, pill, pink, prod, paid, place, pride, please, pitch, plug
board("Words that make a new word when you put a P in front", "Anagrams and wordplay", "easy", ["wordplay", "letters"],
 ["Lane", "Ray", "Rice", "Each", "Ear", "Lump", "Ill", "Ink", "Rod", "Aid", "Lace", "Ride", "Lease", "Itch", "Lug"],
 ["Sock", "Lamp", "Book", "Cake", "Door"])
# CARpet, sCARf, sCARce, sCARlet, BUSy, BUSh, amBUSh, aBUSe, VANish, VANilla, adVANce, CABin, CABbage, TRAMpoline, TRAMple
VEHICLES = ["car", "bus", "van", "cab", "tram", "taxi", "ship", "boat", "train", "bike", "jet", "cart", "ute", "sub", "ark", "raft", "yacht", "lorry", "coach", "barge", "punt", "kart", "gig", "tank"]
RIGHT = ["Carpet", "Scarf", "Scarce", "Scarlet", "Busy", "Bush", "Ambush", "Abuse", "Vanish", "Vanilla", "Advance", "Cabin", "Cabbage", "Trampoline", "Trample"]
WRONG = ["Pillow", "Lemon", "Garden", "Sister", "Mirror"]
assert all(any(v in w.lower() for v in VEHICLES) for w in RIGHT)
assert not [w for w in WRONG if any(v in w.lower() for v in VEHICLES)]
board("Words with a vehicle hidden inside them", "Anagrams and wordplay", "medium", ["wordplay", "hidden words", "vehicles"], RIGHT, WRONG)

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-97.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
