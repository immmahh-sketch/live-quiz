# Bank session 10 Oct 2026: new Wipeout boards -> bank/wipeout-18.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Words that make a new word when you add 'work' to the end", "Words and language", "easy", ["wordplay", "compound words"],
 ["Home", "House", "Net", "Frame", "Fire", "Wood", "Clock", "Team", "Patch", "Paper", "Needle", "Ground", "Leg", "Art", "Guess"],
 ["Office", "Job", "Car", "Chair", "Shop"])
board("Words that make a new word when you add 'time' to the end", "Words and language", "easy", ["wordplay", "compound words"],
 ["Bed", "Lunch", "Tea", "Night", "Day", "Summer", "Winter", "Half", "Over", "Play", "Pass", "Life", "Show", "War", "Spring"],
 ["Week", "Year", "Hour", "Morning", "Evening"])
board("Words that make a new word when you add 'bag' to the end", "Words and language", "medium", ["wordplay", "compound words"],
 ["Hand", "Sand", "Bean", "Tea", "Wind", "Gas", "Rag", "Saddle", "Mail", "Air", "Punch", "Kit", "Nose", "Carpet", "School"],
 ["Shop", "Bin", "Food", "Pocket", "Plastic"])
board("Words that make a new word when you add 'fire' to the end", "Words and language", "medium", ["wordplay", "compound words"],
 ["Bon", "Camp", "Wild", "Gun", "Cross", "Back", "Cease", "Mis", "Spit", "Hell", "Quick", "Sure", "Brush", "Hang", "Grass"],
 ["Log", "Coal", "Forest", "Candle", "Smoke"])
board("TV dramas and comedies set in a hospital", "Film and TV", "medium", ["TV", "hospitals"],
 ["Casualty", "Holby City", "ER", "Grey's Anatomy", "Scrubs", "House", "M*A*S*H", "Chicago Med", "The Good Doctor", "Green Wing", "St Elsewhere", "Chicago Hope", "General Hospital", "The Pitt", "The Royal"],
 ["The Bill", "Line of Duty", "Suits", "Law & Order", "Silent Witness"])
board("TV shows set or made in the North East", "The North East", "medium", ["TV", "North East"],
 ["Byker Grove", "Vera", "Spender", "The Likely Lads", "Our Friends in the North", "55 Degrees North", "Geordie Shore", "When the Boat Comes In", "Inspector George Gently", "Sunderland 'Til I Die", "Crocodile Shoes", "The Tube", "The Dumping Ground", "Wolfblood", "Hebburn"],
 ["Coronation Street", "Emmerdale", "Heartbeat", "Last of the Summer Wine", "The Royle Family"])
board("TV shows set in London", "Film and TV", "medium", ["TV", "London"],
 ["EastEnders", "The Bill", "Only Fools and Horses", "Sherlock", "Luther", "Peep Show", "The IT Crowd", "Fleabag", "Absolutely Fabulous", "Spooks", "Top Boy", "Call the Midwife", "Black Books", "Bodyguard", "Ted Lasso"],
 ["Gavin & Stacey", "Shameless", "Still Game", "Derry Girls", "Peaky Blinders"])
board("Films directed by Ridley Scott", "Film", "medium", ["Ridley Scott", "directors"],
 ["Alien", "Blade Runner", "Thelma & Louise", "Gladiator", "Black Hawk Down", "Hannibal", "Kingdom of Heaven", "American Gangster", "Prometheus", "The Martian", "Napoleon", "Legend", "The Duellists", "G.I. Jane", "House of Gucci"],
 ["Top Gun", "Man on Fire", "Crimson Tide", "True Romance", "Days of Thunder"])
board("Films starring Leonardo DiCaprio", "Film", "medium", ["Leonardo DiCaprio", "actors"],
 ["Titanic", "Inception", "The Revenant", "The Wolf of Wall Street", "Catch Me If You Can", "The Departed", "Shutter Island", "Django Unchained", "The Great Gatsby", "Romeo + Juliet", "Blood Diamond", "The Beach", "Revolutionary Road", "Don't Look Up", "What's Eating Gilbert Grape"],
 ["Fight Club", "The Talented Mr. Ripley", "Gladiator", "Interstellar", "Good Will Hunting"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-18.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'boards written')
