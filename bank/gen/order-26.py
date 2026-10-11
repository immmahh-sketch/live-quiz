# Bank session 11 Oct 2026: 3 more Put in order questions -> bank/order-23.json (Bake Off and MasterChef winners, Sports Personality winners).
# Each theme was checked against every order question title in the live bank (the server also skips any whose items match one already there).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

A = lambda band, tags, diff, items: o("Music", [band, "albums"] + tags, diff, f"Put these {band} albums in order of release, earliest first", items, "earliest first")
F = lambda who, diff, items: o("Film", [who, "directors"], diff, f"Put these {who} films in order of release, earliest first", items, "earliest first")
o("TV", ["Bake Off", "winners"], "medium", "Put these Great British Bake Off winners in order, earliest first", ["Edd Kimber", "John Whaite", "Nadiya Hussain", "Candice Brown", "Rahul Mandal", "Peter Sawkins", "Matty Edgell"], "earliest first")
o("TV", ["MasterChef", "winners"], "hard", "Put these MasterChef winners in order, earliest first", ["Thomasina Miers", "Mat Follas", "Dhruv Baker", "Tim Anderson", "Shelina Permalloo", "Ping Coombes", "Simon Wood"], "earliest first")
o("Sport", ["Sports Personality of the Year", "BBC"], "medium", "Put these BBC Sports Personality of the Year winners in order, earliest first", ["David Beckham", "Jonny Wilkinson", "Andrew Flintoff", "Joe Calzaghe", "Ryan Giggs", "Bradley Wiggins", "Lewis Hamilton"], "earliest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-23.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
