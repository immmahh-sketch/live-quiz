# Bank session 11 Oct 2026: 9 more Play Your Cards Right games -> bank/cards-79.json (football legends and modern stars). A row of 5-7 cards each:
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

game("the numbers of Jack Charlton", "Football", "medium", ["Jack Charlton", "Leeds", "Ireland"], [
 ("Year he was born, in Ashington", "1935", 1935), ("His club-record appearances for Leeds", "773", 773), ("Year he won the World Cup", "1966", 1966),
 ("His England caps", "35", 35), ("Year he became Ireland manager", "1986", 1986)])
game("the numbers of Nobby Stiles", "Football", "medium", ["Nobby Stiles", "England", "1966"], [
 ("Year he was born", "1942", 1942), ("His England caps", "28", 28), ("Year he won the World Cup", "1966", 1966),
 ("Year he died", "2020", 2020), ("Year he won the European Cup with Manchester United", "1968", 1968)])
game("the numbers of Bob Paisley", "Football", "medium", ["Bob Paisley", "Liverpool", "managers"], [
 ("Year he was born", "1919", 1919), ("European Cups he won as manager", "3", 3), ("Year he became Liverpool manager", "1974", 1974),
 ("League titles he won as manager", "6", 6), ("Year he retired", "1983", 1983)])
game("the numbers of Ian Rush", "Football", "medium", ["Ian Rush", "Liverpool", "Wales"], [
 ("Year he was born", "1961", 1961), ("His club-record goals for Liverpool", "346", 346), ("Year he joined Liverpool", "1980", 1980),
 ("His goals for Wales", "28", 28), ("Year he joined Juventus", "1987", 1987)])
game("the numbers of Dennis Bergkamp", "Football", "medium", ["Dennis Bergkamp", "Arsenal", "Netherlands"], [
 ("Year he was born", "1969", 1969), ("Premier League titles he won", "3", 3), ("Year he joined Arsenal", "1995", 1995),
 ("His goals for the Netherlands", "37", 37), ("Year he retired", "2006", 2006)])
game("the numbers of Johan Cruyff", "Football", "medium", ["Johan Cruyff", "Netherlands", "Barcelona"], [
 ("Year he was born", "1947", 1947), ("Ballons d'Or he won", "3", 3), ("Year of his World Cup final", "1974", 1974),
 ("Year he died", "2016", 2016), ("Year he became Barcelona manager", "1988", 1988)])
game("the numbers of Franz Beckenbauer", "Football", "medium", ["Franz Beckenbauer", "Germany"], [
 ("Year he was born", "1945", 1945), ("His caps for West Germany", "103", 103), ("Year he won the World Cup as captain", "1974", 1974),
 ("Year he died", "2024", 2024), ("Year he won the World Cup as manager", "1990", 1990)])
game("the numbers of Jamie Vardy", "Football", "medium", ["Jamie Vardy", "Leicester City"], [
 ("Year he was born", "1987", 1987), ("Premier League games in a row he scored in", "11", 11), ("Year he joined Leicester", "2012", 2012),
 ("His England caps", "26", 26), ("Year Leicester won the league", "2016", 2016)])
game("the numbers of Jude Bellingham", "Football", "medium", ["Jude Bellingham", "England", "Real Madrid"], [
 ("Year he was born", "2003", 2003), ("The shirt number Birmingham retired for him", "22", 22), ("Year he joined Borussia Dortmund", "2020", 2020),
 ("Year of his overhead kick against Slovakia", "2024", 2024), ("Year he joined Real Madrid", "2023", 2023)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-79.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
