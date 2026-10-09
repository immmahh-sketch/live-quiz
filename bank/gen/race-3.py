# Bank session 9 Oct 2026 (second pass): 4 more general races -> bank/race-3.json. 20 rows each, target 10; wrong
# options are the same kind of thing, never another row's right answer, and never also right for that row.
import json, os
R = []
def race(title, cat, diff, tags, rows):
    rights = {r[1] for r in rows}
    assert len(rows) == 20, (title, len(rows))
    assert len(rights) == 20, (title, 'duplicate right answers')
    for q, right, wrong in rows:
        assert len(wrong) == 3 and len(set(wrong)) == 3, (title, q)
        bad = [w for w in wrong if w in rights]
        assert not bad, (title, q, 'recycled', bad)
    R.append({"type": "race", "text": "The Race: " + title, "target": 10, "category": cat, "tags": tags, "difficulty": diff,
              "bank": [{"q": q, "right": right, "wrong": wrong} for q, right, wrong in rows]})

race("which animal makes this sound?", "Animals", "easy", ["animals", "sounds"], [
 ("Brays", "Donkey", ["Camel", "Llama", "Deer"]), ("Neighs", "Horse", ["Camel", "Llama", "Goat"]), ("Hoots", "Owl", ["Robin", "Magpie", "Swan"]),
 ("Croaks", "Frog", ["Lizard", "Newt", "Hamster"]), ("Hisses", "Snake", ["Robin", "Sheep", "Deer"]), ("Roars", "Lion", ["Hyena", "Fox", "Badger"]),
 ("Trumpets", "Elephant", ["Giraffe", "Hippo", "Rhino"]), ("Howls", "Wolf", ["Bear", "Badger", "Deer"]), ("Gobbles", "Turkey", ["Swan", "Pheasant", "Peacock"]),
 ("Quacks", "Duck", ["Swan", "Gull", "Pheasant"]), ("Clucks", "Hen", ["Parrot", "Swan", "Gull"]), ("Purrs", "Cat", ["Fox", "Badger", "Monkey"]),
 ("Squeaks", "Mouse", ["Badger", "Fox", "Sheep"]), ("Grunts and oinks", "Pig", ["Sheep", "Goat", "Swan"]), ("Moos", "Cow", ["Sheep", "Goat", "Llama"]),
 ("Barks", "Dog", ["Sheep", "Rabbit", "Goat"]), ("Caws", "Crow", ["Robin", "Swan", "Pheasant"]), ("Coos", "Pigeon", ["Magpie", "Gull", "Robin"]),
 ("Honks", "Goose", ["Robin", "Pheasant", "Parrot"]), ("Buzzes", "Bee", ["Butterfly", "Ladybird", "Spider"])])

race("complete the famous pair", "Entertainment", "easy", ["double acts", "pairs"], [
 ("Ant and …", "Dec", ["Dan", "Del", "Den"]), ("Morecambe and …", "Wise", ["Wilson", "Wood", "West"]), ("Laurel and …", "Hardy", ["Harvey", "Hart", "Hall"]),
 ("French and …", "Saunders", ["Sanders", "Simmons", "Stevens"]), ("Cannon and …", "Ball", ["Bell", "Bull", "Bowl"]), ("Little and …", "Large", ["Long", "Lord", "Lane"]),
 ("Mel and …", "Sue", ["Sal", "Sam", "Sid"]), ("Hale and …", "Pace", ["Price", "Parker", "Page"]), ("Smith and …", "Jones", ["James", "Johns", "Jenkins"]),
 ("Torvill and …", "Dean", ["Dawson", "Dale", "Dunn"]), ("Simon and …", "Garfunkel", ["Goldberg", "Grossman", "Gershwin"]), ("Sonny and …", "Cher", ["Cheryl", "Chaka", "Celine"]),
 ("Bill and …", "Ben", ["Bob", "Bert", "Bud"]), ("Tom and …", "Jerry", ["Jimmy", "Jack", "Joey"]), ("Wallace and …", "Gromit", ["Gnasher", "Gizmo", "Goofy"]),
 ("Chas and …", "Dave", ["Don", "Dick", "Doug"]), ("Pinky and …", "Perky", ["Porky", "Parky", "Pinkie"]), ("Zig and …", "Zag", ["Zog", "Zak", "Zip"]),
 ("Romeo and …", "Juliet", ["Julia", "Juliana", "Josephine"]), ("Rosencrantz and …", "Guildenstern", ["Goldstein", "Gildersleeve", "Guinevere"])])

