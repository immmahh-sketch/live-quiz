# Bank session 10 Oct 2026: new Wipeout boards -> bank/wipeout-44.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Songs by Roy Orbison", "Music", "medium", ["Roy Orbison", "1960s", "songs"],
 ["Oh, Pretty Woman", "Crying", "Only the Lonely", "In Dreams", "It's Over", "You Got It", "Running Scared", "Blue Bayou", "Dream Baby", "Pretty Paper", "Ooby Dooby", "Mean Woman Blues", "Leah", "I Drove All Night", "She's a Mystery to Me"],
 ["Peggy Sue", "Great Balls of Fire", "Return to Sender", "I Walk the Line", "Be-Bop-a-Lula"])
board("Songs by Simon & Garfunkel", "Music", "medium", ["Simon & Garfunkel", "1960s", "songs"],
 ["The Sound of Silence", "Mrs. Robinson", "Bridge over Troubled Water", "The Boxer", "Cecilia", "Homeward Bound", "Scarborough Fair", "I Am a Rock", "America", "El Condor Pasa", "Kathy's Song", "A Hazy Shade of Winter", "The 59th Street Bridge Song (Feelin' Groovy)", "Old Friends", "April Come She Will"],
 ["Graceland", "You Can Call Me Al", "American Pie", "Blowin' in the Wind", "Everybody's Talkin'"])
board("Songs by Calvin Harris, solo or with guest singers", "Music", "medium", ["Calvin Harris", "dance", "songs"],
 ["Feel So Close", "Summer", "We Found Love", "This Is What You Came For", "How Deep Is Your Love", "Blame", "Under Control", "One Kiss", "Promises", "Outside", "Sweet Nothing", "I Need Your Love", "Acceptable in the 80s", "Feels", "Slide"],
 ["Titanium", "Wake Me Up", "Animals", "Lean On", "Don't You Worry Child"])
board("Songs by Daft Punk, or featuring them", "Music", "medium", ["Daft Punk", "dance", "songs"],
 ["Around the World", "One More Time", "Get Lucky", "Harder, Better, Faster, Stronger", "Da Funk", "Digital Love", "Instant Crush", "Lose Yourself to Dance", "Technologic", "Robot Rock", "Aerodynamic", "Something About Us", "Starboy", "I Feel It Coming", "Revolution 909"],
 ["Sandstorm", "Blue (Da Ba Dee)", "Music Sounds Better with You", "Lady (Hear Me Tonight)", "Insomnia"])
board("Songs by Sam Smith, solo or as a featured singer", "Music", "medium", ["Sam Smith", "songs"],
 ["Stay with Me", "Too Good at Goodbyes", "Writing's on the Wall", "Latch", "La La La", "Unholy", "Dancing with a Stranger", "Promises", "I'm Not the Only One", "Lay Me Down", "Money on My Mind", "Fire on Fire", "Diamonds", "How Do You Sleep?", "Like I Can"],
 ["Someone You Loved", "Rather Be", "Hold Back the River", "Shotgun", "Budapest"])
board("Songs by The Weeknd", "Music", "medium", ["The Weeknd", "songs"],
 ["Blinding Lights", "Starboy", "Can't Feel My Face", "Save Your Tears", "The Hills", "Earned It", "I Feel It Coming", "Die for You", "In Your Eyes", "Heartless", "Call Out My Name", "Often", "After Hours", "Popular", "Out of Time"],
 ["Blurred Lines", "Hotline Bling", "Stay", "Peaches", "Can't Stop the Feeling!"])
board("Songs by Keane", "Music", "hard", ["Keane", "songs"],
 ["Somewhere Only We Know", "Everybody's Changing", "This Is the Last Time", "Bedshaped", "Is It Any Wonder?", "Crystal Ball", "Atlantic", "Nothing in My Way", "A Bad Dream", "Spiralling", "The Lovers Are Losing", "Perfect Symmetry", "Silenced by the Night", "Disconnected", "Bend and Break"],
 ["Chasing Cars", "Fix You", "The Scientist", "Run", "Why Does It Always Rain on Me?"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-44.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'boards written')
