# Bank session 10 Oct 2026: 8 more Play Your Cards Right games -> bank/cards-50.json (famous lives). A row of 5-7 cards each:
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

game("the numbers of Charles Darwin", "Science", "medium", ["Charles Darwin", "scientists"], [
 ("Year he was born", "1809", 1809), ("Years the Beagle voyage lasted", "5", 5), ("Year 'On the Origin of Species' came out", "1859", 1859),
 ("His age when he died", "73", 73), ("Year he died", "1882", 1882)])
game("the numbers of Isaac Newton", "Science", "medium", ["Isaac Newton", "scientists"], [
 ("Year he was born", "1642", 1642), ("His laws of motion", "3", 3), ("Year 'Principia' was published", "1687", 1687),
 ("His age when he died", "84", 84), ("Year he died", "1727", 1727)])
game("the numbers of Mozart", "Music", "medium", ["Mozart", "composers"], [
 ("Year he was born", "1756", 1756), ("His age when he died", "35", 35), ("Numbered symphonies", "41", 41),
 ("Year he died", "1791", 1791), ("His age when he wrote his first pieces", "5", 5)])
game("the numbers of Beethoven", "Music", "medium", ["Beethoven", "composers"], [
 ("Year he was born", "1770", 1770), ("Symphonies", "9", 9), ("Piano sonatas", "32", 32),
 ("Year he died", "1827", 1827), ("His age when he died", "56", 56)])
game("the numbers of Agatha Christie", "Books", "medium", ["Agatha Christie", "crime fiction"], [
 ("Year she was born", "1890", 1890), ("Detective novels she wrote", "66", 66), ("Novels starring Poirot", "33", 33),
 ("Year she died", "1976", 1976), ("Days she went missing in 1926", "11", 11)])
game("the numbers of Usain Bolt", "Sport", "medium", ["Usain Bolt", "athletics"], [
 ("Olympic gold medals", "8", 8), ("Year he was born", "1986", 1986), ("World Championship gold medals", "11", 11),
 ("Year he set both sprint world records, in Berlin", "2009", 2009), ("Olympic Games he ran at", "4", 4)])
game("the numbers of Muhammad Ali", "Sport", "medium", ["Muhammad Ali", "boxing"], [
 ("Year he was born", "1942", 1942), ("Professional fights", "61", 61), ("Professional defeats", "5", 5),
 ("Year he won Olympic gold", "1960", 1960), ("Professional wins", "56", 56)])
game("the numbers of Sir Bobby Robson", "Football", "medium", ["Bobby Robson", "Newcastle United", "England"], [
 ("Year he was born", "1933", 1933), ("England caps as a player", "20", 20), ("Years in charge of Ipswich", "13", 13),
 ("Year he became Newcastle manager", "1999", 1999), ("His age when he died", "76", 76)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-50.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
