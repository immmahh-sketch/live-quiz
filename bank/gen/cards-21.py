# Bank session 10 Oct 2026: 20 more Play Your Cards Right games -> bank/cards-21.json. A row of 5-7 cards each:
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

game("the year each debut album came out", "Music", "medium", ["albums", "debuts", "years"], [
 ("Oasis: Definitely Maybe", "1994", 1994), ("Sam Fender: Hypersonic Missiles", "2019", 2019), ("Coldplay: Parachutes", "2000", 2000),
 ("Ed Sheeran: +", "2011", 2011), ("Amy Winehouse: Frank", "2003", 2003), ("Arctic Monkeys: Whatever People Say I Am, That's What I'm Not", "2006", 2006)])
game("the year each political show began", "Film and TV", "medium", ["politics", "TV", "years"], [
 ("Question Time", "1979", 1979), ("Mock the Week", "2005", 2005), ("Yes Minister", "1980", 1980), ("Have I Got News for You", "1990", 1990), ("Spitting Image", "1984", 1984)])
game("the year each cookery show began", "Food and drink", "medium", ["cooking", "TV", "years"], [
 ("MasterChef", "1990", 1990), ("Great British Menu", "2006", 2006), ("Ready Steady Cook", "1994", 1994),
 ("Come Dine with Me", "2005", 2005), ("The Naked Chef", "1999", 1999), ("Saturday Kitchen", "2002", 2002)])
game("the numbers in The Lord of the Rings", "Books", "medium", ["Tolkien", "numbers"], [
 ("Rings for the Elven-kings", "3", 3), ("Rings for mortal Men", "9", 9), ("The One Ring", "1", 1), ("Rings for the Dwarf-lords", "7", 7), ("Hobbits in the Fellowship", "4", 4)])
game("the year of each Northumbrian battle", "The North East", "hard", ["battles", "North East", "years"], [
 ("Neville's Cross, Durham", "1346", 1346), ("The siege of Newcastle", "1644", 1644), ("Otterburn", "1388", 1388),
 ("Flodden", "1513", 1513), ("Heavenfield", "634", 634)])
game("the year each gadget came out", "Science and technology", "medium", ["gadgets", "years"], [
 ("The Motorola DynaTAC, the first mobile phone", "1983", 1983), ("Amazon's Echo", "2014", 2014), ("The Segway", "2001", 2001),
 ("The Google Pixel", "2016", 2016), ("The Motorola Razr", "2004", 2004), ("The first Fitbit", "2009", 2009)])
game("how many on each TV show?", "Film and TV", "medium", ["game shows", "numbers"], [
 ("Hopefuls behind the screen on Blind Date", "3", 3), ("Contestants on the original Weakest Link", "9", 9), ("Strictly judges", "4", 4),
 ("Dragons in the first Dragons' Den", "5", 5), ("Players facing the Chaser", "4", 4)])
game("the year each wreck was found or raised", "History", "hard", ["shipwrecks", "years"], [
 ("The Vasa is raised in Stockholm", "1961", 1961), ("Shackleton's Endurance is found", "2022", 2022), ("The Mary Rose is raised", "1982", 1982),
 ("The Bismarck's wreck is found", "1989", 1989), ("The Titanic's wreck is found", "1985", 1985)])
game("the year of each football first", "Football", "hard", ["football history", "years"], [
 ("Today's offside rule (two defenders)", "1925", 1925), ("Goal-line technology in the Premier League", "2013", 2013), ("Numbered shirts in an FA Cup final", "1933", 1933),
 ("Names on shirts in the Premier League", "1993", 1993), ("The first league game under floodlights (Portsmouth v Newcastle)", "1956", 1956)])
game("the year of each space discovery", "Space", "hard", ["astronomy", "years"], [
 ("Uranus is found", "1781", 1781), ("Pluto is demoted to a dwarf planet", "2006", 2006), ("Ceres is found", "1801", 1801),
 ("The first planet round a Sun-like star", "1995", 1995), ("Neptune is found", "1846", 1846), ("Pluto is found", "1930", 1930)])
game("the year each cartoon series began", "Film and TV", "medium", ["cartoons", "years"], [
 ("The Flintstones", "1960", 1960), ("Bluey", "2018", 2018), ("Danger Mouse", "1981", 1981), ("Family Guy", "1999", 1999), ("South Park", "1997", 1997)])
game("the year of each first in women's sport", "Sport", "hard", ["women's sport", "years"], [
 ("The first Ladies' Wimbledon", "1884", 1884), ("The first women's Boat Race on the Thames tideway", "2015", 2015), ("The first women's Test match", "1934", 1934),
 ("Women's boxing at the Olympics", "2012", 2012), ("The first women's FA Cup final", "1971", 1971)])
game("the year of each North East transport first", "The North East", "hard", ["transport", "North East", "years"], [
 ("Newcastle Airport opens", "1935", 1935), ("The second Tyne Tunnel opens", "2011", 2011), ("The Metro reaches the airport", "1991", 1991),
 ("The Metro reaches Sunderland", "2002", 2002), ("Durham's railway viaduct opens", "1857", 1857)])
game("the year each scientist died", "Science and nature", "hard", ["scientists", "years"], [
 ("Galileo", "1642", 1642), ("Stephen Hawking", "2018", 2018), ("Isaac Newton", "1727", 1727), ("Albert Einstein", "1955", 1955), ("Charles Darwin", "1882", 1882), ("Marie Curie", "1934", 1934)])
game("the year each act won Eurovision", "Eurovision", "hard", ["Eurovision", "winners", "years"], [
 ("ABBA", "1974", 1974), ("Måneskin", "2021", 2021), ("Johnny Logan (his first)", "1980", 1980), ("Loreen (her first)", "2012", 2012), ("Céline Dion", "1988", 1988), ("Lordi", "2006", 2006)])
game("how many degrees?", "Maths and numbers", "medium", ["angles", "shapes"], [
 ("A corner of an equilateral triangle", "60", 60), ("A full turn", "360", 360), ("A right angle", "90", 90),
 ("A straight line", "180", 180), ("A corner of a regular hexagon", "120", 120), ("A corner of a regular octagon", "135", 135)])
game("how hot or cold, in °F?", "Science and nature", "medium", ["temperature", "Fahrenheit"], [
 ("Water freezes", "32°F", 32), ("Water boils", "212°F", 212), ("Where °C and °F are the same", "−40°F", -40), ("Normal body temperature", "98.6°F", 98.6), ("A hot summer's day of 30°C", "86°F", 86)])
game("the year each record label began", "Music", "hard", ["record labels", "years"], [
 ("Motown", "1959", 1959), ("Def Jam", "1984", 1984), ("Virgin Records", "1972", 1972), ("Factory Records", "1978", 1978), ("Stiff Records", "1976", 1976), ("Creation Records", "1983", 1983)])
game("the year each Saturday morning show began", "Nostalgia", "medium", ["children's TV", "Saturday", "years"], [
 ("Tiswas", "1974", 1974), ("SMTV Live", "1998", 1998), ("Multi-Coloured Swap Shop", "1976", 1976),
 ("Live & Kicking", "1993", 1993), ("Saturday Superstore", "1982", 1982), ("Going Live!", "1987", 1987)])
game("the year each dream car arrived", "Cars", "hard", ["cars", "years"], [
 ("The Jaguar E-Type", "1961", 1961), ("The Bugatti Veyron", "2005", 2005), ("The Ford GT40", "1964", 1964),
 ("The McLaren F1", "1992", 1992), ("The Lamborghini Countach", "1974", 1974), ("The DeLorean", "1981", 1981)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-21.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
