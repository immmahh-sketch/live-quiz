# Bank session 11 Oct 2026: 5 more Put in order questions -> bank/order-21.json (screen Hulks, Scrooges, Queens, Jack Ryans, Wonkas).
# Each theme was checked against every order question title in the live bank (the server also skips any whose items match one already there).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

A = lambda band, tags, diff, items: o("Music", [band, "albums"] + tags, diff, f"Put these {band} albums in order of release, earliest first", items, "earliest first")
F = lambda who, diff, items: o("Film", [who, "directors"], diff, f"Put these {who} films in order of release, earliest first", items, "earliest first")
o("Film", ["the Hulk", "Marvel", "actors"], "medium", "Put these actors in the order they first played the Hulk, earliest first", ["Lou Ferrigno", "Eric Bana", "Edward Norton", "Mark Ruffalo"], "earliest first")
o("Film", ["Scrooge", "A Christmas Carol", "actors"], "medium", "Put these screen Scrooges in order, earliest first", ["Alastair Sim", "Albert Finney", "Michael Caine", "Patrick Stewart", "Jim Carrey"], "earliest first")
o("Film", ["Elizabeth II", "actors", "The Crown"], "medium", "Put these actresses in the order they first played Elizabeth II on screen, earliest first", ["Helen Mirren", "Claire Foy", "Olivia Colman", "Imelda Staunton"], "earliest first")
o("Film", ["Jack Ryan", "Tom Clancy", "actors"], "hard", "Put these screen Jack Ryans in order, earliest first", ["Alec Baldwin", "Harrison Ford", "Ben Affleck", "Chris Pine", "John Krasinski"], "earliest first")
o("Film", ["Willy Wonka", "Roald Dahl", "actors"], "easy", "Put these screen Willy Wonkas in order, earliest first", ["Gene Wilder", "Johnny Depp", "Timothée Chalamet"], "earliest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-21.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
