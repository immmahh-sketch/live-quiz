# Bank session 19 Oct 2026: 3 Play Your Cards Right games -> bank/cards-111.json (the buzzard, the osprey, the jellyfish).
# Probed against every cards game in the live bank first (no buzzard, osprey or jellyfish games). Numbers are the commonly quoted ones.
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

game("the numbers of a buzzard", "Nature", "medium", ["buzzards", "birds of prey", "British wildlife"], [
 ("Centimetres across its wings", "120", 120), ("Breeding pairs in the UK, roughly", "70,000", 70000), ("Eggs in a typical clutch", "3", 3),
 ("Years it can live", "25", 25), ("Kilograms it weighs, roughly", "1", 1)])
game("the numbers of an osprey", "Nature", "hard", ["ospreys", "birds of prey", "Scotland"], [
 ("Centimetres across its wings", "160", 160), ("Kilometres it flies to West Africa each winter, roughly", "5,000", 5000), ("Eggs in a typical clutch", "3", 3),
 ("Year ospreys came back to breed in Scotland", "1954", 1954), ("Breeding pairs in the UK now, roughly", "300", 300)])
game("the numbers of a jellyfish", "Nature", "medium", ["jellyfish", "sea life", "animals"], [
 ("Percentage of its body that's water", "95", 95), ("Brains", "0", 0), ("Millions of years jellyfish have been around", "500", 500),
 ("Metres a lion's mane jellyfish's tentacles can reach", "30", 30), ("Hearts", "0", 0)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-111.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
