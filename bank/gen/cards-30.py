# Bank session 10 Oct 2026: 12 more Play Your Cards Right games -> bank/cards-30.json. A row of 5-7 cards each:
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

game("the numbers of Christmas", "Christmas", "easy", ["Christmas", "numbers"], [
 ("Christmas Day's date in December", "25", 25), ("Wise men", "3", 3), ("Doors on a usual advent calendar", "24", 24),
 ("Santa's reindeer, counting Rudolph", "9", 9), ("Days of Christmas", "12", 12), ("Ghosts who visit Scrooge, counting Marley", "4", 4)])
game("the numbers in The Beatles", "Music", "medium", ["The Beatles", "numbers"], [
 ("'When I'm ___'", "64", 64), ("Beatles", "4", 4), ("UK number one singles", "17", 17),
 ("'___ Days a Week'", "8", 8), ("UK studio albums", "12", 12), ("'Revolution ___'", "9", 9)])
game("the numbers in Greek myth", "Myths and legends", "medium", ["Greek myth", "numbers"], [
 ("Labours of Heracles", "12", 12), ("Heads on Cerberus", "3", 3), ("Muses", "9", 9),
 ("Olympian gods", "12", 12), ("Years of the Trojan War", "10", 10), ("Fates", "3", 3)])
game("the numbers on a piano", "Music", "medium", ["piano", "instruments"], [
 ("Keys", "88", 88), ("Pedals on most pianos", "3", 3), ("White keys", "52", 52), ("Octaves (just over)", "7", 7), ("Black keys", "36", 36)])
game("the numbers in rugby league", "Rugby", "medium", ["rugby league"], [
 ("Players a side", "13", 13), ("Points for a drop goal", "1", 1), ("Tackles in a set", "6", 6),
 ("Points for a conversion", "2", 2), ("Points for a try", "4", 4), ("Minutes in the sin bin", "10", 10)])
game("the numbers in horse racing", "Sport", "hard", ["horse racing"], [
 ("Fences jumped in the Grand National", "30", 30), ("Days of the Cheltenham Festival", "4", 4), ("Most runners allowed in the Grand National", "34", 34),
 ("Races in the English Triple Crown", "3", 3), ("Furlongs in a mile", "8", 8), ("Roughly how many furlongs the Derby is", "12", 12)])
game("the numbers in the calendar", "General knowledge", "easy", ["calendar", "time"], [
 ("Months with 31 days", "7", 7), ("Weeks in a year", "52", 52), ("Days in February in a leap year", "29", 29),
 ("Hours in a week", "168", 168), ("Bank holidays in England and Wales in a usual year", "8", 8), ("Days in a normal year", "365", 365)])
game("the numbers in The Hunger Games", "Books", "medium", ["The Hunger Games", "numbers"], [
 ("Katniss's district", "12", 12), ("Tributes in each Games", "24", 24), ("Districts in all, counting the lost one", "13", 13),
 ("The Games Katniss first wins (the ___th)", "74", 74), ("Tributes from each district", "2", 2), ("The Quarter Quell (the ___th Games)", "75", 75)])
game("the numbers in Doctor Who", "Doctor Who", "medium", ["Doctor Who", "numbers"], [
 ("The Doctor's hearts", "2", 2), ("The TARDIS is a Type ___", "40", 40), ("Regenerations allowed under the old rule", "12", 12),
 ("Numbered Doctors on TV, up to Ncuti Gatwa", "15", 15), ("Series of the revival before the 2024 relaunch", "13", 13)])
game("the numbers in Texas hold'em poker", "Games and toys", "medium", ["poker", "cards"], [
 ("Hole cards each player gets", "2", 2), ("Ranks of poker hand", "10", 10), ("Cards in the flop", "3", 3), ("Community cards in all", "5", 5), ("Cards in the turn", "1", 1)])
game("the numbers in the Tour de France", "Cycling", "medium", ["Tour de France", "cycling"], [
 ("Stages", "21", 21), ("Rest days", "2", 2), ("Riders in each team", "8", 8), ("Grand Tours in cycling", "3", 3), ("Main jerseys to win", "4", 4)])
game("the numbers in swimming", "Sport", "medium", ["swimming"], [
 ("Length of an Olympic pool, in metres", "50", 50), ("Swimmers in a relay team", "4", 4), ("Lanes in an Olympic pool", "10", 10),
 ("Length of a short-course pool, in metres", "25", 25), ("The longest Olympic pool race, in metres", "1,500", 1500)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-30.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
