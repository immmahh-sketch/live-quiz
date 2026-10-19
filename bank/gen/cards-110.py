# Bank session 19 Oct 2026: 3 Play Your Cards Right games -> bank/cards-110.json (the beaver, the hazel dormouse, the seahorse).
# Probed against every cards game in the live bank first (no beaver, dormouse or seahorse games). Numbers are the commonly quoted ones.
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

game("the numbers of a beaver", "Nature", "hard", ["beavers", "British wildlife", "rewilding"], [
 ("Years beavers were missing from Britain, roughly", "400", 400), ("Kilograms an adult weighs", "20", 20), ("Kits in a typical litter", "3", 3),
 ("Minutes it can stay under water", "15", 15), ("Year of the official trial release at Knapdale in Scotland", "2009", 2009)])
game("the numbers of a hazel dormouse", "Nature", "hard", ["dormice", "British wildlife", "hibernation"], [
 ("Months it can spend hibernating", "7", 7), ("Grams it weighs", "20", 20), ("Years it can live", "5", 5),
 ("Babies in a typical litter", "4", 4), ("Percentage its numbers have fallen since 2000, roughly", "70", 70)])
game("the numbers of a seahorse", "Nature", "medium", ["seahorses", "sea life", "fish"], [
 ("Kinds of seahorse found in UK waters", "2", 2), ("Kinds of seahorse worldwide, roughly", "46", 46), ("Babies a male can give birth to at once", "1,000", 1000),
 ("Centimetres long, a UK seahorse", "15", 15), ("Years it can live", "4", 4)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-110.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
