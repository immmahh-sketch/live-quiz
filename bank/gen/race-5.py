# Bank session 9 Oct 2026 (fourth pass): 4 more general races -> bank/race-5.json. 20 rows each, target 10; wrong
# options are the same kind of thing, never another row's right answer, and never also right for that row.
import json, os
R = []
def race(title, cat, diff, tags, rows):
    rights = {r[1] for r in rows}
    assert len(rows) == 20, (title, len(rows))
    assert len(rights) == 20, (title, 'duplicate right answers')
    bad = [(q, w) for q, right, wrong in rows for w in wrong if w in rights]
    assert not bad, (title, 'recycled', bad)
    for q, right, wrong in rows:
        assert len(wrong) == 3 and len(set(wrong)) == 3, (title, q)
    R.append({"type": "race", "text": "The Race: " + title, "target": 10, "category": cat, "tags": tags, "difficulty": diff,
              "bank": [{"q": q, "right": right, "wrong": wrong} for q, right, wrong in rows]})

race("finish the Christmas song title", "Christmas songs", "easy", ["Christmas", "songs"], [
 ("All I Want for Christmas Is …", "You", ["Me", "Mine", "Here"]), ("Rockin' Around the Christmas …", "Tree", ["Fire", "Square", "Table"]),
 ("Fairytale of New …", "York", ["Jersey", "Orleans", "Mexico"]), ("Merry Xmas …", "Everybody", ["Everyone", "Anyone", "Somebody"]),
 ("Stop the …", "Cavalry", ["Calvary", "Cavaliers", "Carnival"]), ("Mistletoe and …", "Wine", ["Mince", "Wishes", "Whisky"]),
 ("Last …", "Christmas", ["Summer", "Chance", "Dance"]), ("Walking in the …", "Air", ["Rain", "Park", "Clouds"]),
 ("Wonderful …", "Christmastime", ["Wintertime", "Snowtime", "Holiday"]), ("Jingle Bell …", "Rock", ["Roll", "Ring", "Rhythm"]),
 ("Santa Claus Is Comin' to …", "Town", ["Tea", "Dinner", "Bed"]), ("I Wish It Could Be Christmas …", "Everyday", ["Forever", "Every Year", "Today"]),
 ("Frosty the …", "Snowman", ["Snowflake", "Snowball", "Iceman"]), ("Rudolph the Red-Nosed …", "Reindeer", ["Nose", "Sleigh", "Elf"]),
 ("Let It …", "Snow", ["Go", "Be", "Shine"]), ("Feliz …", "Navidad", ["Noël", "Natale", "Navidades"]),
 ("Deck the …", "Halls", ["Hall", "Walls", "Hearth"]), ("Silent …", "Night", ["Morning", "Evening", "Knight"]),
 ("Baby, It's Cold …", "Outside", ["Inside", "Tonight", "Out There"]), ("Little Drummer …", "Boy", ["Girl", "Man", "Band"])])

race("what's the German word?", "Words and language", "medium", ["German", "languages"], [
 ("Dog", "Hund", ["Hand", "Huhn", "Hut"]), ("Cat", "Katze", ["Kuchen", "Kerze", "Kasse"]), ("House", "Haus", ["Hose", "Hals", "Heu"]),
 ("Water", "Wasser", ["Wetter", "Wagen", "Wurst"]), ("Bread", "Brot", ["Brief", "Brücke", "Bruder"]), ("Beer", "Bier", ["Biene", "Birne", "Bild"]),
 ("Car", "Auto", ["Ampel", "Arm", "Abend"]), ("Book", "Buch", ["Bauch", "Baum", "Berg"]), ("Friend", "Freund", ["Frage", "Feuer", "Fenster"]),
 ("Night", "Nacht", ["Nase", "Nadel", "Nebel"]), ("Day", "Tag", ["Tisch", "Tor", "Tee"]), ("Red", "Rot", ["Rad", "Rose", "Rock"]),
 ("Black", "Schwarz", ["Schnee", "Schloss", "Schiff"]), ("White", "Weiß", ["Wein", "Wald", "Wolke"]), ("Apple", "Apfel", ["Affe", "Ast", "Anfang"]),
 ("Milk", "Milch", ["Mond", "Maus", "Mutter"]), ("Child", "Kind", ["König", "Kopf", "Kuh"]), ("Woman", "Frau", ["Fisch", "Fuß", "Flasche"]),
 ("Man", "Mann", ["Messer", "Mantel", "Markt"]), ("Thank you", "Danke", ["Bitte", "Hallo", "Tschüss"])])

