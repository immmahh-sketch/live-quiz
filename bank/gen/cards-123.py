# Bank session 19 Oct 2026: 3 Play Your Cards Right games -> bank/cards-123.json (Gavin & Stacey, Cold Feet, Line of Duty).
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

game("the numbers of Gavin & Stacey", "Television", "medium", ["Gavin & Stacey", "sitcoms", "BBC"], [
 ("Year it began", "2007", 2007), ("Series made", "3", 3), ("Year James Corden was born", "1978", 1978),
 ("Millions who watched the 2019 Christmas special, roughly", "18", 18), ("Year of the final episode", "2024", 2024)])
game("the numbers of Cold Feet", "Television", "hard", ["Cold Feet", "TV drama", "ITV"], [
 ("Year of the pilot", "1997", 1997), ("Couples at the heart of it", "3", 3), ("Year James Nesbitt was born", "1965", 1965),
 ("Series made in all", "9", 9), ("Year it came back", "2016", 2016)])
game("the numbers of Line of Duty", "Television", "medium", ["Line of Duty", "TV drama", "BBC"], [
 ("Year it began", "2012", 2012), ("The number in AC-12", "12", 12), ("Year Adrian Dunbar, who plays Ted Hastings, was born", "1958", 1958),
 ("Series made", "6", 6), ("Millions who watched the 2021 finale, roughly", "13", 13)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-123.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
