# Bank session 10 Oct 2026: 20 more Play Your Cards Right games -> bank/cards-18.json. A row of 5-7 cards each:
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

game("the year each Best Picture winner came out", "The Oscars and award winners", "medium", ["Oscars", "films", "years"], [
 ("Casablanca", "1942", 1942), ("Oppenheimer", "2023", 2023), ("The Godfather", "1972", 1972),
 ("Slumdog Millionaire", "2008", 2008), ("Forrest Gump", "1994", 1994), ("Gladiator", "2000", 2000)])
game("the year of each famous goal", "Football", "medium", ["goals", "years"], [
 ("Maradona's 'Hand of God'", "1986", 1986), ("Rooney's overhead kick against City", "2011", 2011), ("Beckham from the halfway line", "1996", 1996),
 ("Bergkamp's spin and finish at St James' Park", "2002", 2002), ("Michael Owen's solo goal against Argentina", "1998", 1998)])
game("the year of each big fight", "Boxing", "hard", ["boxing", "years"], [
 ("Henry Cooper floors Cassius Clay", "1963", 1963), ("Joshua beats Klitschko at Wembley", "2017", 2017), ("The Rumble in the Jungle", "1974", 1974),
 ("Tyson Fury beats Klitschko", "2015", 2015), ("The Thrilla in Manila", "1975", 1975), ("Frank Bruno becomes world champion", "1995", 1995)])
game("the year each website or gadget launched", "Science and technology", "medium", ["internet", "years"], [
 ("eBay", "1995", 1995), ("ChatGPT", "2022", 2022), ("Wikipedia", "2001", 2001), ("The Kindle", "2007", 2007), ("Gmail", "2004", 2004), ("Google Maps", "2005", 2005)])
game("the year of each great season", "Football", "medium", ["titles", "trebles", "years"], [
 ("Blackburn win the league", "1995", 1995), ("Manchester City's treble", "2023", 2023), ("Manchester United's treble", "1999", 1999),
 ("Liverpool's first Premier League title", "2020", 2020), ("Arsenal's Invincibles", "2004", 2004), ("Leicester's 5,000-1 title", "2016", 2016)])
game("how many chromosomes?", "Science and nature", "hard", ["genetics", "animals"], [
 ("A fruit fly", "8", 8), ("A dog", "78", 78), ("A cat", "38", 38), ("A chimpanzee", "48", 48), ("A human", "46", 46)])
game("the year each quiz show began", "Film and TV", "medium", ["quiz shows", "years"], [
 ("Fifteen to One", "1988", 1988), ("Tipping Point", "2012", 2012), ("The Weakest Link", "2000", 2000),
 ("Pointless", "2009", 2009), ("Eggheads", "2003", 2003), ("Only Connect", "2008", 2008)])
game("the year of each music first", "Music", "hard", ["charts", "awards", "years"], [
 ("The first UK singles chart", "1952", 1952), ("The first Mercury Prize", "1992", 1992), ("The first Eurovision", "1956", 1956),
 ("The first Brit Awards", "1977", 1977), ("The first Grammys", "1959", 1959)])
game("the year each bank began", "Money", "hard", ["banks", "years"], [
 ("Barclays", "1690", 1690), ("Monzo", "2015", 2015), ("The Bank of England", "1694", 1694), ("NatWest", "1968", 1968), ("Lloyds", "1765", 1765)])
game("how many monarchs of England or Britain had each name?", "Kings and queens", "medium", ["monarchs", "names"], [
 ("Victoria", "1", 1), ("Henry", "8", 8), ("Elizabeth", "2", 2), ("George", "6", 6), ("Richard", "3", 3), ("Edward", "8", 8)])
game("the year each explorer died", "History", "hard", ["explorers", "years"], [
 ("Christopher Columbus", "1506", 1506), ("Ernest Shackleton", "1922", 1922), ("Ferdinand Magellan", "1521", 1521),
 ("Captain Scott", "1912", 1912), ("Captain Cook", "1779", 1779), ("David Livingstone", "1873", 1873)])
game("the year each tower was finished", "Famous landmarks", "hard", ["towers", "years"], [
 ("Blackpool Tower", "1894", 1894), ("Tokyo Skytree", "2012", 2012), ("Seattle's Space Needle", "1962", 1962),
 ("Portsmouth's Spinnaker Tower", "2005", 2005), ("London's BT Tower", "1965", 1965), ("Toronto's CN Tower", "1976", 1976)])
game("the year each great church was begun or finished", "Famous landmarks", "hard", ["churches", "years"], [
 ("Westminster Abbey (today's) is begun", "1245", 1245), ("Liverpool's Anglican Cathedral is finished", "1978", 1978), ("St Paul's Cathedral is finished", "1710", 1710),
 ("The new Coventry Cathedral is consecrated", "1962", 1962), ("The Sagrada Família is begun", "1882", 1882)])
game("the year each fashion classic arrived", "Fashion", "hard", ["fashion", "years"], [
 ("Barbour", "1894", 1894), ("Crocs", "2002", 2002), ("Converse All Stars", "1917", 1917), ("The bikini", "1946", 1946), ("Ray-Ban Aviators", "1937", 1937)])
game("the year each children's favourite first appeared", "Nostalgia", "medium", ["children's TV", "books", "years"], [
 ("The Wombles", "1968", 1968), ("Bob the Builder", "1999", 1999), ("The Clangers", "1969", 1969),
 ("In the Night Garden", "2007", 2007), ("Mr. Men", "1971", 1971), ("Fireman Sam", "1987", 1987)])
game("the year of each political exit or win", "Politics", "medium", ["Prime Ministers", "years"], [
 ("Margaret Thatcher resigns", "1990", 1990), ("Boris Johnson resigns", "2022", 2022), ("John Major wins the election", "1992", 1992),
 ("The Brexit referendum", "2016", 2016), ("Tony Blair stands down", "2007", 2007)])
game("the year each long-running stage show opened in London", "Theatre", "hard", ["theatre", "West End", "years"], [
 ("The Mousetrap", "1952", 1952), ("The Book of Mormon", "2013", 2013), ("Blood Brothers", "1988", 1988), ("Matilda the Musical", "2011", 2011), ("The Woman in Black", "1989", 1989)])
game("the year each trophy was first played for", "Sport", "hard", ["trophies", "years"], [
 ("The Calcutta Cup", "1879", 1879), ("The football World Cup", "1930", 1930), ("The Ashes", "1882", 1882),
 ("The Ryder Cup", "1927", 1927), ("The Davis Cup", "1900", 1900), ("The Champions League, by that name", "1992", 1992)])
game("the year each tunnel opened", "Engineering", "hard", ["tunnels", "years"], [
 ("The Blackwall Tunnel", "1897", 1897), ("The Gotthard Base Tunnel", "2016", 2016), ("The Rotherhithe Tunnel", "1908", 1908),
 ("The Dartford Tunnel", "1963", 1963), ("The Mersey's Queensway Tunnel", "1934", 1934)])
game("points scored on Countdown", "Film and TV", "hard", ["Countdown", "scoring"], [
 ("A nine-letter word", "18", 18), ("Numbers round, within 5", "7", 7), ("Numbers round, spot on", "10", 10), ("Numbers round, within 10", "5", 5), ("An eight-letter word", "8", 8)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-18.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
