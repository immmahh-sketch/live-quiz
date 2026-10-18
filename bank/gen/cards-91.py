# Bank session 18 Oct 2026: 2 Play Your Cards Right games -> bank/cards-91.json (the emperor penguin, the honeybee).
# Probed against every cards game in the live bank first (no penguin or bee games). Numbers are the commonly quoted ones.
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

game("the numbers of an emperor penguin", "Nature", "hard", ["penguins", "Antarctica", "birds"], [
 ("Its height, in centimetres", "120", 120), ("Its weight at the heaviest, in kilos", "45", 45), ("How deep it can dive, in metres", "500", 500),
 ("How long it can hold its breath, in minutes", "20", 20), ("Days the father keeps the egg warm on his feet", "65", 65)])
game("the numbers of a honeybee", "Nature", "medium", ["bees", "insects", "honey"], [
 ("Its legs", "6", 6), ("Bees in a busy summer hive, roughly", "50,000", 50000), ("Its wings", "4", 4),
 ("How fast it flies, in mph", "15", 15), ("Its eyes", "5", 5)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-91.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
