# Bank session 10 Oct 2026: new Wipeout boards -> bank/wipeout-34.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Films starring Robert De Niro", "Film", "medium", ["Robert De Niro", "actors"],
 ["Taxi Driver", "Raging Bull", "Goodfellas", "The Deer Hunter", "Casino", "Heat", "Meet the Parents", "Cape Fear", "The Godfather Part II", "Analyze This", "The Irishman", "Silver Linings Playbook", "Ronin", "Midnight Run", "Awakenings"],
 ["Scarface", "Serpico", "Donnie Brasco", "Dog Day Afternoon", "Carlito's Way"])
board("Films starring Sylvester Stallone", "Film", "medium", ["Sylvester Stallone", "actors"],
 ["Rocky", "First Blood", "Cliffhanger", "Demolition Man", "The Expendables", "Cobra", "Creed", "Over the Top", "Tango & Cash", "Judge Dredd", "Escape to Victory", "Cop Land", "Lock Up", "Daylight", "Get Carter (2000)"],
 ["Commando", "Predator", "The Terminator", "Total Recall", "Die Hard"])
board("Films starring Arnold Schwarzenegger", "Film", "medium", ["Arnold Schwarzenegger", "actors"],
 ["The Terminator", "Predator", "Commando", "Total Recall", "Twins", "Kindergarten Cop", "True Lies", "Conan the Barbarian", "The Running Man", "Red Heat", "Junior", "Jingle All the Way", "Eraser", "Last Action Hero", "Batman & Robin"],
 ["Cliffhanger", "Demolition Man", "Universal Soldier", "Bloodsport", "Die Hard"])
board("Songs by Dire Straits", "Music", "medium", ["Dire Straits", "songs"],
 ["Sultans of Swing", "Money for Nothing", "Walk of Life", "Romeo and Juliet", "Brothers in Arms", "Private Investigations", "Tunnel of Love", "So Far Away", "Calling Elvis", "Twisting by the Pool", "Lady Writer", "Industrial Disease", "Telegraph Road", "Your Latest Trick", "Skateaway"],
 ["Layla", "Hotel California", "Comfortably Numb", "Owner of a Lonely Heart", "Every Breath You Take"])
board("Songs by Status Quo", "Music", "medium", ["Status Quo", "songs"],
 ["Rockin' All Over the World", "Whatever You Want", "Down Down", "Pictures of Matchstick Men", "Caroline", "In the Army Now", "Marguerita Time", "Paper Plane", "Again and Again", "Rain", "What You're Proposing", "Burning Bridges", "Ice in the Sun", "Roll Over Lay Down", "Wild Side of Life"],
 ["All Right Now", "Smoke on the Water", "Black Night", "School's Out", "Hold Your Head Up"])
board("Rod Stewart hits, solo or with the Faces", "Music", "medium", ["Rod Stewart", "songs"],
 ["Maggie May", "Sailing", "Da Ya Think I'm Sexy?", "You Wear It Well", "The First Cut Is the Deepest", "Tonight's the Night", "Baby Jane", "I Don't Want to Talk About It", "Have I Told You Lately", "Young Turks", "Rhythm of My Heart", "Stay with Me", "Hot Legs", "You're in My Heart", "Downtown Train"],
 ["Love Is All Around", "The Lady in Red", "Careless Whisper", "Sorry Seems to Be the Hardest Word", "You Are So Beautiful"])
board("Songs by the Beach Boys", "Music", "medium", ["Beach Boys", "songs"],
 ["Good Vibrations", "Surfin' U.S.A.", "God Only Knows", "Wouldn't It Be Nice", "I Get Around", "California Girls", "Help Me, Rhonda", "Barbara Ann", "Sloop John B", "Kokomo", "Fun, Fun, Fun", "Do It Again", "Heroes and Villains", "Don't Worry Baby", "Then I Kissed Her"],
 ["Surf City", "Pipeline", "Wipe Out", "California Dreamin'", "Da Doo Ron Ron"])
board("Songs by the Eagles", "Music", "medium", ["Eagles", "songs"],
 ["Hotel California", "Take It Easy", "Desperado", "Lyin' Eyes", "One of These Nights", "Life in the Fast Lane", "New Kid in Town", "Take It to the Limit", "Tequila Sunrise", "Heartache Tonight", "The Long Run", "Witchy Woman", "Peaceful Easy Feeling", "Already Gone", "I Can't Tell You Why"],
 ["A Horse with No Name", "The Boys of Summer", "Sweet Home Alabama", "Go Your Own Way", "Ventura Highway"])
board("Songs by Bon Jovi", "Music", "medium", ["Bon Jovi", "songs"],
 ["Livin' on a Prayer", "You Give Love a Bad Name", "Wanted Dead or Alive", "Always", "It's My Life", "Bed of Roses", "Keep the Faith", "Bad Medicine", "Born to Be My Baby", "Have a Nice Day", "Runaway", "In These Arms", "Lay Your Hands on Me", "This Ain't a Love Song", "Someday I'll Be Saturday Night"],
 ["The Final Countdown", "Here I Go Again", "Pour Some Sugar on Me", "Is This Love", "Poison"])
board("Songs by Duran Duran", "Music", "medium", ["Duran Duran", "songs"],
 ["Rio", "Hungry Like the Wolf", "Girls on Film", "The Reflex", "Save a Prayer", "Wild Boys", "A View to a Kill", "Notorious", "Ordinary World", "Is There Something I Should Know?", "Union of the Snake", "Planet Earth", "Come Undone", "Skin Trade", "New Moon on Monday"],
 ["True", "Gold", "Tainted Love", "Don't You Want Me", "Vienna"])
board("Songs by the Pet Shop Boys", "Music", "medium", ["Pet Shop Boys", "songs"],
 ["West End Girls", "It's a Sin", "Always on My Mind", "Go West", "Heart", "Suburbia", "Rent", "Domino Dancing", "Left to My Own Devices", "So Hard", "Being Boring", "Opportunities (Let's Make Lots of Money)", "What Have I Done to Deserve This?", "Se a vida é", "Where the Streets Have No Name (I Can't Take My Eyes Off You)"],
 ["Smalltown Boy", "Tainted Love", "Enola Gay", "Relax", "Don't Leave Me This Way"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-34.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'boards written')
