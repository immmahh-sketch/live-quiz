# Bank session 10 Oct 2026: new Wipeout boards -> bank/wipeout-47.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Mr Men and Little Miss characters", "Books", "easy", ["Mr Men", "Little Miss", "children's books"],
 ["Mr Tickle", "Mr Happy", "Mr Greedy", "Mr Bump", "Mr Strong", "Mr Silly", "Mr Messy", "Mr Grumpy", "Mr Topsy-Turvy", "Mr Nosey", "Mr Small", "Mr Sneeze", "Little Miss Sunshine", "Little Miss Bossy", "Little Miss Naughty"],
 ["Mr Benn", "Mr Blobby", "Mr Tumble", "Mr Bean", "Little Miss Muffet"])
board("Films directed by Quentin Tarantino or Christopher Nolan", "Film", "medium", ["directors", "Tarantino", "Nolan"],
 ["Reservoir Dogs", "Pulp Fiction", "Jackie Brown", "Kill Bill", "Inglourious Basterds", "Django Unchained", "The Hateful Eight", "Once Upon a Time in Hollywood", "Memento", "The Prestige", "The Dark Knight", "Inception", "Interstellar", "Dunkirk", "Oppenheimer"],
 ["True Romance", "From Dusk till Dawn", "Natural Born Killers", "Fight Club", "The Usual Suspects"])
board("Countries with a Pacific Ocean coastline", "World geography", "medium", ["Pacific", "oceans", "countries"],
 ["USA", "Canada", "Mexico", "Guatemala", "Costa Rica", "Panama", "Colombia", "Ecuador", "Peru", "Chile", "Japan", "Russia", "Philippines", "New Zealand", "Australia"],
 ["Argentina", "Venezuela", "Bolivia", "Brazil", "Belize"])
board("Coffees you can order in a coffee shop", "Food and drink", "easy", ["coffee", "drinks"],
 ["Espresso", "Cappuccino", "Latte", "Flat white", "Americano", "Macchiato", "Mocha", "Cortado", "Ristretto", "Lungo", "Affogato", "Frappé", "Irish coffee", "Cold brew", "Piccolo"],
 ["Chai latte", "Matcha latte", "Rooibos", "Horlicks", "Ovaltine"])
board("Curries on a British Indian restaurant menu (not starters or sides)", "Food and drink", "easy", ["curry", "Indian food", "takeaway"],
 ["Korma", "Tikka masala", "Jalfrezi", "Vindaloo", "Madras", "Bhuna", "Dopiaza", "Rogan josh", "Dhansak", "Balti", "Pasanda", "Phall", "Butter chicken", "Pathia", "Karahi"],
 ["Pakora", "Bhaji", "Samosa", "Naan", "Poppadom"])
board("Butterflies you can see in Britain (watch out for moths)", "Nature", "hard", ["butterflies", "wildlife", "British nature"],
 ["Red Admiral", "Peacock", "Small Tortoiseshell", "Painted Lady", "Comma", "Brimstone", "Orange-tip", "Large White", "Small White", "Common Blue", "Meadow Brown", "Speckled Wood", "Holly Blue", "Gatekeeper", "Ringlet"],
 ["Cinnabar", "Garden Tiger", "Six-spot Burnet", "Silver Y", "Magpie"])
board("Breakfast cereals", "Food and drink", "easy", ["breakfast", "cereal", "brands"],
 ["Weetabix", "Cornflakes", "Rice Krispies", "Shreddies", "Cheerios", "Coco Pops", "Frosties", "Shredded Wheat", "Special K", "Crunchy Nut", "Bran Flakes", "Alpen", "Ready Brek", "Sugar Puffs", "Fruit 'n Fibre"],
 ["Pop-Tarts", "Belvita", "Nutella", "Marmite", "Hovis"])
board("Mammals that live in the sea", "Animals", "medium", ["sea", "mammals", "marine life"],
 ["Dolphin", "Blue whale", "Orca", "Porpoise", "Grey seal", "Sea lion", "Walrus", "Manatee", "Dugong", "Sea otter", "Narwhal", "Beluga", "Humpback whale", "Sperm whale", "Elephant seal"],
 ["Whale shark", "Basking shark", "Seahorse", "Manta ray", "Leatherback turtle"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-47.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
