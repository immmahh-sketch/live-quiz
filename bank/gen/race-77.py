# Bank session 10 Oct 2026: 2 more general races -> bank/race-77.json. 20 rows each, target 10; wrong options are
# the same kind of thing, never another row's right answer, and never also right for that row.
import json, os
R = []
def race(title, cat, diff, tags, rows):
    rights = {r[1] for r in rows}
    assert len(rows) == 20, (title, len(rows))
    assert len(rights) == 20, (title, 'duplicate right answers')
    bad = [(q, w) for q, right, wrong in rows for w in wrong if w in rights]
    assert not bad, (title, 'recycled', bad)
    for q, right, wrong in rows:
        assert len(wrong) == 3 and len(set(wrong)) == 3 and right not in wrong, (title, q)
    R.append({"type": "race", "text": "The Race: " + title, "target": 10, "category": cat, "tags": tags, "difficulty": diff,
              "bank": [{"q": q, "right": right, "wrong": wrong} for q, right, wrong in rows]})

race("which famous 'Heart'?", "General knowledge", "medium", ["hearts", "wordplay"], [
 ("Mel Gibson's 1995 film about William Wallace", "Braveheart", ["Rob Roy", "Highlander", "Outlaw King"]), ("Richard I's nickname", "Lionheart", ["Longshanks", "Lackland", "Beauclerc"]),
 ("Billy Ray Cyrus's 1992 line-dance hit", "Achy Breaky Heart", ["Cotton Eye Joe", "Boot Scootin' Boogie", "Islands in the Stream"]), ("The US medal for soldiers wounded in action", "Purple Heart", ["Bronze Star", "Silver Star", "Medal of Honor"]),
 ("Edgar Allan Poe's story of a heart beating under the floorboards", "The Tell-Tale Heart", ["The Raven", "The Black Cat", "The Pit and the Pendulum"]), ("The full name of Edinburgh's 'Hearts'", "Heart of Midlothian", ["Hibernian", "St Mirren", "Queen of the South"]),
 ("Bonnie Tyler's 1983 number one", "Total Eclipse of the Heart", ["It's a Heartache", "Holding Out for a Hero", "Lost in France"]), ("Joseph Conrad's novella about a journey up the Congo", "Heart of Darkness", ["Lord Jim", "Nostromo", "The Secret Agent"]),
 ("Neil Young's 1972 US number one", "Heart of Gold", ["Harvest Moon", "Old Man", "Rockin' in the Free World"]), ("Elton John and Kiki Dee's 1976 duet", "Don't Go Breaking My Heart", ["Islands in the Stream", "Up Where We Belong", "I Got You Babe"]),
 ("Céline Dion's song from Titanic", "My Heart Will Go On", ["The Power of Love", "Because You Loved Me", "It's All Coming Back to Me Now"]), ("ITV's police drama set in 1960s Yorkshire", "Heartbeat", ["The Royal", "Born and Bred", "All Creatures Great and Small"]),
 ("Toni Braxton's 1996 ballad", "Un-Break My Heart", ["Breathe Again", "You're Makin' Me High", "He Wasn't Man Enough"]), ("What the Tin Man wants from the Wizard", "A heart", ["A brain", "Courage", "A home"]),
 ("The 'Off with their heads!' card in Alice in Wonderland", "The Queen of Hearts", ["The Red Queen", "The White Queen", "The Duchess"]), ("Elvis's first big hit, in 1956", "Heartbreak Hotel", ["Blue Suede Shoes", "Hound Dog", "Jailhouse Rock"]),
 ("The Ealing comedy where Alec Guinness plays eight victims", "Kind Hearts and Coronets", ["The Ladykillers", "The Lavender Hill Mob", "Passport to Pimlico"]), ("Nirvana's 1993 single from In Utero", "Heart-Shaped Box", ["Smells Like Teen Spirit", "Come as You Are", "Lithium"]),
 ("Yes's 1983 US number one", "Owner of a Lonely Heart", ["Roundabout", "Leave It", "Wonderous Stories"]), ("Blondie's 1979 number one", "Heart of Glass", ["Call Me", "Atomic", "Sunday Girl"])])

race("which famous 'Ice'?", "General knowledge", "medium", ["ice", "wordplay"], [
 ("The rapper of 'Ice Ice Baby'", "Vanilla Ice", ["MC Hammer", "Snow", "Young MC"]), ("The N.W.A rapper who went on to star in Friday", "Ice Cube", ["Dr. Dre", "Eazy-E", "MC Ren"]),
 ("The rapper who plays Fin in Law & Order: SVU", "Ice-T", ["LL Cool J", "Ludacris", "Busta Rhymes"]), ("ITV's celebrity skating show", "Dancing on Ice", ["Strictly Come Dancing", "Stars on Ice", "Skate Nation"]),
 ("Frozen carbon dioxide, used for stage smoke", "Dry ice", ["Liquid nitrogen", "Frost", "Salt"]), ("The invisible frozen layer that makes roads lethal", "Black ice", ["Rime", "Frost", "Slush"]),
 ("George R. R. Martin's fantasy book series", "A Song of Ice and Fire", ["The Wheel of Time", "The Kingkiller Chronicle", "The Dark Tower"]), ("Val Kilmer's rival pilot in Top Gun", "Iceman", ["Maverick", "Goose", "Viper"]),
 ("The 1958 film where John Mills dreams of a cold lager", "Ice Cold in Alex", ["The Cruel Sea", "Sea of Sand", "The Bridge on the River Kwai"]), ("The animated films with Manny, Sid and Scrat", "Ice Age", ["Madagascar", "Shrek", "Kung Fu Panda"]),
 ("The 2014 viral charity craze for motor neurone disease", "Ice Bucket Challenge", ["Cold Water Challenge", "Movember", "No Make-Up Selfie"]), ("The reality show about lorry drivers on frozen Canadian roads", "Ice Road Truckers", ["Deadliest Catch", "Ax Men", "Highway Thru Hell"]),
 ("Doctor Who's reptile warriors from Mars", "Ice Warriors", ["Sontarans", "Silurians", "Zygons"]), ("A huge chunk of glacier floating at sea", "Iceberg", ["Ice floe", "Icicle", "Snowdrift"]),
 ("The sport of the Stanley Cup", "Ice hockey", ["Field hockey", "Lacrosse", "Curling"]), ("The country of Björk and geysers", "Iceland", ["Greenland", "Norway", "Faroe Islands"]),
 ("Ang Lee's 1997 film about two families in 1970s Connecticut", "The Ice Storm", ["Sense and Sensibility", "Brokeback Mountain", "Crouching Tiger, Hidden Dragon"]), ("The 1968 Cold War submarine thriller with Rock Hudson", "Ice Station Zebra", ["The Hunt for Red October", "Das Boot", "Run Silent, Run Deep"]),
 ("A ship built to smash a path through frozen seas", "Icebreaker", ["Ice cutter", "Snowplough", "Trawler"]), ("The touring skating show that began in Ohio in 1943", "Holiday on Ice", ["Disney on Ice", "Stars on Ice", "Ice Capades"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-77.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
