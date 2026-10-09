# Bank session 10 Oct 2026: 20 more Play Your Cards Right games -> bank/cards-7.json. A row of 5-7 cards each:
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

game("the year each album came out", "Music", "medium", ["albums", "years"], [
 ("Pink Floyd: The Dark Side of the Moon", "1973", 1973), ("Amy Winehouse: Back to Black", "2006", 2006), ("Fleetwood Mac: Rumours", "1977", 1977),
 ("Adele: 21", "2011", 2011), ("Michael Jackson: Thriller", "1982", 1982), ("Oasis: (What's the Story) Morning Glory?", "1995", 1995)])
game("how many in each famous set?", "Myths and legends", "hard", ["myths", "numbers"], [
 ("Horsemen of the Apocalypse", "4", 4), ("Labours of Hercules", "12", 12), ("Pillars of Islam", "5", 5), ("Muses in Greek myth", "9", 9), ("Wonders of the Ancient World", "7", 7)])
game("the year each TV channel launched", "Film and TV", "medium", ["TV channels", "years"], [
 ("BBC Television (now BBC One)", "1936", 1936), ("Channel 5", "1997", 1997), ("ITV", "1955", 1955),
 ("Sky Television", "1989", 1989), ("BBC Two", "1964", 1964), ("Channel 4", "1982", 1982)])
game("England caps won", "Football", "hard", ["England", "caps"], [
 ("Bobby Charlton", "106", 106), ("Peter Shilton", "125", 125), ("Ashley Cole", "107", 107), ("Wayne Rooney", "120", 120), ("Bobby Moore", "108", 108), ("David Beckham", "115", 115)])
game("England goals scored", "Football", "hard", ["England", "goals"], [
 ("Alan Shearer", "30", 30), ("Wayne Rooney", "53", 53), ("Michael Owen", "40", 40), ("Bobby Charlton", "49", 49), ("Jimmy Greaves", "44", 44), ("Gary Lineker", "48", 48)])
game("how many states, provinces or counties?", "World geography", "hard", ["countries", "regions"], [
 ("States of Australia", "6", 6), ("States of the USA", "50", 50), ("Provinces of Canada", "10", 10),
 ("States of India", "28", 28), ("States of Germany", "16", 16), ("Counties on the island of Ireland", "32", 32)])
game("the year each country joined the EU (or the EEC)", "Europe", "hard", ["EU", "years"], [
 ("Greece", "1981", 1981), ("Croatia", "2013", 2013), ("The United Kingdom", "1973", 1973), ("Poland", "2004", 2004), ("Spain", "1986", 1986), ("Sweden", "1995", 1995)])
game("the year each video game came out", "Games and toys", "medium", ["video games", "years"], [
 ("Space Invaders", "1978", 1978), ("Fortnite", "2017", 2017), ("Pac-Man", "1980", 1980),
 ("Grand Theft Auto V", "2013", 2013), ("Tetris", "1984", 1984), ("Pokémon Red and Green", "1996", 1996)])
game("Formula One race wins, up to 2025", "Motor sport", "hard", ["F1", "wins"], [
 ("Jenson Button", "15", 15), ("Lewis Hamilton", "105", 105), ("Damon Hill", "22", 22), ("Michael Schumacher", "91", 91), ("Nigel Mansell", "31", 31), ("Ayrton Senna", "41", 41)])
game("Formula One world titles", "Motor sport", "medium", ["F1", "champions"], [
 ("Nigel Mansell", "1", 1), ("Lewis Hamilton", "7", 7), ("Ayrton Senna", "3", 3), ("Juan Manuel Fangio", "5", 5), ("Jenson Button", "1", 1), ("Alain Prost", "4", 4)])
game("how many in each story?", "Books", "easy", ["stories", "numbers"], [
 ("Cinderella's stepsisters", "2", 2), ("The Bennet sisters in Pride and Prejudice", "5", 5), ("The little pigs", "3", 3),
 ("Willy Wonka's golden tickets", "5", 5), ("The March sisters in Little Women", "4", 4)])
game("how many times was each made Prime Minister?", "British history", "hard", ["Prime Ministers"], [
 ("Margaret Thatcher", "1", 1), ("William Gladstone", "4", 4), ("Winston Churchill", "2", 2), ("Stanley Baldwin", "3", 3), ("Harold Wilson", "2", 2)])
game("the year of each North East invention", "The North East", "hard", ["inventions", "North East", "years"], [
 ("George Stephenson's 'Geordie' safety lamp", "1815", 1815), ("Turbinia, the turbine-powered ship, is launched", "1894", 1894),
 ("John Walker of Stockton invents the friction match", "1826", 1826), ("Charles Parsons' steam turbine", "1884", 1884),
 ("Cragside, the first house lit by hydroelectricity", "1878", 1878), ("Joseph Swan shows his light bulb in Newcastle", "1879", 1879)])
game("the year each cartoon star first appeared", "Film and TV", "medium", ["cartoons", "years"], [
 ("Mickey Mouse", "1928", 1928), ("Peppa Pig", "2004", 2004), ("Bugs Bunny", "1940", 1940),
 ("SpongeBob SquarePants", "1999", 1999), ("Scooby-Doo", "1969", 1969), ("The Simpsons, as a series", "1989", 1989)])
game("how many letters in each alphabet?", "Words and language", "hard", ["alphabets", "languages"], [
 ("Hebrew", "22", 22), ("Russian", "33", 33), ("Greek", "24", 24), ("Arabic", "28", 28), ("Italian", "21", 21), ("English", "26", 26)])
game("the year each royal was born", "The royal family", "easy", ["royals", "birthdays", "years"], [
 ("King Charles III", "1948", 1948), ("Prince George", "2013", 2013), ("Princess Anne", "1950", 1950),
 ("Princess Charlotte", "2015", 2015), ("Prince William", "1982", 1982), ("Prince Harry", "1984", 1984)])
game("the number in the song title", "Music", "medium", ["songs", "numbers"], [
 ("Nena: '___ Red Balloons'", "99", 99), ("Paul Hardcastle: '___'", "19", 19), ("The Proclaimers: '___ Miles'", "500", 500),
 ("Youssou N'Dour and Neneh Cherry: '___ Seconds'", "7", 7), ("Bryan Adams: 'Summer of '___'", "69", 69), ("Taylor Swift: '___'", "22", 22)])
game("how long is each, in metres?", "Sport", "hard", ["pitches", "measurements"], [
 ("A cricket pitch", "20.12 m", 20.12), ("The pitch at Wembley", "105 m", 105), ("A badminton court", "13.4 m", 13.4),
 ("An Olympic swimming pool", "50 m", 50), ("A tennis court", "23.77 m", 23.77), ("A basketball court", "28 m", 28)])
game("the year each horse won the Grand National", "Horse racing", "hard", ["Grand National", "years"], [
 ("Foinavon", "1967", 1967), ("Minella Times, with Rachael Blackmore", "2021", 2021), ("Red Rum (first win)", "1973", 1973),
 ("Tiger Roll (first win)", "2018", 2018), ("Aldaniti", "1981", 1981), ("Mr Frisk", "1990", 1990)])
game("the year of each first", "Music", "medium", ["festivals", "years"], [
 ("The first Isle of Wight Festival", "1968", 1968), ("The first Download festival", "2003", 2003), ("The first Glastonbury", "1970", 1970),
 ("The first Leeds Festival", "1999", 1999), ("Live Aid", "1985", 1985), ("The first Creamfields", "1998", 1998)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-7.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
