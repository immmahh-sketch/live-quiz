# Bank session 9 Oct 2026: 20 new Wipeout boards -> bank/wipeout-3.json. 15 right answers (certain, fairly well
# known) and 5 wrong ones (plausible, definitely wrong) each; none of these subjects is already a board.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Countries whose capital city begins with B", "Geography", "medium", ["capitals", "countries"],
 ["Belgium", "Germany", "Hungary", "Romania", "Serbia", "Slovakia", "Switzerland", "Thailand", "Colombia", "Lebanon", "Argentina", "Iraq", "Brazil", "Barbados", "Belize"],
 ["Belarus", "Bulgaria", "Bolivia", "Bangladesh", "Botswana"])
board("Things you'd find in a first aid kit", "General knowledge", "easy", ["first aid", "household"],
 ["Plasters", "Bandages", "Antiseptic wipes", "Gauze pads", "Safety pins", "Tweezers", "Scissors", "Disposable gloves", "Eye wash", "Triangular bandage", "Burn gel", "Instant cold pack", "Medical tape", "Thermometer", "Foil blanket"],
 ["Defibrillator", "Stethoscope", "Syringe", "Oxygen mask", "Blood pressure cuff"])
board("Things you'd find around a snooker or pool table", "Sport", "easy", ["snooker", "pool"],
 ["Cue", "Chalk", "Rest", "Spider", "Cushion", "Pocket", "Baize", "Triangle", "Cue ball", "Black ball", "Red ball", "The D", "Baulk line", "Spot", "Extension"],
 ["Putter", "Shuttlecock", "Wicket", "Puck", "Tee"])
board("Golf terms", "Sport", "easy", ["golf", "words"],
 ["Birdie", "Eagle", "Albatross", "Bogey", "Par", "Tee", "Fairway", "Green", "Bunker", "Rough", "Putter", "Driver", "Wedge", "Caddie", "Hole in one"],
 ["Wicket", "Try", "Deuce", "Offside", "Scrum"])
board("Tennis terms", "Sport", "easy", ["tennis", "words"],
 ["Love", "Deuce", "Advantage", "Ace", "Let", "Rally", "Volley", "Lob", "Smash", "Baseline", "Tiebreak", "Break point", "Double fault", "Backhand", "Forehand"],
 ["Birdie", "Wicket", "Scrum", "Offside", "Bogey"])
board("Cricket terms", "Sport", "medium", ["cricket", "words"],
 ["Wicket", "Over", "Maiden", "Duck", "LBW", "Stumps", "Bails", "Crease", "Yorker", "Googly", "Century", "Boundary", "No-ball", "Wide", "Hat-trick"],
 ["Love", "Birdie", "Scrum", "Offside", "Puck"])
board("Rugby terms", "Sport", "medium", ["rugby", "words"],
 ["Scrum", "Try", "Conversion", "Line-out", "Ruck", "Maul", "Knock-on", "Sin bin", "Drop goal", "Hooker", "Prop", "Fly-half", "Scrum-half", "Garryowen", "Grand Slam"],
 ["Birdie", "Love", "Wicket", "Deuce", "LBW"])
board("Desserts and cakes from France", "Food and drink", "medium", ["French food", "desserts"],
 ["Crème brûlée", "Éclair", "Macaron", "Mille-feuille", "Profiterole", "Tarte Tatin", "Crêpe", "Madeleine", "Soufflé", "Clafoutis", "Chocolate mousse", "Croquembouche", "Paris-Brest", "Financier", "Île flottante"],
 ["Tiramisu", "Baklava", "Pavlova", "Panna cotta", "Strudel"])
board("Dishes you'd find on a British Indian restaurant menu", "Food and drink", "easy", ["curry", "Indian food"],
 ["Korma", "Tikka masala", "Biryani", "Dhal", "Vindaloo", "Jalfrezi", "Onion bhaji", "Samosa", "Dopiaza", "Madras", "Rogan josh", "Pakora", "Naan", "Tandoori chicken", "Saag aloo"],
 ["Massaman curry", "Beef rendang", "Laksa", "Katsu curry", "Thai green curry"])
board("Dishes from a British Chinese takeaway", "Food and drink", "easy", ["takeaway", "Chinese food"],
 ["Chow mein", "Sweet and sour chicken", "Crispy aromatic duck", "Spring rolls", "Egg fried rice", "Prawn crackers", "Kung pao chicken", "Char siu pork", "Wonton soup", "Dim sum", "Chop suey", "Crispy chilli beef", "Salt and pepper chips", "Beef in black bean sauce", "Lemon chicken"],
 ["Pad thai", "Pho", "Bibimbap", "Nasi goreng", "Teriyaki chicken"])
