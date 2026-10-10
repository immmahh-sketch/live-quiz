# Bank session 10 Oct 2026: new Wipeout boards -> bank/wipeout-42.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Films starring Bradley Cooper", "Film", "medium", ["Bradley Cooper", "films"],
 ["The Hangover", "Silver Linings Playbook", "American Sniper", "A Star Is Born", "Limitless", "American Hustle", "Wedding Crashers", "The A-Team", "Guardians of the Galaxy", "Burnt", "Nightmare Alley", "Licorice Pizza", "Maestro", "He's Just Not That into You", "The Place Beyond the Pines"],
 ["Crazy, Stupid, Love.", "The Wolf of Wall Street", "Zoolander", "Old School", "Knocked Up"])
board("Films starring Jake Gyllenhaal", "Film", "medium", ["Jake Gyllenhaal", "films"],
 ["Donnie Darko", "Brokeback Mountain", "Nightcrawler", "Zodiac", "Prisoners", "The Day After Tomorrow", "Source Code", "Southpaw", "Spider-Man: Far From Home", "Jarhead", "Nocturnal Animals", "End of Watch", "Road House", "October Sky", "Okja"],
 ["Fight Club", "Memento", "Se7en", "Shutter Island", "Drive"])
board("Films starring Nicolas Cage", "Film", "medium", ["Nicolas Cage", "films"],
 ["Face/Off", "Con Air", "The Rock", "Leaving Las Vegas", "National Treasure", "Moonstruck", "Raising Arizona", "Gone in 60 Seconds", "Ghost Rider", "Adaptation", "Kick-Ass", "Wild at Heart", "Pig", "Mandy", "The Wicker Man"],
 ["Speed", "Die Hard", "Point Break", "Armageddon", "The Fifth Element"])
board("Films starring Jennifer Lawrence", "Film", "easy", ["Jennifer Lawrence", "films"],
 ["The Hunger Games", "Silver Linings Playbook", "Winter's Bone", "American Hustle", "Joy", "X-Men: First Class", "Passengers", "Red Sparrow", "Don't Look Up", "Mother!", "No Hard Feelings", "The Hunger Games: Catching Fire", "The Hunger Games: Mockingjay – Part 1", "The Hunger Games: Mockingjay – Part 2", "Causeway"],
 ["Twilight", "Divergent", "La La Land", "Black Swan", "The Maze Runner"])
board("Films starring Natalie Portman", "Film", "medium", ["Natalie Portman", "films"],
 ["Léon", "Black Swan", "V for Vendetta", "Closer", "Jackie", "Thor", "Star Wars: Episode I – The Phantom Menace", "Garden State", "Annihilation", "Heat", "Mars Attacks!", "The Other Boleyn Girl", "No Strings Attached", "May December", "Beautiful Girls"],
 ["Pride and Prejudice", "Atonement", "Amélie", "Gravity", "The Devil Wears Prada"])
board("Films starring Angelina Jolie", "Film", "easy", ["Angelina Jolie", "films"],
 ["Lara Croft: Tomb Raider", "Mr. & Mrs. Smith", "Maleficent", "Girl, Interrupted", "Wanted", "Salt", "Changeling", "Gone in 60 Seconds", "Hackers", "Kung Fu Panda", "Eternals", "The Tourist", "Alexander", "A Mighty Heart", "Maria"],
 ["Charlie's Angels", "Kill Bill", "Resident Evil", "Underworld", "Catwoman"])
board("Films starring Cameron Diaz", "Film", "easy", ["Cameron Diaz", "films"],
 ["There's Something About Mary", "The Mask", "Charlie's Angels", "Shrek", "The Holiday", "Being John Malkovich", "Vanilla Sky", "Gangs of New York", "My Best Friend's Wedding", "Knight and Day", "Bad Teacher", "The Other Woman", "Annie", "What Happens in Vegas", "Back in Action"],
 ["Legally Blonde", "Bridesmaids", "Pretty Woman", "Miss Congeniality", "Clueless"])
board("Films starring Reese Witherspoon", "Film", "medium", ["Reese Witherspoon", "films"],
 ["Legally Blonde", "Walk the Line", "Sweet Home Alabama", "Cruel Intentions", "Election", "Pleasantville", "Wild", "This Means War", "Water for Elephants", "Four Christmases", "Just Like Heaven", "Monsters vs. Aliens", "Sing", "A Wrinkle in Time", "Hot Pursuit"],
 ["Clueless", "Miss Congeniality", "Mean Girls", "13 Going on 30", "Bridget Jones's Diary"])
board("Films starring Anne Hathaway", "Film", "easy", ["Anne Hathaway", "films"],
 ["The Princess Diaries", "The Devil Wears Prada", "Les Misérables", "Interstellar", "Brokeback Mountain", "Ocean's 8", "The Intern", "Rachel Getting Married", "One Day", "Love & Other Drugs", "Alice in Wonderland", "The Dark Knight Rises", "Bride Wars", "Get Smart", "The Witches"],
 ["Mean Girls", "13 Going on 30", "Pretty Woman", "Legally Blonde", "Notting Hill"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-42.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'boards written')
