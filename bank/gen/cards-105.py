# Bank session 19 Oct 2026: 3 Play Your Cards Right games -> bank/cards-105.json (the adder, the pipistrelle bat, the bumblebee).
# Probed against every cards game in the live bank first (no adder, bat or bumblebee games). Numbers are the commonly quoted ones.
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

game("the numbers of an adder", "Nature", "hard", ["adders", "snakes", "British wildlife"], [
 ("Venomous snakes native to Britain", "1", 1), ("Centimetres long, fully grown", "60", 60), ("Babies born at once, roughly", "10", 10),
 ("Months it hibernates", "5", 5), ("People killed by adder bites in Britain since 1876", "14", 14)])
game("the numbers of a pipistrelle bat", "Nature", "hard", ["bats", "British wildlife", "animals"], [
 ("Grams it weighs", "5", 5), ("Insects it can eat in a night", "3,000", 3000), ("Species of bat in the UK", "18", 18),
 ("Babies a female has a year", "1", 1), ("Centimetres across its wings", "20", 20)])
game("the numbers of a bumblebee", "Nature", "medium", ["bees", "insects", "British wildlife"], [
 ("Legs", "6", 6), ("Times its wings beat each second", "200", 200), ("Species of bumblebee in the UK", "24", 24),
 ("Eyes, counting the small ones", "5", 5), ("Bees in a big nest, roughly", "400", 400)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-105.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