board("Jobs on a film set", "Film", "medium", ["film", "jobs"],
 ["Director", "Producer", "Gaffer", "Best boy", "Grip", "Clapper loader", "Boom operator", "Stunt double", "Make-up artist", "Costume designer", "Cinematographer", "Script supervisor", "Runner", "Focus puller", "Extra"],
 ["Prompter", "Usher", "Projectionist", "Stage manager", "Box office manager"])
board("Horse racing courses in England", "Sport", "medium", ["horse racing", "places"],
 ["Aintree", "Ascot", "Epsom", "Cheltenham", "Newmarket", "York", "Doncaster", "Goodwood", "Haydock Park", "Sandown Park", "Kempton Park", "Newbury", "Chester", "Uttoxeter", "Wetherby"],
 ["Silverstone", "Wembley", "Twickenham", "Lord's", "Brands Hatch"])
board("Formula One world champions", "Sport", "medium", ["Formula One", "motorsport"],
 ["Lewis Hamilton", "Michael Schumacher", "Ayrton Senna", "Alain Prost", "Sebastian Vettel", "Max Verstappen", "Fernando Alonso", "Kimi Räikkönen", "Jenson Button", "Damon Hill", "Nigel Mansell", "Niki Lauda", "Jackie Stewart", "Jim Clark", "Juan Manuel Fangio"],
 ["David Coulthard", "Martin Brundle", "Mark Webber", "Rubens Barrichello", "Felipe Massa"])
board("Real ships from history (not fictional ones)", "History", "medium", ["ships", "history"],
 ["Titanic", "Mary Rose", "Cutty Sark", "HMS Victory", "Golden Hind", "Mayflower", "Endeavour", "Bismarck", "Lusitania", "Queen Mary", "HMS Beagle", "Bounty", "Ark Royal", "Endurance", "Santa María"],
 ["Black Pearl", "Flying Dutchman", "Hispaniola", "Pequod", "Nostromo"])
board("Countries that still have a king, queen or emperor of their own", "Geography", "hard", ["monarchies", "countries"],
 ["Spain", "Netherlands", "Belgium", "Denmark", "Norway", "Sweden", "Japan", "Thailand", "Saudi Arabia", "Morocco", "Jordan", "Bhutan", "Cambodia", "Tonga", "Lesotho"],
 ["Greece", "Italy", "Portugal", "Austria", "Romania"])
board("Famous people called David: which surnames?", "People", "easy", ["famous names"],
 ["Beckham", "Bowie", "Attenborough", "Cameron", "Tennant", "Walliams", "Hockney", "Jason", "Essex", "Seaman", "Frost", "Livingstone", "Copperfield", "Moyes", "Haye"],
 ["Lineker", "Hamilton", "Gascoigne", "Clarkson", "Corden"])
board("Famous people called John: which surnames?", "People", "easy", ["famous names"],
 ["Lennon", "Major", "Cleese", "Travolta", "Terry", "Barnes", "Prescott", "Bishop", "Legend", "Peel", "Logie Baird", "Constable", "Lewis", "Wayne", "McEnroe"],
 ["Stokes", "Lampard", "Hurst", "Owen", "Bolt"])
board("Words that make a new word when you add 'man' to the end", "Words and language", "medium", ["wordplay"],
 ["Post", "Fire", "Snow", "Chair", "Police", "Fisher", "Milk", "Sales", "Gentle", "Horse", "Sports", "Door", "Bats", "Middle", "Fresh"],
 ["Cat", "Tree", "Blue", "Lamp", "Cup"])
board("Things you'd have with a traditional Sunday roast", "Food and drink", "easy", ["British food"],
 ["Roast potatoes", "Yorkshire pudding", "Gravy", "Stuffing", "Roast parsnips", "Carrots", "Peas", "Cauliflower cheese", "Horseradish", "Mint sauce", "Apple sauce", "Roast beef", "Roast chicken", "Broccoli", "Cabbage"],
 ["Mushy peas", "Black pudding", "Hash browns", "Pease pudding", "Piccalilli"])
board("Bands and acts from Greater Manchester", "Music", "medium", ["bands", "Manchester"],
 ["Oasis", "The Smiths", "Joy Division", "New Order", "The Stone Roses", "Happy Mondays", "Inspiral Carpets", "Take That", "Simply Red", "The Hollies", "Herman's Hermits", "Elbow", "The Courteeners", "James", "Buzzcocks"],
 ["The Beatles", "Arctic Monkeys", "Blur", "The Kinks", "Duran Duran"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-3.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'boards written; all 15 right / 5 wrong, no overlaps')
