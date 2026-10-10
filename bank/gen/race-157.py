# Bank session 11 Oct 2026: 3 more general races -> bank/race-157.json (photography, knights and navy words). 20 rows each, target 10; wrong options are
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

race("what's this photography word?", "Art", "medium", ["photography", "cameras", "words"], [
 ("The curved glass at the front of the camera", "Lens", ["Prism", "Monocle", "Pane"]),
 ("Snaps open and shut to let the light in", "Shutter", ["Hatch", "Valve", "Lid"]),
 ("A burst of light for dark rooms", "Flash", ["Glare", "Beam", "Spark"]),
 ("A three-legged camera stand", "Tripod", ["Monopod", "Easel", "Lectern"]),
 ("A photo you take of yourself", "Selfie", ["Snapshot", "Mugshot", "Headshot"]),
 ("The instant camera whose prints develop in your hand", "Polaroid", ["Brownie", "Box Brownie", "Kodachrome"]),
 ("The film image with dark and light swapped round", "Negative", ["Print", "Proof", "Slide"]),
 ("Where film is developed under a red light", "Darkroom", ["Green room", "Back room", "Box room"]),
 ("The lens that brings faraway things closer", "Zoom", ["Fisheye", "Macro", "Wide-angle"]),
 ("Glowing pupils caused by the flash", "Red-eye", ["Pink eye", "Black eye", "Lazy eye"]),
 ("A very wide photo of a whole view", "Panorama", ["Diorama", "Collage", "Montage"]),
 ("A tiny dot that makes up a digital image", "Pixel", ["Grain", "Speck", "Byte"]),
 ("Making the picture sharp, not blurry", "Focus", ["Contrast", "Saturation", "Filter"]),
 ("How much light reaches the film or sensor", "Exposure", ["Contrast", "Saturation", "Sharpness"]),
 ("Popping up uninvited in someone else's picture", "Photobomb", ["Photo finish", "Photocopy", "Photofit"]),
 ("The upright picture shape, taller than it's wide", "Portrait", ["Square", "Widescreen", "Letterbox"]),
 ("The picture shape that's wider than it's tall", "Landscape", ["Square", "Upright", "Letterbox"]),
 ("A darkened room that projects an image through a pinhole, centuries before film", "Camera obscura", ["Magic lantern", "Kaleidoscope", "Periscope"]),
 ("Photographers who chase celebrities", "Paparazzi", ["Pundits", "Groupies", "Roadies"]),
 ("Touching up a photo to hide the flaws", "Airbrush", ["Watermark", "Crop", "Caption"])])

race("what's this knight word?", "History", "medium", ["knights", "medieval", "words"], [
 ("A knight's young assistant, training to be a knight", "Squire", ["Herald", "Steward", "Jester"]),
 ("A boy of about seven, just starting knight training", "Page", ["Herald", "Steward", "Jester"]),
 ("Two knights charging at each other with lances", "Joust", ["Fencing", "Duel", "Archery"]),
 ("The long pole a knight charges with", "Lance", ["Pike", "Halberd", "Javelin"]),
 ("Armour made of linked metal rings", "Chain mail", ["Plate armour", "Brigandine", "Gambeson"]),
 ("The hinged part of a helmet that covers the face", "Visor", ["Gorget", "Breastplate", "Pauldron"]),
 ("An armoured glove", "Gauntlet", ["Vambrace", "Greave", "Pauldron"]),
 ("The design on a knight's shield showing his family", "Coat of arms", ["Family tree", "Hallmark", "Monogram"]),
 ("To make someone a knight with a tap of the sword", "Dub", ["Crown", "Anoint", "Ordain"]),
 ("The knightly code of honour and good manners", "Chivalry", ["Heraldry", "Fealty", "Piety"]),
 ("The system of land given in return for loyalty and service", "Feudalism", ["Capitalism", "Socialism", "Monarchy"]),
 ("A peasant tied to the lord's land", "Serf", ["Yeoman", "Freeman", "Burgher"]),
 ("The water-filled ditch around a castle", "Moat", ["Motte", "Bailey", "Keep"]),
 ("Surrounding a castle to starve it out", "Siege", ["Raid", "Ambush", "Skirmish"]),
 ("The giant catapult swung by a counterweight", "Trebuchet", ["Ballista", "Mangonel", "Battering ram"]),
 ("A holy war fought over the Holy Land", "Crusade", ["Pilgrimage", "Odyssey", "Exodus"]),
 ("King Arthur's sword", "Excalibur", ["Durendal", "Glamdring", "Andúril"]),
 ("Where Arthur's knights sat as equals", "Round Table", ["High Table", "Top Table", "Card table"]),
 ("In the old stories, the young woman in distress", "Damsel", ["Wench", "Dowager", "Matron"]),
 ("A knight's horse, in poetic language", "Steed", ["Mule", "Donkey", "Pony"])])

race("what's this navy word?", "History", "medium", ["Royal Navy", "ships", "words"], [
 ("The highest naval rank", "Admiral", ["Commodore", "Commander", "Captain"]),
 ("The warship that travels under the water", "Submarine", ["Frigate", "Corvette", "Minesweeper"]),
 ("A floating airfield", "Aircraft carrier", ["Frigate", "Corvette", "Tanker"]),
 ("The tube for seeing above the surface from a submarine", "Periscope", ["Telescope", "Kaleidoscope", "Stethoscope"]),
 ("An underwater missile", "Torpedo", ["Depth charge", "Mortar", "Grenade"]),
 ("The daily 'tot' sailors got until 1970", "Rum ration", ["Ale ration", "Gin ration", "Brandy ration"]),
 ("The old nickname for a British sailor", "Jack Tar", ["Tommy", "Jerry", "Yank"]),
 ("The flared trousers sailors wore", "Bell-bottoms", ["Plus-fours", "Jodhpurs", "Drainpipes"]),
 ("The ship's kitchen", "Galley", ["Pantry", "Scullery", "Larder"]),
 ("The ship's jail", "Brig", ["Hold", "Bilge", "Hatch"]),
 ("The sailors' hanging bed", "Hammock", ["Futon", "Divan", "Four-poster"]),
 ("Nelson's final battle, in 1805", "Trafalgar", ["Jutland", "Copenhagen", "The Nile"]),
 ("Nelson's flagship, now kept at Portsmouth", "HMS Victory", ["HMS Belfast", "Cutty Sark", "HMS Warrior"]),
 ("Henry VIII's warship, raised from the Solent in 1982", "Mary Rose", ["Golden Hind", "Endeavour", "Beagle"]),
 ("The navy's commando soldiers", "Royal Marines", ["Royal Engineers", "Royal Signals", "Paras"]),
 ("The 1906 battleship that made every other warship out of date", "Dreadnought", ["Leviathan", "Juggernaut", "Behemoth"]),
 ("Merchant ships sailing together under naval escort", "Convoy", ["Regatta", "Armada", "Cortège"]),
 ("Sailors rising up against their captain", "Mutiny", ["Desertion", "Treason", "Sabotage"]),
 ("The ship of Captain Bligh's famous mutiny", "Bounty", ["Endeavour", "Beagle", "Discovery"]),
 ("The professional head of the Royal Navy: First ___", "Sea Lord", ["Mate", "Officer", "Lieutenant"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-157.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
