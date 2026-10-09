# Bank session 9 Oct 2026 (third pass): 20 more Only One prompts appended to bank/unique-prompts.json. Each is a
# closed list with every correct answer (other accepted forms after a slash), so a fair answer is never knocked out.
import json, os
NEW = [
 ("Name a character from The Magic Roundabout", ["Dougal", "Zebedee", "Florence", "Brian", "Ermintrude", "Dylan", "Mr Rusty", "Mr McHenry"]),
 ("Name an animal the mouse meets in The Gruffalo, or the Gruffalo itself", ["Fox", "Owl", "Snake", "Gruffalo/The Gruffalo"]),
 ("Name one of Jupiter's four Galilean moons, or Saturn's biggest moon", ["Io", "Europa", "Ganymede", "Callisto", "Titan"]),
 ("Name a state of matter, or one of the three main types of rock", ["Solid", "Liquid", "Gas", "Plasma", "Igneous", "Sedimentary", "Metamorphic"]),
 ("Name a vitamin by its letter", ["A", "B/B1/B2/B3/B5/B6/B7/B9/B12", "C", "D", "E", "K"]),
 ("Name an Olympic athletics throwing event or jumping event", ["Shot put/Shot", "Discus", "Hammer/Hammer throw", "Javelin", "High jump", "Long jump", "Triple jump", "Pole vault"]),
 ("Name a club in Scotland's Premiership in the 2025–26 season", ["Aberdeen", "Celtic", "Dundee", "Dundee United", "Falkirk", "Hearts/Heart of Midlothian", "Hibernian/Hibs", "Kilmarnock", "Livingston", "Motherwell", "Rangers", "St Mirren"]),
 ("Name a child of Henry VIII", ["Mary I/Mary", "Elizabeth I/Elizabeth", "Edward VI/Edward", "Henry FitzRoy", "Henry, Duke of Cornwall"]),
 ("Name an airport that calls itself a London airport", ["Heathrow", "Gatwick", "Stansted", "Luton", "London City/City", "Southend", "Biggin Hill"]),
 ("Name a bird of the crow family found in Britain", ["Crow/Carrion crow/Hooded crow", "Rook", "Raven", "Jackdaw", "Magpie", "Jay", "Chough"]),
 ("Name a drum or cymbal in a standard drum kit", ["Bass drum/Kick drum", "Snare drum/Snare", "Hi-hat", "Crash cymbal/Crash", "Ride cymbal/Ride", "Tom-tom/Tom/Rack tom", "Floor tom"]),
 ("Name a colour on a classic Rubik's Cube", ["White", "Yellow", "Red", "Orange", "Blue", "Green"]),
 ("Name a wedge colour or a subject in classic Trivial Pursuit", ["Blue", "Pink", "Yellow", "Brown", "Green", "Orange", "Geography", "Entertainment", "History", "Arts and Literature/Art and Literature", "Science and Nature", "Sport and Leisure/Sports and Leisure"]),
 ("Name an Olympic swimming stroke, or a weapon used in Olympic fencing", ["Freestyle/Front crawl/Crawl", "Backstroke", "Breaststroke", "Butterfly", "Foil", "Épée/Epee", "Sabre/Saber"]),
 ("Name a member of the Monkees or of Wham!", ["Davy Jones", "Micky Dolenz", "Michael Nesmith/Mike Nesmith", "Peter Tork", "George Michael", "Andrew Ridgeley"]),
 ("Name a coin from Britain's old pre-decimal money", ["Farthing", "Halfpenny/Ha'penny", "Penny", "Threepenny bit/Thruppenny bit/Threepence", "Sixpence/Tanner", "Shilling/Bob", "Florin/Two shillings/Two bob", "Half crown/Half a crown", "Crown", "Guinea", "Sovereign", "Groat"]),
 ("Name one of the six New England states", ["Maine", "New Hampshire", "Vermont", "Massachusetts", "Rhode Island", "Connecticut"]),
 ("Name a British Army officer rank", ["Second Lieutenant", "Lieutenant", "Captain", "Major", "Lieutenant Colonel", "Colonel", "Brigadier", "Major General", "Lieutenant General", "General", "Field Marshal"]),
 ("Name a colour of one of the Olympic rings", ["Blue", "Yellow", "Black", "Green", "Red"]),
 ("Name an English county that has a coastline on the North Sea", ["Northumberland", "Tyne and Wear", "County Durham/Durham", "North Yorkshire", "East Riding of Yorkshire", "Lincolnshire", "Norfolk", "Suffolk", "Essex", "Kent"]),
]
here = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(here, '..', 'unique-prompts.json')
cur = json.load(open(path, encoding='utf-8'))
have = {x['p'].lower() for x in cur}
added = [{"p": p, "a": a} for p, a in NEW if p.lower() not in have]
json.dump(cur + added, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(added), 'prompts added; now', len(cur) + len(added))
