# Bank session 10 Oct 2026: 20 more Play Your Cards Right games -> bank/cards-6.json. A row of 5-7 cards each:
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

game("the year each Star Wars film came out", "Film", "medium", ["Star Wars", "years"], [
 ("The Empire Strikes Back", "1980", 1980), ("The Force Awakens", "2015", 2015), ("Return of the Jedi", "1983", 1983),
 ("Revenge of the Sith", "2005", 2005), ("The Phantom Menace", "1999", 1999), ("Rogue One", "2016", 2016)])
game("the year each Marvel film came out", "Film", "medium", ["Marvel", "years"], [
 ("Iron Man", "2008", 2008), ("Avengers: Endgame", "2019", 2019), ("Avengers Assemble", "2012", 2012),
 ("Black Panther", "2018", 2018), ("Guardians of the Galaxy", "2014", 2014), ("Spider-Man: Homecoming", "2017", 2017)])
game("the year each Christmas film came out", "Christmas", "medium", ["Christmas", "films", "years"], [
 ("It's a Wonderful Life", "1946", 1946), ("Elf", "2003", 2003), ("The Snowman", "1982", 1982),
 ("The Holiday", "2006", 2006), ("Die Hard", "1988", 1988), ("Home Alone", "1990", 1990)])
game("roughly how far from the Sun, in millions of miles?", "Space", "hard", ["planets", "distances"], [
 ("Earth", "about 93 million", 93), ("Mercury", "about 36 million", 36), ("Saturn", "about 886 million", 886),
 ("Venus", "about 67 million", 67), ("Jupiter", "about 484 million", 484), ("Mars", "about 142 million", 142)])
game("the numbers of the Solar System", "Space", "medium", ["space", "numbers"], [
 ("Planets", "8", 8), ("Moons of Mars", "2", 2), ("Recognised dwarf planets", "5", 5), ("Moons of Earth", "1", 1),
 ("Planets with rings", "4", 4), ("Minutes for sunlight to reach Earth", "about 8", 8)])
game("which day of the month is it?", "Calendar", "easy", ["dates", "festivals"], [
 ("Bonfire Night", "5th", 5), ("Christmas Day", "25th", 25), ("April Fools' Day", "1st", 1), ("Halloween", "31st", 31), ("Valentine's Day", "14th", 14), ("St George's Day", "23rd", 23)])
game("the house number on each famous front door", "Books and TV", "medium", ["addresses"], [
 ("The Prime Minister, Downing Street", "10", 10), ("Sherlock Holmes, Baker Street", "221B", 221), ("The Dursleys, Privet Drive", "4", 4),
 ("The Simpsons, Evergreen Terrace", "742", 742), ("Paddington and the Browns, Windsor Gardens", "32", 32)])
game("the year each Apple product launched", "Science and technology", "medium", ["Apple", "gadgets", "years"], [
 ("The Macintosh", "1984", 1984), ("The Apple Watch", "2015", 2015), ("The iPod", "2001", 2001), ("AirPods", "2016", 2016), ("The iPad", "2010", 2010)])
game("roughly how many people, in millions (2025)?", "World geography", "hard", ["population", "countries"], [
 ("Ireland", "about 5.4 million", 5.4), ("The USA", "about 340 million", 340), ("Australia", "about 27 million", 27),
 ("China", "about 1,410 million", 1410), ("The UK", "about 69 million", 69), ("Canada", "about 41 million", 41)])
game("the year each star died", "Famous people in history", "medium", ["deaths", "years"], [
 ("Marilyn Monroe", "1962", 1962), ("Michael Jackson", "2009", 2009), ("Elvis Presley", "1977", 1977),
 ("Elizabeth II", "2022", 2022), ("John Lennon", "1980", 1980), ("Freddie Mercury", "1991", 1991)])
game("how long is each film, in minutes?", "Film", "hard", ["films", "running times"], [
 ("Toy Story", "81", 81), ("Titanic", "194", 194), ("Frozen", "102", 102), ("Avengers: Endgame", "181", 181), ("The Lion King (1994)", "88", 88), ("The Godfather", "175", 175)])
game("the numbers in Parliament", "Politics", "hard", ["Parliament", "numbers"], [
 ("Most years between general elections", "5", 5), ("MPs in the House of Commons", "650", 650), ("Members of the Northern Ireland Assembly", "90", 90),
 ("Seats needed for a Commons majority", "326", 326), ("Members of the Scottish Parliament", "129", 129)])
game("the year each bridge opened", "Famous landmarks", "hard", ["bridges", "years"], [
 ("Brooklyn Bridge", "1883", 1883), ("Humber Bridge", "1981", 1981), ("Forth Bridge (the railway one)", "1890", 1890),
 ("Severn Bridge", "1966", 1966), ("Sydney Harbour Bridge", "1932", 1932), ("Golden Gate Bridge", "1937", 1937)])
game("the year each war ended", "History", "hard", ["wars", "years"], [
 ("The Crimean War", "1856", 1856), ("The Falklands War", "1982", 1982), ("The First World War", "1918", 1918),
 ("The Vietnam War", "1975", 1975), ("The Second Boer War", "1902", 1902), ("The Korean War", "1953", 1953)])
game("the year of each moment in North East history", "The North East", "hard", ["North East", "history", "years"], [
 ("Hadrian's Wall is begun", "AD 122", 122), ("The first Great North Run", "1981", 1981), ("Vikings raid Lindisfarne", "793", 793),
 ("The Stockton and Darlington Railway opens", "1825", 1825), ("Durham Cathedral is begun", "1093", 1093), ("Newcastle's Swing Bridge opens", "1876", 1876)])
game("the numbers in music", "Music", "medium", ["music", "numbers"], [
 ("Lines on a stave", "5", 5), ("Keys on a piano", "88", 88), ("Beats in a bar of a waltz", "3", 3),
 ("Beethoven's symphonies", "9", 9), ("Strings on a cello", "4", 4), ("Mozart's numbered symphonies", "41", 41)])
game("the year each opened in the UK", "Food and drink", "hard", ["fast food", "years"], [
 ("Greggs is founded (in Gosforth)", "1939", 1939), ("Subway's first UK shop", "1996", 1996), ("KFC's first UK shop", "1965", 1965),
 ("Burger King's first UK shop", "1977", 1977), ("Pizza Hut's first UK restaurant", "1973", 1973), ("McDonald's first UK restaurant", "1974", 1974)])
game("how many in each?", "Words and language", "easy", ["quantities", "words"], [
 ("A pair", "2", 2), ("A gross", "144", 144), ("A baker's dozen", "13", 13), ("A ream of paper", "500", 500), ("A dozen", "12", 12), ("A hat-trick", "3", 3)])
game("the year each attraction opened", "Days out", "hard", ["theme parks", "years"], [
 ("Blackpool Pleasure Beach", "1896", 1896), ("The Eden Project", "2001", 2001), ("Thorpe Park", "1979", 1979),
 ("Legoland Windsor", "1996", 1996), ("Alton Towers theme park", "1980", 1980), ("Center Parcs Sherwood Forest", "1987", 1987)])
game("how many children in each TV family?", "Film and TV", "medium", ["TV", "families"], [
 ("The Simpsons", "3", 3), ("The Waltons", "7", 7), ("The Addams Family", "2", 2), ("The Brady Bunch", "6", 6), ("My Family (the Harpers)", "3", 3)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-6.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
