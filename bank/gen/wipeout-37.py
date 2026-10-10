# Bank session 10 Oct 2026: new Wipeout boards -> bank/wipeout-37.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Hits by Diana Ross or the Supremes", "Music", "medium", ["Diana Ross", "Supremes", "Motown", "songs"],
 ["Baby Love", "Where Did Our Love Go", "Stop! In the Name of Love", "You Can't Hurry Love", "Reflections", "Ain't No Mountain High Enough", "Chain Reaction", "Upside Down", "I'm Coming Out", "Endless Love", "Touch Me in the Morning", "Theme from Mahogany", "Love Child", "Someday We'll Be Together", "Why Do Fools Fall in Love"],
 ["Respect", "My Girl", "Dancing in the Street", "I Heard It Through the Grapevine", "Please Mr. Postman"])
board("Songs by Shirley Bassey", "Music", "medium", ["Shirley Bassey", "Wales", "songs"],
 ["Goldfinger", "Diamonds Are Forever", "Moonraker", "Big Spender", "This Is My Life", "As I Love You", "Kiss Me, Honey Honey, Kiss Me", "Reach for the Stars", "What Now My Love", "I (Who Have Nothing)", "Something", "Never, Never, Never", "History Repeating", "Get the Party Started", "As Long as He Needs Me"],
 ["Thunderball", "Nobody Does It Better", "All Time High", "From Russia with Love", "A View to a Kill"])
board("Hits by Dusty Springfield", "Music", "medium", ["Dusty Springfield", "1960s", "songs"],
 ["I Only Want to Be with You", "You Don't Have to Say You Love Me", "Son of a Preacher Man", "I Just Don't Know What to Do with Myself", "The Look of Love", "Wishin' and Hopin'", "Going Back", "In Private", "What Have I Done to Deserve This?", "Losing You", "Some of Your Lovin'", "I Close My Eyes and Count to Ten", "Nothing Has Been Proved", "All I See Is You", "Little by Little"],
 ["Anyone Who Had a Heart", "Downtown", "Walk On By", "To Sir with Love", "Alfie"])
board("Hits by Cilla Black", "Music", "medium", ["Cilla Black", "1960s", "Liverpool", "songs"],
 ["Anyone Who Had a Heart", "You're My World", "Alfie", "Step Inside Love", "Something Tells Me (Something's Gonna Happen Tonight)", "Surround Yourself with Sorrow", "Conversations", "You've Lost That Lovin' Feelin'", "Love's Just a Broken Heart", "It's for You", "Don't Answer Me", "A Fool Am I", "Liverpool Lullaby", "Baby We Can't Go Wrong", "Through the Years"],
 ["Son of a Preacher Man", "Downtown", "Puppet on a String", "Boom Bang-a-Bang", "To Sir with Love"])
board("Songs by Bryan Adams", "Music", "medium", ["Bryan Adams", "songs"],
 ["(Everything I Do) I Do It for You", "Summer of '69", "Heaven", "Run to You", "Please Forgive Me", "All for Love", "Have You Ever Really Loved a Woman?", "Cuts Like a Knife", "The Only Thing That Looks Good on Me Is You", "Somebody", "Straight from the Heart", "When You're Gone", "It's Only Love", "Can't Stop This Thing We Started", "18 till I Die"],
 ["Livin' on a Prayer", "Born in the U.S.A.", "Total Eclipse of the Heart", "I Want to Know What Love Is", "Eye of the Tiger"])
board("Songs by Meat Loaf", "Music", "hard", ["Meat Loaf", "Jim Steinman", "songs"],
 ["Bat Out of Hell", "I'd Do Anything for Love (But I Won't Do That)", "Two Out of Three Ain't Bad", "Paradise by the Dashboard Light", "You Took the Words Right Out of My Mouth", "Dead Ringer for Love", "Rock and Roll Dreams Come Through", "Objects in the Rear View Mirror May Appear Closer Than They Are", "I'm Gonna Love Her for Both of Us", "Midnight at the Lost and Found", "Modern Girl", "Not a Dry Eye in the House", "It's All Coming Back to Me Now", "Couldn't Have Said It Better", "Life Is a Lemon and I Want My Money Back"],
 ["Total Eclipse of the Heart", "Holding Out for a Hero", "Making Love Out of Nothing at All", "Livin' on a Prayer", "Kickstart My Heart"])
board("Songs by the Human League", "Music", "medium", ["Human League", "Sheffield", "songs"],
 ["Don't You Want Me", "Mirror Man", "(Keep Feeling) Fascination", "Together in Electric Dreams", "Human", "Love Action (I Believe in Love)", "Open Your Heart", "The Sound of the Crowd", "Louise", "The Lebanon", "Tell Me When", "Being Boiled", "Life on Your Own", "Heart Like a Wheel", "One Man in My Heart"],
 ["Tainted Love", "Vienna", "Enola Gay", "Fade to Grey", "Blue Monday"])
board("Songs by Simple Minds", "Music", "medium", ["Simple Minds", "Scotland", "songs"],
 ["Don't You (Forget About Me)", "Alive and Kicking", "Belfast Child", "Promised You a Miracle", "Waterfront", "Sanctify Yourself", "All the Things She Said", "Glittering Prize", "Mandela Day", "Let There Be Love", "See the Lights", "She's a River", "Someone Somewhere in Summertime", "Up on the Catwalk", "Speed Your Love to Me"],
 ["Pride (In the Name of Love)", "With or Without You", "Everybody Wants to Rule the World", "The Whole of the Moon", "Dancing with Tears in My Eyes"])
board("Songs by Nirvana", "Music", "medium", ["Nirvana", "grunge", "songs"],
 ["Smells Like Teen Spirit", "Come as You Are", "Lithium", "In Bloom", "Heart-Shaped Box", "All Apologies", "About a Girl", "Polly", "Breed", "Dumb", "Pennyroyal Tea", "Where Did You Sleep Last Night", "The Man Who Sold the World", "You Know You're Right", "Sliver"],
 ["Black Hole Sun", "Alive", "Everlong", "Creep", "Song 2"])
board("Songs by Green Day", "Music", "medium", ["Green Day", "punk", "songs"],
 ["Basket Case", "American Idiot", "Boulevard of Broken Dreams", "Good Riddance (Time of Your Life)", "Wake Me Up When September Ends", "Holiday", "Longview", "When I Come Around", "Minority", "Jesus of Suburbia", "Know Your Enemy", "21 Guns", "Welcome to Paradise", "Hitchin' a Ride", "Brain Stew"],
 ["All the Small Things", "The Middle", "Fat Lip", "Pretty Fly (for a White Guy)", "Mr. Brightside"])
board("Songs by the Red Hot Chili Peppers", "Music", "medium", ["Red Hot Chili Peppers", "songs"],
 ["Californication", "Under the Bridge", "Scar Tissue", "Otherside", "Give It Away", "By the Way", "Can't Stop", "Dani California", "Snow (Hey Oh)", "Soul to Squeeze", "Around the World", "The Zephyr Song", "Breaking the Girl", "Suck My Kiss", "Tell Me Baby"],
 ["Black Hole Sun", "Smells Like Teen Spirit", "Killing in the Name", "Song 2", "Everlong"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-37.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'boards written')
