# Bank session 10 Oct 2026: 3 more general races -> bank/race-50.json. 20 rows each, target 10; wrong options are
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

race("which US state was this famous American born in?", "History", "hard", ["USA", "birthplaces", "states"], [
 ("Elvis Presley", "Mississippi", ["Florida", "North Carolina", "Oklahoma"]), ("Barack Obama", "Hawaii", ["Alaska", "Oregon", "Nevada"]),
 ("Donald Trump", "New York", ["Florida", "Connecticut", "New Hampshire"]), ("Dolly Parton", "Tennessee", ["North Carolina", "West Virginia", "Virginia"]),
 ("Taylor Swift", "Pennsylvania", ["Maryland", "Delaware", "Connecticut"]), ("Beyoncé", "Texas", ["Oklahoma", "Florida", "Arizona"]),
 ("Bruce Springsteen", "New Jersey", ["Delaware", "Connecticut", "Maryland"]), ("Bob Dylan", "Minnesota", ["Wisconsin", "Michigan", "Iowa"]),
 ("Michael Jackson", "Indiana", ["Michigan", "Wisconsin", "Iowa"]), ("Johnny Cash", "Arkansas", ["Oklahoma", "Florida", "North Carolina"]),
 ("Abraham Lincoln", "Kentucky", ["Virginia", "West Virginia", "North Carolina"]), ("Marilyn Monroe", "California", ["Nevada", "Oregon", "Arizona"]),
 ("Neil Armstrong", "Ohio", ["Michigan", "Wisconsin", "West Virginia"]), ("Martin Luther King Jr", "Georgia", ["Florida", "South Carolina", "North Carolina"]),
 ("Jimi Hendrix", "Washington", ["Oregon", "Idaho", "Montana"]), ("Louis Armstrong", "Louisiana", ["Florida", "Oklahoma", "South Carolina"]),
 ("Mark Twain", "Missouri", ["Kansas", "Iowa", "Nebraska"]), ("Walt Disney", "Illinois", ["Michigan", "Wisconsin", "Iowa"]),
 ("John F. Kennedy", "Massachusetts", ["Connecticut", "Rhode Island", "Vermont"]), ("Harper Lee", "Alabama", ["Florida", "South Carolina", "North Carolina"])])

race("which city is this famous market in?", "Travel", "medium", ["markets", "cities"], [
 ("The Grand Bazaar", "Istanbul", ["Ankara", "Izmir", "Athens"]), ("La Boqueria", "Barcelona", ["Valencia", "Seville", "Bilbao"]),
 ("Borough Market", "London", ["Birmingham", "Manchester", "Bristol"]), ("Chatuchak Weekend Market", "Bangkok", ["Chiang Mai", "Phuket", "Hanoi"]),
 ("Toyosu fish market", "Tokyo", ["Osaka", "Kyoto", "Yokohama"]), ("Pike Place Market", "Seattle", ["Portland", "San Francisco", "Boston"]),
 ("Mercado de San Miguel", "Madrid", ["Valencia", "Seville", "Bilbao"]), ("Khan el-Khalili", "Cairo", ["Alexandria", "Luxor", "Marrakesh"]),
 ("The Naschmarkt", "Vienna", ["Salzburg", "Graz", "Budapest"]), ("The Viktualienmarkt", "Munich", ["Berlin", "Hamburg", "Frankfurt"]),
 ("The Mercato Centrale", "Florence", ["Rome", "Milan", "Bologna"]), ("The Rialto Market", "Venice", ["Verona", "Padua", "Trieste"]),
 ("The Albert Cuyp Market", "Amsterdam", ["Rotterdam", "Utrecht", "The Hague"]), ("The Queen Victoria Market", "Melbourne", ["Sydney", "Adelaide", "Brisbane"]),
 ("The Grainger Market", "Newcastle", ["Sunderland", "Durham", "Middlesbrough"]), ("Kirkgate Market", "Leeds", ["Bradford", "Sheffield", "York"]),
 ("St Lawrence Market", "Toronto", ["Montreal", "Ottawa", "Vancouver"]), ("La Vucciria", "Palermo", ["Naples", "Catania", "Bari"]),
 ("Chandni Chowk", "Delhi", ["Mumbai", "Kolkata", "Jaipur"]), ("Torvehallerne", "Copenhagen", ["Stockholm", "Oslo", "Aarhus"])])

race("which sport does this body run?", "Sport", "medium", ["governing bodies", "sport"], [
 ("FIDE", "Chess", ["Draughts", "Bridge", "Backgammon"]), ("The PDC", "Darts", ["Pool", "Bowls", "Skittles"]),
 ("The WPBSA", "Snooker", ["Pool", "Bowls", "Table tennis"]), ("The R&A", "Golf", ["Bowls", "Croquet", "Archery"]),
 ("The ITF", "Tennis", ["Badminton", "Squash", "Table tennis"]), ("World Rugby", "Rugby union", ["Netball", "Lacrosse", "Handball"]),
 ("The RFL", "Rugby league", ["Netball", "Lacrosse", "Handball"]), ("The FIA", "Motor sport", ["Sailing", "Rowing", "Bobsleigh"]),
 ("FIBA", "Basketball", ["Netball", "Handball", "Lacrosse"]), ("The FIVB", "Volleyball", ["Handball", "Netball", "Badminton"]),
 ("FIS", "Skiing", ["Bobsleigh", "Curling", "Sailing"]), ("The ISU", "Ice skating", ["Curling", "Bobsleigh", "Gymnastics"]),
 ("The FEI", "Equestrian", ["Polo", "Archery", "Fencing"]), ("The IJF", "Judo", ["Wrestling", "Fencing", "Weightlifting"]),
 ("The FIH", "Hockey", ["Lacrosse", "Netball", "Handball"]), ("The British Boxing Board of Control", "Boxing", ["Wrestling", "Fencing", "Weightlifting"]),
 ("The Jockey Club", "Horse racing", ["Polo", "Greyhound racing", "Show jumping"]), ("The UCI", "Cycling", ["Rowing", "Sailing", "Canoeing"]),
 ("The ICC", "Cricket", ["Rounders", "Baseball", "Softball"]), ("World Aquatics (once FINA)", "Swimming", ["Rowing", "Sailing", "Canoeing"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-50.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
