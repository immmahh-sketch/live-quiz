# Bank session 11 Oct 2026: 3 more general races -> bank/race-176.json (library, museum and motorway words). 20 rows each, target 10; wrong options are
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

race("what's this library word?", "Books", "easy", ["libraries", "books", "words"], [
 ("The person who runs the library", "Librarian", ["Curator", "Usher", "Clerk"]),
 ("What lets you borrow the books", "Library card", ["Credit card", "Loyalty card", "Railcard"]),
 ("A book brought back late", "Overdue", ["Overdone", "Overdrawn", "Overtime"]),
 ("What you pay for a late book", "Fine", ["Toll", "Tip", "Deposit"]),
 ("The numbering system for sorting the books", "Dewey Decimal", ["Morse code", "Highway Code", "PIN code"]),
 ("Made-up stories", "Fiction", ["Diction", "Friction", "Faction"]),
 ("Books of facts", "Non-fiction", ["Nonsense", "Non-stop", "Nonentity"]),
 ("The edge of the book you see on the shelf", "Spine", ["Index", "Margin", "Flyleaf"]),
 ("The short description on the back cover", "Blurb", ["Burp", "Blob", "Bulb"]),
 ("A book with a stiff cover", "Hardback", ["Hardware", "Hardship", "Hard shoulder"]),
 ("A book with a soft cover", "Paperback", ["Paperweight", "Paper chase", "Paperwork"]),
 ("What the stereotypical librarian says", "Shh!", ["Boo!", "Oi!", "Ahem!"]),
 ("Books with bigger text", "Large print", ["Small print", "Fine print", "Footprint"]),
 ("A book read aloud as a recording", "Audiobook", ["Notebook", "Scrapbook", "Logbook"]),
 ("A book read on a screen", "E-book", ["E-mail", "E-number", "E-scooter"]),
 ("Books you can't take home, like encyclopedias", "Reference", ["Preference", "Conference", "Deference"]),
 ("The quiet room for study", "Reading room", ["Waiting room", "Boardroom", "Box room"]),
 ("The UK's national library, next to St Pancras", "British Library", ["Bodleian", "Ashmolean", "John Rylands"]),
 ("A book's 13-digit number, by its initials", "ISBN", ["PIN", "IBAN", "VIN"]),
 ("Someone who loves reading", "Bookworm", ["Earthworm", "Bookend", "Bookmaker"])])

race("what's this museum word?", "Art", "medium", ["museums", "galleries", "words"], [
 ("The person in charge of the collection", "Curator", ["Librarian", "Conductor", "Steward"]),
 ("An object on display", "Exhibit", ["Inhibit", "Prohibit", "Exit"]),
 ("Where you exit through, according to Banksy's film", "Gift shop", ["Café", "Cloakroom", "Ticket office"]),
 ("The glass box protecting the objects", "Display case", ["Pencil case", "Briefcase", "Suitcase"]),
 ("Ancient remains turned to stone", "Fossil", ["Pebble", "Crystal", "Geode"]),
 ("The Natural History Museum's famous diplodocus cast", "Dippy", ["Sue", "Stan", "Archie"]),
 ("The blue whale skeleton that replaced it in 2017", "Hope", ["Faith", "Charity", "Grace"]),
 ("Home of the Rosetta Stone", "British Museum", ["Science Museum", "National Gallery", "Imperial War Museum"]),
 ("The London museum of design, named after a royal couple, by its initials", "V&A", ["RA", "NPG", "BFI"]),
 ("The gallery in an old power station on the Thames", "Tate Modern", ["Tate Britain", "Saatchi Gallery", "Hayward Gallery"]),
 ("The Paris museum that's home to the Mona Lisa", "Louvre", ["Musée d'Orsay", "Prado", "Uffizi"]),
 ("The film where the exhibits come to life", "Night at the Museum", ["Night Shift", "Night Fever", "Night School"]),
 ("A headset telling you about each room", "Audio guide", ["Sat nav", "Walkie-talkie", "Hearing aid"]),
 ("An object made by people long ago", "Artefact", ["Artifice", "Artichoke", "Article"]),
 ("The base a statue stands on", "Plinth", ["Plank", "Plant", "Plunge"]),
 ("An old-fashioned room of odd collected objects", "Cabinet of curiosities", ["Cabinet reshuffle", "Kitchen cabinet", "Filing cabinet"]),
 ("The expert who repairs and preserves the objects", "Conservator", ["Conservative", "Conservatory", "Conversation"]),
 ("The price of getting into most UK national museums", "Free entry", ["Half price", "Peak fare", "Season ticket"]),
 ("The open-air museum of North East life, near Stanley", "Beamish", ["St Fagans", "Ironbridge", "Black Country Living Museum"]),
 ("The ancient Greek sculptures Greece wants returned", "Elgin Marbles", ["Venus de Milo", "Terracotta Army", "Winged Victory"])])

race("what's this motorway word?", "Travel", "medium", ["motorways", "driving", "words"], [
 ("The strip kept for breakdowns", "Hard shoulder", ["Cold shoulder", "Hard hat", "Hard line"]),
 ("The stop for fuel, food and toilets", "Services", ["Lay-by", "Roundabout", "Car park"]),
 ("Where you join or leave, numbered", "Junction", ["Function", "Unction", "Conjunction"]),
 ("The ramp onto the motorway", "Slip road", ["Slipway", "Side road", "Ring road"]),
 ("The barrier strip between the two carriageways", "Central reservation", ["Table reservation", "Hotel reservation", "Nature reserve"]),
 ("Reflective studs in the road", "Cat's eyes", ["Cat flap", "Cat's cradle", "Catwalk"]),
 ("A motorway that uses the hard shoulder as a lane at busy times", "Smart motorway", ["Smartphone", "Smart casual", "Smart meter"]),
 ("Britain's first full motorway, opened in 1959", "M1", ["M6", "M62", "A1"]),
 ("The orbital road round London", "M25", ["M4", "M40", "North Circular"]),
 ("Birmingham's famous tangle of flyovers", "Spaghetti Junction", ["Clapham Junction", "Scotch Corner", "Hanger Lane"]),
 ("The nickname for the outside lane", "Fast lane", ["Bus lane", "Memory lane", "Fast food"]),
 ("Driving far too close behind", "Tailgating", ["Tailspin", "Ponytail", "Tail end"]),
 ("The overhead frame holding the signs", "Gantry", ["Pantry", "Gantt chart", "Gangway"]),
 ("Changing limits shown on the overhead signs", "Variable speed limit", ["Speed date", "Speed camera", "Speedometer"]),
 ("The speed limit for cars on a motorway, in mph", "70", ["60", "80", "50"]),
 ("Traffic switched to the other side for roadworks", "Contraflow", ["Overflow", "Cash flow", "Workflow"]),
 ("Orange markers around the roadworks", "Cones", ["Buoys", "Kegs", "Funnels"]),
 ("Allowed on motorways with an instructor since 2018", "Learner drivers", ["Cyclists", "Horse riders", "Pedestrians"]),
 ("The fee to use the M6 ___", "Toll", ["Tax", "Ticket", "Tithe"]),
 ("Comes to tow your broken-down car", "Recovery truck", ["Ice cream van", "Milk float", "Hearse"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-176.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
