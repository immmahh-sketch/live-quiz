# Bank session 19 Oct 2026: 3 Play Your Cards Right games -> bank/cards-115.json (the kestrel, the stag beetle, the red squirrel).
# Probed against every cards game in the live bank first (no kestrel, beetle or red squirrel games). Numbers are the commonly quoted ones.
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

game("the numbers of a kestrel", "Nature", "hard", ["kestrels", "birds of prey", "British wildlife"], [
 ("Grams it weighs, roughly", "200", 200), ("Wingspan in cm, roughly", "75", 75), ("Years it usually lives in the wild", "4", 4),
 ("Days its eggs take to hatch, roughly", "28", 28), ("Thousands of breeding pairs in the UK, roughly", "30", 30)])
game("the numbers of a stag beetle", "Nature", "hard", ["stag beetles", "insects", "British wildlife"], [
 ("Length of a big male in mm, roughly", "75", 75), ("Legs it has", "6", 6), ("Wings it has", "4", 4),
 ("Years it can spend as a grub underground, at most", "7", 7), ("Month (1-12) you're most likely to see one flying", "6 (June)", 6)])
game("the numbers of a red squirrel", "Nature", "medium", ["red squirrels", "British wildlife"], [
 ("Year grey squirrels were first let loose in Britain", "1876", 1876), ("Grams it weighs, roughly", "300", 300),
 ("Kittens in a typical litter", "3", 3), ("Length of its tail in cm, roughly", "18", 18),
 ("Percentage of the UK's red squirrels that live in Scotland, roughly", "75", 75), ("Years it usually lives in the wild", "3", 3)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-115.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
