# Bank session 10 Oct 2026: 8 more Play Your Cards Right games -> bank/cards-36.json. A row of 5-7 cards each:
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

game("the numbers of the Eiffel Tower", "Famous landmarks", "medium", ["Eiffel Tower", "Paris"], [
 ("Height in metres, with its aerials", "330", 330), ("Levels open to visitors", "3", 3), ("Year it opened", "1889", 1889),
 ("It gets repainted every how many years?", "7", 7), ("Tonnes of iron in it", "7,300", 7300)])
game("the numbers of Stonehenge", "History", "hard", ["Stonehenge", "prehistory"], [
 ("Its age in years, roughly", "5,000", 5000), ("Upright sarsens in the outer circle, originally", "30", 30), ("Great trilithons", "5", 5),
 ("Miles the bluestones came from Wales, roughly", "150", 150), ("Year it became a World Heritage Site", "1986", 1986)])
game("the numbers of Big Ben", "London", "medium", ["Big Ben", "Westminster"], [
 ("Clock faces", "4", 4), ("Steps up the tower", "334", 334), ("Height of the tower, in metres", "96", 96),
 ("Weight of the great bell, in tonnes", "13.7", 13.7), ("Year the bell first rang out", "1859", 1859)])
game("the numbers of the Colosseum", "History", "hard", ["Rome", "Colosseum"], [
 ("Year it opened (AD)", "80", 80), ("Spectators it held, roughly", "50,000", 50000), ("Storeys", "4", 4),
 ("Days of games to open it", "100", 100), ("Numbered arches round the outside", "80", 80)])
game("the numbers of the Panama Canal", "World geography", "medium", ["Panama Canal"], [
 ("Length in miles, roughly", "50", 50), ("Year it opened", "1914", 1914), ("Sets of locks", "3", 3),
 ("Oceans it joins", "2", 2), ("Metres the ships are lifted up to Gatun Lake", "26", 26)])
game("the numbers of the Channel Tunnel", "Britain", "medium", ["Channel Tunnel"], [
 ("Length in miles, roughly", "31", 31), ("Year it opened", "1994", 1994), ("Tunnels side by side", "3", 3),
 ("Minutes on Le Shuttle, roughly", "35", 35), ("Deepest point below sea level, in metres", "75", 75)])
game("the numbers of the London Eye", "London", "easy", ["London Eye"], [
 ("Height in metres", "135", 135), ("Capsules", "32", 32), ("Minutes for one turn", "30", 30), ("Year it opened", "2000", 2000), ("People each capsule can hold", "25", 25)])
game("the numbers of Buckingham Palace", "The royal family", "medium", ["Buckingham Palace", "royals"], [
 ("Rooms", "775", 775), ("State rooms", "19", 19), ("Royal and guest bedrooms", "52", 52), ("Bathrooms", "78", 78), ("Year Queen Victoria moved in", "1837", 1837)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-36.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
