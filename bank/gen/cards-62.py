# Bank session 11 Oct 2026: 9 more Play Your Cards Right games -> bank/cards-62.json (famous lives). A row of 5-7 cards each:
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

game("the numbers of Gary Lineker", "Football", "medium", ["Gary Lineker", "England"], [
 ("Year he was born", "1960", 1960), ("His England goals", "48", 48), ("Year he won the World Cup Golden Boot", "1986", 1986),
 ("His goals at that World Cup", "6", 6), ("Year he began presenting Match of the Day", "1999", 1999), ("His England caps", "80", 80)])
game("the numbers of Sir Kenny Dalglish", "Football", "medium", ["Kenny Dalglish", "Liverpool", "Scotland"], [
 ("Year he was born", "1951", 1951), ("His Scotland caps", "102", 102), ("Year he joined Liverpool", "1977", 1977),
 ("His Scotland goals", "30", 30), ("Year he won the Premier League with Blackburn", "1995", 1995), ("European Cups he won as a player", "3", 3)])
game("the numbers of Sir Nick Faldo", "Sport", "medium", ["Nick Faldo", "golf"], [
 ("Year he was born", "1957", 1957), ("Majors he won", "6", 6), ("Year of his first major", "1987", 1987),
 ("Green jackets he won at the Masters", "3", 3), ("Year he captained Europe's Ryder Cup team", "2008", 2008)])
game("the numbers of Rafael Nadal", "Sport", "medium", ["Rafael Nadal", "tennis"], [
 ("Year he was born", "1986", 1986), ("French Open titles he won", "14", 14), ("Year of his first French Open title", "2005", 2005),
 ("His Grand Slam singles titles", "22", 22), ("Year he retired", "2024", 2024)])
game("the numbers of Robbie Williams", "Music", "medium", ["Robbie Williams", "Take That", "pop stars"], [
 ("Year he was born", "1974", 1974), ("Brit Awards he's won, Take That ones included", "18", 18), ("Year he left Take That", "1995", 1995),
 ("Thousands of fans at each of his Knebworth gigs", "125", 125), ("Year of those Knebworth gigs", "2003", 2003)])
game("the numbers of Sting", "Music", "medium", ["Sting", "The Police", "North East"], [
 ("Year he was born, in Wallsend", "1951", 1951), ("The Police's studio albums", "5", 5), ("Year The Police formed", "1977", 1977),
 ("Grammy Awards he's won, with The Police included", "17", 17), ("Year 'Every Breath You Take' came out", "1983", 1983)])
game("the numbers of L. S. Lowry", "Art", "hard", ["L. S. Lowry", "artists", "Salford"], [
 ("Year he was born", "1887", 1887), ("Honours he turned down, a record", "5", 5), ("His age when he retired as a rent collector", "65", 65),
 ("Year he died", "1976", 1976), ("Year The Lowry arts centre opened in Salford", "2000", 2000)])
game("the numbers of Freddie Flintoff", "Sport", "medium", ["Freddie Flintoff", "cricket", "England"], [
 ("Year he was born", "1977", 1977), ("His Test caps", "79", 79), ("Year of his famous Ashes summer", "2005", 2005),
 ("His Test wickets", "226", 226), ("Year he became a Top Gear presenter", "2019", 2019)])
game("the numbers of Dame Shirley Bassey", "Music", "medium", ["Shirley Bassey", "singers", "Wales"], [
 ("Year she was born", "1937", 1937), ("Bond themes she sang", "3", 3), ("Year 'Goldfinger' came out", "1964", 1964),
 ("Year she became a dame", "2000", 2000), ("Year she played Glastonbury", "2007", 2007)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-62.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
