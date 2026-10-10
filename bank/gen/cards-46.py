# Bank session 10 Oct 2026: 8 more Play Your Cards Right games -> bank/cards-46.json. A row of 5-7 cards each:
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

game("the numbers of the Rolling Stones", "Music", "hard", ["Rolling Stones", "bands"], [
 ("Year they formed", "1962", 1962), ("UK number one singles", "8", 8), ("Year Mick Jagger was born", "1943", 1943),
 ("Years from their first single to 'Hackney Diamonds'", "60", 60), ("Year Charlie Watts died", "2021", 2021)])
game("the numbers of Queen", "Music", "medium", ["Queen", "bands"], [
 ("Year they formed", "1970", 1970), ("Members in the classic line-up", "4", 4), ("Year of their Live Aid set", "1985", 1985),
 ("Minutes they played at Live Aid, roughly", "21", 21), ("Length of 'Bohemian Rhapsody', in seconds", "355", 355)])
game("the numbers of a Premier League season", "Football", "easy", ["Premier League", "football"], [
 ("Clubs", "20", 20), ("Games each club plays", "38", 38), ("Points for a win", "3", 3),
 ("Matches in a whole season", "380", 380), ("Clubs relegated", "3", 3)])
game("the numbers of the 2026 World Cup", "Football", "medium", ["World Cup", "football"], [
 ("Teams taking part", "48", 48), ("Matches played", "104", 104), ("Host countries", "3", 3),
 ("Host cities", "16", 16), ("Year of the following World Cup", "2030", 2030)])
game("the numbers of Coronation Street", "TV", "hard", ["Coronation Street", "soaps"], [
 ("Year it began", "1960", 1960), ("Episodes shown each week these days", "3", 3), ("Episodes made, in thousands, roughly", "11", 11),
 ("Years William Roache had played Ken Barlow by 2025", "65", 65), ("Number of the Barlows' house on the Street", "1", 1)])
game("the numbers of Team GB at Paris 2024", "Olympics", "hard", ["Paris 2024", "Team GB"], [
 ("Gold medals", "14", 14), ("Medals altogether", "65", 65), ("Silver medals", "22", 22),
 ("Bronze medals", "29", 29), ("Sports at the Games", "32", 32)])
game("the numbers of a dartboard", "Sport", "medium", ["darts"], [
 ("Numbered segments", "20", 20), ("Points for the bullseye", "50", 50), ("Points for the outer bull", "25", 25),
 ("Most you can score with three darts", "180", 180), ("The highest possible checkout", "170", 170)])
game("the numbers of the Moon landings", "Space", "medium", ["Apollo", "Moon"], [
 ("Apollo missions that landed", "6", 6), ("Men who walked on the Moon", "12", 12), ("Year of the last landing", "1972", 1972),
 ("Kilograms of Moon rock brought home, roughly", "382", 382), ("Year of the first landing", "1969", 1969)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-46.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
