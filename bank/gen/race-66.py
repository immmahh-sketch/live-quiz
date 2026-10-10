# Bank session 10 Oct 2026: 2 more general races -> bank/race-66.json. 20 rows each, target 10; wrong options are
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

race("which famous 'Park'?", "General knowledge", "medium", ["parks", "wordplay"], [
 ("Steven Spielberg's 1993 dinosaur film", "Jurassic", ["Cretaceous", "Triassic", "Prehistoric"]), ("New York's great park, with Strawberry Fields", "Central", ["Prospect", "Battery", "Bryant"]),
 ("London park with Speakers' Corner and the Serpentine", "Hyde", ["Green", "St James's", "Holland"]), ("Cartoon town in Colorado, home of Cartman and Kenny", "South", ["North", "East", "West"]),
 ("Where Alan Turing and the codebreakers cracked Enigma", "Bletchley", ["Woburn", "Cliveden", "Chequers"]), ("The Moscow park in the Scorpions' 'Wind of Change'", "Gorky", ["Pushkin", "Lenin", "Tolstoy"]),
 ("The Glasgow ground nicknamed 'Paradise'", "Celtic", ["Fir", "Rugby", "McDiarmid"]), ("Everton's home until 2025", "Goodison", ["Prenton", "Boundary", "Ewood"]),
 ("Sunderland's ground until 1997", "Roker", ["Ayresome", "Victoria", "Brunton"]), ("Newcastle United's home", "St James'", ["St Andrew's", "Brunton", "Ayresome"]),
 ("Crystal Palace's ground", "Selhurst", ["Upton", "Griffin", "Boundary"]), ("Scotland's national football stadium", "Hampden", ["Fir", "McDiarmid", "Rugby"]),
 ("The American band behind 'In the End' and 'Numb'", "Linkin", ["Lincoln", "Laurel", "Lynwood"]), ("Home of London Zoo", "Regent's", ["Holland", "Victoria", "Green"]),
 ("London's biggest Royal Park, where deer roam free", "Richmond", ["Bushy", "Greenwich", "Holland"]), ("Dublin's huge park, home of the Irish President", "Phoenix", ["Herbert", "Marlay", "Fairview"]),
 ("America's first national park, home of Old Faithful", "Yellowstone", ["Yosemite", "Glacier", "Sequoia"]), ("Jane Austen's novel about Fanny Price", "Mansfield", ["Northanger", "Netherfield", "Pemberley"]),
 ("Aston Villa's home", "Villa", ["Ewood", "Prenton", "Boundary"]), ("The Thames-side park with a Peace Pagoda, opposite Chelsea", "Battersea", ["Bishop's", "Kennington", "Vauxhall"])])

race("which famous 'Hill'?", "General knowledge", "medium", ["hills", "wordplay"], [
 ("Hugh Grant's travel bookshop is in this 1999 film", "Notting", ["Kensington", "Holland", "Bayswater"]), ("Home of the US Congress", "Capitol", ["Senate", "Liberty", "Federal"]),
 ("The London viewpoint just north of Regent's Park", "Primrose", ["Parliament", "Telegraph", "Haverstock"]), ("The Surrey beauty spot of the picnic in Jane Austen's Emma", "Box", ["Leith", "Ranmore", "Holmbury"]),
 ("The comedian chased about to 'Yakety Sax'", "Benny", ["Dick", "Kenny", "Frankie"]), ("Formula One champion in 1996, son of a champion", "Damon", ["Graham", "Phil", "Jimmy"]),
 ("The big-collared comedian of TV Burp", "Harry", ["Bobby", "Paul", "Vic"]), ("Europe's tallest prehistoric man-made mound, near Avebury", "Silbury", ["Maiden", "Solsbury", "Haddon"]),
 ("The 1775 battle outside Boston", "Bunker", ["Cemetery", "Seminary", "Chapultepec"]), ("The Lancashire hill of the 1612 witch trials", "Pendle", ["Rivington", "Darwen", "Holcombe"]),
 ("The Fugees singer of 'Doo Wop (That Thing)'", "Lauryn", ["Erykah", "Alicia", "Macy"]), ("Where traitors were publicly beheaded, beside the Tower of London", "Tower", ["Ludgate", "Snow", "Cornhill"]),
 ("The cobbled Shaftesbury street from the Hovis advert", "Gold", ["Silver", "Castle", "Bell"]), ("The hill of the emperors' palaces in Rome", "Palatine", ["Capitoline", "Aventine", "Quirinal"]),
 ("The 1987 Vietnam War film about the fight for Hill 937", "Hamburger", ["Pork Chop", "Heartbreak", "Firebase"]), ("Where Fats Domino found his thrill", "Blueberry", ["Strawberry", "Cherry", "Huckleberry"]),
 ("Edinburgh's hill with the unfinished National Monument", "Calton", ["Corstorphine", "Blackford", "Braid"]), ("The South London velodrome used at the 1948 Olympics", "Herne", ["Tulse", "Forest", "Denmark"]),
 ("The North London district below Alexandra Palace", "Muswell", ["Tufnell", "Haverstock", "Forest"]), ("The country singer married to Tim McGraw", "Faith", ["Shania", "Reba", "Dolly"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-66.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
