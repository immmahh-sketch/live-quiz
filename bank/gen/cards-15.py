# Bank session 10 Oct 2026: 20 more Play Your Cards Right games -> bank/cards-15.json. A row of 5-7 cards each:
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

game("the year each fashion name began", "Fashion", "hard", ["fashion", "brands", "years"], [
 ("Burberry", "1856", 1856), ("Nike", "1971", 1971), ("Levi's jeans", "1873", 1873), ("Dr. Martens boots in Britain", "1960", 1960), ("Chanel No. 5", "1921", 1921), ("Adidas", "1949", 1949)])
game("the year of each moment in North East history (part two)", "The North East", "hard", ["North East", "history", "years"], [
 ("St Cuthbert dies", "687", 687), ("The Jarrow March", "1936", 1936), ("The Lindisfarne Gospels are made", "about 715", 715),
 ("The miners' strike begins", "1984", 1984), ("Bede dies at Jarrow", "735", 735), ("The first Durham Miners' Gala", "1871", 1871)])
game("lengths of an Olympic pool in each race", "Swimming", "medium", ["swimming", "distances"], [
 ("400 metres", "8", 8), ("1,500 metres", "30", 30), ("100 metres", "2", 2), ("800 metres", "16", 16), ("50 metres", "1", 1), ("200 metres", "4", 4)])
game("the year each Christmas song came out", "Christmas", "medium", ["Christmas", "songs", "years"], [
 ("Bing Crosby: White Christmas", "1942", 1942), ("Mariah Carey: All I Want for Christmas Is You", "1994", 1994), ("Slade: Merry Xmas Everybody", "1973", 1973),
 ("The Pogues: Fairytale of New York", "1987", 1987), ("Wham!: Last Christmas", "1984", 1984), ("Chris Rea: Driving Home for Christmas", "1988", 1988)])
game("the year of each famous concert", "Music", "hard", ["concerts", "years"], [
 ("Woodstock", "1969", 1969), ("Live 8", "2005", 2005), ("The Beatles' last paid concert", "1966", 1966), ("Oasis at Knebworth", "1996", 1996), ("The Freddie Mercury tribute concert", "1992", 1992)])
game("roughly how long does each animal live, in years?", "Animals", "medium", ["animals", "lifespans"], [
 ("A hamster", "about 2", 2), ("A Galápagos tortoise", "over 100", 100), ("A pet cat", "about 15", 15),
 ("An African elephant", "about 65", 65), ("A pet rabbit", "about 9", 9), ("A horse", "about 28", 28)])
game("the year of each tennis moment", "Tennis", "medium", ["tennis", "years"], [
 ("Virginia Wade wins Wimbledon", "1977", 1977), ("Emma Raducanu wins the US Open", "2021", 2021), ("Björn Borg wins his fifth Wimbledon", "1980", 1980),
 ("Andy Murray's Olympic gold at Wimbledon", "2012", 2012), ("Roger Federer's first Wimbledon title", "2003", 2003)])
game("which year is each Roman numeral?", "Maths and numbers", "hard", ["Roman numerals", "years"], [
 ("MCMLXVI", "1966", 1966), ("MLXVI", "1066", 1066), ("MMXXII", "2022", 2022), ("MDCCLXXVI", "1776", 1776), ("MCMXCIX", "1999", 1999), ("MCMXLV", "1945", 1945)])
game("the year of each medical breakthrough", "Science and nature", "medium", ["medicine", "years"], [
 ("Jenner's smallpox vaccine", "1796", 1796), ("The first Covid jab in the UK", "2020", 2020), ("X-rays are discovered", "1895", 1895),
 ("Smallpox is wiped out", "1980", 1980), ("Insulin is discovered", "1921", 1921), ("The first kidney transplant", "1954", 1954)])
