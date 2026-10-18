# Bank session 18 Oct 2026: 3 Play Your Cards Right games -> bank/cards-100.json (the horse, the hen, the rabbit).
# Probed against every cards game in the live bank first (horse races are in, but no horse, hen or rabbit games). Numbers are the commonly quoted ones.
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

game("the numbers of a horse", "Nature", "medium", ["horses", "animals"], [
 ("Bones in its body", "205", 205), ("Months a mare is pregnant", "11", 11), ("Hands high, a typical riding horse", "16", 16),
 ("Years it can live", "30", 30), ("Litres of water it drinks a day", "40", 40)])
game("the numbers of a hen", "Nature", "easy", ["chickens", "farming", "animals"], [
 ("Toes on each foot", "4", 4), ("Days an egg takes to hatch", "21", 21), ("Eggs a good layer lays in a year", "300", 300),
 ("Hours it takes to make each egg", "26", 26), ("Years it can live", "8", 8)])
game("the numbers of a rabbit", "Nature", "medium", ["rabbits", "pets", "animals"], [
 ("Babies in a typical litter", "6", 6), ("Days a doe is pregnant", "31", 31), ("Teeth in its mouth", "28", 28),
 ("Years a pet rabbit can live", "9", 9), ("Degrees it can see around itself, almost", "360", 360)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-100.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
