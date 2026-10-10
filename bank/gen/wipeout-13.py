# Bank session 10 Oct 2026: new Wipeout boards -> bank/wipeout-13.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Sea areas in the BBC Shipping Forecast", "Britain", "hard", ["Shipping Forecast", "sea areas"],
 ["Viking", "Forties", "Cromarty", "Tyne", "Dogger", "German Bight", "Humber", "Thames", "Dover", "Wight", "Plymouth", "FitzRoy", "Fastnet", "Rockall", "Malin"],
 ["Solent", "Tees", "Mersey", "Clyde", "Orkney"])
board("British freshwater fish", "Animals", "medium", ["fish", "fishing", "rivers"],
 ["Pike", "Perch", "Roach", "Carp", "Tench", "Bream", "Chub", "Barbel", "Rudd", "Dace", "Grayling", "Brown trout", "Gudgeon", "Zander", "Minnow"],
 ["Pollock", "Mackerel", "Plaice", "Whiting", "Dab"])
board("Makers of motorbikes", "Motoring", "medium", ["motorbikes", "brands"],
 ["Harley-Davidson", "Ducati", "Triumph", "Kawasaki", "Yamaha", "Honda", "Suzuki", "BMW", "KTM", "Norton", "Royal Enfield", "Aprilia", "Moto Guzzi", "MV Agusta", "Indian"],
 ["Ferrari", "Mazda", "Subaru", "Alfa Romeo", "Lotus"])
board("Breeds of cattle", "Animals", "hard", ["cattle", "farming", "breeds"],
 ["Aberdeen Angus", "Hereford", "Highland", "Jersey", "Guernsey", "Friesian", "Holstein", "Charolais", "Limousin", "Simmental", "Dexter", "Belted Galloway", "Longhorn", "Shorthorn", "Ayrshire"],
 ["Suffolk", "Texel", "Herdwick", "Swaledale", "Jacob"])
board("Breeds of chicken", "Animals", "hard", ["chickens", "poultry", "breeds"],
 ["Rhode Island Red", "Leghorn", "Orpington", "Light Sussex", "Plymouth Rock", "Wyandotte", "Silkie", "Brahma", "Marans", "Cochin", "Australorp", "Welsummer", "Dorking", "Araucana", "Faverolles"],
 ["Aylesbury", "Indian Runner", "Khaki Campbell", "Muscovy", "Mallard"])
board("Shades of blue", "Art and design", "medium", ["colours", "blue"],
 ["Navy", "Royal blue", "Sky blue", "Cobalt", "Azure", "Cerulean", "Ultramarine", "Sapphire", "Periwinkle", "Powder blue", "Duck egg", "Midnight blue", "Prussian blue", "Cornflower", "Electric blue"],
 ["Chartreuse", "Puce", "Vermilion", "Mauve", "Taupe"])
board("Characters from The Muppet Show", "Film and TV", "easy", ["The Muppets", "puppets"],
 ["Kermit", "Miss Piggy", "Fozzie Bear", "Gonzo", "Animal", "Rowlf", "Scooter", "Beaker", "Dr Bunsen Honeydew", "The Swedish Chef", "Statler", "Waldorf", "Sam Eagle", "Rizzo the Rat", "Pepe the King Prawn"],
 ["Big Bird", "Elmo", "Cookie Monster", "Oscar the Grouch", "Bert"])
board("US national parks", "World geography", "medium", ["USA", "national parks"],
 ["Yellowstone", "Yosemite", "Grand Canyon", "Zion", "Arches", "Everglades", "Glacier", "Acadia", "Bryce Canyon", "Death Valley", "Joshua Tree", "Olympic", "Redwood", "Great Smoky Mountains", "Denali"],
 ["Monument Valley", "Niagara Falls", "Mount Rushmore", "Lake Tahoe", "Hoover Dam"])
board("Films directed by Martin Scorsese", "Film", "medium", ["Martin Scorsese", "directors"],
 ["Mean Streets", "Taxi Driver", "Raging Bull", "The Color of Money", "Goodfellas", "Cape Fear", "Casino", "Gangs of New York", "The Aviator", "The Departed", "Shutter Island", "Hugo", "The Wolf of Wall Street", "The Irishman", "Killers of the Flower Moon"],
 ["The Godfather Part II", "Heat", "Once Upon a Time in America", "Donnie Brasco", "Scarface"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-13.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'boards written')
