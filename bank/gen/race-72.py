# Bank session 10 Oct 2026: 2 more general races -> bank/race-72.json. 20 rows each, target 10; wrong options are
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

race("which famous 'Rock'?", "General knowledge", "medium", ["rocks", "wordplay"], [
 ("Graham Greene's 1938 novel, named after the sweet in Pinkie's pocket", "Brighton", ["Blackpool", "Margate", "Southend"]), ("Uluru's old English name", "Ayers", ["Olgas", "Kings", "Simpson"]),
 ("Where the Pilgrim Fathers are said to have stepped ashore", "Plymouth", ["Provincetown", "Boston", "Jamestown"]), ("The state capital of Arkansas", "Little", ["Fort Smith", "Hot Springs", "Fayetteville"]),
 ("The music of the Sex Pistols and the Clash", "Punk", ["Garage", "Grunge", "Indie"]), ("Fred Flintstone's home town", "Bedrock", ["Rockville", "Stonebridge", "Granite"]),
 ("Jim Henson's 1980s puppet show set in a cave", "Fraggle", ["Muppet", "Doozer", "Gorg"]), ("The Detroit rapper-rocker behind 'All Summer Long'", "Kid", ["Iggy", "Pop", "Ice"]),
 ("Elvis's 1957 film and hit song", "Jailhouse", ["Jailbird", "Prison", "Cellblock"]), ("The café chain founded in London in 1971, with guitars on the walls", "Hard", ["Heavy", "Soft", "Planet"]),
 ("'Picnic at ... Rock', the 1975 Australian mystery film", "Hanging", ["Standing", "Hidden", "Haunted"]), ("The comedian slapped by Will Smith at the 2022 Oscars", "Chris", ["Kevin", "Dave", "Eddie"]),
 ("The music of T. Rex, Slade and Sweet", "Glam", ["Pub", "Soft", "Folk"]), ("Stephen King's fictional Maine town, and Rob Reiner's film company", "Castle", ["Salem's", "Derry", "Haven"]),
 ("The Firth of Forth island with the world's biggest gannet colony", "Bass", ["May", "Inchkeith", "Fidra"]), ("Smooth 1970s soft rock, later nicknamed after boats", "Yacht", ["Boat", "Cruise", "Sail"]),
 ("A Dublin suburb, and the world's biggest investment firm", "Blackrock", ["Blackstone", "Blackpool", "Rockefeller"]), ("What the Apollo astronauts brought back to Earth", "Moon", ["Star", "Space", "Comet"]),
 ("The music of Yes, Genesis and ELP", "Prog", ["Psych", "Soft", "Folk"]), ("Western Australia's granite cliff shaped like a breaking wave", "Wave", ["Surf", "Tide", "Crest"])])

race("which famous 'Valley'?", "General knowledge", "medium", ["valleys", "wordplay"], [
 ("California's tech hub", "Silicon", ["Silver", "Digital", "Carbon"]), ("America's hottest place, in California's desert", "Death", ["Devil's", "Dust", "Dry"]),
 ("Africa's Great ... Valley", "Rift", ["Divide", "Fault", "Crack"]), ("The California wine valley of Robert Mondavi and Opus One", "Napa", ["Sonoma", "Central", "Russian River"]),
 ("The police force covering Oxfordshire, Berkshire and Buckinghamshire", "Thames", ["Chiltern", "Kennet", "Cotswold"]), ("The Idaho resort where Hemingway died, and media moguls meet each July", "Sun", ["Bear", "Aspen", "Vail"]),
 ("Sarah Lancashire's Yorkshire police drama", "Happy", ["Sunny", "Calder", "Hidden"]), ("The creepy dip in how we feel about almost-human robots", "Uncanny", ["Eerie", "Weird", "Creepy"]),
 ("The Virginia valley and national park along the Skyline Drive", "Shenandoah", ["Blue Ridge", "Cumberland", "Appalachian"]), ("The valley of the river where Jesus was baptised", "Jordan", ["Kidron", "Hinnom", "Jezreel"]),
 ("The ancient civilisation of Harappa and Mohenjo-daro", "Indus", ["Ganges", "Tigris", "Nile"]), ("The New South Wales wine valley north of Sydney", "Hunter", ["Clare", "Barossa", "Yarra"]),
 ("The sandstone buttes of John Ford's westerns, on the Arizona–Utah border", "Monument", ["Painted", "Canyon", "Red Rock"]), ("The river valley of Tintern Abbey on the Welsh border", "Wye", ["Usk", "Severn", "Teme"]),
 ("Los Angeles's 'Valley', home of the 'Valley girls'", "San Fernando", ["Santa Clarita", "San Gabriel", "Simi"]), ("The California resort that hosted the 1960 Winter Olympics", "Squaw", ["Bear", "Aspen", "Vail"]),
 ("The Peak District valley of Castleton and the Blue John caverns", "Hope", ["Edale", "Derwent", "Dove"]), ("Jacqueline Susann's 1966 bestseller, 'Valley of the ...'", "Dolls", ["Diamonds", "Angels", "Lovers"]),
 ("The Pakistani valley where Malala Yousafzai grew up", "Swat", ["Kashmir", "Hunza", "Chitral"]), ("The Lancashire valley around Clitheroe", "Ribble", ["Lune", "Calder", "Rossendale"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-72.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
