# Bank session 10 Oct 2026: 8 more Play Your Cards Right games -> bank/cards-39.json. A row of 5-7 cards each:
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

game("the numbers of the Sydney Opera House", "Famous landmarks", "hard", ["Sydney Opera House", "Australia"], [
 ("Year it opened", "1973", 1973), ("Tiles on the roof shells", "1,056,006", 1056006), ("Years it took to build", "14", 14),
 ("Height in metres", "65", 65), ("Year it became a World Heritage Site", "2007", 2007)])
game("the numbers of Edinburgh Castle", "Scotland", "hard", ["Edinburgh Castle", "Edinburgh"], [
 ("Hour the One O'Clock Gun fires, on the 24-hour clock", "13", 13), ("Year of the first Military Tattoo on the esplanade", "1950", 1950), ("Height of Castle Rock above sea level, in metres", "130", 130),
 ("Year the great cannon Mons Meg was made", "1449", 1449), ("Weight of Mons Meg, in tonnes, roughly", "6", 6)])
game("the numbers of Blackpool Tower and the Illuminations", "Britain", "medium", ["Blackpool", "seaside"], [
 ("Year the Tower opened", "1894", 1894), ("Height of the Tower, in metres", "158", 158), ("Miles of Illuminations along the front, roughly", "6", 6),
 ("Year the first lights were switched on", "1879", 1879), ("Lights in the Illuminations, in millions, roughly", "1", 1)])
game("the numbers of Windsor Castle", "Royals", "hard", ["Windsor Castle", "royals"], [
 ("Rooms, roughly", "1,000", 1000), ("Year of the great fire", "1992", 1992), ("Knights of the Garter, not counting royals", "24", 24),
 ("Year William the Conqueror began it, roughly", "1070", 1070), ("Acres the castle covers, roughly", "13", 13)])
game("the numbers of the Hoover Dam", "Famous landmarks", "hard", ["Hoover Dam", "USA"], [
 ("Year it was finished", "1936", 1936), ("Height in metres", "221", 221), ("Official count of workers who died building it", "96", 96),
 ("Generators (turbines) in its power plant", "17", 17), ("Years it took to build, roughly", "5", 5)])
game("the numbers of Machu Picchu", "Famous landmarks", "hard", ["Machu Picchu", "Peru"], [
 ("Year the Incas built it, roughly", "1450", 1450), ("Year Hiram Bingham made it famous", "1911", 1911), ("Height above sea level, in metres", "2,430", 2430),
 ("Year it became a World Heritage Site", "1983", 1983), ("Year it was voted one of the New Seven Wonders", "2007", 2007)])
game("the numbers of Christ the Redeemer", "Famous landmarks", "hard", ["Christ the Redeemer", "Rio de Janeiro"], [
 ("Year it was finished", "1931", 1931), ("Height of the statue in metres, without its base", "30", 30), ("Arm span in metres", "28", 28),
 ("Height of Corcovado mountain, in metres, roughly", "700", 700), ("Weight in tonnes, roughly", "635", 635)])
game("the numbers of Concorde", "Transport", "medium", ["Concorde", "aircraft"], [
 ("Year of its first flight", "1969", 1969), ("Cruising speed in mph, roughly", "1,350", 1350), ("Aircraft built", "20", 20),
 ("Passengers on board", "100", 100), ("Year it last flew", "2003", 2003)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-39.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
