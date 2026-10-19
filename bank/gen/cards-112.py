# Bank session 19 Oct 2026: 3 Play Your Cards Right games -> bank/cards-112.json (the African grey parrot, the wren, the swift).
# Probed against every cards game in the live bank first (no parrot, wren or swift games). Numbers are the commonly quoted ones.
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

game("the numbers of an African grey parrot", "Nature", "medium", ["parrots", "birds", "pets"], [
 ("Years it can live", "60", 60), ("Words Alex, the famous African grey, knew, roughly", "100", 100), ("Eggs in a typical clutch", "3", 3),
 ("Grams it weighs", "400", 400), ("Toes on each foot", "4", 4)])
game("the numbers of a wren", "Nature", "hard", ["wrens", "birds", "British wildlife"], [
 ("Grams it weighs", "10", 10), ("Eggs in a typical clutch", "6", 6), ("Millions of breeding pairs in the UK, roughly", "11", 11),
 ("Years it usually lives", "2", 2), ("Year its coin, the farthing, stopped being legal tender", "1960", 1960)])
game("the numbers of a swift", "Nature", "hard", ["swifts", "birds", "migration"], [
 ("Months a young swift can stay in the air without landing", "10", 10), ("Top speed in km/h", "110", 110), ("Years it can live", "20", 20),
 ("Eggs in a typical clutch", "2", 2), ("Weeks it spends in Britain each summer, roughly", "14", 14)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-112.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
