# Bank session 10 Oct 2026: 8 more Play Your Cards Right games -> bank/cards-33.json. A row of 5-7 cards each:
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

game("the numbers in archery", "Sport", "hard", ["archery"], [
 ("Scoring rings on the target", "10", 10), ("Olympic shooting distance, in metres", "70", 70), ("Arrows in each 'end' outdoors", "6", 6),
 ("Width of an Olympic target face, in centimetres", "122", 122), ("Archers in an Olympic team", "3", 3)])
game("the numbers in triathlon", "Sport", "medium", ["triathlon"], [
 ("Olympic swim, in kilometres", "1.5", 1.5), ("Olympic bike ride, in kilometres", "40", 40), ("Olympic run, in kilometres", "10", 10),
 ("Sports in a triathlon", "3", 3), ("Ironman bike ride, in miles", "112", 112)])
game("the numbers in Tetris", "Games and toys", "medium", ["Tetris", "video games"], [
 ("Different shapes", "7", 7), ("Width of the grid, in squares", "10", 10), ("Height of the grid, in squares", "20", 20),
 ("Squares in every piece", "4", 4), ("Year it was invented", "1984", 1984)])
game("the numbers in Pac-Man", "Games and toys", "hard", ["Pac-Man", "video games"], [
 ("Ghosts", "4", 4), ("Dots in a maze", "240", 240), ("Points for eating one dot", "10", 10),
 ("The level with the 'kill screen'", "256", 256), ("Year it came out", "1980", 1980)])
game("the numbers in a game of bingo", "Games and toys", "easy", ["bingo"], [
 ("Balls in UK bingo", "90", 90), ("Rows on a ticket", "3", 3), ("Numbers on a ticket", "15", 15),
 ("Columns on a ticket", "9", 9), ("Numbers in each row of a ticket", "5", 5)])
game("the numbers in Cluedo", "Games and toys", "medium", ["Cluedo", "board games"], [
 ("Suspects", "6", 6), ("Rooms", "9", 9), ("Weapons", "6", 6), ("Cards hidden in the envelope", "3", 3), ("Year it first went on sale", "1949", 1949)])
game("the numbers in Connect 4", "Games and toys", "easy", ["Connect 4", "games"], [
 ("Columns", "7", 7), ("Rows", "6", 6), ("Holes in the grid", "42", 42), ("Counters each player gets", "21", 21), ("Counters in a row to win", "4", 4)])
game("the numbers in Battleships", "Games and toys", "medium", ["Battleships", "games"], [
 ("Squares on each grid", "100", 100), ("Ships in each fleet", "5", 5), ("Length of the destroyer", "2", 2),
 ("Length of the aircraft carrier", "5", 5), ("Squares the whole fleet covers", "17", 17)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-33.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
