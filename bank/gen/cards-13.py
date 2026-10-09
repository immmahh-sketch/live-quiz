# Bank session 10 Oct 2026: 20 more Play Your Cards Right games -> bank/cards-13.json. A row of 5-7 cards each:
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

game("Olympic gold medals for each legend", "The Olympics", "medium", ["Olympics", "legends"], [
 ("Steve Redgrave", "5", 5), ("Michael Phelps", "23", 23), ("Usain Bolt", "8", 8), ("Carl Lewis", "9", 9), ("Simone Biles", "7", 7), ("Mark Spitz", "9", 9)])
game("the year each tech company was founded", "Science and technology", "hard", ["companies", "years"], [
 ("Nintendo", "1889", 1889), ("Apple", "1976", 1976), ("IBM", "1911", 1911), ("Microsoft", "1975", 1975), ("Samsung", "1938", 1938), ("Sony", "1946", 1946)])
game("the year each car maker began", "Cars", "hard", ["cars", "companies", "years"], [
 ("Ford", "1903", 1903), ("Tesla", "2003", 2003), ("Rolls-Royce", "1906", 1906), ("Toyota", "1937", 1937), ("Aston Martin", "1913", 1913), ("Mercedes-Benz", "1926", 1926)])
game("how many wheels?", "Cars", "easy", ["wheels", "vehicles"], [
 ("A unicycle", "1", 1), ("An American 18-wheeler", "18", 18), ("A motorbike", "2", 2), ("A car", "4", 4), ("A Reliant Robin", "3", 3)])
game("the year each radio show began", "Radio", "hard", ["radio", "years"], [
 ("Desert Island Discs", "1942", 1942), ("I'm Sorry I Haven't a Clue", "1972", 1972), ("Woman's Hour", "1946", 1946),
 ("Just a Minute", "1967", 1967), ("The Archers", "1951", 1951), ("The Today programme", "1957", 1957)])
game("the year each royal building was begun", "Kings and queens", "hard", ["palaces", "castles", "years"], [
 ("Windsor Castle", "about 1070", 1070), ("Balmoral Castle (today's)", "1853", 1853), ("The Tower of London's White Tower", "about 1078", 1078),
 ("Buckingham House", "1703", 1703), ("Hampton Court Palace", "1514", 1514)])
game("the year each toy craze began", "Games and toys", "hard", ["toys", "years"], [
 ("Care Bears", "1981", 1981), ("Beanie Babies", "1993", 1993), ("My Little Pony", "1982", 1982),
 ("Polly Pocket", "1989", 1989), ("Transformers", "1984", 1984), ("Sylvanian Families", "1985", 1985)])
game("the year each Tube line opened", "London", "hard", ["London Underground", "years"], [
 ("The Metropolitan line", "1863", 1863), ("The Jubilee line", "1979", 1979), ("The Waterloo & City line", "1898", 1898),
 ("The Victoria line", "1968", 1968), ("The Central line", "1900", 1900), ("The Bakerloo line", "1906", 1906)])
game("UK number one singles", "Music", "hard", ["number ones", "acts"], [
 ("Take That", "12", 12), ("Elvis Presley", "21", 21), ("Madonna", "13", 13), ("The Beatles", "17", 17), ("Cliff Richard", "14", 14)])
game("the numbers in Shakespeare", "Books", "medium", ["Shakespeare", "numbers"], [
 ("Witches in Macbeth", "3", 3), ("Shakespeare's sonnets", "154", 154), ("Acts in each play", "5", 5), ("Juliet's age", "13", 13), ("Lines in a sonnet", "14", 14)])
game("the year each author died", "Books", "hard", ["authors", "years"], [
 ("William Shakespeare", "1616", 1616), ("Roald Dahl", "1990", 1990), ("Jane Austen", "1817", 1817),
 ("Agatha Christie", "1976", 1976), ("Charlotte Brontë", "1855", 1855), ("Charles Dickens", "1870", 1870)])
game("the year each computer arrived", "Science and technology", "medium", ["computers", "years"], [
 ("The IBM PC", "1981", 1981), ("The Raspberry Pi", "2012", 2012), ("The ZX Spectrum", "1982", 1982), ("Windows 95", "1995", 1995), ("The Amiga", "1985", 1985)])
game("the year each treaty or deal was signed", "History", "hard", ["treaties", "years"], [
 ("The Act of Union (England and Scotland)", "1707", 1707), ("The Good Friday Agreement", "1998", 1998), ("The Treaty of Versailles", "1919", 1919),
 ("The Maastricht Treaty", "1992", 1992), ("The Treaty of Rome", "1957", 1957)])
game("the year of each great TV moment", "Film and TV", "hard", ["TV", "moments", "years"], [
 ("Lulu the elephant runs riot on Blue Peter", "1969", 1969), ("Bake Off moves to Channel 4", "2017", 2017), ("Who shot JR?", "1980", 1980),
 ("Del Boy falls through the bar", "1989", 1989), ("Den hands Angie the divorce papers", "1986", 1986)])
game("men's world records, in metres", "Athletics", "hard", ["records", "field events"], [
 ("High jump", "2.45 m", 2.45), ("Javelin", "98.48 m", 98.48), ("Long jump", "8.95 m", 8.95), ("Shot put", "23.56 m", 23.56), ("Triple jump", "18.29 m", 18.29)])
game("the year of each first for women", "History", "hard", ["women", "firsts", "years"], [
 ("Nancy Astor takes her seat as an MP", "1919", 1919), ("Margaret Thatcher becomes Prime Minister", "1979", 1979), ("Gertrude Ederle swims the Channel", "1926", 1926),
 ("Junko Tabei climbs Everest", "1975", 1975), ("Nan Winton reads the news on BBC TV", "1960", 1960), ("The Equal Pay Act", "1970", 1970)])
game("the measurements of a football pitch", "Football", "medium", ["pitch", "measurements"], [
 ("To the penalty spot, in yards", "12", 12), ("Width of the goal, in yards", "8", 8), ("Depth of the penalty area, in yards", "18", 18),
 ("Depth of the six-yard box, in yards", "6", 6), ("Radius of the centre circle, in yards", "10", 10), ("Height of the goal, in feet", "8", 8)])
game("the year each horse race was first run", "Horse racing", "hard", ["races", "years"], [
 ("The first racing at Ascot", "1711", 1711), ("The Cheltenham Gold Cup", "1924", 1924), ("The St Leger", "1776", 1776),
 ("The King George VI Chase", "1937", 1937), ("The Derby", "1780", 1780), ("The Northumberland Plate", "1833", 1833)])
game("the year of each famous diary", "Books", "medium", ["diaries", "years"], [
 ("Samuel Pepys begins his diary", "1660", 1660), ("Diary of a Wimpy Kid", "2007", 2007), ("Anne Frank's diary is published", "1947", 1947),
 ("Bridget Jones's Diary", "1996", 1996), ("The Secret Diary of Adrian Mole", "1982", 1982)])
game("the year of each flight", "History", "medium", ["flight", "years"], [
 ("The Wright brothers' first flight", "1903", 1903), ("Concorde's last flight", "2003", 2003), ("Alcock and Brown fly the Atlantic", "1919", 1919),
 ("Concorde's first passenger flight", "1976", 1976), ("Amelia Earhart flies the Atlantic solo", "1932", 1932), ("The first jumbo jet passenger flight", "1970", 1970)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-13.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
