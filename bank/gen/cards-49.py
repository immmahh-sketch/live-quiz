# Bank session 10 Oct 2026: 8 more Play Your Cards Right games -> bank/cards-49.json. A row of 5-7 cards each:
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

game("the numbers of Sherlock Holmes", "Books", "medium", ["Sherlock Holmes", "detectives"], [
 ("His house number on Baker Street", "221", 221), ("Novels about him", "4", 4), ("Short stories about him", "56", 56),
 ("Year he first appeared", "1887", 1887), ("Year Arthur Conan Doyle was born", "1859", 1859)])
game("the numbers of Winnie-the-Pooh", "Children's books", "medium", ["Winnie-the-Pooh", "children's books"], [
 ("Year the first Pooh book came out", "1926", 1926), ("The number in the name of his wood", "100", 100), ("Year Disney's 'The Many Adventures of Winnie the Pooh' came out", "1977", 1977),
 ("Year 'The House at Pooh Corner' came out", "1928", 1928), ("Year the film 'Christopher Robin' came out", "2018", 2018)])
game("the numbers of the Wright brothers' first flight", "History", "medium", ["flight", "Wright brothers"], [
 ("Year of the flight", "1903", 1903), ("Seconds the first flight lasted", "12", 12), ("Feet it covered", "120", 120),
 ("Flights they made that day", "4", 4), ("Seconds the longest flight that day lasted", "59", 59)])
game("the numbers of the Berlin Wall", "History", "medium", ["Berlin Wall", "Cold War"], [
 ("Year it went up", "1961", 1961), ("Year it came down", "1989", 1989), ("Years it stood", "28", 28),
 ("Length in kilometres, roughly", "155", 155), ("Year Germany reunified", "1990", 1990)])
game("the numbers of the Battle of Waterloo", "History", "medium", ["Waterloo", "Napoleon", "battles"], [
 ("Year of the battle", "1815", 1815), ("Day of June it was fought", "18", 18), ("Wellington's age at the battle", "46", 46),
 ("Year Napoleon died on St Helena", "1821", 1821), ("Years before ABBA won Eurovision with 'Waterloo'", "159", 159)])
game("the numbers of Dracula", "Books", "hard", ["Dracula", "Whitby", "horror"], [
 ("Year 'Dracula' was published", "1897", 1897), ("Steps up to Whitby Abbey", "199", 199), ("Year Bram Stoker was born", "1847", 1847),
 ("Boxes of earth the Count ships to England", "50", 50), ("Year Bela Lugosi's film came out", "1931", 1931)])
game("the numbers of Roman Britain", "History", "hard", ["Romans", "Britain"], [
 ("Year (BC) Julius Caesar first landed", "55", 55), ("Year (AD) of the Claudian invasion", "43", 43), ("Year (AD) Hadrian's Wall was begun", "122", 122),
 ("Legions usually stationed in Britain", "3", 3), ("Year (AD) the Romans left, roughly", "410", 410)])
game("the numbers of 'A Christmas Carol'", "Christmas", "medium", ["A Christmas Carol", "Dickens", "Christmas"], [
 ("Year it was published", "1843", 1843), ("Ghosts who visit Scrooge, counting Marley", "4", 4), ("Chapters, which Dickens called 'staves'", "5", 5),
 ("Shillings a week Bob Cratchit earns", "15", 15), ("Year Dickens was born", "1812", 1812)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-49.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
