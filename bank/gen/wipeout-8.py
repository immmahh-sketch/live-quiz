# Bank session 10 Oct 2026: new Wipeout boards -> bank/wipeout-8.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Characters in Peaky Blinders (watch for impostors)", "Film and TV", "medium", ["Peaky Blinders", "drama"],
 ["Thomas Shelby", "Arthur Shelby", "John Shelby", "Polly Gray", "Ada Shelby", "Finn Shelby", "Michael Gray", "Grace Burgess", "Alfie Solomons", "Inspector Campbell", "Lizzie Stark", "Johnny Dogs", "Jeremiah Jesus", "Aberama Gold", "Oswald Mosley"],
 ["Maggie Shelby", "Henry Gray", "Sam Solomons", "Inspector Grant", "Eddie Shelby"])
board("Characters in Blackadder (watch for impostors)", "Comedy", "medium", ["Blackadder", "sitcoms"],
 ["Edmund Blackadder", "Baldrick", "Lord Percy", "Queenie", "Nursie", "Lord Melchett", "General Melchett", "Captain Darling", "Prince George", "Bob", "Lord Flashheart", "Mrs Miggins", "Ludwig the Indestructible", "Dr Johnson", "King Richard IV"],
 ["Sir Wilfred", "Lady Percy", "Corporal Baldwin", "Captain Flash", "Mrs Muggins"])
board("Britons who have won a Grand Slam singles title", "Tennis", "hard", ["tennis", "Grand Slams"],
 ["Andy Murray", "Emma Raducanu", "Virginia Wade", "Fred Perry", "Sue Barker", "Ann Jones", "Angela Mortimer", "Christine Truman", "Dorothy Round", "Kitty Godfree", "Laurie Doherty", "Reggie Doherty", "Arthur Gore", "Charlotte Cooper", "Dorothea Lambert Chambers"],
 ["Tim Henman", "Greg Rusedski", "Johanna Konta", "Bunny Austin", "Kyle Edmund"])
board("Scottish lochs", "Britain", "medium", ["Scotland", "lochs"],
 ["Loch Ness", "Loch Lomond", "Loch Awe", "Loch Tay", "Loch Morar", "Loch Rannoch", "Loch Katrine", "Loch Maree", "Loch Fyne", "Loch Long", "Loch Earn", "Loch Shiel", "Loch Linnhe", "Loch Leven", "Loch Arkaig"],
 ["Lough Neagh", "Lough Erne", "Lough Corrib", "Llyn Padarn", "Ullswater"])
board("Members of The Wanted, JLS, Busted or McFly", "Boy bands and girl groups", "medium", ["boy bands", "members"],
 ["Max George", "Siva Kaneswaran", "Jay McGuiness", "Tom Parker", "Nathan Sykes", "Aston Merrygold", "Oritsé Williams", "Marvin Humes", "JB Gill", "James Bourne", "Matt Willis", "Charlie Simpson", "Tom Fletcher", "Danny Jones", "Dougie Poynter"],
 ["Kian Egan", "Niall Horan", "Simon Webbe", "Lee Ryan", "Ronan Keating"])
board("Cocktails made with gin", "Food and drink", "medium", ["cocktails", "gin"],
 ["Negroni", "Martini", "Tom Collins", "Gimlet", "Bramble", "Aviation", "French 75", "Clover Club", "Singapore Sling", "Gin Fizz", "Bee's Knees", "White Lady", "Last Word", "Southside", "Martinez"],
 ["Mojito", "Margarita", "Cosmopolitan", "Manhattan", "Sidecar"])
board("Slang words for money", "Words and language", "medium", ["slang", "money"],
 ["Quid", "Fiver", "Tenner", "Grand", "Monkey", "Pony", "Ton", "Score", "Bob", "Nicker", "Dosh", "Wonga", "Bread", "Lolly", "Readies"],
 ["Clobber", "Grub", "Kip", "Gaff", "Plonk"])
board("Fells and mountains in the Lake District", "Britain", "hard", ["Lake District", "mountains"],
 ["Scafell Pike", "Helvellyn", "Skiddaw", "Great Gable", "Blencathra", "Catbells", "The Old Man of Coniston", "Fairfield", "Bowfell", "Pillar", "High Street", "Haystacks", "Great End", "Crinkle Crags", "Esk Pike"],
 ["Cross Fell", "Whernside", "The Cheviot", "Pen-y-ghent", "Ingleborough"])
board("Characters in Downton Abbey (watch for impostors)", "Film and TV", "medium", ["Downton Abbey", "drama"],
 ["Robert Crawley", "Cora Crawley", "Lady Mary", "Lady Edith", "Lady Sybil", "Violet, the Dowager Countess", "Matthew Crawley", "Carson", "Mrs Hughes", "Bates", "Anna", "Thomas Barrow", "Daisy", "Mrs Patmore", "Isobel Crawley"],
 ["Mr Hudson", "Mrs Bridges", "Lady Margaret Crawley", "Mr Pembroke", "Lady Clarissa"])
board("Spices (not herbs)", "Food and drink", "medium", ["spices", "cooking"],
 ["Cinnamon", "Nutmeg", "Cumin", "Turmeric", "Paprika", "Cardamom", "Cloves", "Saffron", "Ginger", "Star anise", "Allspice", "Fenugreek", "Mace", "Cayenne", "Sumac"],
 ["Basil", "Oregano", "Thyme", "Rosemary", "Sage"])
board("Areas of Sunderland", "The North East", "medium", ["Sunderland", "places", "North East"],
 ["Roker", "Seaburn", "Hendon", "Fulwell", "Millfield", "Pallion", "Southwick", "Monkwearmouth", "Castletown", "Hylton", "Ryhope", "Silksworth", "Grindon", "Thorney Close", "Doxford Park"],
 ["Jesmond", "Heaton", "Byker", "Benwell", "Gosforth"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-8.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'boards written')
