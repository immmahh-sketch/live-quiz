# Bank session 10 Oct 2026: 20 more Play Your Cards Right games -> bank/cards-14.json. A row of 5-7 cards each:
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

game("the year of each North East football moment", "Newcastle v Sunderland", "hard", ["Newcastle", "Sunderland", "years"], [
 ("Kevin Keegan's 'I would love it' rant", "1996", 1996), ("Newcastle's Saudi-led takeover", "2021", 2021), ("Newcastle beat Barcelona 3–2 at St James'", "1997", 1997),
 ("Sunderland win the play-off final at Wembley", "2025", 2025), ("Sunderland's 105-point title season ends", "1999", 1999)])
game("the year each opera or ballet was first performed", "Classical music", "hard", ["opera", "ballet", "years"], [
 ("The Magic Flute", "1791", 1791), ("Madama Butterfly", "1904", 1904), ("Carmen", "1875", 1875),
 ("La Bohème", "1896", 1896), ("Swan Lake", "1877", 1877), ("The Nutcracker", "1892", 1892)])
game("the year each sports show began", "Film and TV", "hard", ["sport on TV", "years"], [
 ("Grandstand", "1958", 1958), ("Gladiators", "1992", 1992), ("Match of the Day", "1964", 1964),
 ("Sky Sports launches", "1991", 1991), ("A Question of Sport", "1970", 1970), ("Superstars", "1973", 1973)])
game("the year each sweet arrived", "Food and drink", "hard", ["sweets", "years"], [
 ("Haribo", "1920", 1920), ("Celebrations", "1998", 1998), ("Maltesers", "1936", 1936), ("Skittles (in the UK)", "1974", 1974), ("Smarties", "1937", 1937)])
game("the year each film musical came out", "Musicals", "medium", ["musicals", "films", "years"], [
 ("The Wizard of Oz", "1939", 1939), ("The Greatest Showman", "2017", 2017), ("Mary Poppins", "1964", 1964),
 ("Mamma Mia!", "2008", 2008), ("The Sound of Music", "1965", 1965), ("La La Land", "2016", 2016)])
game("the year of each famous speech", "History", "hard", ["speeches", "years"], [
 ("Lincoln's Gettysburg Address", "1863", 1863), ("The Queen's 'annus horribilis'", "1992", 1992), ("Churchill: 'We shall fight on the beaches'", "1940", 1940),
 ("Thatcher: 'The lady's not for turning'", "1980", 1980), ("Macmillan's 'wind of change'", "1960", 1960), ("Martin Luther King: 'I have a dream'", "1963", 1963)])
game("the year of each Beatles moment", "Music", "hard", ["Beatles", "years"], [
 ("Lennon meets McCartney", "1957", 1957), ("The Beatles split", "1970", 1970), ("Ringo joins", "1962", 1962),
 ("The rooftop concert", "1969", 1969), ("The Ed Sullivan Show in America", "1964", 1964)])
game("the year each zoo or safari park opened", "Animals", "hard", ["zoos", "years"], [
 ("London Zoo", "1828", 1828), ("Longleat Safari Park", "1966", 1966), ("Bristol Zoo", "1836", 1836), ("Chester Zoo", "1931", 1931), ("Edinburgh Zoo", "1913", 1913)])
game("men's world records, in seconds", "Athletics", "hard", ["records", "track"], [
 ("200 metres", "19.19", 19.19), ("1,500 metres", "3:26.00 (206 seconds)", 206), ("100 metres", "9.58", 9.58),
 ("800 metres", "1:40.91 (100.91 seconds)", 100.91), ("110 metres hurdles", "12.80", 12.80), ("400 metres", "43.03", 43.03)])
game("the year of each space mission", "Space", "medium", ["space", "missions", "years"], [
 ("Valentina Tereshkova, the first woman in space", "1963", 1963), ("The Curiosity rover lands on Mars", "2012", 2012), ("The first spacewalk", "1965", 1965),
 ("New Horizons flies past Pluto", "2015", 2015), ("Voyager 1 is launched", "1977", 1977), ("The first Space Shuttle flight", "1981", 1981)])
game("the number for each bingo call", "Games and toys", "easy", ["bingo", "numbers"], [
 ("Kelly's eye", "1", 1), ("Two fat ladies", "88", 88), ("Legs eleven", "11", 11), ("Clickety-click", "66", 66), ("Unlucky for some", "13", 13), ("Top of the shop", "90", 90)])
game("the year each mountain was first climbed", "World geography", "hard", ["mountains", "years"], [
 ("Mont Blanc", "1786", 1786), ("K2", "1954", 1954), ("The Matterhorn", "1865", 1865), ("The Eiger's north face", "1938", 1938), ("Kilimanjaro", "1889", 1889)])
game("the year each sporting home opened", "Sport", "hard", ["venues", "years"], [
 ("Lord's (today's ground)", "1814", 1814), ("The Crucible hosts the snooker", "1977", 1977), ("Twickenham", "1909", 1909),
 ("Murrayfield", "1925", 1925), ("Old Trafford", "1910", 1910), ("Wimbledon moves to Church Road", "1922", 1922)])
game("the year each film series began", "Film", "medium", ["film series", "years"], [
 ("Indiana Jones", "1981", 1981), ("The Hunger Games", "2012", 2012), ("Jurassic Park", "1993", 1993),
 ("Pirates of the Caribbean", "2003", 2003), ("Mission: Impossible", "1996", 1996), ("The Fast and the Furious", "2001", 2001)])
game("the year each everyday invention arrived", "Science and technology", "hard", ["inventions", "years"], [
 ("Cat's eyes on the roads", "1934", 1934), ("Post-it notes", "1980", 1980), ("Sellotape", "1937", 1937),
 ("The Rubik's Cube", "1974", 1974), ("The Biro", "1938", 1938), ("The lava lamp", "1963", 1963)])
game("roughly how high is each waterfall, in metres?", "World geography", "hard", ["waterfalls", "heights"], [
 ("High Force in Teesdale", "about 21 m", 21), ("Angel Falls", "about 979 m", 979), ("Niagara's Horseshoe Falls", "about 51 m", 51),
 ("Victoria Falls", "about 108 m", 108), ("Iguazu's Devil's Throat", "about 82 m", 82)])
game("the year each game character first appeared", "Games and toys", "medium", ["video games", "characters", "years"], [
 ("Mario", "1981", 1981), ("Master Chief", "2001", 2001), ("Link", "1986", 1986), ("Lara Croft", "1996", 1996), ("Sonic the Hedgehog", "1991", 1991)])
game("the year each app launched", "Science and technology", "medium", ["apps", "years"], [
 ("Skype", "2003", 2003), ("Zoom", "2013", 2013), ("Twitter", "2006", 2006), ("Tinder", "2012", 2012), ("WhatsApp", "2009", 2009), ("Snapchat", "2011", 2011)])
game("the year each poem was published", "Books", "hard", ["poems", "years"], [
 ("Wordsworth: Daffodils", "1807", 1807), ("T. S. Eliot: The Waste Land", "1922", 1922), ("Shelley: Ozymandias", "1818", 1818),
 ("Kipling: If—", "1910", 1910), ("Tennyson: The Charge of the Light Brigade", "1854", 1854), ("Lear: The Owl and the Pussy-cat", "1871", 1871)])
game("the year each party was founded", "Politics", "hard", ["parties", "years"], [
 ("The Conservatives", "1834", 1834), ("The Liberal Democrats", "1988", 1988), ("Labour", "1900", 1900),
 ("UKIP", "1993", 1993), ("Plaid Cymru", "1925", 1925), ("The SNP", "1934", 1934)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-14.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
