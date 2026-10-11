# Bank session 11 Oct 2026: 3 more general races -> bank/race-202.json (Gavin & Stacey, EastEnders and Simpsons words). 20 rows each, target 10; wrong options are
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

race("what's this Gavin & Stacey word?", "TV", "easy", ["Gavin & Stacey", "sitcoms", "words"], [
 ("Stacey's Welsh seaside home", "Barry Island", ["Caldey Island", "Porthcawl", "Tenby"]),
 ("Gavin's Essex home town", "Billericay", ["Basildon", "Chelmsford", "Romford"]),
 ("Nessa's famous greeting", "Oh, what's occurring?", ["Alright, my lover?", "Wotcha!", "How you doin'?"]),
 ("Stacey's best friend, played by Ruth Jones", "Nessa", ["Dawn", "Cheryl", "Debbie"]),
 ("Gavin's best mate, played by James Corden", "Smithy", ["Smudger", "Jonesy", "Robbo"]),
 ("Stacey's uncle, never over the fishing trip", "Uncle Bryn", ["Uncle Albert", "Uncle Fester", "Uncle Monty"]),
 ("Nessa's on-off man with the coach firm", "Dave Coaches", ["Dave Courtney", "Dave Gorman", "Dave Benson Phillips"]),
 ("Gavin's dramatic mum", "Pam", ["Pat", "Peggy", "Pauline"]),
 ("Gavin's laid-back dad", "Mick", ["Mike", "Mack", "Mitch"]),
 ("Stacey's mum, always offering to make an omelette", "Gwen", ["Gwyneth", "Glenys", "Gloria"]),
 ("The foul-mouthed neighbour", "Doris", ["Dora", "Dolly", "Edna"]),
 ("Nessa and Smithy's son", "Neil the Baby", ["Damien", "Dennis", "Darren"]),
 ("Welsh slang for something good", "Tidy", ["Cushty", "Mint", "Peachy"]),
 ("What Nessa does to Smithy at the end of the 2019 special", "Proposal", ["Divorce", "Resignation", "Confession"]),
 ("The co-writer who played Nessa", "Ruth Jones", ["Ruth Langsford", "Ruth Madoc", "Ruth Wilson"]),
 ("The co-writer who played Smithy", "James Corden", ["James Acaster", "James May", "Jimmy Carr"]),
 ("The actor who played Uncle Bryn", "Rob Brydon", ["Rob Beckett", "Rhod Gilbert", "Michael Sheen"]),
 ("Gavin's county", "Essex", ["Kent", "Surrey", "Sussex"]),
 ("Stacey's brother and Smithy's love rival", "Jason", ["Jamie", "Justin", "Josh"]),
 ("Bryn's mysterious incident nobody talks about", "The fishing trip", ["The camping trip", "The coach trip", "The stag do"])])

