# Bank session 10 Oct 2026: new Wipeout boards -> bank/wipeout-43.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Songs by Celine Dion", "Music", "easy", ["Celine Dion", "songs"],
 ["My Heart Will Go On", "The Power of Love", "Think Twice", "Because You Loved Me", "It's All Coming Back to Me Now", "All by Myself", "That's the Way It Is", "I'm Alive", "A New Day Has Come", "Falling into You", "Beauty and the Beast", "Tell Him", "I Drove All Night", "To Love You More", "Where Does My Heart Beat Now"],
 ["I Will Always Love You", "Hero", "Un-Break My Heart", "How Do I Live", "Total Eclipse of the Heart"])
board("Songs by Shania Twain", "Music", "medium", ["Shania Twain", "country", "songs"],
 ["Man! I Feel Like a Woman!", "That Don't Impress Me Much", "You're Still the One", "From This Moment On", "Any Man of Mine", "Up!", "Ka-Ching!", "Forever and for Always", "Party for Two", "I'm Gonna Getcha Good!", "Don't Be Stupid (You Know I Love You)", "You've Got a Way", "Whose Bed Have Your Boots Been Under?", "Honey, I'm Home", "Waiter! Bring Me Water!"],
 ["Jolene", "9 to 5", "Achy Breaky Heart", "Before He Cheats", "Need You Now"])
board("Songs by Bruno Mars, solo or as a featured star", "Music", "easy", ["Bruno Mars", "songs"],
 ["Just the Way You Are", "Grenade", "Uptown Funk", "Locked Out of Heaven", "When I Was Your Man", "Treasure", "24K Magic", "That's What I Like", "Finesse", "The Lazy Song", "Marry You", "Leave the Door Open", "Die with a Smile", "APT.", "It Will Rain"],
 ["Happy", "Can't Stop the Feeling!", "Shape of You", "Blurred Lines", "Get Lucky"])
board("Songs by Justin Timberlake", "Music", "medium", ["Justin Timberlake", "songs"],
 ["Cry Me a River", "Rock Your Body", "SexyBack", "Mirrors", "Can't Stop the Feeling!", "Señorita", "What Goes Around... Comes Around", "My Love", "Suit & Tie", "Like I Love You", "Not a Bad Thing", "Summer Love", "LoveStoned", "Filthy", "4 Minutes"],
 ["Uptown Funk", "Happy", "Billie Jean", "Toxic", "Hollaback Girl"])
board("Songs by Dua Lipa", "Music", "easy", ["Dua Lipa", "songs"],
 ["New Rules", "Don't Start Now", "Levitating", "One Kiss", "IDGAF", "Physical", "Break My Heart", "Be the One", "Hotter than Hell", "Blow Your Mind (Mwah)", "Houdini", "Training Season", "Dance the Night", "Scared to Be Lonely", "Love Again"],
 ["Bad Guy", "Sweet but Psycho", "Flowers", "As It Was", "Espresso"])
board("Songs by Slade", "Music", "medium", ["Slade", "glam rock", "songs"],
 ["Coz I Luv You", "Take Me Bak 'Ome", "Mama Weer All Crazee Now", "Cum On Feel the Noize", "Skweeze Me Pleeze Me", "Merry Xmas Everybody", "Gudbuy T'Jane", "My Friend Stan", "Far Far Away", "Everyday", "Look Wot You Dun", "Run Runaway", "My Oh My", "Bangin' Man", "Thanks for the Memory"],
 ["Ballroom Blitz", "Blockbuster", "Tiger Feet", "Metal Guru", "School's Out"])
board("Songs by Foo Fighters", "Music", "medium", ["Foo Fighters", "songs"],
 ["Everlong", "Learn to Fly", "Best of You", "The Pretender", "My Hero", "Times Like These", "All My Life", "Monkey Wrench", "Big Me", "This Is a Call", "Walk", "Rope", "Long Road to Ruin", "Breakout", "These Days"],
 ["Smells Like Teen Spirit", "Basket Case", "Seven Nation Army", "Mr. Brightside", "Song 2"])
board("Songs by Kings of Leon", "Music", "medium", ["Kings of Leon", "songs"],
 ["Sex on Fire", "Use Somebody", "Closer", "Molly's Chambers", "The Bucket", "Revelry", "Notion", "Radioactive", "Waste a Moment", "Pyro", "On Call", "Fans", "Supersoaker", "Back Down South", "Crawl"],
 ["Mr. Brightside", "Somebody Told Me", "Chelsea Dagger", "Take Me Out", "Seven Nation Army"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-43.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'boards written')
