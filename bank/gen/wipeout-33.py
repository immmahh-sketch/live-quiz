# Bank session 10 Oct 2026: new Wipeout boards -> bank/wipeout-25.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Words that make a new word when you put 'fire' in front", "Words and language", "easy", ["wordplay", "compound words"],
 ["Work", "Man", "Place", "Fly", "Ball", "Arm", "Wood", "Wall", "Cracker", "Side", "Proof", "Guard", "Storm", "Brand", "Light"],
 ["Smoke", "Flame", "Heat", "Burn", "Ash"])
board("Words that make a new word when you put 'bed' in front", "Words and language", "medium", ["wordplay", "compound words"],
 ["Room", "Side", "Time", "Spread", "Bug", "Pan", "Rock", "Sit", "Post", "Sore", "Clothes", "Fellow", "Stead", "Roll", "Head"],
 ["Pillow", "Duvet", "Mattress", "Blanket", "Sleep"])
board("Words that make a new word when you put 'cross' in front", "Words and language", "medium", ["wordplay", "compound words"],
 ["Word", "Roads", "Bow", "Fire", "Bar", "Over", "Walk", "Bones", "Hair", "Bill", "Talk", "Wind", "Breed", "Wise", "Patch"],
 ["Line", "Point", "Path", "Box", "Gate"])
board("Films starring Steve Martin", "Film", "medium", ["Steve Martin", "actors"],
 ["The Jerk", "Planes, Trains and Automobiles", "Roxanne", "Father of the Bride", "Parenthood", "Dirty Rotten Scoundrels", "Cheaper by the Dozen", "The Pink Panther", "It's Complicated", "Bringing Down the House", "L.A. Story", "Three Amigos!", "Little Shop of Horrors", "Bowfinger", "The Man with Two Brains"],
 ["National Lampoon's Vacation", "Caddyshack", "Fletch", "Innerspace", "Ghostbusters"])
board("Films starring Dustin Hoffman", "Film", "medium", ["Dustin Hoffman", "actors"],
 ["The Graduate", "Midnight Cowboy", "Rain Man", "Tootsie", "Kramer vs. Kramer", "All the President's Men", "Marathon Man", "Hook", "Meet the Fockers", "Little Big Man", "Papillon", "Straw Dogs", "Outbreak", "Wag the Dog", "Kung Fu Panda"],
 ["Butch Cassidy and the Sundance Kid", "The Sting", "Out of Africa", "Serpico", "Scarface"])
board("Songs the Bee Gees released themselves", "Music", "hard", ["Bee Gees", "songs"],
 ["Stayin' Alive", "Night Fever", "How Deep Is Your Love", "You Should Be Dancing", "Jive Talkin'", "Tragedy", "Massachusetts", "Words", "I Started a Joke", "To Love Somebody", "More Than a Woman", "Too Much Heaven", "You Win Again", "How Can You Mend a Broken Heart", "New York Mining Disaster 1941"],
 ["Islands in the Stream", "Chain Reaction", "Grease", "Woman in Love", "Heartbreaker"])
board("Songs by Kate Bush", "Music", "medium", ["Kate Bush", "songs"],
 ["Wuthering Heights", "Running Up That Hill", "Babooshka", "Wow", "The Man with the Child in His Eyes", "Cloudbusting", "Hounds of Love", "This Woman's Work", "Army Dreamers", "Sat in Your Lap", "Don't Give Up", "Moments of Pleasure", "Rubberband Girl", "King of the Mountain", "Breathing"],
 ["Cornflake Girl", "Dog Days Are Over", "Teardrop", "Crucify", "Sweet Dreams (Are Made of This)"])
board("Songs by the Police", "Music", "medium", ["The Police", "songs"],
 ["Roxanne", "Every Breath You Take", "Message in a Bottle", "Walking on the Moon", "Don't Stand So Close to Me", "Every Little Thing She Does Is Magic", "Spirits in the Material World", "Invisible Sun", "King of Pain", "Wrapped Around Your Finger", "Can't Stand Losing You", "So Lonely", "De Do Do Do, De Da Da Da", "Synchronicity II", "Bring On the Night"],
 ["Englishman in New York", "Fields of Gold", "Desert Rose", "If You Love Somebody Set Them Free", "Shape of My Heart"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-33.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'boards written')
