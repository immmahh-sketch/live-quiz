# Bank session 11 Oct 2026: 4 more Put in order questions -> bank/order-19.json (Doctor Who monsters, Bond girls, charity concerts, Supergrass).
# Each theme was checked against every order question title in the live bank (the server also skips any whose items match one already there).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

A = lambda band, tags, diff, items: o("Music", [band, "albums"] + tags, diff, f"Put these {band} albums in order of release, earliest first", items, "earliest first")
F = lambda who, diff, items: o("Film", [who, "directors"], diff, f"Put these {who} films in order of release, earliest first", items, "earliest first")
o("TV", ["Doctor Who", "monsters"], "medium", "Put these Doctor Who monsters in order of first appearance, earliest first", ["Daleks", "Cybermen", "Sontarans", "Zygons", "The Ood", "Weeping Angels", "The Silence"], "earliest first")
o("Film", ["James Bond", "Bond girls"], "medium", "Put these Bond girls in the order of their film, earliest first", ["Honey Ryder", "Pussy Galore", "Solitaire", "Holly Goodhead", "Xenia Onatopp", "Vesper Lynd", "Madeleine Swann"], "earliest first")
o("Music", ["charity", "concerts"], "medium", "Put these charity concerts in order, earliest first", ["The Concert for Bangladesh", "Live Aid", "Nelson Mandela 70th Birthday Tribute", "The Freddie Mercury Tribute Concert", "Live 8", "One Love Manchester"], "earliest first")
A("Supergrass", ["Britpop", "Oxford"], "hard", ["I Should Coco", "In It for the Money", "Supergrass", "Life on Other Planets", "Road to Rouen", "Diamond Hoo Ha"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-19.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
