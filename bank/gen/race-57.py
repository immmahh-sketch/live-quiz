# Bank session 10 Oct 2026: 3 more general races -> bank/race-57.json. 20 rows each, target 10; wrong options are
# the same kind of thing, never another row's right answer, and never also right for that row.
import json, os
R = []
def race(title, cat, diff, tags, rows):
    rights = {r[1] for r in rows}
    assert len(rows) == 20, (title, len(rows))
    assert len(rights) == 20, (title, 'duplicate right answers')
    bad = [(q, w) for q, right, wrong in rows for w in wrong if w in rights]
    assert not bad, (title, 'recycled', bad)
    for q, right, wrong in rows:
        assert len(wrong) == 3 and len(set(wrong)) == 3 and right not in wrong, (title, q)
    R.append({"type": "race", "text": "The Race: " + title, "target": 10, "category": cat, "tags": tags, "difficulty": diff,
              "bank": [{"q": q, "right": right, "wrong": wrong} for q, right, wrong in rows]})

race("what does this sailing word mean?", "Words and language", "medium", ["sailing", "ships", "words"], [
 ("Port", "Left side", ["Top deck", "Middle", "Lower deck"]), ("Starboard", "Right side", ["Top deck", "Middle", "Lower deck"]),
 ("Bow", "Front", ["Middle", "Top deck", "Lower deck"]), ("Stern", "Back", ["Middle", "Top deck", "Lower deck"]),
 ("Galley", "Kitchen", ["Dining room", "Storeroom", "Lounge"]), ("Head", "Toilet", ["Captain's cabin", "Lookout post", "Crow's nest"]),
 ("Bulkhead", "Wall", ["Ceiling", "Roof", "Stairs"]), ("Deck", "Floor", ["Ceiling", "Roof", "Stairs"]),
 ("Hull", "Main body", ["Engine room", "Cargo hold", "Sail"]), ("Keel", "Spine along the bottom", ["Sail", "Flag", "Crow's nest"]),
 ("Bilge", "Lowest part inside", ["Crow's nest", "Lookout post", "Top deck"]), ("Berth", "Bed", ["Cupboard", "Ladder", "Deckchair"]),
 ("Brig", "Prison", ["Lounge", "Storeroom", "Dining room"]), ("Helm", "Steering wheel", ["Engine room", "Lifeboat", "Anchor"]),
 ("Leeward", "Side away from the wind", ["Sunny side", "Shady side", "Quayside"]), ("Windward", "Side facing the wind", ["Sunny side", "Shady side", "Quayside"]),
 ("Gunwale", "Top edge of the side", ["Ladder", "Plank", "Rope"]), ("Porthole", "Window", ["Ladder", "Cupboard", "Plank"]),
 ("Ballast", "Weight for balance", ["Rope", "Anchor", "Engine room"]), ("Hatch", "Door in the deck", ["Ladder", "Cupboard", "Plank"])])

