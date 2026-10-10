# Bank session 10 Oct 2026: new Wipeout boards -> bank/wipeout-36.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Hits by Lionel Richie, solo or with the Commodores", "Music", "medium", ["Lionel Richie", "Commodores", "songs"],
 ["Hello", "All Night Long (All Night)", "Dancing on the Ceiling", "Say You, Say Me", "Easy", "Three Times a Lady", "Endless Love", "Truly", "Running with the Night", "Stuck on You", "Penny Lover", "Still", "Sail On", "Ballerina Girl", "Deep River Woman"],
 ["Careless Whisper", "Against All Odds", "The Lady in Red", "Up Where We Belong", "Hard to Say I'm Sorry"])
board("Songs Neil Diamond recorded", "Music", "medium", ["Neil Diamond", "songs"],
 ["Sweet Caroline", "Cracklin' Rosie", "Song Sung Blue", "I'm a Believer", "Love on the Rocks", "America", "Forever in Blue Jeans", "Hello Again", "Red Red Wine", "Solitary Man", "Kentucky Woman", "Beautiful Noise", "Girl, You'll Be a Woman Soon", "Cherry, Cherry", "I Am... I Said"],
 ["Mandy", "Copacabana", "Rhinestone Cowboy", "Delilah", "Islands in the Stream"])
board("Songs by the Carpenters", "Music", "medium", ["Carpenters", "songs"],
 ["(They Long to Be) Close to You", "We've Only Just Begun", "Top of the World", "Yesterday Once More", "Superstar", "Rainy Days and Mondays", "Calling Occupants of Interplanetary Craft", "Only Yesterday", "Please Mr. Postman", "Jambalaya (On the Bayou)", "Hurting Each Other", "Goodbye to Love", "For All We Know", "Sing", "Merry Christmas Darling"],
 ["Bright Eyes", "I'd Like to Teach the World to Sing", "Seasons in the Sun", "Annie's Song", "Don't Cry for Me Argentina"])
board("Hits by UB40", "Music", "medium", ["UB40", "reggae", "songs"],
 ["Red Red Wine", "Kingston Town", "(I Can't Help) Falling in Love with You", "Food for Thought", "One in Ten", "Rat in Mi Kitchen", "Cherry Oh Baby", "Homely Girl", "Here I Am (Come and Take Me)", "Higher Ground", "Don't Break My Heart", "I Got You Babe", "Breakfast in Bed", "Sing Our Own Song", "The Way You Do the Things You Do"],
 ["Pass the Dutchie", "Uptown Top Ranking", "Israelites", "Ghost Town", "Too Much Too Young"])
board("Songs by Simply Red", "Music", "medium", ["Simply Red", "songs"],
 ["Holding Back the Years", "Stars", "Fairground", "Money's Too Tight (to Mention)", "Something Got Me Started", "If You Don't Know Me by Now", "Say You Love Me", "For Your Babies", "It's Only Love", "A New Flame", "Angel", "The Right Thing", "Sunrise", "Ain't That a Lot of Love", "Ev'ry Time We Say Goodbye"],
 ["Love Is All Around", "Wherever I Lay My Hat", "Sweet Little Mystery", "Every Loser Wins", "Sacrifice"])
board("Songs by Tears for Fears", "Music", "medium", ["Tears for Fears", "songs"],
 ["Mad World", "Everybody Wants to Rule the World", "Shout", "Head over Heels", "Sowing the Seeds of Love", "Pale Shelter", "Change", "Woman in Chains", "Mothers Talk", "Advice for the Young at Heart", "Break It Down Again", "I Believe", "Suffer the Children", "Laid So Low (Tears Roll Down)", "Raoul and the Kings of Spain"],
 ["Don't You (Forget About Me)", "Fade to Grey", "Relax", "Smalltown Boy", "Enola Gay"])
board("Hits by Culture Club or Boy George", "Music", "medium", ["Culture Club", "Boy George", "songs"],
 ["Karma Chameleon", "Do You Really Want to Hurt Me", "Church of the Poison Mind", "Time (Clock of the Heart)", "Victims", "It's a Miracle", "Miss Me Blind", "I'll Tumble 4 Ya", "The War Song", "Move Away", "Everything I Own", "The Crying Game", "I Just Wanna Be Loved", "Mistake No. 3", "God Thank You Woman"],
 ["Tainted Love", "Relax", "Wham Rap!", "Too Shy", "Come On Eileen"])
board("Songs by Wet Wet Wet", "Music", "medium", ["Wet Wet Wet", "songs", "Scotland"],
 ["Love Is All Around", "Sweet Little Mystery", "Wishing I Was Lucky", "Angel Eyes", "Goodnight Girl", "With a Little Help from My Friends", "Julia Says", "Temptation", "Sweet Surrender", "Don't Want to Forgive Me Now", "Somewhere Somehow", "If I Never See You Again", "Strange", "Yesterday", "Hold Back the River"],
 ["Holding Back the Years", "Stars", "Wonderful Life", "Perfect", "Ordinary World"])
board("Songs by Arctic Monkeys", "Music", "medium", ["Arctic Monkeys", "Sheffield", "songs"],
 ["I Bet You Look Good on the Dancefloor", "When the Sun Goes Down", "Fluorescent Adolescent", "Do I Wanna Know?", "R U Mine?", "Why'd You Only Call Me When You're High?", "505", "Brianstorm", "Crying Lightning", "Mardy Bum", "A Certain Romance", "Arabella", "Teddy Picker", "Four Out of Five", "Cornerstone"],
 ["Mr. Brightside", "I Predict a Riot", "Chelsea Dagger", "Take Me Out", "Ruby"])
board("Songs by the Stereophonics", "Music", "medium", ["Stereophonics", "Wales", "songs"],
 ["Dakota", "Have a Nice Day", "Maybe Tomorrow", "Local Boy in the Photograph", "The Bartender and the Thief", "Just Looking", "Pick a Part That's New", "Mr. Writer", "Indian Summer", "It Means Nothing", "Moviestar", "Handbags and Gladrags", "Step on My Old Size Nines", "A Thousand Trees", "Superman"],
 ["A Design for Life", "Mulder and Scully", "Road Rage", "Motorcycle Emptiness", "Chasing Cars"])
board("Songs by Lady Gaga", "Music", "easy", ["Lady Gaga", "songs"],
 ["Just Dance", "Poker Face", "Bad Romance", "Paparazzi", "Telephone", "Alejandro", "Born This Way", "Shallow", "Rain on Me", "Applause", "Million Reasons", "Hold My Hand", "Die with a Smile", "Always Remember Us This Way", "The Edge of Glory"],
 ["Umbrella", "Toxic", "Firework", "Halo", "Chandelier"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-36.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'boards written')
