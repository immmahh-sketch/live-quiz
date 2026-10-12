# Bank session 12 Oct 2026: 5 more Play Your Cards Right games -> bank/cards-80.json (North East people and the Great North Run). A row of 5-7 cards each:
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

game("the numbers of the Great North Run", "Sport", "medium", ["Great North Run", "running", "North East"], [
 ("Year of the first Great North Run", "1981", 1981), ("Miles from Newcastle to South Shields", "13.1", 13.1), ("Year Mo Farah first won it", "2014", 2014),
 ("Mo Farah's wins in a row", "6", 6), ("Year its founder Brendan Foster was born", "1948", 1948)])
game("the numbers of Stan Laurel", "Film", "hard", ["Stan Laurel", "Laurel and Hardy", "comedy"], [
 ("Year he was born, in Ulverston", "1890", 1890), ("Films he made with Oliver Hardy", "107", 107), ("Year he first teamed up with Hardy", "1927", 1927),
 ("His age when he died", "74", 74), ("Year he got his honorary Oscar", "1961", 1961)])
game("the numbers of Rowan Atkinson", "TV", "medium", ["Rowan Atkinson", "Mr Bean", "Blackadder", "North East"], [
 ("Year he was born, in Consett", "1955", 1955), ("Series of Blackadder", "4", 4), ("Year Mr Bean was first shown", "1990", 1990),
 ("Johnny English films", "3", 3), ("Year the first Johnny English film came out", "2003", 2003)])
game("the numbers of Robert Stephenson", "History", "hard", ["Robert Stephenson", "railways", "North East"], [
 ("Year he was born, at Willington Quay", "1803", 1803), ("Year he became MP for Whitby", "1847", 1847), ("His age when he died", "55", 55),
 ("Year his High Level Bridge opened in Newcastle", "1849", 1849), ("Year he died", "1859", 1859)])
game("the numbers of Jimmy Nail", "Music", "medium", ["Jimmy Nail", "Auf Wiedersehen, Pet", "North East"], [
 ("Year he was born", "1954", 1954), ("Year Auf Wiedersehen, Pet began", "1983", 1983), ("Weeks Ain't No Doubt spent at number one", "3", 3),
 ("Year Spender began", "1991", 1991), ("Year Crocodile Shoes was first shown", "1994", 1994)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-80.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
