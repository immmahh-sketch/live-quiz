# Bank session 19 Oct 2026: 3 Play Your Cards Right games -> bank/cards-101.json (the pet dog, the pet cat, the goldfish).
# Probed against every cards game in the live bank first (no dog, cat or goldfish games). Numbers are the commonly quoted ones.
# A row of 5-7 cards each: what's on the card, what it shows when it flips, and the number compared. No equal neighbours.
import json, os
G = []
def game(text, cat, diff, tags, cards):
    ns = [n for _, _, n in cards]
    assert 5 <= len(cards) <= 7, text
    assert all(ns[i] != ns[i - 1] for i in range(1, len(ns))), (text, 'equal neighbours')
    assert len({l for l, _, _ in cards}) == len(cards), (text, 'repeated card')
    G.append({"type": "cards", "text": "Play Your Cards Right: " + text, "category": cat, "tags": ["Play Your Cards Right"] + tags, "difficulty": diff,
              "cards": [{"label": l, "value": v, "n": n} for l, v, n in cards]})

game("the numbers of a pet dog", "Nature", "easy", ["dogs", "pets", "animals"], [
 ("Teeth in an adult dog's mouth", "42", 42), ("Millions of pet dogs in the UK", "13", 13), ("Days a dog is pregnant", "63", 63),
 ("Puppies in a typical litter", "6", 6), ("Years a dog usually lives", "13", 13)])
game("the numbers of a pet cat", "Nature", "easy", ["cats", "pets", "animals"], [
 ("Toes in total on its four paws", "18", 18), ("Whiskers on its muzzle", "24", 24), ("Hours a day it sleeps", "15", 15),
 ("Kittens in a typical litter", "4", 4), ("Days a cat is pregnant", "65", 65)])
game("the numbers of a goldfish", "Nature", "medium", ["goldfish", "pets", "fish"], [
 ("Seconds its memory lasts, according to the myth", "3", 3), ("Years a well-kept goldfish can live", "20", 20), ("Age of Tish, the oldest goldfish on record", "43", 43),
 ("Centimetres long a big one can grow", "30", 30), ("Eggs a female can lay at once", "1,000", 1000)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-101.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
