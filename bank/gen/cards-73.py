# Bank session 11 Oct 2026: 9 more Play Your Cards Right games -> bank/cards-73.json (football, boxing, snooker and athletics greats). A row of 5-7 cards each:
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

game("the numbers of Pelé", "Football", "medium", ["Pelé", "Brazil", "World Cup"], [
 ("Year he was born", "1940", 1940), ("World Cups he won", "3", 3), ("Year of his first World Cup win", "1958", 1958),
 ("His age at that first win", "17", 17), ("Year he died", "2022", 2022)])
game("the numbers of Diego Maradona", "Football", "medium", ["Diego Maradona", "Argentina", "World Cup"], [
 ("Year he was born", "1960", 1960), ("World Cups he won", "1", 1), ("Year he joined Napoli", "1984", 1984),
 ("Year he died", "2020", 2020), ("Year of the 'Hand of God' goal", "1986", 1986)])
game("the numbers of Mike Tyson", "Sport", "medium", ["Mike Tyson", "boxing"], [
 ("Year he was born", "1966", 1966), ("His age when he first became heavyweight champion", "20", 20), ("Year he first became champion", "1986", 1986),
 ("Year he fought Jake Paul", "2024", 2024), ("Year he bit Evander Holyfield's ear", "1997", 1997)])
game("the numbers of Frank Bruno", "Sport", "medium", ["Frank Bruno", "boxing"], [
 ("Year he was born", "1961", 1961), ("Times he fought Mike Tyson", "2", 2), ("Year of his first fight with Tyson", "1989", 1989),
 ("Year of his second fight with Tyson", "1996", 1996), ("Year he won the WBC heavyweight title", "1995", 1995)])
game("the numbers of Steve Davis", "Sport", "medium", ["Steve Davis", "snooker"], [
 ("Year he was born", "1957", 1957), ("His world titles", "6", 6), ("Year of his first world title", "1981", 1981),
 ("Year he retired", "2016", 2016), ("Year of his last world title", "1989", 1989)])
game("the numbers of Stephen Hendry", "Sport", "medium", ["Stephen Hendry", "snooker", "Scotland"], [
 ("Year he was born", "1969", 1969), ("His world titles", "7", 7), ("Year of his first world title", "1990", 1990),
 ("His age at that first title", "21", 21), ("Year he retired", "2012", 2012)])
game("the numbers of Jimmy White", "Sport", "medium", ["Jimmy White", "snooker"], [
 ("Year he was born", "1962", 1962), ("World finals he lost", "6", 6), ("Year of his first world final", "1984", 1984),
 ("His world titles", "0", 0), ("Year of his last world final", "1994", 1994)])
game("the numbers of Dame Kelly Holmes", "Sport", "medium", ["Kelly Holmes", "athletics", "Olympics"], [
 ("Year she was born", "1970", 1970), ("Olympic golds she won", "2", 2), ("Year she won them", "2004", 2004),
 ("Distance of the shorter of those races, in metres", "800", 800), ("Year she became a dame", "2005", 2005)])
game("the numbers of Daley Thompson", "Sport", "medium", ["Daley Thompson", "decathlon", "Olympics"], [
 ("Year he was born", "1958", 1958), ("Olympic decathlon golds", "2", 2), ("Year of his first Olympic gold", "1980", 1980),
 ("His 1984 world-record points total", "8,847", 8847), ("Year of his second Olympic gold", "1984", 1984)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-73.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
