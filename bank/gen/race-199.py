# Bank session 11 Oct 2026: 3 more general races -> bank/race-199.json (Pancake Day, Remembrance and Wimbledon words). 20 rows each, target 10; wrong options are
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

race("what's this Pancake Day word?", "Food and drink", "easy", ["Pancake Day", "Shrove Tuesday", "words"], [
 ("The proper name for Pancake Day", "Shrove Tuesday", ["Maundy Thursday", "Good Friday", "Plough Monday"]),
 ("The day after, when Lent begins", "Ash Wednesday", ["Maundy Thursday", "Palm Sunday", "Holy Saturday"]),
 ("The forty days of giving things up", "Lent", ["Advent", "Ramadan", "Passover"]),
 ("Flour, eggs and milk whisked together", "Batter", ["Dough", "Pastry", "Butter"]),
 ("Turning it over in mid-air with the pan", "Flipping", ["Flapping", "Flopping", "Slipping"]),
 ("The classic British topping", "Lemon and sugar", ["Salt and vinegar", "Fish and chips", "Bread and butter"]),
 ("The Buckinghamshire town with a pancake race since 1445", "Olney", ["Oakham", "Ludlow", "Ely"]),
 ("What you cook it in", "Frying pan", ["Saucepan", "Dustpan", "Peter Pan"]),
 ("A thin French pancake", "Crêpe", ["Crumpet", "Croissant", "Brioche"]),
 ("French for 'Fat Tuesday'", "Mardi Gras", ["Carnaval", "Fiesta", "Mamma Mia"]),
 ("The Canadian topping poured over stacks", "Maple syrup", ["Golden syrup", "Cough syrup", "Treacle"]),
 ("Small thick pancakes also called drop scones", "Scotch pancakes", ["Scotch eggs", "Scotch broth", "Hopscotch"]),
 ("Running while flipping one in a pan", "Pancake race", ["Egg and spoon race", "Sack race", "Rat race"]),
 ("The hazelnut chocolate spread everyone reaches for", "Nutella", ["Marmite", "Lurpak", "Bovril"]),
 ("A tall pile of American pancakes", "Stack", ["Stake", "Snack", "Stash"]),
 ("A savoury Breton buckwheat pancake", "Galette", ["Gazette", "Gavotte", "Galleon"]),
 ("Small Russian pancakes served with caviar", "Blini", ["Bellini", "Bikini", "Linguini"]),
 ("A crispy South Indian rice-and-lentil pancake", "Dosa", ["Samosa", "Doha", "Dosh"]),
 ("Confessing your sins, which gave the day its name", "Shriving", ["Shaving", "Thriving", "Striving"]),
 ("Used up before Lent, along with the milk and fat", "Eggs", ["Apples", "Potatoes", "Biscuits"])])

