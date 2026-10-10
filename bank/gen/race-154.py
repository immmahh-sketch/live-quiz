# Bank session 11 Oct 2026: 3 more general races -> bank/race-154.json (builders, skiing and dentist words). 20 rows each, target 10; wrong options are
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

race("what's this builder's word?", "Everyday life", "medium", ["building", "trades", "words"], [
 ("Metal poles and planks put up around a building", "Scaffolding", ["Trellis", "Pergola", "Lattice"]),
 ("A three-sided box on a pole for carrying bricks up a ladder", "Hod", ["Trug", "Pannier", "Satchel"]),
 ("The big metal bin left in the road for rubble", "Skip", ["Hopper", "Silo", "Vat"]),
 ("The paste between the bricks", "Mortar", ["Grout", "Putty", "Glue"]),
 ("The tool with a bubble that checks a surface is flat", "Spirit level", ["Set square", "Tape measure", "Protractor"]),
 ("The flat, diamond-shaped blade for spreading mortar", "Trowel", ["Spatula", "Chisel", "Scraper"]),
 ("The tradesperson who smooths the walls before painting", "Plasterer", ["Tiler", "Joiner", "Thatcher"]),
 ("Fits the glass in the windows", "Glazier", ["Tiler", "Joiner", "Thatcher"]),
 ("A horizontal beam that holds up a floor", "Joist", ["Rafter", "Purlin", "Post"]),
 ("The beam across the top of a door or window opening", "Lintel", ["Sill", "Jamb", "Architrave"]),
 ("A big grey building block made with cinders", "Breeze block", ["Paving slab", "Kerbstone", "Flagstone"]),
 ("The layer near the bottom of a wall that stops water rising", "Damp-proof course", ["Soffit", "Flashing", "Fascia"]),
 ("The concrete foundations under the walls", "Footings", ["Gables", "Eaves", "Coving"]),
 ("The rotating drum that churns the concrete", "Cement mixer", ["Tumble dryer", "Butter churn", "Cement silo"]),
 ("Builders' slang for an electrician", "Sparky", ["Scouser", "Squaddie", "Roadie"]),
 ("Builders' slang for a carpenter", "Chippy", ["Bobby", "Roadie", "Squaddie"]),
 ("Builders' slang for a bricklayer", "Brickie", ["Roadie", "Squaddie", "Bobby"]),
 ("The protective helmet worn on site", "Hard hat", ["Bowler", "Beret", "Deerstalker"]),
 ("A builder's price for the job, given before they start", "Quote", ["Invoice", "Receipt", "Statement"]),
 ("A dodgy tradesman who does shoddy work", "Cowboy builder", ["Ghost writer", "Back-seat driver", "Fair-weather friend"])])

race("what's this skiing word?", "Sport", "medium", ["skiing", "winter sports", "words"], [
 ("A marked, groomed ski run", "Piste", ["Track", "Lane", "Circuit"]),
 ("Seats on a cable carrying skiers up the mountain", "Chairlift", ["Funicular", "Rack railway", "Escalator"]),
 ("Drinks and partying after a day on the slopes", "Après-ski", ["Hors d'oeuvre", "Déjà vu", "Faux pas"]),
 ("The beginner's move: ski tips together in a V to slow down", "Snowplough", ["Herringbone", "Telemark", "Parallel turn"]),
 ("A bump on a ski slope", "Mogul", ["Boulder", "Crevasse", "Cornice"]),
 ("The hardest grade of run in Europe", "Black run", ["Blue run", "Red run", "Green run"]),
 ("Racing in a zig-zag between gates", "Slalom", ["Downhill", "Biathlon", "Luge"]),
 ("Skiing on unmarked, ungroomed snow", "Off-piste", ["Freestyle", "Slopestyle", "Big air"]),
 ("A great slide of snow down the mountain", "Avalanche", ["Blizzard", "Whiteout", "Snowdrift"]),
 ("Padded ski trousers held up by braces", "Salopettes", ["Jodhpurs", "Culottes", "Dungarees"]),
 ("Protect your eyes from the snow glare", "Goggles", ["Monocle", "Lorgnette", "Pince-nez"]),
 ("The ticket that lets you use the lifts", "Ski pass", ["Boarding pass", "Bus pass", "Backstage pass"]),
 ("A disc between your legs that drags you up the slope", "Button lift", ["Rack railway", "Escalator", "Travelator"]),
 ("Rides down on a single board", "Snowboarder", ["Tobogganist", "Bobsledder", "Luger"]),
 ("Launching off a huge ramp to fly as far as possible", "Ski jump", ["Half-pipe", "Skeleton", "Curling"]),
 ("Britain's famously hopeless 1988 Olympic ski jumper", "Eddie the Eagle", ["Torvill and Dean", "Robin Cousins", "Amy Williams"]),
 ("A wooden holiday house in the Alps", "Chalet", ["Bungalow", "Bothy", "Igloo"]),
 ("Fresh, fluffy, untouched snow that skiers love", "Powder", ["Slush", "Sleet", "Hail"]),
 ("An enclosed cabin on a cable, carrying a few people up", "Gondola", ["Funicular", "Rack railway", "Paternoster"]),
 ("The sticks you push yourself along with", "Poles", ["Crooks", "Canes", "Staves"])])

race("what's this dentist word?", "Health", "medium", ["dentist", "teeth", "words"], [
 ("The big, flat tooth at the back, for chewing", "Molar", ["Tusk", "Fang", "Gum"]),
 ("The sharp, flat front tooth, for biting", "Incisor", ["Tusk", "Fang", "Gum"]),
 ("The pointed tooth named after dogs", "Canine", ["Feline", "Lupine", "Bovine"]),
 ("The last molar to come through, often in your late teens or twenties", "Wisdom tooth", ["Sweet tooth", "Snaggletooth", "Dogtooth"]),
 ("A baby tooth", "Milk tooth", ["Sweet tooth", "Snaggletooth", "Dogtooth"]),
 ("What plugs the hole in a decayed tooth", "Filling", ["Retainer", "Denture", "Veneer"]),
 ("A cap fitted over a damaged tooth", "Crown", ["Veneer", "Bridge", "Inlay"]),
 ("Wires that straighten your teeth", "Brace", ["Splint", "Sling", "Truss"]),
 ("The sticky film of bacteria on your teeth", "Plaque", ["Mucus", "Pollen", "Moss"]),
 ("Plaque that's hardened into a crust", "Tartar", ["Rust", "Limescale", "Scab"]),
 ("The hardest substance in the body, coating your teeth", "Enamel", ["Dentine", "Cartilage", "Keratin"]),
 ("Inflamed, bleeding gums", "Gingivitis", ["Tonsillitis", "Conjunctivitis", "Laryngitis"]),
 ("Treatment that clears out the infected pulp inside a tooth", "Root canal", ["Bypass", "Keyhole", "Stent"]),
 ("The thread you pull between your teeth", "Floss", ["Twine", "Yarn", "Tinsel"]),
 ("The minty rinse you swish and spit", "Mouthwash", ["Shampoo", "Cordial", "Linctus"]),
 ("Does the scale and polish", "Hygienist", ["Optician", "Pharmacist", "Phlebotomist"]),
 ("The specialist who straightens teeth", "Orthodontist", ["Optician", "Chiropodist", "Audiologist"]),
 ("False teeth", "Dentures", ["Fangs", "Tusks", "Veneers"]),
 ("The mineral added to toothpaste to strengthen teeth", "Fluoride", ["Chlorine", "Iodine", "Helium"]),
 ("The whirring tool used on the decay", "Drill", ["Lathe", "Router", "Grinder"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-154.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
