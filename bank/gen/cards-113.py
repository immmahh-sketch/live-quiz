# Bank session 19 Oct 2026: 3 Play Your Cards Right games -> bank/cards-113.json (the barn owl, the brown hare, the gannet).
# Probed against every cards game in the live bank first (no owl, hare or gannet games). Numbers are the commonly quoted ones.
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

game("the numbers of a barn owl", "Nature", "hard", ["owls", "birds", "British wildlife"], [
 ("Years it usually lives in the wild", "4", 4), ("Wingspan in cm, roughly", "90", 90), ("Degrees it can turn its head", "270", 270),
 ("Eggs in a typical clutch", "5", 5), ("Grams it weighs, roughly", "300", 300), ("Days its eggs take to hatch, roughly", "30", 30)])
game("the numbers of a brown hare", "Nature", "hard", ["hares", "British wildlife"], [
 ("Top speed in mph", "45", 45), ("Days it is pregnant, roughly", "42", 42), ("Leverets in a typical litter", "3", 3),
 ("Centimetres long its ears are, roughly", "10", 10), ("Kilograms it weighs, roughly", "4", 4)])
game("the numbers of a gannet", "Nature", "hard", ["gannets", "seabirds", "British wildlife"], [
 ("Wingspan in cm, roughly", "180", 180), ("Eggs it lays each year", "1", 1), ("Top diving speed in mph", "60", 60),
 ("Years before it starts breeding, roughly", "5", 5), ("Thousands of gannets on the Bass Rock, roughly", "150", 150),
 ("Weeks a chick spends on the nest, roughly", "13", 13)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-113.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
