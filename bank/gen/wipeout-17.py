# Bank session 10 Oct 2026: new Wipeout boards -> bank/wipeout-17.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Words that make a new word when you put 'sea' in front", "Words and language", "easy", ["wordplay", "compound words"],
 ["Shell", "Side", "Weed", "Food", "Gull", "Horse", "Son", "Sick", "Front", "Bed", "Port", "Plane", "Shore", "Farer", "Man"],
 ["Wave", "Sand", "Rock", "Tide", "Coast"])
board("Words that make a new word when you put 'back' in front", "Words and language", "easy", ["wordplay", "compound words"],
 ["Bone", "Fire", "Ground", "Pack", "Side", "Stage", "Stroke", "Hand", "Log", "Lash", "Yard", "Drop", "Gammon", "Track", "Water"],
 ["Front", "Leg", "Arm", "Head", "Neck"])
board("Words that make a new word when you add 'pot' to the end", "Words and language", "medium", ["wordplay", "compound words"],
 ["Tea", "Jack", "Hot", "Crack", "Des", "Flower", "Stock", "Fuss", "Ink", "Honey", "Pepper", "Coffee", "Flesh", "Tin", "Chamber"],
 ["Pan", "Cup", "Mug", "Bowl", "Plate"])
board("Words that make a new word when you put 'head' in front", "Words and language", "easy", ["wordplay", "compound words"],
 ["Ache", "Line", "Light", "Master", "Phone", "Quarters", "Room", "Stone", "Way", "Band", "Board", "Land", "Rest", "Strong", "Wind"],
 ["Hat", "Neck", "Hair", "Face", "Nose"])
board("Cocktails made with vodka", "Food and drink", "medium", ["cocktails", "vodka"],
 ["Moscow Mule", "Cosmopolitan", "Bloody Mary", "White Russian", "Black Russian", "Screwdriver", "Sex on the Beach", "Espresso Martini", "Woo Woo", "Sea Breeze", "Harvey Wallbanger", "Kamikaze", "Caipiroska", "Porn Star Martini", "Lemon Drop"],
 ["Negroni", "Mojito", "Margarita", "Daiquiri", "Tom Collins"])
board("Fictional doctors: 'Dr ___'", "Film and TV", "medium", ["doctors", "fictional characters"],
 ["Who", "Jekyll", "Frankenstein", "Dolittle", "No", "Evil", "Watson", "Zhivago", "Strange", "House", "Octopus", "Doom", "Strangelove", "Moreau", "Faustus"],
 ["Livingstone", "Johnson", "Crippen", "Barnardo", "Beeching"])
board("Chilli peppers", "Food and drink", "medium", ["chillies", "spices"],
 ["Jalapeño", "Habanero", "Scotch bonnet", "Bird's eye", "Cayenne", "Chipotle", "Serrano", "Poblano", "Ancho", "Ghost pepper", "Carolina Reaper", "Padrón", "Piri piri", "Naga", "Anaheim"],
 ["Sichuan pepper", "Black pepper", "Wasabi", "Horseradish", "Sumac"])
board("Varieties of tomato", "Food and drink", "hard", ["tomatoes", "gardening"],
 ["Gardener's Delight", "Moneymaker", "Alicante", "San Marzano", "Beefsteak", "Sungold", "Ailsa Craig", "Shirley", "Tigerella", "Black Krim", "Marmande", "Brandywine", "Roma", "Sweet Million", "Costoluto Fiorentino"],
 ["King Edward", "Maris Piper", "Charlotte", "Desiree", "Rooster"])
board("Dances you'd do at a ceilidh", "Scotland", "hard", ["ceilidh", "dancing", "Scotland"],
 ["Strip the Willow", "Gay Gordons", "Dashing White Sergeant", "Canadian Barn Dance", "Eightsome Reel", "Military Two-Step", "Flying Scotsman", "Hamilton House", "Pride of Erin Waltz", "St Bernard's Waltz", "Britannia Two-Step", "Circassian Circle", "Boston Two-Step", "Highland Schottische", "Waltz Country Dance"],
 ["Foxtrot", "Rumba", "Tango", "Cha-cha-cha", "Paso doble"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-17.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'boards written')
