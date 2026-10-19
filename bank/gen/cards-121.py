# Bank session 19 Oct 2026: 3 Play Your Cards Right games -> bank/cards-121.json (Sherlock, Happy Valley, Call the Midwife).
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

game("the numbers of Sherlock", "Television", "medium", ["Sherlock", "TV drama", "BBC"], [
 ("Year it began", "2010", 2010), ("Series made", "4", 4), ("House number on Baker Street", "221", 221),
 ("Episodes made, counting the Victorian special", "13", 13), ("Year of the last episode", "2017", 2017)])
game("the numbers of Happy Valley", "Television", "medium", ["Happy Valley", "TV drama", "BBC"], [
 ("Year it began", "2014", 2014), ("Series made", "3", 3), ("Year Sarah Lancashire was born", "1964", 1964),
 ("Episodes in each series", "6", 6), ("Year the final series aired", "2023", 2023)])
game("the numbers of Call the Midwife", "Television", "hard", ["Call the Midwife", "TV drama", "BBC"], [
 ("Year it began", "2012", 2012), ("Year the first series is set", "1957", 1957), ("Year Jennifer Worth's memoir came out", "2002", 2002),
 ("Year Vanessa Redgrave, the narrator, was born", "1937", 1937), ("Year Miranda Hart, who played Chummy, was born", "1972", 1972)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-121.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
