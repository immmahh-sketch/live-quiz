# Bank session 10 Oct 2026: new Wipeout boards -> bank/wipeout-25.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Words that make a new word when you add 'shot' to the end", "Words and language", "medium", ["wordplay", "compound words"],
 ["Snap", "Mug", "Gun", "Long", "Big", "Ear", "Sling", "Bird", "Grape", "Moon", "Buck", "Hot", "Over", "Pot", "Screen"],
 ["Photo", "Picture", "Bullet", "Arrow", "Drink"])
board("Words that make a new word when you add 'boat' to the end", "Words and language", "easy", ["wordplay", "compound words"],
 ["Life", "Steam", "Speed", "House", "Row", "Sail", "Motor", "Gun", "Show", "Dream", "Long", "Tug", "River", "Paddle", "Ferry"],
 ["Ship", "Yacht", "Canoe", "Raft", "Sea"])
board("Words that make a new word when you add 'top' to the end", "Words and language", "easy", ["wordplay", "compound words"],
 ["Lap", "Desk", "Table", "Roof", "Hill", "Tree", "Mountain", "Tip", "Work", "Counter", "Hard", "Black", "Flat", "Stove", "Cliff"],
 ["Bottom", "Peak", "Summit", "Lid", "Cap"])
board("Films starring Ben Stiller", "Film", "medium", ["Ben Stiller", "actors"],
 ["Night at the Museum", "Zoolander", "Meet the Parents", "Meet the Fockers", "There's Something About Mary", "Dodgeball", "Tropic Thunder", "The Secret Life of Walter Mitty", "Reality Bites", "The Royal Tenenbaums", "Starsky & Hutch", "Along Came Polly", "Madagascar", "Mystery Men", "Heavyweights"],
 ["Wedding Crashers", "Old School", "Elf", "Step Brothers", "Talladega Nights"])
board("Films starring Emma Stone", "Film", "medium", ["Emma Stone", "actors"],
 ["La La Land", "Easy A", "The Help", "Birdman", "Superbad", "Zombieland", "Crazy, Stupid, Love", "The Amazing Spider-Man", "Poor Things", "The Favourite", "Cruella", "Battle of the Sexes", "Kinds of Kindness", "Bugonia", "The Croods"],
 ["Silver Linings Playbook", "The Hunger Games", "Joy", "Passengers", "Don't Look Up"])
board("Films starring Tom Hardy", "Film", "medium", ["Tom Hardy", "actors"],
 ["Bronson", "Inception", "Warrior", "Tinker Tailor Soldier Spy", "The Dark Knight Rises", "Locke", "Mad Max: Fury Road", "Legend", "The Revenant", "Dunkirk", "Venom", "Lawless", "Star Trek: Nemesis", "The Drop", "The Bikeriders"],
 ["American Psycho", "The Prestige", "Ford v Ferrari", "Shame", "12 Years a Slave"])
board("Songs by the Rolling Stones", "Music", "medium", ["Rolling Stones", "songs"],
 ["(I Can't Get No) Satisfaction", "Paint It Black", "Jumpin' Jack Flash", "Honky Tonk Women", "Brown Sugar", "Angie", "Start Me Up", "Gimme Shelter", "Sympathy for the Devil", "Wild Horses", "Ruby Tuesday", "You Can't Always Get What You Want", "Get Off of My Cloud", "Miss You", "Under My Thumb"],
 ["My Generation", "Pinball Wizard", "You Really Got Me", "Waterloo Sunset", "Lola"])
board("Songs by Fleetwood Mac", "Music", "hard", ["Fleetwood Mac", "songs"],
 ["Dreams", "Go Your Own Way", "Rhiannon", "The Chain", "Landslide", "Everywhere", "Little Lies", "Don't Stop", "Albatross", "Big Love", "Seven Wonders", "Tusk", "Sara", "Gypsy", "Songbird"],
 ["Edge of Seventeen", "Stand Back", "Hotel California", "Heart of Glass", "Africa"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-28.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'boards written')
