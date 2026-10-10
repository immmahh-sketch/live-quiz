# Bank session 10 Oct 2026: 20 more Play Your Cards Right games -> bank/cards-27.json. A row of 5-7 cards each:
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

game("the year each children's TV classic began", "Nostalgia", "medium", ["children's TV", "years"], [
 ("Captain Pugwash", "1957", 1957), ("Count Duckula", "1988", 1988), ("Thunderbirds", "1965", 1965), ("The Raggy Dolls", "1986", 1986), ("Mr Benn", "1971", 1971), ("SuperTed", "1982", 1982)])
game("the year each sports brand began", "Sport", "hard", ["sports brands", "years"], [
 ("Mitre", "1817", 1817), ("Under Armour", "1996", 1996), ("Slazenger", "1881", 1881), ("Lonsdale", "1960", 1960), ("Gola", "1905", 1905), ("Puma", "1948", 1948)])
game("the year each classic sitcom began", "Comedy", "medium", ["sitcoms", "years"], [
 ("Steptoe and Son", "1962", 1962), ("Miranda", "2009", 2009), ("Rising Damp", "1974", 1974), ("The IT Crowd", "2006", 2006), ("The Good Life", "1975", 1975), ("The Vicar of Dibley", "1994", 1994)])
game("the year of each moment in American history", "World history", "medium", ["USA", "years"], [
 ("Prohibition begins", "1920", 1920), ("Barack Obama is elected", "2008", 2008), ("Pearl Harbor", "1941", 1941), ("Hurricane Katrina", "2005", 2005), ("The Civil Rights Act", "1964", 1964)])
game("the year of each moment in European history", "World history", "hard", ["Europe", "years"], [
 ("The Spanish Civil War begins", "1936", 1936), ("The Velvet Revolution", "1989", 1989), ("The Prague Spring", "1968", 1968), ("Chernobyl", "1986", 1986), ("Portugal's Carnation Revolution", "1974", 1974)])
game("how many letters in each long word?", "Words and language", "hard", ["long words", "letters"], [
 ("Antidisestablishmentarianism", "28", 28), ("Pneumonoultramicroscopicsilicovolcanoconiosis", "45", 45), ("Honorificabilitudinitatibus", "27", 27),
 ("Supercalifragilisticexpialidocious", "34", 34), ("Floccinaucinihilipilification", "29", 29), ("Uncopyrightable", "15", 15)])
game("the year of each North East sporting moment", "The North East", "hard", ["North East", "sport", "years"], [
 ("Durham become a first-class cricket county", "1992", 1992), ("Middlesbrough reach the UEFA Cup final", "2006", 2006), ("Newcastle Falcons win the Premiership", "1998", 1998),
 ("Durham's first County Championship", "2008", 2008), ("Middlesbrough win the League Cup", "2004", 2004)])
game("each speed record, in mph", "Science and technology", "hard", ["speed records"], [
 ("Mallard, the steam engine", "126 mph", 126), ("Thrust SSC on land", "763 mph", 763), ("The fastest tennis serve", "163 mph", 163),
 ("Bluebird K7 on water", "276 mph", 276), ("The fastest anyone has ridden a bicycle", "183.9 mph", 183.9)])
game("the year each British design classic arrived", "Britain", "hard", ["design", "years"], [
 ("The Anglepoise lamp", "1932", 1932), ("The Routemaster bus", "1956", 1956), ("Harry Beck's Tube map", "1933", 1933),
 ("The Kenwood Chef", "1950", 1950), ("Penguin paperbacks", "1935", 1935), ("The 'Keep Calm and Carry On' poster", "1939", 1939)])
game("the year of each great discovery about the universe", "Space", "hard", ["astronomy", "years"], [
 ("Lemaître's 'primeval atom' (the Big Bang idea)", "1927", 1927), ("The first picture of a black hole", "2019", 2019), ("Hubble shows the universe is expanding", "1929", 1929),
 ("Gravitational waves are detected", "2015", 2015), ("Jocelyn Bell Burnell finds pulsars", "1967", 1967), ("The cosmic microwave background is found", "1965", 1965)])
