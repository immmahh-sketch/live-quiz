# Bank session 10 Oct 2026: 8 more Play Your Cards Right games -> bank/cards-32.json. A row of 5-7 cards each:
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

game("the numbers in rugby union (not the points)", "Rugby", "medium", ["rugby union"], [
 ("Players a side", "15", 15), ("Replacements on the bench", "8", 8), ("Minutes in a match", "80", 80),
 ("Teams in the Six Nations", "6", 6), ("Teams at the 2023 Rugby World Cup", "20", 20), ("Minutes in the sin bin", "10", 10)])
game("the numbers in hockey (on grass)", "Sport", "medium", ["hockey"], [
 ("Players a side", "11", 11), ("Quarters", "4", 4), ("Minutes in each quarter", "15", 15),
 ("Radius of the shooting circle, in yards", "16", 16), ("Minutes off for a green card", "2", 2)])
game("the numbers in volleyball", "Sport", "medium", ["volleyball"], [
 ("Players on court per team", "6", 6), ("Sets needed to win a match", "3", 3), ("Points to win a normal set", "25", 25),
 ("Points to win the deciding set", "15", 15), ("Height of the men's net, in metres", "2.43", 2.43)])
game("the numbers in gymnastics", "Sport", "medium", ["gymnastics"], [
 ("Pieces of apparatus for men", "6", 6), ("Pieces of apparatus for women", "4", 4), ("The old 'perfect' score", "10", 10),
 ("Gymnasts in each team at Paris 2024", "5", 5), ("Height of the balance beam, in centimetres", "125", 125)])
game("the numbers in law and justice", "Politics", "medium", ["law", "justice"], [
 ("People on a jury in England", "12", 12), ("Justices on the US Supreme Court", "9", 9), ("Jurors who must agree for a majority verdict", "10", 10),
 ("The year of Magna Carta", "1215", 1215), ("Justices on the UK Supreme Court", "12", 12)])
game("the numbers in world religions", "Religion", "medium", ["religion", "faith"], [
 ("Pillars of Islam", "5", 5), ("Noble Truths in Buddhism", "4", 4), ("Nights of Hanukkah", "8", 8),
 ("Human Sikh Gurus", "10", 10), ("Stations of the Cross", "14", 14)])
game("the numbers in The Great British Bake Off", "Film and TV", "easy", ["Bake Off", "TV"], [
 ("Bakers who usually start a series", "12", 12), ("Challenges each week", "3", 3), ("Weeks in a series", "10", 10),
 ("Judges", "2", 2), ("Year of the first series", "2010", 2010)])
game("the numbers in Strictly Come Dancing", "Film and TV", "easy", ["Strictly", "TV"], [
 ("Judges on the panel", "4", 4), ("Highest possible score for one dance", "40", 40), ("Top mark on a judge's paddle", "10", 10),
 ("Year it started", "2004", 2004), ("Glitterball trophies handed out each series", "1", 1)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-32.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
