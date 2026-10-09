# Bank session 9 Oct 2026 (second pass): 15 new Wipeout boards -> bank/wipeout-4.json. 15 right answers (certain,
# fairly well known) and 5 wrong ones (plausible, definitely wrong) each; none of these subjects is already a board.
# Decoys must need knowledge of the subject: a review rejected a Corrie board whose wrong names came from other soaps.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Fruits that grow on trees", "Food and drink", "easy", ["fruit"],
 ["Apple", "Pear", "Plum", "Cherry", "Orange", "Lemon", "Lime", "Peach", "Apricot", "Mango", "Fig", "Olive", "Avocado", "Coconut", "Date"],
 ["Strawberry", "Raspberry", "Grape", "Pineapple", "Watermelon"])
board("Vegetables that grow underground", "Food and drink", "easy", ["vegetables"],
 ["Carrot", "Potato", "Parsnip", "Turnip", "Swede", "Beetroot", "Radish", "Onion", "Garlic", "Ginger", "Sweet potato", "Celeriac", "Horseradish", "Yam", "Shallot"],
 ["Broccoli", "Cauliflower", "Cabbage", "Peas", "Courgette"])
board("Genuine Coronation Street characters (watch for mixed-up names)", "Film and TV", "easy", ["soaps", "Coronation Street"],
 ["Ken Barlow", "Gail Platt", "Steve McDonald", "Roy Cropper", "Hilda Ogden", "Bet Lynch", "Jack Duckworth", "Vera Duckworth", "Audrey Roberts", "Tyrone Dobbs", "Kevin Webster", "Sally Webster", "Deirdre Barlow", "Norris Cole", "Rita Sullivan"],
 ["Hilda Barlow", "Norris Webster", "Rita Duckworth", "Ken Platt", "Bet Ogden"])
board("Liverpool landmarks", "Places", "medium", ["Liverpool", "landmarks"],
 ["Albert Dock", "Royal Liver Building", "The Cavern Club", "Anfield", "Goodison Park", "Penny Lane", "Strawberry Field", "Mathew Street", "Lime Street station", "St George's Hall", "Pier Head", "Liverpool Cathedral", "Metropolitan Cathedral", "Walker Art Gallery", "Speke Hall"],
 ["Old Trafford", "Tyne Bridge", "Etihad Stadium", "Blackpool Tower", "Angel of the North"])
board("Sights in Newcastle and Gateshead", "The North East of England", "medium", ["Newcastle", "Gateshead", "landmarks"],
 ["Grey's Monument", "St James' Park", "Baltic Centre", "The Glasshouse (formerly Sage Gateshead)", "The Quayside", "Laing Art Gallery", "Castle Keep", "Black Gate", "Grainger Market", "Theatre Royal", "Eldon Square", "Central Station", "Jesmond Dene", "Angel of the North", "MetroCentre"],
 ["Penshaw Monument", "Roker Pier", "Durham Cathedral", "Beamish Museum", "Bamburgh Castle"])
board("Words that make a new word when you add 'side' to the end", "Words and language", "medium", ["wordplay"],
 ["Sea", "Country", "Road", "Fire", "Bed", "Way", "Out", "In", "Up", "Down", "Back", "Lake", "River", "Hill", "Ring"],
 ["Cat", "Tree", "Pen", "Car", "Cup"])
board("Words that make a new word when you add 'ship' to the end", "Words and language", "medium", ["wordplay"],
 ["Friend", "Member", "Relation", "Owner", "Leader", "Partner", "Champion", "Citizen", "Hard", "Court", "Battle", "Space", "War", "Apprentice", "Scholar"],
 ["Happy", "Water", "Brother", "Cup", "Tree"])
board("Famous women called Mary: which surnames?", "People", "medium", ["famous names"],
 ["Berry", "Shelley", "Seacole", "Whitehouse", "Beard", "Portas", "Quant", "Anning", "Pickford", "Wollstonecraft", "Earps", "Peters", "Hopkin", "J. Blige", "Archer"],
 ["Nightingale", "Pankhurst", "Curie", "Austen", "Brontë"])
board("Italian cheeses", "Food and drink", "medium", ["cheese", "Italian food"],
 ["Mozzarella", "Parmesan", "Gorgonzola", "Ricotta", "Mascarpone", "Pecorino", "Provolone", "Burrata", "Taleggio", "Fontina", "Asiago", "Dolcelatte", "Grana Padano", "Bel Paese", "Scamorza"],
 ["Feta", "Halloumi", "Manchego", "Gouda", "Brie"])
board("Characters in The Simpsons", "Film and TV", "easy", ["cartoons", "The Simpsons"],
 ["Homer", "Marge", "Bart", "Lisa", "Maggie", "Ned Flanders", "Mr Burns", "Smithers", "Moe", "Barney", "Krusty the Clown", "Apu", "Milhouse", "Chief Wiggum", "Sideshow Bob"],
 ["Bart Flanders", "Marge Wiggum", "Monty Simpson", "Ned Gumble", "Apu Smithers"])
board("Towns and cities on the River Thames", "UK geography", "medium", ["rivers", "places"],
 ["Oxford", "Reading", "Henley-on-Thames", "Marlow", "Maidenhead", "Windsor", "Eton", "Staines", "Kingston upon Thames", "Richmond", "Abingdon", "Wallingford", "Lechlade", "Gravesend", "Southend-on-Sea"],
 ["Cambridge", "Bath", "Stratford-upon-Avon", "York", "Bristol"])
board("Breeds of cat", "Animals", "easy", ["cats", "pets"],
 ["Siamese", "Persian", "Maine Coon", "Bengal", "Ragdoll", "Sphynx", "British Shorthair", "Burmese", "Abyssinian", "Russian Blue", "Scottish Fold", "Birman", "Manx", "Siberian", "Devon Rex"],
 ["Welsh Shorthair", "Irish Blue", "Norwegian Rex", "Spanish Sphynx", "Persian Fold"])
board("Characters in the Toy Story films", "Film", "easy", ["Pixar", "Toy Story"],
 ["Woody", "Buzz Lightyear", "Jessie", "Mr Potato Head", "Rex", "Hamm", "Slinky Dog", "Bo Peep", "Bullseye", "Lotso", "Forky", "Andy", "Sid", "Zurg", "Stinky Pete"],
 ["Action Man", "Stretch Armstrong", "Teddy Ruxpin", "Cabbage Patch Kid", "Sindy"])
board("Gemstones", "Science", "easy", ["gems", "minerals"],
 ["Diamond", "Ruby", "Emerald", "Sapphire", "Opal", "Amethyst", "Topaz", "Garnet", "Jade", "Turquoise", "Aquamarine", "Peridot", "Onyx", "Tourmaline", "Lapis lazuli"],
 ["Granite", "Marble", "Slate", "Chalk", "Flint"])
board("Animals with hooves", "Animals", "medium", ["animals"],
 ["Horse", "Cow", "Pig", "Sheep", "Goat", "Deer", "Zebra", "Giraffe", "Rhinoceros", "Moose", "Donkey", "Antelope", "Bison", "Reindeer", "Wild boar"],
 ["Elephant", "Kangaroo", "Dog", "Bear", "Lion"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-4.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'boards written')
