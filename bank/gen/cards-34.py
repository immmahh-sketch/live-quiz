# Bank session 10 Oct 2026: 8 more Play Your Cards Right games -> bank/cards-34.json. A row of 5-7 cards each:
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

game("the numbers in UK money", "Britain", "easy", ["money", "coins"], [
 ("Different coins in everyday use", "8", 8), ("Sides on a 50p", "7", 7), ("Sides on today's £1 coin", "12", 12),
 ("Pence in a pound", "100", 100), ("Bank of England notes in use", "4", 4)])
game("the numbers of the London Underground", "London", "medium", ["London Underground", "Tube"], [
 ("Tube lines", "11", 11), ("Stations, roughly", "272", 272), ("Year the first line opened", "1863", 1863),
 ("Fare zones", "9", 9), ("Year the Elizabeth line opened", "2022", 2022)])
game("the numbers in your hand", "Science and nature", "medium", ["the body", "bones"], [
 ("Bones in your hand and wrist", "27", 27), ("Fingers and thumbs", "5", 5), ("Finger bones (phalanges)", "14", 14),
 ("Bones in your wrist", "8", 8), ("Bones in your palm", "5", 5)])
game("the numbers in American politics", "Politics", "medium", ["USA", "politics"], [
 ("States", "50", 50), ("Senators", "100", 100), ("Members of the House of Representatives", "435", 435),
 ("Supreme Court justices", "9", 9), ("Electoral votes needed to win", "270", 270), ("Years in a president's term", "4", 4)])
game("the numbers of the European Union", "Politics", "medium", ["European Union", "Europe"], [
 ("Member countries in 2025", "27", 27), ("Official languages", "24", 24), ("Countries using the euro in 2025", "20", 20),
 ("Year euro notes and coins arrived", "2002", 2002), ("Year of the UK's Brexit vote", "2016", 2016)])
game("the numbers of the United Nations", "Politics", "medium", ["United Nations"], [
 ("Member countries", "193", 193), ("Members of the Security Council", "15", 15), ("Permanent members of the Security Council", "5", 5),
 ("Year it was founded", "1945", 1945), ("Official languages", "6", 6)])
game("the numbers of NATO", "Politics", "medium", ["NATO"], [
 ("Member countries in 2025", "32", 32), ("Year it was founded", "1949", 1949), ("The famous 'attack on one is an attack on all' Article", "5", 5),
 ("Founding members", "12", 12), ("Nordic countries that joined in 2023–24", "2", 2)])
game("the numbers of the Commonwealth", "Politics", "hard", ["Commonwealth"], [
 ("Member countries", "56", 56), ("Years between Commonwealth Games", "4", 4), ("Year of the London Declaration that shaped it", "1949", 1949),
 ("Heads of the Commonwealth so far", "3", 3), ("Countries with the King as head of state", "15", 15)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-34.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
