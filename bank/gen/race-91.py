# Bank session 10 Oct 2026: 2 more general races -> bank/race-91.json. 20 rows each, target 10; wrong options are
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

race("which famous 'Glass'?", "General knowledge", "medium", ["glass", "wordplay"], [
 ("Rian Johnson's 2022 Knives Out sequel", "Glass Onion", ["Wake Up Dead Man", "Knives Out", "Death on the Nile"]), ("The invisible barrier that stops women reaching the top", "Glass ceiling", ["Glass cliff", "Brick wall", "Iron curtain"]),
 ("The Oxford band behind 'Heat Waves'", "Glass Animals", ["Foals", "Alt-J", "Radiohead"]), ("What Cinderella leaves on the palace steps", "Glass slipper", ["Ruby slipper", "Silver shoe", "Golden sandal"]),
 ("Gateshead's music venue on the Tyne, renamed in 2022", "The Glasshouse", ["Baltic", "The Biscuit Factory", "The Tyne Theatre"]), ("Lewis Carroll's 1871 sequel to Alice", "Through the Looking-Glass", ["The Hunting of the Snark", "Sylvie and Bruno", "Alice's Adventures Under Ground"]),
 ("The coloured windows of a cathedral", "Stained glass", ["Frosted glass", "Cut glass", "Crown glass"]), ("The American composer of Einstein on the Beach", "Philip Glass", ["Steve Reich", "John Adams", "Terry Riley"]),
 ("How an optimist sees the glass", "Half full", ["Half empty", "Overflowing", "Topped up"]), ("What a boxer who's easily knocked out is said to have", "Glass jaw", ["Cauliflower ear", "Iron fist", "Weak spot"]),
 ("Tennessee Williams's 1944 play about Laura and her ornaments", "The Glass Menagerie", ["A Streetcar Named Desire", "Cat on a Hot Tin Roof", "Sweet Bird of Youth"]), ("David Bowie's 1987 world tour", "Glass Spider", ["Serious Moonlight", "Sound + Vision", "Ziggy Stardust"]),
 ("M. Night Shyamalan's 2019 follow-up to Unbreakable and Split", "Glass", ["Old", "Signs", "The Village"]), ("Shaping molten glass by blowing down a pipe", "Glassblowing", ["Glazing", "Pottery", "Smelting"]),
 ("Sunderland's museum of glassmaking by the Wear", "National Glass Centre", ["Winter Gardens", "Beamish", "Baltic"]), ("Dashiell Hammett's 1931 crime novel", "The Glass Key", ["The Maltese Falcon", "The Thin Man", "Red Harvest"]),
 ("Sherlock Holmes's tool for studying clues", "Magnifying glass", ["Deerstalker", "Pipe", "Violin"]), ("A small glass for a quick slug of spirits", "Shot glass", ["Tumbler", "Snifter", "Highball"]),
 ("Billy Joel's 1980 album", "Glass Houses", ["The Stranger", "52nd Street", "An Innocent Man"]), ("The famous glass made on an island near Venice", "Murano glass", ["Waterford crystal", "Bohemian glass", "Pyrex"])])

race("which famous 'Steel'?", "General knowledge", "medium", ["steel", "wordplay"], [
 ("Superman's 2013 film", "Man of Steel", ["Superman Returns", "Batman v Superman", "Justice League"]), ("The 1989 film with Julia Roberts and Dolly Parton", "Steel Magnolias", ["Pretty Woman", "9 to 5", "Mystic Pizza"]),
 ("The jazz-rock band of Walter Becker and Donald Fagen", "Steely Dan", ["Toto", "Chicago", "The Doobie Brothers"]), ("A Caribbean band playing tuned oil drums", "Steel band", ["Brass band", "Calypso band", "Ska band"]),
 ("The rust-proof metal used for cutlery", "Stainless steel", ["Pewter", "Chrome", "Silver plate"]), ("Pittsburgh's NFL team", "Pittsburgh Steelers", ["Pittsburgh Pirates", "Pittsburgh Penguins", "Cleveland Browns"]),
 ("Sheffield's nickname", "The Steel City", ["The Smoke", "The Granite City", "Cottonopolis"]), ("The romance novelist with over 190 books", "Danielle Steel", ["Jackie Collins", "Barbara Taylor Bradford", "Jilly Cooper"]),
 ("Britain's first rock'n'roll star, of 'Singing the Blues'", "Tommy Steele", ["Cliff Richard", "Billy Fury", "Marty Wilde"]), ("What you need to stay calm under pressure", "Nerves of steel", ["Stiff upper lip", "Thick skin", "Heart of gold"]),
 ("The Rolling Stones' 1989 album", "Steel Wheels", ["Voodoo Lounge", "Tattoo You", "Dirty Work"]), ("Hugh Jackman's robot-boxing film", "Real Steel", ["Chappie", "Pacific Rim", "Logan"]),
 ("The Teesside town whose giant blast furnace went cold in 2015", "Redcar", ["Scunthorpe", "Port Talbot", "Middlesbrough"]), ("The County Durham town whose steelworks closed in 1980", "Consett", ["Stanley", "Spennymoor", "Shotton"]),
 ("The glam metal spoof band of 'Death to All but Metal'", "Steel Panther", ["Spinal Tap", "Tenacious D", "Steel Dragon"]), ("The guitar played flat on the lap in country music", "Steel guitar", ["Dobro", "Banjo", "Mandolin"]),
 ("What safety boots have in the front", "Steel toecaps", ["Hobnails", "Rubber soles", "Leather welts"]), ("The comedian behind Mark ... 's in Town", "Mark Steel", ["Mark Thomas", "Mark Watson", "Jeremy Hardy"]),
 ("The Birmingham reggae band of 'Handsworth Revolution'", "Steel Pulse", ["Aswad", "UB40", "Musical Youth"]), ("Coarsely chopped oats for a chewy porridge", "Steel-cut oats", ["Rolled oats", "Bran flakes", "Muesli"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-91.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
