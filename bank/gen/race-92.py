# Bank session 10 Oct 2026: 2 more general races -> bank/race-92.json. 20 rows each, target 10; wrong options are
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

race("which famous 'Bear'?", "General knowledge", "medium", ["bears", "wordplay"], [
 ("The colourful cartoon bears with symbols on their tummies", "Care Bears", ["Gummi Bears", "Berenstain Bears", "Bananas in Pyjamas"]), ("Haribo's chewy jelly sweets", "Gummy bears", ["Jelly Babies", "Fruit Pastilles", "Wine Gums"]),
 ("The survival TV adventurer who became Chief Scout", "Bear Grylls", ["Ray Mears", "Ben Fogle", "Steve Backshall"]), ("Ursa Major's English name", "The Great Bear", ["The Plough", "Orion", "Cassiopeia"]),
 ("The tall fur hat of the Guards outside Buckingham Palace", "Bearskin", ["Busby", "Tricorn", "Shako"]), ("Michael Rosen's picture book, 'We're Going on a ...'", "Bear Hunt", ["Lion Hunt", "Picnic", "Adventure"]),
 ("The TV series about a Chicago sandwich shop kitchen", "The Bear", ["The Kitchen", "The Chef", "Boiling Point"]), ("Disney's 2003 film about a boy turned into a bear", "Brother Bear", ["Brave", "The Fox and the Hound", "Bambi"]),
 ("Alistair MacLean's 1971 Arctic thriller", "Bear Island", ["Ice Station Zebra", "Where Eagles Dare", "The Guns of Navarone"]), ("Chicago's NFL team", "Chicago Bears", ["Chicago Bulls", "Chicago Cubs", "Chicago Fire"]),
 ("The Glasgow suburb on the line of the Antonine Wall", "Bearsden", ["Milngavie", "Bishopbriggs", "Kirkintilloch"]), ("The Wall Street bank that collapsed in 2008, months before Lehman", "Bear Stearns", ["Lehman Brothers", "Merrill Lynch", "Goldman Sachs"]),
 ("The Arctic's top predator", "Polar bear", ["Grizzly bear", "Walrus", "Arctic fox"]), ("The toy named after President Theodore Roosevelt", "Teddy bear", ["Rag doll", "Gonk", "Jack-in-the-box"]),
 ("A tight, friendly squeeze", "Bear hug", ["Group hug", "Headlock", "Full nelson"]), ("The smallest bear of all, from South-East Asia", "Sun bear", ["Moon bear", "Spectacled bear", "Sloth bear"]),
 ("The 1976 comedy about a hopeless Little League baseball team", "The Bad News Bears", ["The Mighty Ducks", "Major League", "The Sandlot"]), ("The Australian animal often wrongly called a bear", "Koala", ["Wombat", "Kangaroo", "Possum"]),
 ("Goldilocks eats their porridge", "The Three Bears", ["The Three Little Pigs", "The Billy Goats Gruff", "The Seven Dwarfs"]), ("The giant brown bears of an island off Alaska", "Kodiak", ["Grizzly", "Kamchatka", "Black"])])

race("which famous 'Lion'?", "General knowledge", "medium", ["lions", "wordplay"], [
 ("Disney's 1994 film about Simba", "The Lion King", ["The Jungle Book", "Bambi", "Tarzan"]), ("The biggest part of something", "The lion's share", ["The wolf's portion", "The eagle's share", "The fox's cut"]),
 ("The barking sea mammal with little outside ears", "Sea lion", ["Seal", "Walrus", "Sea otter"]), ("The Argentine genius of Barcelona and Inter Miami", "Lionel Messi", ["Diego Maradona", "Neymar", "Luis Suárez"]),
 ("The singer of 'Hello' and 'All Night Long'", "Lionel Richie", ["Luther Vandross", "Smokey Robinson", "Barry White"]), ("The rugby team made up of players from Britain and Ireland", "British & Irish Lions", ["Barbarians", "Home Nations XV", "Celtic Warriors"]),
 ("England's women's football team", "The Lionesses", ["The Three Lions", "The Red Roses", "The Vixens"]), ("The character in The Wizard of Oz who wants courage", "The Cowardly Lion", ["The Tin Man", "The Scarecrow", "Toto"]),
 ("The dance performed at Chinese New Year by two people in one costume", "Lion dance", ["Dragon dance", "Fan dance", "Ribbon dance"]), ("Nestlé's chocolate bar that 'roars'", "Lion Bar", ["Yorkie", "Toffee Crisp", "Boost"]),
 ("The yellow weed named from the French for 'lion's tooth'", "Dandelion", ["Daisy", "Buttercup", "Thistle"]), ("Tight Fit's 1982 number one", "The Lion Sleeps Tonight", ["Back to the Sixties", "Fantasy Island", "Pass the Dutchie"]),
 ("Where Daniel was thrown in the Bible", "The lions' den", ["The fiery furnace", "The pit", "The whale"]), ("The American big cat also called a puma or cougar", "Mountain lion", ["Jaguar", "Lynx", "Ocelot"]),
 ("The circus act with a whip and a chair", "Lion tamer", ["Ringmaster", "Strongman", "Knife thrower"]), ("The Give Us a Clue captain famous for tap dancing", "Lionel Blair", ["Una Stubbs", "Michael Aspel", "Bruce Forsyth"]),
 ("C. S. Lewis's first Narnia book", "The Lion, the Witch and the Wardrobe", ["Prince Caspian", "The Magician's Nephew", "The Silver Chair"]), ("Detroit's NFL team", "Detroit Lions", ["Detroit Pistons", "Detroit Tigers", "Detroit Red Wings"]),
 ("The Royal Banner of Scotland, a red lion on gold", "Lion Rampant", ["Saltire", "Lion Passant", "Red Ensign"]), ("The city whose name means 'Lion City'", "Singapore", ["Kuala Lumpur", "Colombo", "Jakarta"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-92.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
