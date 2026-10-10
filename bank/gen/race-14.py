# Bank session 10 Oct 2026: 4 more general races -> bank/race-14.json. 20 rows each, target 10; wrong options are
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

race("name the famous elephant (or mammoth)", "Film, TV and books", "medium", ["elephants", "characters"], [
 ("Disney's flying elephant", "Dumbo", ["Casey Junior", "Timothy", "Mr. Stork"]), ("The elephant king in a green suit", "Babar", ["Arthur", "Zephir", "Cornelius"]),
 ("Babar's queen", "Celeste", ["Arthur", "Cornelius", "Isabelle"]), ("Dumbo's mum", "Mrs. Jumbo", ["Prissy", "Giddy", "Catty"]),
 ("The London Zoo elephant sold to Barnum's circus", "Jumbo", ["Alice", "Tom Thumb", "Toby"]), ("The Seuss elephant who hears a Who", "Horton", ["Mayzie", "Vlad", "Sour Kangaroo"]),
 ("The patchwork elephant", "Elmer", ["Wilbur", "Eglantine", "Rose"]), ("The Jungle Book's marching elephant", "Colonel Hathi", ["Baloo", "Bagheera", "Kaa"]),
 ("Tarzan's nervous elephant friend", "Tantor", ["Terk", "Kerchak", "Kala"]), ("Bart Simpson's elephant", "Stampy", ["Santa's Little Helper", "Snowball II", "Mojo"]),
 ("Piggie's best friend in the Mo Willems books", "Gerald", ["Pigeon", "Knuffle Bunny", "Trixie"]), ("The baby elephant Pokémon", "Phanpy", ["Donphan", "Snorlax", "Teddiursa"]),
 ("The elephant-headed Hindu god", "Ganesh", ["Hanuman", "Shiva", "Vishnu"]), ("Hannibal's bravest war elephant", "Surus", ["Bucephalus", "Hasdrubal", "Barca"]),
 ("Ice Age's woolly mammoth", "Manny", ["Diego", "Sid", "Scrat"]), ("She packed her trunk and said goodbye to the circus", "Nellie", ["Ella", "Rosie", "Daisy"]),
 ("Manny's mate in Ice Age 2", "Ellie", ["Peaches", "Shira", "Granny"]), ("Big Bird's woolly friend on Sesame Street", "Mr. Snuffleupagus", ["Oscar", "Grover", "Elmo"]),
 ("The elephant-like creature Pooh is scared of", "Heffalump", ["Woozle", "Jagular", "Backson"]), ("Kipling's curious young elephant who gets a long trunk", "The Elephant's Child", ["The Cat That Walked by Himself", "Rikki-Tikki-Tavi", "The Kolokolo Bird"])])

race("in which country is this festival held?", "Faiths and festivals", "medium", ["festivals", "countries"], [
 ("Oktoberfest", "Germany", ["Austria", "Switzerland", "Belgium"]), ("The Rio Carnival", "Brazil", ["Argentina", "Colombia", "Portugal"]),
 ("La Tomatina", "Spain", ["Portugal", "Argentina", "Greece"]), ("Holi, the festival of colours", "India", ["Sri Lanka", "Malaysia", "Indonesia"]),
 ("Songkran, the water festival", "Thailand", ["Vietnam", "Malaysia", "Indonesia"]), ("The Day of the Dead", "Mexico", ["Colombia", "Cuba", "Argentina"]),
 ("Hogmanay", "Scotland", ["Northern Ireland", "the Isle of Man", "Norway"]), ("The National Eisteddfod", "Wales", ["Northern Ireland", "the Isle of Man", "Iceland"]),
 ("Mardi Gras in New Orleans", "the USA", ["Canada", "Cuba", "Jamaica"]), ("The Sapporo Snow Festival", "Japan", ["South Korea", "China", "Taiwan"]),
 ("The Venice Carnival", "Italy", ["Croatia", "Greece", "Austria"]), ("Glastonbury", "England", ["Northern Ireland", "the Isle of Man", "Belgium"]),
 ("Roskilde", "Denmark", ["Norway", "Finland", "Iceland"]), ("Sziget", "Hungary", ["Czechia", "Romania", "Croatia"]),
 ("Bastille Day", "France", ["Belgium", "Switzerland", "Canada"]), ("King's Day, when everyone wears orange", "the Netherlands", ["Belgium", "Norway", "Luxembourg"]),
 ("Puck Fair, where a goat is crowned king", "Ireland", ["Northern Ireland", "the Isle of Man", "Iceland"]), ("Inti Raymi, the Inca festival of the sun", "Peru", ["Bolivia", "Ecuador", "Chile"]),
 ("Midsommar, with dancing round the maypole", "Sweden", ["Norway", "Finland", "Iceland"]), ("Junkanoo", "the Bahamas", ["Jamaica", "Cuba", "Trinidad and Tobago"])])

