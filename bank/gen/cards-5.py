# Bank session 9 Oct 2026: 20 more Play Your Cards Right games -> bank/cards-5.json. A row of 5-7 cards each:
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

game("the year each Pixar film came out", "Film", "medium", ["Pixar", "years"], [
 ("Toy Story", "1995", 1995), ("Up", "2009", 2009), ("Monsters, Inc.", "2001", 2001), ("Coco", "2017", 2017), ("Finding Nemo", "2003", 2003), ("Inside Out", "2015", 2015)])
game("World Snooker Championship titles, up to 2025", "Snooker", "medium", ["snooker"], [
 ("Judd Trump", "1", 1), ("Stephen Hendry", "7", 7), ("Alex Higgins", "2", 2), ("Steve Davis", "6", 6), ("Mark Selby", "4", 4), ("Ronnie O'Sullivan", "7", 7)])
game("world darts titles, up to 2025", "Darts", "hard", ["darts"], [
 ("Luke Littler", "1", 1), ("Phil Taylor", "16", 16), ("Gary Anderson", "2", 2), ("Eric Bristow", "5", 5), ("Michael van Gerwen", "3", 3), ("Raymond van Barneveld", "5", 5)])
game("the year each manager took over", "Newcastle v Sunderland", "hard", ["managers", "Newcastle", "Sunderland"], [
 ("Kevin Keegan at Newcastle (first time)", "1992", 1992), ("Eddie Howe at Newcastle", "2021", 2021), ("Bobby Robson at Newcastle", "1999", 1999),
 ("Roy Keane at Sunderland", "2006", 2006), ("Peter Reid at Sunderland", "1995", 1995), ("Rafa Benítez at Newcastle", "2016", 2016)])
game("how many Ballon d'Or awards did each player win?", "Football", "medium", ["Ballon d'Or"], [
 ("Michael Owen", "1", 1), ("Lionel Messi", "8", 8), ("Michel Platini", "3", 3), ("Cristiano Ronaldo", "5", 5), ("George Best", "1", 1), ("Johan Cruyff", "3", 3)])
game("the year each World Cup was won", "Football", "medium", ["World Cup", "years"], [
 ("England at Wembley", "1966", 1966), ("Argentina in Qatar", "2022", 2022), ("France at home", "1998", 1998),
 ("Germany in Brazil", "2014", 2014), ("Italy in Germany", "2006", 2006), ("Spain in South Africa", "2010", 2010)])
game("the year each car was launched", "Cars", "hard", ["cars", "years"], [
 ("Ford Model T", "1908", 1908), ("Nissan Qashqai (built in Sunderland)", "2006", 2006), ("Mini", "1959", 1959),
 ("Ford Fiesta", "1976", 1976), ("Ford Escort", "1968", 1968), ("Volkswagen Golf", "1974", 1974)])
game("weeks at number one in the UK", "Music", "hard", ["number ones", "charts"], [
 ("Queen: Bohemian Rhapsody (1975)", "9", 9), ("Frankie Laine: I Believe", "18", 18), ("Ed Sheeran: Shape of You", "14", 14),
 ("Bryan Adams: (Everything I Do) I Do It for You", "16", 16), ("Wet Wet Wet: Love Is All Around", "15", 15)])
game("the year of each famous first", "History", "medium", ["firsts", "years"], [
 ("First climb to the top of Everest", "1953", 1953), ("Dolly the sheep is born", "1996", 1996), ("First man in space", "1961", 1961),
 ("The Channel Tunnel opens", "1994", 1994), ("First heart transplant", "1967", 1967), ("First test-tube baby", "1978", 1978)])
game("the year each Prime Minister first took office", "British history", "medium", ["Prime Ministers", "years"], [
 ("Winston Churchill", "1940", 1940), ("Keir Starmer", "2024", 2024), ("Harold Wilson", "1964", 1964),
 ("Tony Blair", "1997", 1997), ("Margaret Thatcher", "1979", 1979), ("David Cameron", "2010", 2010)])
game("seats won at the 2024 general election", "Politics", "hard", ["elections", "parties"], [
 ("Reform UK", "5", 5), ("Labour", "411", 411), ("Greens", "4", 4), ("Conservatives", "121", 121), ("SNP", "9", 9), ("Liberal Democrats", "72", 72)])
game("the year each book was first published", "Books", "hard", ["books", "years"], [
 ("Pride and Prejudice", "1813", 1813), ("To Kill a Mockingbird", "1960", 1960), ("Frankenstein", "1818", 1818),
 ("Lord of the Flies", "1954", 1954), ("Dracula", "1897", 1897), ("The Hobbit", "1937", 1937)])
game("the numbers behind each sporting event", "Sport", "medium", ["sport", "numbers"], [
 ("Holes in a round of golf", "18", 18), ("Frames in the World Snooker final (best of)", "35", 35), ("Miles in a marathon", "26.2", 26.2),
 ("Fences in the Grand National", "30", 30), ("Stages in the Tour de France", "21", 21), ("Overs per side in a T20 match", "20", 20)])
game("the year of each royal occasion", "The royal family", "easy", ["royals", "years"], [
 ("Elizabeth II's coronation", "1953", 1953), ("Harry and Meghan's wedding", "2018", 2018), ("Charles and Diana's wedding", "1981", 1981),
 ("Charles III's coronation", "2023", 2023), ("Diana dies in Paris", "1997", 1997), ("William and Catherine's wedding", "2011", 2011)])
game("the year each TV detective series began", "Film and TV", "medium", ["detectives", "TV", "years"], [
 ("Taggart", "1983", 1983), ("Vera", "2011", 2011), ("Inspector Morse", "1987", 1987),
 ("Line of Duty", "2012", 2012), ("Midsomer Murders", "1997", 1997), ("Sherlock", "2010", 2010)])
game("Wimbledon singles titles, up to 2025", "Tennis", "medium", ["Wimbledon", "tennis"], [
 ("Andy Murray", "2", 2), ("Martina Navratilova", "9", 9), ("Björn Borg", "5", 5), ("Roger Federer", "8", 8), ("Virginia Wade", "1", 1), ("Novak Djokovic", "7", 7)])
game("how many on each board or grid?", "Games and toys", "medium", ["board games", "puzzles"], [
 ("Columns in Connect 4", "7", 7), ("Squares in Snakes and Ladders", "100", 100), ("Points on a backgammon board", "24", 24),
 ("Spaces round a Monopoly board", "40", 40), ("Squares in noughts and crosses", "9", 9), ("Squares in a sudoku", "81", 81)])
game("the year each London landmark was finished", "London", "hard", ["London", "landmarks", "years"], [
 ("Tower Bridge", "1894", 1894), ("The Shard", "2012", 2012), ("Nelson's Column", "1843", 1843),
 ("The new Wembley Stadium", "2007", 2007), ("Big Ben's clock", "1859", 1859), ("The London Eye", "2000", 2000)])
game("how many countries in each?", "World geography", "medium", ["countries", "organisations"], [
 ("Scandinavia", "3", 3), ("The United Nations", "193", 193), ("The G7", "7", 7), ("The Commonwealth", "56", 56), ("The United Kingdom", "4", 4), ("The European Union", "27", 27)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-5.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
