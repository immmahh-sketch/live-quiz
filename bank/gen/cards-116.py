# Bank session 19 Oct 2026: 3 Play Your Cards Right games -> bank/cards-116.json (the pine marten, the blackbird, the house sparrow).
# Probed against every cards game in the live bank first (no marten, blackbird or sparrow games). Numbers are the commonly quoted ones.
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

game("the numbers of a pine marten", "Nature", "hard", ["pine martens", "British wildlife"], [
 ("Grams it weighs, roughly", "1,500", 1500), ("Kits in a typical litter", "3", 3), ("Year pine martens were released back into Wales", "2015", 2015),
 ("Length of its tail in cm, roughly", "25", 25), ("Teeth it has", "38", 38)])
game("the numbers of a blackbird", "Nature", "medium", ["blackbirds", "birds", "British wildlife"], [
 ("Grams it weighs, roughly", "100", 100), ("Eggs in a typical clutch", "4", 4), ("Days its eggs take to hatch, roughly", "13", 13),
 ("Millions of breeding pairs in the UK, roughly", "5", 5), ("Years it usually lives", "3", 3)])
game("the numbers of a house sparrow", "Nature", "medium", ["sparrows", "birds", "British wildlife"], [
 ("Grams it weighs, roughly", "30", 30), ("Eggs in a typical clutch", "4", 4), ("Percentage the UK population fell by from the 1970s, roughly", "70", 70),
 ("Broods it can raise in a year", "3", 3), ("Millions of breeding pairs in the UK, roughly", "5", 5)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-116.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
