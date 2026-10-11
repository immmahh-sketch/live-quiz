# Bank session 11 Oct 2026: 3 more general races -> bank/race-201.json (Crystal Maze, The Chase and Only Fools and Horses). 20 rows each, target 10; wrong options are
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

race("what's this Crystal Maze word?", "TV", "medium", ["The Crystal Maze", "game shows", "words"], [
 ("The giant dome where you grab tickets in the final", "Crystal Dome", ["Millennium Dome", "Thunderdome", "Snow globe"]),
 ("The tickets that count towards your total", "Gold tokens", ["Gold coins", "Gold stars", "Golden tickets"]),
 ("The tickets that get taken off your total", "Silver tokens", ["Bronze tokens", "Red tokens", "Black tokens"]),
 ("What each game wins", "Crystals", ["Diamonds", "Rubies", "Pearls"]),
 ("The original host, who played the harmonica", "Richard O'Brien", ["Richard Whiteley", "Richard Madeley", "Richard Hammond"]),
 ("The host who took over in 1993", "Ed Tudor-Pole", ["Ed Balls", "Ed Sheeran", "Ed Byrne"]),
 ("The host of the 2017 revival", "Richard Ayoade", ["Stephen Merchant", "Rob Brydon", "Noel Fielding"]),
 ("The instrument the first host played", "Harmonica", ["Kazoo", "Ukulele", "Banjo"]),
 ("Trapped in the cell when time runs out", "Lock-in", ["Lockjaw", "Lockdown", "Lock-up"]),
 ("What breaking a rule triggers", "Automatic lock-in", ["Automatic win", "Penalty kick", "Time-out"]),
 ("Swapping a crystal to free a trapped teammate", "Buy-back", ["Buy-out", "Payback", "Cashback"]),
 ("Skill, Physical, Mental and ...", "Mystery", ["Musical", "Magic", "Memory"]),
 ("The zone with a pyramid and sand", "Aztec", ["Roman", "Viking", "Greek"]),
 ("The zone set on a space station", "Futuristic", ["Galactic", "Cosmic", "Lunar"]),
 ("The zone of pipes, steam and machinery", "Industrial", ["Victorian", "Mechanical", "Steampunk"]),
 ("The zone of castles and knights", "Medieval", ["Tudor", "Gothic", "Norman"]),
 ("The famous line before the final", "Start the fans, please!", ["Let's get ready to rumble!", "Come on down!", "Lights, camera, action!"]),
 ("The live London version you can play yourself", "Crystal Maze Live", ["Crystal Palace", "Crystal Ball", "Crystal Method"]),
 ("The channel it first aired on", "Channel 4", ["BBC One", "ITV", "Channel 5"]),
 ("Players in a team", "6", ["4", "5", "8"])])

