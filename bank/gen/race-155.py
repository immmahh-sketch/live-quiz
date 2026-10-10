# Bank session 11 Oct 2026: 3 more general races -> bank/race-155.json (prison, swimming and festival words). 20 rows each, target 10; wrong options are
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

race("what's this prison word?", "Law", "medium", ["prison", "crime", "words"], [
 ("The small room a prisoner is locked in", "Cell", ["Ward", "Cubicle", "Booth"]),
 ("The person in charge of a British prison", "Governor", ["Mayor", "Provost", "Bailiff"]),
 ("Old prison slang for a guard", "Screw", ["Bolt", "Nail", "Rivet"]),
 ("Slang for time inside, and a Ronnie Barker sitcom", "Porridge", ["Gruel", "Stew", "Broth"]),
 ("'Doing ___': more slang for a sentence, from rhyming slang 'bird lime'", "Bird", ["Fish", "Pig", "Hen"]),
 ("Early release on good behaviour, under supervision", "Parole", ["Bail", "Remand", "Amnesty"]),
 ("Being locked up completely alone", "Solitary confinement", ["Open conditions", "Day release", "House arrest"]),
 ("A prisoner serving a life sentence", "Lifer", ["Rookie", "Trusty", "Remand"]),
 ("Slang for an informer", "Grass", ["Moss", "Fern", "Clover"]),
 ("A jail with no walls, for low-risk inmates", "Open prison", ["Halfway house", "Bail hostel", "Safe house"]),
 ("The old name for a youth prison", "Borstal", ["Workhouse", "Asylum", "Almshouse"]),
 ("The island prison in San Francisco Bay", "Alcatraz", ["Rikers", "Sing Sing", "Devil's Island"]),
 ("The West London prison known as 'the Scrubs'", "Wormwood Scrubs", ["Pentonville", "Holloway", "Brixton"]),
 ("The Manchester prison that saw a famous rooftop riot in 1990", "Strangeways", ["Durham", "Walton", "Armley"]),
 ("A homemade prison knife", "Shank", ["Cosh", "Truncheon", "Baton"]),
 ("Emptying the cell's bucket toilet each morning, a practice ended in 1996", "Slopping out", ["Lights out", "Roll call", "Mucking in"]),
 ("All prisoners confined to their cells after trouble", "Lockdown", ["Roll call", "Association", "Exercise yard"]),
 ("The pass a family needs to come and see an inmate", "Visiting order", ["Search warrant", "Court order", "Summons"]),
 ("Another word for a prisoner", "Inmate", ["Tenant", "Patient", "Lodger"]),
 ("The electronic device worn on the ankle after release", "Tag", ["Badge", "Lanyard", "Pager"])])

