# Bank session 11 Oct 2026: 3 more general races -> bank/race-156.json (walking, beach and science words). 20 rows each, target 10; wrong options are
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

race("what's this walking word?", "Everyday life", "medium", ["walking", "countryside", "words"], [
 ("The bag on your back", "Rucksack", ["Holdall", "Satchel", "Briefcase"]),
 ("A concrete pillar on a hilltop, put there by map-makers", "Trig point", ["Milestone", "Bollard", "Gatepost"]),
 ("A pile of stones marking a path or summit", "Cairn", ["Dolmen", "Menhir", "Henge"]),
 ("The walkers' map, by its two-letter initials", "OS", ["AA", "RAC", "BT"]),
 ("Shows you which way is north", "Compass", ["Sextant", "Barometer", "Protractor"]),
 ("Lines on a map joining places of equal height", "Contour lines", ["Grid lines", "Isobars", "Latitude lines"]),
 ("The Lake District word for a hill or mountain", "Fell", ["Tor", "Brae", "Ben"]),
 ("A Scottish mountain over 3,000 feet", "Munro", ["Wainwright", "Marilyn", "Corbett"]),
 ("Climbing with your hands on rocky ground", "Scramble", ["Abseil", "Hike", "Trek"]),
 ("A member of a walking club out in the countryside", "Rambler", ["Rover", "Ranger", "Drifter"]),
 ("A path open to walkers, cyclists and horse riders", "Bridleway", ["Footpath", "Ginnel", "Snicket"]),
 ("The path beside a canal", "Towpath", ["Promenade", "Boardwalk", "Causeway"]),
 ("A little arrow on a post pointing out the route", "Waymarker", ["Signet", "Bookmark", "Bollard"]),
 ("Covers worn over boots and lower legs to keep out the mud", "Gaiters", ["Spats", "Puttees", "Garters"]),
 ("The sugary Lake District energy bar taken up Everest", "Kendal Mint Cake", ["Grasmere gingerbread", "Eccles cake", "Bakewell tart"]),
 ("The legal freedom to walk across open countryside", "Right to roam", ["Freedom of the city", "Habeas corpus", "Squatters' rights"]),
 ("The very top of the mountain", "Summit", ["Saddle", "Col", "Ridge"]),
 ("A basic shelter in the hills, free for anyone to use", "Bothy", ["Chalet", "Gîte", "Lodge"]),
 ("A painful bubble on the heel from new boots", "Blister", ["Bunion", "Corn", "Verruca"]),
 ("A pair of sticks that take the strain off your knees", "Walking poles", ["Crutches", "Batons", "Stilts"])])

race("what's this beach word?", "Everyday life", "easy", ["seaside", "beach", "words"], [
 ("A striped fabric screen pegged into the sand", "Windbreak", ["Gazebo", "Awning", "Trellis"]),
 ("A folding canvas seat", "Deckchair", ["Bean bag", "Pouffe", "Rocking chair"]),
 ("A pool left among the rocks when the tide goes out", "Rock pool", ["Plunge pool", "Paddling pool", "Millpond"]),
 ("A wooden barrier running down the beach into the sea", "Groyne", ["Jetty", "Slipway", "Boardwalk"]),
 ("The sea coming in and going out twice a day", "Tide", ["Current", "Swell", "Surf"]),
 ("Watches the swimmers from a high chair", "Lifeguard", ["Coastguard", "Harbourmaster", "Steward"]),
 ("Red and yellow ones show where it's safe to swim", "Flags", ["Buoys", "Cones", "Bunting"]),
 ("Built with a bucket and spade", "Sandcastle", ["Snowman", "Igloo", "Bonfire"]),
 ("The paved walk along the seafront", "Promenade", ["Arcade", "Concourse", "Precinct"]),
 ("A long platform on stilts out to sea, often with arcades", "Pier", ["Lighthouse", "Breakwater", "Harbour wall"]),
 ("Slimy green and brown plants washed up on the shore", "Seaweed", ["Moss", "Lichen", "Ivy"]),
 ("A see-through sea creature that can sting", "Jellyfish", ["Starfish", "Sea urchin", "Sea cucumber"]),
 ("A brightly painted wooden cabin on the seafront", "Beach hut", ["Chalet", "Shed", "Kiosk"]),
 ("The traditional seaside ride at Blackpool and Weston", "Donkey rides", ["Pony trekking", "Camel rides", "Hay rides"]),
 ("Rub it on so you don't burn", "Suncream", ["Moisturiser", "Aftershave", "Hand cream"]),
 ("Rubber sandals held on between your toes", "Flip-flops", ["Clogs", "Espadrilles", "Moccasins"]),
 ("A beach of small pebbles instead of sand", "Shingle", ["Silt", "Clay", "Loam"]),
 ("The line of seaweed and shells left by the high tide", "Strandline", ["Skyline", "Treeline", "Horizon"]),
 ("An inflatable mattress you float on", "Lilo", ["Futon", "Hammock", "Bean bag"]),
 ("A cheeky seaside hat with a slogan on it", "Kiss-me-quick hat", ["Bobble hat", "Deerstalker", "Trilby"])])

race("what's this science word?", "Science and nature", "medium", ["science", "physics", "chemistry", "biology"], [
 ("The tiny building block of every element", "Atom", ["Pixel", "Crystal", "Fibre"]),
 ("The smallest unit of a living thing", "Cell", ["Organ", "Tissue", "Limb"]),
 ("Two or more atoms bonded together, like H2O", "Molecule", ["Isotope", "Ion", "Photon"]),
 ("The negatively charged particle whizzing round an atom", "Electron", ["Photon", "Positron", "Quark"]),
 ("The centre of an atom", "Nucleus", ["Shell", "Orbit", "Membrane"]),
 ("The force that pulls things towards the Earth", "Gravity", ["Inertia", "Momentum", "Magnetism"]),
 ("The force that slows things down as they rub together", "Friction", ["Inertia", "Momentum", "Magnetism"]),
 ("How plants make food from sunlight", "Photosynthesis", ["Pollination", "Germination", "Fermentation"]),
 ("Releasing energy from food inside your cells", "Respiration", ["Digestion", "Circulation", "Excretion"]),
 ("A liquid turning into a gas", "Evaporation", ["Melting", "Freezing", "Sublimation"]),
 ("A gas turning back into a liquid", "Condensation", ["Melting", "Freezing", "Sublimation"]),
 ("Has a pH below 7, like lemon juice", "Acid", ["Base", "Salt", "Buffer"]),
 ("Has a pH above 7, like bleach", "Alkali", ["Salt", "Buffer", "Solvent"]),
 ("An idea you test with an experiment", "Hypothesis", ["Conclusion", "Theorem", "Variable"]),
 ("Speeds up a reaction without being used up", "Catalyst", ["Solvent", "Inhibitor", "Residue"]),
 ("The energy of movement", "Kinetic energy", ["Thermal energy", "Nuclear energy", "Chemical energy"]),
 ("Energy stored by something raised up high", "Potential energy", ["Thermal energy", "Sound energy", "Light energy"]),
 ("The amount of matter in something, measured in kilograms", "Mass", ["Weight", "Volume", "Density"]),
 ("The unit of force, named after a famous scientist", "Newton", ["Joule", "Watt", "Pascal"]),
 ("A space with nothing in it, not even air", "Vacuum", ["Vortex", "Vapour", "Venturi"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-156.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
