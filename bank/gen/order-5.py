# Bank session 10 Oct 2026: 20 more Put in order questions -> bank/order-2.json. Checked against every order question in
# the live bank (the server also skips any whose items match one already there).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

o("History", ["army", "ranks"], "medium", "Put these British Army ranks in order, most junior first", ["Private", "Lance Corporal", "Corporal", "Sergeant", "Lieutenant", "Captain", "Major"], "most junior first")
o("History", ["navy", "ranks"], "hard", "Put these Royal Navy ranks in order, most junior first", ["Able Seaman", "Petty Officer", "Lieutenant", "Commander", "Captain", "Admiral"], "most junior first")
o("Royals", ["peerage"], "medium", "Put these ranks of the peerage in order, highest first", ["Duke", "Marquess", "Earl", "Viscount", "Baron"], "highest first")
o("Britain", ["landmarks", "height"], "medium", "Put these British structures in order of height, shortest first", ["Nelson's Column", "Big Ben's tower", "Blackpool Tower", "BT Tower", "One Canada Square", "The Shard"], "shortest first")
o("Everyday life", ["beds"], "easy", "Put these bed sizes in order, smallest first", ["Single", "Small double", "Double", "King", "Super king"], "smallest first")
o("Words and language", ["NATO alphabet"], "easy", "Put these code words in the order they come in the NATO phonetic alphabet", ["Bravo", "Echo", "Juliett", "Oscar", "Tango", "Yankee"], "A to Z")
o("Britain", ["Shipping Forecast"], "hard", "Put these Shipping Forecast areas in the order they are read out, starting from Viking", ["Viking", "Forties", "Cromarty", "Forth", "Tyne", "Dogger"], "as read on the radio")
o("Science", ["Moon"], "medium", "Put these phases of the Moon in order, starting from new moon", ["New moon", "Waxing crescent", "First quarter", "Waxing gibbous", "Full moon", "Waning gibbous"], "from new moon")
o("Science", ["dinosaurs", "geology"], "hard", "Put these periods of Earth's history in order, oldest first", ["Cambrian", "Devonian", "Carboniferous", "Triassic", "Jurassic", "Cretaceous"], "oldest first")
o("Everyday life", ["paper"], "easy", "Put these paper sizes in order, smallest first", ["A6", "A5", "A4", "A3", "A2"], "smallest first")
o("Science and tech", ["computers"], "easy", "Put these amounts of computer memory in order, smallest first", ["Bit", "Byte", "Kilobyte", "Megabyte", "Gigabyte", "Terabyte"], "smallest first")
o("Food and drink", ["baking"], "easy", "Put these steps of making a loaf of bread in order", ["Mix the dough", "Knead", "Leave to rise", "Knock back and shape", "Bake"], "first step first")
o("Science", ["Earth"], "easy", "Put these layers of the Earth in order, from the surface down", ["Crust", "Mantle", "Outer core", "Inner core"], "from the surface down")
o("Science", ["atmosphere"], "hard", "Put these layers of the atmosphere in order, lowest first", ["Troposphere", "Stratosphere", "Mesosphere", "Thermosphere", "Exosphere"], "lowest first")
o("Science", ["light"], "hard", "Put these kinds of radiation in order of wavelength, longest first", ["Radio waves", "Microwaves", "Infrared", "Visible light", "Ultraviolet", "X-rays", "Gamma rays"], "longest wavelength first")
o("Science", ["weather"], "easy", "Put these stages of the water cycle in order, starting from the sea", ["Evaporation", "Condensation", "Precipitation", "Collection"], "starting from the sea")
o("History", ["Britain"], "medium", "Put these periods of British history in order, earliest first", ["Stone Age", "Bronze Age", "Iron Age", "Roman Britain", "Anglo-Saxon England", "Norman Conquest"], "earliest first")
o("History", ["royals", "dynasties"], "medium", "Put these royal houses of England and Britain in order, earliest first", ["Normans", "Plantagenets", "Tudors", "Stuarts", "Hanoverians", "Windsors"], "earliest first")
o("Science", ["human body"], "easy", "Put these in the order your food passes through them", ["Mouth", "Oesophagus", "Stomach", "Small intestine", "Large intestine"], "first stop first")
o("Words and language", ["Greek alphabet"], "medium", "Put these Greek letters in alphabetical order", ["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta"], "alpha first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-2.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
