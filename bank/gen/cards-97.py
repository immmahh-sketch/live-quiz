# Bank session 18 Oct 2026: 3 Play Your Cards Right games -> bank/cards-97.json (the bottlenose dolphin, the red fox, the mute swan).
# Probed against every cards game in the live bank first (no dolphin, fox or swan games). Numbers are the commonly quoted ones.
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

game("the numbers of a bottlenose dolphin", "Nature", "medium", ["dolphins", "sea life", "animals"], [
 ("Teeth in its mouth, roughly", "90", 90), ("Top speed in km/h", "35", 35), ("Minutes it can hold its breath", "10", 10),
 ("Years it can live", "40", 40), ("Metres long, fully grown", "3", 3)])
game("the numbers of a red fox", "Nature", "medium", ["foxes", "British wildlife", "animals"], [
 ("Cubs in a typical litter", "5", 5), ("Top speed in km/h", "50", 50), ("Years it usually lives in the wild", "2", 2),
 ("Kilograms an adult weighs", "6", 6), ("Metres away it can hear a watch tick, so it's said", "40", 40)])
game("the numbers of a mute swan", "Nature", "medium", ["swans", "birds", "British wildlife"], [
 ("Metres across its wings", "2", 2), ("Kilograms a big male weighs", "12", 12), ("Eggs in a typical clutch", "6", 6),
 ("Years it can live", "20", 20), ("Flying speed in km/h", "80", 80)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-97.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
