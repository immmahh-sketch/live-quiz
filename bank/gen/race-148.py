# Bank session 10 Oct 2026: 3 more general races -> bank/race-148.json (pub words, pet words, computer words). 20 rows each, target 10; wrong options are
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

race("what's this pub word?", "Food and drink", "easy", ["pubs", "drinks", "words"], [
 ("The bell rung shortly before closing, your final chance to buy", "Last orders", ["Happy hour", "Nightcap", "Hair of the dog"]),
 ("Drinking on behind closed doors after hours", "Lock-in", ["Happy hour", "Open mic", "Meat raffle"]),
 ("Buying drinks for the whole group, then it's someone else's turn", "Round", ["Happy hour", "Nightcap", "Meat raffle"]),
 ("A small, cosy private room in a pub", "Snug", ["Saloon", "Cellar", "Hatch"]),
 ("Everyone chips into a pot of money that pays for the drinks", "Kitty", ["Meat raffle", "Tombola", "Happy hour"]),
 ("Beer mixed with lemonade", "Shandy", ["Black velvet", "Spritzer", "Boilermaker"]),
 ("The upside-down bottle on the wall that measures out a shot", "Optic", ["Swizzle stick", "Ice bucket", "Cocktail shaker"]),
 ("The outdoor seating area for summer pints", "Beer garden", ["Cellar", "Saloon", "Skittle alley"]),
 ("The person who runs the pub", "Landlord", ["Cellarman", "Glass collector", "Doorman"]),
 ("Teams with silly names answering questions on a weeknight", "Pub quiz", ["Open mic", "Karaoke", "Meat raffle"]),
 ("Put a coin in and pick a song", "Jukebox", ["Fruit machine", "Dartboard", "Cigarette machine"]),
 ("A little cardboard square to stand your pint on", "Beer mat", ["Tankard", "Swizzle stick", "Ice bucket"]),
 ("A tall seat at the counter", "Bar stool", ["Settle", "Pew", "Booth"]),
 ("A short drink knocked back after a pint", "Chaser", ["Spritzer", "Black velvet", "Mixer"]),
 ("A pub not tied to any one brewery", "Free house", ["Tied house", "Brewery tap", "Gastropub"]),
 ("Running up a bill to settle at the end of the night", "Tab", ["Tombola", "Meat raffle", "Happy hour"]),
 ("Crunchy fried pig skin in a little packet", "Pork scratchings", ["Scampi fries", "Twiglets", "Bombay mix"]),
 ("A smaller glass, half the size of a pint", "Half", ["Tankard", "Stein", "Schooner"]),
 ("Lager with a splash of lemonade on top", "Lager top", ["Black velvet", "Spritzer", "Boilermaker"]),
 ("Lager and cider mixed together", "Snakebite", ["Black velvet", "Spritzer", "Boilermaker"])])

race("what's this pet word?", "Animals", "easy", ["pets", "words"], [
 ("A wooden home for a rabbit or guinea pig", "Hutch", ["Coop", "Sty", "Byre"]),
 ("A little swinging door so the cat can come and go", "Cat flap", ["Hatch", "Trapdoor", "Porthole"]),
 ("Where an indoor cat goes to the loo", "Litter tray", ["Basket", "Crate", "Trough"]),
 ("A herb that sends cats a bit giddy", "Catnip", ["Rosemary", "Lavender", "Thyme"]),
 ("A rope-wrapped pole for sharpening claws on", "Scratching post", ["Perch", "Chew toy", "Trough"]),
 ("A dog's wooden house in the garden", "Kennel", ["Coop", "Sty", "Byre"]),
 ("Clipped onto the collar for walkies", "Lead", ["Muzzle", "Rawhide", "Tag"]),
 ("Worn round the neck, with a name tag on it", "Collar", ["Muzzle", "Harness", "Rawhide"]),
 ("The animal doctor", "Vet", ["Breeder", "Kennel maid", "Farrier"]),
 ("Lets your dog travel abroad with you", "Pet passport", ["Pedigree certificate", "Dog licence", "Tag"]),
 ("Hung in a budgie's cage for it to peck at for calcium", "Cuttlefish bone", ["Mirror", "Bell", "Perch"]),
 ("A glass tank of water for pet fish", "Aquarium", ["Aviary", "Coop", "Run"]),
 ("A heated glass home for a pet lizard or snake", "Vivarium", ["Aviary", "Coop", "Run"]),
 ("Dry, biscuit-like pellets of pet food", "Kibble", ["Rawhide", "Chew toy", "Wormer"]),
 ("A tiny tag under the skin that identifies a lost pet", "Microchip", ["Tag", "Dog licence", "Muzzle"]),
 ("Spins round as a little rodent runs all night", "Hamster wheel", ["Chew toy", "Perch", "Bell"]),
 ("A round glass bowl for a fairground prize fish", "Goldfish bowl", ["Aviary", "Coop", "Trough"]),
 ("Where you go to adopt an unwanted animal", "Rescue centre", ["Kennel Club", "Crufts", "Breeder"]),
 ("The operation that stops a pet having babies", "Neutering", ["Worming", "Grooming", "Vaccinating"]),
 ("Washes, clips and trims a dog's coat", "Groomer", ["Breeder", "Kennel maid", "Farrier"])])

race("what's this computer word?", "Computers and the internet", "easy", ["computers", "technology", "words"], [
 ("You slide it across the desk to move the pointer", "Mouse", ["Stylus", "Scanner", "Projector"]),
 ("The screen you look at on a desktop computer", "Monitor", ["Projector", "Scanner", "Graphics card"]),
 ("Puts your document onto paper", "Printer", ["Scanner", "Projector", "Fan"]),
 ("A little plug-in stick for carrying files around", "USB stick", ["Heat sink", "Sound card", "Power supply"]),
 ("Lets people see you on a video call", "Webcam", ["Projector", "Scanner", "Joystick"]),
 ("The box that spreads Wi-Fi round the house", "Router", ["Projector", "Scanner", "Power supply"]),
 ("Where all your files are stored for keeps", "Hard drive", ["Cache", "Fan", "Heat sink"]),
 ("Short-term memory that's wiped when you switch off", "RAM", ["Firmware", "Driver", "Heat sink"]),
 ("The 'brain' chip that does the thinking", "Processor", ["Fan", "Heat sink", "Sound card"]),
 ("The main circuit board everything plugs into", "Motherboard", ["Graphics card", "Sound card", "Power supply"]),
 ("A folding computer you can rest on your knees", "Laptop", ["Projector", "Scanner", "Joystick"]),
 ("A flat touchscreen computer with no keyboard", "Tablet", ["Projector", "Scanner", "Joystick"]),
 ("Plugs in to top up the battery", "Charger", ["Dongle", "Joystick", "Stylus"]),
 ("One tiny dot of colour on the screen", "Pixel", ["Icon", "Widget", "Cookie"]),
 ("Copying a file from the internet onto your device", "Download", ["Driver", "Firmware", "Cache"]),
 ("Switching it off and on again", "Reboot", ["Driver", "Firmware", "Cache"]),
 ("A moving picture that appears when you leave the computer alone", "Screensaver", ["Taskbar", "Widget", "Folder"]),
 ("The flashing line that shows where you'll type", "Cursor", ["Icon", "Widget", "Taskbar"]),
 ("The main screen with all your icons on it", "Desktop", ["Taskbar", "Folder", "Widget"]),
 ("The touch-sensitive pad below a laptop's keyboard", "Trackpad", ["Stylus", "Joystick", "Scanner"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-148.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
