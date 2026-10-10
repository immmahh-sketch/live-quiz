# Bank session 10 Oct 2026: 4 more general races -> bank/race-16.json. 20 rows each, target 10; wrong options are
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

race("which country uses this internet domain?", "Science and technology", "medium", ["internet", "countries"], [
 (".de", "Germany", ["Belgium", "Luxembourg", "Norway"]), (".ch", "Switzerland", ["Chile", "Chad", "Belgium"]),
 (".es", "Spain", ["Estonia", "El Salvador", "Ethiopia"]), (".nl", "the Netherlands", ["Nepal", "Nigeria", "Norway"]),
 (".at", "Austria", ["Australia", "Argentina", "Algeria"]), (".se", "Sweden", ["Senegal", "Serbia", "Seychelles"]),
 (".dk", "Denmark", ["Dominica", "Djibouti", "Norway"]), (".ie", "Ireland", ["Israel", "Iran", "Italy"]),
 (".pl", "Poland", ["Portugal", "the Philippines", "Peru"]), (".jp", "Japan", ["Jamaica", "Jordan", "Jersey"]),
 (".cn", "China", ["Canada", "Cameroon", "Colombia"]), (".in", "India", ["Indonesia", "Iran", "Israel"]),
 (".br", "Brazil", ["Britain", "Belarus", "Bahrain"]), (".mx", "Mexico", ["Malta", "Malaysia", "Morocco"]),
 (".za", "South Africa", ["Zambia", "Zimbabwe", "Tanzania"]), (".nz", "New Zealand", ["Niger", "Nauru", "Norway"]),
 (".tv", "Tuvalu", ["Tonga", "Taiwan", "Trinidad and Tobago"]), (".is", "Iceland", ["Israel", "Italy", "Iran"]),
 (".cz", "Czechia", ["Cyprus", "Cuba", "Slovakia"]), (".kr", "South Korea", ["North Korea", "Kenya", "Kyrgyzstan"])])

race("name the Simpsons character", "Film and TV", "medium", ["The Simpsons", "characters"], [
 ("Bart's best friend, with glasses", "Milhouse", ["Martin", "Rod", "Todd"]), ("The nuclear plant's evil owner", "Mr. Burns", ["Mayor Quimby", "Fat Tony", "Superintendent Chalmers"]),
 ("Mr. Burns's devoted assistant", "Smithers", ["Lenny", "Carl", "Gil"]), ("The Kwik-E-Mart's owner", "Apu", ["Sanjay", "Snake", "Cletus"]),
 ("The miserable barman", "Moe", ["Lenny", "Carl", "Gil"]), ("Homer's burping barfly friend", "Barney", ["Lenny", "Carl", "Duffman"]),
 ("The Simpsons' 'okily-dokily' neighbour", "Ned Flanders", ["Rev. Lovejoy", "Rod", "Todd"]), ("Lisa's saxophone-playing hero", "Bleeding Gums Murphy", ["Sideshow Mel", "Disco Stu", "Lou"]),
 ("The Scottish groundskeeper", "Willie", ["Snake", "Cletus", "Hans Moleman"]), ("The school's principal", "Skinner", ["Superintendent Chalmers", "Mayor Quimby", "Rev. Lovejoy"]),
 ("Bart's chain-smoking teacher", "Edna Krabappel", ["Ms. Hoover", "Patty", "Selma"]), ("The clown Bart idolises", "Krusty", ["Sideshow Mel", "Troy McClure", "Kent Brockman"]),
 ("Krusty's murderous ex-sidekick", "Sideshow Bob", ["Sideshow Mel", "Snake", "Fat Tony"]), ("The school bus driver", "Otto", ["Snake", "Cletus", "Disco Stu"]),
 ("Springfield's useless police chief", "Chief Wiggum", ["Lou", "Eddie", "Fat Tony"]), ("'I'm learnding!' — Wiggum's son", "Ralph", ["Martin", "Rod", "Todd"]),
 ("The bully who laughs 'Ha-ha!'", "Nelson", ["Jimbo", "Kearney", "Dolph"]), ("The Simpsons' greyhound", "Santa's Little Helper", ["Snowball II", "Laddie", "Mr. Teeny"]),
 ("'Hi, everybody!' — the dodgy doctor", "Dr. Nick", ["Dr. Hibbert", "Professor Frink", "Dr. Marvin Monroe"]), ("The ambulance-chasing lawyer", "Lionel Hutz", ["Troy McClure", "Kent Brockman", "Hans Moleman"])])

