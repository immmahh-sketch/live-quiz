# Bank session 10 Oct 2026: 20 more Play Your Cards Right games -> bank/cards-8.json. A row of 5-7 cards each:
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

game("the year each was finished", "Famous landmarks", "medium", ["buildings", "years"], [
 ("The Statue of Liberty", "1886", 1886), ("The Burj Khalifa", "2010", 2010), ("The Eiffel Tower", "1889", 1889),
 ("The Gherkin", "2004", 2004), ("The Empire State Building", "1931", 1931), ("Sydney Opera House", "1973", 1973)])
game("how many acting Oscars did each win?", "The Oscars and award winners", "hard", ["Oscars", "actors"], [
 ("Leonardo DiCaprio", "1", 1), ("Katharine Hepburn", "4", 4), ("Tom Hanks", "2", 2), ("Meryl Streep", "3", 3), ("Judi Dench", "1", 1), ("Daniel Day-Lewis", "3", 3)])
game("the year each sitcom began", "Film and TV", "medium", ["sitcoms", "years"], [
 ("Dad's Army", "1968", 1968), ("Gavin & Stacey", "2007", 2007), ("Porridge", "1974", 1974),
 ("The Office", "2001", 2001), ("Blackadder", "1983", 1983), ("Peep Show", "2003", 2003)])
game("the year each musical opened in London", "Musicals", "hard", ["musicals", "West End", "years"], [
 ("Cats", "1981", 1981), ("Hamilton", "2017", 2017), ("Les Misérables", "1985", 1985),
 ("Wicked", "2006", 2006), ("The Phantom of the Opera", "1986", 1986), ("Mamma Mia!", "1999", 1999)])
game("the year each everyday thing arrived", "British history", "hard", ["firsts", "years"], [
 ("The Penny Black stamp", "1840", 1840), ("The first text message", "1992", 1992), ("The MOT test", "1960", 1960),
 ("The first contactless bank cards", "2007", 2007), ("Premium Bonds", "1956", 1956), ("The first cash machine", "1967", 1967)])
game("the number in each saying", "Words and language", "easy", ["sayings", "numbers"], [
 ("On cloud ___", "9", 9), ("Catch-___", "22", 22), ("___th heaven", "7", 7),
 ("Behind the ___ ball", "8", 8), ("The ___th hour", "11", 11), ("A stitch in time saves ___", "9", 9)])
game("the year each monarch died", "Kings and queens", "hard", ["monarchs", "years"], [
 ("Richard III", "1485", 1485), ("Queen Victoria", "1901", 1901), ("Henry VIII", "1547", 1547),
 ("George III", "1820", 1820), ("Elizabeth I", "1603", 1603), ("Charles I", "1649", 1649)])
game("the year of each battle", "British history", "medium", ["battles", "years"], [
 ("Agincourt", "1415", 1415), ("The Battle of Britain", "1940", 1940), ("Bosworth", "1485", 1485),
 ("Waterloo", "1815", 1815), ("Culloden", "1746", 1746), ("Trafalgar", "1805", 1805)])
game("roughly how fast, in mph?", "Science and nature", "hard", ["speed"], [
 ("Usain Bolt at full speed", "about 27.8 mph", 27.8), ("A peregrine falcon diving", "over 200 mph", 200), ("A garden snail", "about 0.03 mph", 0.03),
 ("Concorde at cruising speed", "about 1,350 mph", 1350), ("A racing greyhound", "about 45 mph", 45), ("A cheetah", "about 70 mph", 70)])
game("the year each world record was set", "Athletics", "hard", ["records", "years"], [
 ("Roger Bannister's four-minute mile", "1954", 1954), ("Usain Bolt's 9.58 seconds", "2009", 2009), ("Bob Beamon's long jump", "1968", 1968),
 ("Paula Radcliffe's marathon", "2003", 2003), ("Sunderland's Steve Cram's mile", "1985", 1985), ("Gateshead's Jonathan Edwards's triple jump", "1995", 1995)])
game("the year each comic or magazine began", "Nostalgia", "hard", ["comics", "magazines", "years"], [
 ("Radio Times", "1923", 1923), ("Viz (started in Newcastle)", "1979", 1979), ("The Dandy", "1937", 1937),
 ("Smash Hits", "1978", 1978), ("The Beano", "1938", 1938), ("Private Eye", "1961", 1961)])
game("the year of each tech first", "Science and technology", "medium", ["gadgets", "years"], [
 ("The Sony Walkman", "1979", 1979), ("The Nokia 3310", "2000", 2000), ("The CD", "1982", 1982),
 ("The first website", "1991", 1991), ("The first UK mobile phone call", "1985", 1985), ("Spotify", "2008", 2008)])
game("roughly how long is each pregnancy, in months?", "Animals", "medium", ["animals", "pregnancy"], [
 ("A dog", "about 2", 2), ("An elephant", "about 22", 22), ("A human", "about 9", 9), ("A giraffe", "about 15", 15), ("A horse", "about 11", 11)])
game("the year each North East landmark was built", "The North East", "hard", ["North East", "landmarks", "years"], [
 ("Newcastle's 'new castle'", "1080", 1080), ("The Sunderland Empire theatre", "1907", 1907), ("Grey's Monument", "1838", 1838),
 ("Sunderland's Northern Spire bridge", "2018", 2018), ("Newcastle Central Station", "1850", 1850), ("Penshaw Monument", "1844", 1844)])
game("how many events in each?", "The Olympics", "medium", ["multi-sport events"], [
 ("Biathlon", "2", 2), ("Decathlon", "10", 10), ("Triathlon", "3", 3), ("Heptathlon", "7", 7), ("Modern pentathlon", "5", 5)])
game("how many over or under par?", "Golf", "medium", ["golf", "scores"], [
 ("An albatross", "3 under", -3), ("A double bogey", "2 over", 2), ("An eagle", "2 under", -2), ("A bogey", "1 over", 1), ("A birdie", "1 under", -1)])
game("the year each newspaper was founded", "Newspapers", "hard", ["newspapers", "years"], [
 ("The Observer", "1791", 1791), ("The Independent", "1986", 1986), ("The Manchester Guardian", "1821", 1821),
 ("Metro", "1999", 1999), ("The Journal (Newcastle)", "1832", 1832), ("The Daily Mail", "1896", 1896)])
game("how many seconds?", "Maths and numbers", "easy", ["time"], [
 ("A minute", "60", 60), ("A day", "86,400", 86400), ("A quarter of an hour", "900", 900), ("An hour", "3,600", 3600), ("Half a minute", "30", 30)])
game("European Cup and Champions League wins, up to 2025", "Football", "medium", ["Champions League", "clubs"], [
 ("Celtic", "1", 1), ("Real Madrid", "15", 15), ("Nottingham Forest", "2", 2), ("AC Milan", "7", 7), ("Manchester United", "3", 3), ("Liverpool", "6", 6)])
game("the year of each great journey", "History", "medium", ["explorers", "years"], [
 ("Columbus reaches the Americas", "1492", 1492), ("Lindbergh flies solo across the Atlantic", "1927", 1927), ("Magellan's ship completes the first trip round the world", "1522", 1522),
 ("Amundsen reaches the South Pole", "1911", 1911), ("Captain Cook lands at Botany Bay", "1770", 1770)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-8.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
