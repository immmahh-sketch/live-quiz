# Bank session 10 Oct 2026: new Wipeout boards -> bank/wipeout-23.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Words that make a new word when you add 'hood' to the end", "Words and language", "easy", ["wordplay", "compound words"],
 ["Child", "Neighbour", "Man", "Brother", "Sister", "Mother", "Father", "Knight", "Priest", "False", "Boy", "Girl", "Adult", "Parent", "Saint"],
 ["Robin", "Uncle", "Cousin", "Teacher", "Doctor"])
board("Words that make a new word when you add 'dom' to the end", "Words and language", "medium", ["wordplay", "compound words"],
 ["King", "Free", "Bore", "Star", "Fan", "Martyr", "Duke", "Earl", "Serf", "Christen", "Sheikh", "Chief", "Prince", "Pope", "Ran"],
 ["Lord", "Baron", "Count", "Squire", "Bishop"])
board("Words that make a new word when you add 'age' to the end", "Words and language", "medium", ["wordplay", "suffixes"],
 ["Bond", "Band", "Short", "Pass", "Post", "Pack", "Mile", "Front", "Wreck", "Leak", "Break", "Dam", "Cab", "Foot", "Sew"],
 ["Cup", "Car", "Hand", "Book", "Pen"])
board("Words that make a new word when you add 'less' to the end", "Words and language", "easy", ["wordplay", "suffixes"],
 ["Home", "Help", "Hope", "Care", "Use", "Pain", "Price", "Fear", "Count", "Point", "End", "Heart", "Speech", "Tire", "Life"],
 ["Happy", "Sad", "Glad", "Proud", "Good"])
board("Words that make a new word when you put 'up' in front", "Words and language", "easy", ["wordplay", "compound words"],
 ["Set", "Hill", "Load", "Date", "Grade", "Right", "Stairs", "Beat", "Hold", "Keep", "Root", "Shot", "Side", "Town", "Turn"],
 ["Down", "Sky", "Top", "Floor", "High"])
board("Films starring Kate Winslet", "Film", "medium", ["Kate Winslet", "actors"],
 ["Titanic", "Sense and Sensibility", "Heavenly Creatures", "Eternal Sunshine of the Spotless Mind", "The Reader", "Revolutionary Road", "Little Children", "The Holiday", "Finding Neverland", "Iris", "Steve Jobs", "Contagion", "Avatar: The Way of Water", "Lee", "Ammonite"],
 ["Atonement", "Pride & Prejudice", "Bend It Like Beckham", "Love Actually", "Howards End"])
board("Films starring Brad Pitt", "Film", "medium", ["Brad Pitt", "actors"],
 ["Fight Club", "Se7en", "Ocean's Eleven", "Troy", "Moneyball", "Inglourious Basterds", "Once Upon a Time in Hollywood", "Mr. & Mrs. Smith", "Thelma & Louise", "Legends of the Fall", "12 Monkeys", "The Curious Case of Benjamin Button", "World War Z", "Fury", "F1"],
 ["Gravity", "Up in the Air", "The Bourne Identity", "Good Will Hunting", "Syriana"])
board("Films starring Denzel Washington", "Film", "medium", ["Denzel Washington", "actors"],
 ["Training Day", "Philadelphia", "Glory", "Malcolm X", "Man on Fire", "The Equalizer", "Remember the Titans", "Inside Man", "American Gangster", "Flight", "Fences", "Gladiator II", "Crimson Tide", "The Hurricane", "Unstoppable"],
 ["Pulp Fiction", "The Shawshank Redemption", "Driving Miss Daisy", "Jackie Brown", "Million Dollar Baby"])
board("Albums by David Bowie", "Music", "hard", ["David Bowie", "albums"],
 ["Space Oddity", "Hunky Dory", "The Rise and Fall of Ziggy Stardust", "Aladdin Sane", "Diamond Dogs", "Young Americans", "Station to Station", "Low", "\"Heroes\"", "Lodger", "Scary Monsters", "Let's Dance", "Outside", "Heathen", "Blackstar"],
 ["Electric Warrior", "Transformer", "For Your Pleasure", "Goodbye Yellow Brick Road", "Sheer Heart Attack"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-23.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'boards written')
