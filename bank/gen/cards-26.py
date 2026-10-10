# Bank session 10 Oct 2026: 20 more Play Your Cards Right games -> bank/cards-26.json. A row of 5-7 cards each:
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

game("the year each won the Nobel Peace Prize", "World history", "medium", ["Nobel Prize", "peace", "years"], [
 ("Martin Luther King", "1964", 1964), ("Barack Obama", "2009", 2009), ("Mother Teresa", "1979", 1979), ("Nelson Mandela", "1993", 1993), ("The Dalai Lama", "1989", 1989), ("Aung San Suu Kyi", "1991", 1991)])
game("the year of each World Cup hat-trick", "Football", "hard", ["World Cup", "hat-tricks", "years"], [
 ("Pelé against France", "1958", 1958), ("Kylian Mbappé in the final", "2022", 2022), ("Geoff Hurst in the final", "1966", 1966), ("Harry Kane against Panama", "2018", 2018), ("Gary Lineker against Poland", "1986", 1986)])
game("the year each ice cream arrived", "Food and drink", "hard", ["ice cream", "years"], [
 ("Wall's ice cream", "1922", 1922), ("Viennetta", "1982", 1982), ("Mr Whippy", "1958", 1958), ("Magnum", "1989", 1989), ("Häagen-Dazs", "1960", 1960), ("Ben & Jerry's", "1978", 1978)])
game("the numbers of a Rubik's Cube", "Games and toys", "medium", ["Rubik's Cube", "numbers"], [
 ("Corner pieces", "8", 8), ("Coloured stickers in all", "54", 54), ("Centre pieces", "6", 6), ("Edge pieces", "12", 12), ("Stickers on one face", "9", 9)])
game("the year each playground craze took off in Britain", "Nostalgia", "medium", ["crazes", "years"], [
 ("Slap bands", "1990", 1990), ("Fidget spinners", "2017", 2017), ("Pogs", "1995", 1995), ("Loom bands", "2014", 2014), ("Pokémon cards", "1999", 1999), ("Beyblades", "2002", 2002)])
game("the year each power station shut down", "Britain", "hard", ["power stations", "years"], [
 ("Bankside (now Tate Modern)", "1981", 1981), ("Ratcliffe-on-Soar, Britain's last coal plant", "2024", 2024), ("Battersea", "1983", 1983),
 ("Ferrybridge C", "2016", 2016), ("Blyth, Northumberland", "2001", 2001), ("Didcot A", "2013", 2013)])
game("the year of each moment in women's football", "Football", "hard", ["women's football", "years"], [
 ("Dick, Kerr Ladies draw 53,000 at Goodison", "1920", 1920), ("The first Women's World Cup", "1991", 1991), ("The FA bans women's football", "1921", 1921),
 ("Women's football joins the Olympics", "1996", 1996), ("England's first official women's international", "1972", 1972)])
game("the year each country joined NATO", "World history", "hard", ["NATO", "years"], [
 ("The UK (a founder)", "1949", 1949), ("Sweden", "2024", 2024), ("Turkey", "1952", 1952), ("Poland", "1999", 1999), ("West Germany", "1955", 1955), ("Spain", "1982", 1982)])
game("the year each brand changed its name", "Adverts and brands", "medium", ["rebrands", "years"], [
 ("Windscale becomes Sellafield", "1981", 1981), ("Norwich Union becomes Aviva", "2009", 2009), ("Marathon becomes Snickers", "1990", 1990),
 ("Dime becomes Daim", "2005", 2005), ("Opal Fruits become Starburst", "1998", 1998), ("Jif becomes Cif", "2001", 2001)])
game("the year each animal came back to Britain", "Animals", "hard", ["wildlife", "reintroductions", "years"], [
 ("Ospreys return to Scotland", "1954", 1954), ("Bison are released in Kent", "2022", 2022), ("White-tailed eagles are brought back", "1975", 1975),
 ("Beavers are trialled in Knapdale", "2009", 2009), ("Red kites are reintroduced", "1989", 1989), ("Great bustards are brought back", "2004", 2004)])
