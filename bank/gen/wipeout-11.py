# Bank session 10 Oct 2026: new Wipeout boards -> bank/wipeout-11.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Colours that are also a fruit or a flower", "Words and language", "easy", ["colours", "words"],
 ["Orange", "Lime", "Peach", "Plum", "Cherry", "Lemon", "Apricot", "Raspberry", "Olive", "Lilac", "Lavender", "Violet", "Rose", "Magnolia", "Primrose"],
 ["Teal", "Maroon", "Scarlet", "Turquoise", "Navy"])
board("Real London Underground stations (watch for fakes)", "London", "medium", ["London Underground", "stations"],
 ["Mornington Crescent", "Cockfosters", "Elephant & Castle", "Seven Sisters", "Tooting Bec", "Burnt Oak", "Ickenham", "Swiss Cottage", "Barking", "Theydon Bois", "Upminster", "Chalk Farm", "Totteridge & Whetstone", "Arnos Grove", "Gants Hill"],
 ["Seven Brothers", "Pigeon Hill", "Elephant & Crown", "Swiss Chalet", "Burnt Pine"])
board("Subjects taught at Hogwarts", "Harry Potter", "medium", ["Hogwarts", "Harry Potter"],
 ["Potions", "Transfiguration", "Charms", "Herbology", "Defence Against the Dark Arts", "History of Magic", "Astronomy", "Divination", "Care of Magical Creatures", "Arithmancy", "Ancient Runes", "Muggle Studies", "Flying", "Apparition", "Alchemy"],
 ["Spellcraft", "Dragonology", "Broom Mechanics", "Magical Law", "Wandlore"])
board("Countries where Spanish is an official language", "World geography", "medium", ["Spanish", "languages", "countries"],
 ["Spain", "Mexico", "Argentina", "Colombia", "Peru", "Chile", "Venezuela", "Cuba", "Bolivia", "Ecuador", "Uruguay", "Paraguay", "Costa Rica", "Panama", "Equatorial Guinea"],
 ["Brazil", "Belize", "The Philippines", "Portugal", "Haiti"])
board("Businesses in The Simpsons' Springfield", "Film and TV", "medium", ["The Simpsons", "places"],
 ["The Kwik-E-Mart", "Moe's Tavern", "Krusty Burger", "The Android's Dungeon", "Lard Lad Donuts", "The Springfield Nuclear Power Plant", "The Leftorium", "Duff Brewery", "Try-N-Save", "The Frying Dutchman", "Luigi's", "Monstromart", "Noiseland Arcade", "Gulp 'n' Blow", "Itchy & Scratchy Land"],
 ["Los Pollos Hermanos", "Central Perk", "The Krusty Krab", "Paddy's Pub", "The Peach Pit"])
board("Streets in Newcastle", "The North East", "medium", ["Newcastle", "streets"],
 ["Grey Street", "Northumberland Street", "Grainger Street", "Collingwood Street", "Clayton Street", "Pilgrim Street", "Blackett Street", "Westgate Road", "Osborne Road", "Shields Road", "Dean Street", "The Side", "Quayside", "Bigg Market", "Pudding Chare"],
 ["Fawcett Street", "High Street West", "Holmeside", "Vine Place", "Hylton Road"])
board("Varieties of apple", "Food and drink", "medium", ["apples", "fruit"],
 ["Granny Smith", "Braeburn", "Gala", "Pink Lady", "Golden Delicious", "Bramley", "Cox's Orange Pippin", "Jazz", "Fuji", "Egremont Russet", "Discovery", "Jonagold", "Red Delicious", "Honeycrisp", "Worcester Pearmain"],
 ["Conference", "Williams", "Comice", "Concorde", "Bosc"])
board("Varieties of potato", "Food and drink", "medium", ["potatoes", "vegetables"],
 ["King Edward", "Maris Piper", "Charlotte", "Jersey Royal", "Desiree", "Rooster", "Kerr's Pink", "Pink Fir Apple", "Anya", "Cara", "Marfona", "Estima", "Nicola", "Arran Pilot", "Vivaldi"],
 ["Gardener's Delight", "Moneymaker", "Alicante", "San Marzano", "Beefsteak"])
board("Gundog breeds", "Animals", "hard", ["dogs", "breeds"],
 ["Labrador Retriever", "Golden Retriever", "Cocker Spaniel", "Springer Spaniel", "Pointer", "English Setter", "Irish Setter", "Weimaraner", "Vizsla", "Flat-coated Retriever", "Brittany", "Gordon Setter", "Chesapeake Bay Retriever", "German Shorthaired Pointer", "Clumber Spaniel"],
 ["Beagle", "Border Collie", "Dachshund", "Jack Russell Terrier", "Dalmatian"])
board("Rugby league clubs", "Rugby", "medium", ["rugby league", "clubs"],
 ["Wigan Warriors", "St Helens", "Leeds Rhinos", "Warrington Wolves", "Hull FC", "Hull Kingston Rovers", "Catalans Dragons", "Castleford Tigers", "Huddersfield Giants", "Wakefield Trinity", "Leigh Leopards", "Salford Red Devils", "Bradford Bulls", "Widnes Vikings", "Featherstone Rovers"],
 ["Leicester Tigers", "Bath", "Saracens", "Gloucester", "Northampton Saints"])
board("White grape varieties", "Food and drink", "hard", ["wine", "grapes"],
 ["Chardonnay", "Sauvignon Blanc", "Riesling", "Pinot Grigio", "Chenin Blanc", "Viognier", "Gewürztraminer", "Sémillon", "Albariño", "Grüner Veltliner", "Muscat", "Marsanne", "Verdejo", "Torrontés", "Vermentino"],
 ["Merlot", "Malbec", "Tempranillo", "Sangiovese", "Pinot Noir"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-11.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'boards written')
