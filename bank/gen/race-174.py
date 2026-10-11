# Bank session 11 Oct 2026: 3 more general races -> bank/race-174.json (canal, firefighter and board game words). 20 rows each, target 10; wrong options are
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

race("what's this canal word?", "Travel", "medium", ["canals", "boats", "words"], [
 ("The long, thin boat built to fit the locks", "Narrowboat", ["Gondola", "Punt", "Coracle"]),
 ("The gated chamber that raises or lowers boats", "Lock", ["Weir", "Dam", "Ford"]),
 ("The person in charge of the lock gates", "Lock keeper", ["Gatekeeper", "Goalkeeper", "Bookkeeper"]),
 ("The L-shaped handle that winds the lock paddles", "Windlass", ["Wind-up", "Windbreak", "Windsock"]),
 ("A bridge carrying the canal over a valley", "Aqueduct", ["Viaduct", "Causeway", "Culvert"]),
 ("Telford's Welsh aqueduct, the highest in Britain", "Pontcysyllte", ["Menai", "Clifton", "Forth"]),
 ("The rotating boat lift in Scotland", "Falkirk Wheel", ["London Eye", "Ferris wheel", "Catherine wheel"]),
 ("Where boats were 'legged' through by men lying on their backs", "Tunnel", ["Chimney", "Mineshaft", "Culvert"]),
 ("Pushing a boat through a tunnel with your feet on the walls", "Legging", ["Paddling", "Poling", "Kedging"]),
 ("The old name for a canal boatman", "Bargee", ["Bargain hunter", "Barman", "Bandsman"]),
 ("How boats were pulled before engines", "Horse-drawn", ["Steam-powered", "Pedal-powered", "Wind-powered"]),
 ("The traditional painted decoration on boats", "Roses and Castles", ["Hearts and Flowers", "Stars and Stripes", "Lions and Unicorns"]),
 ("To tie up the boat for the night", "Moor", ["Anchor", "Beach", "Ground"]),
 ("Someone who idly watches the boats at a lock", "Gongoozler", ["Busybody", "Twitcher", "Trainspotter"]),
 ("Locks joined in a flight with no gap, like Bingley Five Rise", "Staircase", ["Ladder", "Escalator", "Spiral"]),
 ("A bridge you push aside to let a boat through", "Swing bridge", ["Rope bridge", "Suspension bridge", "Toll bridge"]),
 ("A wide spot where a long boat can turn round", "Winding hole", ["Rabbit hole", "Pothole", "Plughole"]),
 ("The Duke's canal of 1761, the start of the canal age", "Bridgewater", ["Grand Union", "Kennet and Avon", "Caledonian"]),
 ("James ___, the engineer who built it", "Brindley", ["Telford", "Brunel", "Stephenson"]),
 ("The stretch of water between two locks", "Pound", ["Penny", "Shilling", "Crown"])])

