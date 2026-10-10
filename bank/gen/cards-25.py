# Bank session 10 Oct 2026: 20 more Play Your Cards Right games -> bank/cards-25.json. A row of 5-7 cards each:
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

game("the year each monarch was born", "Kings and queens", "hard", ["monarchs", "birthdays", "years"], [
 ("Richard III", "1452", 1452), ("George III", "1738", 1738), ("Henry VIII", "1491", 1491), ("Queen Victoria", "1819", 1819), ("Elizabeth I", "1533", 1533), ("Charles I", "1600", 1600)])
game("the year each Paris landmark was finished", "Famous landmarks", "hard", ["Paris", "landmarks", "years"], [
 ("Notre-Dame", "about 1345", 1345), ("The Louvre Pyramid", "1989", 1989), ("The Arc de Triomphe", "1836", 1836), ("The Pompidou Centre", "1977", 1977), ("Sacré-Cœur", "1914", 1914)])
game("the year each New York landmark opened", "Famous landmarks", "medium", ["New York", "landmarks", "years"], [
 ("Central Park", "1858", 1858), ("One World Trade Center", "2014", 2014), ("Grand Central Terminal", "1913", 1913), ("The High Line", "2009", 2009), ("The Chrysler Building", "1930", 1930)])
game("the numbers behind famous TV shows", "Film and TV", "medium", ["TV", "numbers"], [
 ("Records on Desert Island Discs", "8", 8), ("The top score on Pointless", "100", 100), ("Lifelines on the original Millionaire", "3", 3),
 ("Questions to win the million on Millionaire", "15", 15), ("A perfect score from one Strictly judge", "10", 10)])
game("the year each scandal broke", "Politics", "medium", ["scandals", "years"], [
 ("The Profumo affair", "1963", 1963), ("MPs' expenses", "2009", 2009), ("Watergate", "1972", 1972), ("Cash for honours", "2006", 2006), ("Clinton and Lewinsky", "1998", 1998)])
game("the year each soft drink was launched", "Food and drink", "hard", ["soft drinks", "years"], [
 ("Dr Pepper", "1885", 1885), ("Sprite", "1961", 1961), ("Pepsi", "1893", 1893), ("Ribena", "1938", 1938), ("Lucozade", "1927", 1927), ("Fanta", "1940", 1940)])
game("how many laps?", "Sport", "hard", ["laps", "races"], [
 ("The 10,000 metres", "25", 25), ("The Indy 500", "200", 200), ("The British Grand Prix", "52", 52), ("The Monaco Grand Prix", "78", 78), ("The 1,500 metres", "3¾", 3.75)])
game("the year each video-game film came out", "Film", "medium", ["video games", "films", "years"], [
 ("Super Mario Bros. (the live-action one)", "1993", 1993), ("The Super Mario Bros. Movie", "2023", 2023), ("Street Fighter", "1994", 1994),
 ("Sonic the Hedgehog", "2020", 2020), ("Lara Croft: Tomb Raider", "2001", 2001), ("Detective Pikachu", "2019", 2019)])
game("the year each Best Actor-winning film came out", "The Oscars and award winners", "hard", ["Oscars", "films", "years"], [
 ("Gandhi", "1982", 1982), ("Bohemian Rhapsody", "2018", 2018), ("My Left Foot", "1989", 1989),
 ("Darkest Hour", "2017", 2017), ("The King's Speech", "2010", 2010), ("The Theory of Everything", "2014", 2014)])
game("the year each piece of software arrived", "Science and technology", "hard", ["software", "years"], [
 ("Microsoft Word", "1983", 1983), ("Google Chrome", "2008", 2008), ("Excel", "1985", 1985), ("Windows XP", "2001", 2001), ("PowerPoint", "1987", 1987), ("Photoshop", "1990", 1990)])
game("the year each long-distance path opened", "Britain", "hard", ["walking", "paths", "years"], [
 ("The Pennine Way", "1965", 1965), ("The Wales Coast Path", "2012", 2012), ("Offa's Dyke Path", "1971", 1971),
 ("Hadrian's Wall Path", "2003", 2003), ("The South West Coast Path", "1978", 1978), ("The West Highland Way", "1980", 1980)])
game("the year of each star's first Wimbledon singles title", "Tennis", "medium", ["Wimbledon", "years"], [
 ("Martina Navratilova", "1978", 1978), ("Jannik Sinner", "2025", 2025), ("Steffi Graf", "1988", 1988),
 ("Carlos Alcaraz", "2023", 2023), ("Pete Sampras", "1993", 1993), ("Rafael Nadal", "2008", 2008)])
game("the year each dish was (supposedly) invented", "Food and drink", "medium", ["dishes", "years"], [
 ("The sandwich", "1762", 1762), ("Hawaiian pizza", "1962", 1962), ("Pizza Margherita", "1889", 1889), ("Nachos", "1943", 1943), ("Caesar salad", "1924", 1924)])
game("the year of each Scottish landmark", "Britain", "hard", ["Scotland", "landmarks", "years"], [
 ("The Forth Road Bridge opens", "1964", 1964), ("The Queensferry Crossing opens", "2017", 2017), ("The Skye Bridge opens", "1995", 1995),
 ("The Kelpies are finished", "2013", 2013), ("The Scottish Parliament meets again", "1999", 1999), ("The Falkirk Wheel opens", "2002", 2002)])
game("the year each comic-book film came out", "Film", "medium", ["superheroes", "films", "years"], [
 ("Superman", "1978", 1978), ("Joker", "2019", 2019), ("Batman (Michael Keaton)", "1989", 1989), ("The Dark Knight", "2008", 2008), ("X-Men", "2000", 2000), ("Spider-Man (Tobey Maguire)", "2002", 2002)])
game("the year each sci-fi film came out", "Film", "medium", ["science fiction", "films", "years"], [
 ("Close Encounters of the Third Kind", "1977", 1977), ("Interstellar", "2014", 2014), ("Alien", "1979", 1979),
 ("Avatar", "2009", 2009), ("Back to the Future", "1985", 1985), ("Inception", "2010", 2010)])
game("the year each war film came out", "Film", "medium", ["war films", "years"], [
 ("The Dam Busters", "1955", 1955), ("1917", "2019", 2019), ("The Great Escape", "1963", 1963), ("Dunkirk", "2017", 2017), ("Apocalypse Now", "1979", 1979), ("Saving Private Ryan", "1998", 1998)])
game("the year of each great cricket moment", "Cricket", "hard", ["cricket", "years"], [
 ("Bradman's last Test", "1948", 1948), ("England win the World Cup", "2019", 2019), ("Jim Laker takes 19 wickets", "1956", 1956),
 ("Brian Lara scores 400", "2004", 2004), ("Shane Warne's 'Ball of the Century'", "1993", 1993), ("England win the Ashes at The Oval", "2005", 2005)])
game("the number behind each darts term", "Darts", "medium", ["darts", "terms"], [
 ("'Madhouse' (double one)", "2", 2), ("'A ton'", "100", 100), ("'Bed and breakfast'", "26", 26), ("Darts in a 'nine-darter'", "9", 9), ("'Treble top'", "60", 60)])
game("the year each TV talent show began", "Film and TV", "medium", ["talent shows", "years"], [
 ("Opportunity Knocks", "1956", 1956), ("The Voice UK", "2012", 2012), ("New Faces", "1973", 1973), ("Fame Academy", "2002", 2002), ("Stars in Their Eyes", "1990", 1990), ("Popstars", "2001", 2001)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-25.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
