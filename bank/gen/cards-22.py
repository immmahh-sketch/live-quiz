# Bank session 10 Oct 2026: 20 more Play Your Cards Right games -> bank/cards-22.json. A row of 5-7 cards each:
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

game("the year each long-running show ended", "Film and TV", "hard", ["TV", "endings", "years"], [
 ("Crackerjack (the first run)", "1984", 1984), ("The Bill", "2010", 2010), ("Tomorrow's World", "2003", 2003), ("Grandstand", "2007", 2007), ("Top of the Pops, as a weekly show", "2006", 2006)])
game("the year each Briton won Olympic gold", "The Olympics", "medium", ["Team GB", "years"], [
 ("Daley Thompson (his first)", "1980", 1980), ("Tom Daley", "2021", 2021), ("Sally Gunnell", "1992", 1992),
 ("Jessica Ennis", "2012", 2012), ("Steve Redgrave (his fifth)", "2000", 2000), ("Kelly Holmes", "2004", 2004)])
game("the year each medical invention arrived", "Science and nature", "hard", ["medicine", "inventions", "years"], [
 ("The stethoscope", "1816", 1816), ("The first MRI scan of a person", "1977", 1977), ("Aspirin", "1897", 1897),
 ("The Pill on the NHS", "1961", 1961), ("The first implanted pacemaker", "1958", 1958)])
game("the year each biscuit arrived", "Food and drink", "hard", ["biscuits", "years"], [
 ("McVitie's Digestive", "1892", 1892), ("Hobnobs", "1985", 1985), ("The Custard Cream", "1908", 1908),
 ("Jammie Dodgers", "1960", 1960), ("Jaffa Cakes", "1927", 1927), ("Wagon Wheels", "1948", 1948)])
game("the year each clothes shop began", "Fashion", "hard", ["shops", "fashion", "years"], [
 ("Topshop", "1964", 1964), ("Superdry", "2003", 2003), ("Zara", "1975", 1975), ("ASOS", "2000", 2000), ("Next", "1982", 1982), ("River Island, by that name", "1988", 1988)])
game("the year of each daredevil moment", "History", "hard", ["daredevils", "years"], [
 ("Blondin crosses Niagara on a tightrope", "1859", 1859), ("Felix Baumgartner jumps from the edge of space", "2012", 2012), ("Evel Knievel's Caesars Palace jump", "1967", 1967),
 ("Eddie the Eagle at the Winter Olympics", "1988", 1988), ("Philippe Petit walks between the Twin Towers", "1974", 1974)])
game("the year each Poet Laureate was appointed", "Books", "hard", ["poets", "years"], [
 ("William Wordsworth", "1843", 1843), ("Simon Armitage", "2019", 2019), ("Alfred, Lord Tennyson", "1850", 1850),
 ("Carol Ann Duffy", "2009", 2009), ("John Betjeman", "1972", 1972), ("Ted Hughes", "1984", 1984)])
game("the numbers on a Monopoly board", "Games and toys", "medium", ["Monopoly", "numbers"], [
 ("Stations", "4", 4), ("Properties to buy (not counting stations and utilities)", "22", 22), ("Utilities", "2", 2), ("Chance cards", "16", 16), ("Colour sets", "8", 8)])
game("the year each BBC One favourite began", "Film and TV", "medium", ["BBC", "years"], [
 ("Songs of Praise", "1961", 1961), ("The One Show", "2006", 2006), ("Gardeners' World", "1968", 1968),
 ("Countryfile", "1988", 1988), ("Antiques Roadshow", "1979", 1979), ("Crimewatch", "1984", 1984)])
game("the famous number in each", "General knowledge", "medium", ["numbers"], [
 ("The Hogwarts Express platform", "9¾", 9.75), ("The number of the beast", "666", 666), ("The Prisoner's number", "6", 6),
 ("The answer to life, the universe and everything", "42", 42), ("The luckiest number in China", "8", 8)])
game("the year of each great crossing", "History", "hard", ["voyages", "years"], [
 ("Matthew Webb swims the Channel", "1875", 1875), ("Ellen MacArthur's round-the-world record", "2005", 2005), ("Francis Chichester sails home", "1967", 1967),
 ("The first balloon across the Atlantic", "1978", 1978), ("Blériot flies across the Channel", "1909", 1909)])
game("how many bones in each?", "The human body", "hard", ["bones", "body"], [
 ("The middle ear", "3", 3), ("The spine", "33", 33), ("The skull", "22", 22), ("One hand and wrist", "27", 27), ("One foot and ankle", "26", 26)])
game("how many films in each franchise?", "Film", "hard", ["film series", "numbers"], [
 ("Police Academy", "7", 7), ("Carry On", "31", 31), ("Indiana Jones", "5", 5), ("James Bond (the official ones)", "25", 25), ("Jurassic Park and Jurassic World", "7", 7)])
game("the year of each Christmas advert", "Christmas", "hard", ["adverts", "Christmas", "years"], [
 ("Coca-Cola: Holidays Are Coming", "1995", 1995), ("Aldi: Kevin the Carrot", "2016", 2016), ("John Lewis: The Long Wait", "2011", 2011),
 ("John Lewis: Monty the Penguin", "2014", 2014), ("John Lewis: The Bear and the Hare", "2013", 2013)])
game("the year each era ended", "British history", "medium", ["endings", "years"], [
 ("The last steam train on British Rail", "1968", 1968), ("Kellingley, the last deep coal mine, closes", "2015", 2015), ("The last £1 note in England", "1988", 1988),
 ("The last classic Mini", "2000", 2000), ("The last Routemaster on a regular route", "2005", 2005)])
game("the year each game came out", "Games and toys", "medium", ["video games", "apps", "years"], [
 ("FIFA (the first one)", "1993", 1993), ("Wordle", "2021", 2021), ("The Sims", "2000", 2000), ("Pokémon Go", "2016", 2016), ("Angry Birds", "2009", 2009), ("Candy Crush", "2012", 2012)])
game("the year each London museum opened", "London", "hard", ["museums", "years"], [
 ("The British Museum", "1759", 1759), ("The Museum of London", "1976", 1976), ("The V&A", "1852", 1852), ("The Imperial War Museum (founded)", "1917", 1917), ("The Natural History Museum", "1881", 1881)])
game("the year of each London travel change", "London", "medium", ["transport", "years"], [
 ("The Travelcard", "1983", 1983), ("The ULEZ", "2019", 2019), ("The Oyster card", "2003", 2003), ("'Boris bikes'", "2010", 2010), ("The Night Tube", "2016", 2016)])
game("the year each punk or new wave single came out", "Music", "hard", ["punk", "singles", "years"], [
 ("Sex Pistols: Anarchy in the UK", "1976", 1976), ("New Order: Blue Monday", "1983", 1983), ("Sex Pistols: God Save the Queen", "1977", 1977),
 ("Joy Division: Love Will Tear Us Apart", "1980", 1980), ("Buzzcocks: Ever Fallen in Love", "1978", 1978), ("The Clash: London Calling", "1979", 1979)])
game("the numbers in American football", "Sport", "medium", ["NFL", "scoring"], [
 ("Points for a touchdown", "6", 6), ("Points for the kick after", "1", 1), ("Points for a field goal", "3", 3), ("Points for a safety", "2", 2), ("Players on the field per team", "11", 11)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-22.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
