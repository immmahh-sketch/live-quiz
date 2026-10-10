# Bank session 10 Oct 2026: 8 more Play Your Cards Right games -> bank/cards-48.json. A row of 5-7 cards each:
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

game("the numbers of ABBA", "Music", "medium", ["ABBA", "bands"], [
 ("Year they won Eurovision", "1974", 1974), ("Members", "4", 4), ("UK number one singles", "9", 9),
 ("Year the 'Voyage' album came out", "2021", 2021), ("Year the 'Mamma Mia!' film came out", "2008", 2008)])
game("the numbers of Grey's Monument", "North East England", "hard", ["Newcastle", "landmarks", "North East"], [
 ("Year the monument was finished", "1838", 1838), ("Steps up to the top", "164", 164), ("Height in metres, roughly", "41", 41),
 ("Year of Earl Grey's Great Reform Act", "1832", 1832), ("Year Earl Grey became Prime Minister", "1830", 1830)])
game("the numbers of Michael Jackson", "Music", "medium", ["Michael Jackson", "singers"], [
 ("Year he was born", "1958", 1958), ("His age when he died", "50", 50), ("Year 'Thriller' came out", "1982", 1982),
 ("Members of the Jackson 5", "5", 5), ("Year he died", "2009", 2009)])
game("the numbers of the Sun", "Science", "medium", ["Sun", "space"], [
 ("Million miles from Earth, roughly", "93", 93), ("Minutes its light takes to reach us, roughly", "8", 8), ("Surface temperature in °C, roughly", "5,500", 5500),
 ("Earths that would fit across it, roughly", "109", 109), ("Planets that orbit it", "8", 8)])
game("the numbers of the Gateshead Millennium Bridge", "North East England", "hard", ["Gateshead", "bridges", "North East"], [
 ("Year it opened", "2001", 2001), ("Degrees it tilts to let ships through", "40", 40), ("Length in metres", "126", 126),
 ("Year it won the Stirling Prize", "2002", 2002), ("Bridges across the Tyne between Newcastle and Gateshead", "7", 7)])
game("the numbers of Magna Carta", "History", "hard", ["Magna Carta", "medieval"], [
 ("Year it was sealed", "1215", 1215), ("Clauses in the original", "63", 63), ("Surviving copies of the 1215 original", "4", 4),
 ("Barons chosen to enforce it", "25", 25), ("Year of its 800th anniversary", "2015", 2015)])
game("the numbers of the Gunpowder Plot", "History", "medium", ["Gunpowder Plot", "Bonfire Night"], [
 ("Year of the plot", "1605", 1605), ("Plotters in all", "13", 13), ("Barrels of gunpowder under Parliament", "36", 36),
 ("Day of November it was foiled", "5", 5), ("Year Guy Fawkes was executed", "1606", 1606)])
game("the numbers of the M25", "Britain", "medium", ["M25", "roads", "London"], [
 ("Miles round, roughly", "117", 117), ("Year it was finished", "1986", 1986), ("Highest junction number", "31", 31),
 ("Year Chris Rea sang 'The Road to Hell' about it", "1989", 1989), ("Speed limit, in mph", "70", 70)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-48.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
