# Bank session 10 Oct 2026: 18 more Put in order questions -> bank/order-8.json (directors, albums, books, science, everyday Britain).
# Checked against every order question in the live bank (the server also skips any whose items match one already there).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

o("Film", ["Martin Scorsese", "directors"], "medium", "Put these Martin Scorsese films in order of release, earliest first", ["Taxi Driver", "Raging Bull", "Goodfellas", "Casino", "The Departed", "The Wolf of Wall Street", "The Irishman"], "earliest first")
o("Film", ["Ridley Scott", "directors"], "medium", "Put these Ridley Scott films in order of release, earliest first", ["Alien", "Blade Runner", "Thelma & Louise", "Gladiator", "Black Hawk Down", "The Martian", "Napoleon"], "earliest first")
o("Film", ["Danny Boyle", "directors"], "medium", "Put these Danny Boyle films in order of release, earliest first", ["Shallow Grave", "Trainspotting", "The Beach", "28 Days Later", "Slumdog Millionaire", "127 Hours", "Yesterday"], "earliest first")
o("Film", ["Stanley Kubrick", "directors"], "hard", "Put these Stanley Kubrick films in order of release, earliest first", ["Dr. Strangelove", "2001: A Space Odyssey", "A Clockwork Orange", "Barry Lyndon", "The Shining", "Full Metal Jacket", "Eyes Wide Shut"], "earliest first")
o("Film", ["Coen brothers", "directors"], "hard", "Put these Coen brothers films in order of release, earliest first", ["Fargo", "The Big Lebowski", "O Brother, Where Art Thou?", "No Country for Old Men", "Burn After Reading", "True Grit", "Inside Llewyn Davis"], "earliest first")
o("Film", ["Wes Anderson", "directors"], "hard", "Put these Wes Anderson films in order of release, earliest first", ["Rushmore", "The Royal Tenenbaums", "The Life Aquatic with Steve Zissou", "Fantastic Mr Fox", "Moonrise Kingdom", "The Grand Budapest Hotel", "Isle of Dogs"], "earliest first")
o("Film", ["Tim Burton", "directors"], "medium", "Put these Tim Burton films in order of release, earliest first", ["Beetlejuice", "Batman", "Edward Scissorhands", "Sleepy Hollow", "Charlie and the Chocolate Factory", "Alice in Wonderland"], "earliest first")
o("Music", ["Muse", "albums"], "hard", "Put these Muse albums in order of release, earliest first", ["Showbiz", "Origin of Symmetry", "Absolution", "Black Holes and Revelations", "The Resistance", "The 2nd Law", "Drones"], "earliest first")
o("Music", ["Pulp", "albums", "Britpop"], "hard", "Put these Pulp albums in order of release, earliest first", ["It", "Freaks", "Separations", "His 'n' Hers", "Different Class", "This Is Hardcore", "We Love Life"], "earliest first")
o("Music", ["Manic Street Preachers", "albums"], "hard", "Put these Manic Street Preachers albums in order of release, earliest first", ["Generation Terrorists", "Gold Against the Soul", "The Holy Bible", "Everything Must Go", "This Is My Truth Tell Me Yours", "Know Your Enemy", "Send Away the Tigers"], "earliest first")
o("Books", ["Sherlock Holmes", "Arthur Conan Doyle", "novels"], "hard", "Put the four Sherlock Holmes novels in order of publication, earliest first", ["A Study in Scarlet", "The Sign of the Four", "The Hound of the Baskervilles", "The Valley of Fear"], "earliest first")
o("Children's books", ["Julia Donaldson", "picture books"], "medium", "Put these Julia Donaldson books in order of publication, earliest first", ["The Gruffalo", "Room on the Broom", "The Snail and the Whale", "Stick Man", "Zog", "The Highway Rat", "The Smeds and the Smoos"], "earliest first")
o("Science", ["biology", "classification"], "hard", "Put these ranks used to classify living things in order, broadest first", ["Kingdom", "Phylum", "Class", "Order", "Family", "Genus", "Species"], "broadest first")
o("Everyday life", ["roads", "speed limits"], "easy", "Put these roads in order of their usual speed limit for a car, lowest first", ["A 20 zone outside a school", "A built-up street", "A country single carriageway", "A motorway"], "lowest first")
o("UK geography", ["Scotland", "cities"], "hard", "Put these Scottish cities in order from north to south", ["Inverness", "Aberdeen", "Dundee", "Perth", "Stirling", "Edinburgh", "Glasgow"], "north to south")
o("Everyday life", ["school", "education"], "easy", "Put these stages of education in order, youngest first", ["Nursery", "Reception", "Primary school", "Secondary school", "Sixth form", "University"], "youngest first")
o("Everyday life", ["coins", "money"], "medium", "Put these coins in the order they first appeared, earliest first", ["50p", "20p", "£1 coin", "£2 coin"], "earliest first")
o("TV", ["Bake Off", "baking"], "easy", "Put these parts of a 'Bake Off' week in order", ["Signature bake", "Technical challenge", "Showstopper", "Star Baker announced", "Someone leaves the tent"], "first to last")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-8.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
