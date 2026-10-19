# Bank session 19 Oct 2026: 3 Play Your Cards Right games -> bank/cards-119.json (Doc Martin, Home and Away, Lundy).
# Probed against every cards game in the live bank first (none on these). Numbers are the commonly quoted ones.
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

game("the numbers of Doc Martin", "Television", "medium", ["Doc Martin", "TV drama", "ITV"], [
 ("Year it began", "2004", 2004), ("Series made", "10", 10), ("Year Martin Clunes was born", "1961", 1961),
 ("Year it ended", "2022", 2022), ("Year the film Saving Grace, where the doctor first appeared, came out", "2000", 2000)])
game("the numbers of Home and Away", "Television", "medium", ["Home and Away", "soaps", "Australia"], [
 ("Year it began", "1988", 1988), ("Years Kate Ritchie played Sally Fletcher", "20", 20), ("Year Isla Fisher joined as Shannon", "1994", 1994),
 ("Year Ray Meagher, who plays Alf, was born", "1944", 1944), ("Year Chris Hemsworth joined as Kim Hyde", "2004", 2004)])
game("the numbers of Lundy", "Geography", "hard", ["Lundy", "islands", "Devon"], [
 ("Length in miles, roughly", "3", 3), ("Year it issued its own 'puffin' coins", "1929", 1929), ("Miles off the north Devon coast, roughly", "12", 12),
 ("Year it became England's first Marine Conservation Zone", "2010", 2010), ("People who live there, roughly", "28", 28)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-119.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
