# Bank session 18 Oct 2026: 2 Play Your Cards Right games -> bank/cards-90.json (the blue whale, the great white shark).
# Probed against every cards game in the live bank first. Numbers are the commonly quoted ones (up to / about).
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

game("the numbers of a blue whale", "Nature", "hard", ["whales", "sea life", "animals"], [
 ("Its length, in metres, at the biggest", "30", 30), ("Weight of its heart, in kilos", "180", 180), ("How long it can live, in years", "90", 90),
 ("Its weight, in tonnes, at the biggest", "200", 200), ("Litres of milk a calf drinks a day", "380", 380)])
game("the numbers of a great white shark", "Nature", "medium", ["sharks", "sea life", "animals"], [
 ("Its length, in metres, at the biggest", "6", 6), ("Teeth in its mouth, roughly", "300", 300), ("Its top speed in a burst, in mph", "25", 25),
 ("Year 'Jaws' came out", "1975", 1975), ("How long it can live, in years", "70", 70)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-90.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
