# Bank session 12 Oct 2026: 4 more Play Your Cards Right games -> bank/cards-82.json (Stadium of Light, the Metro, Lucy Bronze, Vera). A row of 5-7 cards each:
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

game("the numbers of the Stadium of Light", "Football", "medium", ["Stadium of Light", "Sunderland", "North East"], [
 ("Year it opened", "1997", 1997), ("Sunderland's record points total, in 1998–99", "105", 105), ("Its capacity, roughly", "49,000", 49000),
 ("Year their old ground Roker Park opened", "1898", 1898), ("Year England first played there", "1999", 1999)])
game("the numbers of the Tyne and Wear Metro", "The North East of England", "medium", ["Metro", "Tyne and Wear", "transport"], [
 ("Year it first opened", "1980", 1980), ("Stations on the network", "60", 60), ("Year it reached Sunderland", "2002", 2002),
 ("Lines on the map", "2", 2), ("Year it reached Newcastle Airport", "1991", 1991)])
game("the numbers of Lucy Bronze", "Football", "medium", ["Lucy Bronze", "Lionesses", "North East"], [
 ("Year she was born, in Berwick", "1991", 1991), ("Women's Champions League titles she has won", "5", 5), ("Year she won the Euros with England", "2022", 2022),
 ("Clubs she won the Champions League with", "2", 2), ("Year she was named FIFA's best women's player", "2020", 2020)])
game("the numbers of Vera", "TV", "medium", ["Vera", "Brenda Blethyn", "North East"], [
 ("Year Vera began on ITV", "2011", 2011), ("Series it ran for", "14", 14), ("Year Brenda Blethyn was born", "1946", 1946),
 ("Oscar nominations Brenda Blethyn has had", "2", 2), ("Year Ann Cleeves published the first Vera novel", "1999", 1999)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-82.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
