# Bank session 11 Oct 2026: 3 more general races -> bank/race-189.json (archaeology, netball and volcano words). 20 rows each, target 10; wrong options are
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

race("what's this archaeology word?", "History", "medium", ["archaeology", "history", "words"], [
 ("The small pointed tool for scraping away soil", "Trowel", ["Spatula", "Chisel", "Ladle"]),
 ("Any object made by people in the past", "Artefact", ["Fossil", "Specimen", "Mineral"]),
 ("Telling a find's age from radioactive decay", "Carbon dating", ["Speed dating", "Carbon copy", "Tree-ring dating"]),
 ("A buried stash of treasure, like the Staffordshire one", "Hoard", ["Horde", "Herd", "Hoop"]),
 ("What hobbyists sweep across ploughed fields", "Metal detector", ["Smoke detector", "Lie detector", "Minesweeper"]),
 ("The Channel 4 show that dug a site in three days", "Time Team", ["Time Lords", "Dream Team", "Time Bandits"]),
 ("Its presenter, once Baldrick", "Tony Robinson", ["Phil Harding", "Mick Aston", "Michael Wood"]),
 ("The Anglo-Saxon ship burial in Suffolk", "Sutton Hoo", ["Sutton Coldfield", "Jarlshof", "Grime's Graves"]),
 ("The Stone Age village on Orkney", "Skara Brae", ["Jarlshof", "Maiden Castle", "Grime's Graves"]),
 ("The Roman fort near Hadrian's Wall famous for its writing tablets", "Vindolanda", ["Vindaloo", "Arbeia", "Segedunum"]),
 ("An ancient rubbish heap", "Midden", ["Mound", "Mire", "Moat"]),
 ("A prehistoric burial mound", "Barrow", ["Moat", "Motte", "Dyke"]),
 ("A circular bank and ditch, like Stonehenge", "Henge", ["Hinge", "Hedge", "Fringe"]),
 ("Broken bits of ancient pottery", "Potsherds", ["Crumbs", "Flakes", "Chips"]),
 ("The man who opened Tutankhamun's tomb in 1922", "Howard Carter", ["Indiana Jones", "Heinrich Schliemann", "Arthur Evans"]),
 ("Scanning under the ground without digging", "Geophysics", ["Geography", "Geometry", "Geology"]),
 ("The long pit dug across a site", "Trench", ["Moat", "Gully", "Tunnel"]),
 ("The stone chipped into tools and arrowheads", "Flint", ["Chalk", "Slate", "Marble"]),
 ("A floor picture of tiny tiles in a Roman villa", "Mosaic", ["Fresco", "Tapestry", "Collage"]),
 ("The slab that cracked Egyptian hieroglyphs", "Rosetta Stone", ["Philosopher's Stone", "Blarney Stone", "Stone of Scone"])])

race("what's this netball word?", "Sport", "medium", ["netball", "words"], [
 ("The vest with letters showing your position", "Bib", ["Sash", "Badge", "Armband"]),
 ("The only two positions allowed to shoot", "Goal Shooter and Goal Attack", ["Wing Attack and Centre", "Goal Keeper and Goal Defence", "Centre and Goal Defence"]),
 ("What GK stands for", "Goal Keeper", ["Game Keeper", "Goal Kicker", "Guard Keeper"]),
 ("What WD stands for", "Wing Defence", ["Wall Defence", "Wide Deep", "Wing Drive"]),
 ("The position allowed everywhere except the shooting circles", "Centre", ["Wing Attack", "Goal Attack", "Goal Defence"]),
 ("How play restarts after every goal", "Centre pass", ["Throw-in", "Bully-off", "Tip-off"]),
 ("The semicircle you must be inside to shoot", "Shooting circle", ["Penalty box", "Crease", "Key"]),
 ("The rule against moving your landing foot while holding the ball", "Footwork", ["Offside", "Double dribble", "Handball"]),
 ("Defending closer than 0.9 metres to the player with the ball", "Obstruction", ["Interference", "Offside", "Encroachment"]),
 ("Players per side on court", "7", ["5", "6", "11"]),
 ("How long you can hold the ball", "3 seconds", ["1 second", "5 seconds", "10 seconds"]),
 ("England's netball team", "The Roses", ["The Lionesses", "The Red Roses", "The Lady Lions"]),
 ("Scotland's netball team", "The Thistles", ["The Lionesses", "The Highlanders", "The Tartan Army"]),
 ("New Zealand's netball team", "The Silver Ferns", ["The All Blacks", "The Black Ferns", "The Kiwis"]),
 ("Australia's netball team", "The Diamonds", ["The Matildas", "The Wallabies", "The Kangaroos"]),
 ("The metal hoop on top of the post", "Ring", ["Backboard", "Basket", "Target"]),
 ("The jump ball when two players grab it at once", "Toss-up", ["Tip-off", "Bully-off", "Face-off"]),
 ("Each of the four periods of play", "Quarter", ["Half", "Innings", "Set"]),
 ("The pass awarded for contact or obstruction", "Penalty pass", ["Free kick", "Penalty corner", "Power play"]),
 ("England's top domestic competition", "Netball Super League", ["Championship", "Premiership", "Champions League"])])

race("what's this volcano word?", "Science", "medium", ["volcanoes", "earthquakes", "words"], [
 ("Molten rock underground", "Magma", ["Mantle", "Magnet", "Marrow"]),
 ("Molten rock once it reaches the surface", "Lava", ["Larva", "Lather", "Slag"]),
 ("The bowl-shaped hole at the top", "Crater", ["Grater", "Crevasse", "Cavern"]),
 ("Not erupting now, but could again", "Dormant", ["Dominant", "Docile", "Drowsy"]),
 ("Never expected to erupt again", "Extinct", ["Instinct", "Extant", "Exhausted"]),
 ("What grounded flights across Europe in 2010", "Ash cloud", ["Smog", "Fog bank", "Hailstorm"]),
 ("The Icelandic volcano that caused it", "Eyjafjallajökull", ["Etna", "Krakatoa", "Hekla"]),
 ("The Roman town buried in AD 79", "Pompeii", ["Pompidou", "Palermo", "Paestum"]),
 ("The volcano that buried it", "Vesuvius", ["Etna", "Stromboli", "Olympus"]),
 ("Huge moving slabs of the Earth's crust", "Tectonic plates", ["Dinner plates", "Number plates", "Hot plates"]),
 ("The old scale for measuring earthquakes", "Richter scale", ["Beaufort scale", "Mohs scale", "Kelvin scale"]),
 ("The point on the surface right above a quake", "Epicentre", ["Bullseye", "Hypocentre", "Midpoint"]),
 ("A smaller quake after the big one", "Aftershock", ["Afterburner", "Aftertaste", "Afterglow"]),
 ("A giant wave caused by an undersea quake", "Tsunami", ["Typhoon", "Monsoon", "Tornado"]),
 ("The instrument that records ground shaking", "Seismograph", ["Barometer", "Thermometer", "Anemometer"]),
 ("A crack where plates slip past each other", "Fault line", ["Fold", "Ridge", "Groove"]),
 ("California's famous fault", "San Andreas", ["San Diego", "Santa Ana", "San Fermín"]),
 ("The Pacific's horseshoe of volcanoes", "Ring of Fire", ["Ring of Kerry", "Circle of Life", "Ring of Brodgar"]),
 ("A deadly rushing avalanche of hot gas and ash", "Pyroclastic flow", ["Lava lamp", "Mudslide", "Firestorm"]),
 ("A hot spring that shoots water into the air", "Geyser", ["Geezer", "Fumarole", "Spout"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-189.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
