# Bank session 10 Oct 2026: 4 more general races -> bank/race-32.json. 20 rows each, target 10; wrong options are
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

race("which city is this university in?", "World geography", "hard", ["universities", "cities"], [
 ("The Sorbonne", "Paris", ["Lyon", "Marseille", "Bordeaux"]), ("Heriot-Watt", "Edinburgh", ["Aberdeen", "Dundee", "Stirling"]),
 ("Strathclyde", "Glasgow", ["Aberdeen", "Dundee", "Paisley"]), ("Bocconi", "Milan", ["Turin", "Bologna", "Florence"]),
 ("Sapienza", "Rome", ["Florence", "Naples", "Bologna"]), ("Yale", "New Haven", ["Boston", "Hartford", "Providence"]),
 ("McGill", "Montreal", ["Toronto", "Quebec City", "Ottawa"]), ("Humboldt", "Berlin", ["Hamburg", "Munich", "Frankfurt"]),
 ("Complutense", "Madrid", ["Barcelona", "Seville", "Valencia"]), ("Charles University", "Prague", ["Brno", "Bratislava", "Vienna"]),
 ("Jagiellonian", "Kraków", ["Warsaw", "Gdańsk", "Wrocław"]), ("The Karolinska Institute", "Stockholm", ["Uppsala", "Gothenburg", "Oslo"]),
 ("Tsinghua", "Beijing", ["Hong Kong", "Nanjing", "Guangzhou"]), ("Fudan", "Shanghai", ["Hong Kong", "Nanjing", "Guangzhou"]),
 ("Northumbria", "Newcastle", ["Sunderland", "Durham", "Middlesbrough"]), ("Aston", "Birmingham", ["Coventry", "Leicester", "Wolverhampton"]),
 ("Johns Hopkins", "Baltimore", ["Annapolis", "Philadelphia", "Richmond"]), ("La Trobe", "Melbourne", ["Sydney", "Adelaide", "Brisbane"]),
 ("Erasmus University", "Rotterdam", ["Amsterdam", "Utrecht", "The Hague"]), ("Georgetown", "Washington, DC", ["Annapolis", "Richmond", "Philadelphia"])])

race("which animal is on this logo?", "Business", "medium", ["logos", "brands", "animals"], [
 ("Peugeot", "Lion", ["Tiger", "Leopard", "Wolf"]), ("Ferrari", "Horse", ["Zebra", "Goat", "Hare"]),
 ("Lamborghini", "Bull", ["Goat", "Buffalo", "Moose"]), ("Lacoste", "Crocodile", ["Lizard", "Frog", "Shark"]),
 ("Bacardi", "Bat", ["Hawk", "Parrot", "Moth"]), ("Twitter (before X)", "Bird", ["Butterfly", "Fish", "Bee"]),
 ("Linux", "Penguin", ["Seal", "Parrot", "Puffin"]), ("WWF", "Panda", ["Koala", "Gorilla", "Tiger"]),
 ("Playboy", "Rabbit", ["Fox", "Cat", "Mouse"]), ("Abarth", "Scorpion", ["Spider", "Wasp", "Lizard"]),
 ("Alfa Romeo", "Snake", ["Lizard", "Eagle", "Wolf"]), ("Saab", "Griffin", ["Eagle", "Dragon", "Phoenix"]),
 ("HMV", "Dog", ["Cat", "Fox", "Wolf"]), ("Kellogg's Corn Flakes", "Cockerel", ["Eagle", "Duck", "Hen"]),
 ("Jägermeister", "Stag", ["Moose", "Goat", "Ram"]), ("Duolingo", "Owl", ["Parrot", "Frog", "Toucan"]),
 ("Evernote", "Elephant", ["Rhino", "Hippo", "Mammoth"]), ("Toblerone (hidden in the mountain)", "Bear", ["Goat", "Eagle", "Ibex"]),
 ("Lufthansa", "Crane", ["Swan", "Eagle", "Stork"]), ("Qantas", "Kangaroo", ["Koala", "Emu", "Wallaby"])])

