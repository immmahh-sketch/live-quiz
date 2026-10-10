# Bank session 10 Oct 2026: 4 more general races -> bank/race-20.json. 20 rows each, target 10; wrong options are
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

race("name the famous fox or wolf", "Film, TV and books", "medium", ["foxes", "wolves", "characters"], [
 ("Roald Dahl's fantastic fox", "Mr. Fox", ["Boggis", "Bunce", "Bean"]), ("'Boom! Boom!' — the puppet fox", "Basil Brush", ["Sooty", "Gordon the Gopher", "Spit the Dog"]),
 ("The fox who tricks Chicken Licken", "Foxy Loxy", ["Turkey Lurkey", "Goosey Loosey", "Ducky Lucky"]), ("The trickster fox of medieval fables", "Reynard", ["Isengrim", "Chanticleer", "Bruin"]),
 ("The fox in The Fox and the Hound", "Tod", ["Copper", "Big Mama", "Amos Slade"]), ("Zootopia's con-artist fox", "Nick Wilde", ["Judy Hopps", "Finnick", "Bellwether"]),
 ("'Swiper, no swiping!'", "Swiper", ["Boots", "Backpack", "Map"]), ("Sonic's two-tailed friend", "Tails", ["Knuckles", "Shadow", "Amy"]),
 ("The fox who robs the rich in Disney's version", "Robin Hood", ["Little John", "Friar Tuck", "Prince John"]), ("Beatrix Potter's fox", "Mr. Tod", ["Tommy Brock", "Mr. Jeremy Fisher", "Benjamin Bunny"]),
 ("The wolf who huffs and puffs", "The Big Bad Wolf", ["Isengrim", "Wolfgang", "Lupo"]), ("The Jungle Book's wolf-pack leader", "Akela", ["Shere Khan", "Baloo", "Bagheera"]),
 ("Mowgli's wolf mother", "Raksha", ["Shere Khan", "Bagheera", "Kaa"]), ("Jack London's wolfdog", "White Fang", ["Buck", "Kazan", "Lassie"]),
 ("Jon Snow's direwolf", "Ghost", ["Nymeria", "Summer", "Grey Wind"]), ("The giant wolf of Norse myth", "Fenrir", ["Sleipnir", "Jörmungandr", "Ratatoskr"]),
 ("The sly fox who leads Pinocchio astray", "Honest John", ["Gideon", "Stromboli", "Jiminy Cricket"]), ("Mr. Fox's wife in the Wes Anderson film", "Felicity", ["Ash", "Kristofferson", "Kylie"]),
 ("The White Witch's wolf captain in Narnia", "Maugrim", ["Ginarrbrik", "Tumnus", "Aslan"]), ("'What's the time, …?'", "Mr. Wolf", ["Mr. Bear", "Mr. Tiger", "Mr. Owl"])])

race("what's this TV detective's first name?", "Film and TV", "hard", ["detectives", "names"], [
 ("Morse", "Endeavour", ["Edmund", "Ernest", "Edward"]), ("Poirot", "Hercule", ["Hector", "Henri", "Hugo"]), ("Frost", "Jack", ["Joe", "Jake", "Jerry"]),
 ("Taggart", "Jim", ["Joe", "Jock", "Jake"]), ("Rebus", "John", ["James", "Jamie", "Ian"]), ("Wallander", "Kurt", ["Karl", "Klaus", "Lars"]),
 ("Lewis", "Robbie", ["Ronnie", "Richie", "Roger"]), ("Barnaby", "Tom", ["Tim", "Ted", "Tony"]), ("Maigret", "Jules", ["Jean", "Julien", "Marcel"]),
 ("Wycliffe", "Charles", ["Christopher", "Colin", "Clive"]), ("Dalziel", "Andy", ["Alfie", "Archie", "Arnold"]), ("Pascoe", "Peter", ["Paul", "Patrick", "Philip"]),
 ("Banks", "Alan", ["Adrian", "Adam", "Albert"]), ("Shoestring", "Eddie", ["Ernie", "Eric", "Ellis"]), ("Spender", "Freddie", ["Frankie", "Felix", "Francis"]),
 ("Kojak", "Theo", ["Tony", "Terry", "Teddy"]), ("Magnum", "Thomas", ["Tim", "Terry", "Ted"]), ("Clouseau", "Jacques", ["Jean", "Henri", "Pierre"]),
 ("Miss Marple", "Jane", ["Joan", "Jennifer", "Julia"]), ("Strike", "Cormoran", ["Corin", "Conrad", "Cameron"])])

