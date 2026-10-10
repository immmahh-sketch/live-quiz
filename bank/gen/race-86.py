# Bank session 10 Oct 2026: 2 more general races -> bank/race-86.json. 20 rows each, target 10; wrong options are
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

race("which famous 'Spring'?", "General knowledge", "medium", ["spring", "wordplay"], [
 ("The uprisings across the Middle East from 2010", "Arab Spring", ["Velvet Revolution", "Orange Revolution", "Green Movement"]), ("Czechoslovakia's 1968 reforms, crushed by Soviet tanks", "Prague Spring", ["Velvet Revolution", "Hungarian Uprising", "Solidarity"]),
 ("Rachel Carson's 1962 book about pesticides", "Silent Spring", ["An Inconvenient Truth", "The Population Bomb", "Gaia"]), ("New Jersey's 'Boss'", "Bruce Springsteen", ["Jon Bon Jovi", "Tom Petty", "John Mellencamp"]),
 ("The Simpsons' home town", "Springfield", ["Shelbyville", "Capital City", "Quahog"]), ("The singer of 'Son of a Preacher Man'", "Dusty Springfield", ["Lulu", "Cilla Black", "Sandie Shaw"]),
 ("Long green onions, also called scallions", "Spring onion", ["Shallot", "Leek", "Chive"]), ("South Africa's rugby team", "Springboks", ["Proteas", "Bafana Bafana", "Lions"]),
 ("Victorian London's leaping bogeyman", "Spring-heeled Jack", ["Jack the Ripper", "Sweeney Todd", "Jack Frost"]), ("The extra-big tides around a new or full moon", "Spring tide", ["Neap tide", "Ebb tide", "Tidal bore"]),
 ("The bouncy gundog breed, English or Welsh", "Springer spaniel", ["Cocker spaniel", "Setter", "Pointer"]), ("A thorough clean of the whole house", "Spring clean", ["Elbow grease", "Lick and a promise", "Once-over"]),
 ("The show-stopping number in Mel Brooks's The Producers", "Springtime for Hitler", ["Keep It Gay", "I Wanna Be a Producer", "Along Came Bialy"]), ("The American talk show host famous for chaotic guests", "Jerry Springer", ["Maury Povich", "Ricki Lake", "Jeremy Kyle"]),
 ("The singer of 'Jessie's Girl'", "Rick Springfield", ["Rick Astley", "Bryan Adams", "Huey Lewis"]), ("The American student holiday of beach parties", "Spring Break", ["Reading week", "Gap year", "Prom"]),
 ("The Californian desert resort that was Sinatra's playground", "Palm Springs", ["Palm Beach", "Santa Barbara", "Scottsdale"]), ("The coiled spring that drives a wind-up watch", "Mainspring", ["Hairspring", "Balance wheel", "Escapement"]),
 ("The BBC's live wildlife show in late May", "Springwatch", ["Winterwatch", "Countryfile", "Autumnwatch"]), ("The crispy fried starter at a Chinese takeaway", "Spring roll", ["Prawn toast", "Wonton", "Dim sum"])])

race("which famous 'Snow'?", "General knowledge", "medium", ["snow", "wordplay"], [
 ("The Northern Irish band behind 'Chasing Cars'", "Snow Patrol", ["Ash", "The Divine Comedy", "Two Door Cinema Club"]), ("The pig chased out of Animal Farm by Napoleon", "Snowball", ["Squealer", "Old Major", "Boxer"]),
 ("Tintin's white fox terrier, in English", "Snowy", ["Pluto", "Gnasher", "Dogmatix"]), ("The kind of owl Hedwig is", "Snowy owl", ["Barn owl", "Tawny owl", "Eagle owl"]),
 ("The Channel 4 newsreader who shares a name with the King in the North", "Jon Snow", ["Jon Sopel", "Jeremy Paxman", "Krishnan Guru-Murthy"]), ("The BBC's original swingometer man", "Peter Snow", ["David Dimbleby", "Jeremy Vine", "Robin Day"]),
 ("The TV historian who is Peter's son", "Dan Snow", ["Dan Jones", "Tom Holland", "David Olusoga"]), ("An insult for an easily offended young person", "Snowflake", ["Wet blanket", "Karen", "Mummy's boy"]),
 ("The endangered big cat of the Himalayas", "Snow leopard", ["Clouded leopard", "Lynx", "Puma"]), ("The 2012 sequel, 'The Snowman and the ...'", "Snowdog", ["Snowbear", "Snowbaby", "Reindeer"]),
 ("Hans Christian Andersen's tale that inspired Frozen", "The Snow Queen", ["The Ice Maiden", "The Little Match Girl", "Thumbelina"]), ("Red Hot Chili Peppers' 2006 hit", "Snow (Hey Oh)", ["Californication", "Scar Tissue", "Dani California"]),
 ("Riding a single board down the slopes", "Snowboarding", ["Skiing", "Sledging", "Skeleton"]), ("When school shuts because of the weather", "Snow day", ["Inset day", "Bank holiday", "Duvet day"]),
 ("The Welsh national park around Yr Wyddfa", "Snowdonia", ["Brecon Beacons", "Pembrokeshire Coast", "Gower"]), ("When a problem keeps rolling and getting bigger", "Snowball effect", ["Domino effect", "Butterfly effect", "Ripple effect"]),
 ("'Oh the weather outside is frightful...'", "Let It Snow!", ["Winter Wonderland", "Baby, It's Cold Outside", "Jingle Bell Rock"]), ("A glass dome you shake to make a winter scene", "Snow globe", ["Lava lamp", "Kaleidoscope", "Music box"]),
 ("The tracked vehicle that grooms the ski slopes", "Snowcat", ["Snowmobile", "Ski-Doo", "Quad bike"]), ("The Disney princess who lives with seven dwarfs", "Snow White", ["Cinderella", "Aurora", "Belle"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-86.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
