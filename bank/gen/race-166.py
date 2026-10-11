# Bank session 11 Oct 2026: 3 more general races -> bank/race-166.json (butcher, climbing and florist words). 20 rows each, target 10; wrong options are
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

race("what's this butcher's word?", "Food and drink", "medium", ["butchers", "meat", "words"], [
 ("The prime beef cut from the lower back", "Sirloin", ["Shank", "Hock", "Scrag"]),
 ("Fatty beef from the chest, slow-cooked for hours", "Brisket", ["Shank", "Hock", "Scrag"]),
 ("The most tender, expensive steak", "Fillet", ["Shank", "Hock", "Scrag"]),
 ("Finely ground meat for burgers and bolognese", "Mince", ["Pâté", "Purée", "Paste"]),
 ("A cured ham steak from a pig's back leg", "Gammon", ["Venison", "Veal", "Oxtail"]),
 ("Meat from an older sheep", "Mutton", ["Lamb", "Venison", "Veal"]),
 ("Liver, kidneys and heart", "Offal", ["Giblets", "Gristle", "Suet"]),
 ("The fat from roast beef, spread on bread", "Dripping", ["Suet", "Lard", "Ghee"]),
 ("Crunchy roasted pork skin", "Crackling", ["Croutons", "Crisps", "Wafers"]),
 ("A sausage made with blood and oatmeal", "Black pudding", ["White pudding", "Haggis", "Faggot"]),
 ("The thick wooden chopping table", "Butcher's block", ["Breadboard", "Cheeseboard", "Draining board"]),
 ("The heavy square knife for chopping through bone", "Cleaver", ["Scalpel", "Machete", "Penknife"]),
 ("Beef hung in a cold room for weeks to deepen the flavour", "Dry-aged", ["Smoked", "Pickled", "Brined"]),
 ("Animals allowed to roam outdoors", "Free-range", ["Battery", "Intensive", "Factory-farmed"]),
 ("A large piece of meat for the Sunday roast", "Joint", ["Escalope", "Medallion", "Cutlet"]),
 ("A small cut of pork or lamb with the bone in", "Chop", ["Escalope", "Medallion", "Collop"]),
 ("A slice of bacon", "Rasher", ["Wafer", "Sliver", "Collop"]),
 ("Melton Mowbray's famous savoury", "Pork pie", ["Scotch egg", "Sausage roll", "Pasty"]),
 ("The long coiled sausage named after an English county", "Cumberland", ["Lincolnshire", "Toulouse", "Frankfurter"]),
 ("The blue-and-white striped thing a butcher wears", "Apron", ["Tabard", "Pinafore", "Smock"])])

race("what's this climbing word?", "Sport", "medium", ["climbing", "mountaineering", "words"], [
 ("Sliding down a rope on purpose", "Abseil", ["Bungee", "Zip line", "Freefall"]),
 ("Holding the rope to protect a climbing partner", "Belay", ["Tether", "Moor", "Hitch"]),
 ("A metal clip with a spring gate", "Carabiner", ["Shackle", "Buckle", "Toggle"]),
 ("Webbing worn round the waist and legs, clipped to the rope", "Harness", ["Corset", "Girdle", "Holster"]),
 ("White powder for dry, grippy hands", "Chalk", ["Talc", "Flour", "Resin"]),
 ("Climbing short walls with no rope, over crash mats", "Bouldering", ["Caving", "Coasteering", "Canyoning"]),
 ("Climbing alone with no rope at all", "Free solo", ["Free fall", "Freestyle", "Freehand"]),
 ("Spikes strapped to boots for the ice", "Crampons", ["Cleats", "Snowshoes", "Gaiters"]),
 ("The tool you swing into frozen slopes", "Ice axe", ["Tomahawk", "Machete", "Hatchet"]),
 ("Rock that leans out past vertical", "Overhang", ["Overpass", "Overcoat", "Overdraft"]),
 ("First climbed by Hillary and Tenzing in 1953", "Everest", ["K2", "Kilimanjaro", "Mont Blanc"]),
 ("Where an expedition sets up below the mountain", "Base camp", ["Boot camp", "Holiday camp", "Summer camp"]),
 ("The Himalayan people famous as mountain guides", "Sherpa", ["Inuit", "Maasai", "Bedouin"]),
 ("Headaches and sickness in thin mountain air", "Altitude sickness", ["Seasickness", "Travel sickness", "Morning sickness"]),
 ("A metal spike hammered into a crack", "Piton", ["Piston", "Python", "Pylon"]),
 ("The number or letter showing how hard a route is", "Grade", ["Rank", "Score", "Tier"]),
 ("The hardest move on a route", "Crux", ["Crutch", "Crust", "Crumb"]),
 ("A crack wide enough to wedge your whole body in", "Chimney", ["Funnel", "Tunnel", "Shaft"]),
 ("Kernmantle: a core inside a woven sheath", "Rope", ["Cable", "Chain", "Twine"]),
 ("Britain's highest peak, with a famous north face", "Ben Nevis", ["Snowdon", "Scafell Pike", "Helvellyn"])])

race("what's this florist word?", "Everyday life", "easy", ["flowers", "florists", "words"], [
 ("A bunch of flowers wrapped up to give", "Bouquet", ["Banquet", "Bucket", "Brochure"]),
 ("A ring of flowers for a funeral or a front door", "Wreath", ["Halo", "Hoop", "Bracelet"]),
 ("A small spray of flowers worn on a dress or wrist", "Corsage", ["Corset", "Cortège", "Collage"]),
 ("A single flower pinned to a groom's lapel", "Buttonhole", ["Cufflink", "Pocket square", "Tie pin"]),
 ("The container for cut flowers", "Vase", ["Urn", "Ewer", "Tankard"]),
 ("The green foam block that holds the stems in place", "Oasis", ["Blur", "Pulp", "Suede"]),
 ("The stalk of a flower", "Stem", ["Root", "Bark", "Trunk"]),
 ("The coloured, leaf-like part of a flower", "Petal", ["Bark", "Root", "Spore"]),
 ("The yellow dust that sets off hay fever", "Pollen", ["Spore", "Sap", "Resin"]),
 ("A sharp prickle on a rose", "Thorn", ["Splinter", "Needle", "Barb"]),
 ("A flower that hasn't opened yet", "Bud", ["Pod", "Seed", "Bulb"]),
 ("The classic Valentine's flowers", "Red roses", ["Lilies", "Carnations", "Daisies"]),
 ("Tiny blue flowers that stand for remembrance", "Forget-me-nots", ["Bluebells", "Cornflowers", "Violets"]),
 ("The red flower worn in November", "Poppy", ["Tulip", "Rose", "Carnation"]),
 ("The yellow flower of Wales and of Marie Curie", "Daffodil", ["Tulip", "Primrose", "Buttercup"]),
 ("The tall flower Van Gogh painted again and again", "Sunflower", ["Marigold", "Dandelion", "Chrysanthemum"]),
 ("Scissor-like snippers for stems", "Secateurs", ["Pliers", "Tweezers", "Tongs"]),
 ("A bowl of scented dried petals", "Pot pourri", ["Pot Noodle", "Pot luck", "Pot roast"]),
 ("Flowers carefully set out in a display", "Arrangement", ["Agreement", "Argument", "Settlement"]),
 ("Sending messages with flowers, as the Victorians did", "Floriography", ["Calligraphy", "Choreography", "Cartography"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-166.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
