# Bank session 18 Oct 2026: 3 Play Your Cards Right games -> bank/cards-95.json (the camel, the gorilla, the koala).
# Probed against every cards game in the live bank first (no camel, gorilla or koala games). Numbers are the commonly quoted ones.
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

game("the numbers of a camel", "Nature", "medium", ["camels", "deserts", "animals"], [
 ("Humps on a dromedary", "1", 1), ("Litres of water it can drink in one go", "100", 100), ("Days it can go without water", "14", 14),
 ("Top speed in km/h", "65", 65), ("Years it can live", "40", 40)])
game("the numbers of a gorilla", "Nature", "medium", ["gorillas", "apes", "animals"], [
 ("Percentage of its DNA shared with us", "98", 98), ("Kilograms a big silverback weighs", "180", 180), ("Gorillas in a typical troop", "10", 10),
 ("Months a mother is pregnant", "9", 9), ("Years it can live in the wild", "40", 40)])
game("the numbers of a koala", "Nature", "medium", ["koalas", "Australia", "marsupials"], [
 ("Hours it sleeps a day", "20", 20), ("Months the joey lives in the pouch", "6", 6), ("Grams of eucalyptus leaves it eats a day", "500", 500),
 ("Thumbs on each front paw", "2", 2), ("Kilograms a big male weighs", "12", 12)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-95.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
