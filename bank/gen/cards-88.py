# Bank session 18 Oct 2026: 3 Play Your Cards Right games -> bank/cards-88.json (Mallard, the Spitfire, Stephenson's Rocket).
# Titles probed against every cards game in the live bank first (Flying Scotsman, Concorde, Routemaster, Cutty Sark and
# HMS Victory games already exist; the Red Arrows were free but short of five sure numbers).
# A row of 5-7 cards each: what's on the card, what it shows when it flips, and the number compared. Zig-zag, no equal neighbours.
import json, os
G = []
def game(text, cat, diff, tags, cards):
    ns = [n for _, _, n in cards]
    assert 5 <= len(cards) <= 7, text
    assert all(ns[i] != ns[i - 1] for i in range(1, len(ns))), (text, 'equal neighbours')
    assert len({l for l, _, _ in cards}) == len(cards), (text, 'repeated card')
    G.append({"type": "cards", "text": "Play Your Cards Right: " + text, "category": cat, "tags": ["Play Your Cards Right"] + tags, "difficulty": diff,
              "cards": [{"label": l, "value": v, "n": n} for l, v, n in cards]})

game("the numbers of Mallard", "History", "hard", ["Mallard", "steam", "railways", "LNER"], [
 ("Year it was built", "1938", 1938), ("Its world record steam speed, in mph", "126", 126), ("Its LNER number", "4468", 4468),
 ("Driving wheels", "6", 6), ("Year it was withdrawn from service", "1963", 1963)])
game("the numbers of the Spitfire", "History", "hard", ["Spitfire", "RAF", "Second World War", "aircraft"], [
 ("Year of its first flight", "1936", 1936), ("Machine guns on the first Spitfires", "8", 8), ("Year of the Battle of Britain", "1940", 1940),
 ("Cylinders in its Rolls-Royce Merlin engine", "12", 12), ("Year its designer R.J. Mitchell died", "1937", 1937)])
game("the numbers of Stephenson's Rocket", "History", "hard", ["Rocket", "Stephenson", "railways", "North East"], [
 ("Year it won the Rainhill Trials", "1829", 1829), ("Its top speed at the trials, in mph", "30", 30), ("Year George Stephenson was born, in Wylam", "1781", 1781),
 ("The prize for winning the trials, in pounds", "500", 500), ("Year the Liverpool and Manchester Railway opened", "1830", 1830)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-88.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
