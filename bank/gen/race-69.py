# Bank session 10 Oct 2026: 2 more general races -> bank/race-69.json. 20 rows each, target 10; wrong options are
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

race("which famous '-wood'?", "General knowledge", "medium", ["wordplay", "who's who"], [
 ("California's film capital", "Hollywood", ["Inglewood", "Burbank", "Hollyoaks"]), ("Mumbai's Hindi-language film industry", "Bollywood", ["Tollywood", "Kollywood", "Mollywood"]),
 ("Nigeria's booming film industry", "Nollywood", ["Tollywood", "Kollywood", "Riverwood"]), ("Robin Hood's forest", "Sherwood", ["Epping", "Arden", "Savernake"]),
 ("The Essex town of The Only Way Is Essex", "Brentwood", ["Billericay", "Basildon", "Romford"]), ("The Lancashire port, and drummer Mick of the Mac", "Fleetwood", ["Blackpool", "Morecambe", "Heysham"]),
 ("Clint, the Man with No Name", "Eastwood", ["Easton", "Eastman", "Eastham"]), ("Vivienne, queen of punk fashion", "Westwood", ["Westfield", "Weston", "Westbrook"]),
 ("Margaret, author of The Handmaid's Tale", "Atwood", ["Attwell", "Atkins", "Atwell"]), ("Jonny, Radiohead's guitarist", "Greenwood", ["Greenfield", "Greenway", "Greenhalgh"]),
 ("Frank, the scheming politician in House of Cards", "Underwood", ["Underhill", "Underdown", "Underworld"]), ("Josiah, the Staffordshire potter", "Wedgwood", ["Spode", "Doulton", "Minton"]),
 ("The admiral who took over at Trafalgar, with a monument at Tynemouth", "Collingwood", ["Hardy", "Codrington", "Jervis"]), ("Matilda's awful family, and a London prison's 'Scrubs'", "Wormwood", ["Trunchbull", "Holloway", "Pentonville"]),
 ("The world's tallest trees", "Redwood", ["Douglas fir", "Mountain ash", "Kauri"]), ("Wood washed up on the beach, and a Travis hit", "Driftwood", ["Flotsam", "Jetsam", "Seawood"]),
 ("The fragrant Indian wood used in incense", "Sandalwood", ["Teak", "Mahogany", "Ebony"]), ("Thin layers of wood glued together", "Plywood", ["Chipboard", "Hardboard", "MDF"]),
 ("Crystal Palace stands in Upper ...", "Norwood", ["Sydenham", "Penge", "Anerley"]), ("Christopher, whose Berlin stories became Cabaret", "Isherwood", ["Auden", "Spender", "Waugh"])])

race("which famous 'Road'?", "General knowledge", "medium", ["roads", "wordplay"], [
 ("The cheapest square on the London Monopoly board", "Old Kent", ["Mile End", "Bow", "Lambeth"]), ("The other brown square on the London Monopoly board", "Whitechapel", ["Mile End", "Bow", "Lambeth"]),
 ("The ancient trade route from China to the Mediterranean", "Silk", ["Spice", "Amber", "Tea"]), ("Dorothy follows it to the Emerald City", "Yellow Brick", ["Golden Brick", "Red Brick", "Emerald"]),
 ("The Second World War supply route over the mountains into China", "Burma", ["Siam", "Hump", "Mandalay"]), ("Leeds United's ground", "Elland", ["Valley", "Bramall", "Oakwell"]),
 ("QPR's ground", "Loftus", ["Craven", "Griffin", "Upton"]), ("Norwich City's ground", "Carrow", ["Abbey", "Layer", "Kenilworth"]),
 ("Ipswich Town's ground", "Portman", ["Layer", "Abbey", "Kenilworth"]), ("Watford's ground", "Vicarage", ["Kenilworth", "Griffin", "Adams"]),
 ("Springsteen's song where 'the screen door slams, Mary's dress waves'", "Thunder", ["Lightning", "Rocky", "Dirt"]), ("The Beatles' last US number one, 'The ... Road'", "Long and Winding", ["Long and Dusty", "Lonely and Winding", "Long and Lonesome"]),
 ("John Denver's 'Take Me Home, ... Roads'", "Country", ["Mountain", "Western", "Valley"]), ("The London street of electronics shops, ending at Centre Point", "Tottenham Court", ["Euston", "Charing Cross", "Gray's Inn"]),
 ("The South Kensington road named after the Great Exhibition", "Exhibition", ["Cromwell", "Albert", "Prince Consort"]), ("Madame Tussauds stands on it", "Marylebone", ["Euston", "Edgware", "Great Portland"]),
 ("Tom Hanks's 2002 gangster film, 'Road to ...'", "Perdition", ["Redemption", "Salvation", "Damnation"]), ("Talking Heads' 1985 hit, 'Road to ...'", "Nowhere", ["Somewhere", "Paradise", "Ruin"]),
 ("Hope and Crosby's 1947 'Road to' film, set in Brazil", "Rio", ["Morocco", "Zanzibar", "Singapore"]), ("The old A1, from London to Edinburgh", "Great North", ["Great West", "Old North", "King's"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-69.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
