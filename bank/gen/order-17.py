# Bank session 11 Oct 2026: 15 more Put in order questions -> bank/order-14.json (rock albums and directors).
# Each theme was checked against every order question title in the live bank (the server also skips any whose items match one already there).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

A = lambda band, tags, diff, items: o("Music", [band, "albums"] + tags, diff, f"Put these {band} albums in order of release, earliest first", items, "earliest first")
F = lambda who, diff, items: o("Film", [who, "directors"], diff, f"Put these {who} films in order of release, earliest first", items, "earliest first")
A("Guns N' Roses", ["rock"], "medium", ["Appetite for Destruction", "G N' R Lies", "Use Your Illusion I", "The Spaghetti Incident?", "Chinese Democracy"])
A("AC/DC", ["rock"], "hard", ["High Voltage", "Highway to Hell", "Back in Black", "For Those About to Rock We Salute You", "The Razors Edge", "Black Ice", "Power Up"])
A("Led Zeppelin", ["rock"], "hard", ["Led Zeppelin II", "Led Zeppelin III", "Houses of the Holy", "Physical Graffiti", "Presence", "In Through the Out Door"])
A("Iron Maiden", ["heavy metal"], "hard", ["Iron Maiden", "The Number of the Beast", "Piece of Mind", "Powerslave", "Seventh Son of a Seventh Son", "Brave New World", "Senjutsu"])
A("Def Leppard", ["rock", "Sheffield"], "hard", ["On Through the Night", "High 'n' Dry", "Pyromania", "Hysteria", "Adrenalize", "Slang"])
A("Aerosmith", ["rock"], "hard", ["Toys in the Attic", "Rocks", "Permanent Vacation", "Pump", "Get a Grip", "Nine Lives"])
A("Linkin Park", ["rock"], "medium", ["Hybrid Theory", "Meteora", "Minutes to Midnight", "A Thousand Suns", "Living Things", "One More Light", "From Zero"])
A("Blink-182", ["pop punk"], "hard", ["Dude Ranch", "Enema of the State", "Take Off Your Pants and Jacket", "Neighborhoods", "California", "One More Time..."])
A("Feeder", ["Wales"], "hard", ["Polythene", "Yesterday Went Too Soon", "Echo Park", "Comfort in Sound", "Pushing the Senses"])
A("Doves", ["Manchester"], "hard", ["Lost Souls", "The Last Broadcast", "Some Cities", "Kingdom of Rust", "The Universal Want"])
F("Francis Ford Coppola", "medium", ["The Godfather", "The Godfather Part II", "Apocalypse Now", "The Outsiders", "The Godfather Part III", "Bram Stoker's Dracula", "Megalopolis"])
F("Sam Raimi", "hard", ["The Evil Dead", "Evil Dead II", "Army of Darkness", "Spider-Man", "Spider-Man 2", "Drag Me to Hell", "Doctor Strange in the Multiverse of Madness"])
F("Ron Howard", "medium", ["Splash", "Cocoon", "Apollo 13", "A Beautiful Mind", "The Da Vinci Code", "Rush"])
F("Steven Soderbergh", "hard", ["Sex, Lies, and Videotape", "Out of Sight", "Erin Brockovich", "Ocean's Eleven", "Contagion", "Magic Mike", "Logan Lucky"])
F("Ari Aster", "hard", ["Hereditary", "Midsommar", "Beau Is Afraid", "Eddington"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-14.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
