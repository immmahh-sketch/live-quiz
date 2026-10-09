# Bank session 10 Oct 2026: 20 more Play Your Cards Right games -> bank/cards-20.json. A row of 5-7 cards each:
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

game("the year each chat show began", "Film and TV", "medium", ["chat shows", "years"], [
 ("The Late Late Show (Ireland)", "1962", 1962), ("The Graham Norton Show", "2007", 2007), ("Parkinson", "1971", 1971),
 ("Loose Women", "1999", 1999), ("Wogan", "1982", 1982), ("This Morning", "1988", 1988)])
game("the year of each medieval moment", "British history", "hard", ["medieval", "years"], [
 ("The Domesday Book", "1086", 1086), ("The Peasants' Revolt", "1381", 1381), ("Thomas Becket is murdered", "1170", 1170),
 ("The Black Death reaches England", "1348", 1348), ("The Battle of Bannockburn", "1314", 1314)])
game("the year of each Tudor or Stuart moment", "British history", "hard", ["Tudors", "Stuarts", "years"], [
 ("Henry VIII becomes king", "1509", 1509), ("The Great Plague of London", "1665", 1665), ("Henry breaks with Rome", "1534", 1534),
 ("Charles II is restored to the throne", "1660", 1660), ("Elizabeth I is crowned", "1559", 1559), ("Mary, Queen of Scots, is executed", "1587", 1587)])
game("the year of each Victorian moment", "British history", "medium", ["Victorians", "years"], [
 ("Victoria is crowned", "1838", 1838), ("Victoria's Diamond Jubilee", "1897", 1897), ("The Great Exhibition", "1851", 1851),
 ("Jack the Ripper's murders", "1888", 1888), ("The Great Stink in London", "1858", 1858)])
game("where does each sit on its scale?", "Science and nature", "hard", ["scales", "science"], [
 ("Talc, on the hardness scale", "1", 1), ("A hurricane, on the Beaufort wind scale", "12", 12), ("Pure water, on the pH scale", "7", 7),
 ("Diamond, on the hardness scale", "10", 10), ("Lemon juice, on the pH scale", "about 2", 2)])
game("the year of each royal upheaval", "The royal family", "medium", ["royals", "years"], [
 ("Edward VIII abdicates", "1936", 1936), ("Harry and Meghan step back", "2020", 2020), ("Princess Margaret gives up Peter Townsend", "1955", 1955),
 ("Prince Andrew's Newsnight interview", "2019", 2019), ("Charles and Diana separate", "1992", 1992)])
game("roughly how many miles is each horse race?", "Horse racing", "hard", ["races", "distances"], [
 ("The 2,000 Guineas", "1", 1), ("The Grand National", "about 4¼", 4.25), ("The Derby", "about 1½", 1.5),
 ("The Cheltenham Gold Cup", "about 3¼", 3.25), ("The St Leger", "about 1¾", 1.75)])
game("the year each won Sports Personality of the Year", "Sport", "medium", ["SPOTY", "years"], [
 ("Bobby Moore", "1966", 1966), ("Mo Farah", "2017", 2017), ("Ian Botham", "1981", 1981),
 ("Lewis Hamilton (his first)", "2014", 2014), ("Paul Gascoigne", "1990", 1990), ("David Beckham", "2001", 2001)])
game("the year each thrill ride opened", "Days out", "hard", ["rollercoasters", "years"], [
 ("Nemesis, Alton Towers", "1994", 1994), ("The Smiler, Alton Towers", "2013", 2013), ("Oblivion, Alton Towers", "1998", 1998),
 ("Stealth, Thorpe Park", "2006", 2006), ("The Corkscrew, Alton Towers", "1980", 1980)])
game("the year each radio station started", "Radio", "hard", ["radio", "years"], [
 ("Radio 1", "1967", 1967), ("talkSPORT", "2000", 2000), ("BBC Radio Newcastle", "1971", 1971),
 ("Radio 5 Live", "1994", 1994), ("Metro Radio", "1974", 1974), ("Classic FM", "1992", 1992)])
game("the year of each money moment", "Money", "hard", ["finance", "years"], [
 ("The 'Big Bang' in the City", "1986", 1986), ("Lehman Brothers collapses", "2008", 2008), ("Black Wednesday", "1992", 1992),
 ("The run on Northern Rock", "2007", 2007), ("The Bank of England is made independent", "1997", 1997)])
game("the atomic number of each element", "Science and nature", "hard", ["elements", "chemistry"], [
 ("Hydrogen", "1", 1), ("Gold", "79", 79), ("Carbon", "6", 6), ("Uranium", "92", 92), ("Oxygen", "8", 8), ("Iron", "26", 26)])
game("the year each group split (or someone left)", "Boy bands and girl groups", "medium", ["bands", "splits", "years"], [
 ("Wham!", "1986", 1986), ("One Direction go on a break", "2016", 2016), ("Take That (the first time)", "1996", 1996),
 ("Girls Aloud", "2013", 2013), ("Geri leaves the Spice Girls", "1998", 1998), ("Oasis", "2009", 2009)])
game("the year each Newcastle building opened", "The North East", "hard", ["Newcastle", "buildings", "years"], [
 ("The Tyne Theatre & Opera House", "1867", 1867), ("The Newcastle Arena", "1995", 1995), ("The Hancock Museum", "1884", 1884),
 ("The Civic Centre", "1968", 1968), ("Seven Stories, the children's book centre", "2005", 2005)])
game("the year each BBC drama began", "Film and TV", "medium", ["BBC", "drama", "years"], [
 ("Casualty", "1986", 1986), ("Doctor Foster", "2015", 2015), ("Holby City", "1999", 1999),
 ("Happy Valley", "2014", 2014), ("Call the Midwife", "2012", 2012), ("Peaky Blinders", "2013", 2013)])
game("the year each sci-fi series began", "Film and TV", "medium", ["science fiction", "TV", "years"], [
 ("Star Trek", "1966", 1966), ("Stranger Things", "2016", 2016), ("Blake's 7", "1978", 1978),
 ("Black Mirror", "2011", 2011), ("Red Dwarf", "1988", 1988), ("The X-Files", "1993", 1993)])
game("the year each competition began", "Sport", "hard", ["leagues", "years"], [
 ("Rugby league's Super League", "1996", 1996), ("Cricket's The Hundred", "2021", 2021), ("The Six Nations", "2000", 2000),
 ("The Women's Super League", "2011", 2011), ("Twenty20 county cricket", "2003", 2003)])
game("the old measures", "Maths and numbers", "hard", ["imperial", "old measures"], [
 ("Inches in a hand (for horses)", "4", 4), ("Acres in a square mile", "640", 640), ("Feet in a fathom", "6", 6),
 ("Chains in a mile", "80", 80), ("Furlongs in a mile", "8", 8), ("Yards in a chain", "22", 22)])
game("the year each animation studio began", "Film", "hard", ["animation", "studios", "years"], [
 ("Disney", "1923", 1923), ("DreamWorks", "1994", 1994), ("Aardman", "1972", 1972), ("Pixar", "1986", 1986), ("Studio Ghibli", "1985", 1985)])
game("the year each first headlined Glastonbury", "Music", "hard", ["Glastonbury", "years"], [
 ("Paul McCartney", "2004", 2004), ("Stormzy", "2019", 2019), ("Jay-Z", "2008", 2008), ("Adele", "2016", 2016), ("Beyoncé", "2011", 2011)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-20.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
