# Bank session 10 Oct 2026: new Wipeout boards -> bank/wipeout-25.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Words that make a new word when you add 'tail' to the end", "Words and language", "medium", ["wordplay", "compound words"],
 ["Pony", "Pig", "Cock", "Swallow", "Dove", "Fish", "Coat", "Ox", "Bob", "Cotton", "Shirt", "Horse", "Wag", "Ring", "Fan"],
 ["Lion", "Tiger", "Cow", "Goat", "Sheep"])
board("Words that make a new word when you add 'worm' to the end", "Words and language", "medium", ["wordplay", "compound words"],
 ["Earth", "Silk", "Book", "Glow", "Ring", "Tape", "Hook", "Wood", "Lug", "Inch", "Blood", "Flat", "Round", "Meal", "Wire"],
 ["Slug", "Snail", "Grub", "Maggot", "Caterpillar"])
board("Films starring Kevin Costner", "Film", "medium", ["Kevin Costner", "actors"],
 ["Dances with Wolves", "The Bodyguard", "Robin Hood: Prince of Thieves", "Field of Dreams", "The Untouchables", "JFK", "Waterworld", "The Postman", "Bull Durham", "Tin Cup", "No Way Out", "Open Range", "Hidden Figures", "Thirteen Days", "Wyatt Earp"],
 ["Braveheart", "Lethal Weapon", "Witness", "The Fugitive", "Mad Max"])
board("Films starring Clint Eastwood", "Film", "medium", ["Clint Eastwood", "actors", "westerns"],
 ["Dirty Harry", "The Good, the Bad and the Ugly", "A Fistful of Dollars", "For a Few Dollars More", "Unforgiven", "Gran Torino", "Million Dollar Baby", "Where Eagles Dare", "Escape from Alcatraz", "The Outlaw Josey Wales", "Every Which Way but Loose", "In the Line of Fire", "The Bridges of Madison County", "Kelly's Heroes", "Pale Rider"],
 ["True Grit", "The Searchers", "Stagecoach", "Rio Bravo", "The Magnificent Seven"])
board("Stevie Wonder hits", "Music", "medium", ["Stevie Wonder", "songs", "Motown"],
 ["Superstition", "Sir Duke", "Isn't She Lovely", "I Just Called to Say I Love You", "Signed, Sealed, Delivered I'm Yours", "You Are the Sunshine of My Life", "Higher Ground", "Living for the City", "Master Blaster (Jammin')", "Happy Birthday", "Uptight (Everything's Alright)", "My Cherie Amour", "Part-Time Lover", "I Wish", "For Once in My Life"],
 ["What's Going On", "Sexual Healing", "Hello", "All Night Long", "Easy"])
board("Songs written by Bob Dylan", "Music", "hard", ["Bob Dylan", "songs"],
 ["Blowin' in the Wind", "Like a Rolling Stone", "The Times They Are a-Changin'", "Mr. Tambourine Man", "Knockin' on Heaven's Door", "Lay Lady Lay", "Subterranean Homesick Blues", "Just Like a Woman", "Tangled Up in Blue", "Hurricane", "All Along the Watchtower", "Make You Feel My Love", "Forever Young", "A Hard Rain's a-Gonna Fall", "Positively 4th Street"],
 ["Hallelujah", "Suzanne", "So Long, Marianne", "The Sound of Silence", "Mrs. Robinson"])
board("Types of rice", "Food and drink", "hard", ["rice", "cooking"],
 ["Basmati", "Jasmine", "Arborio", "Carnaroli", "Brown", "Long-grain", "Pudding", "Glutinous", "Bomba", "Sushi", "Camargue red", "Black", "Patna", "Vialone Nano", "Calasparra"],
 ["Couscous", "Bulgur", "Quinoa", "Orzo", "Pearl barley"])
board("Cocktails made with whisky", "Food and drink", "hard", ["cocktails", "whisky"],
 ["Old Fashioned", "Manhattan", "Whisky Sour", "Mint Julep", "Rob Roy", "Sazerac", "Rusty Nail", "Irish Coffee", "Hot Toddy", "Boulevardier", "Penicillin", "Godfather", "Blood and Sand", "Whisky Mac", "Highball"],
 ["Negroni", "Sidecar", "Margarita", "Mojito", "Martini"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-30.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'boards written')
