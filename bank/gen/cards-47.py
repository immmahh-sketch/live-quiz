# Bank session 10 Oct 2026: 9 more Play Your Cards Right games -> bank/cards-47.json. A row of 5-7 cards each:
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

game("the numbers of St James' Park", "Football", "medium", ["Newcastle United", "football", "North East"], [
 ("Year Newcastle United's story there began", "1892", 1892), ("Capacity, in thousands, roughly", "52", 52), ("Year Alan Shearer signed", "1996", 1996),
 ("Shearer's goals for Newcastle", "206", 206), ("The shirt number Shearer made famous", "9", 9)])
game("the numbers of Sunderland AFC", "Football", "medium", ["Sunderland", "football", "North East"], [
 ("Year the club was founded", "1879", 1879), ("Top-flight league titles won", "6", 6), ("Year they beat Leeds in the FA Cup final", "1973", 1973),
 ("Stadium of Light capacity, in thousands, roughly", "49", 49), ("Year the Stadium of Light opened", "1997", 1997)])
game("the numbers of Take That", "Music", "medium", ["Take That", "bands"], [
 ("Year they formed", "1990", 1990), ("Members in the original line-up", "5", 5), ("Year Robbie Williams left", "1995", 1995),
 ("Members today", "3", 3), ("Year they first split up", "1996", 1996)])
game("the numbers of the Battle of Hastings", "History", "medium", ["1066", "battles", "Normans"], [
 ("Year of the battle", "1066", 1066), ("Day of October it was fought", "14", 14), ("Length of the Bayeux Tapestry, in metres, roughly", "70", 70),
 ("Months Harold was king", "9", 9), ("Days after Harold's win at Stamford Bridge", "19", 19)])
game("the numbers of the Great Fire of London", "History", "hard", ["Great Fire of London", "London"], [
 ("Year it happened", "1666", 1666), ("Days it burned", "4", 4), ("Houses destroyed, roughly", "13,200", 13200),
 ("Parish churches destroyed", "87", 87), ("Height of the Monument, in feet", "202", 202)])
game("the numbers of the human heart", "Science", "easy", ["heart", "human body"], [
 ("Chambers", "4", 4), ("Typical resting beats a minute", "70", 70), ("Valves", "4", 4),
 ("Weight in grams, roughly", "300", 300), ("Litres of blood pumped a minute at rest, roughly", "5", 5)])
game("the numbers of Mars", "Science", "medium", ["Mars", "planets", "space"], [
 ("Moons", "2", 2), ("Earth days in a Martian year", "687", 687), ("Its place from the Sun", "4", 4),
 ("Height of Olympus Mons, in kilometres, roughly", "22", 22), ("Year the Perseverance rover landed", "2021", 2021)])
game("the numbers of Lego", "Toys and games", "hard", ["Lego", "toys"], [
 ("Year the modern brick was patented", "1958", 1958), ("Studs on a classic 2x4 brick", "8", 8), ("Year Legoland Windsor opened", "1996", 1996),
 ("Year the company was founded", "1932", 1932), ("Year the minifigure arrived", "1978", 1978)])
game("the numbers of Elvis Presley", "Music", "medium", ["Elvis Presley", "singers"], [
 ("Year he was born", "1935", 1935), ("His age when he died", "42", 42), ("Year he bought Graceland", "1957", 1957),
 ("UK number one singles", "21", 21), ("Year he died", "1977", 1977)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-47.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
