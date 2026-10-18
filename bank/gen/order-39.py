# Bank session 18 Oct 2026: 4 Put in order questions -> bank/order-39.json (coins by size, planets by length of day,
# banknote faces by value, coffees by milk). Each theme probed against every order question title and item list in the
# live bank first (coins by value, champagne bottles, Tube lines, Wallace & Gromit and peaks were already there).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

# diameters: 5p 18.0 mm, 1p 20.3, 20p 21.4, £1 23.43, 10p 24.5, 2p 25.9
o("Money", ["coins", "money", "UK"], "hard", "Put these UK coins in order of size, smallest across first",
  ["5p", "1p", "20p", "£1", "10p", "2p"], "smallest first")
# one turn on its axis: Jupiter ~9h 56m, Saturn ~10h 33m, Earth ~23h 56m, Mars ~24h 37m, Mercury ~59 days, Venus ~243 days
o("Space and astronomy", ["planets", "solar system", "days"], "hard", "Put these planets in order of how long one day lasts (one turn on its axis), shortest first",
  ["Jupiter", "Saturn", "Earth", "Mars", "Mercury", "Venus"], "shortest first")
o("Money", ["banknotes", "Bank of England", "famous faces"], "medium", "Put these faces on Bank of England notes in order of the note's value, lowest first",
  ["Winston Churchill", "Jane Austen", "JMW Turner", "Alan Turing"], "lowest value first")
o("Food and drink", ["coffee", "cafés", "drinks"], "medium", "Put these coffees in order of how much milk is in them, least first",
  ["Espresso", "Macchiato", "Cortado", "Flat white", "Latte"], "least milk first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-39.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
