# Bank session 19 Oct 2026: new Wipeout boards -> bank/wipeout-114.json (words that take TH in front; weather hidden in words).
# Same shapes as wipeout-92 to 94. Every decoy was checked letter by letter: no word made by putting TH in front of Milk/Fish/
# Cup/Coin/Tree, and no weather (asserted against a list) hidden in Pillow/Garden/Button/Ladder/Basket.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

# think, there, throw, thrust, thrash, thread, thrice, thought, throb, thrift, thin, than, that, thrush, thwart
board("Words that make a new word when you put TH in front", "Anagrams and wordplay", "medium", ["wordplay", "letters"],
 ["Ink", "Ere", "Row", "Rust", "Rash", "Read", "Rice", "Ought", "Rob", "Rift", "In", "An", "At", "Rush", "Wart"],
 ["Milk", "Fish", "Cup", "Coin", "Tree"])
# tRAIN, bRAIN, gRAIN, MISTake, cheMISTry, WINDow, reWIND, nightinGALE, reGALE, HAZEl, prICE, slICE, notICE, disGUST, auGUST
WEATHER = ["rain", "snow", "hail", "mist", "fog", "sun", "wind", "gale", "haze", "sleet", "frost", "thaw", "storm", "dew", "ice", "cloud", "smog",
           "gust", "heat", "thunder", "drizzle", "breeze", "squall", "flood", "hurricane", "tornado", "monsoon", "blizzard"]
RIGHT = ["Train", "Brain", "Grain", "Mistake", "Chemistry", "Window", "Rewind", "Nightingale", "Regale", "Hazel", "Price", "Slice", "Notice", "Disgust", "August"]
WRONG = ["Pillow", "Garden", "Button", "Ladder", "Basket"]
assert all(any(v in w.lower() for v in WEATHER) for w in RIGHT)
assert not [w for w in WRONG if any(v in w.lower() for v in WEATHER)], [w for w in WRONG if any(v in w.lower() for v in WEATHER)]
board("Words with a type of weather hidden inside them", "Anagrams and wordplay", "medium", ["wordplay", "hidden words", "weather"], RIGHT, WRONG)

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-114.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
