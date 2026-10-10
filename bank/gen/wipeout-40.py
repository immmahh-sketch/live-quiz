# Bank session 10 Oct 2026: new Wipeout boards -> bank/wipeout-40.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Songs by Mariah Carey", "Music", "easy", ["Mariah Carey", "songs"],
 ["Hero", "Fantasy", "We Belong Together", "Vision of Love", "Always Be My Baby", "Without You", "Emotions", "Dreamlover", "One Sweet Day", "Honey", "Heartbreaker", "Touch My Body", "Obsessed", "Endless Love", "All I Want for Christmas Is You"],
 ["I Will Always Love You", "Un-Break My Heart", "Because You Loved Me", "My Heart Will Go On", "Greatest Love of All"])
board("Songs by Snow Patrol", "Music", "medium", ["Snow Patrol", "songs"],
 ["Chasing Cars", "Run", "Open Your Eyes", "Set the Fire to the Third Bar", "Spitting Games", "Chocolate", "Signal Fire", "Take Back the City", "Crack the Shutters", "Shut Your Eyes", "You're All I Have", "Called Out in the Dark", "Just Say Yes", "Hands Open", "Don't Give In"],
 ["Somewhere Only We Know", "Fix You", "Starlight", "Ruby", "Sweet Disposition"])
board("Songs by Muse", "Music", "medium", ["Muse", "songs"],
 ["Supermassive Black Hole", "Starlight", "Uprising", "Hysteria", "Time Is Running Out", "Plug In Baby", "Knights of Cydonia", "Madness", "Feeling Good", "Map of the Problematique", "Resistance", "Undisclosed Desires", "Psycho", "Sing for Absolution", "Butterflies and Hurricanes"],
 ["Seven Nation Army", "Mr. Brightside", "Paranoid Android", "Song 2", "Somebody Told Me"])
board("Songs by the Manic Street Preachers", "Music", "hard", ["Manic Street Preachers", "Wales", "songs"],
 ["A Design for Life", "If You Tolerate This Your Children Will Be Next", "Motorcycle Emptiness", "You Love Us", "Everything Must Go", "Australia", "Tsunami", "The Masses Against the Classes", "Your Love Alone Is Not Enough", "Kevin Carter", "Motown Junk", "Theme from M*A*S*H (Suicide Is Painless)", "Faster", "La Tristesse Durera (Scream to a Sigh)", "The Everlasting"],
 ["Mulder and Scully", "Road Rage", "Have a Nice Day", "Dakota", "Northern Lites"])
board("Songs by New Order", "Music", "medium", ["New Order", "Manchester", "songs"],
 ["Blue Monday", "True Faith", "Regret", "World in Motion", "Bizarre Love Triangle", "Temptation", "Ceremony", "Confusion", "The Perfect Kiss", "Fine Time", "Round & Round", "Touched by the Hand of God", "Crystal", "Krafty", "1963"],
 ["Love Will Tear Us Apart", "Enjoy the Silence", "Fools Gold", "Step On", "Don't You Want Me"])
board("Songs by Spandau Ballet", "Music", "medium", ["Spandau Ballet", "1980s", "songs"],
 ["True", "Gold", "Only When You Leave", "Through the Barricades", "Communication", "Lifeline", "Instinction", "Chant No. 1 (I Don't Need This Pressure On)", "To Cut a Long Story Short", "Musclebound", "Highly Strung", "I'll Fly for You", "Round and Round", "The Freeze", "Paint Me Down"],
 ["Vienna", "Rio", "Fade to Grey", "Club Tropicana", "Wild Boys"])
board("Songs by Jamiroquai", "Music", "medium", ["Jamiroquai", "songs"],
 ["Virtual Insanity", "Cosmic Girl", "Canned Heat", "Space Cowboy", "Deeper Underground", "Alright", "Little L", "Love Foolosophy", "Too Young to Die", "When You Gonna Learn", "Emergency on Planet Earth", "Seven Days in Sunny June", "Feels Just Like It Should", "Runaway", "Blow Your Mind"],
 ["Groove Is in the Heart", "Lady (Hear Me Tonight)", "Music Sounds Better with You", "Don't Stop 'Til You Get Enough", "Get Lucky"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-40.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'boards written')
