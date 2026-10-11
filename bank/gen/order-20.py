# Bank session 11 Oct 2026: 7 more Put in order questions -> bank/order-17.json (sponsors, consoles, games, papers, channels, radio, Wimbledon).
# Each theme was checked against every order question title in the live bank (the server also skips any whose items match one already there).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

A = lambda band, tags, diff, items: o("Music", [band, "albums"] + tags, diff, f"Put these {band} albums in order of release, earliest first", items, "earliest first")
F = lambda who, diff, items: o("Film", [who, "directors"], diff, f"Put these {who} films in order of release, earliest first", items, "earliest first")
o("Football", ["Newcastle United", "shirt sponsors"], "medium", "Put these Newcastle United shirt sponsors in order, earliest first", ["NTL", "Northern Rock", "Virgin Money", "Wonga", "Fun88", "Sela"], "earliest first")
o("Games", ["Sega", "consoles"], "hard", "Put these Sega consoles in order of release, earliest first", ["Master System", "Mega Drive", "Game Gear", "Saturn", "Dreamcast"], "earliest first")
o("Games", ["Mario", "Nintendo"], "medium", "Put these Mario games in order of release, earliest first", ["Donkey Kong", "Super Mario Bros.", "Super Mario World", "Super Mario 64", "Super Mario Galaxy", "Super Mario Odyssey"], "earliest first")
o("History", ["newspapers", "Fleet Street"], "hard", "Put these national newspapers in the order they were founded, earliest first", ["The Times", "The Guardian", "Daily Mail", "Daily Express", "Daily Mirror", "The Sun", "The Independent"], "earliest first")
o("TV", ["TV channels", "broadcasting"], "medium", "Put these UK TV channels in the order they launched, earliest first", ["BBC One", "ITV", "BBC Two", "Channel 4", "Sky One", "Channel 5", "E4"], "earliest first")
o("Music", ["radio", "broadcasting"], "hard", "Put these UK radio stations in the order they launched, earliest first", ["Radio 1", "Capital", "Classic FM", "Virgin Radio", "5 Live", "6 Music", "Radio X"], "earliest first")
o("Sport", ["tennis", "Wimbledon"], "medium", "Put these women in order of their first Wimbledon singles title, earliest first", ["Virginia Wade", "Martina Navratilova", "Steffi Graf", "Venus Williams", "Serena Williams", "Maria Sharapova", "Ashleigh Barty"], "earliest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-17.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
