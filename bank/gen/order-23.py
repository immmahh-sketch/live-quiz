# Bank session 11 Oct 2026: 5 more Put in order questions -> bank/order-20.json (screen Jokers, Masters, Holmeses, Robin Hoods, Bond henchmen).
# Each theme was checked against every order question title in the live bank (the server also skips any whose items match one already there).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

A = lambda band, tags, diff, items: o("Music", [band, "albums"] + tags, diff, f"Put these {band} albums in order of release, earliest first", items, "earliest first")
F = lambda who, diff, items: o("Film", [who, "directors"], diff, f"Put these {who} films in order of release, earliest first", items, "earliest first")
o("Film", ["the Joker", "Batman", "actors"], "medium", "Put these actors in the order they first played the Joker, earliest first", ["Cesar Romero", "Jack Nicholson", "Heath Ledger", "Jared Leto", "Joaquin Phoenix"], "earliest first")
o("TV", ["Doctor Who", "the Master", "actors"], "hard", "Put these actors in the order they first played the Master in Doctor Who, earliest first", ["Roger Delgado", "Anthony Ainley", "Eric Roberts", "John Simm", "Michelle Gomez", "Sacha Dhawan"], "earliest first")
o("TV", ["Sherlock Holmes", "actors"], "medium", "Put these screen Sherlock Holmeses in order, earliest first", ["Basil Rathbone", "Jeremy Brett", "Robert Downey Jr.", "Benedict Cumberbatch"], "earliest first")
o("Film", ["Robin Hood", "actors"], "medium", "Put these screen Robin Hoods in order, earliest first", ["Errol Flynn", "Michael Praed", "Kevin Costner", "Russell Crowe", "Taron Egerton"], "earliest first")
o("Film", ["James Bond", "henchmen"], "medium", "Put these Bond henchmen in the order of their film, earliest first", ["Oddjob", "Nick Nack", "Jaws", "May Day", "Mr Hinx"], "earliest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-20.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
