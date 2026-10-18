# Bank session 18 Oct 2026: 3 Play Your Cards Right games -> bank/cards-99.json (the dairy cow, the sheep, the pig).
# Probed against every cards game in the live bank first (no cow, sheep or pig games; Lester Piggott is in). Numbers are the commonly quoted ones.
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

game("the numbers of a dairy cow", "Nature", "medium", ["cows", "farming", "animals"], [
 ("Compartments in its stomach", "4", 4), ("Litres of milk it gives a day", "25", 25), ("Months it's pregnant", "9", 9),
 ("Hours a day it spends chewing the cud", "8", 8), ("Kilograms it weighs", "650", 650)])
game("the numbers of a sheep", "Nature", "medium", ["sheep", "farming", "animals"], [
 ("Millions of sheep in the UK", "31", 31), ("Kilograms of wool it grows a year", "4", 4), ("Degrees it can see around itself", "300", 300),
 ("Months it's pregnant", "5", 5), ("Years it can live", "12", 12)])
game("the numbers of a pig", "Nature", "medium", ["pigs", "farming", "animals"], [
 ("Piglets in a typical litter", "11", 11), ("Decibels of its loudest squeal", "115", 115), ("Months a sow is pregnant, roughly", "4", 4),
 ("Teats on a sow", "14", 14), ("Millions of pigs in the UK", "5", 5)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-99.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
