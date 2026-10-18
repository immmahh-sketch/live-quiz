# Bank session 18 Oct 2026: 3 Play Your Cards Right games -> bank/cards-98.json (the barn owl, the robin, the badger).
# Probed against every cards game in the live bank first (no owl, robin or badger games). Numbers are the commonly quoted ones.
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

game("the numbers of a barn owl", "Nature", "medium", ["owls", "birds", "British wildlife"], [
 ("Degrees it can turn its head", "270", 270), ("Eggs in a typical clutch", "5", 5), ("Grams it weighs", "300", 300),
 ("Years it usually lives in the wild", "4", 4), ("Centimetres across its wings", "90", 90)])
game("the numbers of a robin", "Nature", "medium", ["robins", "birds", "British wildlife"], [
 ("Eggs in a typical clutch", "5", 5), ("Grams it weighs", "18", 18), ("Broods it raises in a year", "2", 2),
 ("Days its eggs take to hatch", "13", 13), ("Years it usually lives", "2", 2)])
game("the numbers of a badger", "Nature", "hard", ["badgers", "British wildlife", "animals"], [
 ("Cubs in a typical litter", "3", 3), ("Kilograms an adult weighs", "12", 12), ("Earthworms it can eat in a night", "200", 200),
 ("Badgers in a typical social group", "6", 6), ("Badgers in England and Wales, roughly", "485,000", 485000)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-98.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
