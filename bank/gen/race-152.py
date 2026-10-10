# Bank session 11 Oct 2026: 3 more general races -> bank/race-152.json (magic words, church words, shopping words). 20 rows each, target 10; wrong options are
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

race("what's this magic word?", "Entertainment", "medium", ["magic", "magicians", "words"], [
 ("The stick a magician waves", "Wand", ["Baton", "Cane", "Sceptre"]),
 ("The classic magic word", "Abracadabra", ["Eureka", "Bingo", "Geronimo"]),
 ("Quick, skilful finger work that fools the eye", "Sleight of hand", ["Mind reading", "Escapology", "Ventriloquism"]),
 ("A performer who wriggles free from chains and locked boxes, like Houdini", "Escapologist", ["Ventriloquist", "Juggler", "Contortionist"]),
 ("The animal pulled out of a hat", "Rabbit", ["Ferret", "Guinea pig", "Hamster"]),
 ("The tall black hat the rabbit comes out of", "Top hat", ["Bowler", "Trilby", "Fez"]),
 ("The person in the sequins who gets sawn in half", "Assistant", ["Usher", "Compère", "Stagehand"]),
 ("Making someone appear to float in mid-air", "Levitation", ["Teleportation", "Hypnosis", "Telepathy"]),
 ("The famous London society of magicians, sworn to secrecy", "Magic Circle", ["Round Table", "Silver Circle", "Inner Temple"]),
 ("Drawing the audience's eyes away from what really matters", "Misdirection", ["Mesmerism", "Hypnosis", "Telekinesis"]),
 ("An audience member secretly in on the trick", "Plant", ["Mark", "Punter", "Heckler"]),
 ("Tricks done at the table, right under your nose", "Close-up magic", ["Stage illusion", "Street theatre", "Pantomime"]),
 ("Mind-reading tricks, the kind Derren Brown does", "Mentalism", ["Spiritualism", "Hypnotherapy", "Escapology"]),
 ("The escape artist who died on Halloween 1926", "Houdini", ["David Blaine", "David Copperfield", "Uri Geller"]),
 ("The Bradford magician who walked across the Thames", "Dynamo", ["Derren Brown", "David Blaine", "Penn Jillette"]),
 ("'You'll like this... not a lot' was his catchphrase", "Paul Daniels", ["Derren Brown", "Uri Geller", "David Copperfield"]),
 ("The comic magician in a fez whose tricks always 'went wrong'", "Tommy Cooper", ["Les Dawson", "Eric Morecambe", "Frankie Howerd"]),
 ("The classic stage illusion with a long box and a big saw", "Sawing in half", ["Zig Zag Girl", "Metamorphosis", "Floating lady"]),
 ("Shuffling a deck so it looks random but stays in order", "False shuffle", ["Riffle shuffle", "Overhand shuffle", "Dovetail"]),
 ("The chat a magician keeps up during a trick", "Patter", ["Encore", "Finale", "Prologue"])])

