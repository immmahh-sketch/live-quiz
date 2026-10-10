# Bank session 10 Oct 2026: new Wipeout boards -> bank/wipeout-45.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Songs by Steps", "Music", "easy", ["Steps", "pop", "songs"],
 ["5,6,7,8", "Last Thing on My Mind", "One for Sorrow", "Heartbeat", "Tragedy", "Better Best Forgotten", "Love's Got a Hold on My Heart", "After the Love Has Gone", "Summer of Love", "Stomp", "It's the Way You Make Me Feel", "Here and Now", "Chain Reaction", "Words Are Not Enough", "Scared of the Dark"],
 ["Reach", "Don't Stop Movin'", "Never Had a Dream Come True", "Bring It All Back", "Mysterious Girl"])
board("Songs by Travis", "Music", "medium", ["Travis", "Scotland", "songs"],
 ["Why Does It Always Rain on Me?", "Sing", "Driftwood", "Turn", "Writing to Reach You", "Side", "Flowers in the Window", "Closer", "Re-Offender", "Love Will Come Through", "Tied to the 90's", "U16 Girls", "All I Want to Do Is Rock", "Happy", "Selfish Jean"],
 ["Chasing Cars", "Yellow", "Somewhere Only We Know", "Run", "Bitter Sweet Symphony"])
board("Songs by Guns N' Roses", "Music", "medium", ["Guns N' Roses", "rock", "songs"],
 ["Sweet Child o' Mine", "Paradise City", "Welcome to the Jungle", "November Rain", "Don't Cry", "Patience", "Knockin' on Heaven's Door", "Live and Let Die", "You Could Be Mine", "Civil War", "Estranged", "Since I Don't Have You", "Yesterdays", "It's So Easy", "Nightrain"],
 ["Livin' on a Prayer", "Pour Some Sugar on Me", "Here I Go Again", "Kickstart My Heart", "Highway to Hell"])
board("Songs by Aerosmith", "Music", "medium", ["Aerosmith", "rock", "songs"],
 ["Dream On", "Walk This Way", "Sweet Emotion", "Janie's Got a Gun", "Love in an Elevator", "Crazy", "Cryin'", "Amazing", "I Don't Want to Miss a Thing", "Livin' on the Edge", "Rag Doll", "Dude (Looks Like a Lady)", "Angel", "Jaded", "Pink"],
 ["Sweet Child o' Mine", "Livin' on a Prayer", "Pour Some Sugar on Me", "Eye of the Tiger", "Final Countdown"])
board("Songs by Jessie J", "Music", "easy", ["Jessie J", "pop", "songs"],
 ["Price Tag", "Domino", "Do It Like a Dude", "Nobody's Perfect", "Who You Are", "Flashlight", "Bang Bang", "Wild", "It's My Party", "Burnin' Up", "Masterpiece", "Thunder", "Laserlight", "Who's Laughing Now", "Sexy Lady"],
 ["Wings", "Heart Skips a Beat", "Run This Town", "Read All About It", "Cannonball"])
board("Songs by Elbow", "Music", "hard", ["Elbow", "Manchester", "songs"],
 ["One Day Like This", "Grounds for Divorce", "Magnificent (She Says)", "Mirrorball", "Lippy Kids", "Station Approach", "Newborn", "Leaders of the Free World", "Fugitive Motel", "Neat Little Rows", "The Bones of You", "New York Morning", "Golden Slumbers", "Starlings", "Weather to Fly"],
 ["Chasing Cars", "Sit Down", "Run", "Fix You", "Somewhere Only We Know"])
board("Songs by Texas", "Music", "medium", ["Texas", "Scotland", "songs"],
 ["I Don't Want a Lover", "Say What You Want", "Summer Son", "Black Eyed Boy", "Halo", "In Demand", "Inner Smile", "Put Your Arms Around Me", "Sleep", "Getaway", "Insane", "In Our Lifetime", "When We Are Together", "Hi", "Let's Work It Out"],
 ["Torn", "Bitch", "Linger", "Ironic", "Zombie"])
board("Songs by the Jackson 5 or the Jacksons", "Music", "medium", ["Jackson 5", "The Jacksons", "Motown", "songs"],
 ["I Want You Back", "ABC", "The Love You Save", "I'll Be There", "Never Can Say Goodbye", "Mama's Pearl", "Lookin' Through the Windows", "Doctor My Eyes", "Blame It on the Boogie", "Can You Feel It", "Shake Your Body (Down to the Ground)", "Show You the Way to Go", "State of Shock", "Dancing Machine", "Walk Right Now"],
 ["Rockin' Robin", "Billie Jean", "My Girl", "Ain't No Mountain High Enough", "Superstition"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-45.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'boards written')
