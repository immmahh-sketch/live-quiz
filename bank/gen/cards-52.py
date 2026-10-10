# Bank session 10 Oct 2026: 8 more Play Your Cards Right games -> bank/cards-52.json (famous lives). A row of 5-7 cards each:
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

game("the numbers of Martin Luther King", "History", "medium", ["Martin Luther King", "civil rights"], [
 ("Year he was born", "1929", 1929), ("His children", "4", 4), ("Year of his 'I Have a Dream' speech", "1963", 1963),
 ("His age when he was killed", "39", 39), ("Year he won the Nobel Peace Prize", "1964", 1964)])
game("the numbers of Marie Curie", "Science", "medium", ["Marie Curie", "scientists"], [
 ("Year she was born", "1867", 1867), ("Nobel Prizes she won", "2", 2), ("Year of her first Nobel Prize", "1903", 1903),
 ("Her age when she died", "66", 66), ("Year of her second Nobel Prize", "1911", 1911)])
game("the numbers of Abraham Lincoln", "History", "medium", ["Abraham Lincoln", "US presidents"], [
 ("Year he was born", "1809", 1809), ("His number as president", "16", 16), ("Year of the Gettysburg Address", "1863", 1863),
 ("Words in the Gettysburg Address, roughly", "270", 270), ("His age when he was shot", "56", 56)])
game("the numbers of Leonardo da Vinci", "Art", "hard", ["Leonardo da Vinci", "artists"], [
 ("Year he was born", "1452", 1452), ("His age when he died", "67", 67), ("Year he finished The Last Supper, roughly", "1498", 1498),
 ("Year he began the Mona Lisa, roughly", "1503", 1503), ("Year he died", "1519", 1519)])
game("the numbers of Charles Dickens", "Books", "medium", ["Charles Dickens", "authors"], [
 ("Year he was born", "1812", 1812), ("Novels he finished", "14", 14), ("His children", "10", 10),
 ("His age when he died", "58", 58), ("Year he died", "1870", 1870)])
game("the numbers of Roald Dahl", "Children's books", "medium", ["Roald Dahl", "authors"], [
 ("Year he was born", "1916", 1916), ("His children", "5", 5), ("Year 'Charlie and the Chocolate Factory' came out", "1964", 1964),
 ("His age when he died", "74", 74), ("Year 'Matilda' came out", "1988", 1988)])
game("the numbers of Albert Einstein", "Science", "medium", ["Albert Einstein", "scientists"], [
 ("Year he was born", "1879", 1879), ("Ground-breaking papers in his 'miracle year'", "4", 4), ("Year of that miracle year", "1905", 1905),
 ("His age when he died", "76", 76), ("Year he won the Nobel Prize", "1921", 1921)])
game("the numbers of Florence Nightingale", "History", "medium", ["Florence Nightingale", "nursing"], [
 ("Year she was born", "1820", 1820), ("Nurses she took to the Crimea", "38", 38), ("Year she went to the Crimean War", "1854", 1854),
 ("Her age when she died", "90", 90), ("Year she died", "1910", 1910)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-52.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
