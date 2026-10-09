# Bank session 9 Oct 2026: more Play Your Cards Right games -> bank/cards-2.json. A row of 6 cards each: what's on the
# card, what it shows when it flips, and the number compared. The numbers zig-zag and no two neighbours are equal.
import json, os
G = []
def game(text, cat, diff, tags, cards):
    ns = [n for _, _, n in cards]
    assert 5 <= len(cards) <= 7, text
    assert all(ns[i] != ns[i - 1] for i in range(1, len(ns))), (text, 'equal neighbours')
    G.append({"type": "cards", "text": "Play Your Cards Right: " + text, "category": cat, "tags": ["Play Your Cards Right"] + tags, "difficulty": diff,
              "cards": [{"label": l, "value": v, "n": n} for l, v, n in cards]})

game("how many years did each monarch reign?", "British history", "medium", ["monarchs"], [
 ("Henry VIII", "37 years", 37), ("Elizabeth II", "70 years", 70), ("Edward VII", "9 years", 9),
 ("Queen Victoria", "63 years", 63), ("George VI", "15 years", 15), ("Elizabeth I", "44 years", 44)])
game("the year each club was founded", "Football", "hard", ["clubs", "years"], [
 ("Sunderland", "1879", 1879), ("Chelsea", "1905", 1905), ("Middlesbrough", "1876", 1876),
 ("Newcastle United", "1892", 1892), ("Manchester United (as Newton Heath)", "1878", 1878), ("Arsenal", "1886", 1886)])
game("what each letter scores in Scrabble", "Games and toys", "medium", ["Scrabble", "words"], [
 ("E", "1", 1), ("Q", "10", 10), ("D", "2", 2), ("J", "8", 8), ("B", "3", 3), ("K", "5", 5)])
game("the year each Doctor first appeared", "Doctor Who", "medium", ["Doctor Who", "years"], [
 ("William Hartnell", "1963", 1963), ("Jodie Whittaker", "2018", 2018), ("Tom Baker", "1974", 1974),
 ("Matt Smith", "2010", 2010), ("Peter Davison", "1982", 1982), ("Christopher Eccleston", "2005", 2005)])
game("how many members in the best-known line-up?", "Boy bands and girl groups", "easy", ["bands"], [
 ("The Beatles", "4", 4), ("S Club 7", "7", 7), ("ABBA", "4", 4), ("Spice Girls", "5", 5), ("Little Mix", "4", 4), ("Girls Aloud", "5", 5)])
game("the year each Disney film came out", "Disney films", "medium", ["Disney", "years"], [
 ("Snow White and the Seven Dwarfs", "1937", 1937), ("Frozen", "2013", 2013), ("Cinderella", "1950", 1950),
 ("The Lion King", "1994", 1994), ("Pinocchio", "1940", 1940), ("Moana", "2016", 2016)])
game("how many series were made?", "Film and TV", "medium", ["TV"], [
 ("Fawlty Towers", "2", 2), ("Friends", "10", 10), ("Gavin & Stacey", "3", 3),
 ("Game of Thrones", "8", 8), ("Breaking Bad", "5", 5), ("Only Fools and Horses", "7", 7)])
game("roughly how many fans does each ground hold, in thousands?", "Football", "medium", ["stadiums"], [
 ("Riverside Stadium", "about 34,000", 34), ("Wembley", "90,000", 90), ("Stadium of Light", "about 49,000", 49),
 ("Old Trafford", "about 74,000", 74), ("St James' Park", "about 52,000", 52), ("Anfield", "about 61,000", 61)])
game("how many strings?", "Music", "easy", ["instruments"], [
 ("Violin", "4", 4), ("Guitar", "6", 6), ("Ukulele", "4", 4), ("Concert harp", "47", 47), ("Banjo", "5", 5), ("Twelve-string guitar", "12", 12)])
game("the number in the title", "Film", "easy", ["films", "numbers"], [
 ("Apollo …", "13", 13), ("… Dalmatians", "101", 101), ("Se…en", "7", 7), ("The … Steps", "39", 39), ("Ocean's …", "11", 11), ("… Days Later", "28", 28)])
game("how many Oscars did each film win?", "The Oscars and award winners", "hard", ["Oscars", "films"], [
 ("Rocky", "3", 3), ("Titanic", "11", 11), ("Gladiator", "5", 5), ("Slumdog Millionaire", "8", 8), ("Forrest Gump", "6", 6), ("Oppenheimer", "7", 7)])
game("the year each band formed", "Music", "medium", ["bands", "years"], [
 ("The Beatles", "1960", 1960), ("Oasis", "1991", 1991), ("The Rolling Stones", "1962", 1962),
 ("Arctic Monkeys", "2002", 2002), ("Queen", "1970", 1970), ("Take That", "1990", 1990)])
game("hours ahead of the UK in winter (minus means behind)", "World geography", "hard", ["time zones"], [
 ("Los Angeles", "−8", -8), ("Tokyo", "+9", 9), ("New York", "−5", -5), ("Sydney", "+11", 11), ("Paris", "+1", 1), ("Dubai", "+4", 4)])
game("roughly how much does each ball weigh, in grams?", "Sport", "hard", ["balls", "weights"], [
 ("Golf ball", "about 46 g", 46), ("Football", "about 430 g", 430), ("Table tennis ball", "about 3 g", 3),
 ("Basketball", "about 620 g", 620), ("Tennis ball", "about 58 g", 58), ("Cricket ball", "about 160 g", 160)])
game("how far is each race, in metres?", "Sport", "medium", ["athletics"], [
 ("The 100 metres", "100 m", 100), ("The 1,500 metres", "1,500 m", 1500), ("The 400 metres", "400 m", 400),
 ("The marathon", "42,195 m", 42195), ("The 800 metres", "800 m", 800), ("The 10,000 metres", "10,000 m", 10000)])
game("how many in a standard pack of cards?", "Games and toys", "easy", ["playing cards"], [
 ("Jokers", "2", 2), ("Cards, not counting jokers", "52", 52), ("Suits", "4", 4), ("Red cards", "26", 26), ("Kings", "4", 4), ("Picture cards", "12", 12)])
game("how many sleeps until Christmas Day from each date?", "Christmas", "easy", ["Christmas", "dates"], [
 ("1 December", "24", 24), ("25 November", "30", 30), ("18 December", "7", 7), ("1 November", "54", 54), ("20 December", "5", 5), ("30 November", "25", 25)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-2.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
