# Bank session 10 Oct 2026: 4 more general races -> bank/race-25.json. 20 rows each, target 10; wrong options are
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

race("name the Doctor Who baddie", "Doctor Who", "hard", ["Doctor Who", "villains"], [
 ("'Exterminate!'", "The Daleks", ["The Toclafane", "The Krotons", "The Ogrons"]), ("'You will be upgraded. Delete!'", "The Cybermen", ["The Krotons", "The Toclafane", "The Axons"]),
 ("Statues that move when you blink", "The Weeping Angels", ["The Whisper Men", "The Boneless", "The Mire"]), ("Potato-headed clone warriors", "The Sontarans", ["The Ogrons", "The Draconians", "The Rutans"]),
 ("Tentacle-faced servants who carry their brains", "The Ood", ["The Hath", "The Sycorax", "The Racnoss"]), ("The Doctor's Time Lord arch-nemesis", "The Master", ["Omega", "Rassilon", "The Toymaker"]),
 ("Living shop-window dummies", "The Autons", ["The Krotons", "The Kandyman", "The Mire"]), ("Shape-shifters with suckers who hide in Loch Ness", "The Zygons", ["The Axons", "The Krillitanes", "The Macra"]),
 ("Cute little creatures made of body fat", "The Adipose", ["The Abzorbaloff", "The Pyroviles", "The Hath"]), ("Lizard people who lived on Earth before us", "The Silurians", ["The Draconians", "The Ogrons", "The Krotons"]),
 ("Aliens you forget the moment you look away", "The Silence", ["The Whisper Men", "The Boneless", "The Mire"]), ("Flesh-eating shadows in the Library", "The Vashta Nerada", ["The Boneless", "The Whisper Men", "The Mara"]),
 ("Turtle-like sea creatures, cousins of the Silurians", "The Sea Devils", ["The Macra", "The Axons", "The Draconians"]), ("Aliens who zip themselves into human skins", "The Slitheen", ["The Abzorbaloff", "The Sycorax", "The Hath"]),
 ("Rhino-headed space police", "The Judoon", ["The Ogrons", "The Sycorax", "The Krotons"]), ("Hissing armoured warriors from Mars", "The Ice Warriors", ["The Draconians", "The Sycorax", "The Rutans"]),
 ("The villain behind the snowmen and the Yeti", "The Great Intelligence", ["The Mara", "Sutekh", "The Toymaker"]), ("The scarred creator of the Daleks", "Davros", ["Omega", "Rassilon", "Sutekh"]),
 ("The renegade Time Lady scientist of the 1980s", "The Rani", ["Omega", "Romana", "Rassilon"]), ("The Master's later female incarnation", "Missy", ["Romana", "Rassilon", "Omega"])])

race("which country is this chocolate maker from?", "Food and drink", "hard", ["chocolate", "countries"], [
 ("Lindt", "Switzerland", ["Luxembourg", "Liechtenstein", "Ireland"]), ("Godiva", "Belgium", ["Luxembourg", "Ireland", "Iceland"]),
 ("Hershey's", "the USA", ["Canada", "Mexico", "Ireland"]), ("Cadbury", "England", ["Ireland", "Wales", "Iceland"]),
 ("Ritter Sport", "Germany", ["Luxembourg", "Liechtenstein", "Slovakia"]), ("Marabou", "Sweden", ["Iceland", "Estonia", "Latvia"]),
 ("Fazer", "Finland", ["Estonia", "Latvia", "Iceland"]), ("Freia", "Norway", ["Iceland", "Estonia", "Ireland"]),
 ("Ferrero", "Italy", ["Spain", "Portugal", "Greece"]), ("Meiji", "Japan", ["South Korea", "Taiwan", "China"]),
 ("Whittaker's", "New Zealand", ["Ireland", "South Africa", "Canada"]), ("Tony's Chocolonely", "the Netherlands", ["Luxembourg", "Ireland", "Iceland"]),
 ("Valrhona", "France", ["Spain", "Luxembourg", "Ireland"]), ("Anthon Berg", "Denmark", ["Iceland", "Estonia", "Latvia"]),
 ("Mirabell, makers of Mozartkugeln", "Austria", ["Liechtenstein", "Hungary", "Slovakia"]), ("E. Wedel", "Poland", ["Lithuania", "Slovakia", "Hungary"]),
 ("Orion", "Czechia", ["Slovakia", "Hungary", "Slovenia"]), ("Haigh's", "Australia", ["South Africa", "Canada", "Ireland"]),
 ("Kraš", "Croatia", ["Slovenia", "Serbia", "Montenegro"]), ("Tunnock's", "Scotland", ["Ireland", "Wales", "Northern Ireland"])])

