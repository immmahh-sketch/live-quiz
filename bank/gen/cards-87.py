# Bank session 18 Oct 2026: 2 Play Your Cards Right games -> bank/cards-87.json (the Severn Bridge, the Royal Mail).
# Titles probed against every cards game in the live bank first. Eden Project and the Sage Gateshead were free too but left out:
# not five numbers I could vouch for.
# A row of 5-7 cards each: what's on the card, what it shows when it flips, and the number compared. Zig-zag, no equal neighbours.
import json, os
G = []
def game(text, cat, diff, tags, cards):
    ns = [n for _, _, n in cards]
    assert 5 <= len(cards) <= 7, text
    assert all(ns[i] != ns[i - 1] for i in range(1, len(ns))), (text, 'equal neighbours')
    assert len({l for l, _, _ in cards}) == len(cards), (text, 'repeated card')
    G.append({"type": "cards", "text": "Play Your Cards Right: " + text, "category": cat, "tags": ["Play Your Cards Right"] + tags, "difficulty": diff,
              "cards": [{"label": l, "value": v, "n": n} for l, v, n in cards]})

game("the numbers of the Severn Bridge", "UK geography", "hard", ["Severn Bridge", "bridges", "Wales", "England"], [
 ("Year it opened", "1966", 1966), ("Length of its main span, in metres", "988", 988), ("Year its tolls were scrapped", "2018", 2018),
 ("Height of its towers, in metres", "136", 136), ("Year the Second Severn Crossing opened beside it", "1996", 1996)])
game("the numbers of the Royal Mail", "History", "medium", ["Royal Mail", "post", "stamps", "Penny Black"], [
 ("Year the Penny Black went on sale", "1840", 1840), ("What a Penny Black cost, in pennies", "1", 1),
 ("Year of the first Royal Mail Christmas stamps", "1966", 1966), ("Year pillar boxes started being painted red", "1874", 1874),
 ("Year postcodes were first tried out, in Norwich", "1959", 1959)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-87.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
