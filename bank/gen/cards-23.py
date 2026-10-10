# Bank session 10 Oct 2026: 20 more Play Your Cards Right games -> bank/cards-23.json. A row of 5-7 cards each:
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

game("the year each children's game show began", "Nostalgia", "medium", ["game shows", "children's TV", "years"], [
 ("Knightmare", "1987", 1987), ("Raven", "2002", 2002), ("Fun House", "1989", 1989), ("Get Your Own Back", "1991", 1991), ("The Crystal Maze", "1990", 1990)])
game("the year each Disney park opened", "Days out", "medium", ["Disney", "theme parks", "years"], [
 ("Disneyland, California", "1955", 1955), ("Shanghai Disneyland", "2016", 2016), ("The Magic Kingdom, Florida", "1971", 1971),
 ("Hong Kong Disneyland", "2005", 2005), ("Epcot", "1982", 1982), ("Disneyland Paris", "1992", 1992)])
game("the year of each great sporting upset", "Sport", "medium", ["upsets", "years"], [
 ("Botham's Ashes at Headingley", "1981", 1981), ("Europe's 'Miracle at Medinah'", "2012", 2012), ("Dennis Taylor's black-ball final", "1985", 1985),
 ("Liverpool's comeback in Istanbul", "2005", 2005), ("Buster Douglas knocks out Tyson", "1990", 1990), ("Greece win the Euros", "2004", 2004)])
game("how many digits or characters?", "General knowledge", "medium", ["numbers", "everyday"], [
 ("A bank card PIN", "4", 4), ("A UK mobile number", "11", 11), ("A bank sort code", "6", 6), ("A credit card number", "16", 16), ("A UK bank account number", "8", 8), ("A new-style ISBN", "13", 13)])
game("the year each BBC children's show began", "Nostalgia", "medium", ["children's TV", "BBC", "years"], [
 ("Play School", "1964", 1964), ("Horrible Histories", "2009", 2009), ("Jackanory", "1965", 1965),
 ("The Story of Tracy Beaker", "2002", 2002), ("Newsround", "1972", 1972), ("Rentaghost", "1976", 1976)])
game("the year each indie or rock album came out", "Music", "medium", ["albums", "indie", "years"], [
 ("The Stone Roses: The Stone Roses", "1989", 1989), ("Coldplay: A Rush of Blood to the Head", "2002", 2002), ("Nirvana: Nevermind", "1991", 1991),
 ("Radiohead: OK Computer", "1997", 1997), ("Blur: Parklife", "1994", 1994), ("Pulp: Different Class", "1995", 1995)])
game("the year each beauty brand began", "Shopping", "hard", ["cosmetics", "brands", "years"], [
 ("Avon", "1886", 1886), ("Lush", "1995", 1995), ("L'Oréal", "1909", 1909), ("The Body Shop", "1976", 1976), ("Nivea", "1911", 1911), ("Superdrug", "1964", 1964)])
game("the year each country first hosted the World Cup", "Football", "medium", ["World Cup", "hosts", "years"], [
 ("England", "1966", 1966), ("Qatar", "2022", 2022), ("Uruguay", "1930", 1930), ("South Africa", "2010", 2010), ("Mexico", "1970", 1970), ("The USA", "1994", 1994)])
game("the year each royal was born (part two)", "The royal family", "medium", ["royals", "birthdays", "years"], [
 ("The Queen Mother", "1900", 1900), ("Prince Louis", "2018", 2018), ("Prince Philip", "1921", 1921),
 ("Prince Edward", "1964", 1964), ("Princess Margaret", "1930", 1930), ("Prince Andrew", "1960", 1960)])
game("the year each famous club night or venue opened", "Music", "hard", ["clubs", "venues", "years"], [
 ("Wigan Casino", "1973", 1973), ("Fabric, London", "1999", 1999), ("Studio 54, New York", "1977", 1977),
 ("Ministry of Sound", "1991", 1991), ("The Haçienda, Manchester", "1982", 1982), ("Cream, Liverpool", "1992", 1992)])
game("the year each picture book came out", "Books", "medium", ["picture books", "years"], [
 ("Where the Wild Things Are", "1963", 1963), ("Room on the Broom", "2001", 2001), ("The BFG", "1982", 1982),
 ("Guess How Much I Love You", "1994", 1994), ("We're Going on a Bear Hunt", "1989", 1989)])
game("the year women got the vote in each country", "World history", "hard", ["votes for women", "years"], [
 ("New Zealand", "1893", 1893), ("Saudi Arabia", "2015", 2015), ("Finland", "1906", 1906), ("Switzerland", "1971", 1971), ("The USA", "1920", 1920), ("France", "1944", 1944)])
game("the year of each crisis", "British history", "hard", ["crises", "years"], [
 ("The Suez Crisis", "1956", 1956), ("The fuel protests", "2000", 2000), ("The Cuban Missile Crisis", "1962", 1962),
 ("The poll tax riots", "1990", 1990), ("The Three-Day Week", "1974", 1974), ("The Winter of Discontent", "1979", 1979)])
game("the year each patriotic song was written", "Music", "hard", ["anthems", "years"], [
 ("Rule, Britannia!", "1740", 1740), ("I Vow to Thee, My Country (Holst's tune)", "1921", 1921), ("God Save the King (first printed)", "1745", 1745),
 ("Jerusalem (Parry's tune)", "1916", 1916), ("Land of Hope and Glory", "1902", 1902)])
game("the year each airport moment happened", "Travel", "hard", ["airports", "years"], [
 ("Manchester Airport opens", "1938", 1938), ("Heathrow's Terminal 5 opens", "2008", 2008), ("Heathrow opens", "1946", 1946),
 ("Liverpool's airport is named after John Lennon", "2001", 2001), ("London City Airport opens", "1987", 1987)])
game("the year each sketch show began", "Comedy", "medium", ["sketch shows", "years"], [
 ("Monty Python's Flying Circus", "1969", 1969), ("Little Britain", "2003", 2003), ("The Two Ronnies", "1971", 1971),
 ("Smack the Pony", "1999", 1999), ("Not the Nine O'Clock News", "1979", 1979), ("The Fast Show", "1994", 1994)])
game("how many steps to the top?", "Famous landmarks", "hard", ["steps", "landmarks"], [
 ("Whitby's steps up to the abbey", "199", 199), ("St Paul's, to the Golden Gallery", "528", 528), ("The Monument, London", "311", 311),
 ("The Eiffel Tower, to the second floor", "674", 674), ("Big Ben's Elizabeth Tower", "334", 334)])
game("the year of each charity record or concert", "Music", "medium", ["charity", "Band Aid", "years"], [
 ("Band Aid", "1984", 1984), ("Band Aid 30", "2014", 2014), ("Band Aid II", "1989", 1989), ("Live 8", "2005", 2005), ("Band Aid 20", "2004", 2004)])
game("the year each won the World Cup Golden Boot", "Football", "hard", ["World Cup", "Golden Boot", "years"], [
 ("Eusébio", "1966", 1966), ("Kylian Mbappé", "2022", 2022), ("Gerd Müller", "1970", 1970),
 ("Thomas Müller", "2010", 2010), ("Gary Lineker", "1986", 1986), ("Ronaldo (Brazil)", "2002", 2002)])
game("the year each way to pay arrived", "Money", "medium", ["payments", "years"], [
 ("The Barclaycard", "1966", 1966), ("Apple Pay in the UK", "2015", 2015), ("PayPal", "1998", 1998), ("Bitcoin", "2009", 2009), ("Chip and PIN becomes the rule", "2006", 2006)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-23.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
