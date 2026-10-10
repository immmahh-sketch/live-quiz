# Bank session 11 Oct 2026: 9 more Play Your Cards Right games -> bank/cards-61.json (famous lives). A row of 5-7 cards each:
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

game("the numbers of Jessica Ennis-Hill", "Sport", "medium", ["Jessica Ennis-Hill", "athletics", "Olympics"], [
 ("Year she was born", "1986", 1986), ("Events in a heptathlon", "7", 7), ("Year she won Olympic gold", "2012", 2012),
 ("Points she scored that night", "6,955", 6955), ("Year she won Olympic silver in Rio", "2016", 2016)])
game("the numbers of Sir Bobby Charlton", "Football", "medium", ["Bobby Charlton", "England", "Manchester United"], [
 ("Year he was born", "1937", 1937), ("His England caps", "106", 106), ("Year of the Munich air crash he survived", "1958", 1958),
 ("His England goals", "49", 49), ("Year he won the World Cup", "1966", 1966), ("His Manchester United goals", "249", 249)])
game("the numbers of Sir David Attenborough", "TV", "medium", ["David Attenborough", "nature", "BBC"], [
 ("Year he was born", "1926", 1926), ("Year 'Life on Earth' was first shown", "1979", 1979), ("Year he joined the BBC", "1952", 1952),
 ("Year 'The Blue Planet' was first shown", "2001", 2001), ("Age he reached in May 2026", "100", 100)])
game("the numbers of Sir Alex Ferguson", "Football", "medium", ["Alex Ferguson", "Manchester United", "managers"], [
 ("Year he was born", "1941", 1941), ("Year he won a European trophy with Aberdeen", "1983", 1983), ("Year he took over at Manchester United", "1986", 1986),
 ("League titles he won with United", "13", 13), ("Year of United's treble", "1999", 1999), ("Champions Leagues he won", "2", 2), ("Year he retired", "2013", 2013)])
game("the numbers of Ronnie O'Sullivan", "Sport", "medium", ["Ronnie O'Sullivan", "snooker"], [
 ("Year he was born", "1975", 1975), ("His world titles", "7", 7), ("Year of his record-fast 147", "1997", 1997),
 ("Minutes that 147 took, just over", "5", 5), ("Year of his first world title", "2001", 2001), ("Official 147 breaks he's made", "15", 15)])
game("the numbers of Phil 'The Power' Taylor", "Sport", "medium", ["Phil Taylor", "darts"], [
 ("Year he was born", "1960", 1960), ("His world titles", "16", 16), ("Year of his first world title", "1990", 1990),
 ("Darts in a perfect nine-dart finish", "9", 9), ("Year he played his last World Championship final", "2018", 2018)])
game("the numbers of Jonny Wilkinson", "Sport", "medium", ["Jonny Wilkinson", "rugby", "England"], [
 ("Year he was born", "1979", 1979), ("His England caps", "91", 91), ("Year of his World Cup-winning drop goal", "2003", 2003),
 ("His England points", "1,179", 1179), ("Year he retired", "2014", 2014)])
game("the numbers of Sir Tom Jones", "Music", "medium", ["Tom Jones", "singers", "Wales"], [
 ("Year he was born", "1940", 1940), ("Year 'It's Not Unusual' went to number one", "1965", 1965), ("Year 'Delilah' came out", "1968", 1968),
 ("Year he was knighted", "2006", 2006), ("Year he became a coach on 'The Voice UK'", "2012", 2012)])
game("the numbers of Dolly Parton", "Music", "medium", ["Dolly Parton", "country music"], [
 ("Year she was born", "1946", 1946), ("Her place among her parents' children", "4th", 4), ("Children in the family", "12", 12),
 ("Year 'Jolene' came out", "1973", 1973), ("Year the film '9 to 5' came out", "1980", 1980), ("Year Dollywood opened", "1986", 1986)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-61.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
