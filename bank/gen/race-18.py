# Bank session 10 Oct 2026: 4 more general races -> bank/race-18.json. 20 rows each, target 10; wrong options are
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

race("which building has this nickname?", "Famous landmarks", "hard", ["buildings", "nicknames"], [
 ("The Gherkin", "30 St Mary Axe", ["The Shard", "One Canada Square", "Tower 42"]), ("The Walkie-Talkie", "20 Fenchurch Street", ["The Shard", "Tower 42", "One Canada Square"]),
 ("The Cheesegrater", "The Leadenhall Building", ["The Shard", "Tower 42", "One Canada Square"]), ("The Scalpel", "52 Lime Street", ["Tower 42", "One Canada Square", "The Shard"]),
 ("The Wobbly Bridge", "The Millennium Bridge, London", ["Tower Bridge", "Hungerford Bridge", "Waterloo Bridge"]), ("The Egg (or the 'glass testicle')", "London's old City Hall", ["Somerset House", "Mansion House", "County Hall"]),
 ("The Wedding Cake", "Rome's Victor Emmanuel II Monument", ["The Colosseum", "The Pantheon", "St Peter's"]), ("The Bird's Nest", "Beijing's National Stadium", ["The Great Hall of the People", "The Forbidden City", "Tiananmen Gate"]),
 ("The Water Cube", "Beijing's National Aquatics Centre", ["The Great Hall of the People", "The Forbidden City", "Tiananmen Gate"]), ("The Iron Lady", "The Eiffel Tower", ["The Statue of Liberty", "Blackpool Tower", "The Atomium"]),
 ("Paddy's Wigwam", "Liverpool's Catholic cathedral", ["Liverpool's Anglican cathedral", "St George's Hall", "The Royal Liver Building"]), ("The Blinking Eye", "The Gateshead Millennium Bridge", ["The Tyne Bridge", "The Swing Bridge", "The Sage"]),
 ("The Coathanger", "Sydney Harbour Bridge", ["Sydney Opera House", "The Golden Gate Bridge", "Brooklyn Bridge"]), ("The Armadillo", "Glasgow's Clyde Auditorium", ["The SSE Hydro", "The Riverside Museum", "Kelvingrove"]),
 ("The Squinty Bridge", "Glasgow's Clyde Arc", ["The Kingston Bridge", "The Squiggly Bridge", "The Bells Bridge"]), ("The Flatiron", "New York's Fuller Building", ["The Chrysler Building", "The Empire State Building", "The Woolworth Building"]),
 ("The Dome", "The O2", ["Wembley Arena", "The Royal Albert Hall", "The Barbican"]), ("The Old Lady of Threadneedle Street", "The Bank of England", ["The Royal Exchange", "The Stock Exchange", "Lloyd's of London"]),
 ("Ally Pally", "Alexandra Palace", ["Crystal Palace", "Hampton Court", "The Albert Hall"]), ("The real 'Big Ben'", "The Great Bell", ["The Elizabeth Tower", "The clock face", "The Victoria Tower"])])

race("which country does this dance come from?", "Music", "medium", ["dance", "countries"], [
 ("Flamenco", "Spain", ["Portugal", "Mexico", "Malta"]), ("The tango", "Argentina", ["Chile", "Peru", "Portugal"]),
 ("The samba", "Brazil", ["Portugal", "Venezuela", "Peru"]), ("The haka", "New Zealand", ["Fiji", "Samoa", "Tonga"]),
 ("The polka", "Czechia", ["Germany", "Slovakia", "Hungary"]), ("The Viennese waltz", "Austria", ["Germany", "Switzerland", "Hungary"]),
 ("The can-can", "France", ["Belgium", "Switzerland", "Germany"]), ("The Highland fling", "Scotland", ["Wales", "Northern Ireland", "the Isle of Man"]),
 ("Morris dancing", "England", ["Wales", "Northern Ireland", "the Isle of Man"]), ("The hula", "Hawaii, USA", ["Fiji", "Samoa", "Tonga"]),
 ("Kathakali", "India", ["Sri Lanka", "Nepal", "Bangladesh"]), ("Salsa", "Cuba", ["Mexico", "Venezuela", "Jamaica"]),
 ("The mazurka", "Poland", ["Slovakia", "Hungary", "Russia"]), ("The tarantella", "Italy", ["Malta", "Portugal", "Croatia"]),
 ("The sirtaki", "Greece", ["Cyprus", "Turkey", "Bulgaria"]), ("The hopak", "Ukraine", ["Russia", "Romania", "Belarus"]),
 ("The merengue", "the Dominican Republic", ["Haiti", "Jamaica", "Puerto Rico"]), ("Cumbia", "Colombia", ["Venezuela", "Peru", "Mexico"]),
 ("Kecak, the monkey chant", "Indonesia", ["Malaysia", "Thailand", "the Philippines"]), ("Irish step dancing", "Ireland", ["Wales", "the Isle of Man", "Iceland"])])

