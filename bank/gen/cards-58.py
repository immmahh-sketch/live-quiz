# Bank session 10 Oct 2026: 9 more Play Your Cards Right games -> bank/cards-58.json (famous lives). A row of 5-7 cards each:
# what's on the card, what it shows when it flips, and the number compared. The numbers zig-zag, no equal neighbours.
# Titles must be new to the bank (the import skips a repeated title as a duplicate).
import json, os
G = []
def game(text, cat, diff, tags, cards):
    ns = [n for _, _, n in cards]
    assert 5 <= len(cards) <= 7, text
    assert all(ns[i] != ns[i - 1] for i in range(1, len(ns))), (text, 'equal neighbours')
    assert len({l for l, _, _ in cards}) == len(cards), (text, 'repeated card')
    G.append({"type": "cards", "text": "Play Your Cards Right: " + text, "category": cat, "tags": ["Play Your Cards Right"] + tags, "difficulty": diff,
              "cards": [{"label": l, "value": v, "n": n} for l, v, n in cards]})

game("the numbers of Barack Obama", "Politics", "medium", ["Barack Obama", "US presidents"], [
 ("Year he was born", "1961", 1961), ("His number as president", "44", 44), ("Year he was first elected", "2008", 2008),
 ("Years he was president", "8", 8), ("Year he won the Nobel Peace Prize", "2009", 2009), ("His daughters", "2", 2)])
game("the numbers of John F. Kennedy", "History", "medium", ["John F. Kennedy", "US presidents"], [
 ("Year he was born", "1917", 1917), ("His number as president", "35", 35), ("Year he was elected", "1960", 1960),
 ("His age when he took office", "43", 43), ("Days he spent in office", "1,036", 1036), ("Year he was shot", "1963", 1963)])
game("the numbers of Amy Johnson", "History", "hard", ["Amy Johnson", "aviation", "Hull"], [
 ("Year she was born, in Hull", "1903", 1903), ("Days her solo flight to Australia took", "19", 19), ("Year of that flight", "1930", 1930),
 ("Her age at the time", "26", 26), ("Year she died", "1941", 1941)])
game("the numbers of Captain Tom Moore", "History", "medium", ["Captain Tom", "NHS"], [
 ("Year he was born", "1920", 1920), ("Laps of his garden he set out to walk", "100", 100), ("Year of his walk", "2020", 2020),
 ("Millions of pounds he raised for NHS charities, roughly", "33", 33), ("Year he died", "2021", 2021)])
game("the numbers of Madonna", "Music", "medium", ["Madonna", "pop stars"], [
 ("Year she was born", "1958", 1958), ("Her UK number one singles", "13", 13), ("Year of her first UK number one", "1985", 1985),
 ("Her children", "6", 6), ("Year 'Ray of Light' came out", "1998", 1998)])
game("the numbers of Michael Jordan", "Sport", "medium", ["Michael Jordan", "basketball"], [
 ("Year he was born", "1963", 1963), ("NBA titles he won", "6", 6), ("His famous shirt number", "23", 23),
 ("Times he was named the league's most valuable player", "5", 5), ("Year he retired for good", "2003", 2003)])
game("the numbers of Tiger Woods", "Sport", "medium", ["Tiger Woods", "golf"], [
 ("Year he was born", "1975", 1975), ("Golf majors he's won", "15", 15), ("Year of his first major, the Masters", "1997", 1997),
 ("His age then", "21", 21), ("Times he's won the Masters", "5", 5), ("Year of his last Masters win", "2019", 2019)])
game("the numbers of Roger Federer", "Sport", "medium", ["Roger Federer", "tennis"], [
 ("Year he was born", "1981", 1981), ("Grand Slam singles titles he won", "20", 20), ("Year of his first Wimbledon title", "2003", 2003),
 ("Wimbledon singles titles he won", "8", 8), ("Year he retired", "2022", 2022)])
game("the numbers of Pelé", "Football", "medium", ["Pelé", "Brazil"], [
 ("Year he was born", "1940", 1940), ("World Cups he won", "3", 3), ("Year of his first World Cup win", "1958", 1958),
 ("His age then", "17", 17), ("Goals he's credited with in all games, roughly", "1,279", 1279), ("Year he died", "2022", 2022)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-58.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
