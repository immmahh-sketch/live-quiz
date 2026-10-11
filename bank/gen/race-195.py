# Bank session 11 Oct 2026: 3 more general races -> bank/race-195.json (scuba diving, beekeeping and brewing words). 20 rows each, target 10; wrong options are
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

race("what's this scuba diving word?", "Sport", "medium", ["scuba diving", "the sea", "words"], [
 ("A neoprene suit that keeps you warm in the water", "Wetsuit", ["Tracksuit", "Boiler suit", "Spacesuit"]),
 ("A sealed suit that keeps the water out altogether", "Drysuit", ["Tracksuit", "Jumpsuit", "Spacesuit"]),
 ("A breathing tube for swimming face-down at the surface", "Snorkel", ["Periscope", "Funnel", "Straw"]),
 ("Rubber fins on your feet", "Flippers", ["Paddles", "Clogs", "Flip-flops"]),
 ("The mouthpiece that delivers air from the tank", "Regulator", ["Radiator", "Respirator", "Ventilator"]),
 ("The bottle of air on your back", "Cylinder", ["Barrel", "Flask", "Keg"]),
 ("Sickness from coming up too fast", "The bends", ["The shakes", "The shivers", "The runs"]),
 ("Pausing on the way up to let gas leave your body", "Decompression stop", ["Pit stop", "Bus stop", "Full stop"]),
 ("The partner you always dive with", "Buddy", ["Caddie", "Chaperone", "Steward"]),
 ("The world's biggest diving qualification body, by its letters", "PADI", ["RNLI", "RSPB", "RAC"]),
 ("A colourful underwater ridge built by tiny animals", "Coral reef", ["Sandbank", "Seabed", "Kelp forest"]),
 ("Exploring a sunken ship", "Wreck dive", ["Salvage run", "Shipshape", "Wreck-It Ralph"]),
 ("The French pioneer of the Aqualung", "Jacques Cousteau", ["Jacques Chirac", "Jacques Brel", "Jacques Clouseau"]),
 ("Lead strapped round your waist so you sink", "Weight belt", ["Seat belt", "Black belt", "Money belt"]),
 ("The inflatable vest you adjust to float or sink", "Buoyancy jacket", ["Straitjacket", "Dinner jacket", "Donkey jacket"]),
 ("The stretchy rubber wetsuits are made of", "Neoprene", ["Nylon", "Polystyrene", "Kevlar"]),
 ("Diving deep on a single breath", "Free diving", ["Skydiving", "Cliff diving", "Deep-sea fishing"]),
 ("Goggles that cover your eyes and nose", "Mask", ["Visor", "Monocle", "Blindfold"]),
 ("How far you can see underwater", "Visibility", ["Velocity", "Viscosity", "Humidity"]),
 ("The world's biggest coral reef system", "Great Barrier Reef", ["Great Wall", "Great Rift Valley", "Great Lakes"])])

race("what's this beekeeping word?", "Nature", "medium", ["bees", "honey", "words"], [
 ("The box the colony lives in", "Hive", ["Hutch", "Coop", "Kennel"]),
 ("The only bee that lays eggs", "Queen", ["Duchess", "Matriarch", "Princess"]),
 ("A male bee", "Drone", ["Stag", "Bull", "Cob"]),
 ("The female bees that do all the jobs", "Workers", ["Soldiers", "Servants", "Labourers"]),
 ("Wax cells where honey is stored", "Honeycomb", ["Honey trap", "Honeydew", "Honeymoon"]),
 ("The six-sided shape of each cell", "Hexagon", ["Pentagon", "Octagon", "Heptagon"]),
 ("Thousands leaving with the old queen to find a new home", "Swarm", ["Stampede", "Flock", "Shoal"]),
 ("Puffs smoke to calm the bees", "Smoker", ["Fogger", "Kettle", "Chimney"]),
 ("Mesh over the beekeeper's face", "Veil", ["Visor", "Balaclava", "Snood"]),
 ("A place where hives are kept", "Apiary", ["Aviary", "Aquarium", "Arboretum"]),
 ("Another word for a beekeeper", "Apiarist", ["Arborist", "Aviator", "Artist"]),
 ("The sugary liquid bees collect from flowers", "Nectar", ["Sap", "Dew", "Syrup"]),
 ("Yellow dust carried home on bees' legs", "Pollen", ["Spores", "Talc", "Sawdust"]),
 ("The special food fed to future queens", "Royal jelly", ["Royal icing", "Royal flush", "Jelly baby"]),
 ("Sticky 'bee glue' made from tree resin", "Propolis", ["Metropolis", "Acropolis", "Necropolis"]),
 ("How a bee tells the others where the flowers are", "Waggle dance", ["Rain dance", "Moonwalk", "Conga"]),
 ("The eggs, larvae and pupae in the comb", "Brood", ["Litter", "Clutch", "Spawn"]),
 ("New Zealand honey prized as a health food", "Manuka", ["Maori", "Marula", "Matcha"]),
 ("What candles and lip balm are made from in the hive", "Beeswax", ["Earwax", "Paraffin", "Tallow"]),
 ("The box stacked on top of the hive for honey", "Super", ["Topper", "Lid", "Attic"])])

race("what's this brewing word?", "Food and drink", "medium", ["beer", "brewing", "words"], [
 ("The flowers that give beer its bitterness", "Hops", ["Barley", "Heather", "Elderflower"]),
 ("Barley soaked, sprouted and dried", "Malt", ["Bran", "Chaff", "Husk"]),
 ("Malt steeped in hot water to release its sugars", "Mash", ["Smash", "Mesh", "Marsh"]),
 ("The sugary liquid drained off before fermenting", "Wort", ["Wart", "Worm", "Whey"]),
 ("Turns the sugar into alcohol", "Yeast", ["Rennet", "Gelatine", "Baking powder"]),
 ("The process where sugar becomes alcohol", "Fermentation", ["Distillation", "Pasteurisation", "Filtration"]),
 ("The barrel real ale is served from", "Cask", ["Casket", "Crate", "Carton"]),
 ("A pressurised metal container for fizzy beer", "Keg", ["Peg", "Leg", "Egg"]),
 ("The Campaign for Real Ale, by its letters", "CAMRA", ["RSPCA", "CAMEO", "NAAFI"]),
 ("Beer that keeps maturing in the cask", "Real ale", ["Real deal", "Real Madrid", "Real time"]),
 ("A dark, roasty beer like Guinness", "Stout", ["Shandy", "Cider", "Perry"]),
 ("Pale, cold, fizzy beer", "Lager", ["Shandy", "Cider", "Perry"]),
 ("Hoppy pale ale first brewed for the voyage to India", "IPA", ["NHS", "BBC", "DIY"]),
 ("The strength on the label, by its letters", "ABV", ["BMI", "RPM", "MPH"]),
 ("The foam on top of a pint", "Head", ["Cap", "Crown", "Hat"]),
 ("A nine-gallon cask", "Firkin", ["Gherkin", "Pumpkin", "Bumpkin"]),
 ("The tall lever the barman pulls", "Hand pump", ["Handbrake", "Bike pump", "Handshake"]),
 ("The nozzle that gives a northern pint its creamy head", "Sparkler", ["Firework", "Glitter", "Sprinkler"]),
 ("A small independent brewery", "Microbrewery", ["Micromanager", "Microwave", "Microchip"]),
 ("The classic copper-coloured English ale", "Bitter", ["Sweet", "Sour", "Savoury"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-195.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