game("the year each newspaper or magazine was founded", "Newspapers", "hard", ["newspapers", "years"], [
 ("The Economist", "1843", 1843), ("The i", "2010", 2010), ("The Daily Telegraph", "1855", 1855), ("The Sun", "1964", 1964), ("The Financial Times", "1888", 1888), ("The Daily Mirror", "1903", 1903)])
game("the year each restaurant chain opened its first UK branch", "Food and drink", "hard", ["restaurants", "years"], [
 ("Pizza Express", "1965", 1965), ("Five Guys", "2013", 2013), ("Harvester", "1983", 1983), ("Zizzi", "1999", 1999), ("TGI Fridays", "1986", 1986), ("Wagamama", "1992", 1992)])
game("the year each music magazine began", "Music", "hard", ["magazines", "years"], [
 ("Melody Maker", "1926", 1926), ("Mojo", "1993", 1993), ("NME", "1952", 1952), ("Q", "1986", 1986), ("Rolling Stone", "1967", 1967), ("Kerrang!", "1981", 1981)])
game("the year of each royal wedding", "The royal family", "medium", ["royal weddings", "years"], [
 ("Princess Elizabeth and Philip", "1947", 1947), ("Princess Beatrice", "2020", 2020), ("Princess Margaret", "1960", 1960),
 ("Charles and Camilla", "2005", 2005), ("Princess Anne (the first time)", "1973", 1973), ("Andrew and Sarah", "1986", 1986)])
game("the year each handheld console came out", "Games and toys", "medium", ["consoles", "years"], [
 ("The Atari Lynx", "1989", 1989), ("The Steam Deck", "2022", 2022), ("The Sega Game Gear", "1990", 1990),
 ("The Nintendo 3DS", "2011", 2011), ("The Game Boy Advance", "2001", 2001), ("The Nintendo DS", "2004", 2004)])
game("the year each American festival began", "Music", "hard", ["festivals", "years"], [
 ("The Monterey Pop Festival", "1967", 1967), ("Coachella", "1999", 1999), ("Burning Man", "1986", 1986), ("Lollapalooza", "1991", 1991), ("SXSW", "1987", 1987)])
game("the year each British film hit came out", "Film", "medium", ["British films", "years"], [
 ("Brassed Off", "1996", 1996), ("Paddington", "2014", 2014), ("The Full Monty", "1997", 1997),
 ("This Is England", "2006", 2006), ("Lock, Stock and Two Smoking Barrels", "1998", 1998), ("Calendar Girls", "2003", 2003)])
game("the year each horror villain first appeared", "Film", "medium", ["horror", "villains", "years"], [
 ("Norman Bates (in the novel Psycho)", "1959", 1959), ("Chucky", "1988", 1988), ("Leatherface", "1974", 1974),
 ("Pinhead", "1987", 1987), ("Mrs Voorhees (Friday the 13th)", "1980", 1980), ("Freddy Krueger", "1984", 1984)])
game("the year each piece of everyday tech arrived", "Science and technology", "hard", ["technology", "years"], [
 ("The JPEG", "1992", 1992), ("The first emoji set", "1999", 1999), ("The QR code", "1994", 1994), ("Wi-Fi", "1997", 1997), ("The PDF", "1993", 1993), ("USB", "1996", 1996)])
game("the year each landmark documentary series first aired", "Film and TV", "medium", ["documentaries", "years"], [
 ("Civilisation", "1969", 1969), ("Blue Planet II", "2017", 2017), ("Life on Earth", "1979", 1979),
 ("Frozen Planet", "2011", 2011), ("The Blue Planet", "2001", 2001), ("Planet Earth", "2006", 2006)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-27.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
