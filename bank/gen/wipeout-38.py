# Bank session 10 Oct 2026: new Wipeout boards -> bank/wipeout-38.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Hits by Beyoncé, solo or with Destiny's Child", "Music", "easy", ["Beyoncé", "Destiny's Child", "songs"],
 ["Crazy in Love", "Single Ladies (Put a Ring on It)", "Halo", "Irreplaceable", "Run the World (Girls)", "Drunk in Love", "Formation", "Survivor", "Say My Name", "Independent Women", "Bootylicious", "If I Were a Boy", "Sweet Dreams", "Déjà Vu", "Texas Hold 'Em"],
 ["Umbrella", "Toxic", "Bad Romance", "Firework", "No Scrubs"])
board("Songs by Rihanna", "Music", "easy", ["Rihanna", "songs"],
 ["Umbrella", "Diamonds", "We Found Love", "Only Girl (In the World)", "Rude Boy", "Don't Stop the Music", "SOS", "Pon de Replay", "Disturbia", "Work", "S&M", "What's My Name?", "Take a Bow", "Where Have You Been", "Shut Up and Drive"],
 ["Halo", "Toxic", "Bad Romance", "California Gurls", "Hollaback Girl"])
board("Songs by Britney Spears", "Music", "easy", ["Britney Spears", "songs"],
 ["...Baby One More Time", "Oops!... I Did It Again", "Toxic", "Sometimes", "Lucky", "Stronger", "Everytime", "Womanizer", "Circus", "Gimme More", "I'm a Slave 4 U", "(You Drive Me) Crazy", "Born to Make You Happy", "Hold It Against Me", "Scream & Shout"],
 ["Genie in a Bottle", "Dirrty", "Since U Been Gone", "Complicated", "Can't Get You Out of My Head"])
board("Songs by Dolly Parton", "Music", "medium", ["Dolly Parton", "country", "songs"],
 ["9 to 5", "Jolene", "I Will Always Love You", "Islands in the Stream", "Coat of Many Colors", "Here You Come Again", "Two Doors Down", "Love Is Like a Butterfly", "Heartbreaker", "Why'd You Come in Here Lookin' Like That", "Yellow Roses", "Joshua", "Better Get to Livin'", "The Bargain Store", "Baby I'm Burnin'"],
 ["Stand by Your Man", "Crazy", "Ring of Fire", "Rhinestone Cowboy", "Coal Miner's Daughter"])
board("Songs by Erasure", "Music", "hard", ["Erasure", "songs"],
 ["A Little Respect", "Sometimes", "Stop!", "Chains of Love", "Oh L'amour", "Blue Savannah", "Victim of Love", "Ship of Fools", "Always", "Love to Hate You", "Drama!", "Star", "Breath of Life", "Who Needs Love Like That", "Solsbury Hill"],
 ["Smalltown Boy", "Tainted Love", "Don't Leave Me This Way", "It's a Sin", "Enola Gay"])
board("Songs by Blur", "Music", "medium", ["Blur", "Britpop", "songs"],
 ["Parklife", "Song 2", "Country House", "The Universal", "Girls & Boys", "Beetlebum", "Tender", "Coffee & TV", "Charmless Man", "End of a Century", "There's No Other Way", "She's So High", "Out of Time", "To the End", "Stereotypes"],
 ["Wonderwall", "Common People", "Disco 2000", "Animal Nitrate", "Alright"])
board("Songs by Pulp", "Music", "medium", ["Pulp", "Britpop", "Sheffield", "songs"],
 ["Common People", "Disco 2000", "Babies", "Sorted for E's & Wizz", "Mis-Shapes", "Do You Remember the First Time?", "Something Changed", "Help the Aged", "This Is Hardcore", "Lipgloss", "Razzmatazz", "A Little Soul", "Bad Cover Version", "Sunrise", "The Trees"],
 ["Parklife", "Song 2", "Wonderwall", "Animal Nitrate", "Stay Together"])
board("Songs by the Smiths", "Music", "hard", ["The Smiths", "Manchester", "songs"],
 ["This Charming Man", "How Soon Is Now?", "There Is a Light That Never Goes Out", "Heaven Knows I'm Miserable Now", "Panic", "Bigmouth Strikes Again", "William, It Was Really Nothing", "Ask", "Girlfriend in a Coma", "Sheila Take a Bow", "Shoplifters of the World Unite", "What Difference Does It Make?", "Hand in Glove", "The Boy with the Thorn in His Side", "Still Ill"],
 ["Suedehead", "Everyday Is Like Sunday", "Love Will Tear Us Apart", "Just Like Heaven", "Fools Gold"])
board("Songs by the Cure", "Music", "hard", ["The Cure", "songs"],
 ["Just Like Heaven", "Friday I'm in Love", "Lovesong", "Boys Don't Cry", "The Lovecats", "Close to Me", "Lullaby", "In Between Days", "A Forest", "Pictures of You", "Why Can't I Be You?", "High", "Let's Go to Bed", "Charlotte Sometimes", "The Walk"],
 ["How Soon Is Now?", "Love Will Tear Us Apart", "Enjoy the Silence", "Ever Fallen in Love", "Atmosphere"])
board("Songs by the Clash", "Music", "hard", ["The Clash", "punk", "songs"],
 ["London Calling", "Should I Stay or Should I Go", "Rock the Casbah", "Train in Vain", "I Fought the Law", "White Riot", "Complete Control", "Tommy Gun", "(White Man) In Hammersmith Palais", "Bankrobber", "Clampdown", "Spanish Bombs", "The Guns of Brixton", "Career Opportunities", "Lost in the Supermarket"],
 ["Anarchy in the U.K.", "God Save the Queen", "Ever Fallen in Love", "Teenage Kicks", "New Rose"])
board("Songs by Metallica", "Music", "hard", ["Metallica", "metal", "songs"],
 ["Enter Sandman", "Nothing Else Matters", "Master of Puppets", "One", "The Unforgiven", "Fade to Black", "Sad but True", "Wherever I May Roam", "For Whom the Bell Tolls", "Seek & Destroy", "Battery", "Fuel", "Until It Sleeps", "Whiskey in the Jar", "The Memory Remains"],
 ["Paranoid", "Ace of Spades", "Holy Wars... The Punishment Due", "Run to the Hills", "Breaking the Law"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-38.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'boards written')
