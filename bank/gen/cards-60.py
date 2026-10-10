# Bank session 10 Oct 2026: 9 more Play Your Cards Right games -> bank/cards-60.json (famous lives). A row of 5-7 cards each:
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

game("the numbers of Beyoncé", "Music", "medium", ["Beyoncé", "pop stars"], [
 ("Year she was born", "1981", 1981), ("Grammy Awards she's won, up to 2025", "35", 35), ("Year of her first solo album", "2003", 2003),
 ("Her children", "3", 3), ("Year she won Album of the Year for 'Cowboy Carter'", "2025", 2025)])
game("the numbers of Elton John", "Music", "medium", ["Elton John", "pop stars"], [
 ("Year he was born", "1947", 1947), ("Year 'Your Song' came out", "1970", 1970), ("Millions of copies 'Candle in the Wind 1997' sold, roughly", "33", 33),
 ("Year that version came out", "1997", 1997), ("Year he completed his EGOT", "2024", 2024)])
game("the numbers of Rod Stewart", "Music", "medium", ["Rod Stewart", "pop stars"], [
 ("Year he was born", "1945", 1945), ("His children", "8", 8), ("Year 'Maggie May' went to number one", "1971", 1971),
 ("His UK number one singles", "6", 6), ("Year he was knighted", "2016", 2016)])
game("the numbers of Gareth Southgate", "Football", "medium", ["Gareth Southgate", "England"], [
 ("Year he was born", "1970", 1970), ("His England caps as a player", "57", 57), ("Year of his Euro 96 penalty miss", "1996", 1996),
 ("Euros finals he took England to", "2", 2), ("Year he became England manager", "2016", 2016), ("Games he took charge of", "102", 102)])
game("the numbers of Sir Steve Redgrave", "Sport", "medium", ["Steve Redgrave", "rowing", "Olympics"], [
 ("Year he was born", "1962", 1962), ("His Olympic gold medals", "5", 5), ("Year of his first Olympic gold", "1984", 1984),
 ("Year of his last Olympic gold", "2000", 2000), ("Year he was knighted", "2001", 2001)])
game("the numbers of Daley Thompson", "Sport", "medium", ["Daley Thompson", "decathlon", "Olympics"], [
 ("Year he was born", "1958", 1958), ("Olympic decathlon golds he won", "2", 2), ("Year of his first Olympic gold", "1980", 1980),
 ("Events in a decathlon", "10", 10), ("Year of his second Olympic gold", "1984", 1984)])
game("the numbers of Tom Daley", "Sport", "medium", ["Tom Daley", "diving", "Olympics"], [
 ("Year he was born", "1994", 1994), ("His age at his first Olympics", "14", 14), ("Year of those Olympics", "2008", 2008),
 ("His Olympic medals in all", "5", 5), ("Year he finally won Olympic gold", "2021", 2021)])
game("the numbers of Dame Kelly Holmes", "Sport", "medium", ["Kelly Holmes", "athletics", "Olympics"], [
 ("Year she was born", "1970", 1970), ("Olympic golds she won at one Games", "2", 2), ("Year of her Olympic double", "2004", 2004),
 ("Her age at the time", "34", 34), ("Year she became a dame", "2005", 2005)])
game("the numbers of Ian Botham", "Sport", "medium", ["Ian Botham", "cricket", "England"], [
 ("Year he was born", "1955", 1955), ("His Test wickets", "383", 383), ("Year of 'Botham's Ashes'", "1981", 1981),
 ("His Test caps", "102", 102), ("His Test runs, roughly", "5,200", 5200)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-60.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