race("name the famous real animal", "Animals", "medium", ["famous animals", "history"], [
 ("The first mammal cloned from an adult cell", "Dolly", ["Polly", "Molly", "Megan"]), ("The first dog in orbit", "Laika", ["Belka", "Strelka", "Albert"]),
 ("Downing Street's Chief Mouser since 2011", "Larry", ["Humphrey", "Palmerston", "Freya"]), ("The dog who found the stolen World Cup in 1966", "Pickles", ["Bruno", "Patch", "Rover"]),
 ("The octopus who 'predicted' World Cup results", "Paul", ["Achilles", "Mani", "Nelly"]), ("The loyal Akita who waited at Shibuya station", "Hachikō", ["Shiro", "Taro", "Hiro"]),
 ("London Zoo's famous giant panda", "Chi Chi", ["An An", "Ling Ling", "Yang Guang"]), ("The polar bear cub who became a Berlin star", "Knut", ["Flocke", "Wilbär", "Lars"]),
 ("The gorilla who learned sign language", "Koko", ["Kanzi", "Washoe", "Nim Chimpsky"]), ("The orca who starred in Free Willy", "Keiko", ["Tilikum", "Shamu", "Willy"]),
 ("The husky made famous by the serum run to Nome", "Balto", ["Togo", "Fala", "Rin Tin Tin"]), ("The Edinburgh terrier who guarded his master's grave", "Greyfriars Bobby", ["Auld Jock", "Hamish", "Bamse"]),
 ("The last passenger pigeon", "Martha", ["Polly", "Booming Ben", "Incas"]), ("The giant tortoise who was the last of his kind", "Lonesome George", ["Harriet", "Jonathan", "Diego"]),
 ("The chimp sent into space in 1961", "Ham", ["Enos", "Albert II", "Gordo"]), ("The Depression-era racehorse who beat War Admiral", "Seabiscuit", ["War Admiral", "Phar Lap", "Man o' War"]),
 ("London Zoo's famous old gorilla", "Guy", ["Kumbuka", "Alfred", "Jambo"]), ("The frowning cat who became an internet star", "Grumpy Cat", ["Lil Bub", "Maru", "Colonel Meow"]),
 ("Elizabeth II's first corgi", "Susan", ["Willow", "Monty", "Holly"]), ("The London Zoo black bear who inspired Winnie-the-Pooh", "Winnie", ["Brumas", "Barnaby", "Edward"])])

race("where is this sitcom set?", "Comedy", "medium", ["sitcoms", "places"], [
 ("Fawlty Towers", "Torquay", ["Paignton", "Brighton", "Weymouth"]), ("Gavin & Stacey (the Welsh half)", "Barry", ["Bridgend", "Swansea", "Cardiff"]),
 ("Only Fools and Horses", "Peckham", ["Brixton", "Lewisham", "Deptford"]), ("The Royle Family", "Manchester", ["Oldham", "Stockport", "Bury"]),
 ("Last of the Summer Wine", "Holmfirth", ["Hebden Bridge", "Huddersfield", "Haworth"]), ("Father Ted", "Craggy Island", ["Rugged Island", "Inis Mór", "Achill"]),
 ("Phoenix Nights", "Bolton", ["Wigan", "Oldham", "Preston"]), ("The Office (UK)", "Slough", ["Reading", "Basingstoke", "Bracknell"]),
 ("Dad's Army", "Walmington-on-Sea", ["Eastgate", "Seaview", "Westcliff"]), ("Peep Show", "Croydon", ["Lewisham", "Bromley", "Sutton"]),
 ("Porridge", "Slade Prison", ["Wormwood Scrubs", "Strangeways", "Barlinnie"]), ("Open All Hours", "Doncaster", ["Rotherham", "Barnsley", "Sheffield"]),
 ("Hi-de-Hi!", "Maplins holiday camp", ["Butlins", "Pontins", "Haven"]), ("Detectorists", "Danebury", ["Dunwich", "Framlingham", "Woodbridge"]),
 ("The League of Gentlemen", "Royston Vasey", ["Royston Vale", "Little Snoring", "Vasey Bridge"]), ("Rab C. Nesbitt", "Govan", ["Partick", "Paisley", "Possil"]),
 ("Still Game", "Craiglang", ["Craigmillar", "Craiglockhart", "Cardonald"]), ("Mrs Brown's Boys", "Finglas", ["Tallaght", "Ballymun", "Crumlin"]),
 ("Friday Night Dinner", "Mill Hill", ["Finchley", "Hendon", "Edgware"]), ("Ghosts", "Button House", ["Bly Manor", "Cliveden", "Blandings Castle"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-18.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
