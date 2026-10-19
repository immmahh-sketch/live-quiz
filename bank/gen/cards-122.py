# Bank session 19 Oct 2026: 3 Play Your Cards Right games -> bank/cards-122.json (Luther, Bodyguard, Poldark).
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

game("the numbers of Luther", "Television", "medium", ["Luther", "TV drama", "BBC"], [
 ("Year it began", "2010", 2010), ("TV series made", "5", 5), ("Year Idris Elba was born", "1972", 1972),
 ("Year the last TV series aired", "2019", 2019), ("Year of the Netflix film The Fallen Sun", "2023", 2023)])
game("the numbers of Bodyguard", "Television", "medium", ["Bodyguard", "TV drama", "BBC"], [
 ("Year it was shown", "2018", 2018), ("Episodes made", "6", 6), ("Year Richard Madden was born", "1986", 1986),
 ("Millions who watched the finale, roughly", "17", 17), ("Year Keeley Hawes was born", "1976", 1976)])
game("the numbers of Poldark", "Television", "hard", ["Poldark", "TV drama", "BBC"], [
 ("Year the first BBC series began", "1975", 1975), ("Poldark novels Winston Graham wrote", "12", 12), ("Year Winston Graham was born", "1908", 1908),
 ("Series in the 2015 remake", "5", 5), ("Year the remake began", "2015", 2015)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-122.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
