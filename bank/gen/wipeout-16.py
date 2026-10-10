# Bank session 10 Oct 2026: new Wipeout boards -> bank/wipeout-16.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Words that make a new word when you add 'land' to the end", "Words and language", "medium", ["wordplay", "compound words"],
 ["Home", "Main", "Wood", "Fen", "Grass", "Heath", "High", "Wet", "Farm", "Waste", "Head", "Wonder", "Father", "Marsh", "Border"],
 ["Sea", "River", "Field", "Hill", "Forest"])
board("Words that make a new word when you put 'water' in front", "Words and language", "easy", ["wordplay", "compound words"],
 ["Fall", "Melon", "Proof", "Front", "Colour", "Cress", "Mark", "Logged", "Line", "Shed", "Side", "Way", "Bed", "Works", "Mill"],
 ["Bottle", "Tap", "Glass", "Rain", "Pool"])
board("Words that make a new word when you add 'stone' to the end", "Words and language", "medium", ["wordplay", "compound words"],
 ["Lime", "Sand", "Mile", "Key", "Cobble", "Corner", "Grave", "Hail", "Head", "Lode", "Mill", "Moon", "Tomb", "Flag", "Touch"],
 ["Rock", "Brick", "Chalk", "Clay", "Glass"])
board("Lakes in Africa", "World geography", "hard", ["Africa", "lakes"],
 ["Victoria", "Tanganyika", "Malawi", "Chad", "Turkana", "Kariba", "Volta", "Albert", "Edward", "Kivu", "Nasser", "Tana", "Kyoga", "Naivasha", "Nakuru"],
 ["Baikal", "Titicaca", "Balkhash", "Van", "Urmia"])
board("Cuts of beef", "Food and drink", "medium", ["beef", "butchery"],
 ["Sirloin", "Rump", "Fillet", "Ribeye", "Brisket", "Chuck", "Flank", "Skirt", "Topside", "Silverside", "T-bone", "Shin", "Oxtail", "Short rib", "Feather blade"],
 ["Gammon", "Scrag end", "Trotters", "Chump", "Crackling"])
board("Breeds of terrier", "Animals", "medium", ["dogs", "terriers", "breeds"],
 ["Jack Russell", "Yorkshire", "Bull", "Staffordshire Bull", "West Highland White", "Cairn", "Scottish", "Airedale", "Border", "Fox", "Bedlington", "Patterdale", "Norfolk", "Lakeland", "Manchester"],
 ["Dachshund", "Beagle", "Whippet", "Pug", "Corgi"])
board("Imperial units of measurement", "Science and nature", "easy", ["imperial units", "measurement"],
 ["Inch", "Foot", "Yard", "Mile", "Furlong", "Chain", "Fathom", "League", "Pint", "Gallon", "Quart", "Ounce", "Pound", "Stone", "Hundredweight"],
 ["Litre", "Gram", "Metre", "Hectare", "Tonne"])
board("Permanent race circuits that have hosted a Formula One Grand Prix", "Motor racing", "hard", ["Formula One", "circuits"],
 ["Silverstone", "Monza", "Spa-Francorchamps", "Suzuka", "Interlagos", "Imola", "Hockenheim", "Nürburgring", "Zandvoort", "Hungaroring", "Red Bull Ring", "Yas Marina", "Circuit of the Americas", "Brands Hatch", "Paul Ricard"],
 ["Daytona", "Thruxton", "Mount Panorama", "Laguna Seca", "Snetterton"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-16.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'boards written')
