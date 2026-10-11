# Bank session 11 Oct 2026: 3 more general races -> bank/race-186.json (woodland, post office and sleep words). 20 rows each, target 10; wrong options are
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

race("what's this woodland word?", "Nature", "medium", ["woodland", "trees", "words"], [
 ("A young tree", "Sapling", ["Sprig", "Shrub", "Twig"]),
 ("The roof of leaves high above", "Canopy", ["Awning", "Thatch", "Dome"]),
 ("The oak's nut", "Acorn", ["Beechnut", "Cobnut", "Chestnut"]),
 ("The horse chestnut's shiny seed", "Conker", ["Marble", "Walnut", "Hazelnut"]),
 ("Cutting trees back to the base so they regrow", "Coppicing", ["Pollarding", "Grafting", "Thinning"]),
 ("What's left in the ground after a tree is felled", "Stump", ["Root", "Trunk", "Bough"]),
 ("A tree's protective outer skin", "Bark", ["Rind", "Husk", "Peel"]),
 ("The sugary fluid running inside a tree", "Sap", ["Nectar", "Syrup", "Pulp"]),
 ("Count these on a stump to tell the tree's age", "Rings", ["Knots", "Burrs", "Veins"]),
 ("Trees that drop their leaves in autumn", "Deciduous", ["Perennial", "Annual", "Hardy"]),
 ("Keeps its leaves all year round", "Evergreen", ["Perennial", "Hardy", "Annual"]),
 ("A tree with needles and cones", "Conifer", ["Broadleaf", "Palm", "Fern"]),
 ("The carpet of blue flowers in spring woods", "Bluebells", ["Violets", "Cornflowers", "Forget-me-nots"]),
 ("An open space in the middle of a wood", "Clearing", ["Thicket", "Hedgerow", "Spinney"]),
 ("A small group of trees", "Copse", ["Glade", "Heath", "Moor"]),
 ("Shrubs and plants growing beneath the trees", "Undergrowth", ["Overgrowth", "Outgrowth", "Ingrowth"]),
 ("A badger's underground home", "Sett", ["Drey", "Holt", "Form"]),
 ("The professional who climbs and cuts trees", "Tree surgeon", ["Steeplejack", "Thatcher", "Farrier"]),
 ("A mushroom-like fungus, often poisonous", "Toadstool", ["Puffball", "Truffle", "Lichen"]),
 ("The layer of dead leaves on the woodland floor", "Leaf litter", ["Compost", "Topsoil", "Peat"])])

race("what's this post office word?", "Lifestyle", "easy", ["post office", "Royal Mail", "words"], [
 ("Letters and numbers like NE1 4ST", "Postcode", ["Area code", "Pin code", "Grid reference"]),
 ("Stuck in the corner to pay for postage", "Stamp", ["Sticker", "Seal", "Label"]),
 ("The faster, dearer stamp", "First class", ["Second class", "Business class", "Express"]),
 ("The old service where someone signs to say it arrived", "Recorded delivery", ["Cash on delivery", "Same-day courier", "Standing order"]),
 ("The inky mark showing where and when it was posted", "Postmark", ["Watermark", "Hallmark", "Trademark"]),
 ("The red cylindrical postbox on the street", "Pillar box", ["Phone box", "Ballot box", "Signal box"]),
 ("The flap in your front door", "Letterbox", ["Cat flap", "Peephole", "Knocker"]),
 ("A numbered mailbox you rent at the post office", "PO Box", ["Safe deposit box", "Left luggage", "Locker room"]),
 ("Where mail is sorted, and where you fetch missed parcels", "Sorting office", ["Booking office", "Box office", "Ticket office"]),
 ("Slang for the person who brings your letters", "Postie", ["Bobby", "Milkie", "Sparky"]),
 ("Letters sent abroad by plane", "Airmail", ["Surface mail", "Junk mail", "Chain mail"]),
 ("Written on mail that can't be delivered", "Return to sender", ["Please forward", "Handle with care", "Do not bend"]),
 ("The company that delivers Britain's letters", "Royal Mail", ["Evri", "DPD", "Yodel"]),
 ("The world's first adhesive stamp, from 1840", "Penny Black", ["Penny Red", "Penny Farthing", "Black Adder"]),
 ("A money slip bought at the counter to send cash safely", "Postal order", ["Standing order", "Direct debit", "Money belt"]),
 ("The paper cover a letter goes in", "Envelope", ["Folder", "Wallet", "Sleeve"]),
 ("A padded envelope, by its famous brand name", "Jiffy bag", ["Bubble wrap", "Carrier bag", "Bum bag"]),
 ("The card left when you're out", "Sorry we missed you", ["Wish you were here", "Get well soon", "Back in five minutes"]),
 ("Printing postage by machine instead of using stamps", "Franking", ["Laminating", "Embossing", "Collating"]),
 ("The deadline for posting cards to arrive by Christmas", "Last posting date", ["Sell-by date", "Due date", "Best-before date"])])

race("what's this sleep word?", "Science", "easy", ["sleep", "bedtime", "words"], [
 ("Being unable to get to sleep", "Insomnia", ["Amnesia", "Narcolepsy", "Anaemia"]),
 ("Noisy breathing while asleep", "Snoring", ["Sneezing", "Hiccuping", "Wheezing"]),
 ("The dreaming stage of sleep, by its initials", "REM", ["RSI", "BMI", "ENT"]),
 ("An afternoon nap in Spain", "Siesta", ["Fiesta", "Tapas", "Paseo"]),
 ("Getting up and wandering about while asleep", "Sleepwalking", ["Moonwalking", "Daydreaming", "Fire walking"]),
 ("A frightening dream", "Nightmare", ["Nightcap", "Nightshade", "Nightingale"]),
 ("The quilted cover filled with feathers", "Duvet", ["Valance", "Throw", "Bolster"]),
 ("Tiredness after flying across time zones", "Jet lag", ["Hangover", "Burnout", "Cabin fever"]),
 ("Your inner 24-hour rhythm", "Body clock", ["Alarm clock", "Grandfather clock", "Stopwatch"]),
 ("Staying in bed late on a weekend morning", "Lie-in", ["Sit-in", "Stand-in", "Walk-in"]),
 ("Someone who stays up late", "Night owl", ["Dark horse", "Lone wolf", "Busy bee"]),
 ("Someone who's up at dawn", "Early bird", ["Dark horse", "Lone wolf", "Cold fish"]),
 ("A short sleep, in the old phrase", "Forty winks", ["Forty thieves", "Twenty questions", "Fifty-fifty"]),
 ("The hormone that makes you sleepy", "Melatonin", ["Adrenaline", "Insulin", "Testosterone"]),
 ("Breathing that stops and starts during sleep", "Sleep apnoea", ["Asthma", "Hay fever", "Vertigo"]),
 ("The classic trick for dropping off", "Counting sheep", ["Counting crows", "Counting cards", "Counting chickens"]),
 ("The wide-mouthed sign you're tired", "Yawn", ["Sigh", "Gasp", "Hiccup"]),
 ("The figure who sprinkles sleepy dust in your eyes", "Sandman", ["Bogeyman", "Tooth fairy", "Snowman"]),
 ("An animal's long winter sleep", "Hibernation", ["Migration", "Moulting", "Aestivation"]),
 ("Beds stacked one above the other", "Bunk beds", ["Sofa bed", "Camp bed", "Water bed"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-186.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
