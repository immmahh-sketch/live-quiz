# Bank session 10 Oct 2026: 8 more Play Your Cards Right games -> bank/cards-54.json (famous lives, North East heroes). A row of 5-7 cards each:
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

game("the numbers of Jane Austen", "Books", "medium", ["Jane Austen", "authors"], [
 ("Year she was born", "1775", 1775), ("Novels she finished", "6", 6), ("Year 'Pride and Prejudice' came out", "1813", 1813),
 ("Her age when she died", "41", 41), ("Year she died", "1817", 1817)])
game("the numbers of Galileo", "Science", "hard", ["Galileo", "astronomy", "scientists"], [
 ("Year he was born", "1564", 1564), ("Moons of Jupiter he discovered", "4", 4), ("Year he spotted them", "1610", 1610),
 ("His age when he died", "77", 77), ("Year he died", "1642", 1642)])
game("the numbers of Emmeline Pankhurst", "History", "hard", ["Emmeline Pankhurst", "suffragettes", "votes for women"], [
 ("Year she was born", "1858", 1858), ("Year she founded the Women's Social and Political Union", "1903", 1903), ("Age women had to be to vote in 1918", "30", 30),
 ("Year the first women won the vote", "1918", 1918), ("Her age when she died", "69", 69), ("Year she died, weeks before women got equal votes", "1928", 1928)])
game("the numbers of Elizabeth I", "History", "medium", ["Elizabeth I", "Tudors"], [
 ("Year she was born", "1533", 1533), ("Her age when she became queen", "25", 25), ("Year she came to the throne", "1558", 1558),
 ("Years she reigned", "44", 44), ("Year of the Spanish Armada", "1588", 1588), ("Year she died", "1603", 1603)])
game("the numbers of Mo Farah", "Sport", "medium", ["Mo Farah", "athletics", "Olympics"], [
 ("Year he was born", "1983", 1983), ("His Olympic gold medals", "4", 4), ("Year of 'Super Saturday' in London", "2012", 2012),
 ("His world championship gold medals", "6", 6), ("Year he was knighted", "2017", 2017)])
game("the numbers of Jackie Milburn", "Football", "hard", ["Jackie Milburn", "Newcastle United", "North East"], [
 ("Year he was born, in Ashington", "1924", 1924), ("His Newcastle goals in league and cup", "200", 200), ("FA Cups he won", "3", 3),
 ("Year of his goal 45 seconds into a Cup final", "1955", 1955), ("His England caps", "13", 13), ("Year he died", "1988", 1988)])
game("the numbers of Brian Clough", "Football", "medium", ["Brian Clough", "managers", "North East"], [
 ("Year he was born, in Middlesbrough", "1935", 1935), ("League goals for Middlesbrough and Sunderland", "251", 251), ("Days he lasted as Leeds manager", "44", 44),
 ("Year he first won the European Cup", "1979", 1979), ("European Cups he won with Forest", "2", 2), ("Year he died", "2004", 2004)])
game("the numbers of Grace Darling", "North East England", "hard", ["Grace Darling", "Northumberland", "lifeboats"], [
 ("Year she was born", "1815", 1815), ("Survivors she and her father rescued", "9", 9), ("Year of the rescue", "1838", 1838),
 ("Her age at the time", "22", 22), ("Year she died", "1842", 1842), ("Her age when she died", "26", 26)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-54.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
