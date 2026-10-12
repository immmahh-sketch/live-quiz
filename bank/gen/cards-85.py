# Bank session 12 Oct 2026: 2 more Play Your Cards Right games -> bank/cards-85.json (The Jungle Book, Watership Down). A row of 5-7 cards each:
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

game("the numbers of The Jungle Book", "Books", "medium", ["The Jungle Book", "Kipling", "Disney"], [
 ("Year Kipling's book came out", "1894", 1894), ("Kipling's age when it was published", "28", 28), ("Year Disney's cartoon came out", "1967", 1967),
 ("Oscar nominations for the Disney cartoon", "1", 1), ("Year of Disney's live-action remake", "2016", 2016)])
game("the numbers of Watership Down", "Books", "medium", ["Watership Down", "Richard Adams", "rabbits"], [
 ("Year the book came out", "1972", 1972), ("Weeks 'Bright Eyes' spent at number one", "6", 6), ("Year the cartoon film came out", "1978", 1978),
 ("Rabbits who set out from Sandleford with Hazel and Fiver, counting them", "11", 11), ("Year Richard Adams was born", "1920", 1920)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-85.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
