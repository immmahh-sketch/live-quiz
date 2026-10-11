# Bank session 11 Oct 2026: 9 more Play Your Cards Right games -> bank/cards-74.json (Man Utd, boxing, snooker, skating and Seb Coe). A row of 5-7 cards each:
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

game("the numbers of Ryan Giggs", "Football", "medium", ["Ryan Giggs", "Manchester United", "Wales"], [
 ("Year he was born", "1973", 1973), ("League titles he won with Manchester United", "13", 13), ("Year of his United debut", "1991", 1991),
 ("His club-record United appearances", "963", 963), ("Year he became Wales manager", "2018", 2018)])
game("the numbers of Eric Cantona", "Football", "medium", ["Eric Cantona", "Manchester United", "France"], [
 ("Year he was born", "1966", 1966), ("Premier League titles he won with United", "4", 4), ("Year of his kung-fu kick at Selhurst Park", "1995", 1995),
 ("Year he joined Manchester United", "1992", 1992), ("Year he retired from football", "1997", 1997)])
game("the numbers of Tyson Fury", "Sport", "medium", ["Tyson Fury", "boxing"], [
 ("Year he was born", "1988", 1988), ("Times he fought Deontay Wilder", "3", 3), ("Year he beat Wladimir Klitschko", "2015", 2015),
 ("His height in centimetres", "206", 206), ("Year he first fought Oleksandr Usyk", "2024", 2024)])
game("the numbers of Lennox Lewis", "Sport", "medium", ["Lennox Lewis", "boxing"], [
 ("Year he was born", "1965", 1965), ("Professional fights he lost", "2", 2), ("Year he won Olympic gold, for Canada", "1988", 1988),
 ("Year he retired", "2003", 2003), ("Year he beat Mike Tyson", "2002", 2002)])
game("the numbers of Joe Calzaghe", "Sport", "medium", ["Joe Calzaghe", "boxing", "Wales"], [
 ("Year he was born", "1972", 1972), ("Professional fights he won", "46", 46), ("Year he won Sports Personality of the Year", "2007", 2007),
 ("Professional fights he lost", "0", 0), ("Year he retired, unbeaten", "2008", 2008)])
game("the numbers of Dennis Taylor", "Sport", "medium", ["Dennis Taylor", "snooker", "Northern Ireland"], [
 ("Year he was born", "1949", 1949), ("Frames he won in the 1985 world final", "18", 18), ("Year of that black-ball final", "1985", 1985),
 ("Frames Steve Davis won in it", "17", 17), ("Year he left the professional tour", "2000", 2000)])
game("the numbers of Alex Higgins", "Sport", "medium", ["Alex Higgins", "snooker", "Northern Ireland"], [
 ("Year he was born", "1949", 1949), ("World titles he won", "2", 2), ("Year of his first world title", "1972", 1972),
 ("Year he died", "2010", 2010), ("Year of his second world title", "1982", 1982)])
game("the numbers of Torvill and Dean", "Sport", "medium", ["Torvill and Dean", "ice dance", "Olympics"], [
 ("Year Jayne Torvill was born", "1957", 1957), ("Perfect sixes for Boléro at Sarajevo", "12", 12), ("Year they won Olympic gold", "1984", 1984),
 ("Year Dancing on Ice began", "2006", 2006), ("Year of their Olympic bronze", "1994", 1994)])
game("the numbers of Lord Coe", "Sport", "medium", ["Seb Coe", "athletics", "Olympics"], [
 ("Year he was born", "1956", 1956), ("Olympic 1500 m golds he won", "2", 2), ("Year of his first Olympic 1500 m gold", "1980", 1980),
 ("Year he became head of world athletics", "2015", 2015), ("Year of his second Olympic 1500 m gold", "1984", 1984)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-74.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
