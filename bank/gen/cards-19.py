# Bank session 10 Oct 2026: 20 more Play Your Cards Right games -> bank/cards-19.json. A row of 5-7 cards each:
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

game("the year each comedy character first appeared", "Comedy", "medium", ["comedy", "characters", "years"], [
 ("Basil Fawlty", "1975", 1975), ("David Brent", "2001", 2001), ("Del Boy", "1981", 1981), ("Ali G", "1998", 1998), ("Edmund Blackadder", "1983", 1983), ("Mr. Bean", "1990", 1990)])
game("the year each sitcom ended", "Comedy", "hard", ["sitcoms", "years"], [
 ("Dad's Army", "1977", 1977), ("Friends", "2004", 2004), ("Fawlty Towers", "1979", 1979), ("Seinfeld", "1998", 1998), ("Blackadder Goes Forth", "1989", 1989), ("Cheers", "1993", 1993)])
game("the year each pier opened", "Britain", "hard", ["seaside", "piers", "years"], [
 ("Blackpool's North Pier", "1863", 1863), ("Brighton Palace Pier", "1899", 1899), ("Brighton's West Pier", "1866", 1866), ("Llandudno Pier", "1877", 1877), ("Saltburn Pier", "1869", 1869)])
game("the year each country took its new name", "World geography", "hard", ["countries", "names", "years"], [
 ("Persia becomes Iran", "1935", 1935), ("Swaziland becomes Eswatini", "2018", 2018), ("Siam becomes Thailand", "1939", 1939),
 ("Burma becomes Myanmar", "1989", 1989), ("Ceylon becomes Sri Lanka", "1972", 1972), ("Rhodesia becomes Zimbabwe", "1980", 1980)])
game("the year each city took its new name", "World geography", "hard", ["cities", "names", "years"], [
 ("Constantinople becomes Istanbul", "1930", 1930), ("Madras becomes Chennai", "1996", 1996), ("Saigon becomes Ho Chi Minh City", "1976", 1976),
 ("Leningrad becomes St Petersburg", "1991", 1991), ("Bombay becomes Mumbai", "1995", 1995)])
game("the year each sporting great died", "Sport", "medium", ["sport", "years"], [
 ("Bobby Moore", "1993", 1993), ("Pelé", "2022", 2022), ("Ayrton Senna", "1994", 1994), ("Muhammad Ali", "2016", 2016), ("George Best", "2005", 2005), ("Seve Ballesteros", "2011", 2011)])
game("the year each castle was begun", "History", "hard", ["castles", "years"], [
 ("Warwick Castle", "1068", 1068), ("Neuschwanstein", "1869", 1869), ("Leeds Castle", "1119", 1119),
 ("Highclere Castle (today's)", "1842", 1842), ("Dover's Great Tower", "about 1181", 1181), ("Caernarfon Castle", "1283", 1283)])
game("how many players per team?", "Sport", "medium", ["team sizes"], [
 ("Polo", "4", 4), ("Hurling", "15", 15), ("Volleyball", "6", 6), ("Men's field lacrosse", "10", 10), ("Water polo", "7", 7), ("Tug of war", "8", 8)])
game("the year each emergency service began", "British history", "hard", ["emergency services", "years"], [
 ("The Metropolitan Police", "1829", 1829), ("The first UK air ambulance", "1987", 1987), ("London's fire brigade", "1866", 1866),
 ("The 999 number", "1937", 1937), ("Neighbourhood Watch in the UK", "1982", 1982)])
game("the year each theatre opened", "Theatre", "hard", ["theatres", "years"], [
 ("The Theatre Royal, Newcastle", "1837", 1837), ("The new Globe", "1997", 1997), ("The Royal Opera House (today's)", "1858", 1858),
 ("The National Theatre on the South Bank", "1976", 1976), ("The London Palladium", "1910", 1910)])
game("the numbers in lottery games", "Games and toys", "hard", ["lottery", "bingo", "numbers"], [
 ("Main balls drawn in Lotto", "6", 6), ("Balls in a bingo game", "90", 90), ("EuroMillions Lucky Stars to pick from", "12", 12),
 ("Lotto numbers to pick from", "59", 59), ("Thunderball main numbers", "39", 39), ("EuroMillions main numbers", "50", 50)])
game("the year each gallery opened", "Art", "hard", ["galleries", "years"], [
 ("The Louvre", "1793", 1793), ("Tate Modern", "2000", 2000), ("The National Gallery", "1824", 1824),
 ("The Guggenheim, Bilbao", "1997", 1997), ("Tate Britain", "1897", 1897), ("The Laing, Newcastle", "1904", 1904)])
game("how many years between each?", "General knowledge", "medium", ["cycles", "years"], [
 ("Ryder Cups", "2", 2), ("Sightings of Halley's Comet", "about 76", 76), ("General elections, at most", "5", 5), ("UK censuses", "10", 10), ("World Cups", "4", 4)])
game("the year of each Nobel Prize", "Science and nature", "hard", ["Nobel Prize", "years"], [
 ("Marie Curie (her first)", "1903", 1903), ("Malala Yousafzai", "2014", 2014), ("Albert Einstein", "1921", 1921),
 ("Peter Higgs", "2013", 2013), ("Alexander Fleming", "1945", 1945), ("Watson and Crick", "1962", 1962)])
game("the year each music format arrived", "Music", "hard", ["formats", "years"], [
 ("The vinyl LP", "1948", 1948), ("The first MP3 player", "1998", 1998), ("The compact cassette", "1963", 1963), ("VHS", "1976", 1976), ("The 8-track cartridge", "1965", 1965)])
game("the year each became a World Heritage Site", "Britain", "hard", ["World Heritage", "years"], [
 ("Durham Cathedral and Castle", "1986", 1986), ("The Lake District", "2017", 2017), ("Hadrian's Wall", "1987", 1987), ("Kew Gardens", "2003", 2003), ("The Jurassic Coast", "2001", 2001)])
game("the year each was knighted", "Famous people", "hard", ["knighthoods", "years"], [
 ("David Attenborough", "1985", 1985), ("Kenny Dalglish", "2018", 2018), ("Paul McCartney", "1997", 1997),
 ("Bobby Robson", "2002", 2002), ("Elton John", "1998", 1998), ("Alex Ferguson", "1999", 1999)])
game("the year each London bridge opened", "London", "hard", ["bridges", "London", "years"], [
 ("Westminster Bridge (today's)", "1862", 1862), ("The Millennium Bridge", "2000", 2000), ("Albert Bridge", "1873", 1873),
 ("London Bridge (today's)", "1973", 1973), ("Hammersmith Bridge", "1887", 1887), ("Waterloo Bridge (today's)", "1945", 1945)])
game("how many musicians in each?", "Classical music", "easy", ["music", "ensembles"], [
 ("A trio", "3", 3), ("An octet", "8", 8), ("A duet", "2", 2), ("A septet", "7", 7), ("A quartet", "4", 4), ("A quintet", "5", 5)])
game("the year each dog film came out", "Film", "medium", ["dogs", "films", "years"], [
 ("Lassie Come Home", "1943", 1943), ("Isle of Dogs", "2018", 2018), ("Lady and the Tramp", "1955", 1955),
 ("Marley & Me", "2008", 2008), ("Turner & Hooch", "1989", 1989), ("Beethoven", "1992", 1992)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-19.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
