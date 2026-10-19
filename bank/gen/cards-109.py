# Bank session 19 Oct 2026: 3 Play Your Cards Right games -> bank/cards-109.json (the kingfisher, the grey heron, the magpie).
# Probed against every cards game in the live bank first (no kingfisher, heron or magpie games). Numbers are the commonly quoted ones.
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

game("the numbers of a kingfisher", "Nature", "hard", ["kingfishers", "birds", "British wildlife"], [
 ("Grams it weighs", "40", 40), ("Broods it raises in a year", "2", 2), ("Centimetres long", "16", 16),
 ("Eggs in a typical clutch", "6", 6), ("Years it usually lives", "2", 2)])
game("the numbers of a grey heron", "Nature", "hard", ["herons", "birds", "British wildlife"], [
 ("Centimetres across its wings", "185", 185), ("Centimetres tall", "95", 95), ("Eggs in a typical clutch", "4", 4),
 ("Breeding pairs in the UK, roughly", "10,000", 10000), ("Years it usually lives", "5", 5)])
game("the numbers of a magpie", "Nature", "medium", ["magpies", "birds", "British wildlife"], [
 ("Magpies for 'a secret never to be told' in the rhyme", "7", 7), ("Eggs in a typical clutch", "6", 6), ("Centimetres long, beak to tail", "45", 45),
 ("Breeding pairs in the UK, roughly", "600,000", 600000), ("Years it usually lives", "3", 3)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-109.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
