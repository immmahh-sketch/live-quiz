# Bank session 12 Oct 2026: 2 more Play Your Cards Right games -> bank/cards-84.json (the Scouts, Girlguiding). A row of 5-7 cards each:
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

game("the numbers of the Scouts", "Everyday life", "medium", ["Scouts", "Baden-Powell"], [
 ("Year of the first camp on Brownsea Island", "1907", 1907), ("Baden-Powell's age at that camp", "50", 50), ("Year Beavers began in the UK", "1986", 1986),
 ("Fingers held up in the Scout salute", "3", 3), ("Year girls could join every section", "2007", 2007)])
game("the numbers of Girlguiding", "Everyday life", "medium", ["Girl Guides", "Brownies", "Girlguiding"], [
 ("Year Guiding began", "1910", 1910), ("February date of Thinking Day", "22", 22), ("Year Rainbows began", "1987", 1987),
 ("Leaves on the trefoil badge", "3", 3), ("Year Brownies began", "1914", 1914)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-84.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
