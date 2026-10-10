# Bank session 10 Oct 2026: 8 more Play Your Cards Right games -> bank/cards-56.json (famous lives). A row of 5-7 cards each:
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

game("the numbers of Charlie Chaplin", "Film", "medium", ["Charlie Chaplin", "silent films"], [
 ("Year he was born, in London", "1889", 1889), ("Children he had", "11", 11), ("Year 'The Kid' came out", "1921", 1921),
 ("His age when he died", "88", 88), ("Year he died", "1977", 1977)])
game("the numbers of Walt Disney", "Film", "medium", ["Walt Disney", "Disney"], [
 ("Year he was born", "1901", 1901), ("Year Mickey Mouse first appeared", "1928", 1928), ("Competitive Oscars he won, a record", "22", 22),
 ("Year Disneyland opened", "1955", 1955), ("His age when he died", "65", 65), ("Year he died", "1966", 1966)])
game("the numbers of Alfred Hitchcock", "Film", "hard", ["Alfred Hitchcock", "directors"], [
 ("Year he was born, in London", "1899", 1899), ("Feature films he directed, roughly", "53", 53), ("Year 'Psycho' came out", "1960", 1960),
 ("Oscars he won for Best Director", "0", 0), ("Year he died", "1980", 1980)])
game("the numbers of J.K. Rowling", "Books", "medium", ["J.K. Rowling", "Harry Potter", "authors"], [
 ("Year she was born", "1965", 1965), ("Harry Potter books in the main series", "7", 7), ("Year the first one came out", "1997", 1997),
 ("Publishers who turned it down, it's said", "12", 12), ("Year the last one came out", "2007", 2007)])
game("the numbers of David Beckham", "Football", "medium", ["David Beckham", "England"], [
 ("Year he was born", "1975", 1975), ("His England caps", "115", 115), ("Year of his goal from the halfway line", "1996", 1996),
 ("His England goals", "17", 17), ("Year he left Manchester United for Real Madrid", "2003", 2003), ("His children", "4", 4)])
game("the numbers of Wayne Rooney", "Football", "medium", ["Wayne Rooney", "England"], [
 ("Year he was born", "1985", 1985), ("His Manchester United goals, a club record", "253", 253), ("Year he made his Everton debut", "2002", 2002),
 ("His England goals", "53", 53), ("His England caps", "120", 120)])
game("the numbers of Bobby Moore", "Football", "medium", ["Bobby Moore", "England", "1966"], [
 ("Year he was born", "1941", 1941), ("His England caps", "108", 108), ("Year he lifted the World Cup", "1966", 1966),
 ("Times he captained England", "90", 90), ("Year he died", "1993", 1993), ("His age when he died", "51", 51)])
game("the numbers of Kylie Minogue", "Music", "medium", ["Kylie Minogue", "pop stars"], [
 ("Year she was born", "1968", 1968), ("Year she joined 'Neighbours' as Charlene", "1986", 1986), ("Her UK number one singles", "7", 7),
 ("Year of her first UK number one", "1988", 1988), ("Year 'Can't Get You Out of My Head' came out", "2001", 2001)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-56.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
