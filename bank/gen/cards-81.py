# Bank session 12 Oct 2026: 4 more Play Your Cards Right games -> bank/cards-81.json (Jordan Henderson, Steve Cram, the Mauretania, Jill Scott). A row of 5-7 cards each:
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

game("the numbers of Jordan Henderson", "Football", "medium", ["Jordan Henderson", "Sunderland", "Liverpool", "North East"], [
 ("Year he was born, in Sunderland", "1990", 1990), ("His Liverpool shirt number", "14", 14), ("Year he lifted the Champions League", "2019", 2019),
 ("Year he made his Sunderland debut", "2008", 2008), ("Year he lifted the Premier League", "2020", 2020)])
game("the numbers of Steve Cram", "Sport", "medium", ["Steve Cram", "athletics", "North East"], [
 ("Year he was born, in Gateshead", "1960", 1960), ("Olympic medals he won", "1", 1), ("Year he became world 1500 m champion", "1983", 1983),
 ("His age when he won that world title", "22", 22), ("Year he set the world mile record", "1985", 1985)])
game("the numbers of the Mauretania", "History", "hard", ["Mauretania", "shipbuilding", "Tyne", "North East"], [
 ("Year she was launched at Wallsend", "1906", 1906), ("Her funnels", "4", 4), ("Year of her maiden voyage", "1907", 1907),
 ("Her famous speed, in knots", "26", 26), ("Year she was scrapped", "1935", 1935)])
game("the numbers of Jill Scott", "Football", "medium", ["Jill Scott", "Lionesses", "North East"], [
 ("Year she was born, in Sunderland", "1987", 1987), ("Her England caps", "161", 161), ("Year she played for Team GB at the London Olympics", "2012", 2012),
 ("Women's World Cups she played in", "3", 3), ("Year England won the Euros", "2022", 2022)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-81.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
