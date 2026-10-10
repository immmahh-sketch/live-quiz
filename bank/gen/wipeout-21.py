# Bank session 10 Oct 2026: new Wipeout boards -> bank/wipeout-21.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Words that make a new word when you add 'line' to the end", "Words and language", "easy", ["wordplay", "compound words"],
 ["Hem", "Head", "Dead", "Life", "Hot", "Air", "Coast", "Out", "Pipe", "Guide", "Base", "Sky", "Under", "Story", "Punch"],
 ["Rope", "String", "Wire", "Cord", "Thread"])
board("Words that make a new word when you add 'way' to the end", "Words and language", "easy", ["wordplay", "compound words"],
 ["Motor", "Path", "Door", "Run", "High", "Rail", "Sub", "Gang", "Express", "Hall", "Stair", "Walk", "Water", "Mid", "Cause"],
 ["Road", "Street", "Lane", "Track", "Avenue"])
board("Words that make a new word when you put 'star' in front", "Words and language", "medium", ["wordplay", "compound words"],
 ["Fish", "Light", "Dust", "Board", "Gazer", "Ship", "Struck", "Burst", "Ling", "Dom", "Let", "Lit", "Fruit", "Gaze", "Flower"],
 ["Moon", "Sun", "Sky", "Planet", "Night"])
board("Films starring Robin Williams", "Film", "medium", ["Robin Williams", "actors"],
 ["Mrs Doubtfire", "Good Will Hunting", "Dead Poets Society", "Jumanji", "Hook", "Good Morning, Vietnam", "Aladdin", "Patch Adams", "Jack", "Flubber", "The Birdcage", "Night at the Museum", "One Hour Photo", "Insomnia", "Awakenings"],
 ["The Mask", "Ace Ventura", "Liar Liar", "The Truman Show", "Bruce Almighty"])
board("Films starring Will Smith", "Film", "medium", ["Will Smith", "actors"],
 ["Men in Black", "Independence Day", "Bad Boys", "The Pursuit of Happyness", "I Am Legend", "Hancock", "Ali", "Enemy of the State", "Wild Wild West", "Hitch", "I, Robot", "King Richard", "Shark Tale", "Suicide Squad", "Seven Pounds"],
 ["Beverly Hills Cop", "Coming to America", "Trading Places", "The Nutty Professor", "Dr. Dolittle"])
board("Films directed by Guy Ritchie", "Film", "medium", ["Guy Ritchie", "directors"],
 ["Lock, Stock and Two Smoking Barrels", "Snatch", "Swept Away", "Revolver", "RocknRolla", "Sherlock Holmes", "Sherlock Holmes: A Game of Shadows", "The Man from U.N.C.L.E.", "King Arthur: Legend of the Sword", "Aladdin (2019)", "The Gentlemen", "Wrath of Man", "Operation Fortune", "The Covenant", "The Ministry of Ungentlemanly Warfare"],
 ["Layer Cake", "Kick-Ass", "Kingsman: The Secret Service", "Stardust", "X-Men: First Class"])
board("Michael Jackson solo songs that aren't on 'Thriller'", "Music", "medium", ["Michael Jackson", "songs"],
 ["Bad", "Smooth Criminal", "Man in the Mirror", "Black or White", "Earth Song", "Don't Stop 'Til You Get Enough", "Rock with You", "The Way You Make Me Feel", "Dirty Diana", "Heal the World", "You Are Not Alone", "Remember the Time", "Scream", "They Don't Care About Us", "Off the Wall"],
 ["Purple Rain", "When Doves Cry", "Kiss", "Raspberry Beret", "Sign o' the Times"])
board("Songs by Madonna", "Music", "medium", ["Madonna", "songs"],
 ["Like a Prayer", "Like a Virgin", "Vogue", "Material Girl", "Holiday", "Into the Groove", "La Isla Bonita", "Papa Don't Preach", "Frozen", "Ray of Light", "Music", "Hung Up", "Express Yourself", "True Blue", "Crazy for You"],
 ["Girls Just Want to Have Fun", "Time After Time", "Can't Get You Out of My Head", "Spinning Around", "Total Eclipse of the Heart"])
board("Films starring Daniel Craig, apart from Bond", "Film", "hard", ["Daniel Craig", "actors"],
 ["Knives Out", "Glass Onion", "Wake Up Dead Man", "Layer Cake", "Munich", "The Girl with the Dragon Tattoo", "Logan Lucky", "Defiance", "Elizabeth", "Road to Perdition", "Enduring Love", "Lara Croft: Tomb Raider", "The Golden Compass", "Cowboys & Aliens", "Queer"],
 ["The Thomas Crown Affair", "Mrs Doubtfire", "The Untouchables", "The Rock", "Mamma Mia!"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-21.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'boards written')
