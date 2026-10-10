# Bank session 10 Oct 2026: new Wipeout boards -> bank/wipeout-10.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Women who have won the Wimbledon singles since 1990", "Tennis", "medium", ["Wimbledon", "tennis"],
 ["Martina Navratilova", "Steffi Graf", "Conchita Martínez", "Jana Novotná", "Lindsay Davenport", "Venus Williams", "Serena Williams", "Maria Sharapova", "Amélie Mauresmo", "Petra Kvitová", "Marion Bartoli", "Garbiñe Muguruza", "Angelique Kerber", "Simona Halep", "Ash Barty"],
 ["Monica Seles", "Kim Clijsters", "Justine Henin", "Caroline Wozniacki", "Naomi Osaka"])
board("Seaside resorts on England's east coast", "Britain", "medium", ["seaside", "resorts"],
 ["Scarborough", "Whitby", "Bridlington", "Skegness", "Cleethorpes", "Great Yarmouth", "Cromer", "Southwold", "Clacton-on-Sea", "Felixstowe", "Whitley Bay", "Seaburn", "Saltburn-by-the-Sea", "Filey", "Redcar"],
 ["Blackpool", "Morecambe", "Southport", "Weston-super-Mare", "Llandudno"])
board("Venues used at the London 2012 Olympics", "The Olympics", "hard", ["London 2012", "venues"],
 ["The Olympic Stadium", "The Aquatics Centre", "The Velodrome", "The Copper Box", "Horse Guards Parade", "Greenwich Park", "Eton Dorney", "Lord's", "Wimbledon", "ExCeL", "Hampton Court Palace", "Hyde Park", "Earls Court", "The O2", "Wembley Arena"],
 ["Twickenham", "Crystal Palace", "Alexandra Palace", "The Royal Albert Hall", "Silverstone"])
board("Clubs that have played in the Premier League", "Football", "hard", ["Premier League", "clubs"],
 ["Swindon Town", "Barnsley", "Blackpool", "Oldham Athletic", "Wimbledon", "Bradford City", "Huddersfield Town", "Cardiff City", "Hull City", "Reading", "Portsmouth", "Wigan Athletic", "Burnley", "Luton Town", "Brentford"],
 ["Preston North End", "Millwall", "Bristol City", "Plymouth Argyle", "Rotherham United"])
board("Bands and acts from Merseyside", "Music", "medium", ["Liverpool", "bands"],
 ["The Beatles", "Gerry and the Pacemakers", "Echo & the Bunnymen", "Frankie Goes to Hollywood", "OMD", "The La's", "The Zutons", "Atomic Kitten", "The Coral", "Cilla Black", "Billy Fury", "The Searchers", "Dead or Alive", "The Farm", "The Lightning Seeds"],
 ["Oasis", "The Smiths", "Joy Division", "Take That", "The Stone Roses"])
board("Words that contain all five vowels", "Words and language", "hard", ["words", "vowels"],
 ["Education", "Sequoia", "Facetious", "Abstemious", "Dialogue", "Favourite", "Behaviour", "Authorise", "Regulation", "Simultaneous", "Precarious", "Automobile", "Miscellaneous", "Cauliflower", "Unquestionably"],
 ["Gracious", "Mountain", "Question", "Beautiful", "Delicious"])
board("Welsh singers", "Music", "medium", ["Wales", "singers"],
 ["Tom Jones", "Shirley Bassey", "Katherine Jenkins", "Duffy", "Bonnie Tyler", "Charlotte Church", "Aled Jones", "Cerys Matthews", "Shakin' Stevens", "Mary Hopkin", "Kelly Jones", "Bryn Terfel", "Marina Diamandis", "James Dean Bradfield", "Cate Le Bon"],
 ["Lulu", "Sheena Easton", "Enya", "Sinéad O'Connor", "Annie Lennox"])
board("Members of the Commonwealth", "World geography", "medium", ["Commonwealth", "countries"],
 ["The United Kingdom", "Canada", "Australia", "New Zealand", "India", "Pakistan", "South Africa", "Kenya", "Nigeria", "Jamaica", "Malta", "Cyprus", "Singapore", "Rwanda", "Mozambique"],
 ["Ireland", "Zimbabwe", "The USA", "Egypt", "Myanmar"])
board("Harry Potter characters who die in the books", "Harry Potter", "medium", ["Harry Potter", "characters"],
 ["Albus Dumbledore", "Severus Snape", "Sirius Black", "Dobby", "Hedwig", "Fred Weasley", "Remus Lupin", "Nymphadora Tonks", "Cedric Diggory", "Mad-Eye Moody", "Lord Voldemort", "Bellatrix Lestrange", "Colin Creevey", "Quirinus Quirrell", "Peter Pettigrew"],
 ["Neville Longbottom", "Luna Lovegood", "Rubeus Hagrid", "George Weasley", "Draco Malfoy"])
board("Men who have captained England in a Test match", "Cricket", "hard", ["England", "cricket", "captains"],
 ["Michael Vaughan", "Andrew Strauss", "Alastair Cook", "Joe Root", "Ben Stokes", "Nasser Hussain", "Michael Atherton", "Graham Gooch", "Mike Gatting", "David Gower", "Ian Botham", "Mike Brearley", "Kevin Pietersen", "Andrew Flintoff", "Alec Stewart"],
 ["Graeme Swann", "Jimmy Anderson", "Stuart Broad", "Jonathan Trott", "Matt Prior"])
board("Characters in The Wizard of Oz film (watch for impostors)", "Film", "medium", ["The Wizard of Oz", "films"],
 ["Dorothy", "Toto", "The Scarecrow", "The Tin Man", "The Cowardly Lion", "Glinda", "The Wicked Witch of the West", "The Wizard", "The Munchkins", "The Wicked Witch of the East", "Aunt Em", "Uncle Henry", "Miss Gulch", "Professor Marvel", "The Winged Monkeys"],
 ["The Tin Soldier", "The Cowardly Bear", "The Good Witch of the West", "Professor Wonder", "Aunt Bea"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-10.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'boards written')
