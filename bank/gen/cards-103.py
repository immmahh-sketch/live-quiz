# Bank session 19 Oct 2026: 3 Play Your Cards Right games -> bank/cards-103.json (the goat, the donkey, the grey squirrel).
# Probed against every cards game in the live bank first (no goat, donkey or squirrel games). Numbers are the commonly quoted ones.
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

game("the numbers of a goat", "Nature", "medium", ["goats", "farming", "animals"], [
 ("Compartments in its stomach", "4", 4), ("Days a nanny goat is pregnant", "150", 150), ("Kids in a typical birth", "2", 2),
 ("Years it can live", "15", 15), ("Degrees it can see around itself", "320", 320)])
game("the numbers of a donkey", "Nature", "medium", ["donkeys", "animals"], [
 ("Months a donkey is pregnant", "12", 12), ("Years it can live", "30", 30), ("Hands high, a typical donkey", "10", 10),
 ("Kilograms it weighs", "200", 200), ("Year the Donkey Sanctuary was founded in Devon", "1969", 1969)])
game("the numbers of a grey squirrel", "Nature", "medium", ["squirrels", "British wildlife", "animals"], [
 ("Year greys were first let loose in Britain", "1876", 1876), ("Millions of grey squirrels in the UK, roughly", "3", 3), ("Years it usually lives", "6", 6),
 ("Teeth in its mouth", "22", 22), ("Babies in a typical litter", "3", 3)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-103.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
