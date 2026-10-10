# Bank session 10 Oct 2026: 11 more Play Your Cards Right games -> bank/cards-31.json. A row of 5-7 cards each:
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

game("the numbers in James Bond", "Film", "medium", ["James Bond", "numbers"], [
 ("Bond's agent number, 00___", "7", 7), ("Official Eon Bond films, up to No Time to Die", "25", 25), ("Actors to play Bond in the Eon films", "6", 6),
 ("Year of the first film, Dr. No", "1962", 1962), ("Bond's Aston Martin, the DB___", "5", 5)])
game("the numbers of the Titanic", "History", "medium", ["Titanic", "ships"], [
 ("The year she sank", "1912", 1912), ("Funnels", "4", 4), ("Lifeboats", "20", 20),
 ("Funnels that were just for show", "1", 1), ("Hours from hitting the iceberg to sinking", "2 hours 40 minutes", 2.67)])
game("the numbers in Game of Thrones", "Film and TV", "medium", ["Game of Thrones", "numbers"], [
 ("Seasons", "8", 8), ("Daenerys's dragons", "3", 3), ("Episodes in all", "73", 73), ("The ___ Kingdoms", "7", 7), ("Children of Ned and Catelyn Stark", "5", 5)])
game("the numbers in Breaking Bad", "Film and TV", "medium", ["Breaking Bad", "numbers"], [
 ("Seasons", "5", 5), ("Episodes", "62", 62), ("Walter White's age in the first episode", "50", 50),
 ("The purity of Walt's blue meth, in per cent", "99.1", 99.1), ("Seasons of Better Call Saul", "6", 6)])
game("the numbers in ice hockey", "Sport", "medium", ["ice hockey"], [
 ("Players on the ice per team", "6", 6), ("Periods", "3", 3), ("Minutes in each period", "20", 20),
 ("Minutes for a minor penalty", "2", 2), ("Teams in the NHL in 2025", "32", 32)])
game("the numbers in netball", "Sport", "medium", ["netball"], [
 ("Players per team on court", "7", 7), ("Quarters", "4", 4), ("Minutes in each quarter", "15", 15),
 ("Seconds you can hold the ball", "3", 3), ("Height of the post, in feet", "10", 10)])
game("the numbers on a clock", "General knowledge", "easy", ["time", "clocks"], [
 ("Numbers on the face", "12", 12), ("Hands on most clocks", "3", 3), ("Minute marks round the dial", "60", 60),
 ("Clock faces on Big Ben's tower", "4", 4), ("Times the hour hand goes round in a day", "2", 2)])
game("the numbers in Scrabble", "Games and toys", "medium", ["Scrabble", "board games"], [
 ("Tiles in the bag", "100", 100), ("Blank tiles", "2", 2), ("Tiles on your rack", "7", 7),
 ("Bonus for using all your tiles at once", "50", 50), ("Squares along each side of the board", "15", 15)])
game("the numbers in badminton", "Sport", "medium", ["badminton"], [
 ("Points to win a game", "21", 21), ("Games to win a match", "2", 2), ("Most points a game can go to", "30", 30),
 ("Feathers on a shuttlecock", "16", 16), ("Height of the net, in feet", "5", 5)])
game("the numbers in table tennis", "Sport", "hard", ["table tennis"], [
 ("Points to win a game", "11", 11), ("Width of the ball, in millimetres", "40", 40), ("Serves each player takes in a row", "2", 2),
 ("Height of the net, in centimetres", "15.25", 15.25), ("Length of the table, in metres", "2.74", 2.74)])
game("the numbers in Eurovision", "Music", "medium", ["Eurovision"], [
 ("Top marks from a jury ('douze points')", "12", 12), ("Longest a song can last, in minutes", "3", 3), ("Most performers allowed on stage", "6", 6),
 ("Countries in the 'Big Five'", "5", 5), ("Points a jury gives its 10th favourite", "1", 1)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-31.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
