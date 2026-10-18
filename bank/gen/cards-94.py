# Bank session 18 Oct 2026: 3 Play Your Cards Right games -> bank/cards-94.json (the octopus, the red kangaroo, the ostrich).
# Probed against every cards game in the live bank first (no octopus, kangaroo or ostrich games). Numbers are the commonly quoted ones.
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

game("the numbers of an octopus", "Nature", "medium", ["octopuses", "sea life", "animals"], [
 ("Hearts", "3", 3), ("Arms", "8", 8), ("Suckers on each arm of a common octopus, roughly", "240", 240),
 ("Years a common octopus usually lives", "1", 1), ("Brains, as it's often said", "9", 9)])
game("the numbers of a red kangaroo", "Nature", "hard", ["kangaroos", "Australia", "animals"], [
 ("Top speed in km/h", "70", 70), ("Metres it can cover in one leap", "8", 8), ("Days pregnant before the joey is born", "33", 33),
 ("Grams a newborn joey weighs, roughly", "1", 1), ("Months the joey lives in the pouch", "8", 8)])
game("the numbers of an ostrich", "Nature", "medium", ["ostriches", "birds", "animals"], [
 ("Toes on each foot", "2", 2), ("Top speed in km/h", "70", 70), ("Chicken eggs one ostrich egg equals, roughly", "24", 24),
 ("Years it can live", "40", 40), ("Centimetres across its eye", "5", 5)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-94.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
