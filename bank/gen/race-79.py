# Bank session 10 Oct 2026: 2 more general races -> bank/race-79.json. 20 rows each, target 10; wrong options are
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

race("which famous 'Cat'?", "General knowledge", "medium", ["cats", "wordplay"], [
 ("Squeeze's 1979 hit", "Cool for Cats", ["Up the Junction", "Labelled with Love", "Tempted"]), ("The singer of 'Wild World', later Yusuf Islam", "Cat Stevens", ["Cat Power", "Van Morrison", "James Taylor"]),
 ("Selina Kyle's alter ego", "Catwoman", ["Harley Quinn", "Poison Ivy", "Black Canary"]), ("The presenter of SM:TV Live with Ant and Dec", "Cat Deeley", ["Holly Willoughby", "Fearne Cotton", "Kate Thornton"]),
 ("The string game passed between two people's fingers", "Cat's cradle", ["Knucklebones", "Jacks", "Pick-up sticks"]), ("An overpaid boss", "Fat cat", ["Old boy", "Golden goose", "Cash cow"]),
 ("The 1995 thriller with Sigourney Weaver on a killer's trail", "Copycat", ["Se7en", "The Bone Collector", "Kiss the Girls"]), ("The swing-wing fighter jet in Top Gun", "Tomcat", ["Hornet", "Eagle", "Falcon"]),
 ("Tom Jones's 1965 hit", "What's New Pussycat?", ["It's Not Unusual", "Delilah", "Green, Green Grass of Home"]), ("Dr Seuss's 1957 book", "The Cat in the Hat", ["Green Eggs and Ham", "How the Grinch Stole Christmas!", "Fox in Socks"]),
 ("Tennessee Williams's play about Maggie and Brick", "Cat on a Hot Tin Roof", ["A Streetcar Named Desire", "The Glass Menagerie", "Sweet Bird of Youth"]), ("The rockabilly band behind 'Stray Cat Strut'", "Stray Cats", ["Alley Cats", "Polecats", "Blue Cats"]),
 ("The girl group behind 'Don't Cha'", "Pussycat Dolls", ["Sugababes", "Girlicious", "Danity Kane"]), ("Edward Lear's pair who went to sea in a pea-green boat", "The Owl and the Pussycat", ["The Jumblies", "The Dong with a Luminous Nose", "The Pobble Who Has No Toes"]),
 ("Andrew Lloyd Webber's musical based on T. S. Eliot", "Cats", ["Evita", "Starlight Express", "Aspects of Love"]), ("Someone who fakes an online identity to fool people", "Catfish", ["Troll", "Sock puppet", "Bot"]),
 ("A nervous, easily frightened person", "Scaredy-cat", ["Wet blanket", "Killjoy", "Couch potato"]), ("The North American wildcat named after its stubby tail", "Bobcat", ["Ocelot", "Puma", "Margay"]),
 ("Disney's 1970 film with Duchess and Thomas O'Malley", "The Aristocats", ["Oliver & Company", "Lady and the Tramp", "The Rescuers"]), ("A thief who climbs into houses", "Cat burglar", ["Cat's paw", "Cracksman", "Pickpocket"])])

race("which famous 'Wall'?", "General knowledge", "medium", ["walls", "wordplay"], [
 ("The Roman wall from Wallsend to Bowness-on-Solway", "Hadrian's Wall", ["Offa's Dyke", "Severus's Wall", "Roman Rampart"]), ("The Roman wall between the Forth and the Clyde", "Antonine Wall", ["Offa's Dyke", "Wat's Dyke", "Severan Wall"]),
 ("It fell in November 1989", "Berlin Wall", ["Iron Curtain", "Checkpoint Charlie", "Peace Wall"]), ("Jerusalem's holiest place of Jewish prayer", "Western Wall", ["Temple Mount", "Dome of the Rock", "Via Dolorosa"]),
 ("New York's financial district", "Wall Street", ["Fifth Avenue", "Broadway", "Madison Avenue"]), ("Pink Floyd's 1979 double album", "The Wall", ["Animals", "The Dark Side of the Moon", "Wish You Were Here"]),
 ("Phil Spector's famous production style", "Wall of Sound", ["Motown Sound", "Philly Sound", "Mersey Beat"]), ("The fairground motorbike stunt round a wooden drum", "Wall of Death", ["Globe of Death", "Loop the Loop", "Ring of Fire"]),
 ("What an actor breaks by talking to the audience", "Fourth wall", ["Third wall", "Proscenium", "Footlights"]), ("A computer's security barrier", "Firewall", ["Antivirus", "Encryption", "Password"]),
 ("The online barrier that makes you subscribe to read", "Paywall", ["Pop-up", "Cookie banner", "Captcha"]), ("A barrier along the shore to keep the waves back", "Sea wall", ["Groyne", "Pier", "Jetty"]),
 ("The 1969 New York riots that sparked the gay rights movement", "Stonewall", ["Greenwich", "Christopher", "Castro"]), ("Pixar's lonely rubbish-squashing robot", "WALL-E", ["EVE", "M-O", "Baymax"]),
 ("The ice cream and sausage brand", "Wall's", ["Walker's", "Lyons", "Birds Eye"]), ("The North Tyneside town where Hadrian's Wall ends", "Wallsend", ["Whitley Bay", "Tynemouth", "North Shields"]),
 ("An indoor wall for rock-climbing practice", "Climbing wall", ["Ropes course", "Via ferrata", "Bouldering mat"]), ("A wall of stones stacked without mortar", "Drystone wall", ["Cob wall", "Wattle and daub", "Pebbledash"]),
 ("China's ancient defence, seen from many a holiday photo", "Great Wall", ["Long Wall", "Forbidden Wall", "Golden Wall"]), ("Labour's northern heartland seats that turned Tory in 2019", "Red Wall", ["Blue Wall", "Brexitland", "Heartland"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-79.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
