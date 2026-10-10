# Bank session 10 Oct 2026: 2 more general races -> bank/race-88.json. 20 rows each, target 10; wrong options are
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

race("which famous 'Wind'?", "General knowledge", "medium", ["wind", "wordplay"], [
 ("Margaret Mitchell's Civil War epic", "Gone with the Wind", ["Rebecca", "Jezebel", "The Good Earth"]), ("Elton John's tribute to Marilyn Monroe, later to Diana", "Candle in the Wind", ["Your Song", "Rocket Man", "Tiny Dancer"]),
 ("Kenneth Grahame's riverbank tale", "The Wind in the Willows", ["Tarka the Otter", "Black Beauty", "The Jungle Book"]), ("Scorpions' 1990 anthem about the end of the Cold War", "Wind of Change", ["Rock You Like a Hurricane", "Still Loving You", "Send Me an Angel"]),
 ("Bob Dylan's 1963 protest song", "Blowin' in the Wind", ["The Times They Are a-Changin'", "Masters of War", "A Hard Rain's a-Gonna Fall"]), ("The ship that brought Caribbean migrants to Tilbury in 1948", "Empire Windrush", ["Queen Mary", "Canberra", "Mayflower"]),
 ("The Cumbrian nuclear site of the 1957 fire, now Sellafield", "Windscale", ["Dounreay", "Calder Hall", "Hinkley Point"]), ("Chicago's nickname", "The Windy City", ["The Big Apple", "The Big Easy", "Motor City"]),
 ("The Soho theatre that 'never closed' through the Blitz", "Windmill Theatre", ["London Palladium", "Raymond Revuebar", "Players' Theatre"]), ("The Caribbean island chain that includes Dominica and St Lucia", "Windward Islands", ["Leeward Islands", "Virgin Islands", "Cayman Islands"]),
 ("The steady winds sailing ships used to cross oceans", "Trade winds", ["Doldrums", "Jet stream", "Sirocco"]), ("An unexpected sum of money", "Windfall", ["Overdraft", "Shortfall", "Pay cut"]),
 ("Someone who never stops talking", "Windbag", ["Wallflower", "Shrinking violet", "Dark horse"]), ("A sudden burst of fresh energy", "Second wind", ["Second fiddle", "Second nature", "Second sight"]),
 ("Bette Midler's song from Beaches", "Wind Beneath My Wings", ["The Rose", "From a Distance", "Boogie Woogie Bugle Boy"]), ("Microsoft's operating system", "Windows", ["macOS", "Linux", "Android"]),
 ("Riding a board with a sail", "Windsurfing", ["Kitesurfing", "Paddleboarding", "Wakeboarding"]), ("Ken Loach's 2006 Palme d'Or winner about Irish independence", "The Wind That Shakes the Barley", ["Kes", "I, Daniel Blake", "Sweet Sixteen"]),
 ("The striped barrier you put up on the beach", "Windbreak", ["Beach hut", "Parasol", "Deckchair"]), ("A tease designed to get a rise out of someone", "Wind-up", ["Pick-up", "Knock-off", "Mix-up"])])

race("which famous 'Storm'?", "General knowledge", "medium", ["storms", "wordplay"], [
 ("The US-led attack on Iraq in 1991", "Operation Desert Storm", ["Operation Desert Shield", "Operation Iraqi Freedom", "Operation Desert Fox"]), ("A big fuss about nothing", "Storm in a teacup", ["Damp squib", "Red herring", "Wild goose chase"]),
 ("Throwing ideas around in a meeting", "Brainstorm", ["Mind map", "Blue-sky thinking", "Think tank"]), ("The grime star who headlined Glastonbury in 2019", "Stormzy", ["Skepta", "Dave", "Kano"]),
 ("The 2021 storm that left thousands in the North East without power", "Storm Arwen", ["Storm Desmond", "Storm Ciara", "Storm Eunice"]), ("George Clooney's 2000 film about a doomed fishing boat", "The Perfect Storm", ["Poseidon", "The Finest Hours", "Captain Phillips"]),
 ("Northern Ireland's parliament building", "Stormont", ["Holyrood", "Senedd", "Hillsborough"]), ("The Empire's white-armoured soldiers", "Stormtroopers", ["Clone troopers", "Sith", "Jawas"]),
 ("Anthony Horowitz's first Alex Rider book", "Stormbreaker", ["Point Blanc", "Skeleton Key", "Eagle Strike"]), ("Halle Berry's weather-controlling X-Man", "Storm", ["Rogue", "Jean Grey", "Mystique"]),
 ("Lena Horne's signature song", "Stormy Weather", ["Cry Me a River", "Summertime", "Blue Skies"]), ("The Doors' 1971 song with the sound of falling rain", "Riders on the Storm", ["Light My Fire", "Break On Through", "L.A. Woman"]),
 ("Bob Dylan's song from Blood on the Tracks", "Shelter from the Storm", ["Tangled Up in Blue", "Simple Twist of Fate", "Idiot Wind"]), ("The quiet spell before trouble breaks", "The calm before the storm", ["Silence is golden", "All quiet on the Western Front", "Still waters run deep"]),
 ("Darude's 1999 trance anthem", "Sandstorm", ["Children", "Better Off Alone", "Blue"]), ("A fire so fierce it makes its own winds, like Dresden in 1945", "Firestorm", ["Wildfire", "Inferno", "Blitz"]),
 ("The moment the French Revolution began, in July 1789", "The Storming of the Bastille", ["The Siege of Paris", "The Tennis Court Oath", "The Reign of Terror"]), ("Thrill-seekers who drive towards tornadoes", "Storm chasers", ["Hurricane hunters", "Weather watchers", "Twisters"]),
 ("A stunt pilot touring country fairs", "Barnstormer", ["Wing walker", "Daredevil", "Stuntman"]), ("The British cruise missile sent to Ukraine, also a G.I. Joe ninja", "Storm Shadow", ["Snake Eyes", "Brimstone", "Tomahawk"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-88.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
