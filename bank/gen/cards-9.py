# Bank session 10 Oct 2026: 20 more Play Your Cards Right games -> bank/cards-9.json. A row of 5-7 cards each:
# what's on the card, what it shows when it flips, and the number compared. The numbers zig-zag, no equal neighbours.
import json, os
G = []
def game(text, cat, diff, tags, cards):
    ns = [n for _, _, n in cards]
    assert 5 <= len(cards) <= 7, text
    assert all(ns[i] != ns[i - 1] for i in range(1, len(ns))), (text, 'equal neighbours')
    assert len({l for l, _, _ in cards}) == len(cards), (text, 'repeated card')
    G.append({"type": "cards", "text": "Play Your Cards Right: " + text, "category": cat, "tags": ["Play Your Cards Right"] + tags, "difficulty": diff,
              "cards": [{"label": l, "value": v, "n": n} for l, v, n in cards]})

game("the year of each UK Eurovision win", "Eurovision", "hard", ["Eurovision", "years"], [
 ("Bucks Fizz", "1981", 1981), ("Sandie Shaw", "1967", 1967), ("Katrina and the Waves", "1997", 1997), ("Lulu", "1969", 1969), ("Brotherhood of Man", "1976", 1976)])
game("the year each ABBA single came out", "Music", "hard", ["ABBA", "years"], [
 ("Waterloo", "1974", 1974), ("The Winner Takes It All", "1980", 1980), ("Mamma Mia", "1975", 1975),
 ("Take a Chance on Me", "1978", 1978), ("Dancing Queen", "1976", 1976), ("Knowing Me, Knowing You", "1977", 1977)])
game("how old was each at that Wimbledon win?", "Tennis", "hard", ["Wimbledon", "ages"], [
 ("Martina Hingis (1997)", "16", 16), ("Roger Federer (2017)", "35", 35), ("Boris Becker (1985)", "17", 17), ("Andy Murray (2013)", "26", 26), ("Novak Djokovic (2011)", "24", 24)])
game("the year each character first appeared in print", "Books", "medium", ["characters", "years"], [
 ("Sherlock Holmes", "1887", 1887), ("Harry Potter", "1997", 1997), ("Peter Rabbit", "1902", 1902),
 ("Paddington Bear", "1958", 1958), ("Winnie-the-Pooh", "1926", 1926), ("James Bond", "1953", 1953)])
game("the year each painting was made", "Art", "hard", ["paintings", "years"], [
 ("The Mona Lisa (begun)", "about 1503", 1503), ("Van Gogh: The Starry Night", "1889", 1889), ("Vermeer: Girl with a Pearl Earring", "about 1665", 1665),
 ("Munch: The Scream", "1893", 1893), ("Constable: The Hay Wain", "1821", 1821), ("Van Gogh: Sunflowers", "1888", 1888)])
game("how many teams in each?", "Sport", "medium", ["tournaments", "teams"], [
 ("The Ryder Cup", "2", 2), ("Euro 2024", "24", 24), ("The Six Nations", "6", 6),
 ("The 2026 World Cup", "48", 48), ("The 2023 Rugby World Cup", "20", 20), ("The 2022 World Cup", "32", 32)])
game("roughly how many miles long?", "Britain", "hard", ["distances", "routes"], [
 ("The Great North Run", "13.1", 13.1), ("The Pennine Way", "about 268", 268), ("The Channel Tunnel", "about 31", 31),
 ("The M1", "about 193", 193), ("The Tyne and Wear Metro network", "about 48", 48), ("Hadrian's Wall", "about 73", 73)])
game("Rugby World Cup wins, up to 2025", "Rugby", "hard", ["Rugby World Cup"], [
 ("England men", "1", 1), ("New Zealand women", "6", 6), ("England women (the Red Roses)", "3", 3),
 ("South Africa men", "4", 4), ("Australia men", "2", 2), ("New Zealand men", "3", 3)])
