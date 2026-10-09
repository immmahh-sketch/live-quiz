# Bank session 9 Oct 2026: 20 more Play Your Cards Right games -> bank/cards-4.json. A row of 5-7 cards each:
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

game("the year each Beatles album came out", "Music", "medium", ["Beatles", "albums", "years"], [
 ("Please Please Me", "1963", 1963), ("Abbey Road", "1969", 1969), ("Help!", "1965", 1965),
 ("Let It Be", "1970", 1970), ("A Hard Day's Night", "1964", 1964), ("Sgt. Pepper's Lonely Hearts Club Band", "1967", 1967)])
game("how many in each famous group?", "Books and film", "easy", ["groups", "numbers"], [
 ("The Famous Five", "5", 5), ("A jury in England", "12", 12), ("The Musketeers in the title", "3", 3),
 ("Snow White's dwarfs", "7", 7), ("The Fantastic Four", "4", 4), ("Danny Ocean's gang in the 2001 film", "11", 11)])
game("how many days?", "Calendar", "easy", ["days", "dates"], [
 ("A week", "7", 7), ("A leap year", "366", 366), ("A fortnight", "14", 14), ("Lent", "40", 40), ("February, not in a leap year", "28", 28), ("September", "30", 30)])
game("the year each chocolate bar was launched", "Food and drink", "hard", ["chocolate", "years"], [
 ("Cadbury Dairy Milk", "1905", 1905), ("Twix", "1967", 1967), ("Crunchie", "1929", 1929),
 ("Galaxy", "1960", 1960), ("Mars bar", "1932", 1932), ("KitKat", "1935", 1935)])
game("Eurovision wins, up to 2025", "Eurovision", "hard", ["Eurovision"], [
 ("Norway", "3", 3), ("Ireland", "7", 7), ("Israel", "4", 4), ("United Kingdom", "5", 5), ("Austria", "3", 3), ("Sweden", "7", 7)])
game("which number US president was each?", "World history", "hard", ["US presidents"], [
 ("George Washington", "1st", 1), ("Barack Obama", "44th", 44), ("Abraham Lincoln", "16th", 16),
 ("Ronald Reagan", "40th", 40), ("Franklin D. Roosevelt", "32nd", 32), ("John F. Kennedy", "35th", 35)])
game("top-flight league titles, up to 2025", "Football", "medium", ["league titles", "clubs"], [
 ("Newcastle United", "4", 4), ("Liverpool", "20", 20), ("Sunderland", "6", 6), ("Arsenal", "13", 13), ("Everton", "9", 9), ("Manchester City", "10", 10)])
game("how many lines in each kind of poem?", "Words and language", "hard", ["poetry"], [
 ("A couplet", "2", 2), ("A sonnet", "14", 14), ("A haiku", "3", 3), ("A villanelle", "19", 19), ("A quatrain", "4", 4), ("A limerick", "5", 5)])
game("how many minutes does each last?", "Sport", "medium", ["sport", "timing"], [
 ("A professional boxing round", "3", 3), ("A football half", "45", 45), ("An NBA quarter", "12", 12),
 ("A rugby union half", "40", 40), ("A netball quarter", "15", 15), ("An ice hockey period", "20", 20)])
game("the year each toy or game first went on sale", "Games and toys", "medium", ["toys", "years"], [
 ("Monopoly", "1935", 1935), ("Furby", "1998", 1998), ("Barbie", "1959", 1959),
 ("Tamagotchi", "1996", 1996), ("Cluedo", "1949", 1949), ("Trivial Pursuit", "1981", 1981)])
game("how many stars on each flag?", "Flags", "hard", ["flags"], [
 ("China", "5", 5), ("The USA", "50", 50), ("New Zealand", "4", 4), ("Brazil", "27", 27), ("Australia", "6", 6), ("The European Union", "12", 12)])
game("the year each coin or note arrived", "Money", "hard", ["money", "years"], [
 ("The 50p coin", "1969", 1969), ("The £2 coin", "1998", 1998), ("The 20p coin", "1982", 1982),
 ("The plastic £5 note", "2016", 2016), ("Decimal Day", "1971", 1971), ("The £1 coin", "1983", 1983)])
game("the year it came in", "British history", "medium", ["laws", "years"], [
 ("The NHS", "1948", 1948), ("The smoking ban in England's pubs", "2007", 2007), ("The vote for some women", "1918", 1918),
 ("The National Lottery", "1994", 1994), ("The breathalyser", "1967", 1967), ("Compulsory front seatbelts", "1983", 1983)])
game("the year each company was founded", "Science and technology", "medium", ["companies", "internet"], [
 ("Google", "1998", 1998), ("Instagram", "2010", 2010), ("Amazon", "1994", 1994), ("Facebook", "2004", 2004), ("Netflix", "1997", 1997), ("YouTube", "2005", 2005)])
game("how many films in each series?", "Film", "medium", ["films", "series"], [
 ("Back to the Future", "3", 3), ("Harry Potter", "8", 8), ("Jaws", "4", 4),
 ("The Star Wars Skywalker saga", "9", 9), ("The Lord of the Rings", "3", 3), ("Rocky (not counting Creed)", "6", 6)])
game("the price of each Monopoly property (London board)", "Games and toys", "medium", ["Monopoly", "prices"], [
 ("Old Kent Road", "£60", 60), ("Mayfair", "£400", 400), ("The Angel Islington", "£100", 100),
 ("Park Lane", "£350", 350), ("Pall Mall", "£140", 140), ("Trafalgar Square", "£240", 240)])
game("points in rugby union", "Rugby", "easy", ["rugby", "scoring"], [
 ("A conversion", "2", 2), ("A penalty try", "7", 7), ("A penalty kick", "3", 3), ("A try", "5", 5), ("A drop goal", "3", 3)])
game("the year each game show began", "Film and TV", "medium", ["game shows", "years"], [
 ("University Challenge", "1962", 1962), ("The Chase", "2009", 2009), ("Mastermind", "1972", 1972),
 ("Who Wants to Be a Millionaire?", "1998", 1998), ("Blankety Blank", "1979", 1979), ("Countdown", "1982", 1982)])
game("Team GB gold medals at each Summer Olympics", "The Olympics", "hard", ["Olympics", "Team GB"], [
 ("Atlanta 1996", "1", 1), ("London 2012", "29", 29), ("Athens 2004", "9", 9), ("Rio 2016", "27", 27), ("Paris 2024", "14", 14), ("Tokyo 2020", "22", 22)])
game("how many years in each?", "Calendar", "easy", ["years", "words"], [
 ("A decade", "10", 10), ("A millennium", "1,000", 1000), ("A score", "20", 20), ("A century", "100", 100), ("A Silver Jubilee", "25", 25), ("A Diamond Jubilee", "60", 60)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-4.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