race("which city is this airport in?", "Travel", "medium", ["airports", "cities"], [
 ("JFK", "New York", ["Philadelphia", "Atlanta", "Detroit"]), ("Charles de Gaulle", "Paris", ["Lyon", "Brussels", "Geneva"]),
 ("Schiphol", "Amsterdam", ["Rotterdam", "Brussels", "Hamburg"]), ("Changi", "Singapore", ["Hong Kong", "Kuala Lumpur", "Bangkok"]),
 ("Narita", "Tokyo", ["Osaka", "Seoul", "Beijing"]), ("O'Hare", "Chicago", ["Dallas", "Atlanta", "Detroit"]),
 ("LAX", "Los Angeles", ["San Francisco", "Las Vegas", "San Diego"]), ("Dulles", "Washington, D.C.", ["Philadelphia", "Baltimore", "Atlanta"]),
 ("Barajas", "Madrid", ["Valencia", "Seville", "Lisbon"]), ("Fiumicino", "Rome", ["Naples", "Florence", "Venice"]),
 ("Kastrup", "Copenhagen", ["Aarhus", "Helsinki", "Hamburg"]), ("Arlanda", "Stockholm", ["Gothenburg", "Helsinki", "Malmö"]),
 ("Gardermoen", "Oslo", ["Bergen", "Helsinki", "Gothenburg"]), ("Malpensa", "Milan", ["Turin", "Venice", "Naples"]),
 ("El Prat", "Barcelona", ["Valencia", "Seville", "Bilbao"]), ("Pearson", "Toronto", ["Montreal", "Vancouver", "Ottawa"]),
 ("Logan", "Boston", ["Seattle", "Denver", "Miami"]), ("Kingsford Smith", "Sydney", ["Melbourne", "Perth", "Brisbane"]),
 ("John Lennon", "Liverpool", ["Manchester", "Leeds", "Glasgow"]), ("George Best", "Belfast", ["Dublin", "Cork", "Derry"])])

race("what's the past tense?", "Words and language", "medium", ["grammar", "words"], [
 ("Go", "Went", ["Goed", "Gone", "Wended"]), ("Swim", "Swam", ["Swum", "Swimmed", "Swimmen"]), ("Run", "Ran", ["Runned", "Rung", "Ranned"]),
 ("Bring", "Brought", ["Brang", "Brung", "Bringed"]), ("Think", "Thought", ["Thunk", "Thinked", "Thaught"]), ("Catch", "Caught", ["Catched", "Cotch", "Caughten"]),
 ("Teach", "Taught", ["Teached", "Tought", "Teachen"]), ("Buy", "Bought", ["Buyed", "Boughten", "Bayed"]), ("Fly", "Flew", ["Flied", "Flown", "Flyed"]),
 ("Draw", "Drew", ["Drawed", "Drawn", "Druw"]), ("Throw", "Threw", ["Throwed", "Thrown", "Thrue"]), ("Sing", "Sang", ["Sung", "Singed", "Sanged"]),
 ("Drink", "Drank", ["Drunk", "Drinked", "Drunked"]), ("Begin", "Began", ["Begun", "Beginned", "Begon"]), ("Freeze", "Froze", ["Frozen", "Freezed", "Frizz"]),
 ("Choose", "Chose", ["Chosen", "Choosed", "Chuse"]), ("Speak", "Spoke", ["Spoken", "Speaked", "Spoked"]), ("Write", "Wrote", ["Written", "Writed", "Wrate"]),
 ("Ride", "Rode", ["Ridden", "Rided", "Rade"]), ("Eat", "Ate", ["Eaten", "Eated", "Ated"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-5.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
