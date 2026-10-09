# Bank session 10 Oct 2026: 20 more Play Your Cards Right games -> bank/cards-17.json. A row of 5-7 cards each:
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

game("the year each boy band formed", "Boy bands and girl groups", "medium", ["boy bands", "years"], [
 ("Boyzone", "1993", 1993), ("One Direction", "2010", 2010), ("Westlife", "1998", 1998), ("BTS", "2013", 2013), ("Busted", "2000", 2000), ("JLS", "2007", 2007)])
game("the year each girl group formed", "Boy bands and girl groups", "medium", ["girl groups", "years"], [
 ("Bananarama", "1980", 1980), ("Little Mix", "2011", 2011), ("All Saints", "1993", 1993), ("Girls Aloud", "2002", 2002), ("The Spice Girls", "1994", 1994), ("Sugababes", "1998", 1998)])
game("the year each comedian died", "Comedy", "hard", ["comedians", "years"], [
 ("Tommy Cooper", "1984", 1984), ("Victoria Wood", "2016", 2016), ("Kenneth Williams", "1988", 1988),
 ("Ronnie Barker", "2005", 2005), ("Les Dawson", "1993", 1993), ("Spike Milligan", "2002", 2002)])
game("the year each came to Britain's roads", "Driving", "hard", ["roads", "years"], [
 ("The first traffic lights", "1868", 1868), ("Speed cameras", "1992", 1992), ("The compulsory driving test", "1935", 1935), ("Zebra crossings", "1951", 1951), ("The Highway Code", "1931", 1931)])
game("the year of each famous FA Cup final", "Football", "hard", ["FA Cup", "finals", "years"], [
 ("The Matthews final", "1953", 1953), ("Wigan beat Manchester City", "2013", 2013), ("Ricky Villa's wonder goal", "1981", 1981),
 ("The Gerrard final", "2006", 2006), ("Wimbledon's Crazy Gang beat Liverpool", "1988", 1988), ("Newcastle lose to Man Utd", "1999", 1999)])
game("the year of each British invention", "Science and technology", "hard", ["inventions", "years"], [
 ("Budding's lawnmower", "1830", 1830), ("The Dyson bagless vacuum", "1993", 1993), ("Whittle's jet engine patent", "1930", 1930),
 ("The hovercraft crosses the Channel", "1959", 1959), ("Stainless steel", "1913", 1913)])
game("the year each dance-along hit came out", "Music", "medium", ["party songs", "years"], [
 ("Village People: YMCA", "1978", 1978), ("PSY: Gangnam Style", "2012", 2012), ("Black Lace: Agadoo", "1984", 1984),
 ("Las Ketchup: The Ketchup Song", "2002", 2002), ("Whigfield: Saturday Night", "1994", 1994), ("Los del Río: Macarena", "1996", 1996)])
game("the year each games console came out", "Games and toys", "medium", ["consoles", "years"], [
 ("The Game Boy", "1989", 1989), ("The PlayStation 5", "2020", 2020), ("The PlayStation 2", "2000", 2000),
 ("The Nintendo Switch", "2017", 2017), ("The Xbox 360", "2005", 2005), ("The Wii", "2006", 2006)])
game("the year each university was founded", "Education", "hard", ["universities", "years"], [
 ("Oxford", "about 1096", 1096), ("The Open University", "1969", 1969), ("Cambridge", "1209", 1209),
 ("Durham", "1832", 1832), ("St Andrews", "1413", 1413), ("University College London", "1826", 1826)])
game("the year of each sea battle", "History", "hard", ["navy", "battles", "years"], [
 ("The Spanish Armada", "1588", 1588), ("The Bismarck is sunk", "1941", 1941), ("The Battle of the Nile", "1798", 1798),
 ("Jutland", "1916", 1916), ("The Battle of the River Plate", "1939", 1939)])
game("the year of each ground's last game", "Football", "hard", ["stadiums", "years"], [
 ("Ayresome Park, Middlesbrough", "1995", 1995), ("White Hart Lane", "2017", 2017), ("Roker Park, Sunderland", "1997", 1997),
 ("Upton Park", "2016", 2016), ("The old Wembley", "2000", 2000), ("Highbury", "2006", 2006)])
game("the year each comic character first appeared", "Nostalgia", "hard", ["comics", "years"], [
 ("Tintin", "1929", 1929), ("Judge Dredd", "1977", 1977), ("Desperate Dan", "1937", 1937),
 ("Andy Capp (from Hartlepool)", "1957", 1957), ("Dennis the Menace", "1951", 1951), ("Minnie the Minx", "1953", 1953)])
game("how many letters in each place name?", "Britain", "medium", ["place names", "letters"], [
 ("Ely", "3", 3), ("Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch", "58", 58), ("Edinburgh", "9", 9),
 ("Newcastle upon Tyne, not counting spaces", "17", 17), ("Sunderland", "10", 10), ("Wolverhampton", "13", 13)])
game("the year of each RAF moment", "History", "hard", ["RAF", "years"], [
 ("The RAF is founded", "1918", 1918), ("The Harrier jump jet enters service", "1969", 1969), ("The Spitfire's first flight", "1936", 1936),
 ("The Red Arrows are formed", "1965", 1965), ("The Dambusters raid", "1943", 1943)])
game("the year each North East figure was born", "The North East", "hard", ["North East", "history", "years"], [
 ("Captain James Cook", "1728", 1728), ("Grace Darling", "1815", 1815), ("Thomas Bewick", "1753", 1753),
 ("Lord Armstrong", "1810", 1810), ("Earl Grey", "1764", 1764), ("George Stephenson", "1781", 1781)])
game("gold medals at Paris 2024", "The Olympics", "hard", ["Olympics", "Paris 2024"], [
 ("Ireland", "4", 4), ("The USA", "40", 40), ("Team GB", "14", 14), ("Japan", "20", 20), ("The Netherlands", "15", 15), ("Australia", "18", 18)])
game("the year each railway station opened", "Trains", "hard", ["stations", "years"], [
 ("Euston", "1837", 1837), ("York (today's station)", "1877", 1877), ("Waterloo", "1848", 1848),
 ("St Pancras", "1868", 1868), ("King's Cross", "1852", 1852), ("Paddington (today's station)", "1854", 1854)])
game("how many zeros in each?", "Maths and numbers", "medium", ["numbers", "zeros"], [
 ("A million", "6", 6), ("A googol", "100", 100), ("A thousand", "3", 3), ("A trillion", "12", 12), ("A hundred", "2", 2), ("A billion", "9", 9)])
game("the year each leader died", "World history", "hard", ["leaders", "years"], [
 ("Napoleon", "1821", 1821), ("Margaret Thatcher", "2013", 2013), ("Abraham Lincoln", "1865", 1865), ("Joseph Stalin", "1953", 1953), ("Mahatma Gandhi", "1948", 1948)])
game("the year each ITV drama began", "Film and TV", "medium", ["ITV", "drama", "years"], [
 ("Emmerdale Farm", "1972", 1972), ("Downton Abbey", "2010", 2010), ("The Bill", "1984", 1984),
 ("Cold Feet", "1997", 1997), ("Prime Suspect", "1991", 1991), ("Heartbeat", "1992", 1992)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-17.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
