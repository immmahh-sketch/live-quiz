# Bank session 10 Oct 2026: 4 more general races -> bank/race-35.json. 20 rows each, target 10; wrong options are
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

race("which country is this famous beach in?", "Travel", "medium", ["beaches", "countries"], [
 ("Bondi", "Australia", ["Fiji", "Samoa", "Chile"]), ("Copacabana", "Brazil", ["Argentina", "Uruguay", "Colombia"]),
 ("Waikiki", "the USA", ["Fiji", "Samoa", "Tonga"]), ("Maya Bay", "Thailand", ["Vietnam", "Malaysia", "the Philippines"]),
 ("Grace Bay", "Turks and Caicos", ["Jamaica", "Barbados", "Cuba"]), ("Anse Source d'Argent", "the Seychelles", ["Mauritius", "the Maldives", "Madagascar"]),
 ("Navagio (Shipwreck Beach)", "Greece", ["Cyprus", "Croatia", "Malta"]), ("Praia da Rocha", "Portugal", ["Spain", "Cape Verde", "Croatia"]),
 ("Playa del Carmen", "Mexico", ["Cuba", "the Dominican Republic", "Costa Rica"]), ("The Skeleton Coast", "Namibia", ["Angola", "Mozambique", "Morocco"]),
 ("Boulders Beach and its penguins", "South Africa", ["Mozambique", "Kenya", "Tanzania"]), ("Pink Sands Beach", "the Bahamas", ["Bermuda", "Barbados", "Jamaica"]),
 ("Reynisfjara's black sand", "Iceland", ["Norway", "the Faroe Islands", "Greenland"]), ("Kuta", "Indonesia", ["the Philippines", "Malaysia", "Vietnam"]),
 ("Durdle Door", "England", ["Wales", "Ireland", "Scotland"]), ("Omaha Beach", "France", ["Belgium", "the Netherlands", "Spain"]),
 ("Mondello", "Italy", ["Spain", "Malta", "Croatia"]), ("Juhu", "India", ["Sri Lanka", "Pakistan", "the Maldives"]),
 ("Cox's Bazar", "Bangladesh", ["Myanmar", "Sri Lanka", "Pakistan"]), ("Piha", "New Zealand", ["Fiji", "Samoa", "Chile"])])

race("which country is this famous square in?", "Travel", "medium", ["squares", "landmarks", "countries"], [
 ("Red Square", "Russia", ["Belarus", "Poland", "Romania"]), ("Tiananmen Square", "China", ["Taiwan", "Mongolia", "Japan"]),
 ("Times Square", "the USA", ["Canada", "Ireland", "Japan"]), ("Trafalgar Square", "the United Kingdom", ["Ireland", "Canada", "Malta"]),
 ("St Mark's Square", "Italy", ["Croatia", "Malta", "Slovenia"]), ("Plaza Mayor (Madrid)", "Spain", ["Colombia", "Peru", "Chile"]),
 ("The Grand-Place", "Belgium", ["France", "Luxembourg", "Switzerland"]), ("Wenceslas Square", "Czechia", ["Slovakia", "Poland", "Hungary"]),
 ("Jemaa el-Fnaa", "Morocco", ["Tunisia", "Algeria", "Lebanon"]), ("Naqsh-e Jahan Square", "Iran", ["Iraq", "Afghanistan", "Pakistan"]),
 ("The Zócalo", "Mexico", ["Colombia", "Peru", "Cuba"]), ("Dam Square", "the Netherlands", ["Denmark", "Luxembourg", "Sweden"]),
 ("Syntagma Square", "Greece", ["Cyprus", "Bulgaria", "Malta"]), ("Taksim Square", "Turkey", ["Cyprus", "Lebanon", "Bulgaria"]),
 ("Tahrir Square (the one in its capital)", "Egypt", ["Lebanon", "Jordan", "Tunisia"]), ("Plaza de Mayo", "Argentina", ["Uruguay", "Chile", "Colombia"]),
 ("Praça do Comércio", "Portugal", ["Brazil", "Angola", "Cape Verde"]), ("Federation Square", "Australia", ["New Zealand", "Canada", "Ireland"]),
 ("Maidan Nezalezhnosti", "Ukraine", ["Belarus", "Poland", "Moldova"]), ("Marienplatz", "Germany", ["Austria", "Switzerland", "Denmark"])])

