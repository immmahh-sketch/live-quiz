# Bank session 10 Oct 2026: 8 more Play Your Cards Right games -> bank/cards-38.json. A row of 5-7 cards each:
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

game("the numbers of the Tower of London", "London", "hard", ["Tower of London", "London"], [
 ("Year the White Tower was begun, roughly", "1078", 1078), ("Ravens that must be kept there, by legend", "6", 6), ("Gems in the Crown Jewels, roughly", "23,578", 23578),
 ("Year Anne Boleyn was beheaded there", "1536", 1536), ("Height of the White Tower, in metres, roughly", "27", 27)])
game("the numbers of Tower Bridge", "London", "medium", ["Tower Bridge", "London"], [
 ("Year it opened", "1894", 1894), ("Height of the towers, in metres", "65", 65), ("Years it took to build", "8", 8),
 ("Total length, in metres", "244", 244), ("Bascules (the halves that lift)", "2", 2)])
game("the numbers of the Empire State Building", "Famous landmarks", "medium", ["Empire State Building", "New York"], [
 ("Year it opened", "1931", 1931), ("Floors", "102", 102), ("Lifts", "73", 73),
 ("Height to the tip, in metres", "443", 443), ("Steps up to the 86th floor", "1,576", 1576)])
game("the numbers of the Great Wall of China", "Famous landmarks", "hard", ["Great Wall of China", "China"], [
 ("Length of all its sections, in km (2012 survey)", "21,196", 21196), ("Year it became a World Heritage Site", "1987", 1987), ("Usual height of the Ming wall, in metres", "7", 7),
 ("Length of the Ming Dynasty wall, in km, roughly", "8,850", 8850), ("Year BC the first emperor began joining up the walls, roughly", "221", 221)])
game("the numbers of the Leaning Tower of Pisa", "Famous landmarks", "hard", ["Leaning Tower of Pisa", "Italy"], [
 ("Year building began", "1173", 1173), ("Height in metres, roughly", "56", 56), ("Bells in the belfry", "7", 7),
 ("Steps to the top, roughly", "294", 294), ("Degrees it leans today, roughly", "4", 4)])
game("the numbers of the Sagrada Família", "Famous landmarks", "hard", ["Sagrada Familia", "Barcelona"], [
 ("Year building began", "1882", 1882), ("Towers once it's finished", "18", 18), ("Year Gaudí died", "1926", 1926),
 ("Height of the tallest tower, in metres", "172.5", 172.5), ("Façades", "3", 3)])
game("the numbers of Westminster Abbey", "London", "hard", ["Westminster Abbey", "royals"], [
 ("Coronations held there since 1066", "40", 40), ("Year Henry III began the church you see today", "1245", 1245), ("Year of the last coronation there", "2023", 2023),
 ("Royal weddings held there, up to 2025", "16", 16), ("Year Chaucer was buried, starting Poets' Corner", "1400", 1400)])
game("the numbers of St Paul's Cathedral", "London", "medium", ["St Paul's Cathedral", "London"], [
 ("Year Old St Paul's burned in the Great Fire", "1666", 1666), ("Steps to the Golden Gallery", "528", 528), ("Height in metres", "111", 111),
 ("Year Wren's cathedral was declared finished", "1711", 1711), ("Steps to the Whispering Gallery", "257", 257)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-38.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
