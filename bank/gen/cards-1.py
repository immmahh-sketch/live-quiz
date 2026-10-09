# Bank session 9 Oct 2026: the first Play Your Cards Right games -> bank/cards.json.
# Each game is a row of 6 cards on one theme: what's on the card, what it shows when it flips, and the number compared.
# The numbers zig-zag so the right call isn't always "higher", and no two neighbours are equal.
import json, os
G = []
def game(text, cat, diff, tags, cards):
    ns = [n for _, _, n in cards]
    assert 5 <= len(cards) <= 7, text
    assert all(ns[i] != ns[i - 1] for i in range(1, len(ns))), (text, 'equal neighbours')
    G.append({"type": "cards", "text": "Play Your Cards Right: " + text, "category": cat, "tags": ["Play Your Cards Right"] + tags, "difficulty": diff,
              "cards": [{"label": l, "value": v, "n": n} for l, v, n in cards]})

game("how tall, in metres?", "Famous landmarks", "medium", ["buildings", "heights"], [
 ("The Angel of the North", "20 m", 20), ("The Shard", "310 m", 310), ("Big Ben's Elizabeth Tower", "96 m", 96),
 ("Burj Khalifa", "828 m", 828), ("Blackpool Tower", "158 m", 158), ("Eiffel Tower", "330 m", 330)])
game("the year each film came out", "Film", "medium", ["films", "years"], [
 ("Star Wars", "1977", 1977), ("Titanic", "1997", 1997), ("Grease", "1978", 1978),
 ("Frozen", "2013", 2013), ("E.T.", "1982", 1982), ("Jaws", "1975", 1975)])
game("how old were they when they died?", "Famous people in history", "medium", ["ages", "people"], [
 ("Amy Winehouse", "27", 27), ("Winston Churchill", "90", 90), ("John Lennon", "40", 40),
 ("Elizabeth II", "96", 96), ("Princess Diana", "36", 36), ("David Bowie", "69", 69)])
game("Premier League titles won, up to 2025", "Football", "medium", ["Premier League", "football"], [
 ("Blackburn Rovers", "1", 1), ("Manchester United", "13", 13), ("Arsenal", "3", 3),
 ("Manchester City", "8", 8), ("Liverpool", "2", 2), ("Chelsea", "5", 5)])
game("men's World Cups won", "Football", "medium", ["World Cup", "football"], [
 ("England", "1", 1), ("Brazil", "5", 5), ("France", "2", 2), ("Germany", "4", 4), ("Spain", "1", 1), ("Argentina", "3", 3)])
game("players on the field per team", "Sport", "easy", ["team sports"], [
 ("Basketball", "5", 5), ("Rugby union", "15", 15), ("Netball", "7", 7), ("Rugby league", "13", 13), ("Ice hockey", "6", 6), ("Football", "11", 11)])
game("how many legs?", "Animals", "easy", ["animals"], [
 ("Bird", "2", 2), ("Spider", "8", 8), ("Snake", "0", 0), ("Lobster", "10", 10), ("Dog", "4", 4), ("Ant", "6", 6)])
game("the year it happened", "British history", "medium", ["history", "years"], [
 ("Magna Carta", "1215", 1215), ("The Great Fire of London", "1666", 1666), ("The Battle of Hastings", "1066", 1066),
 ("The first Moon landing", "1969", 1969), ("The Titanic sinks", "1912", 1912), ("The Berlin Wall falls", "1989", 1989)])
game("how high, in metres?", "World geography", "medium", ["mountains"], [
 ("Snowdon", "1,085 m", 1085), ("Everest", "8,849 m", 8849), ("Scafell Pike", "978 m", 978),
 ("Kilimanjaro", "5,895 m", 5895), ("Ben Nevis", "1,345 m", 1345), ("Mont Blanc", "4,806 m", 4806)])
game("how old was each actor when his first Bond film came out?", "James Bond", "hard", ["Bond", "ages"], [
 ("George Lazenby", "30", 30), ("Roger Moore", "45", 45), ("Sean Connery", "32", 32),
 ("Pierce Brosnan", "42", 42), ("Daniel Craig", "38", 38), ("Timothy Dalton", "43", 43)])
