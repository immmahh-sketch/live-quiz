# Bank session 10 Oct 2026: 20 more Play Your Cards Right games -> bank/cards-24.json. A row of 5-7 cards each:
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

game("how many in each part of the UK?", "Britain", "hard", ["counties", "geography"], [
 ("Counties in Northern Ireland", "6", 6), ("Ceremonial counties in England", "48", 48), ("Preserved counties in Wales", "8", 8),
 ("Council areas in Scotland", "32", 32), ("National parks in the UK", "15", 15)])
game("the year each British city hosted Eurovision", "Eurovision", "hard", ["Eurovision", "hosts", "years"], [
 ("London (the first time)", "1960", 1960), ("Liverpool", "2023", 2023), ("Edinburgh", "1972", 1972),
 ("Birmingham", "1998", 1998), ("Brighton", "1974", 1974), ("Harrogate", "1982", 1982)])
game("the year each music legend died", "Music", "medium", ["musicians", "years"], [
 ("Buddy Holly", "1959", 1959), ("Prince", "2016", 2016), ("Jimi Hendrix", "1970", 1970),
 ("Whitney Houston", "2012", 2012), ("Marc Bolan", "1977", 1977), ("Kurt Cobain", "1994", 1994)])
game("the year of each famous voyage", "History", "hard", ["voyages", "ships", "years"], [
 ("The Mayflower sails to America", "1620", 1620), ("The Kon-Tiki raft crosses the Pacific", "1947", 1947), ("Cook's Endeavour sets sail", "1768", 1768),
 ("The Lusitania is sunk", "1915", 1915), ("Darwin's Beagle sets sail", "1831", 1831)])
game("the year each Prime Minister was born", "Politics", "hard", ["Prime Ministers", "birthdays", "years"], [
 ("Clement Attlee", "1883", 1883), ("David Cameron", "1966", 1966), ("Harold Wilson", "1916", 1916),
 ("Tony Blair", "1953", 1953), ("Margaret Thatcher", "1925", 1925), ("John Major", "1943", 1943)])
game("the year each British comedy film came out", "Film", "medium", ["comedy", "British films", "years"], [
 ("Carry On Sergeant", "1958", 1958), ("In Bruges", "2008", 2008), ("The Italian Job", "1969", 1969),
 ("Shaun of the Dead", "2004", 2004), ("Withnail and I", "1987", 1987), ("A Fish Called Wanda", "1988", 1988)])
game("the year of each wild British weather event", "Britain", "medium", ["weather", "years"], [
 ("London's Great Smog", "1952", 1952), ("Storm Arwen batters the North East", "2021", 2021), ("The Big Freeze", "1963", 1963),
 ("The 'Beast from the East'", "2018", 2018), ("The Great Storm", "1987", 1987), ("The Boscastle flood", "2004", 2004)])
game("the year of each Olympic first", "The Olympics", "hard", ["Olympics", "firsts", "years"], [
 ("Women compete for the first time", "1900", 1900), ("The first Paralympics", "1960", 1960), ("London's first Games", "1908", 1908),
 ("The first torch relay", "1936", 1936), ("The first Winter Olympics", "1924", 1924)])
game("the year each record shop opened its first store", "Music", "hard", ["record shops", "years"], [
 ("Woolworths' first UK store", "1909", 1909), ("Fopp", "1981", 1981), ("HMV", "1921", 1921), ("The Virgin Megastore", "1979", 1979), ("Our Price", "1971", 1971)])
game("total stopping distance in metres (Highway Code)", "Driving", "hard", ["stopping distances", "Highway Code"], [
 ("At 30 mph", "23 m", 23), ("At 70 mph", "96 m", 96), ("At 20 mph", "12 m", 12), ("At 60 mph", "73 m", 73), ("At 40 mph", "36 m", 36), ("At 50 mph", "53 m", 53)])
game("the year of each Christmas TV moment", "Christmas", "medium", ["Christmas TV", "years"], [
 ("Morecambe & Wise's record Christmas audience", "1977", 1977), ("The Gavin & Stacey finale", "2024", 2024), ("The Snowman is first shown", "1982", 1982),
 ("Doctor Who's first modern Christmas special", "2005", 2005), ("Only Fools' 'Time on Our Hands'", "1996", 1996)])
game("the year each BBC Two show began", "Film and TV", "medium", ["BBC Two", "years"], [
 ("Top Gear (the original)", "1977", 1977), ("Dragons' Den", "2005", 2005), ("Newsnight", "1980", 1980), ("QI", "2003", 2003), ("Never Mind the Buzzcocks", "1996", 1996)])
game("the year of each flying first", "History", "hard", ["aviation", "years"], [
 ("Amy Johnson flies solo to Australia", "1930", 1930), ("The A380's first flight", "2005", 2005), ("The first flight over Everest", "1933", 1933),
 ("Freddie Laker's Skytrain", "1977", 1977), ("The Comet, the first jet airliner, carries passengers", "1952", 1952)])
game("the year each royal home came to the royals", "The royal family", "hard", ["royal homes", "years"], [
 ("Kensington Palace", "1689", 1689), ("Highgrove", "1980", 1980), ("Clarence House is built", "1827", 1827),
 ("Sandringham", "1862", 1862), ("Balmoral", "1852", 1852)])
game("the year each sports film came out", "Film", "medium", ["sport", "films", "years"], [
 ("Rocky", "1976", 1976), ("Million Dollar Baby", "2004", 2004), ("Raging Bull", "1980", 1980),
 ("Space Jam", "1996", 1996), ("Chariots of Fire", "1981", 1981), ("Cool Runnings", "1993", 1993)])
game("the number you'd dial", "General knowledge", "medium", ["phone numbers"], [
 ("NHS non-emergency", "111", 111), ("Emergency in the USA", "911", 911), ("Police non-emergency", "101", 101),
 ("The directory enquiries with the moustached runners", "118 118", 118118), ("Emergency anywhere in Europe", "112", 112),
 ("Directory enquiries, the old way", "192", 192), ("Emergency in the UK", "999", 999)])
game("the year each change came to Wimbledon", "Tennis", "hard", ["Wimbledon", "years"], [
 ("The Open era begins", "1968", 1968), ("A tie-break in the final set", "2019", 2019), ("Tie-breaks arrive", "1971", 1971),
 ("Centre Court gets a roof", "2009", 2009), ("Yellow balls", "1986", 1986), ("Hawk-Eye", "2007", 2007)])
game("the year each car went out of production", "Cars", "hard", ["cars", "years"], [
 ("The Morris Minor", "1971", 1971), ("The Ford Fiesta", "2023", 2023), ("The Ford Cortina", "1982", 1982),
 ("The original Land Rover Defender", "2016", 2016), ("The original VW Beetle", "2003", 2003)])
game("the year of each star's first UK number one", "Music", "hard", ["number ones", "years"], [
 ("Cliff Richard", "1959", 1959), ("Ed Sheeran", "2014", 2014), ("George Michael", "1984", 1984),
 ("Adele", "2011", 2011), ("Kylie Minogue", "1988", 1988), ("Robbie Williams", "1998", 1998)])
game("the year each fast-food favourite arrived", "Food and drink", "medium", ["fast food", "years"], [
 ("The Whopper", "1957", 1957), ("Greggs' vegan sausage roll", "2019", 2019), ("The Filet-O-Fish", "1962", 1962),
 ("The McFlurry", "1997", 1997), ("The Big Mac", "1967", 1967), ("Chicken McNuggets", "1983", 1983)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-24.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