race("finish the band's name", "Music", "easy", ["bands", "names"], [
 ("Arctic …", "Monkeys", ["Foxes", "Lions", "Penguins"]), ("Duran …", "Duran", ["Durango", "Duo", "Duncan"]), ("Simply …", "Red", ["Blue", "Green", "Pink"]),
 ("Spandau …", "Ballet", ["Opera", "Waltz", "Theatre"]), ("Fleetwood …", "Mac", ["Mick", "Max", "Mag"]), ("Pet Shop …", "Boys", ["Girls", "Dogs", "Lads"]),
 ("Dire …", "Straits", ["Streets", "Waters", "Strikes"]), ("Kings of …", "Leon", ["Lyon", "Leeds", "Leo"]), ("Florence + the …", "Machine", ["Machines", "Engine", "Mechanics"]),
 ("Red Hot Chili …", "Peppers", ["Pickles", "Beans", "Poppers"]), ("Guns N' …", "Roses", ["Rosie", "Rockets", "Riots"]), ("Iron …", "Maiden", ["Maidens", "Lady", "Man"]),
 ("Def …", "Leppard", ["Leopard", "Lepper", "Lizard"]), ("Pink …", "Floyd", ["Lloyd", "Flamingo", "Fluid"]), ("Tears for …", "Fears", ["Years", "Fools", "Feelings"]),
 ("Culture …", "Club", ["Shock", "Clash", "Vulture"]), ("Depeche …", "Mode", ["Mood", "Code", "Model"]), ("Led …", "Zeppelin", ["Balloon", "Zebra", "Zipper"]),
 ("Manic Street …", "Preachers", ["Teachers", "Prophets", "Sweepers"]), ("Frankie Goes to …", "Hollywood", ["Hollyoaks", "Holloway", "Holland"])])

race("which animal does this word describe?", "Words and language", "medium", ["animals", "adjectives"], [
 ("Feline", "Cat", ["Rabbit", "Ferret", "Otter"]), ("Canine", "Dog", ["Badger", "Otter", "Weasel"]), ("Bovine", "Cow", ["Camel", "Llama", "Hippo"]),
 ("Equine", "Horse", ["Camel", "Llama", "Giraffe"]), ("Ovine", "Sheep", ["Alpaca", "Llama", "Rabbit"]), ("Porcine", "Pig", ["Badger", "Hippo", "Hedgehog"]),
 ("Lupine", "Wolf", ["Hare", "Lynx", "Badger"]), ("Vulpine", "Fox", ["Weasel", "Badger", "Lynx"]), ("Ursine", "Bear", ["Badger", "Otter", "Beaver"]),
 ("Leonine", "Lion", ["Tiger", "Leopard", "Panther"]), ("Aquiline", "Eagle", ["Owl", "Hawk", "Vulture"]), ("Corvine", "Crow", ["Pigeon", "Sparrow", "Owl"]),
 ("Anserine", "Goose", ["Swan", "Duck", "Hen"]), ("Piscine", "Fish", ["Whale", "Dolphin", "Seal"]), ("Serpentine", "Snake", ["Lizard", "Worm", "Eel"]),
 ("Simian", "Ape or monkey", ["Lemur", "Sloth", "Bat"]), ("Cervine", "Deer", ["Antelope", "Gazelle", "Llama"]), ("Murine", "Mouse", ["Mole", "Shrew", "Hamster"]),
 ("Caprine", "Goat", ["Antelope", "Alpaca", "Llama"]), ("Apian", "Bee", ["Wasp", "Ant", "Hornet"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-14.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
