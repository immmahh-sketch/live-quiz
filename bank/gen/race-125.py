# Bank session 10 Oct 2026: 2 more general races -> bank/race-125.json (DIY tools, parts of a castle). 20 rows each, target 10; wrong options are
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


race("which DIY tool is this?", "Everyday life", "medium", ["DIY", "tools"], [
 ("Drives nails in, and its split back end pulls them out", "Claw hammer", ["Nail punch", "Scraper", "Rasp"]),
 ("A wooden or rubber-headed hammer for tapping a chisel or tent pegs", "Mallet", ["Nail punch", "Bolster", "Rasp"]),
 ("Comes in flat-head and Phillips varieties", "Screwdriver", ["Countersink", "Torque wrench", "Socket set"]),
 ("A bubble in a tube tells you if a shelf is straight", "Spirit level", ["Set square", "Chalk line", "Plumb bob"]),
 ("Grips the flats of a nut to turn it", "Spanner", ["Pipe cutter", "Wire strippers", "Countersink"]),
 ("Two pivoting jaws for gripping, bending and snipping wire", "Pliers", ["Pipe cutter", "Tile cutter", "Hole saw"]),
 ("A fine-toothed saw held taut in a frame, made for cutting metal", "Hacksaw", ["Coping saw", "Tenon saw", "Pipe cutter"]),
 ("A sharp-edged blade you tap with a mallet to carve or shape wood", "Chisel", ["Rasp", "Spokeshave", "File"]),
 ("Pushed along a plank to shave off thin curls and leave it smooth and flat", "Plane", ["Rasp", "File", "Belt sander"]),
 ("A sheet with a gritty surface, graded by numbers like 80 or 240", "Sandpaper", ["Wire brush", "Scraper", "Grout float"]),
 ("A coiled metal strip that springs back into its case", "Tape measure", ["Stud finder", "Set square", "Plumb bob"]),
 ("An L-shaped hexagonal bar that comes free with flat-pack furniture", "Allen key", ["Socket set", "Torque wrench", "Countersink"]),
 ("Bolted to a workbench, its jaws hold your work tight while you saw", "Vice", ["Mitre box", "Lathe", "Router"]),
 ("A long iron bar with a flattened end for prising things open", "Crowbar", ["Scraper", "Nail punch", "Torque wrench"]),
 ("A small pointed tool for making a starter hole for a screw", "Bradawl", ["Nail punch", "Hole saw", "Countersink"]),
 ("Heats up to melt metal and join electrical wires", "Soldering iron", ["Heat gun", "Glue gun", "Angle grinder"]),
 ("Fires metal staples into wood to fix fabric or cables", "Staple gun", ["Glue gun", "Caulking gun", "Nail punch"]),
 ("A power saw with a thin up-and-down blade for cutting curves", "Jigsaw", ["Angle grinder", "Router", "Belt sander"]),
 ("A fluffy cylinder on a handle for covering walls quickly", "Paint roller", ["Scraper", "Grout float", "Wire brush"]),
 ("A flat pointed blade for spreading mortar when laying bricks", "Trowel", ["Grout float", "Scraper", "Tile cutter"])])

race("which part of a castle is this?", "History", "medium", ["castles", "medieval", "architecture"], [
 ("A water-filled ditch dug around the walls", "Moat", ["Glacis", "Ravelin", "Bastion"]),
 ("Raised on chains so nobody can cross the ditch", "Drawbridge", ["Lych gate", "Sally port", "Casemate"]),
 ("A heavy iron-tipped grille that drops down to seal the gateway", "Portcullis", ["Lych gate", "Casemate", "Bastion"]),
 ("The strongest tower at the heart of the castle, the last place to hold out", "Keep", ["Belfry", "Bastion", "Casemate"]),
 ("Notched walls along the top that defenders shoot through", "Battlements", ["Buttress", "Pinnacle", "Belfry"]),
 ("A narrow gap in the wall for archers to fire from", "Arrow slit", ["Lancet window", "Rose window", "Squint"]),
 ("Openings in the gatehouse ceiling for dropping stones on attackers", "Murder holes", ["Squint", "Rose window", "Undercroft"]),
 ("The open courtyard inside the castle walls", "Bailey", ["Cloister", "Nave", "Undercroft"]),
 ("The man-made earth mound a Norman wooden tower stood on", "Motte", ["Glacis", "Barrow", "Ravelin"]),
 ("The fortified entrance building guarding the castle gate", "Gatehouse", ["Lych gate", "Belfry", "Vestry"]),
 ("An underground prison cell", "Dungeon", ["Crypt", "Undercroft", "Larder"]),
 ("The main room where the lord ate, entertained and held court", "Great hall", ["Nave", "Chancel", "Buttery"]),
 ("The outer defensive wall linking the towers", "Curtain wall", ["Buttress", "Ha-ha", "Glacis"]),
 ("An extra fortified gateway built out in front of the main gate", "Barbican", ["Lych gate", "Casemate", "Belfry"]),
 ("A medieval toilet that emptied down the outside wall", "Garderobe", ["Buttery", "Scullery", "Vestry"]),
 ("A small back gate for slipping in and out unseen", "Postern", ["Lych gate", "Squint", "Casemate"]),
 ("Stonework jutting out at the top of the wall, with holes for dropping things on attackers", "Machicolations", ["Gargoyle", "Buttress", "Pinnacle"]),
 ("A small tower sticking out from the corner of a bigger tower or wall", "Turret", ["Spire", "Belfry", "Pinnacle"]),
 ("The lord and lady's private upstairs room, away from the noise of the hall", "Solar", ["Buttery", "Vestry", "Scullery"]),
 ("A balcony above the hall where musicians played during feasts", "Minstrels' gallery", ["Belfry", "Squint", "Chancel"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-125.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