race("what's this EastEnders word?", "TV", "easy", ["EastEnders", "soaps", "words"], [
 ("The pub on the Square", "Queen Vic", ["Rovers Return", "Woolpack", "Nag's Head"]),
 ("Where most of it happens", "Albert Square", ["Trafalgar Square", "Brookside Close", "Leicester Square"]),
 ("The fictional East End borough", "Walford", ["Weatherfield", "Emmerdale", "Holby"]),
 ("The drumbeats at the end of every episode", "Duff duff", ["Dum dum", "Tick tock", "Ding dong"]),
 ("Phil and Grant", "Mitchell brothers", ["Kray twins", "Beale brothers", "Slater brothers"]),
 ("Phil's garage under the railway", "The Arches", ["The Vaults", "The Docks", "The Yard"]),
 ("Where Dot and Pauline gossiped over the washing", "Launderette", ["Library", "Bingo hall", "Bakery"]),
 ("The chain-smoking busybody played by June Brown", "Dot Cotton", ["Ethel Skinner", "Pat Butcher", "Pauline Fowler"]),
 ("The landlord who handed Angie divorce papers at Christmas", "Den Watts", ["Frank Butcher", "Alfie Moon", "Grant Mitchell"]),
 ("The landlady who yelled 'Get outta my pub!'", "Peggy Mitchell", ["Pat Butcher", "Bianca Jackson", "Pauline Fowler"]),
 ("The café owner and Walford's great survivor", "Ian Beale", ["Mark Fowler", "Ricky Butcher", "Martin Fowler"]),
 ("Played by Jessie Wallace", "Kat Slater", ["Stacey Slater", "Janine Butcher", "Tiffany Mitchell"]),
 ("The name Ricky always yelled", "Bianca!", ["Sharon!", "Kathy!", "Janine!"]),
 ("Den and Angie's adopted daughter, played by Letitia Dean", "Sharon", ["Sam", "Stacey", "Sonia"]),
 ("The market street", "Bridge Street", ["Coronation Street", "Carnaby Street", "Electric Avenue"]),
 ("The Tube station", "Walford East", ["Walford West", "Albert Gate", "Whitechapel"]),
 ("Den and Angie's poodle", "Roly", ["Rover", "Rex", "Rufus"]),
 ("Who was shot in the 2001 'Who Shot ...?' whodunnit", "Phil", ["Den", "Ian", "Alfie"]),
 ("The channel it's on", "BBC One", ["ITV", "Channel 4", "Sky One"]),
 ("The year it began", "1985", ["1975", "1980", "1995"])])

race("what's this Simpsons word?", "TV", "medium", ["The Simpsons", "cartoons", "words"], [
 ("The family's home town", "Springfield", ["Shelbyville", "Quahog", "South Park"]),
 ("Homer's favourite beer", "Duff", ["Buzz Cola", "Krusty", "Fudd"]),
 ("The bar where Homer drinks", "Moe's Tavern", ["Cheers", "The Drunken Clam", "Paddy's Pub"]),
 ("Apu's shop", "Kwik-E-Mart", ["Leftorium", "Costington's", "Try-N-Save"]),
 ("The fast-food chain named after a clown", "Krusty Burger", ["Pizza Planet", "Bob's Burgers", "Big Kahuna Burger"]),
 ("The giant statue holding a doughnut", "Lard Lad", ["Bob's Big Boy", "Colonel Sanders", "Ronald McDonald"]),
 ("The Simpsons' version of a slushie", "Squishee", ["Slurpee", "Frosty", "Icee"]),
 ("Homer's cry of annoyance", "D'oh!", ["Ugh!", "Drat!", "Blast!"]),
 ("Bart's cheeky catchphrase", "Eat my shorts", ["Hasta la vista", "Yabba dabba doo", "Holy cow"]),
 ("Mr Burns's sinister one-word catchphrase", "Excellent", ["Marvellous", "Splendid", "Delightful"]),
 ("Bart's cry of surprise", "Ay, caramba!", ["Mamma mia!", "Sacré bleu!", "Holy moly!"]),
 ("Flanders' happy reply", "Okily dokily", ["Hunky dory", "Easy peasy", "Okey cokey"]),
 ("The violent cartoon cat and mouse the kids watch", "Itchy & Scratchy", ["Tom and Jerry", "Pinky and the Brain", "Ren and Stimpy"]),
 ("The yearly Halloween episodes", "Treehouse of Horror", ["House of Horrors", "Haunted Treehouse", "Fright Night"]),
 ("The family's street", "Evergreen Terrace", ["Wisteria Lane", "Ramsay Street", "Elm Street"]),
 ("Their house number", "742", ["221", "4", "1313"]),
 ("The show's creator", "Matt Groening", ["Seth MacFarlane", "Mike Judge", "Trey Parker"]),
 ("The transport system a conman sells the town", "Monorail", ["Funicular", "Tramway", "Hyperloop"]),
 ("Where Homer works", "Nuclear power plant", ["Coal mine", "Steelworks", "Brewery"]),
 ("Lisa's instrument", "Saxophone", ["Clarinet", "Trumpet", "Violin"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-202.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