game("how many of each gift in 'The Twelve Days of Christmas'?", "Christmas", "easy", ["Christmas", "carols"], [
 ("Partridges in a pear tree", "1", 1), ("Lords a-leaping", "10", 10), ("Turtle doves", "2", 2),
 ("Drummers drumming", "12", 12), ("Gold rings", "5", 5), ("Maids a-milking", "8", 8)])
game("the year it was the Christmas number one", "Christmas songs", "medium", ["Christmas", "number ones"], [
 ("Mr Blobby", "1993", 1993), ("Killing in the Name", "2009", 2009), ("Mull of Kintyre", "1977", 1977),
 ("Stay Another Day", "1994", 1994), ("Do They Know It's Christmas?", "1984", 1984), ("Mistletoe and Wine", "1988", 1988)])
game("how old were they when they became Prime Minister?", "British history", "hard", ["Prime Ministers", "ages"], [
 ("Rishi Sunak", "42", 42), ("Winston Churchill", "65", 65), ("Tony Blair", "43", 43),
 ("Gordon Brown", "56", 56), ("John Major", "47", 47), ("Keir Starmer", "61", 61)])
game("the year each city hosted the Summer Olympics", "The Olympics", "medium", ["Olympics", "years"], [
 ("Moscow", "1980", 1980), ("Paris", "2024", 2024), ("Atlanta", "1996", 1996),
 ("London", "2012", 2012), ("Los Angeles", "1984", 1984), ("Beijing", "2008", 2008)])
game("the year each song came out", "Music", "medium", ["songs", "years"], [
 ("Dancing Queen", "1976", 1976), ("Wonderwall", "1995", 1995), ("Billie Jean", "1983", 1983),
 ("Rolling in the Deep", "2010", 2010), ("Bohemian Rhapsody", "1975", 1975), ("Wannabe", "1996", 1996)])
game("how many sides?", "Maths and numbers", "easy", ["shapes"], [
 ("Triangle", "3", 3), ("Octagon", "8", 8), ("Square", "4", 4), ("Decagon", "10", 10), ("Pentagon", "5", 5), ("Hexagon", "6", 6)])
game("the year of each North East trophy", "Newcastle v Sunderland", "hard", ["Newcastle", "Sunderland", "trophies"], [
 ("Sunderland's first FA Cup", "1937", 1937), ("Newcastle's League Cup", "2025", 2025), ("Newcastle's first FA Cup", "1910", 1910),
 ("Sunderland beat Leeds in the FA Cup final", "1973", 1973), ("Newcastle's last FA Cup", "1955", 1955), ("Newcastle's Fairs Cup", "1969", 1969)])
game("how many minutes long is a match, not counting stoppages?", "Sport", "medium", ["sport", "rules"], [
 ("Rugby union", "80", 80), ("Netball", "60", 60), ("Football", "90", 90), ("Basketball (NBA)", "48", 48), ("Rugby league", "80", 80), ("Ice hockey", "60", 60)])
game("the year each TV show began", "Film and TV", "medium", ["TV", "years"], [
 ("Coronation Street", "1960", 1960), ("Strictly Come Dancing", "2004", 2004), ("Doctor Who", "1963", 1963),
 ("The Great British Bake Off", "2010", 2010), ("EastEnders", "1985", 1985), ("Blue Peter", "1958", 1958)])
game("the numbers behind classic games", "Games and toys", "hard", ["board games"], [
 ("Chess pieces per player", "16", 16), ("Draughts pieces per player", "12", 12), ("Pounds each player starts with in UK Monopoly", "£1,500", 1500),
 ("Dominoes in a double-six set", "28", 28), ("Tiles in a Scrabble set", "100", 100), ("Squares on a chessboard", "64", 64)])
game("how many letters in each word?", "Words and language", "easy", ["words"], [
 ("Cat", "3", 3), ("Elephant", "8", 8), ("Bird", "4", 4), ("Crocodile", "9", 9), ("Horse", "5", 5), ("Penguin", "7", 7)])
game("the year each was invented or first used", "Science and technology", "hard", ["inventions", "years"], [
 ("The telephone", "1876", 1876), ("The World Wide Web", "1989", 1989), ("The steam locomotive (Rocket)", "1829", 1829),
 ("The first iPhone", "2007", 2007), ("Television (Baird's demonstration)", "1926", 1926), ("The first email", "1971", 1971)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
