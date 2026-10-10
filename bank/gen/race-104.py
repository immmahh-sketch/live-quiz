# Bank session 10 Oct 2026: 2 more general races -> bank/race-104.json (brand mascots, fictional companies). 20 rows each, target 10; wrong options are
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

race("which brand's mascot is this?", "Brands", "easy", ["brands", "adverts", "mascots"], [
 ("Tony the Tiger", "Frosties", ["Corn Flakes", "Shreddies", "Weetabix"]),
 ("Snap, Crackle and Pop", "Rice Krispies", ["Cheerios", "Ready Brek", "Golden Nuggets"]),
 ("The Honey Monster", "Sugar Puffs", ["Golden Nuggets", "Cheerios", "Crunchy Nut"]),
 ("Coco the Monkey", "Coco Pops", ["Weetabix", "Cheerios", "Ready Brek"]),
 ("Bibendum, the man made of tyres", "Michelin", ["Goodyear", "Dunlop", "Pirelli"]),
 ("The Colonel", "KFC", ["Burger King", "Wimpy", "Pizza Hut"]),
 ("Ronald, a clown", "McDonald's", ["Burger King", "Wimpy", "Domino's"]),
 ("A nodding bulldog who says 'Oh yes!'", "Churchill", ["Direct Line", "Aviva", "Admiral"]),
 ("Aleksandr Orlov the meerkat", "Compare the Market", ["GoCompare", "MoneySupermarket", "Confused.com"]),
 ("A Labrador puppy running off with the loo roll", "Andrex", ["Cushelle", "Charmin", "Velvet"]),
 ("A jolly green giant going 'Ho ho ho'", "Green Giant", ["Del Monte", "Princes", "Heinz"]),
 ("A bearded sea captain", "Birds Eye", ["Young's", "Findus", "Ross"]),
 ("Chimps having a tea party", "PG Tips", ["Typhoo", "Yorkshire Tea", "Twinings"]),
 ("The Tea Folk", "Tetley", ["Typhoo", "Yorkshire Tea", "Twinings"]),
 ("Laughing tin robots from Mars", "Smash", ["Bisto", "Oxo", "Pot Noodle"]),
 ("Bertie, a man made of sweets", "Bassett's Liquorice Allsorts", ["Haribo", "Rowntree's", "Trebor"]),
 ("A cowboy kid in round glasses", "Milkybar", ["Yorkie", "Milky Way", "Galaxy"]),
 ("A giggling doughboy", "Pillsbury", ["Jus-Rol", "Greggs", "Warburtons"]),
 ("A pink drumming bunny in the UK ads", "Duracell", ["Ever Ready", "Panasonic", "Varta"]),
 ("An Old English Sheepdog", "Dulux", ["Crown", "Johnstone's", "Farrow & Ball"])])

race("which film or show features this fictional company?", "Film", "medium", ["films", "TV", "fictional companies"], [
 ("Acme Corporation", "Looney Tunes", ["Tom and Jerry", "The Pink Panther", "Wacky Races"]),
 ("Cyberdyne Systems", "The Terminator", ["The Matrix", "Total Recall", "Predator"]),
 ("Weyland-Yutani", "Alien", ["Predator", "Event Horizon", "The Thing"]),
 ("The Umbrella Corporation", "Resident Evil", ["Silent Hill", "28 Days Later", "The Walking Dead"]),
 ("Wernham Hogg paper merchants", "The Office", ["Peep Show", "The IT Crowd", "W1A"]),
 ("Initech", "Office Space", ["Horrible Bosses", "The Internship", "9 to 5"]),
 ("Los Pollos Hermanos", "Breaking Bad", ["Ozark", "Narcos", "Weeds"]),
 ("Sterling Cooper", "Mad Men", ["Suits", "Billions", "The West Wing"]),
 ("Wayne Enterprises", "Batman", ["Superman", "The Flash", "Green Lantern"]),
 ("Stark Industries", "Iron Man", ["Captain America", "Thor", "Ant-Man"]),
 ("Oscorp", "Spider-Man", ["Daredevil", "Fantastic Four", "Hulk"]),
 ("Buy n Large", "WALL-E", ["Up", "Toy Story", "Ratatouille"]),
 ("The Slate Rock and Gravel Company", "The Flintstones", ["The Jetsons", "Yogi Bear", "Top Cat"]),
 ("The Krusty Krab", "SpongeBob SquarePants", ["Rugrats", "Hey Arnold!", "The Fairly OddParents"]),
 ("Grace Brothers department store", "Are You Being Served?", ["Open All Hours", "The Brittas Empire", "Dad's Army"]),
 ("The Bluth Company", "Arrested Development", ["Schitt's Creek", "Veep", "Parks and Recreation"]),
 ("The Tyrell Corporation", "Blade Runner", ["Total Recall", "The Matrix", "Minority Report"]),
 ("OCP (Omni Consumer Products)", "RoboCop", ["Total Recall", "Judge Dredd", "Demolition Man"]),
 ("InGen", "Jurassic Park", ["King Kong", "Godzilla", "Westworld"]),
 ("Waystar Royco", "Succession", ["Billions", "Industry", "Dallas"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-104.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
