# Bank session 10 Oct 2026: 4 more general races -> bank/race-29.json. 20 rows each, target 10; wrong options are
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

race("which fruit or vegetable is this a variety of?", "Food and drink", "medium", ["fruit", "vegetables", "varieties"], [
 ("Granny Smith", "Apple", ["Quince", "Peach", "Nectarine"]), ("Conference", "Pear", ["Quince", "Apricot", "Peach"]),
 ("Cavendish", "Banana", ["Papaya", "Pineapple", "Guava"]), ("Hass", "Avocado", ["Papaya", "Guava", "Lime"]),
 ("Victoria", "Plum", ["Apricot", "Peach", "Nectarine"]), ("Maris Piper", "Potato", ["Parsnip", "Sweet potato", "Turnip"]),
 ("Morello", "Cherry", ["Raspberry", "Blackcurrant", "Redcurrant"]), ("Elsanta", "Strawberry", ["Raspberry", "Blackberry", "Gooseberry"]),
 ("Seville", "Orange", ["Lemon", "Lime", "Tangerine"]), ("Medjool", "Date", ["Apricot", "Prune", "Lychee"]),
 ("Alphonso", "Mango", ["Papaya", "Lychee", "Guava"]), ("Brown Turkey", "Fig", ["Pomegranate", "Quince", "Apricot"]),
 ("Moneymaker", "Tomato", ["Pepper", "Aubergine", "Cucumber"]), ("Galia", "Melon", ["Pineapple", "Papaya", "Cucumber"]),
 ("Hayward", "Kiwi fruit", ["Gooseberry", "Passion fruit", "Lychee"]), ("Thompson Seedless", "Grape", ["Blueberry", "Redcurrant", "Gooseberry"]),
 ("Little Gem", "Lettuce", ["Cabbage", "Spinach", "Kale"]), ("Chantenay", "Carrot", ["Parsnip", "Turnip", "Beetroot"]),
 ("Tenderstem", "Broccoli", ["Cauliflower", "Asparagus", "Kale"]), ("Ruby Red", "Grapefruit", ["Lemon", "Pomegranate", "Tangerine"])])

race("what does this Yiddish word mean?", "Words and language", "medium", ["Yiddish", "words"], [
 ("Chutzpah", "Cheek or nerve", ["Bad luck", "Show-off", "Rumour"]), ("Klutz", "Clumsy person", ["Show-off", "Coward", "Liar"]),
 ("Schlep", "Trudge or haul", ["Gossip", "Shout", "Doze"]), ("Kvetch", "Complain", ["Gossip", "Shout", "Boast"]),
 ("Nosh", "Food or a snack", ["Party", "Hangover", "Bargain"]), ("Mensch", "Good, decent person", ["Show-off", "Bully", "Liar"]),
 ("Schmaltz", "Sickly sentimentality", ["Noise", "Rumour", "Bargain"]), ("Spiel", "Sales patter", ["Argument", "Bargain", "Rumour"]),
 ("Shtick", "Comic routine", ["Argument", "Bad luck", "Hangover"]), ("Maven", "Expert", ["Fool", "Coward", "Thief"]),
 ("Meshuga", "Crazy", ["Sleepy", "Delicious", "Lucky"]), ("Tush", "Bottom", ["Belly", "Nose", "Elbow"]),
 ("Schmooze", "Chat someone up", ["Shout at someone", "Steal from someone", "Tell on someone"]), ("Mazel tov", "Congratulations", ["Goodbye", "Cheers", "Get well soon"]),
 ("Nebbish", "Timid, pitiful person", ["Bully", "Show-off", "Thief"]), ("Kibitz", "Give unwanted advice", ["Steal small items", "Haggle", "Boast"]),
 ("Schmutz", "Dirt", ["Noise", "Hangover", "Rumour"]), ("Glitch", "Small fault", ["Bargain", "Rumour", "Headache"]),
 ("Bupkis", "Absolutely nothing", ["Lucky charm", "Bargain", "Feast"]), ("Tchotchke", "Trinket", ["Tickle", "Hiccup", "Sneeze"])])

