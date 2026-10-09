# Bank session 9 Oct 2026 (fourth pass): 2 more Put in Order questions for 12 broad topics that had 5 live.
# Items are listed in the right order; wording is specific so it can't clash with another topic's.
# Writes bank/topics/<slug>__o5.json; import each with FILE=<slug>__o5 TOPICS=<slug> LQ_PASSWORD=… node tools/import-bank.mjs topics
import json, os
OUT = {}
def o(slug, diff, text, *items):
    assert 4 <= len(items) <= 5 and len(set(items)) == len(items), text
    OUT.setdefault(slug, []).append({"type": "order", "text": text, "items": list(items), "difficulty": diff})

o("christmas-tv", "medium", "Put these festive animations in the order they were first shown, earliest first", "The Snowman", "Father Christmas", "The Gruffalo", "Room on the Broom", "Stick Man")
o("christmas-tv", "medium", "Put these Christmas TV adverts in the order they first aired, earliest first", "Coca-Cola's 'Holidays Are Coming' lorries", "John Lewis's 'The Long Wait'", "John Lewis's 'Monty the Penguin'", "Aldi's 'Kevin the Carrot'")

o("football", "medium", "Put these clubs in the order they first won the Premier League, earliest first", "Manchester United", "Blackburn Rovers", "Arsenal", "Chelsea", "Leicester City")
o("football", "medium", "Put these nations in the order they first won the World Cup, earliest first", "Uruguay", "Italy", "West Germany", "Brazil", "England")

o("north-east-england", "medium", "Put these North East landmarks in the order they were built, earliest first", "Durham Cathedral", "Newcastle's Castle Keep", "Grey's Monument", "The Tyne Bridge", "The Angel of the North")
o("north-east-england", "medium", "Put these North East football grounds in order of capacity, largest first", "St James' Park", "Stadium of Light", "Riverside Stadium", "Victoria Park, Hartlepool")

o("harry-potter", "medium", "Put these Defence Against the Dark Arts teachers in the order Harry had them, earliest first", "Quirrell", "Lockhart", "Lupin", "Umbridge", "Snape")
o("harry-potter", "medium", "Put these Weasley children in age order, eldest first", "Bill", "Charlie", "Percy", "Ron", "Ginny")

o("james-bond", "medium", "Put these Bond theme songs in release order, earliest first", "Goldfinger", "Live and Let Die", "Nobody Does It Better", "A View to a Kill", "Skyfall")
o("james-bond", "hard", "Put these Bond villains in the order of their film, earliest first", "Francisco Scaramanga", "Max Zorin", "Alec Trevelyan", "Le Chiffre", "Raoul Silva")

o("london", "medium", "Put these London landmarks in order of height, tallest first", "The Shard", "One Canada Square", "The BT Tower", "The London Eye", "Big Ben's Elizabeth Tower")
o("london", "medium", "Put these Thames bridges in order going downstream, west to east", "Westminster Bridge", "Waterloo Bridge", "Blackfriars Bridge", "London Bridge", "Tower Bridge")

o("musicals", "medium", "Put these Andrew Lloyd Webber musicals in the order they opened, earliest first", "Jesus Christ Superstar", "Evita", "Cats", "The Phantom of the Opera", "Sunset Boulevard")
o("musicals", "easy", "Put these film musicals in release order, earliest first", "The Wizard of Oz", "The Sound of Music", "Grease", "Mamma Mia!", "The Greatest Showman")

o("soaps", "medium", "Put these Australian soaps in order of their first episode, earliest first", "Prisoner: Cell Block H", "Sons and Daughters", "Neighbours", "Home and Away")
o("soaps", "medium", "Put these British soaps in the order they ended, earliest first", "Eldorado", "Brookside", "Family Affairs", "Doctors")

o("royal-family", "easy", "Put these royal children in order of birth, eldest first", "Prince George", "Princess Charlotte", "Prince Louis", "Archie", "Lilibet")
o("royal-family", "medium", "Put these Westminster Abbey royal weddings in order, earliest first", "Elizabeth and Philip", "Princess Margaret and Antony Armstrong-Jones", "Princess Anne and Mark Phillips", "William and Kate")

o("tudors", "medium", "Put these Tudor events in order, earliest first", "The Battle of Bosworth", "Henry VIII becomes king", "The break with Rome", "The Dissolution of the Monasteries begins", "The Spanish Armada")
o("tudors", "hard", "Put these Tudor voyages in order, earliest first", "John Cabot reaches North America", "Martin Frobisher sails for the Northwest Passage", "Francis Drake sets off round the world", "Walter Raleigh's first Roanoke expedition")

o("world-wars", "easy", "Put these key moments of the Second World War in order, earliest first", "Germany invades Poland", "The Dunkirk evacuation", "Pearl Harbor", "D-Day", "VE Day")
o("world-wars", "medium", "Put these Western Front and Gallipoli battles in order, earliest first", "Mons", "Gallipoli", "The Somme", "Passchendaele", "Amiens")

o("olympics", "medium", "Put these Summer Olympic host cities in order, from 1948 on", "London", "Rome", "Tokyo", "Mexico City", "Munich")
o("olympics", "medium", "Put these British Olympians in the order they won their first gold, earliest first", "Daley Thompson", "Steve Redgrave", "Sally Gunnell", "Jason Kenny", "Max Whitlock")

here = os.path.dirname(os.path.abspath(__file__))
for slug, items in OUT.items():
    json.dump(items, open(os.path.join(here, '..', 'topics', slug + '__o5.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(sum(map(len, OUT.values())), 'orders in', len(OUT), 'topics:', ' '.join(OUT))
