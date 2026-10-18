# Bank session 18 Oct 2026: 2 Play Your Cards Right games -> bank/cards-93.json (the saltwater crocodile, the hedgehog).
# Probed against every cards game in the live bank first (no crocodile or hedgehog games). Numbers are the commonly quoted ones.
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

game("the numbers of a saltwater crocodile", "Nature", "hard", ["crocodiles", "reptiles", "Australia"], [
 ("Its length at the biggest, in metres", "6", 6), ("Teeth in its jaws", "66", 66), ("Eggs in a typical nest", "50", 50),
 ("How long it can live, in years", "70", 70), ("Minutes it can stay under water on one breath", "60", 60)])
game("the numbers of a hedgehog", "Nature", "medium", ["hedgehogs", "British wildlife", "animals"], [
 ("Spines on its back, roughly", "6,000", 6000), ("Years it usually lives in the wild", "3", 3), ("Months it hibernates", "5", 5),
 ("Hoglets in a typical litter", "4", 4), ("Kilometres it can walk in a night", "2", 2)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-93.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
