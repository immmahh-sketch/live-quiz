# Bank session 11 Oct 2026: 9 more Play Your Cards Right games -> bank/cards-64.json (sport stars and screen favourites). A row of 5-7 cards each:
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

game("the numbers of Michael Phelps", "Sport", "medium", ["Michael Phelps", "swimming", "Olympics"], [
 ("Year he was born", "1985", 1985), ("His Olympic golds", "23", 23), ("Year of his first Olympics", "2000", 2000),
 ("Golds he won at one Games, a record", "8", 8), ("Year of that Games", "2008", 2008), ("His Olympic medals in all", "28", 28)])
game("the numbers of Novak Djokovic", "Sport", "medium", ["Novak Djokovic", "tennis"], [
 ("Year he was born", "1987", 1987), ("His Grand Slam singles titles", "24", 24), ("Year of his first Grand Slam title", "2008", 2008),
 ("His Wimbledon singles titles", "7", 7), ("Year he finally won Olympic gold", "2024", 2024)])
game("the numbers of Rory McIlroy", "Sport", "medium", ["Rory McIlroy", "golf"], [
 ("Year he was born", "1989", 1989), ("His age when he won his first major", "22", 22), ("Year of that first major", "2011", 2011),
 ("Majors he's won, up to 2025", "5", 5), ("Year he won the Masters to complete the career Grand Slam", "2025", 2025)])
game("the numbers of Luke Littler", "Sport", "medium", ["Luke Littler", "darts"], [
 ("Year he was born", "2007", 2007), ("His age at his first World Championship final", "16", 16), ("Year of that final", "2024", 2024),
 ("His age when he became world champion", "17", 17), ("Year he became world champion", "2025", 2025)])
game("the numbers of Paula Radcliffe", "Sport", "medium", ["Paula Radcliffe", "marathon", "athletics"], [
 ("Year she was born", "1973", 1973), ("London Marathons she won", "3", 3), ("Year she set her marathon world record", "2003", 2003),
 ("Minutes over two hours that record took", "15", 15), ("Year she retired", "2015", 2015)])
game("the numbers of Steven Gerrard", "Football", "medium", ["Steven Gerrard", "Liverpool", "England"], [
 ("Year he was born", "1980", 1980), ("His England caps", "114", 114), ("Year of Liverpool's Istanbul comeback", "2005", 2005),
 ("His Liverpool goals", "186", 186), ("His Liverpool appearances", "710", 710)])
game("the numbers of Frank Lampard", "Football", "medium", ["Frank Lampard", "Chelsea", "England"], [
 ("Year he was born", "1978", 1978), ("His Chelsea goals, a club record", "211", 211), ("Year he joined Chelsea", "2001", 2001),
 ("His England caps", "106", 106), ("Premier League titles he won", "3", 3)])
game("the numbers of Wallace and Gromit", "Film", "medium", ["Wallace and Gromit", "Aardman"], [
 ("Year 'A Grand Day Out' first aired", "1989", 1989), ("Oscars Nick Park has won", "4", 4), ("Year 'The Wrong Trousers' first aired", "1993", 1993),
 ("Year 'The Curse of the Were-Rabbit' came out", "2005", 2005), ("Year 'Vengeance Most Fowl' first aired", "2024", 2024)])
game("the numbers of Mr Bean", "TV", "medium", ["Mr Bean", "Rowan Atkinson", "comedy"], [
 ("Year Rowan Atkinson was born", "1955", 1955), ("Year Mr Bean first aired", "1990", 1990), ("Year 'Bean' the film came out", "1997", 1997),
 ("Year 'Mr Bean's Holiday' came out", "2007", 2007), ("Year he played 'Chariots of Fire' at the Olympic opening ceremony", "2012", 2012)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-64.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