race("what's this fictional character's job?", "Film and TV", "medium", ["characters", "jobs"], [
 ("Hannibal Lecter", "Psychiatrist", ["Surgeon", "Dentist", "Pharmacist"]), ("Indiana Jones", "Archaeologist", ["Geologist", "Astronomer", "Pilot"]),
 ("Walter White", "Chemistry teacher", ["Pharmacist", "Accountant", "Lawyer"]), ("Homer Simpson", "Nuclear safety inspector", ["Electrician", "Plumber", "Mechanic"]),
 ("Fred Flintstone", "Quarry worker", ["Plumber", "Butcher", "Mechanic"]), ("Sweeney Todd", "Barber", ["Butcher", "Tailor", "Baker"]),
 ("Basil Fawlty", "Hotelier", ["Estate agent", "Butcher", "Taxi driver"]), ("Del Boy", "Market trader", ["Taxi driver", "Estate agent", "Plumber"]),
 ("Ross Geller", "Palaeontologist", ["Geologist", "Astronomer", "Historian"]), ("Jessica Fletcher", "Crime writer", ["Librarian", "Lawyer", "Florist"]),
 ("Clark Kent", "Reporter", ["Photographer", "Police officer", "Librarian"]), ("Ted Mosby", "Architect", ["Estate agent", "Plumber", "Photographer"]),
 ("Monica Geller", "Chef", ["Florist", "Librarian", "Photographer"]), ("Phoebe Buffay", "Masseuse", ["Florist", "Lifeguard", "Librarian"]),
 ("Captain Mainwaring", "Bank manager", ["Accountant", "Estate agent", "Butcher"]), ("Mrs Doubtfire", "Housekeeper", ["Librarian", "Florist", "Waiter"]),
 ("Rocky Balboa", "Boxer", ["Wrestler", "Jockey", "Police officer"]), ("James Herriot", "Vet", ["Zookeeper", "Farmer", "Pharmacist"]),
 ("Dexter Morgan", "Blood-spatter analyst", ["Photographer", "Pharmacist", "Lifeguard"]), ("Bob Cratchit", "Clerk", ["Butcher", "Tailor", "Baker"])])

race("which sport did this Briton win Olympic gold in?", "Sport", "medium", ["Olympics", "Team GB"], [
 ("Steve Redgrave", "Rowing", ["Canoe sprint", "Kayaking", "Water polo"]), ("Chris Hoy", "Track cycling", ["BMX", "Mountain biking", "Speed skating"]),
 ("Jessica Ennis-Hill", "Heptathlon", ["Hurdles", "Modern pentathlon", "Pole vault"]), ("Mo Farah", "Long-distance running", ["Sprinting", "Hurdles", "Race walking"]),
 ("Tom Daley", "Diving", ["Trampolining", "Water polo", "Synchronised swimming"]), ("Adam Peaty", "Swimming", ["Water polo", "Canoe sprint", "Kayaking"]),
 ("Ben Ainslie", "Sailing", ["Canoe sprint", "Kayaking", "Water polo"]), ("Max Whitlock", "Gymnastics", ["Weightlifting", "Climbing", "Judo"]),
 ("Nicola Adams", "Boxing", ["Judo", "Wrestling", "Karate"]), ("Charlotte Dujardin", "Dressage", ["Show jumping", "Eventing", "Modern pentathlon"]),
 ("Jade Jones", "Taekwondo", ["Judo", "Karate", "Fencing"]), ("Andy Murray", "Tennis", ["Badminton", "Squash", "Table tennis"]),
 ("Lizzy Yarnold", "Skeleton", ["Bobsleigh", "Luge", "Curling"]), ("Jayne Torvill and Christopher Dean", "Ice dance", ["Speed skating", "Curling", "Bobsleigh"]),
 ("Justin Rose", "Golf", ["Archery", "Curling", "Squash"]), ("Kate Richardson-Walsh", "Hockey", ["Handball", "Rugby sevens", "Water polo"]),
 ("Daley Thompson", "Decathlon", ["Pole vault", "Modern pentathlon", "Hurdles"]), ("Peter Wilson", "Shooting", ["Archery", "Fencing", "Curling"]),
 ("Alistair Brownlee", "Triathlon", ["Modern pentathlon", "Race walking", "Road cycling"]), ("Joe Clarke", "Canoe slalom", ["Canoe sprint", "Water polo", "Windsurfing"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-32.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
