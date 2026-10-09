# Bank session 10 Oct 2026: 20 more Play Your Cards Right games -> bank/cards-10.json. A row of 5-7 cards each:
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

game("the year each Elton John song came out", "Music", "hard", ["Elton John", "years"], [
 ("Your Song", "1970", 1970), ("I'm Still Standing", "1983", 1983), ("Rocket Man", "1972", 1972),
 ("Can You Feel the Love Tonight", "1994", 1994), ("Candle in the Wind (the first version)", "1973", 1973)])
game("the year each first appeared in Doctor Who", "Doctor Who", "hard", ["Doctor Who", "monsters", "years"], [
 ("The Daleks", "1963", 1963), ("The Weeping Angels", "2007", 2007), ("The Cybermen", "1966", 1966),
 ("K9", "1977", 1977), ("The Master", "1971", 1971), ("The Sontarans", "1973", 1973)])
game("the year each Christmas tradition began", "Christmas", "hard", ["Christmas", "traditions", "years"], [
 ("The first Christmas card", "1843", 1843), ("The first televised royal Christmas message", "1957", 1957), ("Christmas crackers", "1847", 1847),
 ("Band Aid", "1984", 1984), ("The first royal Christmas broadcast, on radio", "1932", 1932), ("Norway's tree in Trafalgar Square", "1947", 1947)])
game("the year each superhero first appeared", "Film and comics", "hard", ["superheroes", "years"], [
 ("Superman", "1938", 1938), ("Deadpool", "1991", 1991), ("Batman", "1939", 1939),
 ("Black Panther", "1966", 1966), ("Wonder Woman", "1941", 1941), ("Spider-Man", "1962", 1962)])
game("the year it happened", "World history", "medium", ["world events", "years"], [
 ("The Russian Revolution", "1917", 1917), ("The 9/11 attacks", "2001", 2001), ("The Wall Street Crash", "1929", 1929),
 ("Nelson Mandela is freed", "1990", 1990), ("JFK is shot", "1963", 1963), ("Euro notes and coins arrive", "2002", 2002)])
game("the number in each TV title", "Film and TV", "medium", ["TV", "numbers"], [
 ("Room ___", "101", 101), ("___ Pints of Lager and a Packet of Crisps", "2", 2), ("___ Rock", "30", 30),
 ("Brooklyn Nine-___", "9", 9), ("Kiefer Sutherland's '___'", "24", 24), ("___ to One", "15", 15)])
game("the year of each great discovery", "Science and nature", "hard", ["science", "years"], [
 ("Newton's Principia", "1687", 1687), ("The Higgs boson is found", "2012", 2012), ("Darwin's On the Origin of Species", "1859", 1859),
 ("The double helix of DNA", "1953", 1953), ("Einstein's special relativity", "1905", 1905), ("Fleming finds penicillin", "1928", 1928)])
game("roughly how many miles?", "Space", "hard", ["distances", "Earth"], [
 ("Up to the top of Everest", "about 5.5", 5.5), ("To the Moon", "about 239,000", 239000), ("Up to the space station", "about 250", 250),
 ("Round the Earth at the equator", "about 24,900", 24900), ("Straight through the middle of the Earth", "about 7,900", 7900)])
game("the year each North East TV show began", "The North East", "medium", ["North East", "TV", "years"], [
 ("When the Boat Comes In", "1976", 1976), ("Geordie Shore", "2011", 2011), ("The Tube", "1982", 1982),
 ("Sunderland 'Til I Die", "2018", 2018), ("Auf Wiedersehen, Pet", "1983", 1983), ("Byker Grove", "1989", 1989)])
game("the numbers in golf", "Golf", "hard", ["golf", "rules"], [
 ("Men's majors in a year", "4", 4), ("Par for most championship courses", "72", 72), ("The width of the hole, in inches", "4.25", 4.25),
 ("Clubs allowed in your bag", "14", 14), ("Minutes allowed to look for a lost ball", "3", 3)])
game("the numbers in Formula One (2025)", "Motor sport", "medium", ["F1", "numbers"], [
 ("Points for 10th place", "1", 1), ("Points for a win", "25", 25), ("Teams", "10", 10), ("Points for 2nd place", "18", 18), ("Cars on the grid", "20", 20)])
game("the year each North East business began", "The North East", "hard", ["North East", "business", "years"], [
 ("Ringtons tea", "1907", 1907), ("Nissan's Sunderland plant", "1986", 1986), ("Domestos (invented in Newcastle)", "1929", 1929),
 ("Northern Rock", "1965", 1965), ("Tyne Tees Television", "1959", 1959)])
game("the numbers of planet Earth", "Science and nature", "medium", ["Earth", "numbers"], [
 ("Oceans", "5", 5), ("Hours for the Earth to spin once", "24", 24), ("Continents", "7", 7),
 ("Days for the Moon to go round the Earth", "about 27.3", 27.3), ("Degrees the Earth is tilted", "about 23.5", 23.5)])
game("what % voted for the winning side?", "Politics", "hard", ["referendums", "votes"], [
 ("Welsh devolution (1997): Yes", "50.3%", 50.3), ("Scottish devolution (1997): Yes", "74.3%", 74.3), ("Brexit (2016): Leave", "51.9%", 51.9),
 ("The AV vote (2011): No", "67.9%", 67.9), ("Scottish independence (2014): No", "55.3%", 55.3), ("Staying in the EEC (1975): Yes", "67.2%", 67.2)])
game("the year each North East star was born", "The North East", "hard", ["North East", "birthdays", "years"], [
 ("Catherine Cookson", "1906", 1906), ("Cheryl", "1983", 1983), ("Sting", "1951", 1951),
 ("Ant McPartlin", "1975", 1975), ("Jimmy Nail", "1954", 1954), ("Alan Shearer", "1970", 1970)])
game("the phone code for each place (without the 0)", "Britain", "medium", ["dialling codes"], [
 ("Newcastle", "0191", 191), ("London", "020", 20), ("Manchester", "0161", 161), ("Leeds", "0113", 113), ("Edinburgh", "0131", 131), ("Birmingham", "0121", 121)])
game("how heavy, in kilograms?", "Science and nature", "medium", ["weights"], [
 ("A bag of sugar", "1 kg", 1), ("A men's Olympic shot", "7.26 kg", 7.26), ("A typical newborn baby", "about 3.5 kg", 3.5),
 ("One stone", "6.35 kg", 6.35), ("A women's Olympic shot", "4 kg", 4)])
game("the year each ship was launched", "History", "hard", ["ships", "years"], [
 ("The Mary Rose", "1511", 1511), ("The Titanic", "1911", 1911), ("HMS Victory", "1765", 1765),
 ("The Queen Mary", "1934", 1934), ("The Cutty Sark", "1869", 1869), ("The Mauretania (built on the Tyne)", "1906", 1906)])
game("the number in each band's name", "Music", "easy", ["bands", "numbers"], [
 ("U___", "2", 2), ("Blink-___", "182", 182), ("Maroon ___", "5", 5), ("UB___", "40", 40), ("S Club ___", "7", 7), ("East ___", "17", 17)])
game("the year of each railway milestone", "Britain", "hard", ["railways", "years"], [
 ("The Flying Scotsman is built", "1923", 1923), ("The Elizabeth line opens", "2022", 2022), ("Mallard's speed record", "1938", 1938),
 ("The InterCity 125 enters service", "1976", 1976), ("The Beeching Report", "1963", 1963)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-10.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
