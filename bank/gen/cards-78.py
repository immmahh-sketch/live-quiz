# Bank session 11 Oct 2026: 9 more Play Your Cards Right games -> bank/cards-78.json (1966 heroes and great managers). A row of 5-7 cards each:
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

game("the numbers of Sir Geoff Hurst", "Football", "medium", ["Geoff Hurst", "England", "1966"], [
 ("Year he was born", "1941", 1941), ("Goals he scored in the 1966 final", "3", 3), ("Year of that World Cup final", "1966", 1966),
 ("His England caps", "49", 49), ("Year he was knighted", "1998", 1998)])
game("the numbers of Gordon Banks", "Football", "medium", ["Gordon Banks", "England", "goalkeepers"], [
 ("Year he was born", "1937", 1937), ("His England caps", "73", 73), ("Year of his famous save from Pelé", "1970", 1970),
 ("Year he died", "2019", 2019), ("Year he lost the sight of an eye in a car crash", "1972", 1972)])
game("the numbers of Sir Alf Ramsey", "Football", "medium", ["Alf Ramsey", "England", "managers"], [
 ("Year he was born", "1920", 1920), ("His England caps as a player", "32", 32), ("Year he won the World Cup as manager", "1966", 1966),
 ("Year he became England manager", "1963", 1963), ("Year he was sacked", "1974", 1974)])
game("the numbers of Bill Shankly", "Football", "medium", ["Bill Shankly", "Liverpool", "managers"], [
 ("Year he was born", "1913", 1913), ("League titles he won with Liverpool", "3", 3), ("Year he took over at Liverpool", "1959", 1959),
 ("Year he died", "1981", 1981), ("Year he retired", "1974", 1974)])
game("the numbers of Arsène Wenger", "Football", "medium", ["Arsène Wenger", "Arsenal", "managers"], [
 ("Year he was born", "1949", 1949), ("FA Cups he won with Arsenal", "7", 7), ("Year he joined Arsenal", "1996", 1996),
 ("Premier League titles he won", "3", 3), ("Year he left Arsenal", "2018", 2018), ("Year the Invincibles finished unbeaten", "2004", 2004)])
game("the numbers of Jürgen Klopp", "Football", "medium", ["Jürgen Klopp", "Liverpool", "managers"], [
 ("Year he was born", "1967", 1967), ("Bundesliga titles he won with Dortmund", "2", 2), ("Year he joined Liverpool", "2015", 2015),
 ("Year he left Liverpool", "2024", 2024), ("Year he won the Champions League", "2019", 2019), ("Year he won the Premier League", "2020", 2020)])
game("the numbers of Pep Guardiola", "Football", "medium", ["Pep Guardiola", "Manchester City", "managers"], [
 ("Year he was born", "1971", 1971), ("Premier League titles he won, 2018 to 2024", "6", 6), ("Year he joined Manchester City", "2016", 2016),
 ("Year he became Barcelona manager", "2008", 2008), ("Year City won the treble", "2023", 2023)])
game("the numbers of José Mourinho", "Football", "medium", ["José Mourinho", "Chelsea", "managers"], [
 ("Year he was born", "1963", 1963), ("Champions League titles he won as a manager", "2", 2), ("Year he first joined Chelsea", "2004", 2004),
 ("Premier League titles he won with Chelsea", "3", 3), ("Year he won the treble with Inter", "2010", 2010)])
game("the numbers of Zinedine Zidane", "Football", "medium", ["Zinedine Zidane", "France", "Real Madrid"], [
 ("Year he was born", "1972", 1972), ("Champions Leagues he won as Real Madrid manager", "3", 3), ("Year he won the World Cup", "1998", 1998),
 ("Year of his headbutt in the World Cup final", "2006", 2006), ("Year of his first Champions League as a manager", "2016", 2016)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-78.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
