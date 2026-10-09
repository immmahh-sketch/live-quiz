# Bank session 10 Oct 2026: 20 more Play Your Cards Right games -> bank/cards-11.json. A row of 5-7 cards each:
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

game("the year each music show began", "Music", "hard", ["music TV", "years"], [
 ("Ready Steady Go!", "1963", 1963), ("The X Factor", "2004", 2004), ("Top of the Pops", "1964", 1964),
 ("Pop Idol", "2001", 2001), ("The Old Grey Whistle Test", "1971", 1971), ("Later... with Jools Holland", "1992", 1992)])
game("the year each children's TV show began", "Film and TV", "medium", ["children's TV", "years"], [
 ("Rainbow", "1972", 1972), ("Teletubbies", "1997", 1997), ("Bagpuss", "1974", 1974),
 ("Thomas the Tank Engine & Friends", "1984", 1984), ("Grange Hill", "1978", 1978), ("Postman Pat", "1981", 1981)])
game("the year of each sporting first", "Sport", "hard", ["sport history", "years"], [
 ("The first Grand National", "1839", 1839), ("The first Tour de France", "1903", 1903), ("The Football Association is founded", "1863", 1863),
 ("The first modern Olympics", "1896", 1896), ("The first FA Cup final", "1872", 1872), ("The first Football League season", "1888", 1888)])
game("the numbers in cricket", "Cricket", "medium", ["cricket", "numbers"], [
 ("Stumps at each end", "3", 3), ("Runs for clearing the rope", "6", 6), ("Bails on the stumps", "2", 2),
 ("Players in a team", "11", 11), ("Balls in an over", "6", 6), ("Days in a Test match", "5", 5)])
game("the year each coin or note was withdrawn", "Money", "hard", ["money", "years"], [
 ("The halfpenny", "1984", 1984), ("The paper £20 note", "2022", 2022), ("The sixpence", "1980", 1980),
 ("The round £1 coin", "2017", 2017), ("The big 50p", "1998", 1998), ("The paper £10 note", "2018", 2018)])
game("the year each composer died", "Classical music", "hard", ["composers", "years"], [
 ("Bach", "1750", 1750), ("Elgar", "1934", 1934), ("Handel", "1759", 1759), ("Tchaikovsky", "1893", 1893), ("Mozart", "1791", 1791), ("Beethoven", "1827", 1827)])
game("the year each festival began", "Days out", "hard", ["festivals", "years"], [
 ("The Hoppings on Newcastle's Town Moor", "1882", 1882), ("The Hay Festival", "1988", 1988), ("The Proms", "1895", 1895),
 ("Notting Hill Carnival", "1966", 1966), ("The Chelsea Flower Show", "1913", 1913), ("The Edinburgh Festival", "1947", 1947)])
game("golf majors won, up to 2025", "Golf", "hard", ["golf", "majors"], [
 ("Tony Jacklin", "2", 2), ("Jack Nicklaus", "18", 18), ("Nick Faldo", "6", 6), ("Tiger Woods", "15", 15), ("Rory McIlroy", "5", 5), ("Gary Player", "9", 9)])
game("Tour de France wins", "Cycling", "hard", ["cycling", "Tour de France"], [
 ("Bradley Wiggins", "1", 1), ("Eddy Merckx", "5", 5), ("Geraint Thomas", "1", 1), ("Chris Froome", "4", 4), ("Bernard Hinault", "5", 5)])
game("the year each North East attraction opened", "The North East", "hard", ["North East", "attractions", "years"], [
 ("Eldon Square shopping centre", "1976", 1976), ("The National Glass Centre, Sunderland", "1998", 1998), ("Kielder Water", "1982", 1982),
 ("The Alnwick Garden", "2001", 2001), ("The Metrocentre", "1986", 1986), ("The Centre for Life", "2000", 2000)])
game("the year each mascot first appeared", "Adverts and brands", "hard", ["mascots", "adverts", "years"], [
 ("The Michelin Man", "1898", 1898), ("Compare the Meerkat", "2009", 2009), ("Tony the Tiger", "1952", 1952),
 ("The Andrex puppy", "1972", 1972), ("The PG Tips chimps", "1956", 1956), ("Ronald McDonald", "1963", 1963)])
game("the numbers of the Olympic Games", "The Olympics", "medium", ["Olympics", "numbers"], [
 ("Olympic rings", "5", 5), ("Michael Phelps's gold medals", "23", 23), ("Years between Summer Games", "4", 4),
 ("Sports at Paris 2024", "32", 32), ("Nations at Paris 2024", "206", 206)])
game("the year each high-street chain collapsed", "Shopping", "medium", ["shops", "years"], [
 ("Woolworths", "2008", 2008), ("Debenhams", "2020", 2020), ("Comet", "2012", 2012), ("Toys R Us (UK)", "2018", 2018), ("Blockbuster (UK)", "2013", 2013), ("BHS", "2016", 2016)])
game("the year each horror film came out", "Film", "medium", ["horror", "films", "years"], [
 ("Psycho", "1960", 1960), ("Get Out", "2017", 2017), ("The Exorcist", "1973", 1973), ("Scream", "1996", 1996), ("Halloween", "1978", 1978), ("The Shining", "1980", 1980)])
game("the year each detective first appeared in a book", "Books", "hard", ["detectives", "years"], [
 ("Father Brown", "1910", 1910), ("Vera Stanhope", "1999", 1999), ("Hercule Poirot", "1920", 1920), ("Rebus", "1987", 1987), ("Inspector Morse", "1975", 1975)])
game("the year each country became independent", "World history", "hard", ["independence", "years"], [
 ("The USA", "1776", 1776), ("South Sudan", "2011", 2011), ("Australia (as one country)", "1901", 1901),
 ("Jamaica", "1962", 1962), ("Ireland (the Free State)", "1922", 1922), ("India", "1947", 1947)])
game("the year each football rule came in", "Football", "hard", ["rules", "years"], [
 ("The penalty kick", "1891", 1891), ("VAR in the Premier League", "2019", 2019), ("Substitutes in the Football League", "1965", 1965),
 ("The back-pass rule", "1992", 1992), ("Yellow and red cards, at the World Cup", "1970", 1970), ("Three points for a win in England", "1981", 1981)])
game("the year each charity began", "Charities", "hard", ["charities", "years"], [
 ("The RNLI", "1824", 1824), ("The first Children in Need telethon", "1980", 1980), ("Barnardo's", "1866", 1866),
 ("The first Red Nose Day", "1988", 1988), ("Macmillan", "1911", 1911), ("Oxfam", "1942", 1942)])
game("imperial into metric", "Maths and numbers", "hard", ["measures", "conversions"], [
 ("Millilitres in a pint", "568", 568), ("Centimetres in an inch", "2.54", 2.54), ("Grams in an ounce", "28.35", 28.35),
 ("Kilometres in a mile", "1.61", 1.61), ("Litres in a gallon", "4.55", 4.55), ("Metres in a yard", "0.91", 0.91)])
game("how many dots?", "Games and toys", "medium", ["dice", "dominoes"], [
 ("All the spots on one dice", "21", 21), ("Opposite sides of a dice, added up", "7", 7), ("A double-six domino", "12", 12),
 ("A seven-spot ladybird", "7", 7), ("Snake eyes", "2", 2)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-11.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
