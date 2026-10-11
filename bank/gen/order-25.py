# Bank session 11 Oct 2026: 6 more Put in order questions -> bank/order-22.json (screen Catwomen, Alfreds, Gordons, Lex Luthors, Lois Lanes and Qs).
# Each theme was checked against every order question title in the live bank (the server also skips any whose items match one already there).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

A = lambda band, tags, diff, items: o("Music", [band, "albums"] + tags, diff, f"Put these {band} albums in order of release, earliest first", items, "earliest first")
F = lambda who, diff, items: o("Film", [who, "directors"], diff, f"Put these {who} films in order of release, earliest first", items, "earliest first")
o("Film", ["Catwoman", "Batman", "actresses"], "medium", "Put these screen Catwomen in order, earliest first", ["Julie Newmar", "Michelle Pfeiffer", "Halle Berry", "Anne Hathaway", "Zoë Kravitz"], "earliest first")
o("Film", ["Alfred", "Batman", "actors"], "medium", "Put these actors in the order they first played Batman's butler Alfred on film, earliest first", ["Michael Gough", "Michael Caine", "Jeremy Irons", "Andy Serkis"], "earliest first")
o("Film", ["Commissioner Gordon", "Batman", "actors"], "hard", "Put these film Commissioner Gordons in order, earliest first", ["Pat Hingle", "Gary Oldman", "J. K. Simmons", "Jeffrey Wright"], "earliest first")
o("Film", ["Lex Luthor", "Superman", "actors"], "medium", "Put these film Lex Luthors in order, earliest first", ["Gene Hackman", "Kevin Spacey", "Jesse Eisenberg", "Nicholas Hoult"], "earliest first")
o("Film", ["Lois Lane", "Superman", "actresses"], "medium", "Put these screen Lois Lanes in order, earliest first", ["Margot Kidder", "Teri Hatcher", "Kate Bosworth", "Amy Adams", "Rachel Brosnahan"], "earliest first")
o("Film", ["James Bond", "Q", "actors"], "easy", "Put these actors who played Q in the Bond films in order, earliest first", ["Desmond Llewelyn", "John Cleese", "Ben Whishaw"], "earliest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-22.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
