# Bank session 19 Oct 2026: new Wipeout boards -> bank/wipeout-106.json (words that take ST in front; sports hidden in words).
# Same shapes as wipeout-92 to 94. Every decoy was checked letter by letter: no word made by putting ST in front of Milk/Fish/
# Cup/Coin/Shoe, and no sport (asserted against a list) hidden in Pillow/Garden/Button/Ladder/Basket.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

# still, stale, stand, stink, store, stripe, strain, strap, straw, stray, stone, state, stage, steel, stream
board("Words that make a new word when you put ST in front", "Anagrams and wordplay", "easy", ["wordplay", "letters"],
 ["Ill", "Ale", "And", "Ink", "Ore", "Ripe", "Rain", "Rap", "Raw", "Ray", "One", "Ate", "Age", "Eel", "Ream"],
 ["Milk", "Fish", "Cup", "Coin", "Shoe"])
# aPOLOgy, gROWING, thROWING, borROWING, narROWING, SKIll, SKIrt, SKIp, SKIn, sTAGe, cotTAGe, hosTAGe, vinTAGe, sPOOL, LiverPOOL
SPORTS = ["ski", "tag", "rowing", "polo", "pool", "golf", "darts", "bowls", "judo", "sumo", "luge", "squash", "tennis", "rugby", "boxing", "chess",
          "fencing", "rally", "karate", "archery", "cricket", "hockey", "netball", "diving", "sailing", "cycling", "running", "surfing", "skating",
          "rounders", "curling", "snooker", "billiards", "kabaddi", "lacrosse", "bandy", "shinty", "hurling"]
RIGHT = ["Apology", "Growing", "Throwing", "Borrowing", "Narrowing", "Skill", "Skirt", "Skip", "Skin", "Stage", "Cottage", "Hostage", "Vintage", "Spool", "Liverpool"]
WRONG = ["Pillow", "Garden", "Button", "Ladder", "Basket"]
assert all(any(v in w.lower() for v in SPORTS) for w in RIGHT)
assert not [w for w in WRONG if any(v in w.lower() for v in SPORTS)]
board("Words with a sport hidden inside them", "Anagrams and wordplay", "medium", ["wordplay", "hidden words", "sport"], RIGHT, WRONG)

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-106.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
