# Bank session 11 Oct 2026: 9 more Play Your Cards Right games -> bank/cards-70.json (TV cooks and football legends). A row of 5-7 cards each:
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

game("the numbers of Jamie Oliver", "TV", "medium", ["Jamie Oliver", "TV cooks"], [
 ("Year he was born", "1975", 1975), ("His children", "5", 5), ("Year The Naked Chef began", "1999", 1999),
 ("Year of Jamie's School Dinners", "2005", 2005), ("Year Jamie's 30-Minute Meals began", "2010", 2010)])
game("the numbers of Mary Berry", "TV", "medium", ["Mary Berry", "Bake Off"], [
 ("Year she was born", "1935", 1935), ("Series of Bake Off she judged on the BBC", "7", 7), ("Year Bake Off began", "2010", 2010),
 ("Year she left Bake Off", "2016", 2016), ("Year she became a dame", "2021", 2021)])
game("the numbers of Delia Smith", "TV", "medium", ["Delia Smith", "TV cooks", "Norwich City"], [
 ("Year she was born", "1941", 1941), ("Year her Complete Cookery Course came out", "1978", 1978), ("Year she became a Norwich City owner", "1996", 1996),
 ("Year 'How to Cook' began", "1998", 1998), ("Year of her 'Let's be 'avin' you!' half-time rallying cry", "2005", 2005)])
game("the numbers of Jackie Milburn", "Football", "medium", ["Jackie Milburn", "Newcastle United"], [
 ("Year he was born", "1924", 1924), ("FA Cups he won with Newcastle", "3", 3), ("Year of his first FA Cup win", "1951", 1951),
 ("His Newcastle goals, roughly", "200", 200), ("Year he died", "1988", 1988)])
game("the numbers of Peter Beardsley", "Football", "medium", ["Peter Beardsley", "Newcastle United", "England"], [
 ("Year he was born", "1961", 1961), ("His England caps", "59", 59), ("Year he joined Liverpool", "1987", 1987),
 ("His England goals", "9", 9), ("Spells he had as a Newcastle player", "2", 2)])
game("the numbers of Niall Quinn", "Football", "medium", ["Niall Quinn", "Sunderland", "Ireland"], [
 ("Year he was born", "1966", 1966), ("His Republic of Ireland caps", "92", 92), ("Year he joined Sunderland", "1996", 1996),
 ("His Ireland goals", "21", 21), ("Year he became Sunderland chairman", "2006", 2006)])
game("the numbers of Kevin Phillips", "Football", "medium", ["Kevin Phillips", "Sunderland"], [
 ("Year he was born", "1973", 1973), ("His Premier League goals in 1999–2000", "30", 30), ("Year he joined Sunderland", "1997", 1997),
 ("His England caps", "8", 8), ("Year he won Europe's Golden Shoe", "2000", 2000)])
game("the numbers of Bobby Moore", "Football", "medium", ["Bobby Moore", "England", "West Ham"], [
 ("Year he was born", "1941", 1941), ("His England caps", "108", 108), ("Year he lifted the World Cup", "1966", 1966),
 ("Games he captained England in", "90", 90), ("Year he died", "1993", 1993)])
game("the numbers of Jimmy Greaves", "Football", "medium", ["Jimmy Greaves", "Tottenham", "England"], [
 ("Year he was born", "1940", 1940), ("His England goals", "44", 44), ("Year he joined Spurs", "1961", 1961),
 ("His Spurs goals, a club record", "266", 266), ("His England caps", "57", 57)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-70.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
