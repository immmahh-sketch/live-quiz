# Bank session 19 Oct 2026: 3 Play Your Cards Right games -> bank/cards-107.json (the otter, the mole, the swallow).
# Probed against every cards game in the live bank first (no otter, mole or swallow games). Numbers are the commonly quoted ones.
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

game("the numbers of an otter", "Nature", "hard", ["otters", "British wildlife", "animals"], [
 ("Cubs in a typical litter", "2", 2), ("Years it usually lives in the wild", "5", 5), ("Kilograms a big male weighs", "10", 10),
 ("Kilometres of river a male patrols", "20", 20), ("Minutes it can stay under water", "4", 4)])
game("the numbers of a mole", "Nature", "medium", ["moles", "British wildlife", "animals"], [
 ("Grams it weighs", "100", 100), ("Teeth in its mouth", "44", 44), ("Metres of tunnel it can dig in a day", "20", 20),
 ("Years it usually lives", "3", 3), ("Babies in a typical litter", "4", 4)])
game("the numbers of a swallow", "Nature", "medium", ["swallows", "birds", "migration"], [
 ("Kilometres it flies to South Africa for the winter", "10,000", 10000), ("Eggs in a typical clutch", "5", 5), ("Broods it raises in a summer", "2", 2),
 ("Grams it weighs", "20", 20), ("Days its eggs take to hatch", "15", 15)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-107.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
