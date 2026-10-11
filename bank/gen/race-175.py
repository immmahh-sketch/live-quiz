# Bank session 11 Oct 2026: 3 more general races -> bank/race-175.json (astronaut, optician and chemist words). 20 rows each, target 10; wrong options are
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

race("what's this astronaut word?", "Space", "medium", ["space", "astronauts", "words"], [
 ("The pressurised outfit for working in space", "Spacesuit", ["Wetsuit", "Boiler suit", "Jumpsuit"]),
 ("Going outside the craft in a suit", "Spacewalk", ["Moonwalk", "Catwalk", "Boardwalk"]),
 ("'10, 9, 8...' before the launch", "Countdown", ["Roll call", "Head count", "Recount"]),
 ("The moment the rocket leaves the pad", "Lift-off", ["Touchdown", "Kick-off", "Sign-off"]),
 ("Coming down in the sea in a capsule", "Splashdown", ["Touchdown", "Crash landing", "Belly flop"]),
 ("The space station, by its initials", "ISS", ["ESA", "RAF", "BBC"]),
 ("America's space agency", "NASA", ["ESA", "JAXA", "Roscosmos"]),
 ("Floating about weightless", "Zero gravity", ["Zero tolerance", "Ground zero", "Zero hour"]),
 ("The British astronaut who ran the London Marathon in space", "Tim Peake", ["Michael Foale", "Piers Sellers", "Tim Henman"]),
 ("The first Briton in space, in 1991", "Helen Sharman", ["Valentina Tereshkova", "Sally Ride", "Mae Jemison"]),
 ("The first person in space, in 1961", "Yuri Gagarin", ["Neil Armstrong", "Buzz Aldrin", "John Glenn"]),
 ("The mission that first landed people on the Moon", "Apollo 11", ["Apollo 13", "Gemini 4", "Vostok 1"]),
 ("'___, we've had a problem'", "Houston", ["Boston", "Dallas", "Austin"]),
 ("The team on the ground running the flight", "Mission control", ["Crowd control", "Remote control", "Air traffic control"]),
 ("The small crew cabin on top of the rocket", "Capsule", ["Cockpit", "Gondola", "Booth"]),
 ("An extra rocket strapped on for launch", "Booster", ["Rooster", "Bouncer", "Busker"]),
 ("The reusable winged spaceplane, retired in 2011", "Space Shuttle", ["Space station", "Space hopper", "Space Invader"]),
 ("How space food is preserved", "Freeze-dried", ["Deep-fried", "Sun-dried", "Pan-fried"]),
 ("Coming back into the atmosphere in a ball of heat", "Re-entry", ["Rerun", "Reboot", "Replay"]),
 ("The dog who orbited the Earth in 1957", "Laika", ["Lassie", "Snoopy", "Gromit"])])

race("what's this optician word?", "Health", "easy", ["opticians", "eyes", "words"], [
 ("Lenses in frames that sit on your nose", "Glasses", ["Binoculars", "Visor", "Mask"]),
 ("Thin discs that sit right on your eyes", "Contact lenses", ["Contact sport", "Contact book", "Contact form"]),
 ("Reading letters off a chart", "Eye test", ["Spelling test", "Driving test", "Blood test"]),
 ("The rows of shrinking letters on the wall", "Snellen chart", ["Pie chart", "Flow chart", "Bar chart"]),
 ("Can't see faraway things clearly", "Short-sighted", ["Cross-eyed", "Snow-blind", "Double-jointed"]),
 ("Can't see close-up things clearly", "Long-sighted", ["Cross-eyed", "Snow-blind", "Double-jointed"]),
 ("Glasses with two lens strengths", "Bifocals", ["Binoculars", "Bicycle", "Bilingual"]),
 ("Specs just for close-up", "Reading glasses", ["Sunglasses", "Opera glasses", "Safety glasses"]),
 ("The professional who tests your eyes", "Optometrist", ["Orthodontist", "Osteopath", "Optimist"]),
 ("The black dot in the centre of the eye", "Pupil", ["Retina", "Cornea", "Lid"]),
 ("The coloured ring around it", "Iris", ["Retina", "Cornea", "Lid"]),
 ("Short slang word for glasses", "Specs", ["Shades", "Bins", "Peepers"]),
 ("The part that holds the lenses", "Frames", ["Cases", "Cloths", "Chains"]),
 ("A soft cloth for wiping the lenses", "Lens cloth", ["Dishcloth", "Loincloth", "Tablecloth"]),
 ("Can't tell red from green", "Colour-blind", ["Cross-eyed", "Snow-blind", "Double-jointed"]),
 ("A weak eye that wanders, often patched in childhood", "Lazy eye", ["Black eye", "Evil eye", "Private eye"]),
 ("Eyes that don't line up", "Squint", ["Wink", "Blink", "Glance"]),
 ("A cloudy lens, common in old age", "Cataract", ["Glaucoma", "Conjunctivitis", "Astigmatism"]),
 ("A painful red lump on the eyelid", "Stye", ["Wart", "Mole", "Freckle"]),
 ("'Should've gone to ___'", "Specsavers", ["Boots", "Vision Express", "Superdrug"])])

race("what's this chemist word?", "Health", "easy", ["chemists", "medicine", "words"], [
 ("The doctor's note for medicine", "Prescription", ["Description", "Subscription", "Inscription"]),
 ("The qualified person who hands out medicines", "Pharmacist", ["Phlebotomist", "Physiotherapist", "Pharaoh"]),
 ("The common painkiller called acetaminophen in America", "Paracetamol", ["Penicillin", "Insulin", "Aspirin"]),
 ("The anti-inflammatory painkiller in Nurofen", "Ibuprofen", ["Penicillin", "Insulin", "Laxative"]),
 ("Tablets for hay fever", "Antihistamine", ["Antibiotic", "Antiseptic", "Laxative"]),
 ("A sticky strip for a cut", "Plaster", ["Coaster", "Poster", "Plasma"]),
 ("A sweet you suck for a sore throat", "Lozenge", ["Gobstopper", "Mint imperial", "Jelly bean"]),
 ("The pink medicine for children", "Calpol", ["Calamine", "Calypso", "Capitol"]),
 ("Measures your temperature", "Thermometer", ["Barometer", "Speedometer", "Pedometer"]),
 ("The puffer for asthma", "Inhaler", ["Kazoo", "Whistle", "Harmonica"]),
 ("Medicine in a little gelatin shell", "Capsule", ["Pellet", "Bead", "Pastille"]),
 ("Medicine you can buy without a prescription", "Over the counter", ["Under the table", "Behind the scenes", "Up for grabs"]),
 ("The cheaper, unbranded version of a medicine", "Generic", ["Genetic", "Genuine", "Generous"]),
 ("Unwanted extra things a medicine can do", "Side effects", ["Special effects", "Sound effects", "Personal effects"]),
 ("How much medicine to take at one time", "Dose", ["Doze", "Dash", "Dollop"]),
 ("The vitamin in oranges, said to fight colds", "Vitamin C", ["Vitamin D", "Vitamin K", "Vitamin B12"]),
 ("The high-street chemist founded by Jesse ___ in Nottingham", "Boots", ["Superdrug", "Lloyds", "Savers"]),
 ("The old symbol of the apothecary", "Pestle and mortar", ["Knife and fork", "Hammer and sickle", "Bow and arrow"]),
 ("The sign outside most chemists", "Green cross", ["Red cross", "Blue cross", "White cross"]),
 ("A dummy pill with no medicine in it", "Placebo", ["Gazebo", "Plateau", "Polo"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-175.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
