# Bank session 10 Oct 2026: 8 more Play Your Cards Right games -> bank/cards-40.json. A row of 5-7 cards each:
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

game("the numbers of the Royal Albert Hall", "London", "hard", ["Royal Albert Hall", "London"], [
 ("Year it opened", "1871", 1871), ("Seats, roughly", "5,272", 5272), ("'Mushrooms' hanging from the ceiling", "85", 85),
 ("Pipes in its great organ", "9,999", 9999), ("Year the Proms moved there", "1941", 1941)])
game("the numbers of HMS Victory", "History", "hard", ["HMS Victory", "Nelson"], [
 ("Year she was launched", "1765", 1765), ("Guns", "104", 104), ("Crew at Trafalgar, roughly", "821", 821),
 ("Masts", "3", 3), ("Year of Trafalgar", "1805", 1805)])
game("the numbers of the Flying Scotsman", "Transport", "hard", ["Flying Scotsman", "railways"], [
 ("Year it was built", "1923", 1923), ("Top speed it officially hit in 1934, in mph", "100", 100), ("Its famous LNER engine number", "4472", 4472),
 ("Year of that 100 mph run", "1934", 1934), ("Miles from London to Edinburgh, roughly", "393", 393)])
game("the numbers of the Mona Lisa", "Art", "hard", ["Mona Lisa", "Leonardo da Vinci"], [
 ("Year Leonardo began it, roughly", "1503", 1503), ("Height in centimetres", "77", 77), ("Year it was stolen from the Louvre", "1911", 1911),
 ("Width in centimetres", "53", 53), ("Years it was missing", "2", 2)])
game("the numbers of Niagara Falls", "Famous landmarks", "hard", ["Niagara Falls", "waterfalls"], [
 ("Separate waterfalls", "3", 3), ("Height of the Horseshoe Falls, in metres, roughly", "51", 51), ("Year Annie Edson Taylor went over in a barrel", "1901", 1901),
 ("Her age when she did it", "63", 63), ("Year the first Maid of the Mist boat sailed", "1846", 1846)])
game("the numbers of the Kremlin", "Famous landmarks", "hard", ["Kremlin", "Moscow"], [
 ("Towers on its walls", "20", 20), ("Length of its walls, in metres", "2,235", 2235), ("Year the red brick walls were finished, roughly", "1495", 1495),
 ("Weight of the Tsar Bell, in tonnes, roughly", "200", 200), ("Year the Tsar Cannon was cast", "1586", 1586)])
game("the numbers of Notre-Dame de Paris", "Famous landmarks", "medium", ["Notre-Dame", "Paris"], [
 ("Year building began", "1163", 1163), ("Height of the towers, in metres", "69", 69), ("Year of the great fire", "2019", 2019),
 ("Steps up the towers", "387", 387), ("Year it reopened", "2024", 2024)])
game("the numbers of the Mayflower", "History", "medium", ["Mayflower", "Pilgrims"], [
 ("Year she sailed", "1620", 1620), ("Passengers", "102", 102), ("Days the crossing took", "66", 66),
 ("Year of the first Thanksgiving", "1621", 1621), ("Crew, roughly", "30", 30)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-40.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
