# Bank session 19 Oct 2026: new Wipeout boards -> bank/wipeout-118.json (words that take a Y on the end; farm animals hidden in words).
# Same shapes as wipeout-92 to 94. Every decoy was checked letter by letter: no word made by adding Y to Cup/Desk/Coin/
# Tree/Lamp, and no farm animal (asserted against a list) hidden in Pillow/Garden/Button/Ladder/Window (Basket hides an ass).
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

# busy, every, handy, lucky, rainy, salty, sandy, windy, dusty, hairy, cloudy, grassy, messy, rusty, bumpy
board("Words that make a new word when you add a Y to the end", "Anagrams and wordplay", "easy", ["wordplay", "letters"],
 ["Bus", "Ever", "Hand", "Luck", "Rain", "Salt", "Sand", "Wind", "Dust", "Hair", "Cloud", "Grass", "Mess", "Rust", "Bump"],
 ["Cup", "Desk", "Coin", "Tree", "Lamp"])
# COWard, sCOWl, PIGment, RAMble, pRAM, dRAMa, jEWEl, BULLet, BULLetin, nightMARE, bOX, OXygen, tOXic, paradOX, RAMp
FARM = ["cow", "pig", "hen", "ram", "ewe", "bull", "hog", "sow", "duck", "colt", "mare", "calf", "lamb", "ox", "goat", "sheep", "horse", "pony",
        "cock", "foal", "mule", "ass", "steer", "heifer", "boar", "gander", "goose", "turkey", "chick", "llama"]
RIGHT = ["Coward", "Scowl", "Pigment", "Ramble", "Pram", "Drama", "Jewel", "Bullet", "Bulletin", "Nightmare", "Box", "Oxygen", "Toxic", "Paradox", "Ramp"]
WRONG = ["Pillow", "Garden", "Button", "Ladder", "Window"]
assert all(any(v in w.lower() for v in FARM) for w in RIGHT)
assert not [w for w in WRONG if any(v in w.lower() for v in FARM)], [w for w in WRONG if any(v in w.lower() for v in FARM)]
board("Words with a farm animal hidden inside them", "Anagrams and wordplay", "medium", ["wordplay", "hidden words", "farm animals"], RIGHT, WRONG)

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-118.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
