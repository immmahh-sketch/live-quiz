# Bank session 10 Oct 2026: 2 more general races -> bank/race-67.json. 20 rows each, target 10; wrong options are
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

race("which famous 'Island'?", "General knowledge", "medium", ["islands", "wordplay"], [
 ("Robert Louis Stevenson's pirate novel", "Treasure", ["Coral", "Mysterious", "Pirate"]), ("ITV's dating show in a Majorcan villa", "Love", ["Temptation", "Paradise", "Heart"]),
 ("The Radio 4 show where guests choose eight records", "Desert", ["Castaway", "Lonely", "Tropical"]), ("New York's seaside funfair with the Cyclone roller coaster", "Coney", ["Staten", "Roosevelt", "Governors"]),
 ("Where millions of immigrants to America were processed", "Ellis", ["Liberty", "Governors", "Staten"]), ("Where Nelson Mandela was imprisoned for 18 years", "Robben", ["Seal", "Penguin", "Dassen"]),
 ("The Pacific island of the giant moai statues", "Easter", ["Pitcairn", "Norfolk", "Bounty"]), ("Lindisfarne's other name", "Holy", ["Farne", "Sacred", "Blessed"]),
 ("The Dorset island of the very first Scout camp", "Brownsea", ["Portland", "Purbeck", "Lundy"]), ("Where the Stone Roses played their 1990 gig in Widnes", "Spike", ["Hilbre", "Salt", "Mersey"]),
 ("The 1970s TV show with Mr Roarke and Tattoo", "Fantasy", ["Paradise", "Dream", "Magic"]), ("The sitcom castaways with the Skipper and the Professor", "Gilligan's", ["Robinson's", "Crusoe's", "McHale's"]),
 ("Scorsese's asylum thriller starring Leonardo DiCaprio", "Shutter", ["Shadow", "Hidden", "Ghost"]), ("King Kong's home", "Skull", ["Monster", "Dinosaur", "Bone"]),
 ("The New York island where you'll find the Hamptons", "Long", ["Staten", "Roosevelt", "Fire"]), ("America's smallest state", "Rhode", ["Block", "Staten", "Fire"]),
 ("Anne of Green Gables' Canadian home", "Prince Edward", ["Vancouver", "Cape Breton", "Baffin"]), ("The Essex island town that gave us Dr Feelgood", "Canvey", ["Mersea", "Foulness", "Hayling"]),
 ("The puffin island just off Amble in Northumberland", "Coquet", ["Farne", "St Mary's", "Lundy"]), ("The Australian island in the Indian Ocean famous for its red crab migration", "Christmas", ["Cocos", "Norfolk", "Lord Howe"])])

race("which famous 'Square'?", "General knowledge", "medium", ["squares", "wordplay"], [
 ("Nelson's Column stands in it", "Trafalgar", ["Waterloo", "Nile", "Copenhagen"]), ("Where the ball drops at New Year in New York", "Times", ["Herald", "Union", "Columbus"]),
 ("Moscow's square beside the Kremlin and St Basil's", "Red", ["Pushkin", "Lubyanka", "Manezh"]), ("Beijing's square of the 1989 protests", "Tiananmen", ["Zhongshan", "Renmin", "Wangfujing"]),
 ("London's square of glitzy film premieres", "Leicester", ["Soho", "Grosvenor", "Hanover"]), ("Where a nightingale sang in the 1940 song", "Berkeley", ["Grosvenor", "Hanover", "Belgrave"]),
 ("The Chelsea square that gave 'Rangers' their name", "Sloane", ["Cadogan", "Belgrave", "Eaton"]), ("Where crowds gather for the Pope's Easter blessing", "St Peter's", ["St Paul's", "St John's", "St Francis'"]),
 ("Venice's square with the great basilica and the pigeons", "St Mark's", ["St Luke's", "St Anthony's", "St Paul's"]), ("Cairo's square at the heart of the 2011 revolution", "Tahrir", ["Ramses", "Opera", "Azhar"]),
 ("Prague's square of the 1989 Velvet Revolution", "Wenceslas", ["Old Town", "Charles", "Republic"]), ("Walford's square in EastEnders", "Albert", ["Victoria", "Coronation", "Edward"]),
 ("Glasgow's main square, with the City Chambers", "George", ["Buchanan", "Blythswood", "Royal Exchange"]), ("The New York 'Garden' where the Knicks play", "Madison", ["Lincoln", "Columbus", "Herald"]),
 ("The Edinburgh New Town square that hosts the Book Festival", "Charlotte", ["St Andrew", "Rutland", "Moray"]), ("The Dublin Georgian square where Oscar Wilde grew up", "Merrion", ["Fitzwilliam", "Mountjoy", "Parnell"]),
 ("Amsterdam's square with the Royal Palace", "Dam", ["Museum", "Leidse", "Rembrandt"]), ("Henry James's novel, and the arch in Greenwich Village", "Washington", ["Gramercy", "Union", "Tompkins"]),
 ("Churchill's statue faces the Houses of Parliament across it", "Parliament", ["Westminster", "Smith", "Horse Guards"]), ("The Bloomsbury square whose Tube station is on the Piccadilly line", "Russell", ["Gordon", "Bedford", "Tavistock"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-67.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