race("which game is this from?", "Games and toys", "medium", ["board games", "games"], [
 ("Colonel Mustard in the library", "Cluedo", ["Murder in the Dark", "Mystery Mansion", "Scotland Yard"]), ("Free Parking", "Monopoly", ["The Game of Life", "Ticket to Ride", "Cashflow"]),
 ("Triple word score", "Scrabble", ["Boggle", "Bananagrams", "Upwords"]), ("Collecting pie wedges", "Trivial Pursuit", ["Cranium", "Articulate", "Taboo"]),
 ("Castling", "Chess", ["Stratego", "Othello", "Halma"]), ("Bearing off", "Backgammon", ["Ludo", "Sorry!", "Frustration"]),
 ("Invading Kamchatka", "Risk", ["Diplomacy", "Axis & Allies", "Stratego"]), ("The crazy contraption that catches mice", "Mouse Trap", ["Pop-up Pirate", "Perfection", "Downfall"]),
 ("'Does your person wear glasses?'", "Guess Who?", ["Taboo", "Charades", "Headbanz"]), ("'You sank my…'", "Battleships", ["Stratego", "Connect 4", "Downfall"]),
 ("Cavity Sam's funny bone", "Operation", ["Pop-up Pirate", "Perfection", "Jenga"]), ("'All play!' while you draw", "Pictionary", ["Charades", "Articulate", "Taboo"]),
 ("Getting crowned when you reach the far side", "Draughts", ["Halma", "Othello", "Nine Men's Morris"]), ("Black and white stones fighting for territory", "Go", ["Othello", "Halma", "Nine Men's Morris"]),
 ("Cracking a secret code of coloured pegs", "Mastermind", ["Yahtzee", "Boggle", "Perfection"]), ("'Right hand, red!'", "Twister", ["Charades", "Jenga", "Hopscotch"]),
 ("Pulling out straws without dropping the marbles", "KerPlunk", ["Jenga", "Pop-up Pirate", "Downfall"]), ("Loading up a kicking mule", "Buckaroo!", ["Pop-up Pirate", "Jenga", "Hungry Hippos"]),
 ("Trading sheep for wood", "Catan", ["Carcassonne", "Ticket to Ride", "Agricola"]), ("Shouting its name when you're down to one card", "Uno", ["Snap", "Crazy Eights", "Happy Families"])])

race("name the famous monkey or ape", "Film, TV and books", "medium", ["monkeys", "apes", "characters"], [
 ("The curious monkey with the Man in the Yellow Hat", "Curious George", ["Hundley", "Charkie", "Jumpy Squirrel"]), ("The Jungle Book's swinging king", "King Louie", ["Baloo", "Bagheera", "Kaa"]),
 ("Aladdin's light-fingered monkey", "Abu", ["Iago", "Rajah", "Genie"]), ("Michael Jackson's pet chimp", "Bubbles", ["Muscles", "Louie", "Gabriel"]),
 ("Tarzan's chimp in the old films", "Cheeta", ["Jane", "Boy", "Tantor"]), ("Ross's capuchin in Friends", "Marcel", ["Hugsy", "Chick", "Duck"]),
 ("Nintendo's tie-wearing gorilla", "Donkey Kong", ["Cranky Kong", "Funky Kong", "Dixie Kong"]), ("Donkey Kong's little buddy in a red cap", "Diddy Kong", ["Cranky Kong", "Funky Kong", "Dixie Kong"]),
 ("The chimp who leads the apes in the modern Planet of the Apes films", "Caesar", ["Koba", "Maurice", "Rocket"]), ("The chimp scientist in the 1968 Planet of the Apes", "Cornelius", ["Zira", "Dr. Zaius", "General Ursus"]),
 ("The Powerpuff Girls' monkey villain", "Mojo Jojo", ["Him", "Fuzzy Lumpkins", "Professor Utonium"]), ("Barbossa's undead monkey", "Jack", ["Pintel", "Ragetti", "Barbossa"]),
 ("Dora the Explorer's monkey friend", "Boots", ["Swiper", "Backpack", "Map"]), ("The giant ape on the Empire State Building", "King Kong", ["Godzilla", "Mothra", "Gorgo"]),
 ("The giant gorilla raised in Africa by a girl called Jill", "Mighty Joe Young", ["Gorgo", "Grape Ape", "Magilla Gorilla"]), ("Krusty the Clown's monkey", "Mr. Teeny", ["Snowball II", "Santa's Little Helper", "Pinchy"]),
 ("The Lion King's wise mandrill", "Rafiki", ["Zazu", "Timon", "Pumbaa"]), ("The gorilla leader in Disney's Tarzan", "Kerchak", ["Kala", "Tantor", "Clayton"]),
 ("Tarzan's wisecracking gorilla friend", "Terk", ["Kala", "Tantor", "Clayton"]), ("The Monkey King of Chinese legend", "Sun Wukong", ["Zhu Bajie", "Sha Wujing", "Tripitaka"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-20.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
