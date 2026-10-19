# Bank session 19 Oct 2026: new Wipeout boards -> bank/wipeout-115.json (words that take CR in front; instruments hidden in words).
# Same shapes as wipeout-92 to 94. Every decoy was checked letter by letter: no word made by putting CR in front of Milk/Fish/
# Cup/Coin/Tree, and no instrument (asserted against a list) hidden in Pillow/Garden/Button/Ladder/Basket.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

# crash, crate, cramp, crow, crown, craft, cram, croak, crone, croft, crouch, credit, crease, creek, crusher
board("Words that make a new word when you put CR in front", "Anagrams and wordplay", "medium", ["wordplay", "letters"],
 ["Ash", "Ate", "Amp", "Ow", "Own", "Aft", "Am", "Oak", "One", "Oft", "Ouch", "Edit", "Ease", "Eek", "Usher"],
 ["Milk", "Fish", "Cup", "Coin", "Tree"])
# sHARP, HARPoon, conunDRUM, absoLUTE, polLUTE, saLUTE, ORGANise, ORGANic, tHORNy, VIOLAte, SAXon, BELLy, reBELLion, dUKE, BELLow
MUSIC = ["harp", "drum", "lute", "organ", "gong", "fife", "horn", "piano", "oboe", "tuba", "viola", "sax", "bell", "bass", "flute", "cello", "lyre",
         "uke", "pipe", "sitar", "harmonica", "banjo", "kazoo", "bongo", "tabla", "zither", "cornet", "bugle", "fiddle", "triangle"]
RIGHT = ["Sharp", "Harpoon", "Conundrum", "Absolute", "Pollute", "Salute", "Organise", "Organic", "Thorny", "Violate", "Saxon", "Belly", "Rebellion", "Duke", "Bellow"]
WRONG = ["Pillow", "Garden", "Button", "Ladder", "Basket"]
assert all(any(v in w.lower() for v in MUSIC) for w in RIGHT)
assert not [w for w in WRONG if any(v in w.lower() for v in MUSIC)], [w for w in WRONG if any(v in w.lower() for v in MUSIC)]
board("Words with a musical instrument hidden inside them", "Anagrams and wordplay", "medium", ["wordplay", "hidden words", "music"], RIGHT, WRONG)

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-115.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
