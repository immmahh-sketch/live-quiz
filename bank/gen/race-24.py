# Bank session 10 Oct 2026: 4 more general races -> bank/race-24.json. 20 rows each, target 10; wrong options are
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

race("name the famous reptile", "Film, TV and books", "medium", ["reptiles", "characters"], [
 ("The Jungle Book's hypnotic python", "Kaa", ["Hathi", "Bagheera", "Shere Khan"]), ("Prince John's snake adviser in Disney's Robin Hood", "Sir Hiss", ["Prince John", "Trigger", "Nutsy"]),
 ("Voldemort's snake", "Nagini", ["Aragog", "Fang", "Norbert"]), ("The clock-swallowing crocodile in Peter Pan", "Tick-Tock", ["Smee", "Starkey", "Nana"]),
 ("The chameleon sheriff of Dirt", "Rango", ["Beans", "Priscilla", "Roadkill"]), ("Rapunzel's chameleon", "Pascal", ["Maximus", "Flynn", "Mother Gothel"]),
 ("The King of the Monsters from Japan", "Godzilla", ["Mothra", "King Ghidorah", "Rodan"]), ("The Rugrats' favourite dinosaur", "Reptar", ["Spike", "Angelica", "Chuckie"]),
 ("Toy Story's nervous dinosaur", "Rex", ["Trixie", "Hamm", "Slinky"]), ("The Land Before Time's young hero", "Littlefoot", ["Cera", "Ducky", "Petrie"]),
 ("The wisecracking gecko of the video games", "Gex", ["Croc", "Spyro", "Sonic"]), ("The children's-book turtle who's afraid of the dark", "Franklin", ["Bear", "Snail", "Beaver"]),
 ("Finding Nemo's surfer-dude sea turtle", "Crush", ["Squirt", "Marlin", "Dory"]), ("Kung Fu Panda's wise old tortoise", "Master Oogway", ["Master Shifu", "Tai Lung", "Po"]),
 ("The Ninja Turtle in the blue mask", "Leonardo", ["Raphael", "Donatello", "Michelangelo"]), ("Mario's fire-breathing arch-enemy", "Bowser", ["Bowser Jr.", "Kamek", "Wario"]),
 ("Mario's green dinosaur steed", "Yoshi", ["Birdo", "Wario", "Toad"]), ("Rango's gun-slinging rattlesnake", "Rattlesnake Jake", ["Bad Bill", "Tortoise John", "Roadkill"]),
 ("The giant serpent in the Chamber of Secrets", "The Basilisk", ["Fluffy", "Aragog", "Norbert"]), ("The Norse serpent that circles the world", "Jörmungandr", ["Fenrir", "Sleipnir", "Níðhöggr"])])

race("which sport is this commentator famous for?", "Sport", "hard", ["commentators", "sports"], [
 ("Murray Walker", "Formula One", ["Speedway", "Rallying", "Powerboating"]), ("Peter Alliss", "Golf", ["Croquet", "Polo", "Archery"]),
 ("Dan Maskell", "Tennis", ["Badminton", "Squash", "Table tennis"]), ("John Motson", "Football", ["Hockey", "Netball", "Basketball"]),
 ("Bill McLaren", "Rugby union", ["American football", "Hockey", "Gaelic football"]), ("Sid Waddell", "Darts", ["Pool", "Archery", "Curling"]),
 ("Ted Lowe", "Snooker", ["Pool", "Croquet", "Curling"]), ("Richie Benaud", "Cricket", ["Baseball", "Hockey", "Polo"]),
 ("Peter O'Sullevan", "Horse racing", ["Greyhound racing", "Polo", "Speedway"]), ("David Coleman", "Athletics", ["Triathlon", "Gymnastics", "Diving"]),
 ("Eddie Waring", "Rugby league", ["American football", "Gaelic football", "Hockey"]), ("Harry Carpenter", "Boxing", ["Judo", "Fencing", "Weightlifting"]),
 ("Hugh Porter", "Cycling", ["Triathlon", "Speedway", "Motorcycling"]), ("David Vine (on Ski Sunday)", "Skiing", ["Curling", "Speed skating", "Bobsleigh"]),
 ("Dorian Williams", "Show jumping", ["Polo", "Greyhound racing", "Rodeo"]), ("Hamilton Bland", "Swimming", ["Water polo", "Canoeing", "Triathlon"]),
 ("David Rhys Jones", "Bowls", ["Croquet", "Curling", "Pétanque"]), ("Kent Walton", "Wrestling", ["Judo", "Sumo", "Fencing"]),
 ("Garry Herbert", "Rowing", ["Canoeing", "Sailing", "Kayaking"]), ("Robin Cousins", "Figure skating", ["Speed skating", "Ballroom dancing", "Curling"])])