race("which animal has this scientific name?", "Animals", "hard", ["animals", "Latin names"], [
 ("Panthera leo", "Lion", ["Leopard", "Jaguar", "Cheetah"]), ("Canis lupus", "Wolf", ["Jackal", "Coyote", "Hyena"]),
 ("Felis catus", "Cat", ["Lynx", "Puma", "Ocelot"]), ("Ursus maritimus", "Polar bear", ["Brown bear", "Black bear", "Walrus"]),
 ("Equus caballus", "Horse", ["Donkey", "Zebra", "Mule"]), ("Sus scrofa", "Wild boar", ["Warthog", "Hippo", "Peccary"]),
 ("Loxodonta africana", "African elephant", ["Asian elephant", "Rhino", "Mammoth"]), ("Vulpes vulpes", "Red fox", ["Arctic fox", "Coyote", "Stoat"]),
 ("Meles meles", "Badger", ["Mole", "Stoat", "Weasel"]), ("Erinaceus europaeus", "Hedgehog", ["Porcupine", "Shrew", "Mole"]),
 ("Lutra lutra", "Otter", ["Mink", "Beaver", "Seal"]), ("Ailuropoda melanoleuca", "Giant panda", ["Red panda", "Koala", "Sun bear"]),
 ("Struthio camelus", "Ostrich", ["Emu", "Rhea", "Camel"]), ("Pan troglodytes", "Chimpanzee", ["Bonobo", "Gorilla", "Orangutan"]),
 ("Panthera tigris", "Tiger", ["Leopard", "Jaguar", "Snow leopard"]), ("Apis mellifera", "Honeybee", ["Wasp", "Hornet", "Bumblebee"]),
 ("Oryctolagus cuniculus", "Rabbit", ["Hare", "Guinea pig", "Squirrel"]), ("Erithacus rubecula", "Robin", ["Wren", "Blackbird", "Thrush"]),
 ("Bufo bufo", "Toad", ["Frog", "Newt", "Lizard"]), ("Salmo salar", "Salmon", ["Trout", "Cod", "Pike"])])

race("who wrote this poem?", "Books", "hard", ["poems", "poets"], [
 ("Daffodils ('I wandered lonely as a cloud')", "William Wordsworth", ["Lord Byron", "John Clare", "Thomas Hardy"]),
 ("The Raven", "Edgar Allan Poe", ["Walt Whitman", "Emily Dickinson", "Henry Longfellow"]),
 ("If—", "Rudyard Kipling", ["Henry Newbolt", "John Betjeman", "Thomas Hardy"]),
 ("The Road Not Taken", "Robert Frost", ["Walt Whitman", "Henry Longfellow", "Emily Dickinson"]),
 ("Do Not Go Gentle into That Good Night", "Dylan Thomas", ["Seamus Heaney", "Ted Hughes", "R. S. Thomas"]),
 ("Ozymandias", "Percy Bysshe Shelley", ["Lord Byron", "Alexander Pope", "John Milton"]),
 ("The Charge of the Light Brigade", "Alfred, Lord Tennyson", ["Robert Browning", "Matthew Arnold", "Thomas Hardy"]),
 ("Jabberwocky", "Lewis Carroll", ["Hilaire Belloc", "Spike Milligan", "Ogden Nash"]),
 ("The Owl and the Pussy-cat", "Edward Lear", ["Hilaire Belloc", "Spike Milligan", "A. A. Milne"]),
 ("Dulce et Decorum Est", "Wilfred Owen", ["Siegfried Sassoon", "Isaac Rosenberg", "Edward Thomas"]),
 ("The Waste Land", "T. S. Eliot", ["Ezra Pound", "W. B. Yeats", "Ted Hughes"]),
 ("Ode to a Nightingale", "John Keats", ["Lord Byron", "John Clare", "Christina Rossetti"]),
 ("The Tyger", "William Blake", ["John Milton", "Alexander Pope", "Lord Byron"]),
 ("Funeral Blues ('Stop all the clocks')", "W. H. Auden", ["Louis MacNeice", "Stephen Spender", "John Betjeman"]),
 ("Still I Rise", "Maya Angelou", ["Langston Hughes", "Alice Walker", "Toni Morrison"]),
 ("Not Waving but Drowning", "Stevie Smith", ["Sylvia Plath", "Christina Rossetti", "Carol Ann Duffy"]),
 ("Kubla Khan", "Samuel Taylor Coleridge", ["Lord Byron", "Robert Southey", "John Clare"]),
 ("To a Mouse", "Robert Burns", ["Walter Scott", "James Hogg", "Hugh MacDiarmid"]),
 ("This Be the Verse", "Philip Larkin", ["Ted Hughes", "John Betjeman", "Kingsley Amis"]),
 ("The Soldier ('If I should die, think only this of me')", "Rupert Brooke", ["Siegfried Sassoon", "Edward Thomas", "Isaac Rosenberg"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-35.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
