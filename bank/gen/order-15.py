# Bank session 11 Oct 2026: 15 more Put in order questions -> bank/order-12.json (albums and directors).
# Each theme was checked against every order question title in the live bank (the server also skips any whose items match one already there).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

A = lambda band, tags, diff, items: o("Music", [band, "albums"] + tags, diff, f"Put these {band} albums in order of release, earliest first", items, "earliest first")
F = lambda who, diff, items: o("Film", [who, "directors"], diff, f"Put these {who} films in order of release, earliest first", items, "earliest first")
A("Mumford & Sons", ["folk"], "medium", ["Sigh No More", "Babel", "Wilder Mind", "Delta", "Rushmere"])
A("Boyzone", ["boy bands", "Ireland"], "hard", ["Said and Done", "A Different Beat", "Where We Belong", "Brother", "BZ20"])
A("Sugababes", ["girl groups"], "hard", ["One Touch", "Angels with Dirty Faces", "Three", "Taller in More Ways", "Change", "Catfights and Spotlights"])
A("Stormzy", ["grime"], "easy", ["Gang Signs & Prayer", "Heavy Is the Head", "This Is What I Mean"])
A("UB40", ["reggae", "Birmingham"], "hard", ["Signing Off", "Present Arms", "Labour of Love", "Rat in the Kitchen", "Promises and Lies"])
A("Simple Minds", ["Scotland", "1980s"], "hard", ["New Gold Dream (81–82–83–84)", "Sparkle in the Rain", "Once Upon a Time", "Street Fighting Years"])
A("Erasure", ["synth-pop"], "hard", ["Wonderland", "The Circus", "The Innocents", "Wild!", "Chorus"])
A("Culture Club", ["1980s"], "medium", ["Kissing to Be Clever", "Colour by Numbers", "Waking Up with the House on Fire", "From Luxury to Heartache"])
A("Elton John", ["solo"], "hard", ["Elton John", "Madman Across the Water", "Honky Château", "Goodbye Yellow Brick Road", "Captain Fantastic and the Brown Dirt Cowboy", "Too Low for Zero", "The Lockdown Sessions"])
A("Kylie Minogue", ["pop"], "medium", ["Kylie", "Enjoy Yourself", "Rhythm of Love", "Light Years", "Fever", "Aphrodite", "Tension"])
A("Keane", [], "hard", ["Hopes and Fears", "Under the Iron Sea", "Perfect Symmetry", "Strangeland", "Cause and Effect"])
F("Sam Mendes", "medium", ["American Beauty", "Road to Perdition", "Revolutionary Road", "Skyfall", "Spectre", "1917", "Empire of Light"])
F("Paul Thomas Anderson", "hard", ["Boogie Nights", "Magnolia", "There Will Be Blood", "The Master", "Phantom Thread", "Licorice Pizza", "One Battle After Another"])
F("Kathryn Bigelow", "hard", ["Point Break", "Strange Days", "The Hurt Locker", "Zero Dark Thirty", "Detroit"])
F("Baz Luhrmann", "medium", ["Strictly Ballroom", "Romeo + Juliet", "Moulin Rouge!", "Australia", "The Great Gatsby", "Elvis"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-12.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
