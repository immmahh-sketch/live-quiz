# Bank session 19 Oct 2026: 3 Play Your Cards Right games -> bank/cards-114.json (the red kite, the starling, the dragonfly).
# Probed against every cards game in the live bank first (no kite, starling or dragonfly games). Numbers are the commonly quoted ones.
# A row of 5-7 cards each: what's on the card, what it shows when it flips, and the number compared. No equal neighbours.
import json, os
G = []
def game(text, cat, diff, tags, cards):
    ns = [n for _, _, n in cards]
    assert 5 <= len(cards) <= 7, text
    assert all(ns[i] != ns[i - 1] for i in range(1, len(ns))), (text, 'equal neighbours')
    assert len({l for l, _, _ in cards}) == len(cards), (text, 'repeated card')
    G.append({"type": "cards", "text": "Play Your Cards Right: " + text, "category": cat, "tags": ["Play Your Cards Right"] + tags, "difficulty": diff,
              "cards": [{"label": l, "value": v, "n": n} for l, v, n in cards]})

game("the numbers of a red kite", "Nature", "hard", ["red kites", "birds of prey", "British wildlife"], [
 ("Year red kites were first released back into England and Scotland", "1989", 1989), ("Wingspan in cm, roughly", "180", 180),
 ("Eggs in a typical clutch", "2", 2), ("Grams it weighs, roughly", "1,000", 1000), ("Years it usually lives in the wild", "4", 4)])
game("the numbers of a starling", "Nature", "hard", ["starlings", "birds", "British wildlife"], [
 ("Grams it weighs, roughly", "75", 75), ("Eggs in a typical clutch", "5", 5), ("Wingspan in cm, roughly", "40", 40),
 ("Days its eggs take to hatch, roughly", "12", 12), ("Years it usually lives", "2", 2)])
game("the numbers of a dragonfly", "Nature", "medium", ["dragonflies", "insects", "British wildlife"], [
 ("Wings it has", "4", 4), ("Millions of years dragonflies have been around, roughly", "300", 300), ("Top speed in mph, roughly", "30", 30),
 ("Wingspan in cm of the giant prehistoric dragonfly Meganeura, roughly", "70", 70), ("Years a larva can spend under water, at most", "5", 5)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-114.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
