# Bank session 18 Oct 2026: 3 Play Your Cards Right games -> bank/cards-96.json (the tiger, the hippo, the giant panda).
# Probed against every cards game in the live bank first (Tiger Woods is in, but no tiger, hippo or panda games). Numbers are the commonly quoted ones.
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

game("the numbers of a tiger", "Nature", "medium", ["tigers", "big cats", "animals"], [
 ("Tigers left in the wild, roughly", "5,500", 5500), ("Stripes on its coat, roughly", "100", 100), ("Cubs in a typical litter", "3", 3),
 ("Top speed in km/h", "65", 65), ("Years it lives in the wild", "15", 15)])
game("the numbers of a hippo", "Nature", "hard", ["hippos", "Africa", "animals"], [
 ("Kilograms a big male weighs", "3,000", 3000), ("Top speed on land in km/h", "30", 30), ("Minutes it can hold its breath", "5", 5),
 ("Kilograms of grass it eats in a night", "35", 35), ("Years it can live", "40", 40)])
game("the numbers of a giant panda", "Nature", "medium", ["pandas", "China", "animals"], [
 ("Hours a day it spends eating", "14", 14), ("Kilograms of bamboo it eats a day, at least", "12", 12), ("Grams a newborn cub weighs", "100", 100),
 ("Giant pandas left in the wild, roughly", "1,800", 1800), ("Years it lives in the wild", "20", 20)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-96.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
