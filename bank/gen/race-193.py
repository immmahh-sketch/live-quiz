# Bank session 11 Oct 2026: 3 more general races -> bank/race-193.json (shoe, singing and caravan words). 20 rows each, target 10; wrong options are
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

race("what's this shoe word?", "Fashion", "medium", ["shoes", "fashion", "words"], [
 ("A very high, very thin heel", "Stiletto", ["Cuban heel", "Block heel", "Cowboy heel"]),
 ("A heel that's solid all the way along the sole", "Wedge", ["Block heel", "Cuban heel", "Spike"]),
 ("A short, slim heel", "Kitten heel", ["Puppy heel", "Block heel", "Cuban heel"]),
 ("A leather shoe with decorative punched holes", "Brogue", ["Mule", "Slipper", "Galosh"]),
 ("A slip-on leather shoe with no laces", "Loafer", ["Lounger", "Slacker", "Drifter"]),
 ("The simple canvas PE shoe", "Plimsoll", ["Galosh", "Sabot", "Mule"]),
 ("A canvas shoe with a rope sole", "Espadrille", ["Espresso", "Esplanade", "Escapade"]),
 ("A Dutch wooden shoe", "Clog", ["Mule", "Slipper", "Moccasin"]),
 ("Air-cushioned boots with yellow stitching", "Doc Martens", ["Timberlands", "Hush Puppies", "Kickers"]),
 ("Rubber boots named after a duke", "Wellies", ["Marlboroughs", "Nelsons", "Napoleons"]),
 ("Someone who mends shoes", "Cobbler", ["Cooper", "Chandler", "Fletcher"]),
 ("The padded layer inside the shoe", "Insole", ["Outsole", "Upper", "Welt"]),
 ("The little hole a lace goes through", "Eyelet", ["Toecap", "Tongue", "Heel tab"]),
 ("The plastic tip on a shoelace", "Aglet", ["Ferrule", "Nib", "Rivet"]),
 ("The curved tool that eases your heel in", "Shoehorn", ["Shoetree", "Shoe brush", "Horn of plenty"]),
 ("A shoe with a very thick sole", "Platform", ["Plinth", "Pedestal", "Podium"]),
 ("Rubber sandals with a post between the toes", "Flip-flops", ["Sliders", "Jellies", "Gladiators"]),
 ("An ankle boot with stretchy side panels", "Chelsea boot", ["Desert boot", "Cowboy boot", "Ugg boot"]),
 ("Chunky foam clogs full of holes", "Crocs", ["Vans", "Birkenstocks", "Converse"]),
 ("The underneath of a shoe", "Sole", ["Upper", "Heel tab", "Vamp"])])

race("what's this singing word?", "Music", "medium", ["singing", "voices", "words"], [
 ("The highest female voice", "Soprano", ["Treble", "Baritone", "Mezzo"]),
 ("The lower female voice", "Alto", ["Baritone", "Treble", "Countertenor"]),
 ("The highest everyday male voice", "Tenor", ["Baritone", "Treble", "Mezzo"]),
 ("The deepest male voice", "Bass", ["Baritone", "Treble", "Mezzo"]),
 ("Singing above your natural range, like the Bee Gees", "Falsetto", ["Staccato", "Legato", "Crescendo"]),
 ("A rapid wobble on a held note", "Vibrato", ["Staccato", "Legato", "Crescendo"]),
 ("Singing with no instruments at all", "A cappella", ["Al fresco", "À la carte", "Al dente"]),
 ("Different notes sung together that blend", "Harmony", ["Melody", "Rhythm", "Tempo"]),
 ("A higher tune sung over the top of a hymn", "Descant", ["Decant", "Discount", "Descent"]),
 ("Singing along to backing tracks, a craze from Japan", "Karaoke", ["Origami", "Kimono", "Sudoku"]),
 ("Miming to a recording", "Lip-sync", ["Lip-read", "Lip gloss", "Lip service"]),
 ("Eight notes up from where you started", "Octave", ["Octopus", "Octagon", "Octet"]),
 ("A grand, demanding star singer", "Diva", ["Diver", "Divan", "Dove"]),
 ("A gentle song to send a baby to sleep", "Lullaby", ["Lollipop", "Lollygag", "Hullabaloo"]),
 ("Alpine singing that flips between chest and head voice", "Yodel", ["Yo-yo", "Yokel", "Yonder"]),
 ("Making drum sounds with your mouth", "Beatbox", ["Jukebox", "Soapbox", "Beatnik"]),
 ("Software that fixes off-key singing", "Auto-Tune", ["Autopilot", "Autocorrect", "Autoplay"]),
 ("A song for two singers", "Duet", ["Duel", "Duvet", "Trio"]),
 ("A group of people singing together", "Choir", ["Squire", "Chore", "Coir"]),
 ("The repeated bit everyone joins in on", "Chorus", ["Verse", "Bridge", "Intro"])])

race("what's this caravan word?", "Travel", "medium", ["caravans", "motorhomes", "words"], [
 ("The tent that fixes to the side", "Awning", ["Gazebo", "Marquee", "Yurt"]),
 ("Fitted to the car so it can pull the caravan", "Tow bar", ["Roof rack", "Tow rope", "Bull bar"]),
 ("Coupling the caravan to the car", "Hitch", ["Latch", "Clinch", "Splice"]),
 ("The small front wheel for moving it by hand", "Jockey wheel", ["Steering wheel", "Cartwheel", "Big wheel"]),
 ("Wind-down legs that stop it rocking", "Corner steadies", ["Stabilisers", "Outriggers", "Stilts"]),
 ("One that stays put on a holiday park", "Static caravan", ["Fifth-wheel caravan", "Folding caravan", "Teardrop caravan"]),
 ("A caravan you tow from site to site", "Touring caravan", ["Houseboat", "Narrowboat", "Chalet"]),
 ("Engine and living quarters in one big vehicle", "Motorhome", ["Horsebox", "Minibus", "Hearse"]),
 ("A smaller van conversion, like a VW", "Campervan", ["Horsebox", "Ice cream van", "Transit"]),
 ("The plot on the site where you park up", "Pitch", ["Patch", "Pier", "Pen"]),
 ("Plugging into the site's mains electricity", "Hook-up", ["Hookah", "Hook line", "Pick-up"]),
 ("The loo you empty at the disposal point", "Chemical toilet", ["Compost heap", "Pit stop", "Bidet"]),
 ("Runs the lights when you're not plugged in", "Leisure battery", ["Car battery", "Battery hen", "Assault and battery"]),
 ("The barrel-shaped water carrier you roll along", "Aquaroll", ["Aqualung", "Swiss roll", "Aquarium"]),
 ("Waste water from the sink and shower", "Grey water", ["Black water", "Fresh water", "Holy water"]),
 ("Luxury camping in yurts and pods", "Glamping", ["Clamping", "Vamping", "Tramping"]),
 ("Pitching up miles from any official site", "Wild camping", ["Wild card", "Wildlife", "Wild goose chase"]),
 ("A gravel or concrete pitch", "Hardstanding", ["Grandstand", "Bandstand", "Understanding"]),
 ("A campervan roof that lifts up for headroom", "Pop-top", ["Sunroof", "Soft top", "Hard top"]),
 ("Extra-wide mirrors so you can see past the caravan", "Towing mirrors", ["Rear-view mirror", "Vanity mirror", "Mirror ball"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-193.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