race("name the leading lady in this Bond film", "James Bond", "hard", ["Bond", "characters"], [
 ("Dr. No", "Honey Ryder", ["Kissy Suzuki", "Paris Carver", "Lupe Lamora"]), ("From Russia with Love", "Tatiana Romanova", ["Xenia Onatopp", "Elektra King", "Magda"]),
 ("Thunderball", "Domino", ["Kissy Suzuki", "Bibi Dahl", "Paloma"]), ("On Her Majesty's Secret Service", "Tracy di Vicenzo", ["Solange", "Lucia Sciarra", "Miranda Frost"]),
 ("Diamonds Are Forever", "Tiffany Case", ["May Day", "Paris Carver", "Strawberry Fields"]), ("Live and Let Die", "Solitaire", ["Kissy Suzuki", "Magda", "Paloma"]),
 ("The Man with the Golden Gun", "Mary Goodnight", ["Bibi Dahl", "Lupe Lamora", "Magda"]), ("The Spy Who Loved Me", "Anya Amasova", ["Xenia Onatopp", "Elektra King", "Fatima Blush"]),
 ("For Your Eyes Only", "Melina Havelock", ["Lupe Lamora", "Paris Carver", "Solange"]), ("A View to a Kill", "Stacey Sutton", ["Magda", "Paloma", "Miranda Frost"]),
 ("The Living Daylights", "Kara Milovy", ["Lupe Lamora", "Kissy Suzuki", "Strawberry Fields"]), ("Licence to Kill", "Pam Bouvier", ["Paris Carver", "Magda", "Fatima Blush"]),
 ("GoldenEye", "Natalya Simonova", ["Elektra King", "Paris Carver", "Solange"]), ("Tomorrow Never Dies", "Wai Lin", ["Elektra King", "Miranda Frost", "Magda"]),
 ("The World Is Not Enough", "Christmas Jones", ["Miranda Frost", "Strawberry Fields", "Paloma"]), ("Die Another Day", "Jinx", ["Strawberry Fields", "Solange", "Lucia Sciarra"]),
 ("Casino Royale (2006)", "Vesper Lynd", ["Strawberry Fields", "Paloma", "Lucia Sciarra"]), ("Quantum of Solace", "Camille Montes", ["Paloma", "Lucia Sciarra", "Solange"]),
 ("Skyfall", "Sévérine", ["Paloma", "Lucia Sciarra", "Kissy Suzuki"]), ("Spectre", "Madeleine Swann", ["Paloma", "Strawberry Fields", "Solange"])])

race("what's this character's family name?", "Film, TV and books", "medium", ["families", "characters"], [
 ("Bart (Springfield)", "Simpson", ["Flanders", "Van Houten", "Wiggum"]), ("Wednesday", "Addams", ["Munster", "Frump", "Cleaver"]),
 ("Meg (Quahog)", "Griffin", ["Swanson", "Quagmire", "Brown"]), ("Pebbles (Bedrock)", "Flintstone", ["Rubble", "Slate", "Gravel"]),
 ("Elroy (Orbit City)", "Jetson", ["Spacely", "Cogswell", "Robinson"]), ("Ginny (Hogwarts)", "Weasley", ["Longbottom", "Lovegood", "Diggory"]),
 ("Draco (Hogwarts)", "Malfoy", ["Crabbe", "Goyle", "Lestrange"]), ("Dudley (Privet Drive)", "Dursley", ["Evans", "Figg", "Polkiss"]),
 ("Matilda", "Wormwood", ["Trunchbull", "Honey", "Phelps"]), ("Charlie (the golden ticket winner)", "Bucket", ["Wonka", "Gloop", "Salt"]),
 ("Wendy (who flies to Neverland)", "Darling", ["Hook", "Smee", "Mullins"]), ("Jane and Michael, Mary Poppins's charges", "Banks", ["Poppins", "Brill", "Lark"]),
 ("Lizzie in Pride and Prejudice", "Bennet", ["Darcy", "Bingley", "Wickham"]), ("Jo in Little Women", "March", ["Laurence", "Bhaer", "Brooke"]),
 ("Tina in Bob's Burgers", "Belcher", ["Fischoeder", "Pesto", "Frond"]), ("Haley in Modern Family", "Dunphy", ["Pritchett", "Tucker", "Delgado"]),
 ("Antony in The Royle Family", "Royle", ["Best", "Carroll", "Pritchard"]), ("Rodney in Only Fools and Horses", "Trotter", ["Boyce", "Pearce", "Driscoll"]),
 ("Lady Mary in Downton Abbey", "Crawley", ["Bates", "Carson", "Levinson"]), ("Dash in The Incredibles", "Parr", ["Best", "Deavor", "Mode"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-24.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
