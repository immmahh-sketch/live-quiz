# Bank session 10 Oct 2026: 4 more general races -> bank/race-34.json. 20 rows each, target 10; wrong options are
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

race("which city is this museum or gallery in?", "Art and culture", "hard", ["museums", "galleries", "cities"], [
 ("The Louvre", "Paris", ["Lyon", "Marseille", "Nice"]), ("The Prado", "Madrid", ["Barcelona", "Seville", "Valencia"]),
 ("The Uffizi", "Florence", ["Rome", "Venice", "Milan"]), ("The Rijksmuseum", "Amsterdam", ["Rotterdam", "Utrecht", "Antwerp"]),
 ("The Hermitage", "St Petersburg", ["Moscow", "Kyiv", "Riga"]), ("MoMA", "New York", ["Boston", "Philadelphia", "Chicago"]),
 ("The Getty Center", "Los Angeles", ["San Francisco", "San Diego", "Las Vegas"]), ("The Kunsthistorisches Museum", "Vienna", ["Salzburg", "Munich", "Budapest"]),
 ("The Pergamon Museum", "Berlin", ["Munich", "Hamburg", "Dresden"]), ("The Egyptian Museum (Tahrir Square)", "Cairo", ["Alexandria", "Luxor", "Aswan"]),
 ("Tate Modern", "London", ["Liverpool", "St Ives", "Manchester"]), ("Kelvingrove", "Glasgow", ["Edinburgh", "Aberdeen", "Dundee"]),
 ("The Baltic Centre for Contemporary Art", "Gateshead", ["Newcastle", "Sunderland", "Durham"]), ("The Ashmolean", "Oxford", ["Bath", "Bristol", "Winchester"]),
 ("The Fitzwilliam Museum", "Cambridge", ["Bath", "Norwich", "York"]), ("The Smithsonian", "Washington, DC", ["Philadelphia", "Boston", "Baltimore"]),
 ("The Munch Museum", "Oslo", ["Bergen", "Stockholm", "Copenhagen"]), ("The Mauritshuis", "The Hague", ["Rotterdam", "Utrecht", "Leiden"]),
 ("Topkapı Palace", "Istanbul", ["Ankara", "Izmir", "Athens"]), ("Te Papa", "Wellington", ["Auckland", "Christchurch", "Sydney"])])

race("whose middle name is this?", "Celebrities", "hard", ["middle names", "famous people"], [
 ("Hercules", "Elton John", ["Rod Stewart", "George Michael", "Freddie Mercury"]), ("Hussein", "Barack Obama", ["Joe Biden", "Bill Clinton", "Jimmy Carter"]),
 ("Winston", "John Lennon", ["Paul McCartney", "Ringo Starr", "George Harrison"]), ("Hilda", "Margaret Thatcher", ["Theresa May", "Liz Truss", "Edward Heath"]),
 ("Rodney", "Keir Starmer", ["Rishi Sunak", "Gordon Brown", "David Cameron"]), ("Fitzgerald", "John F. Kennedy", ["Harry Truman", "Dwight Eisenhower", "Jimmy Carter"]),
 ("Walker", "George W. Bush", ["Bill Clinton", "Ronald Reagan", "Joe Biden"]), ("Bilius", "Ron Weasley", ["Harry Potter", "Neville Longbottom", "Draco Malfoy"]),
 ("Laurie Blue", "Adele", ["Amy Winehouse", "Duffy", "Lily Allen"]), ("de Pfeffel", "Boris Johnson", ["David Cameron", "Jacob Rees-Mogg", "Michael Gove"]),
 ("Marvolo", "Tom Riddle (Voldemort)", ["Draco Malfoy", "Severus Snape", "Sirius Black"]), ("Tiberius", "Captain James T. Kirk", ["Jean-Luc Picard", "Han Solo", "Mr Spock"]),
 ("Aaron", "Elvis Presley", ["Johnny Cash", "Buddy Holly", "Roy Orbison"]), ("Delano", "Franklin D. Roosevelt", ["Harry Truman", "Woodrow Wilson", "Herbert Hoover"]),
 ("Baines", "Lyndon B. Johnson", ["Harry Truman", "Gerald Ford", "Jimmy Carter"]), ("Milhous", "Richard Nixon", ["Gerald Ford", "Ronald Reagan", "Jimmy Carter"]),
 ("Amadeus", "Mozart", ["Beethoven", "Haydn", "Schubert"]), ("Percival", "Albus Dumbledore", ["Severus Snape", "Sirius Black", "Remus Lupin"]),
 ("Jeffrey", "Tom Hanks", ["Tom Cruise", "Brad Pitt", "Kevin Costner"]), ("Lynton", "Tony Blair", ["Gordon Brown", "John Major", "David Cameron"])])

