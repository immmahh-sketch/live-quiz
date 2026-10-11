# Bank session 11 Oct 2026: 9 more Play Your Cards Right games -> bank/cards-75.json (boxing, athletics, swimming, cycling and racing greats). A row of 5-7 cards each:
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

game("the numbers of Anthony Joshua", "Sport", "medium", ["Anthony Joshua", "boxing"], [
 ("Year he was born", "1989", 1989), ("Year he won Olympic gold", "2012", 2012), ("Year he first became world champion", "2016", 2016),
 ("The Wembley crowd for his Klitschko fight", "90,000", 90000), ("Year he lost to Andy Ruiz Jr", "2019", 2019)])
game("the numbers of Ricky Hatton", "Sport", "medium", ["Ricky Hatton", "boxing", "Manchester"], [
 ("Year he was born", "1978", 1978), ("Professional fights he won", "45", 45), ("Year he beat Kostya Tszyu", "2005", 2005),
 ("Professional fights he lost", "3", 3), ("Year he fought Floyd Mayweather", "2007", 2007)])
game("the numbers of Linford Christie", "Sport", "medium", ["Linford Christie", "athletics", "Olympics"], [
 ("Year he was born", "1960", 1960), ("His age when he won Olympic 100 m gold", "32", 32), ("Year of that Olympic gold", "1992", 1992),
 ("His age when he moved from Jamaica to London", "7", 7), ("Year he became world 100 m champion", "1993", 1993)])
game("the numbers of Colin Jackson", "Sport", "medium", ["Colin Jackson", "hurdles", "Wales"], [
 ("Year he was born", "1967", 1967), ("World titles he won", "2", 2), ("Year he set the 110 m hurdles world record", "1993", 1993),
 ("That world record, in seconds", "12.91", 12.91), ("Year he was on Strictly", "2005", 2005)])
game("the numbers of Adam Peaty", "Sport", "medium", ["Adam Peaty", "swimming", "Olympics"], [
 ("Year he was born", "1994", 1994), ("Olympic golds he won in Rio and Tokyo", "3", 3), ("Year of his first Olympic gold", "2016", 2016),
 ("His 100 m breaststroke world record, in seconds", "56.88", 56.88), ("Year he was on Strictly", "2021", 2021)])
game("the numbers of Geraint Thomas", "Sport", "medium", ["Geraint Thomas", "cycling", "Wales"], [
 ("Year he was born", "1986", 1986), ("Olympic golds he won on the track", "2", 2), ("Year he won the Tour de France", "2018", 2018),
 ("Year of his first Olympic gold", "2008", 2008), ("Year of his second Olympic gold", "2012", 2012)])
game("the numbers of Sir Mark Cavendish", "Sport", "medium", ["Mark Cavendish", "cycling", "Isle of Man"], [
 ("Year he was born", "1985", 1985), ("His record Tour de France stage wins", "35", 35), ("Year he became world road race champion", "2011", 2011),
 ("Year he was knighted", "2024", 2024), ("Year he won Sports Personality of the Year", "2011", 2011)])
game("the numbers of Lester Piggott", "Sport", "medium", ["Lester Piggott", "horse racing"], [
 ("Year he was born", "1935", 1935), ("His Derby wins", "9", 9), ("Year of his first Derby win", "1954", 1954),
 ("His age at that first Derby win", "18", 18), ("Year he died", "2022", 2022)])
game("the numbers of Sir AP McCoy", "Sport", "medium", ["AP McCoy", "horse racing", "jump racing"], [
 ("Year he was born", "1974", 1974), ("Champion jockey titles in a row", "20", 20), ("Year he won the Grand National", "2010", 2010),
 ("Year he was knighted", "2016", 2016), ("Year he retired", "2015", 2015)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-75.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
