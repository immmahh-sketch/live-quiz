# Bank session 19 Oct 2026: 3 Play Your Cards Right games -> bank/cards-106.json (the grey seal, the red deer, the puffin).
# Probed against every cards game in the live bank first (no seal, deer or puffin games). Numbers are the commonly quoted ones.
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

game("the numbers of a grey seal", "Nature", "hard", ["seals", "sea life", "British wildlife"], [
 ("Kilograms a big bull weighs", "300", 300), ("Percentage of the world's grey seals living around Britain", "40", 40), ("Weeks a pup keeps its white coat", "3", 3),
 ("Years it can live", "30", 30), ("Minutes it can stay under water", "20", 20)])
game("the numbers of a red deer", "Nature", "hard", ["deer", "Scotland", "British wildlife"], [
 ("Points on a 'royal' stag's antlers", "12", 12), ("Months a hind is pregnant", "8", 8), ("Centimetres tall at the shoulder", "120", 120),
 ("Red deer in Scotland, roughly", "400,000", 400000), ("Kilograms a big stag weighs", "190", 190)])
game("the numbers of a puffin", "Nature", "medium", ["puffins", "seabirds", "British wildlife"], [
 ("Eggs it lays a year", "1", 1), ("Fish it can carry in its beak at once, the record", "62", 62), ("Times its wings beat in a minute", "400", 400),
 ("Top flying speed in km/h", "88", 88), ("Years it can live", "20", 20)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-106.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
