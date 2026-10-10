# Bank session 10 Oct 2026: new Wipeout boards -> bank/wipeout-14.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Breeds of horse or pony", "Animals", "medium", ["horses", "ponies", "breeds"],
 ["Shetland", "Clydesdale", "Shire", "Arabian", "Thoroughbred", "Appaloosa", "Mustang", "Welsh Cob", "Exmoor", "Dartmoor", "Connemara", "Percheron", "Lipizzaner", "Andalusian", "Fell"],
 ["Palomino", "Piebald", "Skewbald", "Dapple grey", "Chestnut"])
board("Fictional pubs and bars from TV, film and books", "Film and TV", "medium", ["pubs", "fictional places"],
 ["The Queen Vic", "The Rovers Return", "The Woolpack", "The Nag's Head", "The Winchester", "The Slaughtered Lamb", "The Leaky Cauldron", "The Prancing Pony", "The Green Dragon", "The Bull (Ambridge)", "The Three Broomsticks", "The Hog's Head", "The Dog in the Pond", "Moe's Tavern", "Cheers"],
 ["The Eagle and Child", "Ye Olde Trip to Jerusalem", "The Lamb and Flag", "The Prospect of Whitby", "The Grenadier"])
board("Birds whose name is also a verb", "Words and language", "medium", ["birds", "words", "verbs"],
 ["Duck", "Swallow", "Crane", "Rook", "Grouse", "Lark", "Hawk", "Quail", "Snipe", "Gull", "Crow", "Parrot", "Kite", "Swan", "Cock"],
 ["Robin", "Wren", "Finch", "Heron", "Thrush"])
board("Countries whose capital is NOT their biggest city", "World geography", "hard", ["capitals", "cities", "countries"],
 ["Australia", "Canada", "USA", "Brazil", "Turkey", "Switzerland", "New Zealand", "Nigeria", "Pakistan", "South Africa", "Morocco", "Vietnam", "Tanzania", "Kazakhstan", "Malta"],
 ["United Kingdom", "France", "Japan", "Argentina", "Egypt"])
board("Shades of green", "Art and design", "medium", ["colours", "green"],
 ["Emerald", "Olive", "Lime", "Jade", "Sage", "Mint", "Bottle green", "Forest green", "Pea green", "Racing green", "Sea green", "Chartreuse", "Avocado", "Viridian", "Pistachio"],
 ["Ochre", "Magenta", "Cerise", "Burgundy", "Mauve"])
board("Fish whose name is also an everyday English word", "Words and language", "hard", ["fish", "words"],
 ["Sole", "Skate", "Ray", "Pike", "Perch", "Carp", "Bass", "Dab", "Flounder", "Brill", "Char", "Mullet", "Tang", "Ling", "Grunt"],
 ["Haddock", "Halibut", "Mackerel", "Turbot", "Anchovy"])
board("Countries whose currency is a dollar (their own or the US one)", "World geography", "hard", ["currencies", "dollars", "countries"],
 ["USA", "Canada", "Australia", "New Zealand", "Singapore", "Jamaica", "Bahamas", "Barbados", "Fiji", "Ecuador", "El Salvador", "Taiwan", "Namibia", "Belize", "Brunei"],
 ["Mexico", "Philippines", "South Africa", "India", "Malaysia"])
board("Words that make a new word when you add 'cake' to the end", "Words and language", "medium", ["wordplay", "compound words"],
 ["Cup", "Pan", "Cheese", "Fruit", "Short", "Fish", "Tea", "Oat", "Beef", "Hot", "Griddle", "Moon", "Johnny", "Seed", "Oil"],
 ["Plate", "Pie", "Bowl", "Bread", "Milk"])
board("Words that make a new word when you add 'book' to the end", "Words and language", "easy", ["wordplay", "compound words"],
 ["Note", "Text", "Hand", "Guide", "Scrap", "Cook", "Pass", "Log", "Story", "Year", "Phrase", "Face", "Pocket", "Sketch", "Hymn"],
 ["Pen", "Desk", "Shelf", "Page", "Ink"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-14.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'boards written')
