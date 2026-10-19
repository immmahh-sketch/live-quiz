# Bank session 19 Oct 2026: 3 Play Your Cards Right games -> bank/cards-108.json (the earthworm, the garden snail, the ladybird).
# Probed against every cards game in the live bank first (no worm, snail or ladybird games). Numbers are the commonly quoted ones.
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

game("the numbers of an earthworm", "Nature", "medium", ["worms", "British wildlife", "gardening"], [
 ("Hearts, as they're usually counted", "5", 5), ("Segments in its body, roughly", "150", 150), ("Eyes", "0", 0),
 ("Centimetres long, at most", "25", 25), ("Years it can live", "8", 8)])
game("the numbers of a garden snail", "Nature", "medium", ["snails", "British wildlife", "gardening"], [
 ("Tentacles on its head", "4", 4), ("Tiny teeth on its tongue, roughly", "14,000", 14000), ("Millimetres it moves in a second", "1", 1),
 ("Eggs in a batch, roughly", "80", 80), ("Years it can live", "3", 3)])
game("the numbers of a ladybird", "Nature", "easy", ["ladybirds", "insects", "British wildlife"], [
 ("Spots on a seven-spot ladybird", "7", 7), ("Kinds of ladybird in the UK", "46", 46), ("Aphids it can eat in its lifetime", "5,000", 5000),
 ("Legs", "6", 6), ("Years it usually lives", "1", 1)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-108.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