race("what's this Remembrance word?", "History", "medium", ["Remembrance", "war", "words"], [
 ("The red flower worn in November", "Poppy", ["Rose", "Carnation", "Tulip"]),
 ("The memorial on Whitehall", "Cenotaph", ["Epitaph", "Autograph", "Monument"]),
 ("Kept at eleven o'clock", "Two-minute silence", ["Minute's applause", "Moment of madness", "Silent night"]),
 ("The bugle call played at the ceremony", "Last Post", ["First Post", "Post Office", "Goalpost"]),
 ("The 1918 agreement that ended the fighting", "Armistice", ["Amnesty", "Ambush", "Annexation"]),
 ("Armistice Day's date", "11 November", ["5 November", "30 November", "11 September"]),
 ("A ring of poppies laid at a memorial", "Wreath", ["Bouquet", "Corsage", "Rosette"]),
 ("The charity behind the Poppy Appeal", "Royal British Legion", ["RSPCA", "Royal Mail", "Foreign Legion"]),
 ("The nameless soldier buried in Westminster Abbey", "Unknown Warrior", ["Lone Ranger", "Unsung Hero", "Iron Duke"]),
 ("John McCrae's poem about poppies", "In Flanders Fields", ["In the Bleak Midwinter", "Strawberry Fields", "Fields of Athenry"]),
 ("The last line of the Exhortation", "We will remember them", ["We'll meet again", "Keep calm and carry on", "Never surrender"]),
 ("The memorial at Ypres where the Last Post sounds every night", "Menin Gate", ["Menai Bridge", "Golden Gate", "Watergate"]),
 ("The Sunday each November when the nation marks its war dead", "Remembrance Sunday", ["Mothering Sunday", "Palm Sunday", "Super Sunday"]),
 ("Someone who has served in the forces", "Veteran", ["Veterinarian", "Volunteer", "Vegetarian"]),
 ("Worn as a symbol of peace", "White poppy", ["White rose", "White feather", "White flag"]),
 ("Remembers the animals lost in war", "Purple poppy", ["Purple Heart", "Purple patch", "Purple Rain"]),
 ("The 1916 battle with 57,000 British casualties on its first day", "The Somme", ["Waterloo", "Hastings", "Agincourt"]),
 ("The body that cares for the white headstones", "Commonwealth War Graves Commission", ["Charity Commission", "Forestry Commission", "Electoral Commission"]),
 ("The musician who plays the Last Post", "Bugler", ["Piper", "Drummer", "Fiddler"]),
 ("The reading that begins 'They shall grow not old'", "Exhortation", ["Exhalation", "Exaltation", "Extortion"])])

race("what's this Wimbledon word?", "Sport", "medium", ["Wimbledon", "tennis", "words"], [
 ("The famous dish eaten at the Championships", "Strawberries and cream", ["Fish and chips", "Scones and jam", "Pie and mash"]),
 ("The main show court, with a retractable roof", "Centre Court", ["Food court", "Royal Court", "Supreme Court"]),
 ("The grassy slope where fans watch on a big screen", "Henman Hill", ["Primrose Hill", "Notting Hill", "Box Hill"]),
 ("The players' dress code", "All white", ["All black", "Black tie", "Blue and white"]),
 ("Where VIP guests sit on Centre Court", "Royal Box", ["Royal Mint", "Royal Mail", "Box office"]),
 ("Wimbledon's postcode", "SW19", ["NE1", "SE1", "W1"]),
 ("The line of fans camping out for tickets", "The Queue", ["The Crowd", "The Mob", "The Rush"]),
 ("The fruity gin drink sipped on the lawns", "Pimm's", ["Baileys", "Guinness", "Sherry"]),
 ("The Harris hawk that scares off the pigeons", "Rufus", ["Rupert", "Rocky", "Roger"]),
 ("Teenagers who fetch the balls", "Ball boys and girls", ["Line judges", "Caddies", "Stewards"]),
 ("The trophy for the women's singles champion", "Venus Rosewater Dish", ["Claret Jug", "Webb Ellis Cup", "Calcutta Cup"]),
 ("The surface it's played on", "Grass", ["Clay", "Hard court", "Carpet"]),
 ("The club that hosts it", "All England Club", ["Queen's Club", "MCC", "Hurlingham Club"]),
 ("The traditional rest day, since scrapped", "Middle Sunday", ["Super Sunday", "Palm Sunday", "Lazy Sunday"]),
 ("How long the Championships last", "Fortnight", ["Weekend", "Month", "Ten days"]),
 ("What the umpire says to hush the crowd", "Quiet, please", ["Shush now", "Silence in court", "Order, order"]),
 ("Rolled over the grass when it rains", "Covers", ["Duvets", "Blankets", "Sheets"]),
 ("The first British man to win the singles since 1936", "Andy Murray", ["Tim Henman", "Greg Rusedski", "Jack Draper"]),
 ("The 1936 champion with a statue at the club", "Fred Perry", ["Fred Dibnah", "Fred Flintstone", "Fred Trueman"]),
 ("The last British woman to win the singles, in 1977", "Virginia Wade", ["Sue Barker", "Emma Raducanu", "Annabel Croft"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-199.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
