# Bank session 10 Oct 2026: new Wipeout boards -> bank/wipeout-12.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Kinds of shark", "Animals", "medium", ["sharks", "sea life"],
 ["Great white", "Hammerhead", "Tiger", "Bull", "Mako", "Whale shark", "Basking", "Nurse", "Blue", "Thresher", "Lemon", "Greenland", "Goblin", "Wobbegong", "Porbeagle"],
 ["Manta", "Sawfish", "Guitarfish", "Barracuda", "Orca"])
board("Kinds of whale", "Animals", "medium", ["whales", "sea life"],
 ["Blue whale", "Humpback", "Sperm whale", "Fin whale", "Minke", "Sei whale", "Bowhead", "Grey whale", "Right whale", "Beluga", "Narwhal", "Killer whale", "Pilot whale", "Bryde's whale", "Cuvier's beaked whale"],
 ["Dugong", "Manatee", "Walrus", "Whale shark", "Elephant seal"])
board("Venomous snakes", "Animals", "medium", ["snakes", "reptiles"],
 ["King cobra", "Black mamba", "Rattlesnake", "Adder", "Taipan", "Puff adder", "Saw-scaled viper", "Copperhead", "Cottonmouth", "Coral snake", "Krait", "Boomslang", "Fer-de-lance", "Gaboon viper", "Sea snake"],
 ["Python", "Boa constrictor", "Anaconda", "Grass snake", "Corn snake"])
board("Breeds of sheep", "Animals", "hard", ["sheep", "farming", "breeds"],
 ["Suffolk", "Texel", "Herdwick", "Swaledale", "Jacob", "Merino", "Cheviot", "Scottish Blackface", "Border Leicester", "Romney", "Shetland", "Soay", "Dorset Horn", "Wensleydale", "Hebridean"],
 ["Gloucester Old Spot", "Tamworth", "Dexter", "Hereford", "Belted Galloway"])
board("Typefaces (fonts)", "Science and technology", "medium", ["fonts", "typography"],
 ["Arial", "Helvetica", "Times New Roman", "Comic Sans", "Garamond", "Calibri", "Verdana", "Futura", "Georgia", "Courier", "Gill Sans", "Baskerville", "Tahoma", "Impact", "Didot"],
 ["Kerning", "Serif", "Pica", "Leading", "Ligature"])
board("English places with a Church of England cathedral", "Britain", "hard", ["cathedrals", "cities"],
 ["Durham", "York", "Canterbury", "Salisbury", "Lincoln", "Ely", "Wells", "Exeter", "Winchester", "Norwich", "Chichester", "Hereford", "Worcester", "Lichfield", "Peterborough"],
 ["Beverley", "Bath", "Tewkesbury", "Hexham", "Selby"])
board("Deserts of the world", "World geography", "medium", ["deserts"],
 ["Sahara", "Gobi", "Kalahari", "Namib", "Atacama", "Mojave", "Sonoran", "Arabian", "Thar", "Great Victoria", "Simpson", "Taklamakan", "Chihuahuan", "Patagonian", "Great Sandy"],
 ["Serengeti", "Okavango", "Pampas", "Masai Mara", "Everglades"])
board("Italian pasta sauces", "Food and drink", "medium", ["Italian food", "sauces"],
 ["Carbonara", "Bolognese", "Arrabbiata", "Puttanesca", "Amatriciana", "Pesto", "Marinara", "Alfredo", "Aglio e olio", "Cacio e pepe", "Vongole", "Primavera", "Napoletana", "Alla Norma", "Gricia"],
 ["Bruschetta", "Saltimbocca", "Gnocchi", "Ossobuco", "Panzanella"])
board("Knots and hitches", "Hobbies", "hard", ["knots", "sailing"],
 ["Reef knot", "Bowline", "Clove hitch", "Sheet bend", "Figure of eight", "Granny knot", "Half hitch", "Round turn and two half hitches", "Sheepshank", "Slip knot", "Hangman's knot", "Overhand knot", "Fisherman's knot", "Rolling hitch", "Timber hitch"],
 ["Mainbrace", "Fathom", "Cleat", "Bollard", "Halyard"])
board("Towns in Yorkshire", "Britain", "medium", ["Yorkshire", "towns"],
 ["Harrogate", "Whitby", "Scarborough", "Skipton", "Halifax", "Huddersfield", "Barnsley", "Rotherham", "Doncaster", "Keighley", "Pontefract", "Thirsk", "Malton", "Batley", "Dewsbury"],
 ["Burnley", "Clitheroe", "Darlington", "Oldham", "Gainsborough"])
board("Songs by David Bowie", "Music", "medium", ["David Bowie", "songs"],
 ["Space Oddity", "Starman", "Life on Mars?", "Heroes", "Changes", "Rebel Rebel", "Ashes to Ashes", "Let's Dance", "China Girl", "Modern Love", "Fame", "Golden Years", "Under Pressure", "The Jean Genie", "Sound and Vision"],
 ["Rocket Man", "Get It On", "Virginia Plain", "The Ballroom Blitz", "20th Century Boy"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-12.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'boards written')
