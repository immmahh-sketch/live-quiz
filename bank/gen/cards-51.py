# Bank session 10 Oct 2026: 8 more Play Your Cards Right games -> bank/cards-51.json (famous lives). A row of 5-7 cards each:
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

game("the numbers of Princess Diana", "Royals", "medium", ["Princess Diana", "royals"], [
 ("Year she was born", "1961", 1961), ("Her age on her wedding day", "20", 20), ("Year of her wedding", "1981", 1981),
 ("Her sons", "2", 2), ("Her age when she died", "36", 36)])
game("the numbers of Nelson Mandela", "History", "medium", ["Nelson Mandela", "South Africa"], [
 ("Year he was born", "1918", 1918), ("Years he spent in prison", "27", 27), ("Year he became president", "1994", 1994),
 ("His age when he died", "95", 95), ("Year he won the Nobel Peace Prize", "1993", 1993)])
game("the numbers of Winston Churchill", "History", "medium", ["Winston Churchill", "Prime Ministers"], [
 ("Year he was born", "1874", 1874), ("Times he became Prime Minister", "2", 2), ("Year he first became Prime Minister", "1940", 1940),
 ("His age when he died", "90", 90), ("Year he won the Nobel Prize in Literature", "1953", 1953)])
game("the numbers of Queen Victoria", "Royals", "medium", ["Queen Victoria", "monarchs"], [
 ("Year she was born", "1819", 1819), ("Her age when she became queen", "18", 18), ("Her children", "9", 9),
 ("Years she reigned", "63", 63), ("Year she died", "1901", 1901)])
game("the numbers of Henry VIII", "History", "medium", ["Henry VIII", "Tudors"], [
 ("Year he was born", "1491", 1491), ("His age when he became king", "17", 17), ("His wives", "6", 6),
 ("Years on the throne, roughly", "38", 38), ("Year he died", "1547", 1547)])
game("the numbers of Neil Armstrong", "Space", "medium", ["Neil Armstrong", "Apollo 11", "space"], [
 ("Year he was born", "1930", 1930), ("Crew on Apollo 11", "3", 3), ("Year he walked on the Moon", "1969", 1969),
 ("Days the Apollo 11 mission lasted", "8", 8), ("His age when he died", "82", 82)])
game("the numbers of Captain James Cook", "History", "medium", ["Captain Cook", "explorers", "North East"], [
 ("Year he was born, in Marton near Middlesbrough", "1728", 1728), ("His great voyages of discovery", "3", 3), ("Year he landed at Botany Bay", "1770", 1770),
 ("His age when he was killed", "50", 50), ("Year he was killed, in Hawaii", "1779", 1779)])
game("the numbers of Freddie Mercury", "Music", "medium", ["Freddie Mercury", "Queen"], [
 ("Year he was born", "1946", 1946), ("Members of Queen", "4", 4), ("Year 'Bohemian Rhapsody' came out", "1975", 1975),
 ("His age when he died", "45", 45), ("Year he died", "1991", 1991)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-51.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
