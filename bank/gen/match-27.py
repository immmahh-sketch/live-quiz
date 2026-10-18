# Bank session 18 Oct 2026: 6 Match questions -> bank/match-27.json (newspaper nicknames, Roman roads, plant Latin names,
# Tyne bridges, famous diarists, the Wombles). Each topic probed against every match question in the live bank first
# (North East castles, spacecraft and London termini were already there, so they were left out).
# Import with: node tools/import-bank.mjs match
import json, os
OUT = []
def m(cat, tags, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff, "category": cat, "tags": tags})

m("Everyday life", ["newspapers", "nicknames", "press"], "hard", "Match each newspaper to its nickname",
  ("The Guardian", "The Grauniad"), ("The Times", "The Thunderer"), ("The Daily Telegraph", "The Torygraph"), ("Financial Times", "The Pink 'Un"))
m("British history", ["Romans", "roads", "Roman Britain"], "hard", "Match each Roman road to the route it ran",
  ("Watling Street", "Dover to Wroxeter, via London"), ("Ermine Street", "London to York"), ("Fosse Way", "Exeter to Lincoln"), ("Dere Street", "York to Scotland"))
m("Nature and the environment", ["plants", "Latin names", "wild flowers"], "hard", "Match each Latin plant name to its common name",
  ("Digitalis", "Foxglove"), ("Galanthus", "Snowdrop"), ("Taraxacum", "Dandelion"), ("Bellis perennis", "Daisy"))
m("Tyne and Wear", ["Newcastle", "Gateshead", "bridges", "North East"], "medium", "Match each Tyne bridge to what it's known for",
  ("Tyne Bridge", "Green steel arch, opened in 1928"), ("Swing Bridge", "Turns to let ships through"),
  ("High Level Bridge", "Road and railway on two decks"), ("Gateshead Millennium Bridge", "Tilts like a blinking eye"))
m("Books and literature", ["diaries", "Pepys", "Anne Frank", "Adrian Mole"], "medium", "Match each diarist to a famous detail from their diary",
  ("Samuel Pepys", "Buried his Parmesan during the Great Fire"), ("Anne Frank", "Called her diary Kitty"),
  ("Adrian Mole", "Aged 13¾"), ("Bridget Jones", "Counted calories, units and cigarettes"))
m("Children's TV", ["Wombles", "children's TV", "1970s TV"], "medium", "Match each Womble to what they're known for",
  ("Great Uncle Bulgaria", "The oldest, who leads the burrow"), ("Orinoco", "Lazy and always hungry"),
  ("Tobermory", "Handyman who fixes everything"), ("Wellington", "Shy, bespectacled scientist"))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'match-27.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'match questions written')
