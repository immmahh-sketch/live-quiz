# Bank session 19 Oct 2026: new Wipeout boards -> bank/wipeout-119.json (take off the last letter; take off the first letter).
# Same shapes as wipeout-92 to 94. Every decoy was checked letter by letter: Lemon/Table/Robin/Garden/Window
# minus their last letter and Lemon/Robin/Garden/Window/Pencil minus their first are not words (Table was kept off the
# first-letter board: 'able').
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

# planet>plane, brand>bran, pearl>pear, scarf>scar, beard>bear, heart>hear, party>part, plant>plan, spark>spar, stare>star,
# fort>for, seat>sea, grime>grim, paste>past, spine>spin
RIGHT = ["Planet", "Brand", "Pearl", "Scarf", "Beard", "Heart", "Party", "Plant", "Spark", "Stare", "Fort", "Seat", "Grime", "Paste", "Spine"]
WRONG = ["Lemon", "Table", "Robin", "Garden", "Window"]
board("Words that leave a new word when you take off the last letter", "Anagrams and wordplay", "easy", ["wordplay", "letters"], RIGHT, WRONG)
# swing>wing, clock>lock, bear>ear, spill>pill, glove>love, scold>cold, price>rice, trust>rust, blink>link, plate>late,
# bring>ring, flower>lower, snow>now, wheat>heat, twig>wig
RIGHT = ["Swing", "Clock", "Bear", "Spill", "Glove", "Scold", "Price", "Trust", "Blink", "Plate", "Bring", "Flower", "Snow", "Wheat", "Twig"]
WRONG = ["Lemon", "Robin", "Garden", "Window", "Pencil"]
board("Words that leave a new word when you take off the first letter", "Anagrams and wordplay", "easy", ["wordplay", "letters"], RIGHT, WRONG)

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-119.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