race("which TV cook is this?", "Food and drink", "medium", ["TV cooks", "chefs"], [
 ("The Naked Chef", "Jamie Oliver", ["Tom Kerridge", "Gary Rhodes", "Brian Turner"]), ("The sweary star of Kitchen Nightmares", "Gordon Ramsay", ["Marco Pierre White", "Michel Roux Jr", "Gary Rhodes"]),
 ("River Cottage", "Hugh Fearnley-Whittingstall", ["Tom Kerridge", "Antony Worrall Thompson", "Phil Vickery"]), ("Host of Saturday Kitchen from 2006 to 2016", "James Martin", ["Antony Worrall Thompson", "Brian Turner", "Phil Vickery"]),
 ("The Galloping Gourmet", "Graham Kerr", ["Robert Carrier", "Philip Harben", "Clement Freud"]), ("How to Cook, and her famous Christmas", "Delia Smith", ["Clarissa Dickson Wright", "Jennifer Paterson", "Madhur Jaffrey"]),
 ("Padstow's seafood chef", "Rick Stein", ["Paul Ainsworth", "Tom Kerridge", "Brian Turner"]), ("The wine-swigging 1980s cook in a bow tie", "Keith Floyd", ["Clement Freud", "Robert Carrier", "Philip Harben"]),
 ("The 'domestic goddess'", "Nigella Lawson", ["Lorraine Pascale", "Rachel Khoo", "Clarissa Dickson Wright"]), ("The Fat Duck's scientist chef", "Heston Blumenthal", ["Michel Roux Jr", "Marco Pierre White", "Tom Kerridge"]),
 ("Ready Steady Cook's longest-serving host", "Ainsley Harriott", ["Brian Turner", "Fern Britton", "Phil Vickery"]), ("MasterChef's first presenter", "Loyd Grossman", ["Gregg Wallace", "John Torode", "Gary Rhodes"]),
 ("Bake Off's original judge in floral jackets", "Mary Berry", ["Paul Hollywood", "Lorraine Pascale", "Rachel Khoo"]), ("The 1950s TV cook in evening gowns, with husband Johnnie", "Fanny Cradock", ["Clarissa Dickson Wright", "Jennifer Paterson", "Marguerite Patten"]),
 ("The 2015 Bake Off winner who got her own cooking shows", "Nadiya Hussain", ["Lorraine Pascale", "Rachel Khoo", "Candice Brown"]), ("The Geordie half of the Hairy Bikers", "Si King", ["Dave Myers", "Tom Kerridge", "Paul Hollywood"]),
 ("The author of Toast and Real Fast Food", "Nigel Slater", ["Yotam Ottolenghi", "Gary Rhodes", "Brian Turner"]), ("The Bake Off judge who replaced Mary Berry", "Prue Leith", ["Paul Hollywood", "Lorraine Pascale", "Candice Brown"]),
 ("The chef behind Le Manoir aux Quat'Saisons", "Raymond Blanc", ["Michel Roux Jr", "Marco Pierre White", "Albert Roux"]), ("The 1980s BBC chef who made the wok famous", "Ken Hom", ["Madhur Jaffrey", "Ching-He Huang", "Yotam Ottolenghi"])])

race("which North East town is this landmark in?", "The North East", "hard", ["North East", "landmarks"], [
 ("Penshaw Monument", "Sunderland", ["Houghton-le-Spring", "Durham", "Peterlee"]), ("The Angel of the North", "Gateshead", ["Durham", "Wallsend", "Consett"]),
 ("The Transporter Bridge", "Middlesbrough", ["Billingham", "Guisborough", "Yarm"]), ("St Mary's Lighthouse", "Whitley Bay", ["Tynemouth", "Blyth", "North Shields"]),
 ("Grey's Monument", "Newcastle", ["Durham", "Wallsend", "North Shields"]), ("HMS Trincomalee", "Hartlepool", ["Billingham", "Peterlee", "Blyth"]),
 ("Locomotion, the railway museum", "Shildon", ["Newton Aycliffe", "Spennymoor", "Ferryhill"]), ("The Bowes Museum", "Barnard Castle", ["Hexham", "Durham", "Stanley"]),
 ("Washington Old Hall", "Washington", ["Houghton-le-Spring", "Durham", "Stanley"]), ("Arbeia Roman Fort", "South Shields", ["Tynemouth", "North Shields", "Wallsend"]),
 ("Preston Park Museum", "Stockton-on-Tees", ["Yarm", "Billingham", "Guisborough"]), ("Head of Steam railway museum", "Darlington", ["Newton Aycliffe", "Spennymoor", "Ferryhill"]),
 ("Bede's monastery and Jarrow Hall", "Jarrow", ["Wallsend", "Hebburn", "North Shields"]), ("Cragside", "Rothbury", ["Alnwick", "Morpeth", "Hexham"]),
 ("Woodhorn mining museum", "Ashington", ["Blyth", "Morpeth", "Cramlington"]), ("The 'Tommy' statue on the seafront", "Seaham", ["Peterlee", "Houghton-le-Spring", "Blyth"]),
 ("The Redcar Beacon", "Redcar", ["Guisborough", "Yarm", "Billingham"]), ("Lumley Castle", "Chester-le-Street", ["Durham", "Stanley", "Houghton-le-Spring"]),
 ("Gibside", "Rowlands Gill", ["Prudhoe", "Stanley", "Consett"]), ("Auckland Castle", "Bishop Auckland", ["Durham", "Spennymoor", "Newton Aycliffe"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-25.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
