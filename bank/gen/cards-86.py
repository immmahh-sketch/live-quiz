# Bank session 18 Oct 2026: 4 Play Your Cards Right games -> bank/cards-86.json (a pack of cards, the Humber Bridge,
# Penshaw Monument, the Shipping Forecast). Titles probed against every cards game in the live bank first (piano, chess,
# Angel of the North, Hadrian's Wall, Titanic and Tyne Bridge games already exist).
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

game("the numbers in a pack of cards", "Games and toys", "easy", ["playing cards", "card games"], [
 ("Cards in a pack, without jokers", "52", 52), ("Suits", "4", 4), ("Red cards", "26", 26), ("Jokers in most packs", "2", 2),
 ("Picture cards", "12", 12), ("All the card values added up, ace = 1 to king = 13", "364", 364)])
game("the numbers of the Humber Bridge", "UK geography", "hard", ["Humber Bridge", "bridges", "Yorkshire", "Lincolnshire"], [
 ("Year it opened", "1981", 1981), ("Length of its main span, in metres", "1,410", 1410), ("Height of its towers, in metres", "155", 155),
 ("Year it lost the title of world's longest single-span suspension bridge", "1998", 1998), ("Years it held that title", "17", 17)])
game("the numbers of Penshaw Monument", "The North East of England", "hard", ["Penshaw Monument", "Sunderland", "landmarks", "North East"], [
 ("Year it was built", "1844", 1844), ("Its height, in feet", "70", 70), ("Number of columns", "18", 18),
 ("Year it was given to the National Trust", "1939", 1939), ("Year the Earl of Durham it honours died", "1840", 1840)])
game("the numbers of the Shipping Forecast", "UK geography", "medium", ["Shipping Forecast", "radio", "sea"], [
 ("Sea areas around the British Isles", "31", 31), ("Broadcasts a day on Radio 4", "4", 4), ("Year Finisterre was renamed FitzRoy", "2002", 2002),
 ("Sea areas with Utsire in the name", "2", 2), ("Year the BBC first broadcast it", "1924", 1924)])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(G, open(os.path.join(here, '..', 'cards-86.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(G), 'cards games written')