race("which sport uses this kit?", "Sport", "medium", ["sports equipment"], [
 ("Shuttlecock", "Badminton", ["Squash", "Table tennis", "Tennis"]), ("Puck", "Ice hockey", ["Shinty", "Polo", "Water polo"]),
 ("Stone and broom", "Curling", ["Bobsleigh", "Luge", "Speed skating"]), ("Épée", "Fencing", ["Judo", "Karate", "Kendo"]),
 ("Sliotar", "Hurling", ["Shinty", "Gaelic football", "Rounders"]), ("Pommel horse", "Gymnastics", ["Equestrian", "Polo", "Horse racing"]),
 ("Bails", "Cricket", ["Rounders", "Softball", "Tennis"]), ("Putter", "Golf", ["Polo", "Tennis", "Hockey"]),
 ("Discus", "Athletics", ["Swimming", "Diving", "Shooting"]), ("Jack", "Bowls", ["Skittles", "Shooting", "Sailing"]),
 ("Toe pick", "Figure skating", ["Speed skating", "Skiing", "Snowboarding"]), ("Belay device", "Climbing", ["Sailing", "Diving", "Skiing"]),
 ("Flights", "Darts", ["Shooting", "Skittles", "Table tennis"]), ("Spray deck", "Kayaking", ["Sailing", "Surfing", "Windsurfing"]),
 ("Spider rest", "Snooker", ["Table tennis", "Skittles", "Shooting"]), ("Quiver", "Archery", ["Shooting", "Biathlon", "Javelin"]),
 ("Mitt", "Baseball", ["Rounders", "Netball", "Volleyball"]), ("Scrum cap", "Rugby", ["Boxing", "Wrestling", "Water polo"]),
 ("Mallet and hoops", "Croquet", ["Polo", "Skittles", "Pétanque"]), ("Derailleur", "Cycling", ["Sailing", "Motocross", "Rowing"])])

race("which US state is this landmark in?", "World geography", "medium", ["USA", "landmarks", "states"], [
 ("Mount Rushmore", "South Dakota", ["North Dakota", "Montana", "Nebraska"]), ("The Golden Gate Bridge", "California", ["Oregon", "Colorado", "New Mexico"]),
 ("The Grand Canyon", "Arizona", ["New Mexico", "Colorado", "Oklahoma"]), ("The Statue of Liberty", "New York", ["Delaware", "Connecticut", "Rhode Island"]),
 ("The Space Needle", "Washington", ["Oregon", "Idaho", "Montana"]), ("The Gateway Arch", "Missouri", ["Kansas", "Iowa", "Arkansas"]),
 ("Graceland", "Tennessee", ["Mississippi", "Arkansas", "Alabama"]), ("The Alamo", "Texas", ["New Mexico", "Oklahoma", "Colorado"]),
 ("Old Faithful", "Wyoming", ["Montana", "Idaho", "Colorado"]), ("The Las Vegas Strip", "Nevada", ["New Mexico", "Colorado", "Oregon"]),
 ("The Everglades", "Florida", ["Georgia", "Alabama", "South Carolina"]), ("The Liberty Bell", "Pennsylvania", ["New Jersey", "Maryland", "Virginia"]),
 ("Pearl Harbor", "Hawaii", ["Oregon", "Virginia", "Maine"]), ("Denali", "Alaska", ["Montana", "Idaho", "Maine"]),
 ("Fenway Park", "Massachusetts", ["Connecticut", "Rhode Island", "New Hampshire"]), ("Arches National Park", "Utah", ["Colorado", "New Mexico", "Idaho"]),
 ("The Rock and Roll Hall of Fame", "Ohio", ["Michigan", "Indiana", "West Virginia"]), ("Cloud Gate ('The Bean')", "Illinois", ["Indiana", "Wisconsin", "Michigan"]),
 ("The French Quarter", "Louisiana", ["Mississippi", "Alabama", "Arkansas"]), ("Fort Knox", "Kentucky", ["West Virginia", "Virginia", "Indiana"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-29.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
