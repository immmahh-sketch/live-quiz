# Bank session 18 Oct 2026: 4 Put in order questions -> bank/order-40.json (Gerry Anderson shows, Hanna-Barbera cartoons,
# David Croft sitcoms, Roy Clarke sitcoms). Each theme probed against every order question title and item list in the live bank.
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

# 1962, 1964, 1965, 1967, 1968, 1983
o("Television", ["Gerry Anderson", "Thunderbirds", "puppets"], "hard", "Put these Gerry Anderson shows in order of first broadcast, earliest first",
  ["Fireball XL5", "Stingray", "Thunderbirds", "Captain Scarlet and the Mysterons", "Joe 90", "Terrahawks"], "earliest first")
# 1958, 1960, 1961, 1962, 1968, 1969
o("Television", ["Hanna-Barbera", "cartoons"], "hard", "Put these Hanna-Barbera cartoons in order of first broadcast, earliest first",
  ["The Huckleberry Hound Show", "The Flintstones", "Top Cat", "The Jetsons", "Wacky Races", "Scooby-Doo, Where Are You!"], "earliest first")
# 1968, 1972, 1974, 1980, 1982, 1988
o("British sitcoms", ["David Croft", "sitcoms", "BBC"], "medium", "Put these David Croft sitcoms in order of first broadcast, earliest first",
  ["Dad's Army", "Are You Being Served?", "It Ain't Half Hot Mum", "Hi-de-Hi!", "'Allo 'Allo!", "You Rang, M'Lord?"], "earliest first")
# 1973, 1976, 1988, 1990, 2013
o("British sitcoms", ["Roy Clarke", "sitcoms", "BBC"], "medium", "Put these Roy Clarke sitcoms in order of first broadcast, earliest first",
  ["Last of the Summer Wine", "Open All Hours", "First of the Summer Wine", "Keeping Up Appearances", "Still Open All Hours"], "earliest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-40.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
