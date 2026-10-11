# Bank session 11 Oct 2026: 3 more general races -> bank/race-172.json (vet, cruise and archery words). 20 rows each, target 10; wrong options are
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

race("what's this vet word?", "Animals", "medium", ["vets", "pets", "words"], [
 ("The operation so a pet can't have babies", "Neutering", ["Grooming", "Clipping", "Docking"]),
 ("A tiny tag under the skin with the owner's details", "Microchip", ["Barcode", "Name badge", "Tattoo"]),
 ("The yearly top-up vaccination", "Booster", ["Bonus", "Refill", "Rebate"]),
 ("The plastic collar that stops a pet licking its wound", "Cone", ["Muzzle", "Harness", "Halter"]),
 ("Tiny jumping pests in a pet's fur", "Fleas", ["Ants", "Gnats", "Moths"]),
 ("Tablets that clear out a pet's gut parasites", "Worming", ["Flossing", "Fumigating", "Bleaching"]),
 ("Neutering a female", "Spay", ["Snip", "Dock", "Crop"]),
 ("Assists the vet in surgery", "Veterinary nurse", ["Matron", "Midwife", "Orderly"]),
 ("Where dogs stay while their owners are away", "Kennel", ["Hutch", "Stable", "Coop"]),
 ("Where cats stay while their owners are away", "Cattery", ["Aviary", "Hutch", "Stable"]),
 ("The policy that pays the vet's bills", "Pet insurance", ["Life insurance", "Car insurance", "Travel insurance"]),
 ("A purebred with a recorded family tree", "Pedigree", ["Mongrel", "Crossbreed", "Stray"]),
 ("The deadly disease that once meant months of quarantine", "Rabies", ["Mange", "Kennel cough", "Hay fever"]),
 ("The document that lets your dog travel abroad", "Pet passport", ["Pet licence", "Boarding pass", "Dog tag"]),
 ("James ___, the Yorkshire vet of All Creatures Great and Small", "Herriot", ["Farnon", "Pumphrey", "Dalton"]),
 ("Noel Fitzpatrick's TV nickname", "Supervet", ["Supernanny", "Superdrug", "Superman"]),
 ("The vet's word for anything to do with horses", "Equine", ["Bovine", "Canine", "Feline"]),
 ("What the vet listens to the heart with", "Stethoscope", ["Telescope", "Periscope", "Kaleidoscope"]),
 ("Where pets and owners sit before being seen", "Waiting room", ["Green room", "Box room", "Boot room"]),
 ("Where the pet is weighed", "Scales", ["Abacus", "Sundial", "Barometer"])])

race("what's this cruise word?", "Travel", "medium", ["cruises", "ships", "words"], [
 ("Your bedroom on board", "Cabin", ["Chalet", "Dorm", "Lodge"]),
 ("One of the ship's floors", "Deck", ["Storey", "Landing", "Mezzanine"]),
 ("A small round window", "Porthole", ["Peephole", "Keyhole", "Pothole"]),
 ("The officer in overall command", "Captain", ["Admiral", "Pilot", "Bosun"]),
 ("The officer looking after money and passengers' affairs", "Purser", ["Bosun", "Galley chef", "Lookout"]),
 ("The front of the ship", "Bow", ["Keel", "Hull", "Mast"]),
 ("The back of the ship", "Stern", ["Keel", "Hull", "Mast"]),
 ("The left-hand side, facing forward", "Port", ["Aft", "Fore", "Abeam"]),
 ("The right-hand side, facing forward", "Starboard", ["Aft", "Fore", "Abeam"]),
 ("The safety practice before sailing", "Muster drill", ["Square bashing", "Roll call", "Dress rehearsal"]),
 ("The all-you-can-eat spread", "Buffet", ["Banquet", "Picnic", "Barbecue"]),
 ("A day trip off the ship at a port", "Shore excursion", ["Long weekend", "Staycation", "Sabbatical"]),
 ("To board the ship", "Embark", ["Disembark", "Debark", "Unpack"]),
 ("The walkway onto the ship", "Gangway", ["Runway", "Slipway", "Fairway"]),
 ("The 'unsinkable' liner of 1912", "Titanic", ["Lusitania", "Queen Mary", "Britannic"]),
 ("Cunard's transatlantic liner, launched in 2003", "Queen Mary 2", ["Queen Elizabeth 2", "Oceana", "Oasis of the Seas"]),
 ("The queasy feeling from the rolling waves", "Seasickness", ["Homesickness", "Altitude sickness", "Sleeping sickness"]),
 ("What a ship's speed is measured in", "Knots", ["Miles per hour", "Fathoms", "Leagues"]),
 ("A big passenger ship crossing the ocean", "Ocean liner", ["Freighter", "Trawler", "Tug"]),
 ("The package where all meals and drinks are covered", "All-inclusive", ["Self-catering", "Room only", "Half board"])])

race("what's this archery word?", "Sport", "medium", ["archery", "bows", "words"], [
 ("The centre of the target", "Bullseye", ["Outer", "Magpie", "Washer"]),
 ("The case holding the arrows", "Quiver", ["Scabbard", "Holster", "Sheath"]),
 ("The cord you draw back", "Bowstring", ["Shoelace", "Guitar string", "Washing line"]),
 ("The English weapon that won at Agincourt", "Longbow", ["Crossbow", "Slingshot", "Catapult"]),
 ("The feathers on the back of the arrow", "Fletching", ["Fledging", "Plucking", "Trimming"]),
 ("The old trade that made arrows", "Fletcher", ["Cooper", "Chandler", "Smith"]),
 ("The old trade that made bows", "Bowyer", ["Cooper", "Chandler", "Wheelwright"]),
 ("Split one arrow with another, in the legend", "Robin Hood", ["Little John", "Hiawatha", "Will Scarlet"]),
 ("Shot an apple off his son's head", "William Tell", ["Guy Fawkes", "Hereward", "Rob Roy"]),
 ("The winged archer of love", "Cupid", ["Mercury", "Apollo", "Pan"]),
 ("The archer of the zodiac", "Sagittarius", ["Taurus", "Aries", "Leo"]),
 ("The Olympic bow whose tips curl away from the archer", "Recurve", ["Compound", "Flatbow", "Slingbow"]),
 ("The pointed tip of an arrow", "Arrowhead", ["Spearhead", "Figurehead", "Arrowroot"]),
 ("What you shoot at, with its coloured rings", "Target", ["Dartboard", "Easel", "Gong"]),
 ("The colour of the inner rings", "Gold", ["Silver", "Green", "Purple"]),
 ("Pulling the string back", "Draw", ["Yank", "Tug", "Heave"]),
 ("The notch at the back of the arrow for the string", "Nock", ["Knock", "Knack", "Neck"]),
 ("Someone who shoots with a bow", "Archer", ["Gunner", "Lancer", "Bowler"]),
 ("The 1415 battle won by English archers", "Agincourt", ["Hastings", "Bosworth", "Culloden"]),
 ("The fancy word for a lover of archery", "Toxophilite", ["Bibliophile", "Audiophile", "Francophile"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-172.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