game("the year of each great British sporting moment", "Sport", "medium", ["moments", "years"], [
 ("Fred Perry wins Wimbledon for the last time", "1936", 1936), ("Ben Stokes's Headingley miracle", "2019", 2019), ("Gazza's goal against Scotland at Wembley", "1996", 1996),
 ("The Lionesses win the Euros", "2022", 2022), ("Jonny Wilkinson's World Cup drop goal", "2003", 2003), ("Andy Murray's first Wimbledon title", "2013", 2013)])
game("the year each road opened", "Britain", "hard", ["roads", "years"], [
 ("The first stretch of the M1", "1959", 1959), ("The M6 Toll", "2003", 2003), ("The first Tyne Tunnel", "1967", 1967),
 ("The Queen Elizabeth II Bridge at Dartford", "1991", 1991), ("Spaghetti Junction", "1972", 1972), ("The M25 (finished)", "1986", 1986)])
game("each transfer fee, in £ millions", "Football", "hard", ["transfers", "fees"], [
 ("Trevor Francis to Nottingham Forest (1979)", "about £1.15m", 1.15), ("Neymar to PSG (2017)", "about £198m", 198), ("Alan Shearer to Newcastle (1996)", "£15m", 15),
 ("Alexander Isak to Liverpool (2025)", "£125m", 125), ("Jack Grealish to Man City (2021)", "£100m", 100), ("Declan Rice to Arsenal (2023)", "£105m", 105)])
game("the year each drink was launched", "Food and drink", "hard", ["drinks", "years"], [
 ("Coca-Cola", "1886", 1886), ("Red Bull", "1987", 1987), ("Irn-Bru", "1901", 1901),
 ("Newcastle Brown Ale", "1927", 1927), ("Vimto", "1908", 1908), ("Tizer", "1924", 1924)])
game("points needed to win a game", "Games and sport", "medium", ["scoring", "games"], [
 ("Table tennis", "11", 11), ("A leg of darts", "501", 501), ("Badminton", "21", 21), ("Cribbage", "121", 121), ("A volleyball set", "25", 25)])
game("the year each British city hosted the Commonwealth Games", "Sport", "hard", ["Commonwealth Games", "years"], [
 ("London", "1934", 1934), ("Birmingham", "2022", 2022), ("Cardiff", "1958", 1958),
 ("Glasgow", "2014", 2014), ("Edinburgh (first time)", "1970", 1970), ("Manchester", "2002", 2002)])
game("the numbers in TV games and board games", "Games and toys", "medium", ["game shows", "games"], [
 ("Dice in Yahtzee", "5", 5), ("Seconds on the Countdown clock", "30", 30), ("Letters picked in a Countdown letters round", "9", 9),
 ("Hexagons on the Blockbusters board", "20", 20), ("Numbers picked in a Countdown numbers round", "6", 6), ("Tiles on a Scrabble rack", "7", 7)])
game("the year of each moment in space", "Space", "medium", ["space", "years"], [
 ("Sputnik 1 is launched", "1957", 1957), ("Tim Peake goes to the space station", "2015", 2015), ("Apollo 13", "1970", 1970),
 ("The first crew moves into the space station", "2000", 2000), ("The Hubble telescope is launched", "1990", 1990), ("Helen Sharman becomes the first Briton in space", "1991", 1991)])
game("the year each shop began", "Shopping", "hard", ["shops", "years"], [
 ("Boots", "1849", 1849), ("Primark", "1969", 1969), ("Fenwick (Newcastle)", "1882", 1882),
 ("Tesco", "1919", 1919), ("John Lewis", "1864", 1864), ("Asda", "1965", 1965)])
game("how many faces?", "Maths and numbers", "medium", ["shapes", "faces"], [
 ("Mount Rushmore", "4", 4), ("An icosahedron", "20", 20), ("A Rubik's Cube", "6", 6), ("A dodecahedron", "12", 12), ("A square-based pyramid", "5", 5)])
game("the year each café or pub chain began", "Food and drink", "hard", ["chains", "years"], [
 ("Costa Coffee", "1971", 1971), ("Starbucks' first UK shop", "1998", 1998), ("Wetherspoon's first pub", "1979", 1979),
 ("Caffè Nero", "1997", 1997), ("Pret A Manger", "1986", 1986), ("Nando's first UK restaurant", "1992", 1992)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-9.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
