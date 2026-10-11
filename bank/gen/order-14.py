# Bank session 11 Oct 2026: 15 more Put in order questions -> bank/order-11.json (albums from the 1980s on).
# Each theme was checked against every order question title in the live bank (the server also skips any whose items match one already there).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

A = lambda band, tags, diff, items: o("Music", [band, "albums"] + tags, diff, f"Put these {band} albums in order of release, earliest first", items, "earliest first")
A("Simply Red", [], "hard", ["Picture Book", "Men and Women", "A New Flame", "Stars", "Life", "Blue", "Home"])
A("Pet Shop Boys", [], "hard", ["Please", "Actually", "Introspective", "Behaviour", "Very", "Bilingual", "Nightlife"])
A("Duran Duran", ["1980s"], "hard", ["Duran Duran", "Rio", "Seven and the Ragged Tiger", "Notorious", "Big Thing", "Future Past"])
A("Bon Jovi", [], "hard", ["Slippery When Wet", "New Jersey", "Keep the Faith", "These Days", "Crush", "Have a Nice Day", "Lost Highway"])
A("Metallica", ["heavy metal"], "hard", ["Kill 'Em All", "Ride the Lightning", "Master of Puppets", "...And Justice for All", "Metallica", "Load", "St. Anger"])
A("Nirvana", ["grunge"], "easy", ["Bleach", "Nevermind", "In Utero"])
A("Foo Fighters", [], "hard", ["Foo Fighters", "The Colour and the Shape", "There Is Nothing Left to Lose", "One by One", "In Your Honor", "Echoes, Silence, Patience & Grace", "Wasting Light"])
A("Red Hot Chili Peppers", [], "hard", ["Mother's Milk", "Blood Sugar Sex Magik", "One Hot Minute", "Californication", "By the Way", "Stadium Arcadium", "I'm with You"])
A("Green Day", ["punk"], "medium", ["Dookie", "Insomniac", "Nimrod", "Warning", "American Idiot", "21st Century Breakdown"])
A("Verve", ["Britpop"], "medium", ["A Storm in Heaven", "A Northern Soul", "Urban Hymns", "Forth"])
A("Travis", ["Scotland"], "hard", ["Good Feeling", "The Man Who", "The Invisible Band", "12 Memories", "The Boy with No Name"])
A("Westlife", ["boy bands", "Ireland"], "hard", ["Westlife", "Coast to Coast", "World of Our Own", "Turnaround", "Face to Face", "The Love Album", "Back Home"])
o("Music", ["George Michael", "albums"], "medium", "Put George Michael's solo albums in order of release, earliest first", ["Faith", "Listen Without Prejudice Vol. 1", "Older", "Patience"], "earliest first")
A("Madness", ["ska"], "hard", ["One Step Beyond...", "Absolutely", "7", "The Rise & Fall", "Keep Moving", "Mad Not Mad"])
A("Spandau Ballet", ["1980s"], "hard", ["Journeys to Glory", "Diamond", "True", "Parade", "Through the Barricades"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-11.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
