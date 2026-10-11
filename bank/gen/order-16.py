# Bank session 11 Oct 2026: 15 more Put in order questions -> bank/order-13.json (albums and directors).
# Each theme was checked against every order question title in the live bank (the server also skips any whose items match one already there).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

A = lambda band, tags, diff, items: o("Music", [band, "albums"] + tags, diff, f"Put these {band} albums in order of release, earliest first", items, "earliest first")
F = lambda who, diff, items: o("Film", [who, "directors"], diff, f"Put these {who} films in order of release, earliest first", items, "earliest first")
A("Lana Del Rey", [], "hard", ["Born to Die", "Ultraviolence", "Honeymoon", "Lust for Life", "Did You Know That There's a Tunnel Under Ocean Blvd"])
A("Billie Eilish", [], "easy", ["When We All Fall Asleep, Where Do We Go?", "Happier Than Ever", "Hit Me Hard and Soft"])
A("Smiths", ["Manchester", "1980s"], "medium", ["The Smiths", "Meat Is Murder", "The Queen Is Dead", "Strangeways, Here We Come"])
A("New Order", ["Manchester"], "hard", ["Movement", "Power, Corruption & Lies", "Low-Life", "Brotherhood", "Technique", "Republic"])
A("Jam", ["punk", "mod"], "hard", ["In the City", "All Mod Cons", "Setting Sons", "Sound Affects", "The Gift"])
A("Clash", ["punk"], "medium", ["The Clash", "Give 'Em Enough Rope", "London Calling", "Sandinista!", "Combat Rock"])
A("Blondie", ["new wave"], "hard", ["Blondie", "Parallel Lines", "Eat to the Beat", "Autoamerican", "The Hunter", "No Exit"])
A("Talking Heads", ["new wave"], "hard", ["Talking Heads: 77", "More Songs About Buildings and Food", "Fear of Music", "Remain in Light", "Speaking in Tongues", "Little Creatures"])
A("R.E.M.", [], "hard", ["Murmur", "Document", "Green", "Out of Time", "Automatic for the People", "Monster", "Up"])
A("Pearl Jam", ["grunge"], "hard", ["Ten", "Vs.", "Vitalogy", "No Code", "Yield"])
F("Martin McDonagh", "medium", ["In Bruges", "Seven Psychopaths", "Three Billboards Outside Ebbing, Missouri", "The Banshees of Inisherin"])
F("Clint Eastwood", "hard", ["Play Misty for Me", "The Outlaw Josey Wales", "Unforgiven", "Mystic River", "Million Dollar Baby", "Gran Torino", "American Sniper"])
F("David Lynch", "hard", ["Eraserhead", "The Elephant Man", "Dune", "Blue Velvet", "Wild at Heart", "Lost Highway", "Mulholland Drive"])
F("Robert Zemeckis", "medium", ["Romancing the Stone", "Back to the Future", "Who Framed Roger Rabbit", "Forrest Gump", "Contact", "Cast Away", "The Polar Express"])
F("Taika Waititi", "medium", ["Boy", "What We Do in the Shadows", "Hunt for the Wilderpeople", "Thor: Ragnarok", "Jojo Rabbit", "Thor: Love and Thunder"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-13.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
