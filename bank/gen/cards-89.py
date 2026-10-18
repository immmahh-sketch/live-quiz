# Bank session 18 Oct 2026: 2 Play Your Cards Right games -> bank/cards-89.json (the giraffe, the African elephant).
# Every big landmark already has a game (London Eye, Eiffel Tower, Statue of Liberty, Shard...), so these are animals,
# probed against every cards game in the live bank first. Numbers are the commonly quoted ones (up to / about).
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

game("the numbers of a giraffe", "Nature", "medium", ["giraffes", "animals", "Africa"], [
 ("Bones in its neck", "7", 7), ("Height of a tall male, in feet", "18", 18), ("How long a pregnancy lasts, in months", "15", 15),
 ("Length of its tongue, in centimetres", "50", 50), ("Its top speed, in mph", "35", 35)])
game("the numbers of an African elephant", "Nature", "medium", ["elephants", "animals", "Africa"], [
 ("How long a pregnancy lasts, in months", "22", 22), ("Weight of a big bull, in tonnes", "6", 6), ("Muscles in its trunk, roughly", "40,000", 40000),
 ("Hours a day it can spend eating", "16", 16), ("How long it can live in the wild, in years", "70", 70)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-89.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
