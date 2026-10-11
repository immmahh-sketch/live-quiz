# Bank session 11 Oct 2026: 15 more Put in order questions -> bank/order-10.json (albums, directors, a TV writer).
# Each theme was checked against every order question title in the live bank (the server also skips any whose items match one already there).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

o("Music", ["Florence + the Machine", "albums"], "hard", "Put these Florence + the Machine albums in order of release, earliest first", ["Lungs", "Ceremonials", "How Big, How Blue, How Beautiful", "High as Hope", "Dance Fever"], "earliest first")
o("Music", ["Kasabian", "albums"], "hard", "Put these Kasabian albums in order of release, earliest first", ["Kasabian", "Empire", "West Ryder Pauper Lunatic Asylum", "Velociraptor!", "48:13", "For Crying Out Loud", "The Alchemist's Euphoria"], "earliest first")
o("Music", ["Biffy Clyro", "albums", "Scotland"], "hard", "Put these Biffy Clyro albums in order of release, earliest first", ["Puzzle", "Only Revolutions", "Opposites", "Ellipsis", "A Celebration of Endings", "The Myth of the Happily Ever After"], "earliest first")
o("Music", ["Paolo Nutini", "albums", "Scotland"], "medium", "Put Paolo Nutini's albums in order of release, earliest first", ["These Streets", "Sunny Side Up", "Caustic Love", "Last Night in the Bittersweet"], "earliest first")
o("Music", ["Dua Lipa", "albums"], "easy", "Put Dua Lipa's albums in order of release, earliest first", ["Dua Lipa", "Future Nostalgia", "Radical Optimism"], "earliest first")
o("Music", ["Harry Styles", "albums"], "easy", "Put Harry Styles's solo albums in order of release, earliest first", ["Harry Styles", "Fine Line", "Harry's House"], "earliest first")
o("Music", ["Bruce Springsteen", "albums"], "hard", "Put these Bruce Springsteen albums in order of release, earliest first", ["Born to Run", "Darkness on the Edge of Town", "The River", "Nebraska", "Born in the U.S.A.", "Tunnel of Love", "The Rising"], "earliest first")
o("Music", ["The Cure", "albums"], "hard", "Put these Cure albums in order of release, earliest first", ["Three Imaginary Boys", "Seventeen Seconds", "Pornography", "The Head on the Door", "Disintegration", "Wish", "Songs of a Lost World"], "earliest first")
o("Music", ["Depeche Mode", "albums"], "hard", "Put these Depeche Mode albums in order of release, earliest first", ["Speak & Spell", "Some Great Reward", "Black Celebration", "Music for the Masses", "Violator", "Songs of Faith and Devotion", "Ultra"], "earliest first")
o("Film", ["Denis Villeneuve", "directors"], "medium", "Put these Denis Villeneuve films in order of release, earliest first", ["Prisoners", "Sicario", "Arrival", "Blade Runner 2049", "Dune", "Dune: Part Two"], "earliest first")
o("Film", ["Greta Gerwig", "directors"], "easy", "Put these Greta Gerwig films in order of release, earliest first", ["Lady Bird", "Little Women", "Barbie"], "earliest first")
o("Film", ["David Fincher", "directors"], "medium", "Put these David Fincher films in order of release, earliest first", ["Se7en", "The Game", "Fight Club", "Panic Room", "Zodiac", "The Social Network", "Gone Girl"], "earliest first")
o("Film", ["Mike Leigh", "directors"], "hard", "Put these Mike Leigh films in order of release, earliest first", ["Life Is Sweet", "Naked", "Secrets & Lies", "Topsy-Turvy", "Vera Drake", "Mr. Turner"], "earliest first")
o("Film", ["Shane Meadows", "directors"], "hard", "Put these Shane Meadows films in order of release, earliest first", ["TwentyFourSeven", "A Room for Romeo Brass", "Dead Man's Shoes", "This Is England", "Somers Town"], "earliest first")
o("TV", ["Jed Mercurio", "British drama"], "medium", "Put these Jed Mercurio dramas in order of first airing, earliest first", ["Cardiac Arrest", "Bodies", "Line of Duty", "Bodyguard"], "earliest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-10.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
