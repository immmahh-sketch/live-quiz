# Bank session 19 Oct 2026: 3 Play Your Cards Right games -> bank/cards-125.json (Cracker, Alan Partridge, Killing Eve).
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

game("the numbers of Cracker", "Television", "hard", ["Cracker", "TV drama", "ITV"], [
 ("Year it began", "1993", 1993), ("Series made", "3", 3), ("Year Robbie Coltrane was born", "1950", 1950),
 ("Year of the revival special, A New Terror", "2006", 2006), ("Year Jimmy McGovern, who created it, was born", "1949", 1949)])
game("the numbers of Alan Partridge", "Television", "medium", ["Alan Partridge", "sitcoms", "BBC"], [
 ("Year Steve Coogan was born", "1965", 1965), ("Year Knowing Me, Knowing You began", "1994", 1994), ("Year I'm Alan Partridge began", "1997", 1997),
 ("Year of the film Alpha Papa", "2013", 2013), ("Year This Time with Alan Partridge began", "2019", 2019)])
game("the numbers of Killing Eve", "Television", "medium", ["Killing Eve", "TV drama", "BBC"], [
 ("Year it began", "2018", 2018), ("Series made", "4", 4), ("Episodes made in all", "32", 32),
 ("Year Sandra Oh was born", "1971", 1971), ("Year Jodie Comer was born", "1993", 1993), ("Year the last series aired", "2022", 2022)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-125.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
