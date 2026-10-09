# Bank session 10 Oct 2026: 20 more Play Your Cards Right games -> bank/cards-16.json. A row of 5-7 cards each:
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

game("the year each comedy film came out", "Film", "medium", ["comedy", "films", "years"], [
 ("Some Like It Hot", "1959", 1959), ("Bridesmaids", "2011", 2011), ("Monty Python and the Holy Grail", "1975", 1975),
 ("Groundhog Day", "1993", 1993), ("Life of Brian", "1979", 1979), ("Ghostbusters", "1984", 1984)])
game("the year each animated film came out", "Film", "medium", ["animation", "films", "years"], [
 ("Watership Down", "1978", 1978), ("Despicable Me", "2010", 2010), ("Who Framed Roger Rabbit", "1988", 1988),
 ("Shrek", "2001", 2001), ("Wallace & Gromit: The Wrong Trousers", "1993", 1993), ("Chicken Run", "2000", 2000)])
game("the year each science fiction book came out", "Books", "hard", ["science fiction", "years"], [
 ("The Time Machine", "1895", 1895), ("The Hitchhiker's Guide to the Galaxy", "1979", 1979), ("The War of the Worlds", "1898", 1898),
 ("Fahrenheit 451", "1953", 1953), ("Brave New World", "1932", 1932), ("Nineteen Eighty-Four", "1949", 1949)])
game("the year each children's book came out", "Books", "medium", ["children's books", "years"], [
 ("Alice's Adventures in Wonderland", "1865", 1865), ("Matilda", "1988", 1988), ("The Lion, the Witch and the Wardrobe", "1950", 1950),
 ("The Very Hungry Caterpillar", "1969", 1969), ("The Cat in the Hat", "1957", 1957), ("Charlie and the Chocolate Factory", "1964", 1964)])
game("how many time zones in each?", "World geography", "hard", ["time zones", "countries"], [
 ("China", "1", 1), ("France, counting its lands overseas", "12", 12), ("The mainland USA", "4", 4), ("Russia", "11", 11), ("Mainland Australia", "3", 3), ("Canada", "6", 6)])
game("the year each holiday name began", "Travel", "hard", ["holidays", "airlines", "years"], [
 ("Butlin's first holiday camp", "1936", 1936), ("easyJet", "1995", 1995), ("British Airways", "1974", 1974), ("Ryanair", "1984", 1984), ("Pontins", "1946", 1946)])
game("the year of each great find", "History", "medium", ["archaeology", "years"], [
 ("The Rosetta Stone", "1799", 1799), ("Richard III under a car park", "2012", 2012), ("Tutankhamun's tomb", "1922", 1922),
 ("The Terracotta Army", "1974", 1974), ("The Sutton Hoo ship burial", "1939", 1939), ("The Dead Sea Scrolls", "1947", 1947)])
game("the year of each great fire", "History", "hard", ["fires", "years"], [
 ("The Houses of Parliament burn down", "1834", 1834), ("Notre-Dame", "2019", 2019), ("The Crystal Palace", "1936", 1936),
 ("Windsor Castle", "1992", 1992), ("York Minster", "1984", 1984), ("Hampton Court Palace", "1986", 1986)])
game("the number on each famous shirt", "Sport", "medium", ["shirt numbers"], [
 ("Alan Shearer at Newcastle", "9", 9), ("David Beckham at Real Madrid", "23", 23), ("Eric Cantona", "7", 7), ("Kobe Bryant, later on", "24", 24), ("Pelé", "10", 10)])
game("the year each spooky novel came out", "Books", "hard", ["horror", "books", "years"], [
 ("Rebecca", "1938", 1938), ("It", "1986", 1986), ("The Exorcist", "1971", 1971), ("The Woman in Black", "1983", 1983), ("Carrie", "1974", 1974), ("The Shining", "1977", 1977)])
game("the year each star retired", "Sport", "medium", ["retirements", "years"], [
 ("Pelé", "1977", 1977), ("Andy Murray", "2024", 2024), ("Muhammad Ali", "1981", 1981), ("Roger Federer", "2022", 2022), ("Alan Shearer", "2006", 2006), ("David Beckham", "2013", 2013)])
game("the year of each Elizabeth II milestone", "The royal family", "easy", ["Elizabeth II", "jubilees", "years"], [
 ("She becomes Queen", "1952", 1952), ("Her Platinum Jubilee", "2022", 2022), ("Charles becomes Prince of Wales at Caernarfon", "1969", 1969),
 ("Her Diamond Jubilee", "2012", 2012), ("Her Silver Jubilee", "1977", 1977), ("Her Golden Jubilee", "2002", 2002)])
game("the year each statue was unveiled", "Famous landmarks", "hard", ["statues", "years"], [
 ("Eros in Piccadilly Circus", "1893", 1893), ("Bobby Moore at Wembley", "2007", 2007), ("The Little Mermaid in Copenhagen", "1913", 1913),
 ("Christ the Redeemer in Rio", "1931", 1931), ("The Lincoln Memorial", "1922", 1922)])
game("how many countries on each continent?", "World geography", "hard", ["continents", "countries"], [
 ("South America", "12", 12), ("Africa", "54", 54), ("Oceania", "14", 14), ("Asia", "48", 48), ("North America", "23", 23)])
game("the year each family game came out", "Games and toys", "hard", ["board games", "years"], [
 ("Mouse Trap", "1963", 1963), ("Pictionary", "1985", 1985), ("Operation", "1965", 1965),
 ("Hungry Hungry Hippos", "1978", 1978), ("Twister", "1966", 1966), ("Connect 4", "1974", 1974)])
game("the year each sport joined (or came back to) the Olympics", "The Olympics", "hard", ["Olympics", "sports", "years"], [
 ("Tennis comes back", "1988", 1988), ("Breaking", "2024", 2024), ("Women's football", "1996", 1996),
 ("Rugby sevens", "2016", 2016), ("Triathlon", "2000", 2000), ("Skateboarding", "2021", 2021)])
game("how many years was each manager in charge?", "Football", "hard", ["managers", "years"], [
 ("Bobby Robson at Newcastle", "5", 5), ("Arsène Wenger at Arsenal", "22", 22), ("Jürgen Klopp at Liverpool", "9", 9),
 ("Brian Clough at Nottingham Forest", "18", 18), ("Bill Shankly at Liverpool", "15", 15)])
game("the year each robot or computer film came out", "Film", "medium", ["robots", "films", "years"], [
 ("2001: A Space Odyssey", "1968", 1968), ("WALL-E", "2008", 2008), ("Blade Runner", "1982", 1982),
 ("The Matrix", "1999", 1999), ("The Terminator", "1984", 1984), ("I, Robot", "2004", 2004)])
game("the year each one stopped printing", "Nostalgia", "hard", ["magazines", "newspapers", "years"], [
 ("Punch (the first time)", "1992", 1992), ("The Dandy", "2012", 2012), ("Smash Hits", "2006", 2006), ("The News of the World", "2011", 2011), ("The Face (the first time)", "2004", 2004)])
game("the numbers on a snooker table", "Snooker", "medium", ["snooker", "numbers"], [
 ("Pockets", "6", 6), ("Balls on the table at the start", "22", 22), ("Colours, not counting the reds", "6", 6), ("Reds", "15", 15), ("Points for clearing the colours", "27", 27)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-16.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
