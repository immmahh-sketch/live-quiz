# Bank session 11 Oct 2026: 7 more Put in order questions -> bank/order-18.json (space, poets, Bond books and sporting hosts).
# Each theme was checked against every order question title in the live bank (the server also skips any whose items match one already there).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

A = lambda band, tags, diff, items: o("Music", [band, "albums"] + tags, diff, f"Put these {band} albums in order of release, earliest first", items, "earliest first")
F = lambda who, diff, items: o("Film", [who, "directors"], diff, f"Put these {who} films in order of release, earliest first", items, "earliest first")
o("Science", ["Mars", "space"], "hard", "Put these Mars landers and rovers in order of landing, earliest first", ["Viking 1", "Mars Pathfinder", "Spirit", "Phoenix", "Curiosity", "InSight", "Perseverance"], "earliest first")
o("Science", ["space telescopes", "space"], "medium", "Put these space telescopes in order of launch, earliest first", ["Hubble", "Chandra", "Spitzer", "Kepler", "TESS", "James Webb"], "earliest first")
o("Books", ["Poets Laureate", "poetry"], "hard", "Put these Poets Laureate in order of appointment, earliest first", ["William Wordsworth", "Alfred, Lord Tennyson", "John Betjeman", "Ted Hughes", "Andrew Motion", "Carol Ann Duffy", "Simon Armitage"], "earliest first")
o("Books", ["James Bond", "Ian Fleming"], "hard", "Put these Ian Fleming Bond novels in order of publication, earliest first", ["Casino Royale", "Live and Let Die", "Moonraker", "Diamonds Are Forever", "From Russia, with Love", "Dr. No", "Goldfinger"], "earliest first")
o("Sport", ["Commonwealth Games", "hosts"], "hard", "Put these Commonwealth Games hosts in order, earliest first", ["Edinburgh", "Auckland", "Victoria", "Kuala Lumpur", "Manchester", "Delhi", "Birmingham"], "earliest first")
o("Sport", ["Winter Olympics", "hosts"], "medium", "Put these Winter Olympics hosts in order, earliest first", ["Lillehammer", "Nagano", "Salt Lake City", "Turin", "Vancouver", "Sochi", "PyeongChang"], "earliest first")
o("Sport", ["cricket", "World Cup"], "hard", "Put these countries in order of their first men's Cricket World Cup win, earliest first", ["West Indies", "India", "Australia", "Pakistan", "Sri Lanka", "England"], "earliest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-18.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
