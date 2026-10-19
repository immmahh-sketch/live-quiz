# Bank session 19 Oct 2026: 3 Play Your Cards Right games -> bank/cards-124.json (Life on Mars, Fleabag, Spooks).
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

game("the numbers of Life on Mars", "Television", "medium", ["Life on Mars", "TV drama", "BBC"], [
 ("Year it began", "2006", 2006), ("Series made", "2", 2), ("Year Sam Tyler wakes up in", "1973", 1973),
 ("Episodes made in all", "16", 16), ("Year the sequel Ashes to Ashes began", "2008", 2008)])
game("the numbers of Fleabag", "Television", "medium", ["Fleabag", "TV drama", "BBC"], [
 ("Year it began", "2016", 2016), ("Series made", "2", 2), ("Episodes made in all", "12", 12),
 ("Year Phoebe Waller-Bridge was born", "1985", 1985), ("Year of the last episode", "2019", 2019)])
game("the numbers of Spooks", "Television", "hard", ["Spooks", "TV drama", "BBC"], [
 ("Year it began", "2002", 2002), ("Series made", "10", 10), ("Episodes made in all", "86", 86),
 ("Year Peter Firth, who plays Harry, was born", "1953", 1953), ("Year it ended", "2011", 2011)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-124.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
