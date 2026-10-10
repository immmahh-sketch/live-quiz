# Bank session 10 Oct 2026: 8 more Play Your Cards Right games -> bank/cards-42.json. A row of 5-7 cards each:
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

game("the numbers of the Tyne Bridge", "North East", "hard", ["Tyne Bridge", "Newcastle"], [
 ("Year it opened", "1928", 1928), ("Length of the arch span, in metres", "161", 161), ("Height above the river, in metres, roughly", "26", 26),
 ("Year its builders' Sydney Harbour Bridge opened", "1932", 1932), ("What it cost, in millions of pounds, roughly", "1.2", 1.2)])
game("the numbers of Durham Cathedral", "North East", "hard", ["Durham Cathedral", "Durham"], [
 ("Year building began", "1093", 1093), ("Height of the central tower, in metres", "66", 66), ("Steps up the tower", "325", 325),
 ("Year St Cuthbert's body arrived in Durham", "995", 995), ("Year it became a World Heritage Site", "1986", 1986)])
game("the numbers of Loch Ness", "Scotland", "hard", ["Loch Ness", "Nessie"], [
 ("Length in miles, roughly", "23", 23), ("Deepest point, in metres, roughly", "230", 230), ("Year of the famous 'Surgeon's Photograph'", "1934", 1934),
 ("Year St Columba is said to have met the monster", "565", 565), ("Height of its surface above sea level, in metres", "16", 16)])
game("the numbers of York Minster", "Britain", "hard", ["York Minster", "York"], [
 ("Years it took to build, roughly", "250", 250), ("Height of the central tower, in metres", "72", 72), ("Steps up the central tower", "275", 275),
 ("Year of the great fire started by lightning", "1984", 1984), ("Panels in the Great East Window", "311", 311)])
game("the numbers of Snowdon (Yr Wyddfa)", "Wales", "hard", ["Snowdon", "mountains"], [
 ("Height in metres", "1,085", 1085), ("Year the mountain railway opened", "1896", 1896), ("Length of the railway, in miles, roughly", "5", 5),
 ("Year the summit café Hafod Eryri opened", "2009", 2009), ("Main paths to the summit", "6", 6)])
game("the numbers of Ben Nevis", "Scotland", "hard", ["Ben Nevis", "mountains"], [
 ("Height in metres", "1,345", 1345), ("Year of the first recorded climb", "1771", 1771), ("Year the summit weather observatory opened", "1883", 1883),
 ("Years the observatory stayed open", "21", 21), ("Munros in Scotland, of which it's the highest", "282", 282)])
game("the numbers of Lindisfarne", "North East", "hard", ["Lindisfarne", "Holy Island"], [
 ("Year St Aidan founded the monastery", "635", 635), ("Year of the Viking raid", "793", 793), ("Year the Lindisfarne Gospels were made, roughly", "715", 715),
 ("Year the castle was built, roughly", "1550", 1550), ("Hours the causeway is cut off each tide, roughly", "5", 5)])
game("the numbers of Kielder Water and Forest", "North East", "hard", ["Kielder", "Northumberland"], [
 ("Year the reservoir opened", "1982", 1982), ("Billion litres of water it holds, roughly", "200", 200), ("Miles of shoreline, roughly", "27", 27),
 ("Trees in Kielder Forest, in millions, roughly", "150", 150), ("Year it became a Dark Sky Park", "2013", 2013)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-42.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