race("what's this word from The Chase?", "TV", "easy", ["The Chase", "quiz shows", "words"], [
 ("The quiz genius chasing the contestants", "Chaser", ["Chancer", "Chaperone", "Chaplain"]),
 ("The host", "Bradley Walsh", ["Ben Shephard", "Alexander Armstrong", "Nick Knowles"]),
 ("Mark Labbett's nickname", "The Beast", ["The Brain", "The Professor", "The Shark"]),
 ("Anne Hegerty's nickname", "The Governess", ["The Headmistress", "The Matron", "The Duchess"]),
 ("Shaun Wallace's nickname", "The Dark Destroyer", ["The Black Panther", "The Terminator", "The Hammer"]),
 ("Paul Sinha's nickname", "The Sinnerman", ["The Saint", "The Bishop", "The Monk"]),
 ("Jenny Ryan's nickname", "The Vixen", ["The Fox", "The Cat", "The Siren"]),
 ("Darragh Ennis's nickname", "The Menace", ["The Brute", "The Bruiser", "The Joker"]),
 ("The first round: as many answers as you can in a minute", "Cash builder", ["Cash cow", "Cash point", "Cashback"]),
 ("Bigger money for starting closer to the Chaser", "Higher offer", ["Better deal", "Top bid", "Gamble"]),
 ("Less money but a head start", "Lower offer", ["Lowball", "Safe bet", "Downgrade"]),
 ("The two-minute showdown at the end", "Final Chase", ["Final Countdown", "Last Lap", "Car Chase"]),
 ("Stopping the clock when the Chaser slips up", "Pushback", ["Comeback", "Kickback", "Flashback"]),
 ("Steps given for each player who reaches the final", "Head start", ["Jump start", "False start", "Fresh start"]),
 ("When the Chaser lands on your step", "Caught", ["Bowled", "Stumped", "Tagged"]),
 ("Getting the money all the way down the board", "Getting home", ["Getting off", "Getting by", "Getting lost"]),
 ("The question format in the head-to-head", "Multiple choice", ["True or false", "Fill in the blank", "Spot the difference"]),
 ("The spin-off where several Chasers take on one player", "Beat the Chasers", ["Beat the Clock", "Beat the Intro", "Beat Bobby Flay"]),
 ("The channel it's on", "ITV", ["BBC One", "Channel 4", "Sky One"]),
 ("The ITV quiz that follows it some afternoons, with a coin-pusher", "Tipping Point", ["Pointless", "Golden Balls", "Deal or No Deal"])])

race("what's this Only Fools and Horses word?", "TV", "easy", ["Only Fools and Horses", "sitcoms", "words"], [
 ("The wheeler-dealer played by David Jason", "Del Boy", ["Arthur Daley", "Frank Spencer", "Albert Steptoe"]),
 ("His younger brother, the 'plonker'", "Rodney", ["Dougal", "Baldrick", "Gareth"]),
 ("The road sweeper who calls Rodney 'Dave'", "Trigger", ["Sparky", "Arthur", "Norman"]),
 ("The smug second-hand car dealer", "Boycie", ["Smithy", "Gareth", "Swiss Toni"]),
 ("The long-suffering lorry driver", "Denzil", ["Dennis", "Derek", "Darren"]),
 ("The old sailor who starts every story 'During the war...'", "Uncle Albert", ["Captain Birdseye", "Captain Pugwash", "Uncle Bulgaria"]),
 ("The old man glued to two tellies", "Grandad", ["Granny", "Grandpa Joe", "Uncle Fester"]),
 ("Del's partner, mother of Damien", "Raquel", ["Rachel", "Rebecca", "Rosie"]),
 ("Rodney's posh wife", "Cassandra", ["Camilla", "Clarissa", "Cordelia"]),
 ("Their local pub", "Nag's Head", ["Rovers Return", "Queen Vic", "Woolpack"]),
 ("The part of London they live in", "Peckham", ["Walford", "Hackney", "Brixton"]),
 ("Their tower block", "Nelson Mandela House", ["Nelson's Column", "Mandela Way", "Churchill House"]),
 ("Their yellow three-wheeled van", "Reliant Regal", ["Ford Transit", "Morris Minor", "Bond Bug"]),
 ("The firm painted on the van", "Trotters Independent Traders", ["Peckham Market Traders", "Del's Discount Deals", "Trotter & Sons"]),
 ("Del's catchphrase for something great", "Lovely jubbly", ["Bob's your uncle", "Easy peasy", "Bang tidy"]),
 ("What Del calls Rodney", "Plonker", ["Wally", "Muppet", "Numpty"]),
 ("What they drop in the famous stately-home scene", "Chandelier", ["Grandfather clock", "Grand piano", "Suit of armour"]),
 ("Their fancy dress in 'Heroes and Villains'", "Batman and Robin", ["Laurel and Hardy", "Starsky and Hutch", "Bananas in Pyjamas"]),
 ("The actor who played Del", "David Jason", ["Nicholas Lyndhurst", "Ronnie Barker", "Dennis Waterman"]),
 ("The writer of the show", "John Sullivan", ["Richard Curtis", "Ben Elton", "Roy Clarke"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-201.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
