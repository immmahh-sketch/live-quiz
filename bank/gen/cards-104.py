# Bank session 19 Oct 2026: 3 Play Your Cards Right games -> bank/cards-104.json (the golden eagle, the peregrine falcon, the common frog).
# Probed against every cards game in the live bank first (no eagle, falcon or frog games). Numbers are the commonly quoted ones.
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

game("the numbers of a golden eagle", "Nature", "hard", ["eagles", "birds of prey", "Scotland"], [
 ("Metres across its wings", "2", 2), ("Top diving speed in km/h", "240", 240), ("Eggs in a typical clutch", "2", 2),
 ("Breeding pairs in Scotland, roughly", "500", 500), ("Years it can live in the wild", "25", 25)])
game("the numbers of a peregrine falcon", "Nature", "hard", ["falcons", "birds of prey", "British wildlife"], [
 ("Top diving speed in km/h", "320", 320), ("Eggs in a typical clutch", "4", 4), ("Breeding pairs in the UK, roughly", "1,750", 1750),
 ("Centimetres across its wings", "100", 100), ("Years it can live", "15", 15)])
game("the numbers of a common frog", "Nature", "medium", ["frogs", "British wildlife", "amphibians"], [
 ("Eggs in a clump of frogspawn, roughly", "2,000", 2000), ("Weeks it spends as a tadpole", "12", 12), ("Years it can live", "8", 8),
 ("Months it hibernates", "4", 4), ("Toes on each back foot", "5", 5)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-104.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