race("finish the TV show title", "Film and TV", "easy", ["TV", "titles"], [
 ("Only Fools and …", "Horses", ["Donkeys", "Ponies", "Mules"]), ("Who Wants to Be a …?", "Millionaire", ["Billionaire", "Winner", "Champion"]),
 ("Keeping Up …", "Appearances", ["Standards", "Pretences", "Traditions"]), ("One Foot in the …", "Grave", ["Door", "Past", "Gutter"]),
 ("Men Behaving …", "Badly", ["Madly", "Sadly", "Oddly"]), ("Last of the Summer …", "Wine", ["Sun", "Holidays", "Rain"]),
 ("Are You Being …?", "Served", ["Seen", "Heard", "Seated"]), ("Strictly Come …", "Dancing", ["Singing", "Skating", "Baking"]),
 ("Ready Steady …", "Cook", ["Bake", "Go", "Eat"]), ("Have I Got … for You", "News", ["Gossip", "Questions", "Jokes"]),
 ("Never Mind the …", "Buzzcocks", ["Bluebells", "Basslines", "Beatles"]), ("Bargain …", "Hunt", ["Trail", "Basement", "Bin"]),
 ("A Question of …", "Sport", ["Taste", "Science", "Fame"]), ("Gavin & …", "Stacey", ["Tracey", "Stephanie", "Sharon"]),
 ("Peep …", "Show", ["Hole", "Toad", "Shop"]), ("Sex and the …", "City", ["Single Girl", "Suburbs", "Village"]),
 ("Desperate …", "Housewives", ["Housemates", "Husbands", "Measures"]), ("The Great British Bake …", "Off", ["Out", "Up", "On"]),
 ("Location, Location, …", "Location", ["Relocation", "Renovation", "Destination"]), ("Dad's …", "Army", ["Navy", "Garage", "Allotment"])])

race("which word goes in front of all three?", "Words and language", "medium", ["wordplay", "compound words"], [
 ("___ball, ___man, ___flake", "Snow", ["Corn", "Hail", "Ice"]), ("___work, ___place, ___man", "Fire", ["Home", "Life", "Gentle"]),
 ("___flower, ___glasses, ___shine", "Sun", ["Wall", "May", "Shoe"]), ("___bow, ___coat, ___drop", "Rain", ["Over", "Tear", "Cross"]),
 ("___ball, ___print, ___step", "Foot", ["Finger", "Base", "Side"]), ("___bag, ___shake, ___writing", "Hand", ["Milk", "Sand", "Tea"]),
 ("___case, ___mark, ___worm", "Book", ["Brief", "Glow", "Land"]), ("___fly, ___cup, ___milk", "Butter", ["Dragon", "Tea", "Coconut"]),
 ("___bird, ___board, ___mail", "Black", ["Song", "Card", "Key"]), ("___fall, ___melon, ___proof", "Water", ["Land", "Sound", "Fool"]),
 ("___brush, ___paste, ___ache", "Tooth", ["Hair", "Belly", "Paint"]), ("___ache, ___line, ___phone", "Head", ["Ear", "Dead", "Hair"]),
 ("___light, ___beam, ___walk", "Moon", ["Cat", "Search", "Laser"]), ("___fish, ___light, ___dust", "Star", ["Gold", "Jelly", "Sword"]),
 ("___shell, ___side, ___horse", "Sea", ["Egg", "Hobby", "Country"]), ("___pack, ___fire, ___bone", "Back", ["Wolf", "Wish", "Camp"]),
 ("___light, ___dream, ___break", "Day", ["Lime", "Night", "Jail"]), ("___bell, ___mat, ___step", "Door", ["Blue", "Bath", "Goose"]),
 ("___port, ___plane, ___line", "Air", ["Sky", "Pass", "Out"]), ("___brow, ___lash, ___sight", "Eye", ["High", "Whip", "Fore"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-3.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
