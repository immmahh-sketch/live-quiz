# Bank session 10 Oct 2026: 2 more general races -> bank/race-102.json (famous cars, weapons and gadgets). 20 rows each, target 10; wrong options are
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

race("which film or show is this famous car from?", "Film", "medium", ["cars", "films", "TV"], [
 ("A DeLorean with a flux capacitor", "Back to the Future", ["Bill & Ted's Excellent Adventure", "Terminator 2", "The Fly"]),
 ("Ecto-1, a converted Cadillac ambulance", "Ghostbusters", ["Men in Black", "Gremlins", "Beetlejuice"]),
 ("KITT, a talking black Pontiac Trans Am", "Knight Rider", ["Airwolf", "The A-Team", "Street Hawk"]),
 ("The General Lee, an orange Dodge Charger with 01 on the doors", "The Dukes of Hazzard", ["The A-Team", "CHiPs", "Magnum, P.I."]),
 ("Herbie, a Volkswagen Beetle numbered 53", "The Love Bug", ["Christine", "Speed Racer", "Wacky Races"]),
 ("An Aston Martin DB5 with an ejector seat, first seen in 1964", "Goldfinger", ["Thunderball", "Moonraker", "Live and Let Die"]),
 ("The Mystery Machine", "Scooby-Doo", ["Wacky Races", "The Partridge Family", "Thunderbirds"]),
 ("A flying car named after the noise its engine makes", "Chitty Chitty Bang Bang", ["Mary Poppins", "Bedknobs and Broomsticks", "The Absent-Minded Professor"]),
 ("Greased Lightnin'", "Grease", ["Hairspray", "Dirty Dancing", "Footloose"]),
 ("Bumblebee, a yellow Camaro that's really a robot", "Transformers", ["Real Steel", "Pacific Rim", "RoboCop"]),
 ("Lightning McQueen, red race car number 95", "Cars", ["Turbo", "Planes", "Speed Racer"]),
 ("The Bluesmobile, an old police Dodge", "The Blues Brothers", ["Animal House", "Dumb and Dumber", "Police Academy"]),
 ("A flying turquoise Ford Anglia", "Harry Potter and the Chamber of Secrets", ["Harry Potter and the Prisoner of Azkaban", "Harry Potter and the Goblet of Fire", "Fantastic Beasts"]),
 ("Three Minis in red, white and blue", "The Italian Job", ["Mr. Bean", "The Persuaders!", "Bullitt"]),
 ("A yellow three-wheeled Reliant Regal van", "Only Fools and Horses", ["Heartbeat", "Last of the Summer Wine", "Steptoe and Son"]),
 ("A red Ford Gran Torino with a white stripe", "Starsky & Hutch", ["Miami Vice", "CHiPs", "The Rockford Files"]),
 ("A red Ferrari 'borrowed' from Cameron's dad", "Ferris Bueller's Day Off", ["Risky Business", "Rain Man", "Weird Science"]),
 ("The black V8 Interceptor", "Mad Max", ["Death Race 2000", "Drive", "Gone in 60 Seconds"]),
 ("A black and gold Pontiac Trans Am outrunning the sheriff", "Smokey and the Bandit", ["The Cannonball Run", "Convoy", "Bullitt"]),
 ("A white Lotus Esprit that turns into a submarine", "The Spy Who Loved Me", ["Moonraker", "For Your Eyes Only", "A View to a Kill"])])

race("whose weapon or gadget is this?", "Film", "easy", ["superheroes", "gadgets", "films"], [
 ("Mjölnir, the enchanted hammer", "Thor", ["Loki", "Odin", "Hercules"]),
 ("A round red, white and blue shield with a star", "Captain America", ["Falcon", "Black Widow", "The Winter Soldier"]),
 ("The golden Lasso of Truth", "Wonder Woman", ["Supergirl", "Catwoman", "Black Widow"]),
 ("Batarangs and a utility belt", "Batman", ["Green Arrow", "Daredevil", "The Flash"]),
 ("Wrist-mounted web-shooters", "Spider-Man", ["Daredevil", "The Wasp", "Black Cat"]),
 ("Adamantium claws", "Wolverine", ["Sabretooth", "Beast", "Colossus"]),
 ("A power ring fuelled by willpower", "Green Lantern", ["Green Arrow", "The Flash", "Cyborg"]),
 ("An arc reactor powering a suit of armour", "Iron Man", ["War Machine", "Vision", "Ultron"]),
 ("A golden trident", "Aquaman", ["The Flash", "Namor", "Cyborg"]),
 ("A bow and trick arrows, in the Avengers", "Hawkeye", ["Green Arrow", "Black Widow", "Falcon"]),
 ("The Infinity Gauntlet", "Thanos", ["Loki", "Ultron", "Red Skull"]),
 ("A ruby-quartz visor that holds back his optic blasts", "Cyclops", ["Storm", "Jean Grey", "Rogue"]),
 ("Cerebro, for tracking down mutants", "Professor X", ["Magneto", "Jean Grey", "Beast"]),
 ("A suit that shrinks him to the size of an insect", "Ant-Man", ["Falcon", "Vision", "Black Panther"]),
 ("The sonic screwdriver", "The Doctor", ["Doctor Strange", "Captain Jack Harkness", "Mr Spock"]),
 ("A red lightsaber, and a mask he has to breathe through", "Darth Vader", ["Luke Skywalker", "Boba Fett", "Han Solo"]),
 ("A cutlass and a compass that doesn't point north", "Captain Jack Sparrow", ["Captain Hook", "Long John Silver", "Captain Barbossa"]),
 ("A holly wand with a phoenix-feather core", "Harry Potter", ["Hermione Granger", "Ron Weasley", "Draco Malfoy"]),
 ("A golden gun, made from a pen, a lighter and a cigarette case", "Scaramanga", ["Goldfinger", "Jaws", "Dr. No"]),
 ("Proton packs for catching ghosts", "The Ghostbusters", ["The A-Team", "Men in Black", "The Goonies"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-102.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
