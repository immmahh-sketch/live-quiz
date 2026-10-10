# Bank session 10 Oct 2026: 8 more Play Your Cards Right games -> bank/cards-55.json (famous lives). A row of 5-7 cards each:
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

game("the numbers of John Lennon", "Music", "medium", ["John Lennon", "The Beatles"], [
 ("Year he was born", "1940", 1940), ("His sons", "2", 2), ("Year 'Imagine' came out", "1971", 1971),
 ("His age when he was killed", "40", 40), ("Year he died", "1980", 1980)])
game("the numbers of Paul McCartney", "Music", "medium", ["Paul McCartney", "The Beatles"], [
 ("Year he was born", "1942", 1942), ("The Beatles' UK number ones", "17", 17), ("Year 'Love Me Do' came out", "1962", 1962),
 ("Year he formed Wings", "1971", 1971), ("Year he was knighted", "1997", 1997)])
game("the numbers of Bob Marley", "Music", "medium", ["Bob Marley", "reggae"], [
 ("Year he was born", "1945", 1945), ("Children he officially acknowledged", "11", 11), ("Year the album 'Exodus' came out", "1977", 1977),
 ("His age when he died", "36", 36), ("Year he died", "1981", 1981)])
game("the numbers of Marilyn Monroe", "Film", "medium", ["Marilyn Monroe", "film stars"], [
 ("Year she was born", "1926", 1926), ("Times she married", "3", 3), ("Year of 'Gentlemen Prefer Blondes'", "1953", 1953),
 ("Her age when she died", "36", 36), ("Year she died", "1962", 1962)])
game("the numbers of Amelia Earhart", "History", "hard", ["Amelia Earhart", "aviation"], [
 ("Year she was born", "1897", 1897), ("Hours her solo Atlantic flight took, roughly", "15", 15), ("Year of that flight", "1932", 1932),
 ("Her age when she vanished", "39", 39), ("Year she vanished over the Pacific", "1937", 1937)])
game("the numbers of Margaret Thatcher", "Politics", "medium", ["Margaret Thatcher", "Prime Ministers"], [
 ("Year she was born", "1925", 1925), ("General elections she won", "3", 3), ("Year she became Prime Minister", "1979", 1979),
 ("Years she was Prime Minister", "11", 11), ("Year she resigned", "1990", 1990), ("Her age when she died", "87", 87)])
game("the numbers of Sir Chris Hoy", "Sport", "medium", ["Chris Hoy", "cycling", "Olympics"], [
 ("Year he was born", "1976", 1976), ("His Olympic gold medals", "6", 6), ("Year he won three golds at one Games", "2008", 2008),
 ("His Olympic medals in all", "7", 7), ("Year he retired", "2013", 2013)])
game("the numbers of Sir Bradley Wiggins", "Sport", "medium", ["Bradley Wiggins", "cycling", "Olympics"], [
 ("Year he was born", "1980", 1980), ("His Olympic gold medals", "5", 5), ("Year he won the Tour de France", "2012", 2012),
 ("His Olympic medals in all", "8", 8), ("Year of his last Olympic gold", "2016", 2016)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-55.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