race("what kind of animal is this character?", "Film and TV", "medium", ["animals", "characters"], [
 ("Scooby-Doo", "Dog", ["Wolf", "Fox", "Bear"]), ("Garfield", "Cat", ["Fox", "Lynx", "Ocelot"]), ("Eeyore", "Donkey", ["Mule", "Horse", "Pony"]),
 ("Sonic", "Hedgehog", ["Porcupine", "Echidna", "Armadillo"]), ("Pumbaa", "Warthog", ["Wild boar", "Pig", "Tapir"]), ("Timon", "Meerkat", ["Mongoose", "Ferret", "Prairie dog"]),
 ("Rafiki", "Mandrill", ["Baboon", "Chimpanzee", "Orangutan"]), ("Zazu", "Hornbill", ["Toucan", "Parrot", "Pelican"]), ("Sid in Ice Age", "Sloth", ["Possum", "Koala", "Anteater"]),
 ("Marty in Madagascar", "Zebra", ["Horse", "Pony", "Okapi"]), ("Gloria in Madagascar", "Hippo", ["Rhino", "Elephant", "Manatee"]), ("Melman in Madagascar", "Giraffe", ["Llama", "Camel", "Ostrich"]),
 ("King Julien", "Lemur", ["Monkey", "Bushbaby", "Marmoset"]), ("Kanga", "Kangaroo", ["Wallaby", "Koala", "Wombat"]), ("Rocket in Guardians of the Galaxy", "Raccoon", ["Badger", "Ferret", "Otter"]),
 ("Shere Khan", "Tiger", ["Lion", "Leopard", "Jaguar"]), ("Feathers McGraw", "Penguin", ["Puffin", "Chicken", "Crow"]), ("Sebastian in The Little Mermaid", "Crab", ["Lobster", "Shrimp", "Prawn"]),
 ("Squidward", "Octopus", ["Squid", "Cuttlefish", "Jellyfish"]), ("Patrick in SpongeBob", "Starfish", ["Sea urchin", "Jellyfish", "Sponge"])])

race("name the ship or spaceship", "Film, TV and books", "medium", ["ships", "spaceships", "fiction"], [
 ("Jack Sparrow's ship", "Black Pearl", ["Interceptor", "Black Swan", "Silent Mary"]), ("Captain Ahab's whaler", "Pequod", ["Rachel", "Essex", "Bachelor"]),
 ("Captain Kirk's starship", "Enterprise", ["Voyager", "Defiant", "Excelsior"]), ("The ship in Firefly", "Serenity", ["Rocinante", "Bebop", "Normandy"]),
 ("Captain Hook's ship", "Jolly Roger", ["Walrus", "Black Hawk", "Sea Witch"]), ("Quint's boat in Jaws", "Orca", ["Andrea Gail", "Kingfisher", "Neptune"]),
 ("The ship in Treasure Island", "Hispaniola", ["Walrus", "Endeavour", "Victory"]), ("Caspian's ship in Narnia", "Dawn Treader", ["Splendour Hyaline", "Black Swan", "Silver Arrow"]),
 ("Han Solo's ship", "Millennium Falcon", ["Slave I", "Tantive IV", "Ghost"]), ("The stolen ship in The Hitchhiker's Guide", "Heart of Gold", ["Red Dwarf", "Starbug", "Planet Express Ship"]),
 ("The Doctor's time machine", "TARDIS", ["Moya", "Bebop", "Rocinante"]), ("The ship in Alien", "Nostromo", ["Sulaco", "Covenant", "Prometheus"]),
 ("Captain Nemo's submarine", "Nautilus", ["Seaview", "Proteus", "Albatross"]), ("The battlestar in Battlestar Galactica", "Galactica", ["Pegasus", "Andromeda", "Normandy"]),
 ("The ship in Blake's 7", "Liberator", ["Moya", "Andromeda", "Normandy"]), ("The Walkers' dinghy in Swallows and Amazons", "Swallow", ["Amazon", "Kingfisher", "Walrus"]),
 ("The ship in 2001: A Space Odyssey", "Discovery One", ["Leonov", "Event Horizon", "Sulaco"]), ("Davy Jones's ship", "Flying Dutchman", ["Silent Mary", "Interceptor", "Endeavour"]),
 ("Sean Connery's Soviet submarine", "Red October", ["Dallas", "Seaview", "Proteus"]), ("Blackbeard's ship", "Queen Anne's Revenge", ["Silent Mary", "Interceptor", "Black Swan"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-16.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
