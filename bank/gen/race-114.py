# Bank session 10 Oct 2026: 2 more general races -> bank/race-114.json (borrowed theme music, famous dogs' breeds). 20 rows each, target 10; wrong options are
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

race("which film or show used this music as its theme?", "TV", "hard", ["theme tunes", "music", "TV"], [
 ("'Barwick Green'", "The Archers", ["Emmerdale Farm", "Woman's Hour", "All Creatures Great and Small"]),
 ("'Johnny Todd', a Liverpool folk song", "Z-Cars", ["Softly, Softly", "Dixon of Dock Green", "Brookside"]),
 ("'Soul Limbo' by Booker T. & the M.G.'s", "Test Match Special", ["Grandstand", "Ski Sunday", "Question of Sport"]),
 ("'Approaching Menace'", "Mastermind", ["University Challenge", "Countdown", "The Krypton Factor"]),
 ("'Sailing By', just before midnight on Radio 4", "The Shipping Forecast", ["The Today Programme", "Desert Island Discs", "The News at Ten"]),
 ("'Devil's Galop'", "Dick Barton", ["Doctor Who", "The Saint", "Thunderbirds"]),
 ("'Gonna Fly Now'", "Rocky", ["Chariots of Fire", "Raging Bull", "The Karate Kid"]),
 ("Sousa's 'The Liberty Bell' march", "Monty Python's Flying Circus", ["Dad's Army", "The Goodies", "Fawlty Towers"]),
 ("'Galloping Home'", "Black Beauty", ["Follyfoot", "Champion the Wonder Horse", "Heartbeat"]),
 ("Fleetwood Mac's 'The Chain'", "Formula One on the BBC", ["Top Gear", "Match of the Day", "Grandstand"]),
 ("Gounod's 'Funeral March of a Marionette'", "Alfred Hitchcock Presents", ["The Twilight Zone", "The Addams Family", "Tales of the Unexpected"]),
 ("Strauss's 'Also sprach Zarathustra'", "2001: A Space Odyssey", ["Star Wars", "Close Encounters of the Third Kind", "Alien"]),
 ("Wagner's 'Ride of the Valkyries'", "Apocalypse Now", ["Platoon", "Full Metal Jacket", "The Deer Hunter"]),
 ("An anthem based on Handel's 'Zadok the Priest'", "The Champions League", ["The FA Cup", "The Europa League", "The World Cup"]),
 ("Pavarotti's 'Nessun Dorma'", "The BBC's Italia 90 coverage", ["Euro 96 coverage", "The 1966 World Cup film", "Match of the Day"]),
 ("Holst's 'Jupiter', reworked as 'World in Union'", "The Rugby World Cup", ["The Six Nations", "The Commonwealth Games", "The Olympics"]),
 ("Scott Joplin's 'The Entertainer'", "The Sting", ["Bonnie and Clyde", "Butch Cassidy and the Sundance Kid", "The Godfather"]),
 ("'Duelling Banjos'", "Deliverance", ["Easy Rider", "Bonnie and Clyde", "O Brother, Where Art Thou?"]),
 ("'Lara's Theme'", "Doctor Zhivago", ["Lawrence of Arabia", "Casablanca", "Ryan's Daughter"]),
 ("Survivor's 'Eye of the Tiger'", "Rocky III", ["Rocky IV", "Top Gun", "The Karate Kid"])])

race("what breed is this famous dog?", "Nature", "medium", ["dogs", "breeds", "films"], [
 ("Lassie", "Rough Collie", ["Bearded Collie", "Shetland Sheepdog", "Afghan Hound"]),
 ("Scooby-Doo", "Great Dane", ["Mastiff", "Irish Wolfhound", "Weimaraner"]),
 ("Snoopy", "Beagle", ["Basset Hound", "Bloodhound", "Springer Spaniel"]),
 ("Hooch, in 'Turner & Hooch'", "Dogue de Bordeaux", ["Mastiff", "Bulldog", "Boxer"]),
 ("Beethoven, the film dog", "St Bernard", ["Newfoundland", "Bernese Mountain Dog", "Old English Sheepdog"]),
 ("Pongo, in '101 Dalmatians'", "Dalmatian", ["Pointer", "English Setter", "Weimaraner"]),
 ("Toto, in 'The Wizard of Oz'", "Cairn Terrier", ["Yorkshire Terrier", "Westie", "Scottie"]),
 ("Brian, in 'Family Guy'", "Labrador", ["Poodle", "Flat-coated Retriever", "Whippet"]),
 ("Hachiko, the faithful dog of Tokyo", "Akita", ["Shiba Inu", "Husky", "Samoyed"]),
 ("Eddie, in 'Frasier'", "Jack Russell", ["Yorkshire Terrier", "Westie", "Chihuahua"]),
 ("Bull's-eye, in 'Oliver Twist'", "Bull Terrier", ["Staffordshire Bull Terrier", "Bulldog", "Boxer"]),
 ("Lady, in 'Lady and the Tramp'", "Cocker Spaniel", ["Springer Spaniel", "King Charles Spaniel", "Setter"]),
 ("Greyfriars Bobby", "Skye Terrier", ["Scottie", "Westie", "Yorkshire Terrier"]),
 ("Rin Tin Tin", "German Shepherd", ["Doberman", "Husky", "Rottweiler"]),
 ("Snowy, Tintin's dog", "Wire Fox Terrier", ["Westie", "Bichon Frise", "Scottie"]),
 ("Dug, in Pixar's 'Up'", "Golden Retriever", ["Labradoodle", "Setter", "Afghan Hound"]),
 ("Slinky Dog, in 'Toy Story'", "Dachshund", ["Basset Hound", "Corgi", "Whippet"]),
 ("Bluey", "Blue Heeler", ["Kelpie", "Husky", "Corgi"]),
 ("Fly, the sheepdog in 'Babe'", "Border Collie", ["Shetland Sheepdog", "Kelpie", "Old English Sheepdog"]),
 ("Bolt, the Disney superdog", "White Shepherd", ["Husky", "Samoyed", "Labradoodle"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-114.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
