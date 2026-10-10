# Bank session 10 Oct 2026: 9 more Play Your Cards Right games -> bank/cards-59.json (famous lives). A row of 5-7 cards each:
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

game("the numbers of Taylor Swift", "Music", "medium", ["Taylor Swift", "pop stars"], [
 ("Year she was born", "1989", 1989), ("Studio albums of new songs, up to 2025", "12", 12), ("Year her first album came out", "2006", 2006),
 ("Shows on the Eras Tour", "149", 149), ("Times she's won the Grammy for Album of the Year", "4", 4)])
game("the numbers of Adele", "Music", "medium", ["Adele", "pop stars"], [
 ("Year she was born", "1988", 1988), ("Her studio albums", "4", 4), ("Year '21' came out", "2011", 2011),
 ("Grammy Awards she's won", "16", 16), ("Year she won an Oscar for 'Skyfall'", "2013", 2013)])
game("the numbers of Lewis Hamilton", "Sport", "medium", ["Lewis Hamilton", "Formula One"], [
 ("Year he was born", "1985", 1985), ("His world championships", "7", 7), ("Year of his first title", "2008", 2008),
 ("Grand Prix races he's won", "105", 105), ("Year he joined Ferrari", "2025", 2025)])
game("the numbers of Andy Murray", "Sport", "medium", ["Andy Murray", "tennis"], [
 ("Year he was born", "1987", 1987), ("Grand Slam singles titles he won", "3", 3), ("Year of his first Wimbledon title", "2013", 2013),
 ("Olympic singles golds he won", "2", 2), ("Year he retired", "2024", 2024)])
game("the numbers of Harry Kane", "Football", "medium", ["Harry Kane", "England", "Tottenham"], [
 ("Year he was born", "1993", 1993), ("His Premier League goals for Spurs", "213", 213), ("Year he won the World Cup Golden Boot", "2018", 2018),
 ("Premier League Golden Boots he won", "3", 3), ("Year he joined Bayern Munich", "2023", 2023)])
game("the numbers of Steve Jobs", "Science", "medium", ["Steve Jobs", "Apple"], [
 ("Year he was born", "1955", 1955), ("Year he co-founded Apple", "1976", 1976), ("His age when he died", "56", 56),
 ("Year he launched the iPhone", "2007", 2007), ("Year he died", "2011", 2011)])
game("the numbers of Ed Sheeran", "Music", "medium", ["Ed Sheeran", "pop stars"], [
 ("Year he was born", "1991", 1991), ("His main studio albums, up to 2025", "6", 6), ("Year '+' came out", "2011", 2011),
 ("Weeks 'Shape of You' spent at number one", "14", 14), ("Year 'Shape of You' came out", "2017", 2017)])
game("the numbers of Prince Philip", "History", "medium", ["Prince Philip", "royal family"], [
 ("Year he was born", "1921", 1921), ("His children", "4", 4), ("Year he married Princess Elizabeth", "1947", 1947),
 ("Years they were married", "73", 73), ("Year he died", "2021", 2021), ("His age when he died", "99", 99)])
game("the numbers of Bill Gates", "Science", "medium", ["Bill Gates", "Microsoft"], [
 ("Year he was born", "1955", 1955), ("His age when he co-founded Microsoft", "19", 19), ("Year he co-founded it", "1975", 1975),
 ("Year Windows first came out", "1985", 1985), ("Year he stepped down as boss", "2000", 2000)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-59.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