race("which country does this famous train run in?", "Travel", "medium", ["trains", "railways", "countries"], [
 ("The Flying Scotsman", "the United Kingdom", ["Ireland", "Norway", "Denmark"]), ("The Shinkansen", "Japan", ["Taiwan", "Vietnam", "Thailand"]),
 ("The TGV", "France", ["Belgium", "Luxembourg", "Austria"]), ("The Rocky Mountaineer", "Canada", ["Norway", "Iceland", "Sweden"]),
 ("The Ghan", "Australia", ["Chile", "Argentina", "Indonesia"]), ("The Glacier Express", "Switzerland", ["Austria", "Norway", "Slovenia"]),
 ("The Trans-Siberian", "Russia", ["Mongolia", "Kazakhstan", "Ukraine"]), ("The Blue Train", "South Africa", ["Namibia", "Kenya", "Zimbabwe"]),
 ("The Palace on Wheels", "India", ["Pakistan", "Sri Lanka", "Thailand"]), ("The ICE", "Germany", ["Austria", "Belgium", "the Netherlands"]),
 ("The AVE", "Spain", ["Portugal", "Greece", "Belgium"]), ("The Frecciarossa", "Italy", ["Portugal", "Greece", "Austria"]),
 ("The California Zephyr", "the USA", ["Argentina", "Chile", "Brazil"]), ("The Shanghai Maglev", "China", ["Taiwan", "Vietnam", "Malaysia"]),
 ("The KTX", "South Korea", ["Taiwan", "Vietnam", "Malaysia"]), ("The Tren Maya", "Mexico", ["Guatemala", "Colombia", "Cuba"]),
 ("The Hiram Bingham, to Machu Picchu", "Peru", ["Bolivia", "Ecuador", "Chile"]), ("The Coastal Pacific", "New Zealand", ["Chile", "Argentina", "Fiji"]),
 ("Al Boraq", "Morocco", ["Egypt", "Tunisia", "Algeria"]), ("The Haramain high-speed railway", "Saudi Arabia", ["the UAE", "Qatar", "Oman"])])

race("what's this country's national flower?", "Science and nature", "hard", ["flowers", "national emblems"], [
 ("England", "Rose", ["Poppy", "Daisy", "Lavender"]), ("Scotland", "Thistle", ["Poppy", "Daisy", "Lavender"]),
 ("Wales", "Daffodil", ["Primrose", "Poppy", "Daisy"]), ("Ireland", "Shamrock", ["Poppy", "Primrose", "Daisy"]),
 ("Northern Ireland", "Flax flower", ["Poppy", "Daisy", "Primrose"]), ("The Netherlands", "Tulip", ["Hyacinth", "Crocus", "Iris"]),
 ("India", "Lotus", ["Marigold", "Magnolia", "Gardenia"]), ("Austria", "Edelweiss", ["Crocus", "Poppy", "Iris"]),
 ("Mexico", "Dahlia", ["Marigold", "Poinsettia", "Magnolia"]), ("Australia", "Golden wattle", ["Eucalyptus blossom", "Waratah", "Kangaroo paw"]),
 ("South Africa", "King protea", ["Bird of paradise", "Agapanthus", "Daisy"]), ("Malaysia", "Hibiscus", ["Frangipani", "Bougainvillea", "Marigold"]),
 ("Ukraine", "Sunflower", ["Daisy", "Lavender", "Marigold"]), ("Spain", "Carnation", ["Bougainvillea", "Orange blossom", "Lavender"]),
 ("Pakistan", "Jasmine", ["Marigold", "Frangipani", "Magnolia"]), ("Bangladesh", "Water lily", ["Marigold", "Frangipani", "Magnolia"]),
 ("Finland", "Lily of the valley", ["Heather", "Crocus", "Poppy"]), ("Germany", "Cornflower", ["Poppy", "Daisy", "Gentian"]),
 ("China", "Peony", ["Chrysanthemum", "Magnolia", "Camellia"]), ("Singapore", "Orchid", ["Frangipani", "Bougainvillea", "Gardenia"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-34.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
