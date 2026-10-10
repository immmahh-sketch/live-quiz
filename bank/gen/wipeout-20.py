# Bank session 10 Oct 2026: new Wipeout boards -> bank/wipeout-20.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Words that make a new word when you add 'wood' to the end", "Words and language", "medium", ["wordplay", "compound words"],
 ["Holly", "Fire", "Drift", "Hard", "Soft", "Ply", "Dog", "Sandal", "Heart", "Brush", "Worm", "Dead", "Match", "Box", "Red"],
 ["Tree", "Leaf", "Branch", "Stick", "Log"])
board("Words that make a new word when you add 'bird' to the end", "Words and language", "medium", ["wordplay", "birds"],
 ["Black", "Blue", "Song", "Sea", "Jail", "Lady", "Love", "Humming", "Mocking", "Thunder", "Cat", "Lyre", "Bower", "Weaver", "Shore"],
 ["Wing", "Nest", "Feather", "Egg", "Tree"])
board("Characters created by Charles Dickens (not in A Christmas Carol)", "Books", "medium", ["Dickens", "characters"],
 ["Fagin", "Oliver Twist", "Pip", "Miss Havisham", "Mr Micawber", "Uriah Heep", "Little Nell", "Bill Sikes", "The Artful Dodger", "Mr Pickwick", "Mrs Gamp", "Sydney Carton", "Madame Defarge", "Mr Gradgrind", "Abel Magwitch"],
 ["Becky Sharp", "Heathcliff", "Dorian Gray", "Mr Rochester", "Tess Durbeyfield"])
board("Characters created by Jane Austen", "Books", "medium", ["Jane Austen", "characters"],
 ["Elizabeth Bennet", "Mr Darcy", "Emma Woodhouse", "Mr Knightley", "Anne Elliot", "Captain Wentworth", "Elinor Dashwood", "Marianne Dashwood", "Mr Collins", "Mr Wickham", "Fanny Price", "Catherine Morland", "Lady Catherine de Bourgh", "Mr Bingley", "Harriet Smith"],
 ["Heathcliff", "Mr Rochester", "Cathy Earnshaw", "Jane Eyre", "Bertha Mason"])
board("Hobbits (and hobbit-folk) in Tolkien", "Books", "hard", ["Tolkien", "hobbits"],
 ["Bilbo Baggins", "Frodo Baggins", "Samwise Gamgee", "Merry Brandybuck", "Pippin Took", "Rosie Cotton", "Lobelia Sackville-Baggins", "Farmer Maggot", "The Gaffer (Hamfast Gamgee)", "Fatty Bolger", "The Old Took", "Déagol", "Sméagol", "Otho Sackville-Baggins", "Lotho Sackville-Baggins"],
 ["Thorin", "Gimli", "Balin", "Bombur", "Dwalin"])
board("Characters from Sesame Street", "Film and TV", "easy", ["Sesame Street", "puppets"],
 ["Big Bird", "Elmo", "Cookie Monster", "Oscar the Grouch", "Bert", "Ernie", "Grover", "The Count", "Mr Snuffleupagus", "Zoe", "Abby Cadabby", "Telly Monster", "Rosita", "Herry Monster", "Baby Bear"],
 ["Fozzie Bear", "Gonzo", "Animal", "Miss Piggy", "The Swedish Chef"])
board("Members of the Order of the Phoenix", "Harry Potter", "medium", ["Harry Potter", "Order of the Phoenix"],
 ["Albus Dumbledore", "Sirius Black", "Remus Lupin", "Mad-Eye Moody", "Nymphadora Tonks", "Kingsley Shacklebolt", "Arthur Weasley", "Molly Weasley", "Bill Weasley", "Severus Snape", "Minerva McGonagall", "Rubeus Hagrid", "Mundungus Fletcher", "Dedalus Diggle", "Aberforth Dumbledore"],
 ["Lucius Malfoy", "Bellatrix Lestrange", "Cornelius Fudge", "Dolores Umbridge", "Horace Slughorn"])
board("Names of Royal Navy ships (HMS ___)", "History", "hard", ["Royal Navy", "ships"],
 ["Victory", "Ark Royal", "Belfast", "Hood", "Bounty", "Beagle", "Endeavour", "Warrior", "Invincible", "Illustrious", "Queen Elizabeth", "Prince of Wales", "Dreadnought", "Sheffield", "Conqueror"],
 ["Bismarck", "Titanic", "Lusitania", "Cutty Sark", "Mayflower"])
board("Mountains in Wales", "Wales", "hard", ["Wales", "mountains"],
 ["Snowdon", "Cadair Idris", "Pen y Fan", "Tryfan", "Glyder Fawr", "Glyder Fach", "Carnedd Llewelyn", "Carnedd Dafydd", "Crib Goch", "Y Garn", "Moel Siabod", "Aran Fawddwy", "Pumlumon", "Corn Du", "Foel Cwmcerwyn"],
 ["Helvellyn", "Skiddaw", "Ben Lomond", "Scafell Pike", "Ben Macdui"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-20.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'boards written')