race("who wrote this famous non-fiction book?", "Books", "medium", ["non-fiction", "authors"], [
 ("A Brief History of Time", "Stephen Hawking", ["Carl Sagan", "Brian Cox", "Richard Feynman"]),
 ("On the Origin of Species", "Charles Darwin", ["Alfred Russel Wallace", "Thomas Huxley", "Gregor Mendel"]),
 ("Silent Spring", "Rachel Carson", ["Jane Goodall", "Dian Fossey", "Gloria Steinem"]),
 ("The Selfish Gene", "Richard Dawkins", ["Steven Pinker", "Christopher Hitchens", "Sam Harris"]),
 ("Sapiens", "Yuval Noah Harari", ["Jared Diamond", "Steven Pinker", "Mary Beard"]),
 ("The Diary of a Young Girl", "Anne Frank", ["Zlata Filipović", "Malala Yousafzai", "Corrie ten Boom"]),
 ("Long Walk to Freedom", "Nelson Mandela", ["Desmond Tutu", "Steve Biko", "Barack Obama"]),
 ("I Know Why the Caged Bird Sings", "Maya Angelou", ["Toni Morrison", "Alice Walker", "Zora Neale Hurston"]),
 ("A Room of One's Own", "Virginia Woolf", ["Simone de Beauvoir", "Germaine Greer", "Mary Wollstonecraft"]),
 ("The Wealth of Nations", "Adam Smith", ["John Maynard Keynes", "David Hume", "Milton Friedman"]),
 ("Das Kapital", "Karl Marx", ["Lenin", "Leon Trotsky", "Mao Zedong"]),
 ("The Prince", "Niccolò Machiavelli", ["Thomas More", "Erasmus", "Dante"]),
 ("The Art of War", "Sun Tzu", ["Confucius", "Lao Tzu", "Genghis Khan"]),
 ("Leviathan", "Thomas Hobbes", ["John Locke", "Jean-Jacques Rousseau", "David Hume"]),
 ("The Tipping Point", "Malcolm Gladwell", ["Nassim Taleb", "Daniel Kahneman", "Steven Pinker"]),
 ("Becoming", "Michelle Obama", ["Hillary Clinton", "Oprah Winfrey", "Barack Obama"]),
 ("Spare", "Prince Harry", ["Prince William", "Meghan Markle", "Prince Andrew"]),
 ("In Cold Blood", "Truman Capote", ["Norman Mailer", "Tom Wolfe", "Hunter S. Thompson"]),
 ("Into the Wild", "Jon Krakauer", ["Bill Bryson", "Paul Theroux", "Bruce Chatwin"]),
 ("Bad Science", "Ben Goldacre", ["Brian Cox", "Adam Rutherford", "Simon Singh"])])

race("which town or city is this theatre in?", "Art and culture", "hard", ["theatres", "cities"], [
 ("Shakespeare's Globe", "London", ["Oxford", "Bristol", "Bath"]), ("The Abbey Theatre", "Dublin", ["Cork", "Galway", "Limerick"]),
 ("The Comédie-Française", "Paris", ["Lyon", "Marseille", "Bordeaux"]), ("The Burgtheater", "Vienna", ["Salzburg", "Graz", "Munich"]),
 ("The Crucible Theatre", "Sheffield", ["Leeds", "Rotherham", "Doncaster"]), ("The Royal Exchange Theatre", "Manchester", ["Bolton", "Salford", "Stockport"]),
 ("Northern Stage", "Newcastle", ["Sunderland", "Gateshead", "Durham"]), ("The Royal Lyceum Theatre", "Edinburgh", ["Aberdeen", "Dundee", "Perth"]),
 ("The Citizens Theatre", "Glasgow", ["Aberdeen", "Dundee", "Perth"]), ("The Everyman Theatre", "Liverpool", ["Chester", "Preston", "Bolton"]),
 ("The Royal Shakespeare Theatre", "Stratford-upon-Avon", ["Warwick", "Coventry", "Oxford"]), ("The Minack Theatre, cut into the cliffs", "Porthcurno", ["St Ives", "Penzance", "Falmouth"]),
 ("Ford's Theatre, where Lincoln was shot", "Washington, DC", ["Philadelphia", "Baltimore", "Richmond"]), ("The Berliner Ensemble", "Berlin", ["Hamburg", "Munich", "Dresden"]),
 ("The Stephen Joseph Theatre", "Scarborough", ["Whitby", "York", "Harrogate"]), ("The Alhambra Theatre", "Bradford", ["Leeds", "Huddersfield", "Halifax"]),
 ("The Grand Opera House", "Belfast", ["Derry", "Cork", "Lisburn"]), ("The Lincoln Center", "New York", ["Boston", "Philadelphia", "Chicago"]),
 ("The Teatro Real", "Madrid", ["Barcelona", "Seville", "Valencia"]), ("The New Vic", "Newcastle-under-Lyme", ["Newcastle upon Tyne", "Crewe", "Stafford"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-57.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