race("what's this church word?", "Religion", "medium", ["churches", "Christianity", "words"], [
 ("The holy table at the east end, where communion is prepared", "Altar", ["Dais", "Plinth", "Trestle"]),
 ("The raised box the vicar preaches the sermon from", "Pulpit", ["Podium", "Rostrum", "Soapbox"]),
 ("The stone basin used for christenings", "Font", ["Trough", "Cistern", "Urn"]),
 ("The long wooden bench the congregation sits on", "Pew", ["Ottoman", "Chaise", "Futon"]),
 ("The main central part of the church, where the congregation sits", "Nave", ["Foyer", "Atrium", "Lobby"]),
 ("The tall, pointed top of the tower", "Spire", ["Dome", "Minaret", "Turret"]),
 ("The room where the vicar changes into robes", "Vestry", ["Pantry", "Scullery", "Larder"]),
 ("The underground chamber, often used for burials", "Crypt", ["Cellar", "Bunker", "Dungeon"]),
 ("The stand, often shaped like an eagle, that holds the Bible for readings", "Lectern", ["Easel", "Trestle", "Plinth"]),
 ("Where the bells hang", "Belfry", ["Loft", "Attic", "Hayloft"]),
 ("The roofed gateway into the churchyard", "Lychgate", ["Portcullis", "Turnstile", "Stile"]),
 ("The church caretaker who leads processions, carrying a rod", "Verger", ["Bailiff", "Steward", "Porter"]),
 ("A song of praise sung by the whole congregation", "Hymn", ["Aria", "Ballad", "Shanty"]),
 ("The group of singers in robes", "Choir", ["Orchestra", "Quartet", "Brass band"]),
 ("The 'arms' of a cross-shaped church", "Transept", ["Annexe", "Porch", "Conservatory"]),
 ("Coloured windows showing Bible scenes", "Stained glass", ["Frosted glass", "Double glazing", "Mirror glass"]),
 ("The huge instrument with pipes", "Organ", ["Harp", "Piano", "Accordion"]),
 ("Read out on three Sundays before a wedding", "Banns", ["Vows", "Rites", "Writs"]),
 ("The clergyman or woman in charge of a Church of England parish", "Vicar", ["Abbot", "Cardinal", "Rabbi"]),
 ("Money gathered in a plate during the service", "Collection", ["Raffle", "Tombola", "Subscription"])])

race("what's this shopping word?", "Everyday life", "easy", ["shopping", "shops", "words"], [
 ("The slip of paper proving what you paid", "Receipt", ["Voucher", "Coupon", "Leaflet"]),
 ("The wheeled cage you push round the supermarket", "Trolley", ["Barrow", "Pram", "Buggy"]),
 ("Where you pay at the front of the shop", "Checkout", ["Stockroom", "Loading bay", "Mezzanine"]),
 ("The walkway between rows of shelves", "Aisle", ["Lobby", "Foyer", "Stockroom"]),
 ("Where you try clothes on before buying", "Fitting room", ["Cloakroom", "Green room", "Staffroom"]),
 ("Something bought for much less than it's worth", "Bargain", ["Rip-off", "Mark-up", "Surcharge"]),
 ("Getting your money back when you return something", "Refund", ["Deposit", "Tip", "Surcharge"]),
 ("Collect points on it, like a Clubcard or Nectar", "Loyalty card", ["Debit card", "Gift card", "Railcard"]),
 ("The black stripes scanned at the till", "Barcode", ["Watermark", "Hologram", "Postcode"]),
 ("A sturdy carrier bag you use again and again", "Bag for life", ["Doggy bag", "Goody bag", "Bin bag"]),
 ("Looking at the goods with no plan to buy", "Window shopping", ["Panic buying", "Bulk buying", "Late-night shopping"]),
 ("'Buy one, get one free', in four letters", "BOGOF", ["RRP", "VAT", "PAYG"]),
 ("Scanning and bagging your own shopping", "Self-checkout", ["Cash machine", "Ticket machine", "Parking meter"]),
 ("Order online, pick it up from the shop", "Click and collect", ["Cash and carry", "Home delivery", "Mail order"]),
 ("Stealing goods from a shop", "Shoplifting", ["Pickpocketing", "Burglary", "Fraud"]),
 ("The late-November day of big American-style sales", "Black Friday", ["Boxing Day", "Cyber Monday", "Shrove Tuesday"]),
 ("Getting money out at the till as you pay", "Cashback", ["Overdraft", "Interest", "Dividend"]),
 ("The American word for a big indoor shopping centre", "Mall", ["Precinct", "Parade", "Arcade"]),
 ("What you carry for a small shop instead of a trolley", "Basket", ["Tray", "Crate", "Satchel"]),
 ("The little label showing what it costs", "Price tag", ["Name badge", "Luggage label", "Gift tag"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-152.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
