# Bank session 10 Oct 2026: 14 more Play Your Cards Right games -> bank/cards-29.json. A row of 5-7 cards each:
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

game("the odd numbers inside animals", "Animals", "hard", ["animals", "anatomy"], [
 ("Eyes on most spiders", "8", 8), ("Hearts in an octopus", "3", 3), ("'Hearts' in an earthworm", "5", 5),
 ("Kidneys in a human", "2", 2), ("Stomach chambers in a cow", "4", 4), ("Eyes on a honeybee", "5", 5)])
game("how many Olympics (Summer and Winter) has each country hosted, up to 2026?", "Sport", "hard", ["Olympics", "hosts"], [
 ("The USA", "8", 8), ("Australia", "2", 2), ("France", "6", 6), ("The UK", "3", 3), ("Italy", "4", 4), ("Greece", "2", 2)])
game("how many pips?", "Games and toys", "medium", ["dice", "dominoes", "cards"], [
 ("A full set of double-six dominoes", "168", 168), ("The ace of spades", "1", 1), ("All six faces of one dice", "21", 21),
 ("The five on a dice", "5", 5), ("The double-six domino", "12", 12), ("The seven of hearts", "7", 7)])
game("roughly how many miles long is each walking trail?", "Britain", "hard", ["walking", "National Trails"], [
 ("The Pennine Way", "268", 268), ("Hadrian's Wall Path", "84", 84), ("The South West Coast Path", "630", 630),
 ("The West Highland Way", "96", 96), ("Offa's Dyke Path", "177", 177), ("The Thames Path", "184", 184)])
game("the numbers in a pack of cards", "Games and toys", "easy", ["playing cards"], [
 ("Cards (without jokers)", "52", 52), ("Jokers", "2", 2), ("Red cards", "26", 26), ("Suits", "4", 4), ("Picture cards", "12", 12), ("Hearts", "13", 13)])
game("the numbers in Harry Potter", "Harry Potter", "medium", ["Harry Potter", "numbers"], [
 ("The platform at King's Cross", "9¾", 9.75), ("Hogwarts houses", "4", 4), ("Points for catching the Golden Snitch", "150", 150),
 ("Books in the series", "7", 7), ("Harry's age when he starts Hogwarts", "11", 11), ("Number of the Dursleys' house on Privet Drive", "4", 4)])
game("the numbers in a football match", "Football", "easy", ["football", "rules"], [
 ("Minutes of normal time", "90", 90), ("Substitutes allowed in the Premier League", "5", 5), ("Players a side", "11", 11),
 ("Minutes of extra time", "30", 30), ("Most minutes allowed for half-time", "15", 15), ("Penalties each in a shoot-out, before sudden death", "5", 5)])
game("the numbers in Star Wars", "Star Wars", "hard", ["Star Wars", "numbers"], [
 ("Order ___", "66", 66), ("Death Stars blown up in the original trilogy", "2", 2), ("Stormtrooper TK-___", "421", 421),
 ("Parsecs for the Kessel Run", "12", 12), ("Docking Bay ___ in Mos Eisley", "94", 94), ("Films in the Skywalker saga", "9", 9)])
game("the numbers in Friends", "Film and TV", "medium", ["Friends", "sitcoms"], [
 ("Episodes made", "236", 236), ("Times Ross got married", "3", 3), ("Joey and Chandler's apartment number", "19", 19),
 ("Series (seasons)", "10", 10), ("Friends in the gang", "6", 6)])
game("the numbers in chess", "Games and toys", "easy", ["chess"], [
 ("Squares on the board", "64", 64), ("Pawns each", "8", 8), ("Pieces on the board at the start", "32", 32), ("Knights each", "2", 2), ("Pieces each", "16", 16)])
game("the numbers in athletics", "Sport", "medium", ["athletics", "running"], [
 ("Metres in one lap of the track", "400", 400), ("Runners in a relay team", "4", 4), ("Jumps (barriers and water) in the 3,000 m steeplechase", "35", 35),
 ("Miles in a marathon", "26.2", 26.2), ("Hurdles in the 110 m hurdles", "10", 10)])
game("the numbers in ten-pin bowling", "Sport", "medium", ["bowling"], [
 ("A perfect score", "300", 300), ("Finger holes in a standard ball", "3", 3), ("Pins", "10", 10), ("Length of the lane, in feet", "60", 60), ("Heaviest ball allowed, in pounds", "16", 16)])
game("the numbers in boxing", "Sport", "medium", ["boxing"], [
 ("Rounds in a world title fight", "12", 12), ("Sides of the ring", "4", 4), ("The referee's count", "10", 10),
 ("Rounds in an Olympic bout", "3", 3), ("Weight divisions in men's professional boxing", "17", 17)])
game("the numbers in basketball", "Sport", "medium", ["basketball"], [
 ("Seconds on the NBA shot clock", "24", 24), ("Players on court per team", "5", 5), ("Height of the hoop, in feet", "10", 10),
 ("Quarters", "4", 4), ("Minutes in an NBA quarter", "12", 12), ("Fouls before an NBA player fouls out", "6", 6)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-29.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