game("the year each game show ended (its first run)", "Film and TV", "hard", ["game shows", "years"], [
 ("3-2-1", "1988", 1988), ("Blind Date", "2003", 2003), ("Every Second Counts", "1993", 1993), ("The Generation Game", "2002", 2002), ("Bullseye", "1995", 1995), ("Telly Addicts", "1998", 1998)])
game("the year each North East drama began (part two)", "The North East", "hard", ["North East", "TV", "years"], [
 ("The Likely Lads", "1964", 1964), ("The Paradise", "2012", 2012), ("Whatever Happened to the Likely Lads?", "1973", 1973), ("55 Degrees North", "2004", 2004), ("Our Friends in the North", "1996", 1996)])
game("the year each games company was founded", "Games and toys", "hard", ["video games", "companies", "years"], [
 ("Atari", "1972", 1972), ("Rockstar Games", "1998", 1998), ("Electronic Arts", "1982", 1982), ("Valve", "1996", 1996), ("Rare", "1985", 1985), ("Ubisoft", "1986", 1986)])
game("the year each British car was launched", "Cars", "hard", ["British cars", "years"], [
 ("The Land Rover", "1948", 1948), ("The Austin Metro", "1980", 1980), ("The MGB", "1962", 1962), ("The Range Rover", "1970", 1970), ("The Aston Martin DB5", "1963", 1963), ("The Ford Capri", "1969", 1969)])
game("the year each famous photo was taken", "History", "hard", ["photographs", "years"], [
 ("Lunch atop a Skyscraper", "1932", 1932), ("The Pale Blue Dot", "1990", 1990), ("Migrant Mother", "1936", 1936),
 ("Afghan Girl", "1984", 1984), ("Earthrise", "1968", 1968), ("The Blue Marble", "1972", 1972)])
game("the year each country abolished the death penalty", "World history", "hard", ["law", "years"], [
 ("West Germany", "1949", 1949), ("South Africa", "1995", 1995), ("The UK, for murder", "1965", 1965), ("France", "1981", 1981), ("Australia", "1973", 1973), ("Canada", "1976", 1976)])
game("the year of each milestone for thinking machines", "Science and technology", "medium", ["computers", "AI", "years"], [
 ("Turing's 'imitation game' paper", "1950", 1950), ("AlphaGo beats Lee Sedol", "2016", 2016), ("ELIZA, the first chatbot", "1966", 1966),
 ("IBM's Watson wins Jeopardy!", "2011", 2011), ("Deep Blue beats Kasparov", "1997", 1997)])
game("the year of each famous newspaper headline", "History", "hard", ["headlines", "newspapers", "years"], [
 ("'Dewey Defeats Truman'", "1948", 1948), ("'Super Caley Go Ballistic, Celtic Are Atrocious'", "2000", 2000), ("'Gotcha'", "1982", 1982),
 ("'It's the Sun Wot Won It'", "1992", 1992), ("'Freddie Starr Ate My Hamster'", "1986", 1986), ("'Up Yours Delors'", "1990", 1990)])
game("the year each soap legend first appeared", "Film and TV", "hard", ["soaps", "characters", "years"], [
 ("Ken Barlow", "1960", 1960), ("Phil Mitchell", "1990", 1990), ("Rita Sullivan", "1964", 1964), ("Zak Dingle", "1994", 1994), ("Gail Platt", "1974", 1974), ("Dot Cotton", "1985", 1985)])
game("the year each dance craze took off", "Music", "medium", ["dance crazes", "years"], [
 ("The Twist", "1960", 1960), ("Vogue", "1990", 1990), ("The Loco-Motion", "1962", 1962), ("The Lambada", "1989", 1989), ("The Time Warp", "1973", 1973), ("The Hustle", "1975", 1975)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-26.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
