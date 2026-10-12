# Bank session 12 Oct 2026: 2 more Play Your Cards Right games -> bank/cards-83.json (Beamish, Dragons' Den). A row of 5-7 cards each:
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

game("the numbers of Beamish Museum", "The North East of England", "medium", ["Beamish", "museums", "North East"], [
 ("Year the museum was founded", "1970", 1970), ("Acres it covers", "350", 350), ("Year its 1900s town is set in", "1913", 1913),
 ("Main eras it recreates", "4", 4), ("Decade of its oldest area, Pockerley", "1820s", 1820)])
game("the numbers of Dragons' Den", "TV", "medium", ["Dragons' Den", "business", "TV"], [
 ("Year it began on the BBC", "2005", 2005), ("Dragons in the Den", "5", 5), ("Year Steven Bartlett joined", "2022", 2022),
 ("Original Dragons still on the show", "1", 1), ("Year County Durham's Sara Davies joined", "2019", 2019)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-83.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
