# Bank session 11 Oct 2026: 9 more Play Your Cards Right games -> bank/cards-65.json (sport stars and a North East author). A row of 5-7 cards each:
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

game("the numbers of Emma Raducanu", "Sport", "medium", ["Emma Raducanu", "tennis"], [
 ("Year she was born", "2002", 2002), ("Her world ranking when she won the US Open", "150", 150), ("Year she won it", "2021", 2021),
 ("Matches she won there, qualifying included", "10", 10), ("Sets she dropped along the way", "0", 0)])
game("the numbers of Mohamed Salah", "Football", "medium", ["Mo Salah", "Liverpool", "Egypt"], [
 ("Year he was born", "1992", 1992), ("Premier League goals in his first Liverpool season", "32", 32), ("Year he joined Chelsea", "2014", 2014),
 ("Premier League Golden Boots he's won, up to 2025", "4", 4), ("Year he joined Liverpool", "2017", 2017)])
game("the numbers of Erling Haaland", "Football", "medium", ["Erling Haaland", "Manchester City", "Norway"], [
 ("Year he was born", "2000", 2000), ("His Premier League goals in his first season, a record", "36", 36), ("Year he joined Manchester City", "2022", 2022),
 ("Goals he scored in one Champions League game against Leipzig", "5", 5), ("His height in centimetres", "195", 195)])
game("the numbers of Paul Scholes", "Football", "medium", ["Paul Scholes", "Manchester United", "England"], [
 ("Year he was born", "1974", 1974), ("His England caps", "66", 66), ("Year he finally retired", "2013", 2013),
 ("Premier League titles he won", "11", 11), ("His Manchester United appearances", "718", 718)])
game("the numbers of Thierry Henry", "Football", "medium", ["Thierry Henry", "Arsenal", "France"], [
 ("Year he was born", "1977", 1977), ("His Arsenal goals, a club record", "228", 228), ("Year he won the World Cup", "1998", 1998),
 ("Year he joined Arsenal", "1999", 1999), ("Year of the Invincibles' title", "2004", 2004)])
game("the numbers of Brian O'Driscoll", "Sport", "medium", ["Brian O'Driscoll", "rugby", "Ireland"], [
 ("Year he was born", "1979", 1979), ("His Ireland caps", "133", 133), ("Year Ireland won the Grand Slam with him as captain", "2009", 2009),
 ("His tries for Ireland", "46", 46), ("British and Irish Lions tours he went on", "4", 4)])
game("the numbers of Martin Johnson", "Sport", "medium", ["Martin Johnson", "rugby", "England"], [
 ("Year he was born", "1970", 1970), ("His England caps", "84", 84), ("Year he lifted the World Cup", "2003", 2003),
 ("Lions tours he captained", "2", 2), ("Year he became England manager", "2008", 2008)])
game("the numbers of Catherine Cookson", "Books", "hard", ["Catherine Cookson", "authors", "South Shields"], [
 ("Year she was born, in Tyne Dock", "1906", 1906), ("Year her first novel came out", "1950", 1950), ("Novels she wrote, roughly", "100", 100),
 ("Year she became a dame", "1993", 1993), ("Year she died", "1998", 1998)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-65.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
