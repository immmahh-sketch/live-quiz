# Bank session 10 Oct 2026: 8 more Play Your Cards Right games -> bank/cards-41.json. A row of 5-7 cards each:
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

game("the numbers of Apollo 11", "Space", "medium", ["Apollo 11", "Moon"], [
 ("Year it landed on the Moon", "1969", 1969), ("Astronauts on board", "3", 3), ("Distance to the Moon, in km, on average", "384,400", 384400),
 ("Days the whole mission lasted, roughly", "8", 8), ("Kilograms of Moon rock brought back, roughly", "22", 22)])
game("the numbers of the Cutty Sark", "History", "hard", ["Cutty Sark", "ships"], [
 ("Year she was launched", "1869", 1869), ("Masts", "3", 3), ("Year she went on show at Greenwich", "1957", 1957),
 ("Top speed in knots, roughly", "17", 17), ("Year of the fire that badly damaged her", "2007", 2007)])
game("the numbers of the Mary Rose", "History", "hard", ["Mary Rose", "Tudors"], [
 ("Year she was launched", "1511", 1511), ("Year she sank", "1545", 1545), ("Year she was raised", "1982", 1982),
 ("Crew who survived the sinking, roughly", "35", 35), ("Years she lay on the seabed", "437", 437)])
game("the numbers of the Hubble Space Telescope", "Space", "hard", ["Hubble", "space"], [
 ("Year it was launched", "1990", 1990), ("Shuttle missions sent to repair or upgrade it", "5", 5), ("Height of its orbit, in km, roughly", "540", 540),
 ("Length in metres, roughly", "13", 13), ("Width of its main mirror, in metres", "2.4", 2.4)])
game("the numbers of the Space Shuttle", "Space", "medium", ["Space Shuttle", "NASA"], [
 ("Year of its first launch", "1981", 1981), ("Shuttles that flew in space", "5", 5), ("Missions flown in all", "135", 135),
 ("Astronauts on a usual crew", "7", 7), ("Year of its last flight", "2011", 2011)])
game("the numbers of Wembley Stadium", "London", "medium", ["Wembley", "football"], [
 ("Year the new stadium opened", "2007", 2007), ("Seats", "90,000", 90000), ("Height of the arch, in metres", "133", 133),
 ("Steps up to the Royal Box", "107", 107), ("Toilets, more than any other building in the world when it opened", "2,618", 2618)])
game("the numbers of Alcatraz", "History", "medium", ["Alcatraz", "San Francisco"], [
 ("Year it opened as a federal prison", "1934", 1934), ("Cells", "336", 336), ("Year Frank Morris and the Anglin brothers escaped", "1962", 1962),
 ("Years it was a federal prison", "29", 29), ("Al Capone's prisoner number, AZ-...", "85", 85)])
game("the numbers of the Grand Canyon", "Famous landmarks", "hard", ["Grand Canyon", "USA"], [
 ("Length in miles", "277", 277), ("Deepest point, in metres, roughly", "1,800", 1800), ("Year it became a national park", "1919", 1919),
 ("Widest point, in miles, roughly", "18", 18), ("Millions of years the Colorado River has been carving it, roughly", "6", 6)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-41.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