game("the youngest age you can be", "General knowledge", "hard", ["ages", "rules"], [
 ("To ride a moped", "16", 16), ("To be US President", "35", 35), ("To learn to drive a car", "17", 17),
 ("To be a US senator", "30", 30), ("To be a UK MP", "18", 18), ("To be in the US House of Representatives", "25", 25)])
game("the year each Saturday night show began", "Film and TV", "medium", ["Saturday night TV", "years"], [
 ("The Generation Game", "1971", 1971), ("The Masked Singer", "2020", 2020), ("Blind Date", "1985", 1985),
 ("Saturday Night Takeaway", "2002", 2002), ("Beadle's About", "1986", 1986), ("Noel's House Party", "1991", 1991)])
game("the year each North East act's big hit came out", "The North East", "hard", ["North East", "music", "years"], [
 ("The Animals: House of the Rising Sun", "1964", 1964), ("Sam Fender: Seventeen Going Under", "2021", 2021), ("Lindisfarne: Meet Me on the Corner", "1972", 1972),
 ("Girls Aloud: Sound of the Underground", "2002", 2002), ("The Police: Roxanne", "1978", 1978), ("Little Mix: Cannonball", "2011", 2011)])
game("the year of each state or royal funeral", "History", "medium", ["funerals", "years"], [
 ("Lord Nelson", "1806", 1806), ("Elizabeth II", "2022", 2022), ("The Duke of Wellington", "1852", 1852), ("The Queen Mother", "2002", 2002), ("Winston Churchill", "1965", 1965)])
game("the numbers in the Bible", "Religion", "medium", ["Bible", "numbers"], [
 ("Gospels", "4", 4), ("Books in the Protestant Bible", "66", 66), ("Days of creation before the day of rest", "6", 6), ("Apostles", "12", 12), ("Commandments", "10", 10)])
game("the numbers in tennis", "Tennis", "medium", ["tennis", "rules"], [
 ("Grand Slams in a year", "4", 4), ("Points to win a tie-break", "7", 7), ("Sets to win a men's Grand Slam match", "3", 3),
 ("Games to win a set", "6", 6), ("Fewest points to win a game", "4", 4)])
game("the number on each engine", "Trains", "hard", ["trains", "numbers"], [
 ("Thomas the Tank Engine", "1", 1), ("The Hogwarts Express engine", "5972", 5972), ("Gordon", "4", 4),
 ("The Flying Scotsman", "4472", 4472), ("Percy", "6", 6), ("Mallard", "4468", 4468)])
game("the year each face went on a Bank of England note", "Money", "hard", ["banknotes", "years"], [
 ("Charles Darwin on the £10", "2000", 2000), ("Alan Turing on the £50", "2021", 2021), ("Elizabeth Fry on the £5", "2002", 2002),
 ("J. M. W. Turner on the £20", "2020", 2020), ("Winston Churchill on the £5", "2016", 2016), ("Jane Austen on the £10", "2017", 2017)])
game("the year each artist died", "Art", "hard", ["artists", "years"], [
 ("Leonardo da Vinci", "1519", 1519), ("L. S. Lowry", "1976", 1976), ("Michelangelo", "1564", 1564),
 ("Vincent van Gogh", "1890", 1890), ("Rembrandt", "1669", 1669), ("Pablo Picasso", "1973", 1973)])
game("how many in each team of heroes?", "Film", "easy", ["heroes", "teams"], [
 ("The Teenage Mutant Ninja Turtles", "4", 4), ("The Fellowship of the Ring", "9", 9), ("The original Power Rangers", "5", 5),
 ("The Avengers in the 2012 film", "6", 6), ("The Ghostbusters", "4", 4)])
game("the year of each show's first winner", "Film and TV", "medium", ["TV", "winners", "years"], [
 ("Mastermind", "1972", 1972), ("The Great British Bake Off", "2010", 2010), ("Who Wants to Be a Millionaire?", "2000", 2000),
 ("The Apprentice", "2005", 2005), ("Pop Idol", "2002", 2002)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-15.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
