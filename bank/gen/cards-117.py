# Bank session 19 Oct 2026: 3 Play Your Cards Right games -> bank/cards-117.json (TV detectives' first years, Inspector Morse,
# the slow worm). Probed against every cards game in the live bank first (no detective, Morse or slow worm games; the swallow and
# beaver already have games). Numbers are the commonly quoted ones.
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

game("the year each TV cop show began", "Television", "medium", ["detectives", "police", "TV drama"], [
 ("Z-Cars", "1962", 1962), ("Bergerac", "1981", 1981), ("The Sweeney", "1975", 1975), ("Taggart", "1983", 1983),
 ("A Touch of Frost", "1992", 1992), ("Inspector Morse", "1987", 1987), ("Midsomer Murders", "1997", 1997)])
game("the numbers of Inspector Morse", "Television", "hard", ["Inspector Morse", "detectives", "ITV"], [
 ("Episodes made with John Thaw", "33", 33), ("Year it began", "1987", 1987), ("Age John Thaw was when he died", "60", 60),
 ("Year Morse died on screen", "2000", 2000), ("Year John Thaw was born", "1942", 1942)])
game("the numbers of a slow worm", "Nature", "hard", ["slow worms", "reptiles", "British wildlife"], [
 ("Legs it has", "0", 0), ("Length in cm, roughly", "40", 40), ("Babies in a typical litter, roughly", "8", 8),
 ("Years it can live in the wild, up to roughly", "20", 20), ("Months a year it hibernates, roughly", "5", 5)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-117.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
