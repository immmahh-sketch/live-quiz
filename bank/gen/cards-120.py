# Bank session 19 Oct 2026: 3 Play Your Cards Right games -> bank/cards-120.json (Downton Abbey, Peaky Blinders, Crossroads).
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

game("the numbers of Downton Abbey", "Television", "medium", ["Downton Abbey", "TV drama", "ITV"], [
 ("Year it began", "2010", 2010), ("Series made", "6", 6), ("Year of the sinking that opens the first episode", "1912", 1912),
 ("Year the TV series ended", "2015", 2015), ("Year of the first film", "2019", 2019)])
game("the numbers of Peaky Blinders", "Television", "medium", ["Peaky Blinders", "TV drama", "BBC"], [
 ("Year it began", "2013", 2013), ("Year the first series is set", "1919", 1919), ("Series made", "6", 6),
 ("Year Cillian Murphy was born", "1976", 1976), ("Year the final series aired", "2022", 2022)])
game("the numbers of Crossroads", "Television", "hard", ["Crossroads", "soaps", "ITV"], [
 ("Year it began", "1964", 1964), ("Years Noele Gordon played Meg", "17", 17), ("Year Meg sailed away on the QE2", "1981", 1981),
 ("Year the original run ended", "1988", 1988), ("Year of the short-lived revival", "2001", 2001)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-120.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
