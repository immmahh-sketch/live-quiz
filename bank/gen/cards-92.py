# Bank session 18 Oct 2026: 2 Play Your Cards Right games -> bank/cards-92.json (the cheetah, the polar bear).
# Probed against every cards game in the live bank first (no cheetah or polar bear games). Numbers are the commonly quoted ones.
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

game("the numbers of a cheetah", "Nature", "medium", ["cheetahs", "big cats", "Africa"], [
 ("Its top speed, in mph", "70", 70), ("Seconds it takes to reach 60 mph", "3", 3), ("Its weight, in kilos", "50", 50),
 ("Cubs in a typical litter", "4", 4), ("Years it lives in the wild", "12", 12)])
game("the numbers of a polar bear", "Nature", "medium", ["polar bears", "Arctic", "bears"], [
 ("Weight of a big male, in kilos", "700", 700), ("Cubs in a usual litter", "2", 2), ("Polar bears left in the wild, roughly", "26,000", 26000),
 ("Its height standing up, in metres", "3", 3), ("Years it lives in the wild", "25", 25)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-92.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
