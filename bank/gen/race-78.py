# Bank session 10 Oct 2026: 2 more general races -> bank/race-78.json. 20 rows each, target 10; wrong options are
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

race("which famous 'Eye'?", "General knowledge", "medium", ["eyes", "wordplay"], [
 ("The giant observation wheel on the South Bank", "London Eye", ["Thames Wheel", "Capital Wheel", "Big Wheel"]), ("The satirical magazine edited by Ian Hislop", "Private Eye", ["Punch", "The Spectator", "The Oldie"]),
 ("Survivor's anthem from Rocky III", "Eye of the Tiger", ["Burning Heart", "Gonna Fly Now", "Hearts on Fire"]), ("Jim Bowen's darts game show", "Bullseye", ["Double Top", "Treble Top", "Arrows"]),
 ("An overnight flight that leaves you shattered", "Red-eye", ["Night owl", "Moonlighter", "Graveyard"]), ("Pierce Brosnan's first Bond film", "GoldenEye", ["Tomorrow Never Dies", "The World Is Not Enough", "Die Another Day"]),
 ("Ken Follett's Second World War spy thriller", "Eye of the Needle", ["The Pillars of the Earth", "The Key to Rebecca", "Night over Water"]), ("Percy Shaw's road studs, invented in Halifax", "Cat's eyes", ["Bollards", "Rumble strips", "Belisha beacons"]),
 ("Jeremy Renner's archer Avenger", "Hawkeye", ["Green Arrow", "Falcon", "Black Widow"]), ("The flaming watcher on top of Barad-dûr", "Eye of Sauron", ["Palantír", "Witch-king", "Balrog"]),
 ("The ancient Egyptian symbol of protection", "Eye of Horus", ["Ankh", "Scarab", "Djed"]), ("Van Morrison's 1967 hit", "Brown Eyed Girl", ["Gloria", "Moondance", "Have I Told You Lately"]),
 ("Kim Carnes's 1981 hit", "Bette Davis Eyes", ["Hungry Eyes", "Angel Eyes", "Pretty Eyes"]), ("The Eagles' 1975 hit about a cheating wife", "Lyin' Eyes", ["Hotel California", "Take It Easy", "Desperado"]),
 ("The calm centre of a hurricane", "Eye of the storm", ["Heart of the storm", "Calm", "Doldrums"]), ("Stanley Kubrick's final film", "Eyes Wide Shut", ["A Clockwork Orange", "Full Metal Jacket", "Barry Lyndon"]),
 ("The mystic spot in the middle of the forehead", "Third eye", ["Crown chakra", "Sixth sense", "Halo"]), ("A bruise from a punch in the face", "Black eye", ["Fat lip", "Thick ear", "Cauliflower ear"]),
 ("Iago's name for jealousy in Othello", "The green-eyed monster", ["The red-eyed devil", "The yellow peril", "The blue-eyed boy"]), ("The eye above the pyramid on a dollar bill", "Eye of Providence", ["Great Seal", "Masonic Square", "Pyramid"])])

race("which famous 'Dog'?", "General knowledge", "medium", ["dogs", "wordplay"], [
 ("Quentin Tarantino's 1992 debut film", "Reservoir Dogs", ["Pulp Fiction", "Jackie Brown", "True Romance"]), ("The East London peninsula with Canary Wharf", "Isle of Dogs", ["Rotherhithe", "Wapping", "Surrey Quays"]),
 ("The BBC's long-running consumer rights show", "Watchdog", ["Rogue Traders", "Crimewatch", "That's Life!"]), ("The team nobody expects to win", "Underdog", ["Also-ran", "Wooden spoon", "Has-been"]),
 ("Elvis's 1956 hit, first sung by Big Mama Thornton", "Hound Dog", ["Heartbreak Hotel", "Blue Suede Shoes", "Don't Be Cruel"]), ("The Baha Men's 2000 hit", "Who Let the Dogs Out", ["Macarena", "Mambo No. 5", "Barbie Girl"]),
 ("Churchill's name for his depression, and a Led Zeppelin song", "Black Dog", ["Black Cloud", "Grey Wolf", "Dark Horse"]), ("Noël Coward: '... and Englishmen go out in the midday sun'", "Mad dogs", ["Wild dogs", "Old dogs", "Hot dogs"]),
 ("The hangover cure: the hair of the ...", "Dog", ["Cat", "Horse", "Hound"]), ("Al Pacino's 1975 bank-robbery film", "Dog Day Afternoon", ["Serpico", "Scarface", "Heat"]),
 ("The North Sea sandbank and Shipping Forecast area", "Dogger", ["Fisher", "Forties", "Viking"]), ("A sausage in a bun", "Hot dog", ["Bratwurst", "Saveloy", "Chipolata"]),
 ("A battered sausage on a stick, sold at American fairs", "Corn dog", ["Pigs in blankets", "Toad in the hole", "Scotch egg"]), ("A salty old sailor", "Sea dog", ["Landlubber", "Sea horse", "Sea lion"]),
 ("Churchill as the symbol of British grit", "British Bulldog", ["British Lion", "John Bull", "Iron Duke"]), ("The 1980s Spanish cartoon dog musketeer", "Dogtanian", ["Willy Fog", "Ulysses 31", "Jamie"]),
 ("Someone who does all the boring jobs", "Dogsbody", ["Busybody", "Everybody", "Nobody"]), ("A long, rambling joke with a pointless punchline", "Shaggy dog story", ["Cock and bull story", "Tall tale", "Fish story"]),
 ("The rapper behind 'Drop It Like It's Hot'", "Snoop Dogg", ["Nate Dogg", "Dr. Dre", "Warren G"]), ("Kevin Smith's 1999 film with Ben Affleck and Matt Damon as fallen angels", "Dogma", ["Clerks", "Mallrats", "Chasing Amy"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-78.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
