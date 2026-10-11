# Bank session 11 Oct 2026: 9 more Play Your Cards Right games -> bank/cards-69.json (modern pop and rock). A row of 5-7 cards each:
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

game("the numbers of Harry Styles", "Music", "medium", ["Harry Styles", "pop stars"], [
 ("Year he was born", "1994", 1994), ("His solo albums", "3", 3), ("Year One Direction formed", "2010", 2010),
 ("Weeks 'As It Was' spent at number one", "10", 10), ("Year 'As It Was' came out", "2022", 2022)])
game("the numbers of Lewis Capaldi", "Music", "medium", ["Lewis Capaldi", "singers", "Scotland"], [
 ("Year he was born", "1996", 1996), ("Weeks 'Someone You Loved' spent at number one", "7", 7), ("Year it reached number one", "2019", 2019),
 ("His studio albums, up to 2025", "2", 2), ("Year of his comeback at Glastonbury", "2025", 2025)])
game("the numbers of Stormzy", "Music", "medium", ["Stormzy", "grime"], [
 ("Year he was born", "1993", 1993), ("His studio albums", "3", 3), ("Year 'Gang Signs & Prayer' came out", "2017", 2017),
 ("His age when he headlined Glastonbury", "25", 25), ("Year he headlined Glastonbury", "2019", 2019)])
game("the numbers of Coldplay", "Music", "medium", ["Coldplay", "bands"], [
 ("Year they formed", "1996", 1996), ("Times they've headlined Glastonbury", "5", 5), ("Year 'Yellow' came out", "2000", 2000),
 ("Their studio albums, up to 2024", "10", 10), ("Year 'Moon Music' came out", "2024", 2024)])
game("the numbers of Arctic Monkeys", "Music", "medium", ["Arctic Monkeys", "bands", "Sheffield"], [
 ("Year they formed", "2002", 2002), ("Their studio albums", "7", 7), ("Year their record-breaking debut came out", "2006", 2006),
 ("Alex Turner's age at the time", "20", 20), ("Year 'The Car' came out", "2022", 2022)])
game("the numbers of One Direction", "Music", "medium", ["One Direction", "boy bands"], [
 ("Year they formed", "2010", 2010), ("Where they finished on The X Factor", "3rd", 3), ("Year Zayn left", "2015", 2015),
 ("Their studio albums", "5", 5), ("Year they went on hiatus", "2016", 2016)])
game("the numbers of Little Mix", "Music", "medium", ["Little Mix", "girl groups"], [
 ("Year they won The X Factor", "2011", 2011), ("Members at the start", "4", 4), ("Year Jesy Nelson left", "2020", 2020),
 ("Their studio albums", "6", 6), ("Their UK number one singles", "5", 5)])
game("the numbers of Sam Fender", "Music", "medium", ["Sam Fender", "North East"], [
 ("Year he was born", "1994", 1994), ("His studio albums, up to 2025", "3", 3), ("Year 'Seventeen Going Under' came out", "2021", 2021),
 ("Nights he played St James' Park in 2023", "2", 2), ("Year of those St James' Park gigs", "2023", 2023)])
game("the numbers of Dua Lipa", "Music", "medium", ["Dua Lipa", "pop stars"], [
 ("Year she was born", "1995", 1995), ("Her studio albums", "3", 3), ("Year 'New Rules' came out", "2017", 2017),
 ("Weeks 'One Kiss' spent at number one", "8", 8), ("Year she headlined Glastonbury", "2024", 2024)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-69.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
