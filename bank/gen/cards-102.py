# Bank session 19 Oct 2026: 3 Play Your Cards Right games -> bank/cards-102.json (the hamster, the tortoise, the mallard).
# Probed against every cards game in the live bank first (no hamster, tortoise or duck games; 'the numbers of Mallard' is the steam engine, a different game). Numbers are the commonly quoted ones.
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

game("the numbers of a hamster", "Nature", "medium", ["hamsters", "pets", "animals"], [
 ("Years it usually lives", "2", 2), ("Days a Syrian hamster is pregnant", "16", 16), ("Babies in a typical litter", "8", 8),
 ("Kilometres it can run on its wheel in a night", "9", 9), ("Teeth in its mouth", "16", 16)])
game("the numbers of a tortoise", "Nature", "hard", ["tortoises", "pets", "reptiles"], [
 ("Age in 2026 of Jonathan, the oldest known land animal", "194", 194), ("Years a pet tortoise can live", "80", 80), ("Months it hibernates", "4", 4),
 ("Eggs in a typical clutch", "6", 6), ("Bones in its shell, roughly", "60", 60)])
game("the numbers of a mallard", "Nature", "medium", ["ducks", "birds", "British wildlife"], [
 ("Eggs in a typical clutch", "10", 10), ("Days its eggs take to hatch", "28", 28), ("Flying speed in km/h", "70", 70),
 ("Days before the ducklings can fly", "55", 55), ("Webbed toes on each foot", "3", 3)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-102.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
