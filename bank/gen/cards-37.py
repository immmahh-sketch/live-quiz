# Bank session 10 Oct 2026: 8 more Play Your Cards Right games -> bank/cards-37.json. A row of 5-7 cards each:
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

game("the numbers of the Golden Gate Bridge", "Famous landmarks", "hard", ["Golden Gate Bridge", "San Francisco"], [
 ("Year it opened", "1937", 1937), ("Total length, in miles", "1.7", 1.7), ("Height of the towers, in metres", "227", 227),
 ("Main cables", "2", 2), ("Length of the main span, in metres", "1,280", 1280)])
game("the numbers of the Statue of Liberty", "Famous landmarks", "medium", ["Statue of Liberty", "New York"], [
 ("Rays on her crown", "7", 7), ("Windows in the crown", "25", 25), ("Steps up to the crown", "354", 354),
 ("Year she was unveiled", "1886", 1886), ("The year written on her tablet", "1776", 1776)])
game("the numbers of the Taj Mahal", "Famous landmarks", "hard", ["Taj Mahal", "India"], [
 ("Minarets", "4", 4), ("Years it took to build, roughly", "22", 22), ("Workers who built it, roughly", "20,000", 20000),
 ("Height in metres", "73", 73), ("Elephants said to have carried the materials", "1,000", 1000)])
game("the numbers of Mount Rushmore", "Famous landmarks", "medium", ["Mount Rushmore", "USA"], [
 ("Presidents' faces", "4", 4), ("Height of each face, in feet", "60", 60), ("Year it was finished", "1941", 1941),
 ("Workers who helped carve it, roughly", "400", 400), ("Years it took", "14", 14)])
game("the numbers of the Sydney Harbour Bridge", "Famous landmarks", "hard", ["Sydney Harbour Bridge", "Australia"], [
 ("Year it opened", "1932", 1932), ("Height above the water, in metres", "134", 134), ("Steps on the BridgeClimb", "1,332", 1332),
 ("Rivets, in millions", "6", 6), ("Road lanes", "8", 8)])
game("the numbers of the Forth Bridge", "Scotland", "hard", ["Forth Bridge", "railways"], [
 ("Year it opened", "1890", 1890), ("Length in miles, roughly", "1.5", 1.5), ("Giant cantilevers", "3", 3),
 ("Tonnes of steel", "54,000", 54000), ("Year it became a World Heritage Site", "2015", 2015)])
game("the numbers of the Burj Khalifa", "Famous landmarks", "medium", ["Burj Khalifa", "Dubai"], [
 ("Height in metres", "828", 828), ("Year it opened", "2010", 2010), ("Lifts", "57", 57),
 ("Floor of the highest viewing deck", "148", 148), ("How far you can see on a clear day, in km", "95", 95)])
game("the numbers of the Shard", "London", "medium", ["The Shard", "London"], [
 ("Height in metres", "310", 310), ("Storeys", "95", 95), ("Panes of glass, roughly", "11,000", 11000),
 ("Year it opened", "2012", 2012), ("Floor of the top viewing gallery", "72", 72)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-37.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
