# Bank session 10 Oct 2026: 2 more general races -> bank/race-65.json. 20 rows each, target 10; wrong options are
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

race("which famous London street?", "London", "medium", ["streets", "London"], [
 ("Number 10, home of the Prime Minister", "Downing Street", ["Birdcage Walk", "Victoria Street", "Northumberland Avenue"]), ("Sherlock Holmes's address, at number 221B", "Baker Street", ["Gower Street", "Marylebone Road", "Wimpole Street"]),
 ("Once home to all of Britain's national newspapers", "Fleet Street", ["Strand", "Cheapside", "Lombard Street"]), ("Famous for its private doctors and clinics", "Harley Street", ["Great Portland Street", "Gower Street", "Euston Road"]),
 ("Soho's hub of Swinging Sixties mod fashion", "Carnaby Street", ["Wardour Street", "Berwick Street", "Old Compton Street"]), ("Where gentlemen go for a bespoke tailored suit", "Savile Row", ["Bond Street", "Mount Street", "Curzon Street"]),
 ("The Beatles' zebra crossing", "Abbey Road", ["Edgware Road", "Ladbroke Grove", "Euston Road"]), ("Home of the Bank of England, the 'Old Lady'", "Threadneedle Street", ["Lombard Street", "Cheapside", "Moorgate"]),
 ("'Tin Pan Alley', lined with guitar shops", "Denmark Street", ["Wardour Street", "Berwick Street", "Dean Street"]), ("Theatreland's avenue with the Lyric, Apollo and Gielgud", "Shaftesbury Avenue", ["Northumberland Avenue", "Charing Cross Road", "Kingsway"]),
 ("Notting Hill's antiques market", "Portobello Road", ["Ladbroke Grove", "Westbourne Grove", "Notting Hill Gate"]), ("The East End street famous for its curry houses", "Brick Lane", ["Columbia Road", "Petticoat Lane", "Commercial Street"]),
 ("Shirtmakers such as Turnbull & Asser", "Jermyn Street", ["Bond Street", "Sloane Street", "Mount Street"]), ("Brixton's street in Eddy Grant's 1983 hit", "Electric Avenue", ["Coldharbour Lane", "Acre Lane", "Atlantic Road"]),
 ("Chelsea street where punk was born in Vivienne Westwood's shop", "King's Road", ["Fulham Road", "Sloane Street", "Brompton Road"]), ("The Cenotaph stands in the middle of it", "Whitehall", ["Birdcage Walk", "Victoria Street", "Northumberland Avenue"]),
 ("The grand hotel road along Hyde Park, a dark blue Monopoly square", "Park Lane", ["Bayswater Road", "Curzon Street", "Piccadilly"]), ("Selfridges stands on it", "Oxford Street", ["Regent Street", "Bond Street", "Piccadilly"]),
 ("Gentlemen's clubs, and named after a game like croquet", "Pall Mall", ["Haymarket", "Piccadilly", "Regent Street"]), ("The red road from Admiralty Arch to Buckingham Palace", "The Mall", ["Birdcage Walk", "Constitution Hill", "Horse Guards Road"])])

race("which famous 'Gate'?", "General knowledge", "medium", ["gates", "wordplay"], [
 ("The 1970s scandal that brought down Richard Nixon", "Watergate", ["Whitewater", "Irangate", "Teapot Dome"]), ("Berlin's landmark with a four-horse chariot on top", "Brandenburg Gate", ["Siegestor", "Holstentor", "Arc de Triomphe"]),
 ("Prisoners came into the Tower of London by boat through it", "Traitors' Gate", ["Byward Tower", "Bloody Tower", "Lion Gate"]), ("The memorial at Ypres where the Last Post sounds every night", "Menin Gate", ["Thiepval Memorial", "Tyne Cot", "Cloth Hall"]),
 ("Delhi's great war memorial arch", "India Gate", ["Gateway of India", "Red Fort", "Qutub Minar"]), ("London's famous fish market", "Billingsgate", ["Smithfield", "Spitalfields", "Leadenhall"]),
 ("The North London cemetery where Karl Marx is buried", "Highgate", ["Kensal Green", "Brompton", "Nunhead"]), ("The Downing Street lockdown parties scandal", "Partygate", ["Plebgate", "Pastygate", "Cash for Honours"]),
 ("Microsoft's co-founder", "Bill Gates", ["Paul Allen", "Steve Ballmer", "Satya Nadella"]), ("The Yorkshire spa town with the Stray and Bettys tea rooms", "Harrogate", ["Ripon", "Knaresborough", "Ilkley"]),
 ("The Kent resort with Dreamland and the Turner Contemporary", "Margate", ["Ramsgate", "Broadstairs", "Herne Bay"]), ("The notorious prison where the Old Bailey now stands", "Newgate", ["Fleet", "Marshalsea", "Clink"]),
 ("The hill that climbs up to St Paul's Cathedral", "Ludgate Hill", ["Cornhill", "Fish Street Hill", "Tower Hill"]), ("Sci-fi film and series about an ancient ring that opens wormholes", "Stargate", ["Farscape", "Babylon 5", "Event Horizon"]),
 ("Scene of the Tube's worst peacetime crash, in 1975", "Moorgate", ["Aldgate", "King's Cross", "Ladbroke Grove"]), ("San Francisco's red suspension bridge", "Golden Gate Bridge", ["Bay Bridge", "Brooklyn Bridge", "Verrazzano Bridge"]),
 ("The roofed gateway into a churchyard", "Lychgate", ["Portcullis", "Lintel", "Cloister"]), ("The Tyneside town at the other end of the Millennium Bridge", "Gateshead", ["Jarrow", "Wallsend", "Hebburn"]),
 ("The Surrey town below the North Downs, near Redhill", "Reigate", ["Dorking", "Guildford", "Leatherhead"]), ("An American party held at the back of a car before the game", "Tailgate", ["Potluck", "Hoedown", "Clambake"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-65.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
