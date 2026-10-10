# Bank session 11 Oct 2026: 15 more Put in order questions -> bank/order-9.json (bands and solo stars, British directors, a TV writer).
# Each theme was checked against every order question title in the live bank (the server also skips any whose items match one already there).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

o("Music", ["Stereophonics", "albums", "Wales"], "hard", "Put these Stereophonics albums in order of release, earliest first", ["Word Gets Around", "Performance and Cocktails", "Just Enough Education to Perform", "You Gotta Go There to Come Back", "Language. Sex. Violence. Other?", "Pull the Pin", "Keep Calm and Carry On"], "earliest first")
o("Music", ["The Killers", "albums"], "medium", "Put these Killers albums in order of release, earliest first", ["Hot Fuss", "Sam's Town", "Day & Age", "Battle Born", "Wonderful Wonderful", "Imploding the Mirage", "Pressure Machine"], "earliest first")
o("Music", ["Kaiser Chiefs", "albums", "Leeds"], "hard", "Put these Kaiser Chiefs albums in order of release, earliest first", ["Employment", "Yours Truly, Angry Mob", "Off with Their Heads", "The Future Is Medieval", "Education, Education, Education & War", "Stay Together", "Duck"], "earliest first")
o("Music", ["Rihanna", "albums"], "medium", "Put these Rihanna albums in order of release, earliest first", ["A Girl Like Me", "Good Girl Gone Bad", "Rated R", "Loud", "Talk That Talk", "Unapologetic", "Anti"], "earliest first")
o("Music", ["Eminem", "albums", "rap"], "medium", "Put these Eminem albums in order of release, earliest first", ["The Slim Shady LP", "The Marshall Mathers LP", "The Eminem Show", "Encore", "Relapse", "Recovery", "Kamikaze"], "earliest first")
o("Music", ["Lady Gaga", "albums"], "medium", "Put these Lady Gaga albums in order of release, earliest first", ["The Fame", "Born This Way", "Artpop", "Joanne", "Chromatica", "Mayhem"], "earliest first")
o("Music", ["Sam Fender", "albums", "North East"], "easy", "Put Sam Fender's albums in order of release, earliest first", ["Hypersonic Missiles", "Seventeen Going Under", "People Watching"], "earliest first")
o("Music", ["Dire Straits", "albums", "Mark Knopfler"], "hard", "Put these Dire Straits albums in order of release, earliest first", ["Dire Straits", "Communiqué", "Making Movies", "Love over Gold", "Brothers in Arms", "On Every Street"], "earliest first")
o("Music", ["Elbow", "albums"], "hard", "Put these Elbow albums in order of release, earliest first", ["Asleep in the Back", "Cast of Thousands", "Leaders of the Free World", "The Seldom Seen Kid", "Build a Rocket Boys!", "The Take Off and Landing of Everything"], "earliest first")
o("Music", ["Snow Patrol", "albums"], "hard", "Put these Snow Patrol albums in order of release, earliest first", ["Final Straw", "Eyes Open", "A Hundred Million Suns", "Fallen Empires", "Wildness"], "earliest first")
o("Music", ["Kings of Leon", "albums"], "hard", "Put these Kings of Leon albums in order of release, earliest first", ["Youth & Young Manhood", "Aha Shake Heartbreak", "Because of the Times", "Only by the Night", "Come Around Sundown", "Mechanical Bull", "Walls"], "earliest first")
o("Film", ["Guy Ritchie", "directors"], "medium", "Put these Guy Ritchie films in order of release, earliest first", ["Lock, Stock and Two Smoking Barrels", "Snatch", "RocknRolla", "Sherlock Holmes", "The Man from U.N.C.L.E.", "Aladdin", "The Gentlemen"], "earliest first")
o("Film", ["Edgar Wright", "directors"], "medium", "Put these Edgar Wright films in order of release, earliest first", ["Shaun of the Dead", "Hot Fuzz", "Scott Pilgrim vs. the World", "The World's End", "Baby Driver", "Last Night in Soho"], "earliest first")
o("Film", ["Ken Loach", "directors"], "hard", "Put these Ken Loach films in order of release, earliest first", ["Kes", "Riff-Raff", "Land and Freedom", "My Name Is Joe", "The Wind That Shakes the Barley", "I, Daniel Blake", "The Old Oak"], "earliest first")
o("TV", ["Sally Wainwright", "British drama"], "hard", "Put these Sally Wainwright dramas in order of first airing, earliest first", ["At Home with the Braithwaites", "Scott & Bailey", "Last Tango in Halifax", "Happy Valley", "Gentleman Jack"], "earliest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-9.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