race("what's this firefighter word?", "Everyday life", "easy", ["firefighters", "fire safety", "words"], [
 ("The big red truck with ladders and hoses", "Fire engine", ["Ambulance", "Police van", "Tow truck"]),
 ("The long tube that sprays the water", "Hose", ["Rope", "Cable", "Chain"]),
 ("The street water point the hose plugs into", "Hydrant", ["Drain", "Manhole", "Meter"]),
 ("The brass rod you slide down to the engine", "Fireman's pole", ["Maypole", "Totem pole", "Flagpole"]),
 ("Carrying someone over your shoulders", "Fireman's lift", ["Ski lift", "Chairlift", "Facelift"]),
 ("The beeping box on the ceiling", "Smoke alarm", ["Burglar alarm", "Car alarm", "Alarm clock"]),
 ("The red cylinder you squeeze to put out a small fire", "Extinguisher", ["Defibrillator", "Inhaler", "Thermos"]),
 ("Thrown over a chip-pan fire", "Fire blanket", ["Picnic blanket", "Electric blanket", "Security blanket"]),
 ("The air tank and mask worn in thick smoke", "Breathing apparatus", ["Stethoscope", "Megaphone", "Visor"]),
 ("The number you call", "999", ["101", "111", "118"]),
 ("The extending ladder that swivels on the engine", "Turntable ladder", ["Stepladder", "Rope ladder", "Snakes and ladders"]),
 ("Where firefighters wait for a call", "Station", ["Depot", "Terminal", "Barracks"]),
 ("A firefighters' shift, like Blue ___ or Red ___", "Watch", ["Squad", "Platoon", "Unit"]),
 ("A practice evacuation", "Fire drill", ["Fire sale", "Fire walk", "Fire eater"]),
 ("Where everyone gathers outside", "Assembly point", ["Bus stop", "Checkpoint", "Lay-by"]),
 ("A heavy, self-closing door that slows a blaze", "Fire door", ["Trapdoor", "Stable door", "Revolving door"]),
 ("Starting a fire on purpose", "Arson", ["Treason", "Larceny", "Perjury"]),
 ("A gap cleared in a forest to stop the flames spreading", "Firebreak", ["Coffee break", "Jailbreak", "Windbreak"]),
 ("The outside staircase for getting out", "Fire escape", ["Back stairs", "Escalator", "Lift shaft"]),
 ("The hero of Pontypandy", "Fireman Sam", ["Postman Pat", "Bob the Builder", "Thomas the Tank Engine"])])

race("what's this board game?", "Games and toys", "easy", ["board games", "family games"], [
 ("Spotted cubes you roll", "Dice", ["Dominoes", "Tiddlywinks", "Marbles"]),
 ("Little pieces you move around the board", "Counters", ["Dominoes", "Cards", "Beads"]),
 ("Buy properties, pass Go, collect £200", "Monopoly", ["Game of Life", "Stratego", "Diplomacy"]),
 ("Colonel Mustard in the library with the candlestick", "Cluedo", ["Guess Who?", "Game of Life", "Othello"]),
 ("Letter tiles on a grid, with triple word scores", "Scrabble", ["Boggle", "Bananagrams", "Snap"]),
 ("Slide down, climb up, first to 100", "Snakes and ladders", ["Sorry!", "Backgammon", "Mancala"]),
 ("Four colours race home, and you need a six to get out", "Ludo", ["Sorry!", "Mancala", "Backgammon"]),
 ("Jump your opponent's pieces diagonally and crown a king", "Draughts", ["Chess", "Othello", "Backgammon"]),
 ("Collect a wedge for each category", "Trivial Pursuit", ["Articulate", "Taboo", "Guess Who?"]),
 ("Draw it for your team to guess", "Pictionary", ["Charades", "Articulate", "Taboo"]),
 ("Conquer the world, one territory at a time", "Risk", ["Diplomacy", "Stratego", "Game of Life"]),
 ("'B4!' 'Miss!' – sink the hidden fleet", "Battleship", ["Stratego", "Guess Who?", "Othello"]),
 ("Crack the hidden code of coloured pegs", "Mastermind", ["Othello", "Guess Who?", "Stratego"]),
 ("Drop discs to get four in a row", "Connect 4", ["Othello", "Snap", "Mancala"]),
 ("Pull out the sticks without dropping the marbles", "Kerplunk", ["Hungry Hippos", "Mousetrap", "Pop-up Pirate"]),
 ("Pull blocks from a tower without toppling it", "Jenga", ["Hungry Hippos", "Mousetrap", "Pop-up Pirate"]),
 ("Remove the funny bone without touching the sides", "Operation", ["Hungry Hippos", "Mousetrap", "Pop-up Pirate"]),
 ("Load the mule until it kicks", "Buckaroo", ["Hungry Hippos", "Mousetrap", "Pop-up Pirate"]),
 ("The ancient Chinese game of black and white stones", "Go", ["Mahjong", "Shogi", "Xiangqi"]),
 ("The Monopoly corner where nothing happens, officially", "Free Parking", ["Jail", "Go to Jail", "Community Chest"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-174.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