race("what's this swimming word?", "Sport", "easy", ["swimming", "pools", "words"], [
 ("The fastest stroke, also called freestyle", "Front crawl", ["Sidestroke", "Trudgen", "Lifesaving stroke"]),
 ("Frog-like kick, head up, arms sweeping round", "Breaststroke", ["Sidestroke", "Trudgen", "Sculling"]),
 ("The stroke swum lying face up", "Backstroke", ["Sidestroke", "Treading water", "Sculling"]),
 ("Both arms over together, with a dolphin kick", "Butterfly", ["Sidestroke", "Trudgen", "Sculling"]),
 ("A child's first stroke, paddling like a puppy", "Doggy paddle", ["Sculling", "Treading water", "Sidestroke"]),
 ("One swimmer using all four strokes in one race", "Individual medley", ["Decathlon", "Triathlon", "Pentathlon"]),
 ("Flipping over at the wall without touching it with your hands", "Tumble turn", ["Handstand", "Cartwheel", "Pirouette"]),
 ("The floating dividers between swimmers", "Lane rope", ["Guide rope", "Washing line", "Tightrope"]),
 ("Where the water's over your head", "Deep end", ["Shallow end", "Paddling pool", "Jacuzzi"]),
 ("Inflatables worn on the arms by beginners", "Armbands", ["Wristbands", "Headbands", "Garters"]),
 ("Keep the chlorine out of your eyes", "Goggles", ["Snorkel", "Visor", "Monocle"]),
 ("An outdoor public swimming pool", "Lido", ["Spa", "Grotto", "Sauna"]),
 ("A painful foot wart picked up at the pool", "Verruca", ["Bunion", "Corn", "Chilblain"]),
 ("Swimming from one end to the other, counted in these", "Lengths", ["Heats", "Rounds", "Innings"]),
 ("Britain's double Olympic champion in Beijing in 2008", "Rebecca Adlington", ["Sharron Davies", "Duncan Goodhew", "Keri-Anne Payne"]),
 ("British breaststroke king, Olympic champion in 2016 and 2021", "Adam Peaty", ["Tom Daley", "Duncan Goodhew", "Mark Foster"]),
 ("The American with a record 23 Olympic golds", "Michael Phelps", ["Mark Spitz", "Ian Thorpe", "Ryan Lochte"]),
 ("The chemical that keeps pool water clean", "Chlorine", ["Fluoride", "Iodine", "Ammonia"]),
 ("A rubber suit for open-water swimming", "Wetsuit", ["Tracksuit", "Jumpsuit", "Boiler suit"]),
 ("Now called artistic swimming: routines in time to music", "Synchronised swimming", ["Water polo", "Aquarobics", "Diving"])])

race("what's this festival word?", "Music", "easy", ["festivals", "Glastonbury", "words"], [
 ("The biggest act, on last at night", "Headliner", ["Support act", "Roadie", "Warm-up man"]),
 ("Glastonbury's famous main stage", "Pyramid Stage", ["Other Stage", "West Holts", "Park Stage"]),
 ("What you wear to prove you've got a ticket", "Wristband", ["Garter", "Anklet", "Armband"]),
 ("Footwear for when it gets muddy", "Wellies", ["Flip-flops", "Brogues", "Stilettos"]),
 ("The plastic toilet cubicle", "Portaloo", ["Gazebo", "Yurt", "Bivvy"]),
 ("The tent that springs open when you take it out of the bag", "Pop-up tent", ["Bell tent", "Teepee", "Marquee"]),
 ("The crush of fans thrashing about at the front", "Mosh pit", ["Ball pit", "Orchestra pit", "Pit stop"]),
 ("Being passed over the heads of the crowd", "Crowd-surfing", ["Body-boarding", "Kite-surfing", "Windsurfing"]),
 ("The extra songs after the band pretends to leave", "Encore", ["Interval", "Overture", "Prelude"]),
 ("The list of acts playing", "Line-up", ["Set list", "Tracklist", "Playlist"]),
 ("The list of demands for a band's dressing room", "Rider", ["Manifest", "Inventory", "Menu"]),
 ("The festival held at Worthy Farm in Somerset", "Glastonbury", ["Reading", "Latitude", "Isle of Wight"]),
 ("The twin festivals on the August bank holiday weekend", "Reading and Leeds", ["T in the Park", "Creamfields", "Latitude"]),
 ("The heavy metal festival at Donington Park", "Download", ["Bestival", "Latitude", "Boardmasters"]),
 ("The dairy farmer who founded Glastonbury", "Michael Eavis", ["Harvey Goldsmith", "Bob Geldof", "Simon Cowell"]),
 ("The year off Glastonbury takes to rest the land", "Fallow year", ["Leap year", "Gap year", "Jubilee year"]),
 ("Dancing with headphones on, so there's no noise", "Silent disco", ["Rave", "Ceilidh", "Tea dance"]),
 ("Testing the gear before the gig", "Sound check", ["Spot check", "Roll call", "Rain check"]),
 ("Posh camping in yurts and bell tents", "Glamping", ["Wild camping", "Caravanning", "Backpacking"]),
 ("The fence holding back the front row", "Barrier", ["Bollard", "Turnstile", "Hoarding"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-155.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
