# Bank session 10 Oct 2026: new Wipeout boards -> bank/wipeout-24.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Words that make a new word when you add 'mate' to the end", "Words and language", "easy", ["wordplay", "compound words"],
 ["Class", "Room", "Ship", "Team", "Play", "Flat", "Check", "Stale", "Help", "House", "Work", "Bunk", "School", "Cell", "Soul"],
 ["Friend", "Pal", "Best", "Brother", "Partner"])
board("Words that make a new word when you add 'fall' to the end", "Words and language", "easy", ["wordplay", "compound words"],
 ["Water", "Rain", "Snow", "Down", "Night", "Short", "Wind", "Land", "Foot", "Pit", "Free", "Prat", "Out", "Rock", "Ice"],
 ["Sky", "Sun", "Cloud", "Storm", "Fog"])
board("Words that make a new word when you add 'hand' to the end", "Words and language", "easy", ["wordplay", "compound words"],
 ["Back", "Fore", "Left", "Right", "Second", "Under", "Over", "Farm", "Deck", "Stage", "Short", "Long", "Off", "Upper", "Free"],
 ["Arm", "Leg", "Finger", "Wrist", "Thumb"])
board("Words that make a new word when you add 'mark' to the end", "Words and language", "medium", ["wordplay", "compound words"],
 ["Book", "Hall", "Land", "Bench", "Birth", "Post", "Trade", "Water", "Pock", "Ear", "Check", "Tide", "Den", "Way", "Foot"],
 ["Pen", "Ink", "Spot", "Dot", "Line"])
board("Films starring Morgan Freeman", "Film", "medium", ["Morgan Freeman", "actors"],
 ["The Shawshank Redemption", "Se7en", "Driving Miss Daisy", "Million Dollar Baby", "Glory", "Invictus", "Bruce Almighty", "Deep Impact", "The Dark Knight", "Lucy", "Now You See Me", "Kiss the Girls", "Robin Hood: Prince of Thieves", "Unforgiven", "Evan Almighty"],
 ["Training Day", "In the Heat of the Night", "Philadelphia", "Guess Who's Coming to Dinner", "Malcolm X"])
board("Films starring Emma Thompson", "Film", "medium", ["Emma Thompson", "actors"],
 ["Sense and Sensibility", "Howards End", "The Remains of the Day", "Love Actually", "Nanny McPhee", "Saving Mr. Banks", "Stranger than Fiction", "Harry Potter and the Prisoner of Azkaban", "In the Name of the Father", "Primary Colors", "Cruella", "Matilda the Musical", "Good Luck to You, Leo Grande", "Last Christmas", "Much Ado About Nothing"],
 ["Titanic", "The Reader", "The Holiday", "Notes on a Scandal", "Iris"])
board("Films directed by the Coen brothers", "Film", "hard", ["Coen brothers", "directors"],
 ["Blood Simple", "Raising Arizona", "Miller's Crossing", "Barton Fink", "The Hudsucker Proxy", "Fargo", "The Big Lebowski", "O Brother, Where Art Thou?", "The Man Who Wasn't There", "Intolerable Cruelty", "No Country for Old Men", "Burn After Reading", "A Serious Man", "True Grit", "Inside Llewyn Davis"],
 ["Pulp Fiction", "Reservoir Dogs", "Jackie Brown", "Django Unchained", "Death Proof"])
board("Films directed by Tim Burton", "Film", "medium", ["Tim Burton", "directors"],
 ["Beetlejuice", "Batman", "Edward Scissorhands", "Batman Returns", "Ed Wood", "Mars Attacks!", "Sleepy Hollow", "Big Fish", "Charlie and the Chocolate Factory", "Corpse Bride", "Sweeney Todd", "Alice in Wonderland", "Frankenweenie", "Dark Shadows", "Dumbo"],
 ["The Nightmare Before Christmas", "Coraline", "Labyrinth", "The Addams Family", "Hook"])
board("Albums by Queen", "Music", "hard", ["Queen", "albums"],
 ["Queen II", "Sheer Heart Attack", "A Night at the Opera", "A Day at the Races", "News of the World", "Jazz", "The Game", "Flash Gordon", "Hot Space", "The Works", "A Kind of Magic", "The Miracle", "Innuendo", "Made in Heaven", "Queen"],
 ["The Rise and Fall of Ziggy Stardust", "Out of the Blue", "Bat Out of Hell", "Hotel California", "Rumours"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-24.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'boards written')
