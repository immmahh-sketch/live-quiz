# Bank session 10 Oct 2026: new Wipeout boards -> bank/wipeout-25.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Words that make a new word when you add 'stick' to the end", "Words and language", "easy", ["wordplay", "compound words"],
 ["Chop", "Drum", "Joy", "Lip", "Match", "Yard", "Broom", "Candle", "Slap", "Dip", "Gear", "Fiddle", "Night", "Bread", "Glow"],
 ["Pencil", "Twig", "Branch", "Rod", "Pole"])
board("Words that make a new word when you add 'field' to the end", "Words and language", "medium", ["wordplay", "compound words"],
 ["Battle", "Mine", "Corn", "Air", "Mid", "Out", "In", "Snow", "Ice", "Wheat", "Coal", "Gold", "Oil", "Wake", "Spring"],
 ["Farm", "Grass", "Meadow", "Park", "Garden"])
board("Films starring Nicole Kidman", "Film", "medium", ["Nicole Kidman", "actors"],
 ["Moulin Rouge!", "The Hours", "Eyes Wide Shut", "The Others", "Practical Magic", "Days of Thunder", "Far and Away", "Cold Mountain", "Dogville", "Lion", "Bewitched", "Paddington", "The Golden Compass", "Aquaman", "Dead Calm"],
 ["Elizabeth", "Blue Jasmine", "Mulholland Drive", "King Kong", "The Ring"])
board("Films starring Matt Damon", "Film", "medium", ["Matt Damon", "actors"],
 ["Good Will Hunting", "Saving Private Ryan", "The Talented Mr. Ripley", "The Bourne Identity", "Ocean's Eleven", "The Departed", "The Martian", "Interstellar", "Invictus", "Elysium", "We Bought a Zoo", "Ford v Ferrari", "Oppenheimer", "Contagion", "True Grit"],
 ["Argo", "Gone Girl", "Pearl Harbor", "Armageddon", "The Town"])
board("Films starring Jack Nicholson", "Film", "medium", ["Jack Nicholson", "actors"],
 ["One Flew Over the Cuckoo's Nest", "The Shining", "Chinatown", "Batman", "A Few Good Men", "As Good as It Gets", "Terms of Endearment", "Easy Rider", "Five Easy Pieces", "The Departed", "Something's Gotta Give", "About Schmidt", "The Bucket List", "Anger Management", "The Witches of Eastwick"],
 ["Taxi Driver", "The Godfather", "Rain Man", "Apocalypse Now", "Scarface"])
board("Films starring Judi Dench", "Film", "medium", ["Judi Dench", "actors"],
 ["Shakespeare in Love", "Mrs Brown", "Iris", "Notes on a Scandal", "Philomena", "Chocolat", "Skyfall", "GoldenEye", "Belfast", "The Best Exotic Marigold Hotel", "Pride & Prejudice", "Mrs Henderson Presents", "Victoria & Abdul", "Cats", "Murder on the Orient Express"],
 ["The Prime of Miss Jean Brodie", "Gosford Park", "Sister Act", "The Lady in the Van", "California Suite"])
board("Oasis songs that never reached number one", "Music", "medium", ["Oasis", "songs", "Britpop"],
 ["Wonderwall", "Live Forever", "Supersonic", "Champagne Supernova", "Roll with It", "Cigarettes & Alcohol", "Whatever", "Stand by Me", "Half the World Away", "Little by Little", "Stop Crying Your Heart Out", "The Masterplan", "Slide Away", "Rock 'n' Roll Star", "Morning Glory"],
 ["Parklife", "Song 2", "Common People", "Disco 2000", "Bitter Sweet Symphony"])
board("Robbie Williams solo hits", "Music", "medium", ["Robbie Williams", "songs"],
 ["Angels", "Let Me Entertain You", "Millennium", "She's the One", "Rock DJ", "Feel", "Kids", "Strong", "No Regrets", "Supreme", "Eternity", "Candy", "Come Undone", "Tripping", "Old Before I Die"],
 ["Back for Good", "Patience", "Shine", "Never Forget", "Pray"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-27.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'boards written')
