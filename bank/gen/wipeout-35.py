# Bank session 10 Oct 2026: new Wipeout boards -> bank/wipeout-35.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Films starring Bruce Willis", "Film", "medium", ["Bruce Willis", "actors"],
 ["Die Hard", "Die Hard 2", "Pulp Fiction", "The Sixth Sense", "Armageddon", "The Fifth Element", "12 Monkeys", "Unbreakable", "Sin City", "Looper", "RED", "Moonrise Kingdom", "The Jackal", "Hudson Hawk", "Last Man Standing"],
 ["Lethal Weapon", "Speed", "Con Air", "Face/Off", "The Rock"])
board("Films starring Mel Gibson", "Film", "medium", ["Mel Gibson", "actors"],
 ["Mad Max", "Lethal Weapon", "Braveheart", "Gallipoli", "What Women Want", "Signs", "Ransom", "The Patriot", "Maverick", "Payback", "Conspiracy Theory", "Bird on a Wire", "Forever Young", "Hamlet", "We Were Soldiers"],
 ["Gladiator", "Rob Roy", "Legends of the Fall", "The Last of the Mohicans", "Point Break"])
board("Films starring Sean Connery, apart from Bond", "Film", "medium", ["Sean Connery", "actors"],
 ["The Untouchables", "The Hunt for Red October", "Indiana Jones and the Last Crusade", "The Rock", "Highlander", "The Name of the Rose", "Entrapment", "The Man Who Would Be King", "Robin and Marian", "Murder on the Orient Express", "Marnie", "Time Bandits", "Finding Forrester", "The League of Extraordinary Gentlemen", "A Bridge Too Far"],
 ["Braveheart", "Trainspotting", "Rob Roy", "The Wicker Man", "Local Hero"])
board("Songs by Taylor Swift", "Music", "easy", ["Taylor Swift", "songs"],
 ["Shake It Off", "Love Story", "You Belong with Me", "Blank Space", "Bad Blood", "Anti-Hero", "Cruel Summer", "We Are Never Ever Getting Back Together", "Style", "Look What You Made Me Do", "Cardigan", "All Too Well", "Lover", "22", "Fortnight"],
 ["Bad Guy", "Drivers License", "Flowers", "Royals", "Teenage Dream"])
board("Songs by Coldplay", "Music", "easy", ["Coldplay", "songs"],
 ["Yellow", "Clocks", "The Scientist", "Fix You", "Viva la Vida", "Paradise", "A Sky Full of Stars", "Trouble", "Speed of Sound", "Hymn for the Weekend", "Adventure of a Lifetime", "Something Just Like This", "In My Place", "Higher Power", "My Universe"],
 ["Chasing Cars", "Somewhere Only We Know", "Mr. Brightside", "Use Somebody", "Run"])
board("Hits by George Michael or Wham!", "Music", "medium", ["George Michael", "Wham!", "songs"],
 ["Careless Whisper", "Last Christmas", "Wake Me Up Before You Go-Go", "Faith", "Freedom! '90", "Club Tropicana", "I'm Your Man", "Young Guns (Go for It!)", "Father Figure", "Jesus to a Child", "Fastlove", "Outside", "The Edge of Heaven", "A Different Corner", "Praying for Time"],
 ["Gold", "Wherever I Lay My Hat", "Relax", "Karma Chameleon", "True"])
board("Songs by Billy Joel", "Music", "medium", ["Billy Joel", "songs"],
 ["Piano Man", "Uptown Girl", "We Didn't Start the Fire", "Just the Way You Are", "She's Always a Woman", "Tell Her About It", "My Life", "Only the Good Die Young", "Movin' Out", "It's Still Rock and Roll to Me", "The River of Dreams", "Honesty", "New York State of Mind", "Scenes from an Italian Restaurant", "Vienna"],
 ["Your Song", "Rocket Man", "Born to Run", "Mandy", "Sweet Caroline"])
board("Phil Collins hits outside Genesis, solo or duets", "Music", "hard", ["Phil Collins", "songs"],
 ["In the Air Tonight", "Against All Odds", "You Can't Hurry Love", "Another Day in Paradise", "Easy Lover", "One More Night", "Sussudio", "Two Hearts", "A Groovy Kind of Love", "I Wish It Would Rain Down", "You'll Be in My Heart", "Take Me Home", "I Missed Again", "Separate Lives", "Both Sides of the Story"],
 ["Invisible Touch", "Land of Confusion", "I Can't Dance", "Mama", "Follow You Follow Me"])
board("Tom Jones hits", "Music", "medium", ["Tom Jones", "songs", "Wales"],
 ["It's Not Unusual", "Delilah", "Green, Green Grass of Home", "Sex Bomb", "Kiss", "She's a Lady", "What's New Pussycat?", "Help Yourself", "I'll Never Fall in Love Again", "Burning Down the House", "Mama Told Me Not to Come", "Thunderball", "Daughter of Darkness", "Love Me Tonight", "Without Love"],
 ["Release Me", "The Last Waltz", "Am I That Easy to Forget", "There Goes My Everything", "Quando Quando Quando"])
board("Songs by Def Leppard", "Music", "hard", ["Def Leppard", "songs", "Sheffield"],
 ["Pour Some Sugar on Me", "Love Bites", "Animal", "Hysteria", "Photograph", "Rock of Ages", "Armageddon It", "Let's Get Rocked", "When Love and Hate Collide", "Two Steps Behind", "Rocket", "Women", "Bringin' On the Heartbreak", "Foolin'", "Have You Ever Needed Someone So Bad"],
 ["Here I Go Again", "Livin' on a Prayer", "The Final Countdown", "Nothin' but a Good Time", "Kickstart My Heart"])
board("Eurythmics or Annie Lennox hits", "Music", "medium", ["Eurythmics", "Annie Lennox", "songs"],
 ["Sweet Dreams (Are Made of This)", "Love Is a Stranger", "Here Comes the Rain Again", "There Must Be an Angel (Playing with My Heart)", "Thorn in My Side", "Who's That Girl?", "Sisters Are Doin' It for Themselves", "Right by Your Side", "Missionary Man", "When Tomorrow Comes", "Why", "Walking on Broken Glass", "No More I Love You's", "Little Bird", "Love Song for a Vampire"],
 ["Don't You Want Me", "Total Eclipse of the Heart", "Running Up That Hill", "Tainted Love", "Smalltown Boy"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-35.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'boards written')
