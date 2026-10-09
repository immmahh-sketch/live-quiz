# Bank session 10 Oct 2026: 20 more Play Your Cards Right games -> bank/cards-12.json. A row of 5-7 cards each:
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

game("the year each reality show began", "Film and TV", "medium", ["reality TV", "years"], [
 ("Big Brother", "2000", 2000), ("Love Island", "2015", 2015), ("I'm a Celebrity...", "2002", 2002),
 ("Gogglebox", "2013", 2013), ("The Apprentice", "2005", 2005), ("Britain's Got Talent", "2007", 2007)])
game("how many books in each series?", "Books", "hard", ["books", "series"], [
 ("The Hunger Games (the first run)", "3", 3), ("Discworld", "41", 41), ("Twilight", "4", 4),
 ("Harry Potter", "7", 7), ("A Song of Ice and Fire (so far)", "5", 5), ("The Chronicles of Narnia", "7", 7)])
game("the year each British film came out", "Film", "medium", ["British films", "years"], [
 ("Get Carter (filmed on Tyneside)", "1971", 1971), ("Love Actually", "2003", 2003), ("Four Weddings and a Funeral", "1994", 1994),
 ("Billy Elliot", "2000", 2000), ("Trainspotting", "1996", 1996), ("Notting Hill", "1999", 1999)])
game("the number in each film title", "Film", "easy", ["films", "numbers"], [
 ("Around the World in ___ Days", "80", 80), ("(___) Days of Summer", "500", 500), ("How to Lose a Guy in ___ Days", "10", 10),
 ("___ Hours", "127", 127), ("___ First Dates", "50", 50)])
game("how many in each game box?", "Games and toys", "medium", ["board games", "numbers"], [
 ("Wedges to win Trivial Pursuit", "6", 6), ("Cards in a pack of Uno", "108", 108), ("Rooms in Cluedo", "9", 9),
 ("Blocks in Jenga", "54", 54), ("Faces in Guess Who?", "24", 24), ("Houses in Monopoly", "32", 32)])
game("the year each British singer was born", "Music", "medium", ["singers", "birthdays", "years"], [
 ("Shirley Bassey", "1937", 1937), ("Ed Sheeran", "1991", 1991), ("Tom Jones", "1940", 1940),
 ("Dua Lipa", "1995", 1995), ("Elton John", "1947", 1947), ("Robbie Williams", "1974", 1974)])
game("the year each canal or dam was finished", "Engineering", "hard", ["canals", "dams", "years"], [
 ("The Suez Canal", "1869", 1869), ("The Thames Barrier", "1982", 1982), ("The Manchester Ship Canal", "1894", 1894),
 ("The Hoover Dam", "1936", 1936), ("The Panama Canal", "1914", 1914)])
game("where is each letter in the alphabet?", "Words and language", "easy", ["alphabet", "letters"], [
 ("M", "13th", 13), ("Z", "26th", 26), ("E", "5th", 5), ("T", "20th", 20), ("A", "1st", 1), ("Q", "17th", 17)])
game("the year each TV first arrived", "Film and TV", "hard", ["television", "years"], [
 ("Colour TV in Britain", "1967", 1967), ("BBC iPlayer", "2007", 2007), ("Ceefax", "1974", 1974),
 ("The end of analogue TV", "2012", 2012), ("Sky+", "2001", 2001), ("Freeview", "2002", 2002)])
game("the year of each famous crime", "History", "hard", ["crime", "years"], [
 ("The Gunpowder Plot", "1605", 1605), ("The Hatton Garden raid", "2015", 2015), ("Colonel Blood steals the Crown Jewels", "1671", 1671),
 ("The Brink's-Mat robbery", "1983", 1983), ("The Mona Lisa is stolen", "1911", 1911), ("The Great Train Robbery", "1963", 1963)])
game("the year of each famous animal moment", "Animals", "hard", ["animals", "years"], [
 ("The last dodo is seen", "about 1662", 1662), ("Paul the Octopus picks the World Cup winners", "2010", 2010), ("Greyfriars Bobby dies", "1872", 1872),
 ("Lonesome George the tortoise dies", "2012", 2012), ("Laika the dog goes into space", "1957", 1957)])
game("the year each toy company began", "Games and toys", "hard", ["toys", "companies", "years"], [
 ("Hamleys", "1760", 1760), ("Mattel", "1945", 1945), ("Hasbro", "1923", 1923), ("Airfix", "1939", 1939), ("Fisher-Price", "1930", 1930), ("Lego", "1932", 1932)])
game("the year each food first went on sale", "Food and drink", "hard", ["food", "years"], [
 ("Marmite", "1902", 1902), ("Pot Noodle", "1979", 1979), ("Bisto", "1908", 1908),
 ("Monster Munch", "1977", 1977), ("Walkers crisps", "1948", 1948), ("Hula Hoops", "1973", 1973)])
game("the year each Tyne or Wear bridge opened", "The North East", "hard", ["bridges", "North East", "years"], [
 ("The High Level Bridge", "1849", 1849), ("The Gateshead Millennium Bridge", "2001", 2001), ("The King Edward VII Bridge", "1906", 1906),
 ("The Redheugh Bridge (today's)", "1983", 1983), ("The Wearmouth Bridge (today's)", "1929", 1929), ("The Queen Elizabeth II Metro Bridge", "1981", 1981)])
game("the number in each famous name", "General knowledge", "easy", ["numbers", "names"], [
 ("Route ___", "66", 66), ("Air Force ___", "One", 1), ("Area ___", "51", 51), ("Agent 00___", "7", 7), ("Studio ___", "54", 54), ("Apollo ___ (the first Moon landing)", "11", 11)])
game("the year each TV soap or drama ended", "Film and TV", "hard", ["soaps", "years"], [
 ("Crossroads (the first run)", "1988", 1988), ("Doctors", "2024", 2024), ("Howards' Way", "1990", 1990),
 ("Neighbours (the first ending)", "2022", 2022), ("Brookside", "2003", 2003), ("Grange Hill", "2008", 2008)])
game("how many teams in each league?", "Sport", "medium", ["leagues", "teams"], [
 ("The Scottish Premiership", "12", 12), ("The NFL", "32", 32), ("The Bundesliga", "18", 18),
 ("The Championship", "24", 24), ("The Premier League", "20", 20), ("The NBA", "30", 30)])
game("how many years did each war last?", "History", "hard", ["wars", "lengths"], [
 ("The First World War", "4", 4), ("The Hundred Years' War", "116", 116), ("The Second World War", "6", 6),
 ("The Wars of the Roses", "32", 32), ("The Thirty Years' War", "30", 30)])
game("the year each music venue opened", "Music", "hard", ["venues", "years"], [
 ("The Royal Albert Hall", "1871", 1871), ("The O2 arena", "2007", 2007), ("Newcastle City Hall", "1927", 1927),
 ("The Cavern Club", "1957", 1957), ("Wembley Arena (as the Empire Pool)", "1934", 1934)])
game("the year each national park was created", "Britain", "hard", ["national parks", "years"], [
 ("The Peak District", "1951", 1951), ("The South Downs", "2010", 2010), ("The North York Moors", "1952", 1952),
 ("The Cairngorms", "2003", 2003), ("Northumberland", "1956", 1956), ("The New Forest", "2005", 2005)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-12.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
