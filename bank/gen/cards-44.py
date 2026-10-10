# Bank session 10 Oct 2026: 8 more Play Your Cards Right games -> bank/cards-44.json. A row of 5-7 cards each:
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

game("the numbers of The Mousetrap", "Theatre", "hard", ["The Mousetrap", "Agatha Christie"], [
 ("Year it opened in the West End", "1952", 1952), ("Actors in the cast", "8", 8), ("Year it moved to St Martin's Theatre", "1974", 1974),
 ("Agatha Christie's age when it opened", "62", 62), ("Year it first went out as the radio play 'Three Blind Mice'", "1947", 1947)])
game("the numbers of Les Misérables", "Theatre", "hard", ["Les Misérables", "musicals"], [
 ("Jean Valjean's prisoner number", "24601", 24601), ("Year Victor Hugo's novel came out", "1862", 1862), ("Years Valjean spent in prison", "19", 19),
 ("Year the musical opened in London", "1985", 1985), ("Year of the film with Hugh Jackman", "2012", 2012)])
game("the numbers of The Phantom of the Opera", "Theatre", "hard", ["Phantom of the Opera", "musicals"], [
 ("Year it opened in the West End", "1986", 1986), ("The Phantom's private box number", "5", 5), ("Year Gaston Leroux's novel came out", "1910", 1910),
 ("Year it closed on Broadway after a record run", "2023", 2023), ("Michael Crawford's age when he first played the Phantom", "44", 44)])
game("the numbers of a London black cab driver's Knowledge", "London", "hard", ["black cabs", "London"], [
 ("Streets drivers must learn, roughly", "25,000", 25000), ("Miles around Charing Cross that the Knowledge covers", "6", 6), ("Routes in the 'Blue Book'", "320", 320),
 ("Years it usually takes to pass, roughly", "4", 4), ("A black cab's turning circle, in feet", "25", 25)])
game("the numbers of the Routemaster bus", "London", "hard", ["Routemaster", "buses"], [
 ("Year it first carried passengers", "1956", 1956), ("Seats", "64", 64), ("Routemasters built", "2,876", 2876),
 ("Crew on board: driver and conductor", "2", 2), ("Year the last regular route stopped using them", "2005", 2005)])
game("the numbers of the Crown Jewels", "Royals", "hard", ["Crown Jewels", "royals"], [
 ("Diamonds on the Imperial State Crown", "2,868", 2868), ("Carats of the Cullinan I, the Great Star of Africa", "530", 530), ("Carats of the Koh-i-Noor", "105.6", 105.6),
 ("Weight of St Edward's Crown, in kilograms", "2.23", 2.23), ("Year Colonel Blood tried to steal them", "1671", 1671)])
game("the numbers of Oasis", "Music", "medium", ["Oasis", "Britpop"], [
 ("Year they formed", "1991", 1991), ("UK number one singles", "8", 8), ("Studio albums", "7", 7),
 ("Fans at Knebworth over two nights, in thousands", "250", 250), ("Year of their reunion tour", "2025", 2025)])
game("the numbers of the Spice Girls", "Music", "medium", ["Spice Girls", "pop"], [
 ("Year they formed", "1994", 1994), ("Members", "5", 5), ("Weeks 'Wannabe' spent at number one in the UK", "7", 7),
 ("UK number one singles", "9", 9), ("Year of their film Spice World", "1997", 1997)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-44.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'games written')
