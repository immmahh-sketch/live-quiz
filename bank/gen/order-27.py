# Bank session 11 Oct 2026: 3 more Put in order questions -> bank/order-24.json (women's Ballon d'Or, Tour de France and Olympic 100 m winners).
# Each theme was checked against every order question title in the live bank (the server also skips any whose items match one already there).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

A = lambda band, tags, diff, items: o("Music", [band, "albums"] + tags, diff, f"Put these {band} albums in order of release, earliest first", items, "earliest first")
F = lambda who, diff, items: o("Film", [who, "directors"], diff, f"Put these {who} films in order of release, earliest first", items, "earliest first")
o("Football", ["Ballon d'Or", "women's football"], "hard", "Put these women in order of their first Ballon d'Or, earliest first", ["Ada Hegerberg", "Megan Rapinoe", "Alexia Putellas", "Aitana Bonmatí"], "earliest first")
o("Sport", ["Tour de France", "cycling"], "medium", "Put these riders in order of their first Tour de France win, earliest first", ["Miguel Induráin", "Marco Pantani", "Bradley Wiggins", "Chris Froome", "Geraint Thomas", "Tadej Pogačar", "Jonas Vingegaard"], "earliest first")
o("Sport", ["Olympics", "100 metres", "athletics"], "medium", "Put these men in order of their first Olympic 100 m gold, earliest first", ["Carl Lewis", "Linford Christie", "Donovan Bailey", "Maurice Greene", "Usain Bolt", "Marcell Jacobs", "Noah Lyles"], "earliest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-24.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
